(() => {
  "use strict";

  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const NETS = { tiktok: "TikTok", instagram: "Instagram", youtube: "YouTube" };
  const NET_SHORT = { tiktok: "TT", instagram: "IG", youtube: "YT" };
  const PARTNER = { pub: "Pub", "produits-offerts": "Produits offerts", invitation: "Invitation" };
  const CAT_EMOJI = { tendances: "🔥", "fast-food": "🍔", "patisserie-glacier": "🧁", "street-food-etranger": "🌍" };
  const PAGE = 24;
  const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;

  const state = { lieux: [], cats: {}, q: "", cat: "", ville: "", type: "", note: 0, rated: false, sort: "note", view: "home", shown: PAGE };
  let map = null, markers = null;

  // ───────── helpers ─────────
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const norm = (s) => String(s ?? "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
  const fmtNote = (n) => (Number.isInteger(n) ? String(n) : n.toFixed(1).replace(".", ","));
  const fmtPrix = (p) => (p == null || p === "" ? "" : typeof p === "number" ? p.toFixed(2).replace(".", ",").replace(",00", "") + " €" : esc(p));
  const fmtDate = (d, short) => (d ? new Date(d + "T12:00:00").toLocaleDateString("fr-FR", short ? { day: "numeric", month: "short", year: "numeric" } : { day: "numeric", month: "long", year: "numeric" }) : "");
  const color = (n) => (n == null ? "var(--none)" : n >= 7.5 ? "var(--good)" : n >= 5 ? "var(--mid)" : "var(--bad)");
  const plural = (n, w) => `${n} ${w}${n > 1 ? "s" : ""}`;
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (_) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (_) { /* stockage indisponible */ } },
  };

  function emojiFor(l) {
    const t = norm([l.specialite, l.nom].join(" "));
    const table = [
      [/burger|smash/, "🍔"], [/poulet|chicken|crousty|tender|wing|fry|frit/, "🍗"], [/tacos/, "🌮"],
      [/pizza|panuozzo|panzerot|italien/, "🍕"], [/kebab|grill|libanais|turc|shawarma/, "🥙"], [/sushi|asiat|wok|thai|japon|coreen|nouille|ramen/, "🍜"],
      [/glace|gelato|sorbet/, "🍦"], [/donut|doughnut/, "🍩"], [/cookie/, "🍪"], [/patiss|boulang|viennois|croissant|gateau|cake|flan/, "🥐"],
      [/afric|ivoir|attieke|poulet braise/, "🍲"], [/crepe/, "🥞"], [/cafe|coffee|brunch/, "☕"],
    ];
    for (const [re, e] of table) if (re.test(t)) return e;
    return CAT_EMOJI[l.categorie] || "🍽️";
  }

  function gradientFor(id) {
    const g = [["#1F5EFF", "#6CC6FF"], ["#3B28CC", "#7C9CFF"], ["#0EA5E9", "#22D3EE"], ["#2563EB", "#A78BFA"], ["#0B3BFF", "#38BDF8"], ["#1D4ED8", "#60A5FA"]];
    let h = 0;
    for (const c of id) h = (h * 31 + c.charCodeAt(0)) >>> 0;
    const [a, b] = g[h % g.length];
    return `linear-gradient(135deg, ${a}, ${b})`;
  }

  // Restaurant logo on a white tile; falls back to an emoji on a blue gradient when there is no logo.
  function thumbHTML(l) {
    const nets = `<span class="thumb__net">${l.nets.map((n) => `<i title="${NETS[n]}">${NET_SHORT[n]}</i>`).join("")}</span>`;
    if (l.logo) {
      return `<span class="thumb thumb--logo" data-emoji="${l.emoji}" style="--g:${gradientFor(l.id)}"><span class="logo-tile"><img src="${esc(l.logo)}" alt="Logo ${esc(l.nom)}" loading="lazy" decoding="async" onerror="const t=this.closest('.thumb');t.classList.replace('thumb--logo','thumb--emoji');t.style.background=t.style.getPropertyValue('--g');this.parentNode.replaceWith(t.dataset.emoji)"></span>${nets}</span>`;
    }
    return `<span class="thumb thumb--emoji" style="background:${gradientFor(l.id)}" aria-hidden="true">${l.emoji}${nets}</span>`;
  }

  function ringHTML(n, size = "") {
    if (n == null) return `<span class="ring ring--none ${size}" aria-label="Note à venir"><svg viewBox="0 0 36 36"><circle class="track" cx="18" cy="18" r="15.5"/></svg><b>Note<br>à venir</b></span>`;
    return `<span class="ring ${size}" style="--p:${n * 10};--c:${color(n)}" aria-label="${fmtNote(n)} sur 10"><svg viewBox="0 0 36 36"><circle class="track" cx="18" cy="18" r="15.5"/><circle class="bar" cx="18" cy="18" r="15.5" pathLength="100"/></svg><b>${fmtNote(n)}</b></span>`;
  }

  const pillNote = (n) => (n == null ? `<span class="pillnote pillnote--none">—</span>` : `<span class="pillnote" style="--c:${color(n)}">${fmtNote(n)}</span>`);

  // A place's score is the average of its rated dishes; a dish tested twice counts with its latest score.
  function enrich(lieu) {
    const visites = [...(lieu.visites || [])].sort((a, b) => (b.date || "").localeCompare(a.date || ""));
    const latest = new Map();
    for (const v of visites) for (const p of v.plats || []) {
      if (typeof p.note === "number" && !latest.has(norm(p.nom))) latest.set(norm(p.nom), { ...p, date: v.date });
    }
    const rated = [...latest.values()];
    // Without any scored dish, fall back to the overall scores Amed gave in his videos.
    const globales = visites.map((v) => v.note_globale).filter((n) => typeof n === "number");
    const pool = rated.length ? rated.map((p) => p.note) : globales;
    const note = pool.length ? Math.round((pool.reduce((s, n) => s + n, 0) / pool.length) * 10) / 10 : null;
    const nets = [...new Set(visites.flatMap((v) => (v.videos || []).map((x) => x.platform)))].filter((n) => NETS[n]);
    const l = { ...lieu, visites, note, rated, nets, derniere: visites[0]?.date || "" };
    l.emoji = emojiFor(l);
    l.haystack = norm([l.nom, l.ville, l.specialite, l.adresse, ...visites.flatMap((v) => [v.titre, ...(v.plats || []).map((p) => p.nom)])].join(" "));
    return l;
  }

  // ───────── reveal + rings ─────────
  const io = "IntersectionObserver" in window && !reduceMotion
    ? new IntersectionObserver((entries) => {
      for (const e of entries) if (e.isIntersecting) { e.target.classList.add("is-in"); $$(".ring", e.target).forEach((r) => r.classList.add("is-in")); io.unobserve(e.target); }
    }, { rootMargin: "0px 0px -6% 0px" })
    : null;

  function reveal(root) {
    $$(".reveal:not(.is-in)", root).forEach((el, i) => {
      el.style.setProperty("--d", `${Math.min(i, 8) * 45}ms`);
      if (io) io.observe(el); else { el.classList.add("is-in"); $$(".ring", el).forEach((r) => r.classList.add("is-in")); }
    });
    $$(".ring:not(.is-in)", root).forEach((r) => { if (!r.closest(".reveal")) requestAnimationFrame(() => r.classList.add("is-in")); });
  }

  function countUp(el, to) {
    if (reduceMotion || to < 2 || document.hidden) { el.textContent = to; return; }
    const t0 = performance.now(), dur = 1100;
    const step = (t) => {
      const k = Math.min(1, (t - t0) / dur);
      el.textContent = Math.round(to * (1 - Math.pow(1 - k, 3)));
      if (k < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }

  // ───────── load ─────────
  async function load() {
    $("#cards").innerHTML = Array.from({ length: 4 }, () => `<li class="skeleton" style="height:98px"></li>`).join("");
    $("#latest").innerHTML = Array.from({ length: 3 }, () => `<div class="skeleton" style="height:240px"></div>`).join("");
    try {
      const res = await fetch("data/guide.json", { cache: "no-cache" });
      if (!res.ok) throw new Error(res.status);
      const data = await res.json();
      state.cats = data.meta?.categories || {};
      state.lieux = (data.lieux || []).map(enrich);
      $("#maj").textContent = data.meta?.maj ? `Dernière mise à jour : ${fmtDate(data.meta.maj)}.` : "";
    } catch (e) {
      $("#cards").innerHTML = "";
      $("#latest").innerHTML = "";
      $("#count").textContent = "Impossible de charger le guide pour le moment. Réessaie dans un instant.";
      return;
    }
    renderStats();
    renderCats();
    renderVilles();
    readHash();
    render();
    renderTop();
  }

  function renderStats() {
    const plats = state.lieux.reduce((s, l) => s + l.visites.reduce((t, v) => t + (v.plats || []).length, 0), 0);
    const videos = state.lieux.reduce((s, l) => s + l.visites.reduce((t, v) => t + (v.videos || []).length, 0), 0);
    $("#stats").innerHTML = [[state.lieux.length, "adresses"], [plats, "plats goûtés"], [videos, "vidéos"]]
      .map(([n, l]) => `<li><b data-n="${n}">0</b><span>${l}</span></li>`).join("");
    $$("#stats b").forEach((b) => countUp(b, Number(b.dataset.n)));
  }

  function renderCats() {
    const keys = Object.keys(state.cats).filter((k) => state.lieux.some((l) => l.categorie === k));
    const tendances = state.lieux.some((l) => l.tendance) ? [["tendances", "Tendances", "🔥"]] : [];
    const all = [["", "Tout", "✨"], ...tendances, ...keys.map((k) => [k, state.cats[k], CAT_EMOJI[k] || "🍽️"])];
    $("#cats").innerHTML = all.map(([k, label, e]) => `<button class="pill" role="tab" data-cat="${esc(k)}" aria-selected="${state.cat === k}"><span aria-hidden="true">${e}</span>${esc(label)}</button>`).join("");
    $("#cats").hidden = keys.length < 2;
  }

  function renderVilles() {
    const counts = new Map();
    for (const l of state.lieux) if (l.ville) counts.set(l.ville, (counts.get(l.ville) || 0) + 1);
    const villes = [...counts].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0], "fr"));
    $("#f-ville").innerHTML = [`<button class="chip-btn${state.ville ? "" : " is-on"}" data-v="">Toutes</button>`, ...villes.map(([v, n]) => `<button class="chip-btn${state.ville === v ? " is-on" : ""}" data-v="${esc(v)}">${esc(v)} <small>${n}</small></button>`)].join("");
  }

  // ───────── filtering ─────────
  function filtered({ ignoreCat = false } = {}) {
    const words = norm(state.q).trim().split(/\s+/).filter(Boolean);
    const list = state.lieux.filter((l) =>
      (!words.length || words.every((w) => l.haystack.includes(w))) &&
      (ignoreCat || !state.cat || (state.cat === "tendances" ? !!l.tendance : l.categorie === state.cat)) &&
      (!state.ville || l.ville === state.ville) &&
      (!state.type || l.type === state.type) &&
      (!state.note || (l.note != null && l.note >= state.note)) &&
      (!state.rated || l.note != null)
    );
    const byNote = (a, b) => (b.note ?? -1) - (a.note ?? -1) || b.derniere.localeCompare(a.derniere);
    const sorters = { note: byNote, recent: (a, b) => b.derniere.localeCompare(a.derniere), nom: (a, b) => a.nom.localeCompare(b.nom, "fr") };
    return list.sort(sorters[state.sort] || byNote);
  }

  const activeFilters = () => [state.ville, state.type, state.note, state.rated].filter(Boolean).length;

  // ───────── home ─────────
  function slideHTML(l, v) {
    const sub = [v.titre, fmtDate(v.date, true)].filter(Boolean).join(" · ");
    return `<button class="slide reveal" data-id="${esc(l.id)}">
      ${thumbHTML(l)}
      ${ringHTML(l.note, "ring--sm")}
      <span class="slide__body"><span class="slide__name">${esc(l.nom)}</span><span class="slide__meta">${esc(sub)}</span></span>
    </button>`;
  }

  function hotHTML(l) {
    return `<button class="slide slide--hot reveal" data-id="${esc(l.id)}">
      ${thumbHTML(l)}
      ${ringHTML(l.note, "ring--sm")}
      <span class="slide__body"><span class="slide__name">${esc(l.nom)}</span><span class="slide__meta">🔥 ${esc(l.tendance)}</span></span>
    </button>`;
  }

  function cardHTML(l, i) {
    const meta = [l.specialite, l.type === "chaine" ? "Chaîne" : l.ville].filter(Boolean).join(" · ") || state.cats[l.categorie] || "";
    const tags = [];
    if (state.sort === "note" && l.note != null && i < 3) tags.push(`<span class="tag tag--rank">#${i + 1}</span>`);
    if (l.visites.length > 1) tags.push(`<span class="tag">${plural(l.visites.length, "visite")}</span>`);
    if (l.derniere) tags.push(`<span class="tag">${fmtDate(l.derniere, true)}</span>`);
    if (l.visites.some((v) => v.partenariat)) tags.push(`<span class="tag tag--gift"><svg><use href="#i-gift"/></svg>Offert</span>`);
    if (l.tendance) tags.unshift(`<span class="tag tag--hot">🔥 Tendance</span>`);
    if (l.statut === "ferme-definitivement") tags.unshift(`<span class="tag tag--closed">Fermé</span>`);
    return `<li class="reveal"><button class="card" data-id="${esc(l.id)}" aria-label="${esc(l.nom)}, ${l.note == null ? "note à venir" : fmtNote(l.note) + " sur 10"}">
      ${thumbHTML(l)}
      <span class="card__txt"><span class="card__name">${esc(l.nom)}</span><span class="card__meta">${esc(meta)}</span><span class="card__tags">${tags.join("")}</span></span>
      ${ringHTML(l.note)}
    </button></li>`;
  }

  function render() {
    const list = filtered();
    const n = activeFilters();
    $("#filter-count").hidden = !n;
    $("#filter-count").textContent = n;
    $$("#cats .pill").forEach((p) => p.setAttribute("aria-selected", String(p.dataset.cat === state.cat)));
    $$("#sort button").forEach((b) => b.setAttribute("aria-checked", String(b.dataset.sort === state.sort)));

    const searching = !!state.q.trim() || n > 0;
    $("#sec-new").hidden = searching;
    // Trending carousel: on the home page only, when no search, filter or category narrows the list.
    const hot = !searching && !state.cat ? state.lieux.filter((l) => l.tendance).sort((a, b) => (b.note ?? -1) - (a.note ?? -1) || b.derniere.localeCompare(a.derniere)) : [];
    $("#sec-hot").hidden = !hot.length;
    $("#hot").innerHTML = hot.map((l) => hotHTML(l)).join("");
    if (!searching) {
      const visits = filtered({}).flatMap((l) => l.visites.map((v) => ({ l, v }))).sort((a, b) => (b.v.date || "").localeCompare(a.v.date || "")).slice(0, 10);
      $("#latest").innerHTML = visits.map(({ l, v }) => slideHTML(l, v)).join("");
      $("#sec-new").hidden = !visits.length;
    }

    $("#list-title").textContent = searching ? "Résultats" : state.cat === "tendances" ? "Les adresses tendances 🔥" : state.cat ? state.cats[state.cat] : "Toutes les adresses";
    $("#count").textContent = plural(list.length, "adresse");
    $("#cards").innerHTML = list.slice(0, state.shown).map(cardHTML).join("");
    $("#more").hidden = list.length <= state.shown;
    $("#more").textContent = `Voir plus d'adresses (${list.length - state.shown})`;
    $("#empty").hidden = list.length > 0;
    reveal($("#view-home"));
    if (state.view === "map") renderMap();
  }

  // ───────── classement ─────────
  function rankItem(l, i, sub, n) {
    return `<li class="reveal"><button data-id="${esc(l.id)}"><span class="rank__pos">${i + 1}</span><span class="rank__txt"><b>${esc(l.nom)}</b><span>${esc(sub)}</span></span>${pillNote(n)}</button></li>`;
  }

  function renderTop() {
    const rated = state.lieux.filter((l) => l.note != null);
    const sub = (l) => [l.specialite, l.type === "chaine" ? "Chaîne" : l.ville].filter(Boolean).join(" · ");
    const top = [...rated].sort((a, b) => b.note - a.note || b.rated.length - a.rated.length);
    const podium = top.slice(0, 3);
    const order = [1, 0, 2].filter((i) => podium[i]);
    $("#podium").innerHTML = podium.length
      ? order.map((i) => `<button class="podium__step podium__step--${i + 1} reveal" data-id="${esc(podium[i].id)}"><span class="podium__medal">${["🥇", "🥈", "🥉"][i]}</span>${ringHTML(podium[i].note, i === 0 ? "" : "ring--sm")}<span class="podium__name">${esc(podium[i].nom)}</span></button>`).join("")
      : "";
    $("#top").innerHTML = top.slice(0, 10).map((l, i) => rankItem(l, i, sub(l), l.note)).join("") || `<li class="rank-empty">Les notes arrivent bientôt.</li>`;
    const plats = state.lieux.flatMap((l) => l.rated.map((p) => ({ ...p, lieu: l }))).sort((a, b) => b.note - a.note).slice(0, 10);
    $("#top-plats").innerHTML = plats.map((p, i) => rankItem(p.lieu, i, `${p.lieu.nom}${p.prix != null ? " · " + fmtPrix(p.prix) : ""}`, p.note).replace(`<b>${esc(p.lieu.nom)}</b>`, `<b>${esc(p.nom)}</b>`)).join("") || `<li class="rank-empty">Les notes arrivent bientôt.</li>`;
    const flop = [...rated].sort((a, b) => a.note - b.note).filter((l) => l.note < 5).slice(0, 5);
    $("#flop").innerHTML = flop.map((l, i) => rankItem(l, i, sub(l), l.note)).join("") || `<li class="rank-empty">Aucune vraie déception pour l'instant 🙌</li>`;
    reveal($("#view-top"));
  }

  // ───────── map ─────────
  function renderMap() {
    if (!window.L) { $("#map-note").textContent = "La carte n'a pas pu se charger."; return; }
    if (!map) {
      map = L.map("map", { zoomControl: false, attributionControl: true }).setView([48.8566, 2.3522], 10);
      L.control.zoom({ position: "bottomright" }).addTo(map);
      L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      }).addTo(map);
      markers = L.layerGroup().addTo(map);
      map.on("popupopen", (e) => {
        const b = e.popup.getElement().querySelector("[data-pop]");
        if (b) b.addEventListener("click", () => openDetail(b.dataset.pop));
      });
    }
    markers.clearLayers();
    const list = filtered();
    const pts = [];
    let k = 0;
    for (const l of list) {
      const spots = [];
      if (Array.isArray(l.coords)) spots.push({ c: l.coords, label: l.adresse || l.ville || "" });
      for (const v of l.visites) if (Array.isArray(v.coords)) spots.push({ c: v.coords, label: v.adresse || "" });
      for (const s of spots) {
        const icon = L.divIcon({ className: "", html: `<div class="pin" style="--c:${color(l.note)};--d:${Math.min(k++, 30) * 25}ms">${l.note == null ? l.emoji : fmtNote(l.note)}</div>`, iconSize: [40, 40], iconAnchor: [20, 20], popupAnchor: [0, -18] });
        L.marker(s.c, { icon, title: l.nom }).bindPopup(`<b>${esc(l.nom)}</b><br>${esc(s.label)}<br><button class="popup-btn" data-pop="${esc(l.id)}">Voir la fiche</button>`).addTo(markers);
        pts.push(s.c);
      }
    }
    const missing = list.filter((l) => !Array.isArray(l.coords) && !l.visites.some((v) => Array.isArray(v.coords))).length;
    $("#map-note").textContent = !pts.length
      ? "Les emplacements arrivent bientôt sur la carte."
      : missing ? `${plural(pts.length, "adresse")} sur la carte · ${missing} sans emplacement précis (souvent des chaînes)` : "";
    setTimeout(() => { map.invalidateSize(); if (pts.length) map.fitBounds(pts, { padding: [50, 50], maxZoom: 14 }); }, 60);
  }

  // ───────── views ─────────
  function setView(view) {
    if (view === state.view) { window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" }); return; }
    const go = () => {
      state.view = view;
      $$(".tab").forEach((t, i) => {
        const on = t.dataset.view === view;
        t.classList.toggle("is-active", on);
        if (on) { t.setAttribute("aria-current", "page"); $(".tabbar").style.setProperty("--i", i); } else t.removeAttribute("aria-current");
      });
      for (const v of ["home", "map", "top"]) {
        const el = $("#view-" + v);
        el.hidden = v !== view;
        if (v === view) { el.classList.remove("is-entering"); void el.offsetWidth; el.classList.add("is-entering"); }
      }
      $(".footer").hidden = view === "map";
      window.scrollTo(0, 0);
      if (view === "map") renderMap();
      if (view === "top") reveal($("#view-top"));
    };
    if (document.startViewTransition && !reduceMotion && document.visibilityState === "visible") {
      const t = document.startViewTransition(go);
      t.ready.catch(() => {}); t.finished.catch(() => {});
    } else go();
  }

  // ───────── sheets ─────────
  function openSheet(dlg) {
    if (!dlg.open) dlg.showModal();
    requestAnimationFrame(() => requestAnimationFrame(() => dlg.classList.add("is-open")));
  }

  function closeSheet(dlg) {
    if (!dlg.open) return;
    dlg.classList.remove("is-open");
    dlg.style.removeProperty("--drag");
    const done = () => { dlg.close(); dlg.removeEventListener("transitionend", done); };
    if (reduceMotion) done(); else { dlg.addEventListener("transitionend", done); setTimeout(() => dlg.open && done(), 600); }
  }

  // Drag the sheet down from its top area to close it.
  function enableDrag(dlg) {
    let y0 = null, dy = 0;
    dlg.addEventListener("pointerdown", (e) => {
      const body = $(".sheet__body", dlg);
      const fromTop = e.clientY - dlg.getBoundingClientRect().top;
      if (body.scrollTop > 0 || fromTop > 120 || e.target.closest("button, a, input")) return;
      y0 = e.clientY; dy = 0; dlg.classList.add("is-dragging");
    });
    window.addEventListener("pointermove", (e) => {
      if (y0 == null) return;
      dy = Math.max(0, e.clientY - y0);
      dlg.style.setProperty("--drag", dy + "px");
    });
    window.addEventListener("pointerup", () => {
      if (y0 == null) return;
      y0 = null; dlg.classList.remove("is-dragging");
      if (dy > 110) closeSheet(dlg); else dlg.style.setProperty("--drag", "0px");
    });
    dlg.addEventListener("cancel", (e) => { e.preventDefault(); closeSheet(dlg); });
    dlg.addEventListener("click", (e) => { if (e.target === dlg || e.target.closest("[data-close]")) closeSheet(dlg); });
  }

  function itineraire(l, v) {
    const coords = v?.coords || l.coords;
    const dest = v?.adresse || l.adresse || (l.type === "independant" ? [l.nom, l.ville].filter(Boolean).join(" ") : "");
    if (!dest && !coords) return "";
    const q = coords ? coords.join(",") : dest;
    return `https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(q)}`;
  }

  function openDetail(id) {
    const l = state.lieux.find((x) => x.id === id);
    if (!l) return;
    const sub = [l.specialite, l.type === "chaine" ? "Chaîne" : l.type === "independant" ? "Indépendant" : "", l.ville].filter(Boolean).join(" · ");
    const tags = [
      l.statut === "ferme-definitivement" && `<span class="tag tag--closed">Fermé définitivement</span>`,
      l.tendance && `<span class="tag tag--hot">🔥 Tendance</span>`,
      state.cats[l.categorie] && `<span class="tag">${CAT_EMOJI[l.categorie] || ""} ${esc(state.cats[l.categorie])}</span>`,
      `<span class="tag">${plural(l.visites.length, "visite")}</span>`,
      ...l.nets.map((n) => `<span class="tag">${NETS[n]}</span>`),
    ].filter(Boolean).join("");
    const pros = (l.points_forts || []).length || (l.points_faibles || []).length
      ? `<div class="box"><div class="proscons">
          <div><h3>Points forts</h3><ul class="plus">${(l.points_forts || []).map((p) => `<li><i><svg><use href="#i-plus"/></svg></i>${esc(p)}</li>`).join("") || "<li>—</li>"}</ul></div>
          <div><h3>Points faibles</h3><ul class="minus">${(l.points_faibles || []).map((p) => `<li><i><svg><use href="#i-minus"/></svg></i>${esc(p)}</li>`).join("") || "<li>—</li>"}</ul></div>
        </div></div>`
      : "";
    const route = itineraire(l);
    const addr = l.adresse || (l.type === "independant" && l.ville)
      ? `<div class="box"><div class="addr"><span class="addr__ico"><svg><use href="#i-pin"/></svg></span><p>${esc(l.adresse || l.ville)}</p>${route ? `<a class="btn btn--sm" href="${route}" target="_blank" rel="noopener">Y aller</a>` : ""}</div></div>`
      : "";
    const visits = l.visites.map((v) => {
      const vroute = l.type === "chaine" ? itineraire(l, v) : "";
      return `<div class="visit">
        <span class="visit__title">${esc(v.titre || "Visite")}</span>
        <span class="visit__date">${fmtDate(v.date)}${v.partenariat ? ` · <span class="tag tag--gift"><svg><use href="#i-gift"/></svg>${esc(PARTNER[v.partenariat] || "Offert")}</span>` : ""}</span>
        ${v.adresse ? `<span class="visit__where"><svg><use href="#i-pin"/></svg>${esc(v.adresse)}</span>` : ""}
        ${(v.plats || []).length ? `<ul class="plats">${v.plats.map((p) => `<li><span class="p-name">${esc(p.nom)}</span><span class="p-price">${fmtPrix(p.prix)}</span>${pillNote(typeof p.note === "number" ? p.note : null)}</li>`).join("")}</ul>` : ""}
        ${v.avis ? `<p class="visit__avis">${esc(v.avis)}</p>` : ""}
        <div class="visit__videos">${(v.videos || []).filter((x) => NETS[x.platform]).map((x) => `<a class="btn btn--net btn--${x.platform}" href="${esc(x.url)}" target="_blank" rel="noopener"><svg><use href="#i-play"/></svg>${NETS[x.platform]}</a>`).join("")}${vroute ? `<a class="btn btn--net btn--soft" href="${vroute}" target="_blank" rel="noopener"><svg><use href="#i-route"/></svg>Itinéraire</a>` : ""}</div>
      </div>`;
    }).join("");

    $("#sheet-body").innerHTML = `
      <div class="detail__hero">${thumbHTML(l)}<button class="icon-btn detail__close" data-close aria-label="Fermer"><svg><use href="#i-close"/></svg></button></div>
      <div class="detail__head">
        <div><h2 id="sheet-title">${esc(l.nom)}</h2>${sub ? `<p class="detail__sub">${esc(sub)}</p>` : ""}</div>
        ${ringHTML(l.note, "ring--lg")}
      </div>
      <div class="detail__tags">${tags}</div>
      <div class="detail__pad">
        ${l.note != null ? `<p class="note-small">${l.rated.length ? `Note = moyenne de ${plural(l.rated.length, "plat")} noté${l.rated.length > 1 ? "s" : ""}.` : "Note globale donnée dans la vidéo."}</p>` : ""}
        ${l.tendance ? `<div class="box box--hot"><h3>🔥 Pourquoi c'est tendance</h3><p class="avis">${esc(l.tendance)}</p></div>` : ""}
        ${l.avis ? `<div class="box"><h3>Mon avis</h3><p class="quote">${esc(l.avis)}</p></div>` : ""}
        ${pros}
        ${addr}
        <div class="box"><h3>${l.visites.length > 1 ? `Mes ${l.visites.length} visites` : "Ce que j'ai goûté"}</h3><div class="timeline">${visits}</div></div>
      </div>
      <div class="detail__actions">
        <button class="btn btn--soft" data-share><svg><use href="#i-share"/></svg>Partager</button>
        ${route ? `<a class="btn" href="${route}" target="_blank" rel="noopener"><svg><use href="#i-route"/></svg>Itinéraire</a>` : ""}
      </div>`;
    const dlg = $("#sheet");
    $(".sheet__body", dlg).scrollTop = 0;
    openSheet(dlg);
    setTimeout(() => $$(".ring", dlg).forEach((r) => r.classList.add("is-in")), 250);
    history.replaceState(null, "", "#lieu=" + encodeURIComponent(l.id));
    $("[data-share]", dlg).addEventListener("click", (e) => share(`${l.nom}${l.note != null ? " : " + fmtNote(l.note) + "/10" : ""} selon Amed 🧢`, location.href, e.currentTarget));
  }

  async function share(text, url, btn) {
    try {
      if (navigator.share) await navigator.share({ title: "Les adresses d'Amed", text, url });
      else { await navigator.clipboard.writeText(url); if (btn) { const t = btn.innerHTML; btn.textContent = "Lien copié ✔"; setTimeout(() => (btn.innerHTML = t), 1800); } }
    } catch (_) { /* partage annulé */ }
  }

  function readHash() {
    const m = location.hash.match(/lieu=([^&]+)/);
    if (m) setTimeout(() => openDetail(decodeURIComponent(m[1])), 50);
  }

  // ───────── install banner ─────────
  function setupInstall() {
    const standalone = matchMedia("(display-mode: standalone)").matches || navigator.standalone;
    if (standalone || store.get("install-dismissed")) return;
    let deferred = null;
    const ios = /iphone|ipad|ipod/i.test(navigator.userAgent) && !/crios|fxios/i.test(navigator.userAgent);
    const show = () => { $("#install").hidden = false; };
    window.addEventListener("beforeinstallprompt", (e) => { e.preventDefault(); deferred = e; setTimeout(show, 6000); });
    if (ios) { $("#install-txt").textContent = "Touche Partager puis « Sur l'écran d'accueil »."; $("#install-go").hidden = true; setTimeout(show, 8000); }
    $("#install-go").addEventListener("click", async () => { if (deferred) { deferred.prompt(); await deferred.userChoice; } $("#install").hidden = true; });
    $("#install-close").addEventListener("click", () => { $("#install").hidden = true; store.set("install-dismissed", "1"); });
  }

  // ───────── events ─────────
  let qTimer;
  $("#q").addEventListener("input", (e) => { clearTimeout(qTimer); qTimer = setTimeout(() => { state.q = e.target.value; state.shown = PAGE; render(); }, 140); });
  $("#cats").addEventListener("click", (e) => {
    const b = e.target.closest(".pill");
    if (!b) return;
    state.cat = b.dataset.cat; state.shown = PAGE; render();
    b.scrollIntoView({ inline: "center", block: "nearest", behavior: reduceMotion ? "auto" : "smooth" });
  });
  document.addEventListener("click", (e) => {
    const b = e.target.closest("[data-cat-link]");
    if (!b) return;
    state.cat = b.dataset.catLink; state.shown = PAGE; render();
    $("#list-title").scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
  });
  $("#sort").addEventListener("click", (e) => { const b = e.target.closest("[data-sort]"); if (b) { state.sort = b.dataset.sort; render(); } });
  $("#more").addEventListener("click", () => { state.shown += PAGE; render(); });
  $$(".tab").forEach((t) => t.addEventListener("click", () => setView(t.dataset.view)));
  document.addEventListener("click", (e) => {
    const b = e.target.closest("[data-id]");
    if (b) openDetail(b.dataset.id);
  });
  $("#share-site").addEventListener("click", (e) => share("Toutes les adresses testées par Amed 🧢", location.origin + location.pathname, null));

  // Filters
  $("#open-filters").addEventListener("click", () => openSheet($("#filters")));
  $("#f-ville").addEventListener("click", (e) => { const b = e.target.closest(".chip-btn"); if (!b) return; state.ville = b.dataset.v; $$("#f-ville .chip-btn").forEach((x) => x.classList.toggle("is-on", x === b)); render(); });
  $("#f-type").addEventListener("click", (e) => { const b = e.target.closest(".chip-btn"); if (!b) return; state.type = b.dataset.v; $$("#f-type .chip-btn").forEach((x) => x.classList.toggle("is-on", x === b)); render(); });
  $("#f-note").addEventListener("input", (e) => { state.note = Number(e.target.value); $("#f-note-out").textContent = state.note ? `${state.note} et plus` : "toutes"; render(); });
  $("#f-rated").addEventListener("change", (e) => { state.rated = e.target.checked; render(); });
  const resetFilters = () => {
    Object.assign(state, { ville: "", type: "", note: 0, rated: false, q: "", cat: "", shown: PAGE });
    $("#q").value = ""; $("#f-note").value = 0; $("#f-note-out").textContent = "toutes"; $("#f-rated").checked = false;
    $$("#f-ville .chip-btn, #f-type .chip-btn").forEach((x) => x.classList.toggle("is-on", x.dataset.v === ""));
    render();
  };
  $("#f-reset").addEventListener("click", resetFilters);
  $("#reset-empty").addEventListener("click", resetFilters);

  enableDrag($("#sheet"));
  enableDrag($("#filters"));
  $("#sheet").addEventListener("close", () => history.replaceState(null, "", location.pathname + location.search));

  const appbar = $("#appbar");
  window.addEventListener("scroll", () => appbar.classList.toggle("is-scrolled", window.scrollY > 8), { passive: true });

  if ("serviceWorker" in navigator && location.protocol === "https:") navigator.serviceWorker.register("sw.js").catch(() => {});

  setupInstall();
  load();
})();

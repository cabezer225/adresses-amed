(() => {
  "use strict";

  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const NETS = { tiktok: "TikTok", instagram: "Instagram", youtube: "YouTube" };
  const PARTNER = { pub: "Pub", "produits-offerts": "Produits offerts", invitation: "Invitation" };
  const CAT_EMOJI = { "fast-food": "🍔", "patisserie-glacier": "🧁", "street-food-etranger": "🌍" };
  const CAT_ICON = { "fast-food": "burger", "patisserie-glacier": "cake", "street-food-etranger": "globe" };
  const PAGE = 30;
  const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const finePointer = matchMedia("(hover: hover) and (pointer: fine)").matches;

  const state = { lieux: [], byId: new Map(), cats: {}, q: "", cat: "", ville: "", type: "", note: 0, rated: false, sort: "note", view: "home", shown: PAGE };
  let map = null, markers = null, mapKey = "";

  // ───────── helpers ─────────
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const norm = (s) => String(s ?? "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
  const fmtNote = (n) => (Number.isInteger(n) ? String(n) : n.toFixed(1).replace(".", ","));
  const fmtPrix = (p) => (p == null || p === "" ? "" : typeof p === "number" ? p.toFixed(2).replace(".", ",").replace(",00", "") + " €" : esc(p));
  const fmtDate = (d, short) => (d ? new Date(d + "T12:00:00").toLocaleDateString("fr-FR", short ? { day: "numeric", month: "short", year: "numeric" } : { day: "numeric", month: "long", year: "numeric" }) : "");
  const tone = (n) => (n == null ? "none" : n >= 7.5 ? "good" : n >= 5 ? "mid" : "bad");
  const scoreEmoji = (n) => (n >= 9.5 ? "🔥" : n >= 8 ? "😋" : n >= 6.5 ? "👍" : n >= 5 ? "😐" : "😬");
  const plural = (n, w) => `${n} ${w}${n > 1 ? "s" : ""}`;
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (_) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (_) { /* stockage indisponible */ } },
  };
  const icon = (id) => `<svg aria-hidden="true"><use href="#i-${id}"/></svg>`;

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

  // Initials for places without a logo, like the monogram tiles of the sketch.
  const initials = (nom) => {
    const w = String(nom).replace(/['’]/g, " ").split(/[\s\-–·&]+/).filter((x) => /^[\p{L}\d]/u.test(x) && !/^(le|la|les|de|du|des|et|l|d|chez|the)$/i.test(x));
    return ((w[0]?.[0] || "") + (w[1]?.[0] || w[0]?.[1] || "")).toUpperCase();
  };

  // Logo on a white tile in relief; a monogram tile when there is no logo or it fails to load.
  function tileHTML(l, size) {
    const s = size ? ` style="--s:${size}px"` : "";
    if (l.logo) return `<span class="tile"${s}><img src="${esc(l.logo)}" alt="" width="256" height="256" loading="lazy" decoding="async" data-mono="${esc(l.mono)}"></span>`;
    return `<span class="tile tile--mono"${s} aria-hidden="true">${esc(l.mono)}</span>`;
  }
  document.addEventListener("error", (e) => {
    const img = e.target;
    if (img.tagName !== "IMG" || !img.dataset.mono) return;
    const t = img.parentNode; t.classList.add("tile--mono"); t.textContent = img.dataset.mono;
  }, true);

  // The verdict stamp, as in the videos: big score, small "/10", optional emoji.
  function stampHTML(n, size = "", emoji = false) {
    if (n == null) return `<span class="stamp stamp--none ${size}">Note<br>à venir</span>`;
    return `<span class="stamp stamp--${tone(n)} ${size}" aria-label="${fmtNote(n)} sur 10">${fmtNote(n)}<small>/10</small>${emoji ? `<span class="emo" aria-hidden="true">${scoreEmoji(n)}</span>` : ""}</span>`;
  }

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
    // The dish shown on the label: the best rated one, else the first one with a price.
    const allPlats = visites.flatMap((v) => v.plats || []);
    const best = [...rated].sort((a, b) => b.note - a.note)[0] || allPlats.find((p) => p.prix != null) || allPlats[0] || null;
    const l = { ...lieu, visites, note, rated, nets, best, derniere: visites[0]?.date || "" };
    l.emoji = emojiFor(l);
    l.mono = initials(l.nom);
    l.haystack = norm([l.nom, l.ville, l.specialite, l.adresse, ...visites.flatMap((v) => [v.titre, ...(v.plats || []).map((p) => p.nom)])].join(" "));
    l.metaLine = [l.specialite, l.type === "chaine" ? "Chaîne" : l.ville].filter(Boolean).join(" · ");
    return l;
  }

  const dishLabel = (p) => (p ? `<span class="label"><span class="label__t">${esc(p.nom)}</span>${p.prix != null && p.prix !== "" ? `<b>· ${fmtPrix(p.prix)}</b>` : ""}</span>` : "");

  // ───────── load ─────────
  async function load() {
    $("#featured").innerHTML = `<div class="skeleton" style="height:190px"></div>`;
    $("#cards").innerHTML = Array.from({ length: 4 }, () => `<li class="skeleton" style="height:84px"></li>`).join("");
    try {
      const res = await fetch("data/guide.json", { cache: "no-cache" });
      if (!res.ok) throw new Error(res.status);
      const data = await res.json();
      state.cats = data.meta?.categories || {};
      state.lieux = (data.lieux || []).map(enrich);
      for (const l of state.lieux) state.byId.set(l.id, l);
      const maj = data.meta?.maj ? `Dernière mise à jour : ${fmtDate(data.meta.maj)}.` : "";
      $$(".footer").forEach((f) => { f.replaceChildren($("#footer-tpl").content.cloneNode(true)); $(".maj", f).textContent = maj; });
          } catch (e) {
      $("#featured").innerHTML = "";
      $("#cards").innerHTML = "";
      $("#count").textContent = "Impossible de charger le guide pour le moment. Réessaie dans un instant.";
      return;
    }
    renderCats();
    renderVilles();
    render();
    renderTop();
    readHash();
  }

  function renderCats() {
    const keys = Object.keys(state.cats).filter((k) => state.lieux.some((l) => l.categorie === k));
    const all = [["", "Tout", ""], ...(state.lieux.some((l) => l.tendance) ? [["tendances", "Tendances", icon("flame")]] : []), ...keys.map((k) => [k, state.cats[k], CAT_ICON[k] ? icon(CAT_ICON[k]) : ""])];
    $("#cats").innerHTML = all.map(([k, label, ic]) => `<button class="pill" data-cat="${esc(k)}" aria-pressed="${state.cat === k}">${ic}${esc(label)}</button>`).join("");
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
  function featureHTML(l, v) {
    const vid = (v.videos || []).find((x) => NETS[x.platform]);
    const plat = (v.plats || []).find((p) => typeof p.note === "number") || (v.plats || [])[0] || l.best;
    const avis = v.avis || l.avis;
    return `<article class="feature lift">
      <button class="feature__hit" data-id="${esc(l.id)}" aria-label="${esc(l.nom)} : ouvrir la fiche"></button>
      ${tileHTML(l)}
      <span><span class="feature__name">${esc(l.nom)}</span><span class="feature__meta">${esc(l.metaLine)}</span><span class="feature__meta">${esc(fmtDate(v.date))}</span></span>
      ${stampHTML(l.note, "stamp--lg", true)}
      <span class="feature__low">${dishLabel(plat)}${vid ? `<a class="watch" href="${esc(vid.url)}" target="_blank" rel="noopener">${icon("play")}Voir la vidéo</a>` : ""}</span>
      ${avis ? `<span class="feature__quote">« ${esc(avis.length > 150 ? avis.slice(0, 147).replace(/\s+\S*$/, "") + "…" : avis)} »</span>` : ""}
    </article>`;
  }

  function slideHTML(l, meta, hot) {
    return `<button class="slide lift" data-id="${esc(l.id)}">
      <span class="slide__top">${tileHTML(l)}${hot ? `<span class="hot">${icon("flame")}Tendance</span>` : ""}${stampHTML(l.note, "stamp--sm")}</span>
      <span class="slide__body"><span class="slide__name">${esc(l.nom)}</span><span class="slide__meta">${esc(meta)}</span></span>
    </button>`;
  }

  function rowHTML(l) {
    const tags = [];
    if (l.statut === "ferme-definitivement") tags.push(`<span class="tag tag--closed">Fermé</span>`);
    if (l.tendance) tags.push(`<span class="tag tag--hot">${icon("flame")}Tendance</span>`);
    if (l.best) tags.push(dishLabel(l.best).replace('class="label"', 'class="label label--soft"'));
    if (l.visites.some((v) => v.partenariat)) tags.push(`<span class="tag tag--gift">${icon("gift")}Offert</span>`);
    return `<button class="row lift" data-id="${esc(l.id)}" aria-label="${esc(l.nom)}, ${l.note == null ? "note à venir" : fmtNote(l.note) + " sur 10"}">
      ${tileHTML(l)}
      <span class="row__txt"><span class="row__name">${esc(l.nom)}</span><span class="row__meta">${esc(l.metaLine || state.cats[l.categorie] || "")}</span>${tags.length ? `<span class="row__tags">${tags.join("")}</span>` : ""}</span>
      ${stampHTML(l.note)}
    </button>`;
  }

  // Each row is built once and reused: filtering only moves existing nodes, so typing stays instant.
  const rowCache = new Map();
  function rowNode(l) {
    let li = rowCache.get(l.id);
    if (!li) { li = document.createElement("li"); li.innerHTML = rowHTML(l); rowCache.set(l.id, li); }
    return li;
  }

  const rendered = { featured: "", latest: "", hot: "" };
  function setOnce(slot, key, el, html) {
    if (rendered[slot] === key) return;
    rendered[slot] = key; el.innerHTML = html(); el.scrollLeft = 0;
  }

  function render() {
    const list = filtered();
    const n = activeFilters();
    $("#filter-count").hidden = !n;
    $("#filter-count").textContent = n;
    $$("#cats .pill").forEach((p) => p.setAttribute("aria-pressed", String(p.dataset.cat === state.cat)));
    $$("#sort button").forEach((b) => b.setAttribute("aria-checked", String(b.dataset.sort === state.sort)));

    const searching = !!state.q.trim() || n > 0;
    $("#sec-new").hidden = searching;
    if (!searching) {
      const visits = filtered({}).flatMap((l) => l.visites.map((v) => ({ l, v }))).sort((a, b) => (b.v.date || "").localeCompare(a.v.date || "")).slice(0, 11);
      $("#sec-new").hidden = !visits.length;
      const key = visits.map(({ l, v }) => l.id + v.date).join("|");
      if (visits.length) {
        setOnce("featured", key, $("#featured"), () => featureHTML(visits[0].l, visits[0].v));
        setOnce("latest", key, $("#latest"), () => visits.slice(1).map(({ l, v }) => slideHTML(l, [v.titre, fmtDate(v.date, true)].filter(Boolean).join(" · "))).join(""));
      }
    }
    // Trending carousel: on the home page only, when no search, filter or category narrows the list.
    const hot = !searching && !state.cat ? state.lieux.filter((l) => l.tendance).sort((a, b) => (b.note ?? -1) - (a.note ?? -1) || b.derniere.localeCompare(a.derniere)) : [];
    $("#sec-hot").hidden = !hot.length;
    if (hot.length) setOnce("hot", hot.map((l) => l.id).join("|"), $("#hot"), () => hot.map((l) => slideHTML(l, l.tendance, true)).join(""));

    $("#list-title").textContent = searching ? "Résultats" : state.cat === "tendances" ? "Les adresses tendances" : state.cat ? state.cats[state.cat] : "Toutes les adresses";
    $("#count").textContent = plural(list.length, "adresse");
    $("#cards").replaceChildren(...list.slice(0, state.shown).map(rowNode));
    $("#more").hidden = list.length <= state.shown;
    $("#more").textContent = `Voir plus d'adresses (${list.length - state.shown})`;
    $("#empty").hidden = list.length > 0;
    if (state.view === "map") renderMap();
  }

  // Coalesce bursts of input (typing, dragging the slider) into one render per frame.
  let raf = 0;
  const scheduleRender = () => {
    if (raf) return;
    const run = () => { raf = 0; render(); };
    raf = document.hidden ? setTimeout(run, 16) : requestAnimationFrame(run);
  };

  // ───────── classement ─────────
  function rankRow(l, i, title, sub, n) {
    return `<li><button class="row lift" data-id="${esc(l.id)}"><span class="rank-pos">${i + 1}</span><span class="row__txt"><span class="row__name">${esc(title)}</span><span class="row__meta">${esc(sub)}</span></span>${stampHTML(n, "stamp--sm")}</button></li>`;
  }

  function renderTop() {
    const rated = state.lieux.filter((l) => l.note != null);
    const top = [...rated].sort((a, b) => b.note - a.note || b.rated.length - a.rated.length);
    const podium = top.slice(0, 3);
    const H = [128, 92, 70];
    $("#podium").innerHTML = [1, 0, 2].filter((i) => podium[i]).map((i) => `
      <button class="step step--${i + 1}" data-id="${esc(podium[i].id)}">
        ${tileHTML(podium[i], i === 0 ? 60 : 52)}
        <span class="step__name">${esc(podium[i].nom)}</span>
        ${stampHTML(podium[i].note, "stamp--sm")}
        <span class="step__block" style="--h:${H[i]}px" aria-hidden="true"><span class="step__top"></span><span class="step__front">${i + 1}</span></span>
      </button>`).join("");
    $("#top").innerHTML = top.slice(0, 10).map((l, i) => rankRow(l, i, l.nom, l.metaLine, l.note)).join("") || `<li class="rank-empty">Les notes arrivent bientôt.</li>`;
    const plats = state.lieux.flatMap((l) => l.rated.map((p) => ({ ...p, lieu: l }))).sort((a, b) => b.note - a.note).slice(0, 10);
    $("#top-plats").innerHTML = plats.map((p, i) => rankRow(p.lieu, i, p.nom, `${p.lieu.nom}${p.prix != null ? " · " + fmtPrix(p.prix) : ""}`, p.note)).join("") || `<li class="rank-empty">Les notes arrivent bientôt.</li>`;
    const flop = [...rated].sort((a, b) => a.note - b.note).filter((l) => l.note < 5).slice(0, 5);
    $("#flop").innerHTML = flop.map((l, i) => rankRow(l, i, l.nom, l.metaLine, l.note)).join("") || `<li class="rank-empty">Aucune vraie déception pour l'instant.</li>`;
  }

  // ───────── map ─────────
  // Google Maps when a key is set, Leaflet + OpenStreetMap otherwise. Either library loads on the
  // first visit to the map, so the home page never waits for it.
  // The key is public by design: restrict it to cabezer225.github.io/* in Google Cloud Console.
  const GMAPS_KEY = "AIzaSyACHKIr0onQLIlw2fV5m_jYs_Ah1G2rBA8";
  const GMAPS_MAP_ID = "1924677edcdcbec2dce20612";
  const useGoogle = !!GMAPS_KEY;
  let mapLib = null, gInfo = null;
  const addScript = (src, attrs = {}) => new Promise((ok, ko) => {
    const js = Object.assign(document.createElement("script"), { src, async: true, ...attrs });
    js.onload = ok; js.onerror = ko; document.head.append(js);
  });
  function loadMapLib() {
    if (mapLib) return mapLib;
    if (useGoogle) {
      const cb = "__gmapsReady";
      mapLib = new Promise((ok, ko) => {
        window[cb] = ok;
        window.gm_authFailure = () => ko(new Error("auth"));
        addScript(`https://maps.googleapis.com/maps/api/js?key=${encodeURIComponent(GMAPS_KEY)}&v=weekly&language=fr&region=FR&loading=async&callback=${cb}`).catch(ko);
      }).then(() => Promise.all([google.maps.importLibrary("maps"), google.maps.importLibrary("marker")]));
    } else {
      document.head.append(Object.assign(document.createElement("link"), { rel: "stylesheet", href: "https://unpkg.com/leaflet@1.9.4/dist/leaflet.css", integrity: "sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=", crossOrigin: "" }));
      mapLib = addScript("https://unpkg.com/leaflet@1.9.4/dist/leaflet.js", { integrity: "sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=", crossOrigin: "" });
    }
    return mapLib;
  }

  const pinHTML = (l) => `<div class="pin${l.note == null ? " pin--none" : ""}" style="--c:${l.note == null ? "" : `var(--${tone(l.note)})`}">${l.note == null ? esc(l.mono) : fmtNote(l.note)}</div>`;
  const popupHTML = (l, label) => `<div class="popup"><b>${esc(l.nom)}</b><br>${esc(label)}<br><button class="popup-btn" data-pop="${esc(l.id)}">Voir la fiche</button></div>`;

  function createMap() {
    if (useGoogle) {
      map = new google.maps.Map($("#map"), {
        center: { lat: 48.8566, lng: 2.3522 }, zoom: 11, mapId: GMAPS_MAP_ID,
        colorScheme: google.maps.ColorScheme ? google.maps.ColorScheme.FOLLOW_SYSTEM : undefined,
        disableDefaultUI: true, zoomControl: true, gestureHandling: "greedy", clickableIcons: false,
      });
      gInfo = new google.maps.InfoWindow();
      markers = [];
    } else {
      map = L.map("map", { zoomControl: false }).setView([48.8566, 2.3522], 11);
      L.control.zoom({ position: "bottomright" }).addTo(map);
      L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      }).addTo(map);
      markers = L.layerGroup().addTo(map);
    }
    // One delegated listener serves the popups of both engines.
    $("#map").addEventListener("click", (e) => {
      const b = e.target.closest("[data-pop]");
      if (b) openDetail(b.dataset.pop);
    });
  }

  function drawMarkers(spots) {
    if (useGoogle) {
      for (const m of markers) m.map = null;
      markers = spots.map(({ l, c, label }) => {
        const tpl = document.createElement("template");
        tpl.innerHTML = pinHTML(l);
        const m = new google.maps.marker.AdvancedMarkerElement({ map, position: { lat: c[0], lng: c[1] }, content: tpl.content.firstElementChild, title: l.nom, gmpClickable: true });
        m.addEventListener("gmp-click", () => { gInfo.setContent(popupHTML(l, label)); gInfo.open({ map, anchor: m }); });
        return m;
      });
      if (spots.length) {
        const bounds = new google.maps.LatLngBounds();
        for (const s of spots) bounds.extend({ lat: s.c[0], lng: s.c[1] });
        map.fitBounds(bounds, 40);
        google.maps.event.addListenerOnce(map, "idle", () => { if (map.getZoom() > 14) map.setZoom(14); });
      }
    } else {
      markers.clearLayers();
      for (const { l, c, label } of spots) {
        const icon = L.divIcon({ className: "", html: pinHTML(l), iconSize: [44, 34], iconAnchor: [22, 17], popupAnchor: [0, -16] });
        L.marker(c, { icon, title: l.nom }).bindPopup(popupHTML(l, label)).addTo(markers);
      }
      if (spots.length) requestAnimationFrame(() => map.fitBounds(spots.map((s) => s.c), { padding: [40, 40], maxZoom: 14, animate: false }));
    }
  }

  function renderMap() {
    if (!map && !(useGoogle ? window.google?.maps?.marker : window.L)) {
      $("#map-note").textContent = "Chargement de la carte…";
      loadMapLib().then(() => { if (state.view === "map") renderMap(); }, () => { mapLib = null; $("#map-note").textContent = "La carte n'a pas pu se charger. Vérifie ta connexion."; });
      return;
    }
    if (!map) createMap();
    const list = filtered();
    const key = list.map((l) => l.id).join("|");
    if (!useGoogle) requestAnimationFrame(() => map.invalidateSize());
    if (key === mapKey) return;   // same places: keep the markers and the current view
    mapKey = key;
    const spots = [];
    for (const l of list) {
      if (Array.isArray(l.coords)) spots.push({ l, c: l.coords, label: l.adresse || l.ville || "" });
      for (const v of l.visites) if (Array.isArray(v.coords)) spots.push({ l, c: v.coords, label: v.adresse || "" });
    }
    drawMarkers(spots);
    const missing = list.filter((l) => !Array.isArray(l.coords) && !l.visites.some((v) => Array.isArray(v.coords))).length;
    $("#map-note").textContent = !spots.length
      ? "Les emplacements arrivent bientôt sur la carte."
      : `${plural(spots.length, "adresse")} sur la carte${missing ? ` · ${missing} sans emplacement précis (souvent des chaînes)` : ""}`;
  }

  // ───────── views ─────────
  const scrollMemo = {};
  function setView(view) {
    if (view === state.view) { window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" }); return; }
    scrollMemo[state.view] = window.scrollY;
    state.view = view;
    $$(".tab").forEach((t, i) => {
      const on = t.dataset.view === view;
      t.classList.toggle("is-active", on);
      if (on) { t.setAttribute("aria-current", "page"); $(".tabbar").style.setProperty("--i", i); } else t.removeAttribute("aria-current");
    });
    for (const v of ["home", "map", "top"]) {
      const el = $("#view-" + v);
      el.hidden = v !== view;
      el.classList.toggle("is-entering", v === view && !reduceMotion);
    }
    window.scrollTo(0, scrollMemo[view] || 0);
    if (view === "map") renderMap();
  }
  $$(".view").forEach((v) => v.addEventListener("animationend", () => v.classList.remove("is-entering")));

  // ───────── press-to-lift (light 3D) ─────────
  function tilt(card, e, k) {
    const r = card.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
    card.style.setProperty("--rx", `${(-y * k).toFixed(2)}deg`);
    card.style.setProperty("--ry", `${(x * k).toFixed(2)}deg`);
  }
  function untilt(card) { card.classList.remove("is-pressed", "is-tilt"); card.style.removeProperty("--rx"); card.style.removeProperty("--ry"); }
  if (!reduceMotion) {
    let pressed = null, timer = 0;
    const release = () => { clearTimeout(timer); if (pressed) { untilt(pressed); pressed = null; } };
    document.addEventListener("pointerdown", (e) => {
      const card = e.target.closest(".lift");
      if (!card || e.target.closest("a")) return;
      release();
      // A short delay, so a scroll that starts on a card does not make it twitch.
      timer = setTimeout(() => { pressed = card; card.classList.add("is-pressed"); tilt(card, e, 7); }, 90);
    }, { passive: true });
    ["pointerup", "pointercancel", "dragstart"].forEach((t) => document.addEventListener(t, () => setTimeout(release, 60), { passive: true }));
    window.addEventListener("scroll", release, { passive: true, capture: true });
    if (finePointer) {
      let hovered = null, frame = 0, last = null;
      document.addEventListener("pointermove", (e) => {
        last = e;
        if (frame) return;
        frame = requestAnimationFrame(() => {
          frame = 0;
          const card = last.target.closest?.(".lift");
          if (hovered && hovered !== card) { hovered.classList.remove("is-tilt"); untilt(hovered); }
          hovered = card;
          if (card) { card.classList.add("is-tilt"); tilt(card, last, 5); }
        });
      }, { passive: true });
    }
  }

  // ───────── sheets ─────────
  const app = $("#app");
  const narrow = () => innerWidth < 760;
  function openSheet(dlg) {
    if (!dlg.open) dlg.showModal();
    app.style.setProperty("--origin-y", `${window.scrollY + innerHeight / 2}px`);
    requestAnimationFrame(() => requestAnimationFrame(() => {
      dlg.classList.add("is-open");
      if (narrow()) app.classList.add("is-behind");
    }));
  }

  function closeSheet(dlg) {
    if (!dlg.open) return;
    dlg.classList.remove("is-open");
    app.classList.remove("is-behind");
    dlg.style.removeProperty("--drag");
    let done = false;
    const finish = () => { if (done) return; done = true; dlg.close(); dlg.removeEventListener("transitionend", onEnd); };
    const onEnd = (e) => { if (e.target === dlg && e.propertyName === "transform") finish(); };
    if (reduceMotion) finish(); else { dlg.addEventListener("transitionend", onEnd); setTimeout(finish, 600); }
  }

  // Drag the sheet down by its top zone ([data-drag]) to close it. Pointer capture keeps the gesture
  // even when the finger leaves the zone; cancel always resets, so the sheet never stays stuck.
  function enableDrag(dlg) {
    let id = null, y0 = 0, dy = 0, t0 = 0;
    dlg.addEventListener("pointerdown", (e) => {
      const zone = e.target.closest("[data-drag]");
      if (!zone || e.target.closest("button, a, input") || !narrow()) return;
      id = e.pointerId; y0 = e.clientY; dy = 0; t0 = performance.now();
      zone.setPointerCapture(id);
      dlg.classList.add("is-dragging");
    });
    dlg.addEventListener("pointermove", (e) => {
      if (e.pointerId !== id) return;
      dy = Math.max(0, e.clientY - y0);
      dlg.style.setProperty("--drag", dy + "px");
    });
    const end = (e) => {
      if (e.pointerId !== id) return;
      id = null; dlg.classList.remove("is-dragging");
      const fast = dy > 40 && dy / (performance.now() - t0) > 0.6;
      if (dy > 120 || fast) closeSheet(dlg); else dlg.style.setProperty("--drag", "0px");
    };
    dlg.addEventListener("pointerup", end);
    dlg.addEventListener("pointercancel", end);
    dlg.addEventListener("lostpointercapture", end);
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
    const l = state.byId.get(id);
    if (!l) return;
    const sub = [l.specialite, l.type === "chaine" ? "Chaîne" : l.type === "independant" ? "Indépendant" : "", l.ville].filter(Boolean).join(" · ");
    const tags = [
      l.statut === "ferme-definitivement" && `<span class="tag tag--closed">Fermé définitivement</span>`,
      l.tendance && `<span class="tag tag--hot">${icon("flame")}Tendance</span>`,
      state.cats[l.categorie] && `<span class="tag">${CAT_ICON[l.categorie] ? icon(CAT_ICON[l.categorie]) : ""}${esc(state.cats[l.categorie])}</span>`,
      `<span class="tag">${plural(l.visites.length, "visite")}</span>`,
      ...l.nets.map((n) => `<span class="tag">${NETS[n]}</span>`),
    ].filter(Boolean).join("");
    const pros = (l.points_forts || []).length || (l.points_faibles || []).length
      ? `<div class="box"><div class="proscons">
          <div><h3>Points forts</h3><ul class="plus">${(l.points_forts || []).map((p) => `<li><i>${icon("plus")}</i>${esc(p)}</li>`).join("") || "<li>—</li>"}</ul></div>
          <div><h3>Points faibles</h3><ul class="minus">${(l.points_faibles || []).map((p) => `<li><i>${icon("minus")}</i>${esc(p)}</li>`).join("") || "<li>—</li>"}</ul></div>
        </div></div>`
      : "";
    const route = itineraire(l);
    const addr = l.adresse || (l.type === "independant" && l.ville)
      ? `<div class="box"><div class="addr"><span class="addr__ico">${icon("pin")}</span><p>${esc(l.adresse || l.ville)}</p>${route ? `<a class="btn btn--sm" href="${route}" target="_blank" rel="noopener">Y aller</a>` : ""}</div></div>`
      : "";
    const visits = l.visites.map((v) => {
      const vroute = l.type === "chaine" ? itineraire(l, v) : "";
      return `<div class="visit">
        <span class="visit__title">${esc(v.titre || "Visite")}</span>
        <span class="visit__date">${fmtDate(v.date)}${v.partenariat ? `<span class="tag tag--gift">${icon("gift")}${esc(PARTNER[v.partenariat] || "Offert")}</span>` : ""}</span>
        ${v.adresse ? `<span class="visit__where">${icon("pin")}${esc(v.adresse)}</span>` : ""}
        ${(v.plats || []).length ? `<ul class="plats">${v.plats.map((p) => `<li><span class="p-name">${esc(p.nom)}</span><span class="p-price">${fmtPrix(p.prix)}</span>${stampHTML(typeof p.note === "number" ? p.note : null, "stamp--sm")}</li>`).join("")}</ul>` : ""}
        ${v.avis ? `<p class="visit__avis">${esc(v.avis)}</p>` : ""}
        <div class="visit__videos">${(v.videos || []).filter((x) => NETS[x.platform]).map((x) => `<a class="btn btn--net btn--${x.platform}" href="${esc(x.url)}" target="_blank" rel="noopener">${icon("play")}${NETS[x.platform]}</a>`).join("")}${vroute ? `<a class="btn btn--net btn--soft" href="${vroute}" target="_blank" rel="noopener">${icon("route")}Itinéraire</a>` : ""}</div>
      </div>`;
    }).join("");

    $("#sheet-body").innerHTML = `
      <div class="detail__hero" data-drag>${tileHTML(l)}<span class="flash" aria-hidden="true"></span><button class="round-btn detail__close" data-close aria-label="Fermer">${icon("close")}</button></div>
      <div class="detail__head">
        <div><h2 id="sheet-title">${esc(l.nom)}</h2>${sub ? `<p class="detail__sub">${esc(sub)}</p>` : ""}</div>
        ${stampHTML(l.note, "stamp--xl", true)}
      </div>
      <div class="detail__tags">${tags}</div>
      <div class="detail__pad">
        ${l.note != null ? `<p class="note-small">${l.rated.length ? `Note = moyenne de ${plural(l.rated.length, "plat")} noté${l.rated.length > 1 ? "s" : ""}.` : "Note globale donnée dans la vidéo."}</p>` : ""}
        ${l.tendance ? `<div class="box box--hot"><h3>Pourquoi c'est tendance</h3><p>${esc(l.tendance)}</p></div>` : ""}
        ${l.avis ? `<div class="box"><p class="quote">« ${esc(l.avis)} »</p></div>` : ""}
        ${pros}
        ${addr}
        <div class="box"><h3>${l.visites.length > 1 ? `Mes ${l.visites.length} visites` : "Ce que j'ai goûté"}</h3><div class="visits">${visits}</div></div>
      </div>
      <div class="detail__actions">
        <button class="btn btn--soft" data-share>${icon("share")}Partager</button>
        ${route ? `<a class="btn" href="${route}" target="_blank" rel="noopener">${icon("route")}Itinéraire</a>` : ""}
      </div>`;
    const dlg = $("#sheet");
    $(".sheet__body", dlg).scrollTop = 0;
    openSheet(dlg);
    history.replaceState(null, "", "#lieu=" + encodeURIComponent(l.id));
    $("[data-share]", dlg).addEventListener("click", (e) => share(`${l.nom}${l.note != null ? " : " + fmtNote(l.note) + "/10" : ""} selon Amed 🧢`, location.href, e.currentTarget));
  }

  // The logo tile in the sheet leans toward the pointer.
  if (!reduceMotion && finePointer) {
    $("#sheet").addEventListener("pointermove", (e) => {
      const hero = e.target.closest(".detail__hero");
      const tile = hero && $(".tile", hero);
      if (tile) tilt(tile, e, 22);
    }, { passive: true });
    $("#sheet").addEventListener("pointerleave", () => { const t = $("#sheet .detail__hero .tile"); if (t) untilt(t); });
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
  // A shared link opened while the guide is already on screen only changes the hash.
  window.addEventListener("hashchange", () => { if (!$("#sheet").open) readHash(); });

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
  $("#q").addEventListener("input", (e) => {
    clearTimeout(qTimer);
    qTimer = setTimeout(() => { state.q = e.target.value; state.shown = PAGE; scheduleRender(); }, 90);
  });
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
    $("#sec-all").scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
  });
  $("#sort").addEventListener("click", (e) => { const b = e.target.closest("[data-sort]"); if (b) { state.sort = b.dataset.sort; render(); } });
  $("#more").addEventListener("click", () => { state.shown += PAGE; render(); });
  $$(".tab").forEach((t) => t.addEventListener("click", () => setView(t.dataset.view)));
  document.addEventListener("click", (e) => {
    const b = e.target.closest("[data-id]");
    if (b) openDetail(b.dataset.id);
  });
  $("#share-site").addEventListener("click", () => share("Toutes les adresses testées par Amed 🧢", location.origin + location.pathname, null));

  // Filters
  $("#open-filters").addEventListener("click", () => openSheet($("#filters")));
  $("#f-ville").addEventListener("click", (e) => { const b = e.target.closest(".chip-btn"); if (!b) return; state.ville = b.dataset.v; $$("#f-ville .chip-btn").forEach((x) => x.classList.toggle("is-on", x === b)); scheduleRender(); });
  $("#f-type").addEventListener("click", (e) => { const b = e.target.closest(".chip-btn"); if (!b) return; state.type = b.dataset.v; $$("#f-type .chip-btn").forEach((x) => x.classList.toggle("is-on", x === b)); scheduleRender(); });
  $("#f-note").addEventListener("input", (e) => { state.note = Number(e.target.value); $("#f-note-out").textContent = state.note ? `${state.note} et plus` : "toutes"; scheduleRender(); });
  $("#f-rated").addEventListener("change", (e) => { state.rated = e.target.checked; scheduleRender(); });
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
  $("#sheet").addEventListener("close", () => { app.classList.remove("is-behind"); history.replaceState(null, "", location.pathname + location.search); });
  $("#filters").addEventListener("close", () => app.classList.remove("is-behind"));

  // The search bar gets a shadow once it is stuck under the status bar.
  const bar = $("#searchbar");
  let stuckAt = 0;
  const measure = () => { stuckAt = $("#view-home .band").offsetHeight - 4; };
  addEventListener("resize", measure, { passive: true });
  addEventListener("scroll", () => { if (state.view === "home") bar.classList.toggle("is-stuck", scrollY > stuckAt); }, { passive: true });

  if ("serviceWorker" in navigator && location.protocol === "https:") navigator.serviceWorker.register("sw.js").catch(() => {});

  measure();
  setupInstall();
  load();
})();

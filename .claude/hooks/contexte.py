"""Contexte partagé entre l'agent principal et ses sous-agents (hooks Claude Code).

Branché dans .claude/settings.json :
- toutes les 5 minutes d'activité, l'agent principal doit réécrire un résumé
  compressé de la conversation dans .contexte/<session>.md ;
- chaque sous-agent reçoit ce résumé et les dernières demandes de l'utilisateur
  dès son lancement, puis la version à jour toutes les 5 minutes s'il travaille longtemps ;
- après une compaction ou une reprise, l'agent principal le reçoit à nouveau.

Intervalle réglable avec la variable d'environnement CONTEXTE_INTERVALLE (en secondes).
Créer le fichier .contexte/DEBUG enregistre chaque appel dans .contexte/debug.log.
Le script ne bloque jamais une session : toute erreur est ignorée.
"""
import fcntl
import json
import os
import re
import sys
import time
from contextlib import contextmanager
from pathlib import Path

INTERVALLE = int(os.environ.get("CONTEXTE_INTERVALLE", 5 * 60))
MAX_DEMANDES = 3
MAX_CAR_DEMANDE = 1200
GARDE_JOURS = 7

ROOT = Path(__file__).resolve().parents[2]
DOSSIER = ROOT / ".contexte"

CONSIGNE = (
    "⏱ Point contexte (toutes les 5 min d'activité) : avant de continuer, réécris en entier "
    "le résumé compressé de cette conversation dans {chemin} (outil Write, 40 lignes max, sans "
    "copier de code) : objectif de l'utilisateur ; décisions et contraintes ; travail fait "
    "(fichiers, commits) ; état actuel ; prochaines étapes ; questions ouvertes. Ce résumé est "
    "transmis automatiquement aux sous-agents et réinjecté après une compaction. Ne parle pas de "
    "cette mise à jour à l'utilisateur."
)


def chemin(session, suffixe):
    return DOSSIER / f"{session}{suffixe}"


def lire_json(f, defaut):
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return defaut


def ecrire_json(f, donnees):
    f.write_text(json.dumps(donnees, ensure_ascii=False), encoding="utf-8")


def mtime(f):
    try:
        return f.stat().st_mtime
    except OSError:
        return 0


@contextmanager
def verrou(session):
    """Évite deux rappels quand plusieurs outils se terminent en parallèle."""
    with open(chemin(session, ".lock"), "a") as v:
        fcntl.flock(v, fcntl.LOCK_EX)
        yield


def repondre(evenement, texte):
    if texte:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": evenement, "additionalContext": texte}},
                         ensure_ascii=False))


def anciennete(secondes):
    minutes = int(secondes // 60)
    if minutes < 1:
        return "à l'instant"
    if minutes < 60:
        return f"il y a {minutes} min"
    return f"il y a {minutes // 60} h {minutes % 60:02d}"


def version(session):
    return max(mtime(chemin(session, ".md")), mtime(chemin(session, ".demandes.json")))


def contexte(session):
    """Résumé + dernières demandes, ou '' si rien n'est encore connu."""
    parties = []
    resume = chemin(session, ".md")
    texte = resume.read_text(encoding="utf-8").strip() if resume.exists() else ""
    if texte:
        parties.append(f"Résumé compressé de la conversation (mis à jour "
                       f"{anciennete(time.time() - mtime(resume))}) :\n{texte}")
    demandes = lire_json(chemin(session, ".demandes.json"), [])
    if demandes:
        parties.append("Dernières demandes de l'utilisateur (la plus récente en dernier) :\n"
                       + "\n".join(f"- {d}" for d in demandes))
    return "\n\n".join(parties)


def nettoyer():
    limite = time.time() - GARDE_JOURS * 86400
    for f in DOSSIER.iterdir():
        if f.is_file() and f.name not in ("DEBUG", "debug.log") and mtime(f) < limite:
            f.unlink(missing_ok=True)


def debut_session(session, source):
    nettoyer()
    if source in ("compact", "resume"):
        bloc = contexte(session)
        if bloc:
            repondre("SessionStart", "Contexte de cette conversation conservé par le hook "
                                     f"contexte ({chemin(session, '.md')}) :\n\n{bloc}")
        return
    with verrou(session):
        ecrire_json(chemin(session, ".etat.json"), {"rappel": time.time(), "evenements": 0})


def noter_demande(session, demande):
    demande = re.sub(r"\s+", " ", demande or "").strip()
    if not demande:
        return
    if len(demande) > MAX_CAR_DEMANDE:
        demande = demande[:MAX_CAR_DEMANDE] + " […]"
    f = chemin(session, ".demandes.json")
    demandes = lire_json(f, [])[-(MAX_DEMANDES - 1):] + [demande]
    ecrire_json(f, demandes)


def tic_principal(session, evenement):
    """Rappelle à l'agent principal de compresser le contexte toutes les 5 minutes d'activité.

    Après une pause, le rappel ne part que si du travail a eu lieu depuis le précédent."""
    maintenant = time.time()
    with verrou(session):
        f = chemin(session, ".etat.json")
        etat = lire_json(f, None)
        if etat is None:
            etat = {"rappel": maintenant, "evenements": 0}
        elif maintenant - etat["rappel"] < INTERVALLE:
            etat["evenements"] += 1
        elif etat["evenements"] == 0:
            etat = {"rappel": maintenant, "evenements": 1}
        else:
            ecrire_json(f, {"rappel": maintenant, "evenements": 0})
            repondre(evenement, CONSIGNE.format(chemin=chemin(session, ".md")))
            return
        ecrire_json(f, etat)


def debut_sous_agent(session, agent):
    ecrire_json(chemin(session, f".agent-{agent}.json"), {"vu": time.time(), "version": version(session)})
    bloc = contexte(session)
    if bloc:
        repondre("SubagentStart", "Contexte de la conversation principale (transmis automatiquement ; "
                                  f"ta mission reste celle de ton prompt) :\n\n{bloc}")


def tic_sous_agent(session, agent):
    """Toutes les 5 minutes, transmet au sous-agent le contexte s'il a changé depuis le dernier envoi."""
    f = chemin(session, f".agent-{agent}.json")
    maintenant = time.time()
    etat = lire_json(f, None)
    if etat is None:
        ecrire_json(f, {"vu": maintenant, "version": version(session)})
        return
    if maintenant - etat["vu"] < INTERVALLE:
        return
    v = version(session)
    ecrire_json(f, {"vu": maintenant, "version": v})
    if v > etat["version"]:
        repondre("PostToolUse", "Mise à jour du contexte de la conversation principale :\n\n" + contexte(session))


def main():
    entree = json.load(sys.stdin)
    DOSSIER.mkdir(exist_ok=True)
    if (DOSSIER / "DEBUG").exists():
        with open(DOSSIER / "debug.log", "a", encoding="utf-8") as log:
            log.write(json.dumps({k: v for k, v in entree.items() if k in (
                "hook_event_name", "session_id", "agent_id", "agent_type", "source", "tool_name")}) + "\n")
    session = re.sub(r"[^A-Za-z0-9_-]", "", str(entree.get("session_id") or "")) or "sans-session"
    agent = re.sub(r"[^A-Za-z0-9_-]", "", str(entree.get("agent_id") or ""))
    evenement = entree.get("hook_event_name")
    if evenement == "SessionStart":
        debut_session(session, entree.get("source"))
    elif evenement == "SubagentStart" and agent:
        debut_sous_agent(session, agent)
    elif evenement == "UserPromptSubmit":
        noter_demande(session, entree.get("prompt"))
        tic_principal(session, evenement)
    elif evenement == "PostToolUse":
        if agent:
            tic_sous_agent(session, agent)
        else:
            tic_principal(session, evenement)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass

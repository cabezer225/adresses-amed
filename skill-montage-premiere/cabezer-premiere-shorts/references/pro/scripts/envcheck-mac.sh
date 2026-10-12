#!/bin/bash
# envcheck-mac.sh : relevé d'environnement en LECTURE SEULE pour le Mac de Cabezer.
# Non exécuté sur macOS à la date de rédaction (sandbox Linux) ; syntaxe et
# comportement hors Mac testés seulement. Chaque chemin est cherché, jamais supposé.
# Usage : bash envcheck-mac.sh [dossier_projet] > Controles/envcheck-$(date +%Y%m%d).txt
set -u
PB=/usr/libexec/PlistBuddy

echo "== Date et système"
date '+%Y-%m-%d %H:%M:%S %Z'
sw_vers 2>/dev/null || echo "sw_vers absent (pas macOS ?)"
echo "Langue système (AppleLanguages) :"
defaults read -g AppleLanguages 2>/dev/null | tr -d '\n' ; echo

echo "== Applications Adobe (dossier /Applications, profondeur 2)"
find /Applications -maxdepth 2 \( -iname "Adobe Premiere*.app" -o -iname "Adobe After Effects*.app" -o -iname "Adobe Media Encoder*.app" \) 2>/dev/null | while read -r app; do
  v=$("$PB" -c "Print CFBundleShortVersionString" "$app/Contents/Info.plist" 2>/dev/null || echo "?")
  b=$("$PB" -c "Print CFBundleIdentifier" "$app/Contents/Info.plist" 2>/dev/null || echo "?")
  echo "$app | version $v | bundle $b"
done

echo "== aerender (chercher, ne pas supposer le chemin)"
find /Applications -maxdepth 4 -name aerender -type f 2>/dev/null | head -5
[ -x "$(find /Applications -maxdepth 4 -name aerender -type f 2>/dev/null | head -1)" ] 2>/dev/null && echo "aerender présent"

echo "== Préférences Adobe (fichiers, nom seulement)"
find "$HOME/Library/Preferences/Adobe" -maxdepth 4 -iname "*Premiere*" 2>/dev/null | head -10
find "$HOME/Library/Preferences/Adobe" -maxdepth 4 -iname "*After Effects*" 2>/dev/null | head -10

echo "== Cache média (taille seulement)"
du -sh "$HOME/Library/Application Support/Adobe/Common/Media Cache Files" 2>/dev/null || echo "Media Cache Files : absent ou non lisible"
du -sh "$HOME/Library/Application Support/Adobe/Common/Media Cache" 2>/dev/null || true

echo "== Journaux de plantage (noms seulement, les 10 plus récents)"
ls -t "$HOME/Library/Logs/DiagnosticReports"/*Premiere* "$HOME/Library/Logs/DiagnosticReports"/*After* 2>/dev/null | head -10
ls -d "$HOME/Library/Application Support/Adobe/LogTransport2" 2>/dev/null || echo "LogTransport2 : absent"

echo "== Polices attendues (présence seulement ; à confirmer dans Police (Font Book))"
if command -v system_profiler >/dev/null 2>&1; then
  system_profiler SPFontsDataType 2>/dev/null | grep -E "Full Name:" | grep -i -E "Avenir Next|Hoefler|Futura|PT Mono" | sed 's/^ */  /' | sort -u | head -40
else
  echo "system_profiler absent"
fi

echo "== Plugins (dossiers seulement)"
ls -d "/Library/Application Support/Adobe/Common/Plug-ins" 2>/dev/null || echo "Common/Plug-ins : absent"
find /Applications -maxdepth 4 -type d -name "Plug-ins" -path "*After Effects*" 2>/dev/null | head -3

echo "== Outils en ligne de commande"
for t in ffmpeg ffprobe python3 whisper node; do
  p=$(command -v "$t" 2>/dev/null) && echo "$t : $p" || echo "$t : absent"
done

if [ -n "${1:-}" ] && [ -d "$1" ]; then
  echo "== Projet : $1 (dossiers de 1er niveau et dossiers d'enregistrement automatique)"
  find "$1" -maxdepth 1 -mindepth 1 -type d 2>/dev/null | sort
  find "$1" -maxdepth 4 -type d -iname "*auto*save*" 2>/dev/null | head -10
fi

echo "== Espace disque du volume utilisateur"
df -h "$HOME" 2>/dev/null | tail -1
echo "== Fin"

#!/bin/sh
# Lädt die Transliterationen von voynich.nu (René Zandbergen, EVMT). Nicht im Repo enthalten.
set -e
curl -sS -o ZL3b-n.txt https://www.voynich.nu/data/ZL3b-n.txt && cp ZL3b-n.txt ZL.txt
curl -sS -o IT2a-n.txt https://www.voynich.nu/data/IT2a-n.txt
curl -sS -o GC2a-n.txt https://www.voynich.nu/data/GC2a-n.txt
echo "ZL.txt (= ZL3b-n), IT2a-n.txt, GC2a-n.txt geladen."
echo "Vergleichskorpora (la.txt, it.txt, de.txt, cs.txt, fi.txt, hu.txt, zh.txt, ...) sind beliebige Klartexte, siehe README."

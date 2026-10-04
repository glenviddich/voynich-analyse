#!/bin/sh
# Lädt die Transliterationen von voynich.nu (René Zandbergen, EVMT). Nicht im Repo enthalten.
set -e
curl -sS -o ZL3b-n.txt https://www.voynich.nu/data/ZL3b-n.txt && cp ZL3b-n.txt ZL.txt
curl -sS -o IT2a-n.txt https://www.voynich.nu/data/IT2a-n.txt
curl -sS -o GC2a-n.txt https://www.voynich.nu/data/GC2a-n.txt
echo "ZL.txt (= ZL3b-n), IT2a-n.txt, GC2a-n.txt geladen."
echo "Vergleichskorpora (la.txt, it.txt, de.txt, cs.txt, fi.txt, hu.txt, zh.txt, ...) sind beliebige Klartexte, siehe README."
# Deutsch der Epoche (Bibliotheca Augustana, tha.de): Nibelungenlied Hs. B, Wittenwiler "Der Ring", Ackermann aus Böhmen
B="https://www.tha.de/~harsch/germanica/Chronologie"
mkdir -p nib && for i in $(seq -w 1 39); do curl -sS -m 60 "$B/12Jh/Nibelungen/nib_b_$i.html" -o nib/$i.html; done
for f in wit_rinp wit_rin1 wit_rin2 wit_rin3; do curl -sS -m 60 "$B/15Jh/Wittenwiler/$f.html" -o $f.html; done
curl -sS -m 60 "$B/15Jh/Tepl/tep_tod.html" -o tep_tod.html
echo "HTML geladen; Textextraktion siehe dialekt.py-Kommentar (Tags entfernen, Zeilennummern und Spaltenmarker 'I' streichen)."

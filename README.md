# Voynich-Analyse

Statistische Untersuchung des Voynich-Manuskripts (Beinecke MS 408), Oktober 2026. Denis Reiss mit Claude (Anthropic) als Analysewerkzeug.

**Entschlüsselt ist nichts.** Dieses Repository enthält die Skripte, Bewertungsdaten und Transkriptionen, mit denen sich die Befunde in `docs/` nachrechnen lassen.

## Stand (4. Oktober 2026)

Vier Befunde mit Kontrollen, Details und Zahlen in `docs/Gesamtbericht.md` (Abschnitt „Stand und nächste Schritte") und `docs/Preprint-Entwurf.md`:

1. **Text kennt Bild, schwach.** Die Wortfamilie chol/chor/shol/shor ist auf Kräuterseiten mit betonter Wurzel seltener. Sprachstratifiziert (Currier A/B getrennt permutiert): −1,6 je 100 Wörter, p ≈ 0,01, über 81 Familien korrigiert 0,02. Eine vorregistrierte Replikation auf 17 weiteren Seiten war ohne Aussagekraft (zu wenige A-Seiten). Noch nicht unabhängig bestätigt.
2. **Kopie mit Variation, drei Hände, eine Rate.** Fast-Zwillinge +6,1 bis +7,1 Punkte je Schreiberhand; sie sitzen in der Zeilenmitte, nicht am Rand.
3. **Absatz-Erstwörter sind seitenspezifisch, in allen Abschnitten.** Hapax-Anteil 41–59 % gegen 11–21 % an normalen Zeilenanfängen; bleibt nach Abzug des Gallows-Anlauts.
4. **Funktionswörter fehlen, auch gegen ein Kräuterbuch derselben Gattung** (UVM MS 2: Top-10-Wörter 26 % der Tokens gegen 17 %).

Dazu: 10 % der Tokens sind Ordnungsvarianten desselben Glypheninventars, handabhängig (Hand 1 dchey/ckhey, Hände 2–3 chedy/cheky); Tierkreis = exakt 30 Beschriftungen je Zeichen, keine Gradzahlen; 17 Hypothesen messbar ausgeschlossen (Substitution, Löffelsprache, Kompression, Steno, Verbose-Chiffre, Homophone, Codebuch, Rugg-Gitter, Selbstzitat, Silbenschrift, Agglutination, Zahlen, Llull, Leet, Spiegelschrift, f57v-Schlüssel, Zauberformeln, fortlaufende Verschiebung pro Wort).

## Nachrechnen

```sh
pip install pillow          # nur für Bild-Hilfsskripte nötig
./fetch_data.sh             # ZL3b-n, IT2a-n, GC2a-n von voynich.nu
python3 qtest.py            # Lader + q-Präfix-Analyse (wird von vielen Skripten per exec eingebunden)
python3 imgcorr.py          # Bildmerkmale vs. Wortfamilien, 110 Seiten (feats.txt)
python3 rep_test.py         # vorregistrierte Replikation (prereg_rep.txt, feats_rep.txt)
python3 para.py && python3 slot.py && python3 shift.py
```

Die Skripte sind Arbeitsskripte einer Analyse-Session: flach im Verzeichnis, laden `ZL.txt` und einander per `exec(open(...).read())`. Sie sind nicht aufgeräumt, aber vollständig. Die Vergleichskorpora (`la.txt` Augustinus, `it.txt` Dante, `de.txt` Faust, `cs.txt`, `fi.txt` Kalevala, `hu.txt`, `zh.txt` Pinyin, `vi_raw.txt`) sind nicht enthalten; jeder Klartext der Sprache mit ≥ 30.000 Wörtern liefert die gleichen Größenordnungen.

### Wichtige Skripte

| Skript | Zweck |
|---|---|
| `tests.py`, `qtest.py`, `para.py` | Lader für ZL-Transliteration mit Seitenmetadaten (Abschnitt, Sprache, Hand, Absatzmarken) |
| `common.py`, `opt.py`, `stream.py`, `hybrid2.py`, `residual.py` | Kennzahlen (h2, Positionstreue, Zwillinge, Kopplung, Zipf) und generative Modelle; Hybrid Bausteinstrom + 15 % Kopie |
| `imgcorr*.py`, `rep_test.py` | Bildmerkmale ↔ Wortfamilien, Permutationstests, Zweitbewertung Kimi, Negativkontrolle Gemini, Replikation |
| `scribe.py`, `twins.py`, `variants.py` | Schreiberhände, Fast-Zwillinge, Kopiervarianten |
| `slot.py` | Ordnungsvarianten desselben Glypheninventars (Slot-Grammatik-Test) |
| `shift.py` | Test „fortlaufende Verschiebung pro Wort" (Abstandsprofil, Periodensuche) |
| `dialekt.py` | Mittelhochdeutsch (Nibelungenlied B), Frühneuhochdeutsch (Wittenwiler 1410, Ackermann 1401) gegen Voynich; Texte per `fetch_data.sh` |
| `combo.py`, `combo2.py`, `combo3.py`, `combo4.py` | Kombinierte Epochen-Chiffren: Abkürzung + Homophone + Nullen + Funktionswort-Verschmelzung; Nomenklator mit Voynich-Codewörtern + Abschrift + Autokey-Regel |
| `zod.py` | Tierkreis-Beschriftungen |
| `sterne_cmp.py` | Sternenteil (285 Absätze) gegen Antidotarium Nicolai 1471 und Tesoro de' poveri 1494 (OCR per `fetch_data.sh`) |
| `alch98.py`, `uvmstat.py` | Alchemistische Kräuterbücher (98 Kapitelnamen), UVM MS 2 Formelstatistik |
| `rohonc_cmp.py`, `rohonc2.py` | Vergleich Rohonc-Codex (braucht `kt/`, nicht enthalten; `ktfetch.sh` lädt über die API von rechnitzer-kodex.hu) |
| `loeffel.py`, `steno.py`, `leet.py`, `zahlen.py`, `llull.py`, `grille.py`, `lazy.py`, `codebook.py`, `selfcite*.py`, `agglut.py`, `viet.py`, `pinyin_test.py`, `sukhotin.py` | Einzelne Hypothesentests |

### Datendateien

| Datei | Inhalt |
|---|---|
| `feats.txt` | Bildmerkmale 110 Kräuterseiten f1v–f57r (Wurzel_betont, Blaetter_gross, Bluete_auffaellig), Blindbewertung Claude |
| `feats_kimi.txt`, `kimi.csv` | unabhängige Zweitbewertung (Kimi), `feats_cons.txt` Konsensseiten |
| `feats_gemini.txt`, `gemini.csv` | Gemini-Bewertung, als Negativkontrolle (Kappa ≈ 0) |
| `prereg_rep.txt`, `feats_rep.txt` | Vorregistrierung und Blindbewertung der 17 Replikationsseiten |
| `voynich_bildmerkmale_blind.md/.csv`, `anweisung_gemini.md`, `voynich_bildmerkmale_pdf.csv` | Bewertungsanleitung und Seitenlisten für weitere Bewerter |
| `herbidx.json`, `uvm_idx.json`, `bod_idx.json` | Zuordnung Folio → Scan (archive.org, UVM IIIF, Bodleian IIIF) |
| `alch98.txt` | die 98 Pflanzennamen der alchemistischen Kräuterbücher (nach Philip Neal / Segre Rutz) |
| `uvm_entries.txt` | eigene Transkription von 13 Einträgen aus UVM MS 2 (Italian Herbal, 15. Jh.) |
| `ap_aries.txt`, `ap_pisces.txt` | Gradtexte Widder und Fische aus dem Astrolabium Planum (Augsburg 1488, BSB bsb00026866) |

## Quellen

- Transliterationen: R. Zandbergen, ZL3b-n; T. Takahashi, IT2a; G. Claston, GC2a – alle über voynich.nu (dort nachlesen, unter welchen Bedingungen die Dateien genutzt werden dürfen; hier nicht weiterverbreitet).
- Bilder: Beinecke MS 408 über archive.org (IIIF); Oxford Bodleian MS. Canon. Misc. 408 (Digital Bodleian); UVM MS 2 (digitalcollections.uvm.edu); Astrolabium Planum 1488 (Münchener Digitalisierungszentrum).
- Rohonc-Codex: Transkription Király & Tokai, rechnitzer-kodex.hu – nicht enthalten.
- Literatur: siehe `docs/Preprint-Entwurf.md`, Abschnitt 10.

## Lizenz

Code und eigene Daten (Bewertungen, Transkriptionen) unter MIT-Lizenz. Fremde Daten (Transliterationen, Rohonc-Transkription, Bilder) sind nicht Teil dieser Lizenz und nicht enthalten.

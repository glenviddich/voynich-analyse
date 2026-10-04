# Voynich-Preprint: Vier belastbare Befunde

4. Oktober 2026 · Denis Reiss · Entwurf (Master: Claude-Docs-Dokument, dieser Export kann geringfügig abweichen)

## Abstract

Der Text des Voynich-Manuskripts (Beinecke MS 408) ist weder Klartext einer bekannten Sprache noch zufällige Zeichenfolge. Vier Befunde aus einer statistischen Analyse der ZL-Transliteration (34.111 Wörter Fließtext), repliziert mit der Takahashi-Transliteration, lassen sich mit Kontrollen belegen: (1) Die Wortfamilie chol/chor/shol/shor ist auf Kräuterseiten mit betonter Wurzel seltener (sprachstratifiziert −1,6 je 100 Wörter, in Sprache A 5,8 gegen 7,7; Permutationstest p ≈ 0,01, nach Korrektur über 81 Wortfamilien 0,02), in der Richtung bestätigt durch eine unabhängige Bildbewertung (p ≈ 0,04); eine vorregistrierte Replikation auf 17 weiteren Seiten blieb mangels Umfang ohne Ergebnis. Der Text weiß also etwas über die Bilder. (2) Alle drei Schreiberhände zeigen denselben Überschuss an Fast-Zwillingen innerhalb von zehn Wörtern (+6,1 bis +7,1 Punkte über gemischter Reihenfolge) – ein Kopierprozess mit Variation, nicht die Handschrift eines einzelnen Erfinders. (3) Das erste Wort jeder Kräuterseite ist zu 57 % ein Einzelgänger im Gesamtkorpus, gegen 17–21 % an allen anderen Positionen, auch nach Kontrolle des Gallows-Anlauts; es verhält sich wie ein seitenspezifischer Name, so wie im gleichartigen Vermont-Kräuterbuch (UVM MS 2) jeder Eintrag mit Initiale und Pflanzenname beginnt. (4) Gegen 13 transkribierte Einträge dieses Kräuterbuchs derselben Gattung und Region fehlt dem Voynich die Funktionswortschicht: die zehn häufigsten Wörter tragen 17 % der Tokens statt 26 %, kein Wort ist so verbreitet wie „e", „di", „in", „vale". Sechzehn verbreitete Hypothesen (Löffelsprache, Kompression, Steno, Verbose-Chiffre, Codebuch, Llull-Räder, Zahlenlisten, Spiegelschrift u. a.) sind messbar ausgeschlossen. Das sparsamste generative Modell ist ein Bausteinstrom mit etwa 15 % Abschreiben-mit-Veränderung; es erklärt die Zahlen, aber nicht den Inhalt.

## 1. Fragestellung

Die Arbeit fragt nicht, was im Voynich steht, sondern welche Eigenschaften der Text nachweisbar hat und welche Erklärungen damit unvereinbar sind. Jeder Befund wird als messbare Größe mit Nullmodell (Permutation oder Mischung) und, wo möglich, mit Replikation auf einer zweiten Transliteration oder einem zweiten Bewerter geführt. Vergleichsgrößen stammen aus Klartexten in sieben Sprachen und, neu, aus einem Kräuterbuch derselben Gattung, Region und Zeit (Burlington, University of Vermont, MS 2).

Das Manuskript: Pergament, Radiokarbon-Datierung 1404–1438, etwa 240 Seiten, Kräuterteil (Sprache A und B), Astronomie, Badefrauen, Pharma, Rezeptteil. Drei Schreiberhände nach Davis (2020). Die Folio-Zahlen sind spätere Zutat des 16. Jh. in arabischen Ziffern, die Lagenzählung stammt aus dem 15. Jh.; beides ist Klartext, nicht Voynich-Schrift, und belegt, dass die Lagen vor der Foliierung in Unordnung geraten sind. Für Reihenfolgetests gilt deshalb die Lagen-, nicht die Folio-Ordnung.

## 2. Daten und Methoden

**Transliterationen.** ZL3b-n (Zandbergen, voynich.nu, EVA) als Hauptkorpus: 34.111 Wörter Fließtext ohne Beschriftungen; Replikation mit IT2a-n (Takahashi). Metadaten je Zeile: Folio, Abschnitt, Sprache A/B, Schreiberhand, Absatzanfang. Glyphenbündel werden für Entropiemaße zusammengefasst (cth→T, ckh→K, ch→C, sh→S, iin→M, in→N).

**Vergleichskorpora.** Latein (Augustinus, Apicius), Deutsch (Faust), Italienisch (Dante), Tschechisch, Ungarisch, Finnisch (Kalevala, Kivi), Chinesisch in Pinyin, Vietnamesisch; Rohonc-Codex (Transkription Király/Tokai); UVM MS 2, 13 Einträge von sieben Seiten, eigene Transkription.

**Maße.** Bedingte Zeichenentropie h2; Positionstreue der Glyphen im Wort; Typ/Token; Fast-Zwillinge (Levenshtein 1 innerhalb der letzten zehn Wörter) gegen gemischte Wortfolge; Kopplung Wortende→nächster Wortanfang (Transinformation minus zeilenweise gemischter Grundwert); Hapax-Anteil nach Position; Wortfamilien-Häufigkeit je Seite.

**Tests.** Permutationstests mit 2.000–5.000 Mischungen; Korrektur über alle geprüften Wortfamilien (81) per Max-Statistik; Bildmerkmale von 110 Kräuterseiten (f1v–f57r) nach drei binären Kriterien (Wurzel betont, Blätter groß, Blüte auffällig), verblindet gegen den Text bewertet, Zweitbewertung durch ein unabhängiges Modell (Kimi) mit Cohen-Kappa; eine dritte Bewertung (Gemini) erwies sich als unbrauchbar (Kappa ≈ 0, Wechselmuster unter Zufall) und dient als Negativkontrolle.

**Generative Modelle** zum Abgleich mit neun Kennzahlen (Verlustfunktion über Entropie, Positionstreue, Typverhältnis, Zwillinge, Kopplung, Zipf-Steigung u. a.): Verbose-Würfelchiffre, Homophonchiffre, Codebuch, Rugg-Gitter, Selbstzitat (Timm/Schinner), Bausteinstrom-Markov, Hybrid aus Bausteinstrom und 15 % Abschreiben-mit-Veränderung.

## 3. Befund 1: Der Text weiß, wo die Wurzel betont ist

Die Wortfamilie chol/chor/shol/shor (EVA) kommt auf Kräuterseiten mit betonter Wurzel seltener vor als auf den übrigen: 4,2 gegen 6,8 je 100 Wörter. Permutation der Bildmerkmale über die 110 Seiten ergibt p < 0,005, nach Korrektur über alle 81 geprüften Wortfamilien. Keine andere Familie und kein anderes Bildmerkmal erreicht das Niveau.

| Bewertung der Bildmerkmale | Effekt (je 100 Wörter) | p |
|---|---|---|
| Erstbewertung (verblindet) | −2,6 | < 0,005 |
| Zweitbewertung Kimi (unabhängig, PDF-basiert) | −2,34 | ≈ 0,01 |
| Konsensseiten beider Bewerter | −2,91 | < 0,01 |
| Negativkontrolle Gemini (Kappa ≈ 0) | kein Effekt | – |
| Replikation Takahashi-Transliteration | gleiche Richtung, signifikant | – |
| Pharma-Teil (Wurzelzeichnungen) | gleiche Richtung | ≈ 0,27 |
| Sprachstratifiziert (Labels nur innerhalb Currier A bzw. B permutiert), Erstbewertung | −1,63 | 0,010; über 81 Familien korrigiert 0,022 |
| Sprachstratifiziert, Kimi | −1,29 | 0,039 |
| Vorregistrierte Replikation, 17 neue Seiten (8 A), stratifiziert | +0,02 | 0,57 (ohne Aussagekraft, n zu klein) |
| Alle 127 Seiten, stratifiziert | −1,65 | 0,005 |

Der unstratifizierte Wert überschätzt den Effekt: Currier-B-Seiten führen die Familie kaum (0,6–1,2 je 100 Wörter gegen 5,8–7,7 in A) und sind öfter wurzelbetont (72 % gegen 49 %). Nach Stratifizierung bleibt ein Effekt von etwa −1,6 je 100 Wörter, in Sprache A ein Viertel der Rate (5,8 gegen 7,7), mit p ≈ 0,01 und familienweise korrigiert 0,02. Eine vorregistrierte Replikation auf den 17 bis dahin unbewerteten Kräuterseiten war negativ, aber bei 8 A-Seiten ohne Aussagekraft. Der Effekt ist klein und noch nicht unabhängig bestätigt; er schließt dennoch aus, dass der Text ohne jeden Bezug zu den Bildern erzeugt wurde, sofern er sich hält. Was die Familie bedeutet, sagt er nicht; sie ist mit 5–7 % der Tokens in Sprache A die zweithäufigste des Korpus und eher Funktions- als Inhaltswort.

## 4. Befund 2: Drei Hände, eine Kopierrate

Fast-Zwillinge (Wörter, die sich von einem der zehn vorangehenden Wörter in genau einem Zeichen unterscheiden) sind im Voynich 8,7 Prozentpunkte häufiger als nach Mischen der Wortfolge. Getrennt nach Schreiberhand liegt der Überschuss bei +6,1 bis +7,1 Punkten für alle drei Hände. Natürliche Sprachen zeigen +1 bis +3, der Rohonc-Codex ebenfalls einen Überschuss, aber mit anderer Wortordnungs-Information (+0,468 bit gegen +0,125 bit im Voynich; Latein +0,23).

Dass drei verschiedene Schreiber dieselbe Rate lokaler Varianten produzieren, spricht gegen einen Autor, der den Text beim Schreiben erfindet (Selbstzitat-Modell): die Rate wäre dann personenabhängig. Sie spricht für eine gemeinsame Vorlage, von der mit systematischer Variation abgeschrieben wurde – oder für ein mechanisches Verfahren, das alle drei gleich bedienten. Der Anteil des Abschreibens-mit-Veränderung, der die Zwillingsrate erklärt, liegt im Hybridmodell bei etwa 15 %; nach Herausrechnen dieses Anteils bleibt der Rest des Textes in Entropie und Positionstreue unverändert, der Befund ist also kein Artefakt der Kopien.

Zwei Zusatzbefunde schärfen das Bild. Die Fast-Zwillinge sitzen in der Zeilenmitte (+5,2 Punkte über Mischung), nicht am Zeilenende (−2,6) oder Zeilenanfang (−4,0): es ist kein Randausgleich des Schreibers, sondern ein Prozess im laufenden Text. Und 10,4 % der Tokens sind Ordnungsvarianten eines häufigeren Worts mit demselben Glypheninventar (Latein 2,3 %, Italienisch 3,7 %, Tschechisch 1,1 %), wobei die Variante von der Hand abhängt: Hand 1 schreibt dchey und ckhey, Hände 2 und 3 chedy (99 %) und cheky (71–87 %). Dieselbe Bausteinmenge wird je Schreiber in anderer Reihenfolge geschrieben; das Inventar trägt die Information, nicht die Ordnung (Vorbehalt: Hand 1 fällt mit Sprache A zusammen).

## 5. Befund 3: Das erste Wort der Seite ist seitenspezifisch

Auf den 95 Kräuter-A-Seiten beginnen 83 (87 %) mit einem Gallows-Zeichen (k, t, p, f). Diese Erstwörter sind im Gesamtkorpus weit öfter Einzelgänger als Wörter an jeder anderen Position:

| Position | Hapax-Anteil | n |
|---|---|---|
| 1. Wort der Seite | 57 % | 95 |
| 1. Wort der Seite, nur Gallows-Anlaut | 61 % | 83 |
| 2. Wort der Seite | 31 % | 95 |
| 1. Wort normaler Zeilen | 21 % | 1.126 |
| Gallows-Wörter am Zeilenanfang | 33 % | 138 |
| Gallows-Wörter in der Zeilenmitte | 18 % | 413 |
| Wörter in der Zeilenmitte | 17 % | 5.026 |

Die Kontrolle über den Gallows-Anlaut zeigt: Es ist nicht die Glyphenklasse, die die Einzelgänger macht, sondern die Position am Seitenanfang. Das Erstwort ist außerdem länger (Median 6 gegen 5 Zeichen) und bevorzugt andere Endungen (-or 18 %, -in 19 %; Korpus: -dy 18 %, -ey 11 %).

Im UVM-Kräuterbuch beginnt jeder Eintrag mit einer vergrößerten Schmuckinitiale (E von „Erba") und dem Pflanzennamen; die Namen sind einmalig, der Rest des Eintrags besteht aus wiederkehrendem Wortschatz. Der Voynich-Befund hat genau diese Form. Die sparsamste Lesart: Gallows-Anlaut = Initiale, Rest des Erstworts = seitenspezifische Bezeichnung.

Zwei Gegenproben fallen negativ aus und begrenzen die Lesart: Erstwörter benachbarter Seiten sind sich nicht ähnlicher als zufällige (Levenshtein 4,99 gegen 4,90, p = 0,76), während in Kräuterbüchern Paare wie „Aridian / Aridian minore" nebeneinander stehen; und die Erstwörter tauchen unter den 191 Pharma-Beschriftungen nicht überzufällig auf (11 Treffer, fast alle Allerweltswörter). Das Erstwort ist seitenspezifisch, aber kein wiederverwendeter Name.

Der Befund ist nicht auf den Kräuterteil beschränkt. Mit den 740 Absatzmarken der ZL-Umschrift liegt der Hapax-Anteil des Absatz-Erstworts bei 46 % (Kräuter A), 41 % (Kräuter B), 52 % (Sterne/Rezepte, 285 Absätze), 47 % (Badefrauen), 46 % (Pharma) und 59 % (Textseiten), gegen 11–21 % für normale Zeilenanfänge und 8–17 % für die Zeilenmitte. Nach Abzug des Gallows-Anlauts bleiben 33–43 % gegen 11–20 %. Jeder Absatz des Manuskripts beginnt mit einem Wort, das sonst kaum vorkommt.

## 6. Befund 4: Die Funktionswortschicht fehlt – auch gegen die eigene Gattung

Der Vergleich mit Dante oder Augustinus lässt sich mit dem Einwand abtun, Kräuterbücher seien eben anders geschrieben. Deshalb der Vergleich mit 13 Einträgen des UVM MS 2 (Norditalien, 15. Jh., volkssprachlich, Pflanze mit Text darunter):

| Maß | UVM MS 2 (13 Einträge) | Voynich Kräuter A (95 Seiten) |
|---|---|---|
| Wörter pro Eintrag/Seite (Median) | 69 | 75 |
| Typ/Token pro Eintrag | 0,77 | 0,83 |
| Zeilen pro Eintrag | 6 | 12 |
| Wörter pro Zeile | 13,9 | 6,1 |
| Häufigstes Wort | e, 9,2 % | daiin, 4,6 % |
| Top-10-Wörter, Anteil der Tokens | 26 % | 17 % |
| Wörter in ≥ 90 % der Einträge | e, di, in, vale | daiin |
| Festes Eintragsanfangswort | Erba (69 %) | keins (Top-5: 9 %) |
| Zeilenanfang Top-5 | 26 % | 10 % |

Umfang und Wortschatzdichte je Pflanze stimmen überein; die Gattung passt. Was fehlt, ist die Schicht der kurzen, allgegenwärtigen Wörter (und, von, in, gilt gegen) und das formelhafte „Erba". Zusammen mit der niedrigen bedingten Entropie (h2 = 2,49 bit gegen 3,1–3,3 in den Vergleichssprachen) und der Positionstreue der Glyphen im Wort (74 %) ist das die stärkste Evidenz gegen eine einfache Substitution eines europäischen Klartexts. Jede Lesart, die den Text als Sprache versteht, muss erklären, wo „und" geblieben ist.

## 7. Ausgeschlossene Hypothesen

Jede Hypothese wurde als generatives Modell oder als Vorhersage einer Kennzahl geprüft; ausgeschlossen heißt: die Vorhersage verfehlt den Messwert außerhalb des Mischfehlers.

| Hypothese | Prüfgröße | Ergebnis |
|---|---|---|
| Einfache Substitution eines europäischen Klartexts | h2, Typ/Token, Funktionswörter | h2 zu niedrig, Funktionswörter fehlen |
| Löffel-/Spielsprache (Silbeneinschub) | Entropie nach Rückbau | kein Einschub senkt h2 auf 2,49 |
| Kompression / Binärkodierung | Entropie, Zipf | Kompression erhöht Entropie, Voynich hat zu wenig |
| Steno / Abkürzungssystem | Positionstreue, Wortlängenverteilung | Positionstreue zu hoch für Kürzel |
| Verbose-/Würfelchiffre (Naibbe-Typ) | Zwillinge, Kopplung | Zwillinge zu selten, Kopplung fehlt |
| Homophon-Chiffre | Typ/Token, h2 | Typverhältnis zu hoch |
| Codebuch / Nomenklator (Wort, Stamm+Suffix) | Zipf-Steigung, Zwillinge | Zwillingsüberschuss nicht erzeugbar |
| Rugg-Gitter | Kopplung, Zwillinge | Kopplung Wortende→Anfang fehlt |
| Selbstzitat (ein Autor erfindet beim Schreiben) | Rate je Schreiberhand | drei Hände, gleiche Rate |
| Silbenschrift (Chinesisch, Vietnamesisch) | h2, Typ/Token | Pinyin trifft h2, verfehlt Typ/Token |
| Agglutinierend (Finnisch, Ungarisch) | Suffix-Statistik, Geschichte | passt nicht, historisch unmöglich |
| Zahlen-/Listenkodierung | Zipf, Wiederholungsmuster | Zipf-Steigung falsch |
| Llull-Kombinatorik | Kombinationsraum vs. Typen | Typenzahl zu hoch |
| Leetspeak / optische Mehrglyphen | Entropie nach Zusammenfassung | kein Gewinn |
| Spiegelschrift | alle Maße (richtungssymmetrisch) | ohne Effekt |
| f57v-Ring als Alphabetschlüssel | Abdeckung der Glyphen | nur 48 % der Textglyphen |
| Magische Formeln / Charms | Tripel, Formelwörter | 8 Tripel, keine Formelanfänge |
| Fortlaufende Verschiebung pro Wort | Glyphenverteilung, Periode, Zwillinge | Verteilung bliebe schief, keine Periode bis 45, Zwillinge nicht erzeugbar |

Nicht ausgeschlossen: ein Bausteinstrom (Markov über BPE-Blöcke) mit etwa 15 % Abschreiben-mit-Veränderung; er reproduziert alle neun Kennzahlen am besten (Verlust 2,6 gegen 4–9 bei den übrigen). Er ist ein Erzeugungsmodell, kein Lesemodell.

## 8. Diskussion

Die vier Befunde ziehen in dieselbe Richtung: Der Text wurde mit Blick auf die Bilder erzeugt (Befund 1), von mehreren Händen nach demselben Verfahren und wahrscheinlich nach einer Vorlage (Befund 2), mit einer Struktur, die das Genre Kräuterbuch nachbildet (Befund 3), aber ohne die Grammatik einer Sprache (Befund 4). Das ist weder Klartext noch Zufall, sondern ein Verfahren.

Welches Verfahren, bleibt offen. Drei Lesarten sind mit allen vier Befunden vereinbar: (a) eine Verschlüsselung, die Funktionswörter tilgt oder in die Glyphenstruktur verschiebt (dann müsste die Positionstreue von 74 % Teil des Schlüssels sein); (b) ein konstruiertes System ohne sprachlichen Inhalt, das nach Vorlage und Bild kontrolliert erzeugt wurde – eine Werkstattarbeit, kein Serafini; (c) eine Mischung, in der Namen und Beschriftungen Inhalt tragen und der Fließtext Füllung ist. Lesart (c) würde erklären, warum Erstwörter seitenspezifisch sind, aber nicht, warum sie dieselbe Bausteingrammatik haben wie der Rest.

Das alchemistische Kräuterbuch (Segre Rutz: 98 Kapitel, Norditalien, Wurzelfokus, Frauenheilkunde als Anhang) und das UVM-Kräuterbuch liefern den bisher besten Rahmen für Bildprogramm und Seitenaufbau. Ein Namenstest gegen die 98 Oxford-Kapitel in Folio-Reihenfolge scheitert (r = 0,07); die Lagenordnung und die Vorlagenfrage sind vor einem zweiten Versuch zu klären.

Offen und prüfbar: ob die chol-Familie an bestimmten Zeilenpositionen den Wurzel-Effekt trägt; ob eine vollständige Transkription des UVM MS 2 (142 Seiten) die Funktionswort-Lücke quantitativ schärft; ob ein dritter, menschlicher Bewerter den Bild-Text-Effekt bestätigt.

## 9. Grenzen

- Die Bildmerkmale wurden von zwei Sprachmodellen bewertet, nicht von Botanikern; Kappa zwischen beiden ist moderat, der Effekt überlebt die Einschränkung auf Konsensseiten, aber eine menschliche Drittbewertung steht aus.
- Die UVM-Transkription umfasst 13 Einträge (≈ 900 Wörter) aus eigener Lesung einer Kursive des 15. Jh.; einzelne Wörter sind unsicher, die Zählmaße sind dagegen robust. Für Entropiemaße ist der Umfang zu klein.
- EVA ist eine Transliteration, keine Glyphendefinition; die Zusammenfassung von Glyphenbündeln beeinflusst h2 um bis zu 0,2 bit. Die Replikation mit Takahashi mindert, aber beseitigt das Problem nicht.
- Permutationstests setzen Austauschbarkeit der Seiten voraus; Lagen- und Schreiberwechsel können Cluster erzeugen. Der Schreiber-Split in Befund 2 ist zugleich die Kontrolle dafür.
- Alle Ergebnisse gelten für den Fließtext; Beschriftungen, Sternen- und Badefrauenteil wurden nur stichprobenartig geprüft.
- Keine der Analysen liest ein Wort. Was ausgeschlossen ist, ist belegt; was übrig bleibt, ist nicht bewiesen.

## 10. Reproduzierbarkeit und Quellen

Skripte (Python, ohne Abhängigkeiten außer Standardbibliothek und PIL), Bildbewertungen (feats.txt, feats_kimi.txt, feats_rep.txt), die UVM-Transkription (uvm_entries.txt), die Astrolabium-Planum-Gradtexte (ap_aries.txt, ap_pisces.txt) und die 98 Kapitelnamen (alch98.txt) liegen in diesem Repository. Die Rohonc-Transkription (Király/Tokai) wurde über die API von rechnitzer-kodex.hu bezogen und wird nicht weiterverbreitet.

- Zandbergen, R.: ZL3b-n Transliteration, voynich.nu
- Takahashi, T.: IT2a Transliteration (über voynich.nu)
- Davis, L. F. (2020): How Many Glyphs and How Many Scribes? Manuscript Studies 5.1
- Timm, T. & Schinner, A. (2020): A possible generating algorithm of the Voynich manuscript. Cryptologia 44
- Rugg, G. (2004): An elegant hoax? Cryptologia 28
- Segre Rutz, V. (2000): Il giardino magico degli alchimisti. Mailand
- Gottlieb, S.: Already Verified. In: Drugs in the Medieval Mediterranean, Cambridge UP
- Neal, P.: Voynich Sources – Alchemical herbals, philipneal.net
- Reeds, K. (2012): Saint John's Wort in the Age of Paracelsus. In: Herbs and Healers from the Ancient Mediterranean through the Medieval West, Ashgate, Kap. 9
- Oxford, Bodleian MS. Canon. Misc. 408, Digital Bodleian
- Burlington, University of Vermont, MS 2 (Italian Herbal), UVM Digital Collections
- Angelus, J.: Astrolabium planum in tabulis ascendens, Augsburg 1488, BSB bsb00026866
- Király, L. & Tokai, G.: Rohonc-Codex-Transkription, rechnitzer-kodex.hu

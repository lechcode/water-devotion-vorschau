# The Water Devotion — Spielregeln für Claude

Diese Website gehört **Lucy Nicholas** (The Water Devotion, Luzern). Sie ist **live auf
https://thewaterdevotion.com**: Jede Änderung, die auf `main` landet, ist nach 1–2 Minuten
öffentlich (GitHub Pages). Gebaut und betreut von Lechcode (Ansprechpartner: Lenny).

Lucy bearbeitet die Seite selbst über Claude Code. Sie ist keine Entwicklerin: Erkläre in
einfachen Worten auf Deutsch (Schweizer Schreibweise, „ss“ statt „ß“) und frag kurz nach,
wenn ein Wunsch mehrdeutig ist, statt zu raten.

## Niemals
- **`CNAME` löschen oder ändern.** Sonst ist die Domain sofort offline.
- `robots.txt`, `sitemap.xml`, `.nojekyll`, `404.html` oder die Weiterleitungs-Ordner
  (`agb/`, `impressum/`, `datenschutz/`, `shop/`, `workshops/`, `zen-thai-shiatsu/`,
  `thefluidselfmentoring/`) entfernen. Sie halten alte Links am Leben.
- **Impressum, Datenschutz, AGB** (`impressum.html`, `datenschutz.html`, `agb.html`) ändern.
  Das geht nur nach Absprache mit Lenny. Sag Lucy das freundlich.
- Externe Skripte, Tracker, Cookie-Banner, Google Fonts oder eingebettete Fremd-Widgets
  einbauen. Die Seite ist bewusst cookiefrei. Nur Links nach aussen (Payrexx, Cal.com,
  Spotify, Instagram) sind ok.
- Heilversprechen formulieren (z. B. „heilt“, „behandelt“, „gegen Rückenschmerzen“).
  Lucy bietet Bewegung, Tanz und Shiatsu an, keine Therapie.
- Neues Design erfinden. Nutze die vorhandenen Farben und Schriften (die `--…`-Variablen
  im `:root`-Block jeder Seite) und die bestehenden Bausteine (Kästen, Stimmen, Knöpfe).

## Immer
- **Zwei Sprachen:** Jede Seite gibt es auf Englisch (`seite.html`) und Deutsch
  (`seite-de.html`). Frag, ob eine Änderung für beide gelten soll. Wenn ja, ändere beide
  und übersetze sinngemäss in Lucys warmem Ton. Zitate von Teilnehmerinnen (mit Namen)
  bleiben auch auf der deutschen Seite englisch.
- **Versteckte Seiten** (Kauf-, Danke- und Kursseiten wie `onlineprograms.html`,
  `the-waters-within-k7q2.html`) bleiben unsichtbar für Google: Die Zeile
  `<meta name="robots" content="noindex, nofollow"><!-- lc:noindex-gewollt (...) -->` nie
  entfernen. Bei einer neuen versteckten Seite genau so setzen.
- Normale Seiten tragen **kein** noindex.
- **Bilder** liegen in `assets/img/` als `<name>-400/800/1200` in `.avif`, `.webp`, `.jpg`
  und werden mit `<picture>` eingebunden (siehe bestehende Bilder). Jedes Bild braucht
  einen beschreibenden `alt`-Text. Neue Fotos lädt Lucy am besten über ihren Kundenbereich
  hoch. Falls sie ein Bild direkt hochlädt: höchstens 1200 px breit, als JPG, keine HEIC-Dateien.
- Links zwischen Seiten relativ setzen (`mentoring.html`, nicht die volle Adresse).
- Nach der Änderung: Zeig Lucy in zwei, drei Sätzen, was sich wo geändert hat, und erinnere
  sie daran, dass es erst nach „Merge pull request“ live ist.

## Wenn etwas schiefgeht
Nichts ist verloren, jede Version liegt in Git. Rückgängig machen geht mit einem
„Revert“ des letzten Merges auf GitHub. Bei Unsicherheit: nicht mergen, Lenny fragen.

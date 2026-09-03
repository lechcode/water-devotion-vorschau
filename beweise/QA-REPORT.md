# QA-Report: water-devotion

**Gesamtampel: 🟡 GELB** · 0 rot / 7 gelb / 9 grün · 03.09.2026 16:47 · Dauer 75 s · lc-qa.py

## 5-Minuten-Abnahme (Mensch)
1. Alle 🔴 unten abgearbeitet? 2. Screenshots in `qa-shots/` überflogen — „würde ich das verschicken?"
3. ROT-Assets in ASSETS-LIZENZEN.md ok für Vorschau? 4. MAIL-KUNDE/VERSAND-NACHRICHT gelesen? 5. Link einmal am eigenen Handy antippen.

## 🔴 ROT (Blocker)
- —

## 🟡 GELB (prüfen/dokumentieren)
- **OG-Tags mein-bereich.html**: fehlt: og:title, og:description, og:image
- **OG-Tags onboarding.html**: fehlt: og:title, og:description, og:image
- **Gesamt-Bildgewicht**: 7456 KB über alle Bilder (Budget je Seite 800 KB — prüfen, was index.html wirklich lädt)
- **impressum.html nicht verlinkt von**: mein-bereich.html, onboarding.html
- **datenschutz.html nicht verlinkt von**: mein-bereich.html, onboarding.html
- **NAP: Straßen-Varianten**: Kosthausstrasse 10 | Nidfeldstrasse 1
- **iOS-Zoom mein-bereich.html**: 1 Eingabefeld(er) mit font-size < 16px

## 🟢 GRÜN
- **Interne Links & Assets**: alle Verweise in 9 Seiten existieren
- **Externe Requests**: keine (cookiefrei/0 Tracker bestätigt)
- **OG-Tags**: index/vorschau vollständig
- **Grep-Fallen & noindex**: clamp/calc sauber, noindex gesetzt
- **Bild-Budget**: kein Einzelbild > 250 KB
- **Lighthouse Performance (mobil)**: 100 (Budget ≥ 95)
- **Lighthouse A11y**: 100 (Ziel 100; 90–99 = Hinweis, < 90 blockt)
- **LCP**: 1.73 s (Budget < 2 s)
- **Playwright-Screenshots**: 9 Seiten × 3 Breiten → qa-shots/

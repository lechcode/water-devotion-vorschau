# QA-Report: water-devotion

**Gesamtampel: 🟡 GELB** · 0 rot / 2 gelb / 9 grün · 03.09.2026 15:48 · Dauer 64 s · lc-qa.py

## 5-Minuten-Abnahme (Mensch)
1. Alle 🔴 unten abgearbeitet? 2. Screenshots in `qa-shots/` überflogen — „würde ich das verschicken?"
3. ROT-Assets in ASSETS-LIZENZEN.md ok für Vorschau? 4. MAIL-KUNDE/VERSAND-NACHRICHT gelesen? 5. Link einmal am eigenen Handy antippen.

## 🔴 ROT (Blocker)
- —

## 🟡 GELB (prüfen/dokumentieren)
- **Gesamt-Bildgewicht**: 7453 KB über alle Bilder (Budget je Seite 800 KB — prüfen, was index.html wirklich lädt)
- **NAP: Straßen-Varianten**: Kosthausstrasse 10 | Nidfeldstrasse 1

## 🟢 GRÜN
- **Interne Links & Assets**: alle Verweise in 7 Seiten existieren
- **Externe Requests**: keine (cookiefrei/0 Tracker bestätigt)
- **OG-Tags**: index/vorschau vollständig
- **Grep-Fallen & noindex**: clamp/calc sauber, noindex gesetzt
- **Bild-Budget**: kein Einzelbild > 250 KB
- **Lighthouse Performance (mobil)**: 100 (Budget ≥ 95)
- **Lighthouse A11y**: 100 (Ziel 100; 90–99 = Hinweis, < 90 blockt)
- **LCP**: 1.66 s (Budget < 2 s)
- **Playwright-Screenshots**: 7 Seiten × 3 Breiten → qa-shots/

# QA-CHECKLISTE · water-devotion (Phase 6, 03.09.2026)

## Maschinell (lc-qa.sh, Lauf 1 — vor vorschau.html)
Gesamtampel 🟡 GELB · **0 rot** / 6 gelb / 9 grün → Report: `beweise/QA-REPORT.md`.
GELB-Begründungen:
- OG-Tags impressum/datenschutz: Rechtsseiten werden nie geteilt (lt. Regelwerk nur GELB) — belassen.
- „Gesamt-Bildgewicht 7 MB": Summe ALLER Formate/Breiten im assets/img-Ordner. Real lädt index 247 KiB (Lighthouse total-byte-weight) — Budget eingehalten.
- Querverlinkung Impressum↔Datenschutz: **gefixt** (Lauf 2 prüft).
- NAP-Straßen-Varianten: zwei Rollen (Sitz Kosthausstrasse vs. Studio Nidfeldstrasse), dokumentiert in NAP-QUELLEN.md — kein Konflikt.

## Menschliches Urteil
1. **Fakten-Abgleich:** Preise (CHF 50/110/190/135–400/210–400/320/150/420/2×210/155/175/499), Termine (05.09., 10.–11.10.), Adressen, Mail, IG gegen INVENTAR.md geprüft ✓. Termin 05.09. = heute → Frage an Lucy (OFFENE-FRAGEN).
2. **Formular:** keins verbaut (bewusst — Buchung via Payrexx-Demo/WhatsApp/mailto wie Altseite) ✓.
3. **A11y:** Lighthouse 100; Skip-Link, ein h1/Seite, Labels n/a, Fokus sichtbar (Token-Outline), reduced-motion-Fallback in CSS+JS ✓.
4. **Recht:** DEMO-Platzhalter-Rechtsseiten mit Hinweis; HWG/HMG-Entschärfungen dokumentiert (TEXT-DELTA D1–D5); kein OS-Link; keine Cookies ✓.
5. **Lesedurchgang:** EN konsistent „you", DE nur Rechtsseiten/Demo-Hinweis; Schreibweisen einheitlich ✓.
6. **Performance-Gate:** Perf 100 · A11y 100 · LCP 1,65–1,7 s · CLS 0 · TBT 0 ms · 247 KiB ✓ (SEO 66 = noindex, gewollt).
7. **Hero-Check:** 390 px + Desktop gerendert (fold-Shots): H1/CTA frei vom Motiv (Hände rechts, Text links), heller Text auf Dual-Scrim (dunkelste Zone), H1+Lead+beide CTAs im ersten Viewport ✓.
8. **Eigenständigkeit (DESIGN-LOG):** Schrift (Instrument Serif+Outfit, beide erstmalig) ✓ · Palette (Teal/Aqua, erstmalig) ✓ · Hero (Vollbild-Wasser ohne Gesicht vs. Diptychon/Typo-Leerfeld/Portal) ✓ · Rhythmus (Tauchgänge + Wellen) ✓ → 4/4 anders.

## Slider-Funktionsbeleg (vorschau.html)
Playwright-Klick bei 70 % → `clip-path: inset(0px 30% 0px 0px)` ✓ · 0 Konsolenfehler.

## Lauf 2 (nach Fix-Runde) — Ergebnis unten nachtragen

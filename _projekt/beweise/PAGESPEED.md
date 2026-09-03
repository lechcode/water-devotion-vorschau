# PAGESPEED · water-devotion

## Vorher (thewaterdevotion.com, live)
Methode: npx lighthouse, headless Chrome, mobil-Emulation, 1 Lauf (03.09.2026). JSON: `lh-alt-mobil.json`.
| Metrik | Wert |
|---|---|
| Performance (mobil) | **63** |
| Accessibility | 88 |
| SEO | 92 |
| FCP | 3,2 s |
| LCP | **8,2 s** |
| Speed Index | 7,0 s |
| CLS | 0 |
| Seitengewicht | **1.482 KiB** |

## Nachher (lokal, python http.server — kostet erfahrungsgemäß 2–5 Punkte ggü. echtem Hosting; noindex drückt SEO gewollt)
Methode: identisch (npx lighthouse, mobil, localhost:8742), 03.09.2026. JSON: `lh-neu-mobil.json`. lc-qa-Zweitlauf bestätigt (Perf 100, LCP 1,65 s).
| Metrik | alt | neu |
|---|---|---|
| Performance (mobil) | 63 | **100** |
| A11y | 88 | **100** |
| LCP | 8,2 s | **1,7 s** (≈ 5× schneller) |
| FCP | 3,2 s | 1,2 s |
| Speed Index | 7,0 s | 1,2 s |
| Seitengewicht | 1.482 KiB | **247 KiB** (6× leichter) |
| Requests | ~50+ (WP/Divi/Woo) | **11** |
| Cookies/Tracker | WP-Cookies | **0 / 0** |

**Tacho-Satz:** „Vorher brauchte das größte Element 8,2 Sekunden, jetzt 1,7 — fast fünfmal schneller, bei einem Sechstel des Gewichts."
(SEO-Score neu 66 = gewollt: noindex der Vorschau drückt ihn.)

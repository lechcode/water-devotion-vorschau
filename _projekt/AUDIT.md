# AUDIT · water-devotion (03.09.2026)

Befunde mit Evidenz — als Verkaufsargumente formulierbar:

1. **Schwere Technik-Last:** WordPress + Divi 4.27 + WooCommerce + jQuery; Startseiten-HTML allein 172 KB vor Assets; et-cache-CSS-Ketten. → Ladezeit & Pflegeaufwand (Plugin-/Sicherheitsupdates, Divi-Lizenz). *Evidenz: Generator-Tag „Divi v.4.27.4", alt-archiv.*
2. **Layout altbacken (O-Ton der Kundin):** zentrierte Divi-Boxen auf Vollflächen-Teal, kleine Buttons, enge Text-Container. *Evidenz: beweise/vorher-desktop.png.*
3. **Bild-Formatierung inkonsistent:** Hoch-/Quer-/Insta-Formate gemischt, B&W neben Farbe ohne System, Karten-Crops uneinheitlich. *Evidenz: vorher-desktop.png (Offerings-Reihe), ALT-ASSETS.md.*
4. **XML-RPC offen** (`xmlrpc.php` verlinkt) — bekanntes Angriffs-/Bruteforce-Ziel bei WordPress. *Evidenz: index.html Head.*
5. **WooCommerce-Overhead für 10 Ticket-Produkte:** Warenkorb/Kasse/Mein-Konto-Maschinerie für einfache Event-Tickets; Zahlung ohnehin via Payrexx. → Paylink-Ansatz spart das komplette Shop-Backend. *Evidenz: /shop/, /kasse/ (Payrexx/TWINT).*
6. **`<title>` der Startseite unvollständig:** „The Water Devotion |" (endet mit Pipe, kein Claim/Ort); keine Meta-Description erkennbar. *Evidenz: index.html.*
7. **Blog-Reste sichtbar:** Shop-Sidebar zeigt „Hello world!"-Beitrag + „A WordPress Commenter". Wirkt unfertig. *Evidenz: shop.html.*
8. **Shop-UI deutsch, Inhalt englisch** („Ergebnisse 1–9 von 10 werden angezeigt" mitten in EN-Seite) — Sprachbruch. *Evidenz: shop.html.*
9. **Impressum minimal** (Name/Adresse/Mail) — für CH ok (kein DDG), aber keine Datenschutzerklärung gefunden (AGB §10 verweist auf „separate Datenschutzerklärung", die nicht verlinkt/auffindbar ist). *Evidenz: impressum.html, agb.html.* → Bei Payrexx/Newsletter DSG/DSGVO-relevant.
10. **Indexierung:** Seite ist live und indexierbar (kein noindex); Rankings nicht geprüft (DEMO). Bei Umzug URL-Pfade konservativ behandeln.

**Positiv (behalten):** starke Profi-Fotografie, klare Farbwelt, poetische, eigene Texte, echte Testimonials, klare Angebotsstruktur.

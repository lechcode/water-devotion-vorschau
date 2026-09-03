#!/usr/bin/env python3
# Baut mentoring/workshops/shiatsu aus dem index-Grundgerüst (Tokens/Nav/Footer identisch).
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
idx = (root/'index.html').read_text()

style = re.search(r'<style>.*?</style>', idx, re.S).group(0)
nav = re.search(r'<header class="nav".*?</header>', idx, re.S).group(0)
footer = re.search(r'<footer class="site-footer">.*?</footer>', idx, re.S).group(0)
script = re.search(r'<script>\n\(function.*?</script>', idx, re.S).group(0)
favicon = re.search(r'<link rel="icon"[^>]*>', idx).group(0)

EXTRA_CSS = """
<style>
/* Unterseiten */
.subhero{background:var(--tiefe);color:#fff;padding:calc(var(--s6) + 3rem) 0 var(--s5)}
.subhero-grid{display:grid;grid-template-columns:1.15fr .85fr;gap:clamp(2rem,5vw,5rem);align-items:center}
.subhero .eyebrow{color:var(--akzent-d);margin-bottom:var(--s2)}
.subhero h1{font-size:var(--fs-4);text-wrap:balance}
.subhero h1 em{color:var(--akzent-d)}
.subhero .lead{font-size:var(--fs-2);margin-top:var(--s3);max-width:46ch;color:var(--aqua-hell)}
.subhero-figur{max-width:420px;justify-self:end;width:100%}
.subhero-figur figure{aspect-ratio:4/5;overflow:hidden;border-radius:var(--radius)}
.subhero-figur img{width:100%;height:100%;object-fit:cover}
.subhero-cta{margin-top:var(--s3);display:flex;flex-wrap:wrap;gap:.9rem}
@media (max-width: 900px){.subhero-grid{grid-template-columns:1fr}.subhero-figur{max-width:300px;justify-self:start}}
.prosa{max-width:62ch}
.prosa p{margin-bottom:var(--s2)}
.prosa strong{font-weight:500}
.trio{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(1.2rem,2.5vw,2rem);margin-top:var(--s4)}
.trio p{font-family:var(--serif);font-size:var(--fs-2);line-height:1.3;border-top:2px solid var(--akzent);padding-top:var(--s2)}
.dunkel .trio p{border-top-color:var(--akzent-d)}
@media (max-width: 900px){.trio{grid-template-columns:1fr}}
.checkliste{display:grid;grid-template-columns:1fr 1fr;gap:.9rem clamp(1.4rem,3vw,2.6rem);list-style:none;margin-top:var(--s3)}
.checkliste li{display:flex;gap:.8rem;align-items:flex-start}
.checkliste svg{flex:0 0 auto;margin-top:.45rem}
@media (max-width: 720px){.checkliste{grid-template-columns:1fr}}
.band{display:flex;flex-wrap:wrap;gap:.7rem;margin-top:var(--s3)}
.band span{border:1px solid var(--akzent);color:var(--akzent);border-radius:999px;padding:.5rem 1.1rem;font-size:var(--fs-0);letter-spacing:.05em}
.dunkel .band span{border-color:rgba(207,232,230,.5);color:var(--akzent-d)}
/* Ticket-Karten */
.tickets{display:grid;grid-template-columns:1fr 1fr;gap:clamp(1.2rem,2.5vw,2rem)}
.ticket{background:var(--papier);border-radius:var(--radius);padding:var(--s3);display:flex;flex-direction:column;gap:.9rem;box-shadow:0 6px 30px rgba(30,50,52,.08)}
.ticket-kopf{display:flex;justify-content:space-between;align-items:flex-start;gap:1rem;flex-wrap:wrap}
.ticket .datum{font-family:var(--serif);font-size:var(--fs-2);color:var(--akzent)}
.ticket .preis{font-weight:500;background:var(--aqua);border-radius:999px;padding:.45rem 1rem;font-size:var(--fs-0);white-space:nowrap}
.ticket h3{font-size:var(--fs-2)}
.ticket .meta{font-size:var(--fs-0);letter-spacing:.08em;text-transform:uppercase;color:var(--akzent)}
.ticket p.beschr{flex:1}
.ticket .spots{font-size:var(--fs-0);color:var(--akzent);letter-spacing:.12em}
.ticket-fuss{display:flex;flex-wrap:wrap;gap:.7rem;align-items:center}
.demo-hinweis{font-size:.82rem;color:var(--flaeche);opacity:.85;margin-top:.4rem}
@media (max-width: 900px){.tickets{grid-template-columns:1fr}}
/* Treatment-Karten */
.behandlungen{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(1.2rem,2.5vw,2rem)}
.behandlung{background:var(--aqua-hell);border-radius:var(--radius);padding:var(--s3);display:flex;flex-direction:column;gap:.9rem}
.behandlung .dauer{font-family:var(--serif);font-size:var(--fs-3);line-height:1}
.behandlung .preis-zeile{font-weight:500;color:var(--akzent);letter-spacing:.06em}
.behandlung ul{list-style:none;flex:1;display:flex;flex-direction:column;gap:.55rem}
.behandlung li{padding-left:1.3rem;position:relative}
.behandlung li::before{content:"";position:absolute;left:0;top:.62em;width:14px;height:6px;border-radius:99px;background:var(--akzent);opacity:.45}
@media (max-width: 900px){.behandlungen{grid-template-columns:1fr}}
.kleingedruckt{font-size:.85rem;opacity:.75;margin-top:var(--s2)}
.band-figur img{width:100%;height:100%;object-fit:cover;object-position:50% 68%}
.schluss-cta{text-align:center}
.schluss-cta h2{font-size:var(--fs-3);margin-bottom:var(--s2)}
.schluss-cta p{max-width:52ch;margin:0 auto var(--s3)}
</style>
"""

def kopf(title, desc, slug):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>document.documentElement.classList.add('js')</script>
<meta name="robots" content="noindex, nofollow"><!-- ENTFERNEN sobald Impressum+Datenschutz live & freigegeben -->
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_US">
<meta property="og:url" content="https://lechcode.github.io/water-devotion-vorschau/{slug}.html"><!-- bei Go-Live auf echte Domain -->
<meta property="og:image" content="https://lechcode.github.io/water-devotion-vorschau/assets/og.jpg"><!-- bei Go-Live auf echte Domain -->
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="theme-color" content="#24494C">
{favicon}
<link rel="preload" href="assets/fonts/playfair-display-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/outfit-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/fonts.css">
{style}
{EXTRA_CSS}
</head>
<body>
<a class="skip" href="#inhalt">Skip to content</a>
{nav}
<main id="inhalt">
"""

FUSS = "\n</main>\n" + footer + "\n" + script + "\n</body>\n</html>\n"

def bild(name, sizes, w, h, alt, breiten=(400,800,1200), lazy=True):
    def srcset(ext):
        return ", ".join(f"assets/img/{name}-{b}.{ext} {b}w" for b in breiten)
    l = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    mid = breiten[min(1,len(breiten)-1)]
    return f"""<picture>
  <source type="image/avif" srcset="{srcset('avif')}" sizes="{sizes}">
  <source type="image/webp" srcset="{srcset('webp')}" sizes="{sizes}">
  <img src="assets/img/{name}-{mid}.jpg" srcset="{srcset('jpg')}" sizes="{sizes}" width="{w}" height="{h}" alt="{alt}"{l}>
</picture>"""

WELLE = '<svg class="treiben" width="140" height="30" viewBox="0 0 140 30" aria-hidden="true"><path d="M6 15c11-13 22-13 33 0s22 13 33 0 22-13 33 0 18 10 29 4" stroke="#CFE8E6" stroke-width="2.5" fill="none" stroke-linecap="round" opacity=".85"/></svg>'
HAKEN = '<svg width="16" height="12" viewBox="0 0 16 12" aria-hidden="true"><path d="M1 6.5 5.5 11 15 1" stroke="#2E6A6E" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def stimmen(liste):
    karten = "\n".join(
        f'        <div class="stimme reveal">\n          <p>&bdquo;{t}&ldquo;</p>\n          <footer>{n}</footer>\n        </div>' for t,n in liste)
    return f"""  <section>
    <div class="wrap">
      <div class="sek-kopf reveal">
        <p class="eyebrow">Voices from the practice</p>
        <h2>What practitioners <em>feel</em></h2>
      </div>
      <div class="stimmen">
{karten}
      </div>
    </div>
  </section>
"""

def schluss_cta(h2, p, btns):
    b = "\n        ".join(btns)
    return f"""  <section class="aqua schluss-cta">
    <div class="wrap reveal">
      <h2>{h2}</h2>
      <p>{p}</p>
      <div class="hero-cta" style="justify-content:center">
        {b}
      </div>
    </div>
  </section>
"""

MAILTO = 'mailto:lucy@thewaterdevotion.com?subject=Discovery%20Call'

# ================= MENTORING =================
m = kopf("1:1 Dance Mentoring in Lucerne | The Water Devotion",
         "The Fluid Self: 1:1 dance mentoring online or in Lucerne. Soft, intuitive work with body awareness, freestyle and expression. Book a free discovery call.",
         "mentoring")
m += f"""
  <section class="subhero">
    <div class="wrap subhero-grid">
      <div>
        <p class="eyebrow">1:1 · online or in Lucerne</p>
        <h1>The Fluid Self — 1:1 <em>Mentoring</em></h1>
        <p class="lead">A space for fluid dance, mindful presence and embodied transformation.</p>
        <div class="subhero-cta">
          <a class="btn btn-voll" href="{MAILTO}">Book your free discovery call</a>
        </div>
      </div>
      <div class="subhero-figur">
        <figure>{bild('card-mentoring','(max-width: 900px) 76vw, 32vw',1365,2048,'Lucy lifting water in her hands at the lake')}</figure>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="prosa reveal">
        <p>You ever wondered what's underneath the surface? Underneath your longing for expression, underneath your own way of moving? You ever wondered how it feels to embrace the fluidity in your body and in your rhythm of life?</p>
        <p><strong>I invite you to go on a journey within.</strong></p>
        <p>Exploring layers you meet every day but were never truly able to touch. A space of slowing down — to listen to your body, your breath and what wants to move through you.</p>
        <p>Expression takes courage and patience. That's why we work with soft, intuitive methods, tailored to you and your body. The pressure to perform is invited to leave. Your dance becomes softer, rounder, more authentic. And slowly, a deep trust in your inner flow begins to unfold.</p>
        <p><strong>You will grow braver in being seen, in your dance, and in your life.</strong></p>
      </div>
      <div class="trio reveal">
        <p>Unfold your inner flow</p>
        <p>Feel empowered in your authentic body</p>
        <p>Surrender to the softness of freedom — beyond achievement</p>
      </div>
    </div>
  </section>

  <section class="aqua-hell">
    <div class="wrap">
      <div class="sek-kopf reveal">
        <p class="eyebrow">What awaits you</p>
        <h2>More flow, more ease, <em>more you</em></h2>
      </div>
      <ul class="checkliste reveal">
        <li>{HAKEN}<span>Personalized 1:1 sessions — online or in Lucerne</span></li>
        <li>{HAKEN}<span>Deepening your body awareness, emotional presence, technique and freestyle</span></li>
        <li>{HAKEN}<span>ZenThai Shiatsu bodywork session (in person only)</span></li>
        <li>{HAKEN}<span>Personalized movement rituals to support you between sessions</span></li>
        <li>{HAKEN}<span>Practice sheets (PDFs) with guidance and reflections</span></li>
        <li>{HAKEN}<span>Curated music playlists to help you drop in</span></li>
        <li>{HAKEN}<span>Online support — for your questions and thoughts</span></li>
        <li>{HAKEN}<span>A community devoted to the waters within</span></li>
      </ul>
      <p class="reveal" style="margin-top:var(--s3);max-width:62ch">For everyone who wants to rediscover themselves in dance and longs to feel strong in their softness. Perfect if you are seeking more lightness, authenticity and self-confidence.</p>
    </div>
  </section>

  <section class="zitat">
    <div class="wrap reveal">
      {WELLE}
      <blockquote style="font-size:var(--fs-2)">&bdquo;Water does not resist. Water flows. When you plunge your hand into it, all you feel is a caress. Water is not a solid wall, it will not stop you. But water always goes where it wants to go, and nothing in the end can stand against it. Water is patient. Dripping water wears away a stone. Remember you are half water. If you can't go through an obstacle, go around it. Water does.&ldquo;
        <cite>Margaret Atwood</cite>
      </blockquote>
    </div>
  </section>

{stimmen([
 ("I was able to learn so much. My expression has opened deeply, and I feel much more connected to my body, to myself. For me, this experience went far beyond dancing. Lucy has an incredibly empathetic and beautiful way of holding and guiding space.","Janine · TWD Practitioner"),
 ("This journey has once again reminded me how deep my passion for dance truly is, and how much I want to nurture and expand my practice. I'm also taking with me the knowing that there are always spaces where connection can be found.","Milena · TWD Practitioner"),
 ("Completely out of comfort — I dived into The Fluid Self Dance Mentoring for three months. Three months of depth, touch, exploring, expanding, integrating and becoming myself. Step by step. […] That was just the beginning.","Kathi · 1:1 Mentoring"),
])}
{schluss_cta("Embark on the <em>journey</em>",
 "Book your free discovery call now to dive into your sweet unfolding.",
 [f'<a class="btn btn-tinte" href="{MAILTO}">Book your free discovery call</a>'])}
"""
m += FUSS

# ================= WORKSHOPS =================
DEMO_HINWEIS = '<p class="demo-hinweis">Demo — im Live-Betrieb öffnet hier deine Payrexx-Bezahlseite (TWINT, Karte&nbsp;…).</p>'
def ticket(datum, titel, meta, text, preis, spots=True, extra_btn=None):
    fuss = f'<a class="btn btn-tline payrexx-demo" href="#payrexx-demo">More information &amp; registration</a>'
    if extra_btn: fuss += f'\n        <a class="btn btn-tline payrexx-demo" href="#payrexx-demo">{extra_btn}</a>'
    s = f'<p class="spots">— Limited spots —</p>' if spots else ''
    meta_html = f'<p class="meta">{meta}</p>' if meta else ''
    return f"""        <article class="ticket reveal">
          <div class="ticket-kopf"><span class="datum">{datum}</span><span class="preis">{preis}</span></div>
          <h3>{titel}</h3>
          {meta_html}
          <p class="beschr">{text}</p>
          {s}
          <div class="ticket-fuss">
        {fuss}
          </div>
          {DEMO_HINWEIS}
        </article>"""

w = kopf("Dance Workshops in Lucerne | The Water Devotion",
         "Workshops and dance journeys in Lucerne: fluid movement, contact improvisation and choreographic landscapes. See the next dates and join the community.",
         "workshops")
w += f"""
  <section class="subhero">
    <div class="wrap subhero-grid">
      <div>
        <p class="eyebrow">Live in Lucerne &amp; online</p>
        <h1>Workshops &amp; Dance <em>Journeys</em></h1>
        <p class="lead">Become part of a community devoted to the waters within.</p>
        <div class="subhero-cta">
          <a class="btn btn-voll" href="#dates">See the next dates</a>
        </div>
      </div>
      <div class="subhero-figur">
        <figure>{bild('workshops-dance','(max-width: 900px) 76vw, 32vw',1365,2048,'A dancer moving freely in the meadow')}</figure>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="prosa reveal">
        <p><strong>The Water Devotion</strong> is here to welcome parts of you that are yet to be explored. A place where we dive into active relaxation, learning to trust and to surrender to an ever unfolding flow — deepening body awareness and fine-tuning movement technique.</p>
        <p>Through symbolism and contact improvisation we explore a world of endless possibilities and awaken our source of inspiration from within. In choreographic landscapes we make a choreo our own, meeting in the rhythm between tension and release, in softness, in clarity, in devotion.</p>
        <p>An invitation to return — to your body, to fluidity, to the inner tides that guide you. Diving into a space where creativity finds its way through us.</p>
      </div>
      <div class="band reveal">
        <span>Fluid movement concepts</span><span>Partnerwork &amp; contact impro</span><span>Explorative dance journey</span><span>Freestyle enhancement</span><span>Choreographic landscapes</span><span>Body awareness</span><span>Togetherness</span>
      </div>
    </div>
  </section>

  <section class="aqua" style="padding:0">
    <figure class="reveal band-figur" style="margin:0;height:min(64vh,560px);overflow:hidden">
      {bild('workshops-room','100vw',2048,1363,'A Water Devotion workshop — the group moving together',(400,800,1200))}
    </figure>
  </section>
  <section style="padding-top:var(--s4);padding-bottom:0">
    <div class="wrap"><p class="reveal" style="max-width:60ch;font-family:var(--serif);font-size:var(--fs-2);line-height:1.4">This is what the waters look like when we share them — <em class="em">the presence, the people, and the practice.</em></p></div>
  </section>

  <section class="aqua-hell" id="dates">
    <div class="wrap">
      <div class="sek-kopf reveal">
        <p class="eyebrow">Upcoming dates</p>
        <h2>Workshops, intensives &amp; <em>journeys</em></h2>
        <p style="margin-top:1rem">Limited spots. Every date is held at Tanzlaboor Luzern unless noted.</p>
      </div>
      <div class="tickets" id="payrexx-demo">
{ticket('05.09.2026','The WATER Devotion — DANCE Workshop','Saturday 17–20h · Tanzlaboor Luzern, Nidfeldstrasse 1, 6010 Kriens','An immersive evening workshop and an invitation to tap into the intelligence of the many ways water communicates through and with us. Diving into fluid movement, deep listening within and shared connection through contact improvisation.','CHF 50–110')}
{ticket('10. &amp; 11.10.2026','A weekend of the waters — TWD Dance Intensive','Saturday 17–20h, Sunday 11–16h · Tanzlaboor Luzern','Through fluid movement practices, meditative exploration and contact improvisation, we engage with depth, surrender and gravity — building trust in the body’s intelligence and in the space we share. An invitation to soften and follow what wants to be felt.','CHF 50–190')}
{ticket('Online · 4 classes','The Waters Within — Online Dance Immersion','','Across four classes we explore the potential of the fluid human body. The journey encourages softening, sensing and surrender — in your own four walls. Tune your dance, welcome your expression.','CHF 320', False, 'Get the recordings · CHF 150')}
{ticket('Dance Journey','Awakening Flow — Dance Journey','','A longer journey through fluid movement, body awareness and shared practice — space to let your expression unfold over time.','CHF 420 · or 2 × 210', False)}
{ticket('Dance Journey','Tides of Expansion Vol. 3 — Dance Journey','','The third tide of this journey: expanding into your movement, your expression and the connection within the group.','CHF 420 · or 2 × 210', False)}
{ticket('2-day intensive','Rhythm of Liberation — 2 Day Intensive','','Two days of moving, releasing and finding rhythm together.','CHF 210–400', False)}
      </div>
    </div>
  </section>

  <section class="zitat">
    <div class="wrap reveal">
      {WELLE}
      <blockquote>&bdquo;The Water Devotion is the art of becoming fluid — strong in softness, free in surrender.&ldquo;
        <cite>Lucy Nicholas</cite>
      </blockquote>
    </div>
  </section>

{stimmen([
 ("I have perceived my body in a new, more holistic way. It helped me become more mindful and more sensitive in feeling into certain areas of it. […] It was a beautiful realization that my body can express so much more than I often think.","Fotini · TWD Practitioner"),
 ("I could truly feel how the movement eventually transformed into real waves, and how I was able to flow effortlessly with my body. I had never experienced this before. […] I would never have thought that I could feel so connected to the other participants in an online class.","Leonie · TWD Online Class"),
 ("The Water Devotion journey connected me with parts of my body that I had never consciously felt before. I allowed myself to be guided by my soul and danced in a way that felt right and good for my body.","Leonora · 1:1 Mentoring &amp; TWD Practitioner"),
])}
{schluss_cta("Questions about a <em>date</em>?",
 "Write me a few lines — we'll find the right way into the water together.",
 ['<a class="btn btn-tinte" href="mailto:lucy@thewaterdevotion.com?subject=Workshops">Write me</a>',
  '<a class="btn btn-tline" href="https://www.instagram.com/luzseed/" target="_blank" rel="noopener noreferrer">Follow on Instagram</a>'])}
"""
w += FUSS

# ================= SHIATSU =================
WA = "https://wa.me/41788636585?text=Ich%20interessiere%20mich%20f%C3%BCr%20ein%20ZenThaiShiatsu%20Treatment.%20"
WA_DD = "https://wa.me/41788636585?text=Ich%20interessiere%20mich%20f%C3%BCr%20das%20ZenThaiShiatsu%20DeepDivePackage.%20"
s = kopf("ZenThai Shiatsu in Lucerne | The Water Devotion",
         "ZenThai Shiatsu in Kriens near Lucerne: conscious touch, assisted stretches and gentle rocking on the futon. 75 or 90 minutes, plus a Deep Dive package.",
         "shiatsu")
s += f"""
  <section class="subhero">
    <div class="wrap subhero-grid">
      <div>
        <p class="eyebrow">Bodywork · Kriens / Lucerne</p>
        <h1>ZenThai <em>Shiatsu</em></h1>
        <p class="lead">A bodywork that invites deep rest and nourishes your overall wellbeing.</p>
        <div class="subhero-cta">
          <a class="btn btn-voll" href="#treatments">Treatment options</a>
        </div>
      </div>
      <div class="subhero-figur">
        <figure>{bild('shiatsu-outdoor','(max-width: 900px) 76vw, 32vw',1365,2048,'Lucy giving a ZenThai Shiatsu session outdoors at dusk')}</figure>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="prosa reveal">
        <p><strong>ZenThai Shiatsu is an invitation to listen.</strong> To the body, to the breath, to the subtle language beneath the surface.</p>
        <p>It weaves together stillness and flow, pressure and movement, grounding and expansion. Through conscious touch and gentle motion, space is created — space for what has been held, forgotten or waiting to be felt.</p>
        <p>The body is not something to be fixed, but a living, fluid landscape to move through. Each session becomes a journey, like a dance. A dance that continues to echo after the treatment has ended.</p>
      </div>
    </div>
  </section>

  <section class="dunkel">
    <div class="wrap">
      <div class="sek-kopf reveal">
        <p class="eyebrow">The practice</p>
        <h2>Rooted in Zen Shiatsu, moved like a <em>dance</em></h2>
      </div>
      <div class="prosa reveal">
        <p>A holistic bodywork practice rooted in Zen Shiatsu, enriched with elements from Thai massage, osteopathic principles, somatic movement and mindfulness-based practices. It works through conscious touch, rhythmic pressure, assisted stretches, gentle rocking and fluid movement.</p>
        <p>Drawing from Traditional Chinese Medicine, ZenThai Shiatsu follows the meridian system and works with the flow of energy throughout the body. Each session unfolds as a unique, embodied journey.</p>
        <p class="kleingedruckt">ZenThai Shiatsu is a wellbeing practice. It does not replace medical diagnosis or treatment.</p>
      </div>
    </div>
  </section>

  <section class="aqua-hell" id="treatments">
    <div class="wrap">
      <div class="sek-kopf reveal">
        <p class="eyebrow">Treatment options</p>
        <h2>Choose your <em>depth</em></h2>
      </div>
      <div class="behandlungen">
        <article class="behandlung reveal">
          <p class="dauer">75 min</p>
          <p class="preis-zeile">Full body · CHF 155</p>
          <ul>
            <li>Individually tailored to your needs</li>
            <li>Pressure points, stretches and passive movement</li>
            <li>Supports deep relaxation, energy flow and body awareness</li>
            <li>Includes time for arrival, intake and integration</li>
          </ul>
          <a class="btn btn-tinte" href="{WA}" target="_blank" rel="noopener noreferrer">Book 75 minutes</a>
        </article>
        <article class="behandlung reveal">
          <p class="dauer">90 min</p>
          <p class="preis-zeile">Full body · CHF 175</p>
          <ul>
            <li>A full body arc with deeper unwinding</li>
            <li>Space for your specific intention</li>
            <li>Pressure points and assisted stretches to invite deep relaxation and embodied awareness</li>
            <li>Includes time for arrival, intake and integration</li>
          </ul>
          <a class="btn btn-tinte" href="{WA}" target="_blank" rel="noopener noreferrer">Book 90 minutes</a>
        </article>
        <article class="behandlung reveal">
          <p class="dauer">Deep Dive</p>
          <p class="preis-zeile">3 × 90 min · CHF 499</p>
          <ul>
            <li>Three sessions to support gentle, lasting change</li>
            <li>Ongoing sessions invite deeper layers of release and awareness</li>
            <li>A holistic, root-oriented approach</li>
          </ul>
          <a class="btn btn-tinte" href="{WA_DD}" target="_blank" rel="noopener noreferrer">Book the Deep Dive</a>
        </article>
      </div>
      <p class="kleingedruckt reveal">Booking opens WhatsApp — you can also simply <a href="mailto:lucy@thewaterdevotion.com?subject=ZenThai%20Shiatsu">write an email</a>.</p>
      <div class="prosa reveal" style="margin-top:var(--s3)">
        <p>Sessions take place in comfortable clothes, on a soft futon on the floor. Your treatment is guided by insights from Traditional Chinese Five Element theory and osteopathy. Touch can be still and anchoring or fluid and rhythmic, depending on what is needed. There is no fixed protocol — the session follows the body's cues. The aim is for you to feel more balanced, grounded and re-energized.</p>
        <p>I offer <strong>student discounts</strong> and special rates for people who can't afford the full price at the moment. Feel free to reach out anytime.</p>
      </div>
    </div>
  </section>

{stimmen([
 ("Lucy's treatments lead you into a transformative dance with the body. Through the active and passive movements, I experienced a deep relaxation and softening, along with an inner centering. Her presence creates a space that allows you to open and truly arrive in the moment.","Jordan"),
 ("I received my first Zen Thai Massage, and I was enchanted for days afterward. Lucy created such a beautiful space where I felt completely safe, held and supported. […] I entered a deeply relaxed state — one I have experienced only a few times in my life.","Martina"),
 ("I felt very comfortable and warmly cared for from the very beginning. Lucy's calm, open and empathetic manner immediately created a sense of trust. […] The treatment was deeply nourishing on a human level. I am very grateful for this experience and can wholeheartedly recommend Lucy.","Lucas"),
])}
{schluss_cta("Book a <em>treatment</em>",
 "Write me a few lines about what brings you — we'll find a time together.",
 [f'<a class="btn btn-tinte" href="{WA}" target="_blank" rel="noopener noreferrer">Book via WhatsApp</a>',
  '<a class="btn btn-tline" href="mailto:lucy@thewaterdevotion.com?subject=ZenThai%20Shiatsu">Write an email</a>'])}
"""
s += FUSS

(root/'mentoring.html').write_text(m)
(root/'workshops.html').write_text(w)
(root/'shiatsu.html').write_text(s)
print('geschrieben: mentoring, workshops, shiatsu')

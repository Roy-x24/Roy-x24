#!/usr/bin/env python3
"""Genera todos los SVG del perfil (assets/) y el README.md.

Uso:  python scripts/build_assets.py
Todo se dibuja como SVG propio (sin servicios externos), en versión dark y light.
"""
import os
from xml.sax.saxutils import escape as esc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets")
os.makedirs(OUT, exist_ok=True)

SANS = "'Segoe UI', -apple-system, 'Helvetica Neue', Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"

THEMES = {
    "dark": dict(page="#0d1117", bg0="#020617", bg1="#0f172a", bg2="#134e4a", card="#0d1117", card2="#111827",
                 border="#1f2937", text="#e2e8f0", muted="#94a3b8", dim="#64748b",
                 a1="#10b981", a2="#22d3ee", a3="#a78bfa", warn="#f59e0b", chip="#161b22", name1="#22d3ee", name2="#10b981", name3="#a78bfa",
                 grid="#ffffff", gridop="0.05"),
    "light": dict(page="#ffffff", bg0="#f0fdf4", bg1="#ecfdf5", bg2="#a7f3d0", card="#ffffff", card2="#f8fafc",
                  border="#e2e8f0", text="#0f172a", muted="#475569", dim="#64748b",
                  a1="#059669", a2="#0891b2", a3="#7c3aed", warn="#d97706", chip="#f1f5f9", name1="#0e7490", name2="#059669", name3="#7c3aed",
                  grid="#0f172a", gridop="0.05"),
}


def tw(text, size, mono=False):
    return len(text) * size * (0.6 if mono else 0.56)


def wrap(text, maxchars):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) > maxchars:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines


def svg(w, h, body, defs="", title=""):
    t = f"<title>{esc(title)}</title>" if title else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{esc(title)}">{t}<defs>{defs}</defs>{body}</svg>\n')


def save(name, theme, content):
    with open(os.path.join(OUT, f"{name}-{theme}.svg"), "w", encoding="utf-8") as f:
        f.write(content)


def wave(y, amp, period, width, fill, opacity, dur, direction=-1, bottom=None):
    """Onda continua que se desplaza en bucle perfecto."""
    n = int(width / period) + 3
    half = period / 2
    d = f"M0,{y} Q{half/2},{y-amp} {half},{y}"
    for i in range(2, n * 2 + 1):
        d += f" T{half*i},{y}"
    b = bottom if bottom is not None else y + 200
    d += f" L{half*(n*2)},{b} L0,{b} Z"
    to = period * direction
    return (f'<g opacity="{opacity}"><path d="{d}" fill="{fill}">'
            f'<animateTransform attributeName="transform" type="translate" from="0 0" to="{to} 0" dur="{dur}s" repeatCount="indefinite"/>'
            f'</path></g>')


# ───────────────────────────── HERO ─────────────────────────────
def hero(t, c):
    W, H = 1200, 360
    roles = ["Full Stack Developer", "Backend Architect", "Frontend Artist", "Cybersecurity Enthusiast"]
    n = len(roles)
    dur = n * 3
    role_svg = ""
    for i, r in enumerate(roles):
        a, b = i / n, (i + 1) / n
        e = 0.03 / n * 3
        kt = f"0;{a:.4f};{a+e:.4f};{b-e:.4f};{b:.4f};1"
        role_svg += (f'<text x="600" y="232" text-anchor="middle" font-family="{MONO}" font-size="26" font-weight="600" fill="{c["a1"]}" opacity="0">'
                     f'<tspan fill="{c["dim"]}">&lt;</tspan>{esc(r)}<tspan fill="{c["dim"]}"> /&gt;</tspan>'
                     f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="{kt}" dur="{dur}s" repeatCount="indefinite"/></text>')
    defs = f'''
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c['bg0']}"/><stop offset=".5" stop-color="{c['bg1']}"/><stop offset="1" stop-color="{c['bg2']}"/></linearGradient>
<linearGradient id="nm" x1="0" x2="1"><stop offset="0" stop-color="{c['name1']}"/><stop offset=".55" stop-color="{c['name2']}"/><stop offset="1" stop-color="{c['name3']}"/></linearGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="55"/></filter>
<pattern id="grid" width="44" height="44" patternUnits="userSpaceOnUse"><path d="M44 0H0V44" fill="none" stroke="{c['grid']}" stroke-opacity="{c['gridop']}"/></pattern>
<radialGradient id="fade" cx=".5" cy=".5" r=".7"><stop offset=".3" stop-color="#fff"/><stop offset="1" stop-color="#000"/></radialGradient>
<mask id="m"><rect width="{W}" height="{H}" fill="url(#fade)"/></mask>'''
    body = f'''
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<rect width="{W}" height="{H}" fill="url(#grid)" mask="url(#m)"/>
<g filter="url(#blur)">
  <circle cx="220" cy="120" r="120" fill="{c['a2']}" opacity=".30"><animate attributeName="cx" values="220;420;220" dur="14s" repeatCount="indefinite"/><animate attributeName="cy" values="120;200;120" dur="11s" repeatCount="indefinite"/></circle>
  <circle cx="980" cy="200" r="140" fill="{c['a3']}" opacity=".28"><animate attributeName="cx" values="980;780;980" dur="16s" repeatCount="indefinite"/><animate attributeName="cy" values="200;110;200" dur="12s" repeatCount="indefinite"/></circle>
  <circle cx="600" cy="300" r="130" fill="{c['a1']}" opacity=".30"><animate attributeName="cx" values="600;700;500;600" dur="18s" repeatCount="indefinite"/></circle>
</g>
<text x="600" y="92" text-anchor="middle" font-family="{MONO}" font-size="15" fill="{c['muted']}" letter-spacing="2">// hello, world — soy</text>
<text x="600" y="176" text-anchor="middle" font-family="{SANS}" font-size="84" font-weight="800" letter-spacing="8" fill="url(#nm)">ROY BARRERA
  <animate attributeName="opacity" from="0" to="1" dur="1.2s" fill="freeze"/></text>
{role_svg}
<g transform="translate(600 284)">
  <rect x="-150" y="-17" width="300" height="34" rx="17" fill="{c['card']}" fill-opacity=".55" stroke="{c['a1']}" stroke-opacity=".5"/>
  <circle cx="-122" cy="0" r="5" fill="{c['a1']}"><animate attributeName="r" values="4;7;4" dur="2s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;.35;1" dur="2s" repeatCount="indefinite"/></circle>
  <text x="-106" y="5" font-family="{MONO}" font-size="13" fill="{c['text']}">Panamá 🇵🇦 · open to collaborate</text>
</g>
{wave(318, 16, 600, W, c['page'], .35, 14, -1, H)}
{wave(332, 14, 400, W, c['page'], 1, 9, 1, H)}'''
    return svg(W, H, body, defs, "Roy Barrera — Full Stack Developer")


# ───────────────────────────── TERMINAL ─────────────────────────────
def terminal(t, c):
    lines = [
        ("name", "Roy Barrera", "text"),
        ("role", "Full Stack Developer", "text"),
        ("degree", "Lic. Desarrollo y Gestión de Software — UTP", "text"),
        ("location", "Panamá 🇵🇦", "text"),
        ("focus", "[Backend, Microservicios, Cloud, Cybersecurity, Clean Code]", "a1"),
        ("building", "Sistemas DDC/KYC · Plataformas de reservas · Apps en tiempo real", "text"),
        ("stack", "React · Vue · TypeScript · Python · Flask · Bun · PostgreSQL · Docker", "a2"),
        ("status", "● open to collaborate on ambitious projects", "warn"),
        ("motto", "\"No solo escribo código — construyo soluciones.\"", "a3"),
    ]
    W = 1000
    top = 62
    lh = 28
    H = top + 38 + lh * len(lines) + 40
    body = f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="{c["card2"]}" stroke="{c["border"]}"/>'
    body += f'<path d="M.5 14.5 a14 14 0 0 1 14-14 H{W-14.5} a14 14 0 0 1 14 14 V44 H.5Z" fill="{c["chip"]}"/>'
    body += f'<line x1="0" y1="44" x2="{W}" y2="44" stroke="{c["border"]}"/>'
    for i, col in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        body += f'<circle cx="{28+i*22}" cy="22" r="6.5" fill="{col}"/>'
    body += f'<text x="{W/2}" y="27" text-anchor="middle" font-family="{MONO}" font-size="12.5" fill="{c["dim"]}">roy@panama: ~/profile</text>'
    body += (f'<text x="32" y="{top+22}" font-family="{MONO}" font-size="15"><tspan fill="{c["a1"]}" font-weight="700">➜</tspan>'
             f'<tspan fill="{c["a2"]}"> ~</tspan><tspan fill="{c["text"]}"> whoami --verbose</tspan></text>')
    y = top + 22 + lh + 6
    for i, (k, v, col) in enumerate(lines):
        d = 0.5 + i * 0.28
        body += (f'<text x="32" y="{y}" font-family="{MONO}" font-size="14.5" opacity="0" xml:space="preserve">'
                 f'<tspan fill="{c["a3"]}">{k}:</tspan><tspan fill="{c["dim"]}">{" "*(10-len(k))}</tspan><tspan fill="{c[col]}">{esc(v)}</tspan>'
                 f'<animate attributeName="opacity" from="0" to="1" dur="0.35s" begin="{d:.2f}s" fill="freeze"/></text>')
        y += lh
    body += (f'<text x="32" y="{y+8}" font-family="{MONO}" font-size="15"><tspan fill="{c["a1"]}" font-weight="700">➜</tspan>'
             f'<tspan fill="{c["a2"]}"> ~</tspan></text>'
             f'<rect x="76" y="{y-6}" width="9" height="19" fill="{c["a1"]}"><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" repeatCount="indefinite"/></rect>')
    return svg(W, H, body, "", "whoami")


# ───────────────────────────── SECTION HEADERS ─────────────────────────────
def header(num, title, sub, c):
    W, H = 1000, 74
    defs = (f'<linearGradient id="ln" x1="0" x2="1"><stop offset="0" stop-color="{c["a1"]}"/><stop offset=".5" stop-color="{c["a2"]}" stop-opacity=".6"/>'
            f'<stop offset="1" stop-color="{c["a3"]}" stop-opacity="0"/></linearGradient>')
    body = (f'<text x="4" y="40" font-family="{MONO}" font-size="16" fill="{c["a1"]}" font-weight="700">{num}</text>'
            f'<text x="44" y="42" font-family="{SANS}" font-size="30" font-weight="800" fill="{c["text"]}">{esc(title)}</text>'
            f'<text x="{44+tw(title,30)+16:.0f}" y="42" font-family="{MONO}" font-size="14" fill="{c["dim"]}">{esc(sub)}</text>'
            f'<rect x="4" y="58" width="992" height="2" rx="1" fill="url(#ln)"/>'
            f'<rect x="4" y="57" width="70" height="4" rx="2" fill="{c["a1"]}">'
            f'<animate attributeName="x" values="4;926;4" dur="6s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"/></rect>')
    return svg(W, H, body, defs, title)


# ───────────────────────────── CHIPS / STACK ─────────────────────────────
BRAND = {
    "React": "#61DAFB", "Vue.js": "#4FC08D", "Next.js": "#9ca3af", "TypeScript": "#3178C6", "JavaScript": "#F7DF1E",
    "Tailwind CSS": "#38BDF8", "Vite": "#9466FF", "HTML5": "#E34F26", "CSS3": "#1572B6",
    "Python": "#3776AB", "Flask": "#9ca3af", "Bun": "#f9a8d4", "Hono": "#E36002", "Node.js": "#5FA04E", "PHP": "#777BB4",
    "Java": "#ED8B00", "C#": "#9B4F96", "REST APIs": "#10b981",
    "PostgreSQL": "#4169E1", "MySQL": "#00758F", "MongoDB": "#47A248", "RabbitMQ": "#FF6600", "SQL Server": "#CC2927",
    "Docker": "#2496ED", "Git": "#F05032", "GitHub Actions": "#2088FF", "Linux": "#FCC624", "Postman": "#FF6C37", "VS Code": "#007ACC",
}


def chip(x, y, label, c, size=13):
    w = tw(label, size) + 34
    col = BRAND.get(label, c["a1"])
    return (f'<g transform="translate({x:.1f} {y})"><rect width="{w:.1f}" height="28" rx="14" fill="{c["chip"]}" stroke="{c["border"]}"/>'
            f'<circle cx="15" cy="14" r="4.5" fill="{col}" stroke="{c["border"]}" stroke-width=".5"/>'
            f'<text x="26" y="18.5" font-family="{SANS}" font-size="{size}" font-weight="600" fill="{c["text"]}">{esc(label)}</text></g>'), w


def flow(labels, c, x0, y0, maxx, gap=8, rowh=36):
    x, y, out = x0, y0, ""
    for l in labels:
        s, w = chip(0, 0, l, c)
        if x + w > maxx:
            x, y = x0, y + rowh
        s, w = chip(x, y, l, c)
        out += s
        x += w + gap
    return out, y + 28


def stack(t, c):
    cats = [
        ("FRONTEND", "🎨", ["React", "Vue.js", "Next.js", "TypeScript", "JavaScript", "Tailwind CSS", "Vite", "HTML5", "CSS3"], c["a2"]),
        ("BACKEND", "⚙️", ["Python", "Flask", "Bun", "Hono", "Node.js", "PHP", "Java", "C#", "REST APIs"], c["a1"]),
        ("DATA", "🗄️", ["PostgreSQL", "MySQL", "MongoDB", "RabbitMQ", "SQL Server"], c["a3"]),
        ("DEVOPS & TOOLS", "🛠️", ["Docker", "Git", "GitHub Actions", "Linux", "Postman", "VS Code"], c["warn"]),
    ]
    W = 1000
    y = 0
    body = ""
    for i, (name, ic, items, col) in enumerate(cats):
        inner, bottom = flow(items, c, 200, y + 22, W - 24)
        h = bottom - y + 22
        body += f'<rect x=".5" y="{y+.5}" width="{W-1}" height="{h}" rx="12" fill="{c["card2"]}" stroke="{c["border"]}"/>'
        body += f'<rect x=".5" y="{y+14}" width="4" height="{h-28}" rx="2" fill="{col}"/>'
        body += f'<text x="28" y="{y+h/2+5}" font-family="{MONO}" font-size="13" font-weight="700" fill="{col}" letter-spacing="1.5">{esc(name)}</text>'
        body += inner
        y += h + 12
    return svg(W, y - 12, body, "", "Tech stack")


# ───────────────────────────── CARDS ─────────────────────────────
def card_final(slug, title, tag, desc, chips, c, bullets=None, link="ver repositorio ↗", accent="a1", W=440, minH=0):
    col = c[accent]
    lines = wrap(desc, 54)
    y = 104
    txt = ""
    for l in lines:
        txt += f'<text x="28" y="{y}" font-family="{SANS}" font-size="13.5" fill="{c["muted"]}">{esc(l)}</text>'
        y += 20
    if bullets:
        y += 6
        for b in bullets:
            txt += (f'<text x="28" y="{y}" font-family="{MONO}" font-size="13" fill="{c["a1"]}" font-weight="700">✓</text>'
                    f'<text x="48" y="{y}" font-family="{SANS}" font-size="13" fill="{c["text"]}">{esc(b)}</text>')
            y += 22
    y += 10
    inner, bottom = flow(chips, c, 28, y, W - 20, rowh=34)
    H = max(bottom + 20 + (28 if link else 0), minH)
    defs = (f'<linearGradient id="tp" x1="0" x2="1"><stop offset="0" stop-color="{col}"/><stop offset="1" stop-color="{c["a3"]}"/></linearGradient>'
            f'<clipPath id="cl"><rect width="{W}" height="{H}" rx="14"/></clipPath>')
    tagw = tw(tag, 11, True) + 20
    body = (f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="{c["card2"]}" stroke="{c["border"]}"/>'
            f'<g clip-path="url(#cl)"><rect width="{W}" height="4" fill="url(#tp)"/>'
            f'<circle cx="{W-30}" cy="10" r="90" fill="{col}" opacity=".08"><animate attributeName="r" values="80;100;80" dur="7s" repeatCount="indefinite"/></circle></g>'
            f'<text x="28" y="46" font-family="{SANS}" font-size="19" font-weight="800" fill="{c["text"]}">{esc(title)}</text>'
            f'<g transform="translate(28 58)"><rect width="{tagw:.0f}" height="20" rx="10" fill="{col}" fill-opacity=".15"/>'
            f'<text x="10" y="14" font-family="{MONO}" font-size="11" font-weight="700" fill="{col}">{esc(tag)}</text></g>'
            + txt + inner)
    if link:
        body += f'<text x="{W-24}" y="{H-16}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{col}" font-weight="700">{esc(link)}</text>'
    return svg(W, H, body, defs, title), H


PROJECTS = [
    ("reservas", "Plataforma de Reservas Turísticas", "MICROSERVICIOS",
     "API Gateway, PostgreSQL por servicio y eventos RabbitMQ. Roles cliente/admin, login con Google, pagos simulados, reseñas moderadas y comprobantes.",
     ["React", "TypeScript", "Python", "PostgreSQL", "RabbitMQ", "Docker"], "a1"),
    ("ddc-inmo", "DDC/KYC Inmobiliario", "IA · OCR · COMPLIANCE",
     "Debida diligencia para promotoras inmobiliarias de Panamá: matriz de riesgo versionada, bandejas por rol, auditoría completa e IA/OCR asistida.",
     ["Python", "JavaScript", "Docker"], "a3"),
    ("ddc-kyc", "Sistema DDC/KYC", "LEY 23 DE 2015",
     "Módulo de Debida Diligencia de Clientes para entidades obligadas de Panamá, con flujo de ramas feature → qa → master.",
     ["Python", "JavaScript", "Docker"], "a2"),
    ("pokepelea", "Pokémon Battle Rooms", "TIEMPO REAL",
     "Batallas 1 vs 1 por salas con código: equipos de hasta 6 y combate por turnos. Auth con Clerk y pagos con Stripe.",
     ["React", "Bun", "Hono", "MongoDB", "Docker"], "warn"),
    ("checkers", "Damas AI", "IA · A*",
     "Damas inglesas 8×8 con un oponente de inteligencia artificial basado en heurísticas de búsqueda A*.",
     ["React", "TypeScript", "Bun", "Docker"], "a2"),
    ("pollclass", "PollClass", "ENCUESTAS EN VIVO",
     "Encuestas para clases con resultados en tiempo real vía HTTP polling y gráficas con Recharts.",
     ["React", "Tailwind CSS", "Bun", "MongoDB"], "a1"),
]
PROJ_URL = {
    "reservas": "plataforma-reservas-turisticas", "ddc-inmo": "sistema-ddc-inmobiliario", "ddc-kyc": "ddc-kyc-sistema",
    "pokepelea": "PokePelea", "checkers": "checkers", "pollclass": "pollclass",
}


# ───────────────────────────── EDUCATION ─────────────────────────────
def education(t, c):
    rows = [
        ("Universidad Tecnológica de Panamá", "Lic. Desarrollo y Gestión de Software", "EN PROGRESO", "a2"),
        ("freeCodeCamp", "Responsive Web Design", "CERTIFICADO", "a1"),
        ("Python Institute", "PCAP – Certified Associate in Python Programming", "EN CURSO", "warn"),
        ("AWS / Microsoft Learn", "Cloud Fundamentals", "EN CURSO", "warn"),
    ]
    W, rh = 1000, 64
    H = rh * len(rows) + 4
    body = f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="{c["card2"]}" stroke="{c["border"]}"/>'
    for i, (inst, prog, st, col) in enumerate(rows):
        y = 2 + i * rh
        if i:
            body += f'<line x1="24" y1="{y}" x2="{W-24}" y2="{y}" stroke="{c["border"]}"/>'
        body += (f'<circle cx="38" cy="{y+rh/2}" r="6" fill="{c[col]}"><animate attributeName="opacity" values="1;.4;1" dur="{2+i*.4}s" repeatCount="indefinite"/></circle>'
                 f'<text x="64" y="{y+27}" font-family="{SANS}" font-size="17" font-weight="700" fill="{c["text"]}">{esc(inst)}</text>'
                 f'<text x="64" y="{y+47}" font-family="{SANS}" font-size="13.5" fill="{c["muted"]}">{esc(prog)}</text>')
        w = tw(st, 11.5, True) + 28
        body += (f'<g transform="translate({W-28-w:.0f} {y+rh/2-12})"><rect width="{w:.0f}" height="24" rx="12" fill="{c[col]}" fill-opacity=".14" stroke="{c[col]}" stroke-opacity=".5"/>'
                 f'<text x="{w/2:.0f}" y="16" text-anchor="middle" font-family="{MONO}" font-size="11.5" font-weight="700" fill="{c[col]}">{st}</text></g>')
    return svg(W, H, body, "", "Educación y certificaciones")


# ───────────────────────────── SKILLS ─────────────────────────────
def skills(t, c):
    items = [("Full Stack Engineering", 90, "a1", "a2"), ("Software Architecture", 85, "a1", "a3"),
             ("Cloud Computing", 70, "a2", "a3"), ("Cybersecurity", 65, "a3", "a2"), ("Problem Solving", 95, "warn", "a1")]
    W, top, rh = 1000, 28, 52
    H = top * 2 + rh * len(items) - 12
    bx, bw = 290, 600
    defs = "".join(f'<linearGradient id="g{i}" x1="0" x2="1"><stop offset="0" stop-color="{c[a]}"/><stop offset="1" stop-color="{c[b]}"/></linearGradient>'
                   for i, (_, _, a, b) in enumerate(items))
    body = f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="{c["card2"]}" stroke="{c["border"]}"/>'
    for i, (lab, pct, a, b) in enumerate(items):
        y = top + i * rh
        w = bw * pct / 100
        d = i * 0.18
        for k in range(1, 4):  # marcas del 25/50/75
            x = bx + bw * k / 4
            body += f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+14}" stroke="{c["border"]}"/>'
        body += (f'<text x="32" y="{y+13}" font-family="{SANS}" font-size="15.5" font-weight="700" fill="{c["text"]}">{lab}</text>'
                 f'<rect x="{bx}" y="{y}" width="{bw}" height="14" rx="7" fill="{c["chip"]}" stroke="{c["border"]}"/>'
                 f'<rect x="{bx}" y="{y}" width="0" height="14" rx="7" fill="url(#g{i})"><animate attributeName="width" from="0" to="{w:.0f}" dur="1.5s" begin="{d:.2f}s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines=".22 1 .36 1"/></rect>'
                 f'<circle cx="{bx}" cy="{y+7}" r="7" fill="{c[b]}" opacity="0"><animate attributeName="cx" from="{bx}" to="{bx+w:.0f}" dur="1.5s" begin="{d:.2f}s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines=".22 1 .36 1"/>'
                 f'<animate attributeName="opacity" values="0;1;1" keyTimes="0;.02;1" dur="1.5s" begin="{d:.2f}s" fill="freeze"/></circle>'
                 f'<text x="{W-32}" y="{y+13}" text-anchor="end" font-family="{MONO}" font-size="15" font-weight="700" fill="{c[a]}">{pct}%</text>')
    return svg(W, H, body, defs, "Skill calibration")


# ───────────────────────────── CONTACT + FOOTER ─────────────────────────────
def contact(t, c):
    W, H = 1000, 190
    defs = (f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c["bg0"]}"/><stop offset=".6" stop-color="{c["bg1"]}"/><stop offset="1" stop-color="{c["bg2"]}"/></linearGradient>'
            f'<linearGradient id="tx" x1="0" x2="1"><stop offset="0" stop-color="{c["name1"]}"/><stop offset="1" stop-color="{c["name2"]}"/></linearGradient>'
            f'<filter id="bl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="40"/></filter>'
            f'<clipPath id="cl"><rect width="{W}" height="{H}" rx="18"/></clipPath>')
    body = (f'<g clip-path="url(#cl)"><rect width="{W}" height="{H}" fill="url(#bg)"/>'
            f'<g filter="url(#bl)"><circle cx="120" cy="40" r="90" fill="{c["a2"]}" opacity=".3"><animate attributeName="cx" values="120;300;120" dur="12s" repeatCount="indefinite"/></circle>'
            f'<circle cx="880" cy="160" r="100" fill="{c["a3"]}" opacity=".3"><animate attributeName="cx" values="880;700;880" dur="13s" repeatCount="indefinite"/></circle></g></g>'
            f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{c["a1"]}" stroke-opacity=".45"/>'
            f'<text x="500" y="70" text-anchor="middle" font-family="{MONO}" font-size="14" fill="{c["muted"]}" letter-spacing="3">OPEN CHANNEL</text>'
            f'<text x="500" y="112" text-anchor="middle" font-family="{SANS}" font-size="34" font-weight="800" fill="url(#tx)">¿Tienes una idea ambiciosa?</text>'
            f'<text x="500" y="148" text-anchor="middle" font-family="{SANS}" font-size="17" fill="{c["text"]}">Freelance · Open source · Oportunidades laborales — hablemos.</text>')
    return svg(W, H, body, defs, "Contacto")


def footer(t, c):
    W, H = 1200, 170
    defs = (f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c["bg0"]}"/><stop offset=".5" stop-color="{c["bg1"]}"/><stop offset="1" stop-color="{c["bg2"]}"/></linearGradient>')
    # ondas superiores rellenando hacia arriba
    top1 = wave(30, 16, 600, W, c["page"], .35, 14, -1, 0)
    top2 = wave(18, 14, 400, W, c["page"], 1, 9, 1, 0)
    body = (f'<rect width="{W}" height="{H}" fill="url(#bg)"/>{top1}{top2}'
            f'<text x="600" y="100" text-anchor="middle" font-family="{SANS}" font-size="26" font-weight="800" letter-spacing="14" fill="{c["name2"]}">ROY BARRERA</text>'
            f'<text x="600" y="132" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{c["muted"]}" letter-spacing="2">PANAMÁ 🇵🇦 · BUILT WITH ♥ AND TOO MUCH COFFEE</text>')
    return svg(W, H, body, defs, "Roy Barrera")



# ───────────────────────────── EXTRAS ─────────────────────────────
import math

ABBR = {"React": "Re", "Vue.js": "Vu", "Next.js": "Nx", "TypeScript": "TS", "JavaScript": "JS", "Tailwind CSS": "Tw",
        "Python": "Py", "Flask": "Fl", "Bun": "Bn", "Hono": "Ho", "Node.js": "No", "PHP": "PHP", "Java": "Jv", "C#": "C#",
        "PostgreSQL": "Pg", "MySQL": "My", "MongoDB": "Mg", "RabbitMQ": "Rb", "Docker": "Dk", "Git": "Git", "Linux": "Lx",
        "GitHub Actions": "GA", "Vite": "Vi"}


def numbers(t, c):
    W, H = 1000, 130
    items = [(28, "Repositorios", "públicos en GitHub", "a1"), (29, "Tecnologías", "en mi stack", "a2"),
             (7, "Microservicios", "en reservas", "a3"), (2, "Experiencias", "DITIC · Ayudinga", "warn")]
    body = ""
    for i, (n, lab, sub, k) in enumerate(items):
        x = i * 257
        col = c[k]
        body += (f'<g transform="translate({x} 0)"><rect x=".5" y=".5" width="228" height="{H-1}" rx="14" fill="{c["card2"]}" stroke="{c["border"]}"/>'
                 f'<circle cx="62" cy="{H/2}" r="34" fill="none" stroke="{c["chip"]}" stroke-width="7"/>'
                 f'<circle cx="62" cy="{H/2}" r="34" fill="none" stroke="{col}" stroke-width="7" stroke-linecap="round" stroke-dasharray="214" stroke-dashoffset="214" transform="rotate(-90 62 {H/2})">'
                 f'<animate attributeName="stroke-dashoffset" from="214" to="{214*(0.12+0.05*i):.0f}" dur="1.6s" begin="{i*.2:.1f}s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines=".22 1 .36 1"/></circle>'
                 f'<text x="62" y="{H/2+8}" text-anchor="middle" font-family="{SANS}" font-size="24" font-weight="800" fill="{c["text"]}">{n}</text>'
                 f'<text x="112" y="{H/2-2}" font-family="{SANS}" font-size="14" font-weight="800" fill="{col}">{esc(lab)}</text>'
                 f'<text x="112" y="{H/2+18}" font-family="{SANS}" font-size="11.5" fill="{c["muted"]}">{esc(sub)}</text></g>')
    return svg(W, H, body, "", "Números")


CODE = [
    [("const", "kw"), (" roy", "text"), (": ", "p"), ("Developer", "fn"), (" = {", "p")],
    [("  name", "key"), (": ", "p"), ('"Roy Barrera"', "str"), (",", "p")],
    [("  location", "key"), (": ", "p"), ('"Panamá"', "str"), (",", "p")],
    [("  roles", "key"), (": ", "p"), ('["Full Stack", "Backend", "Cybersecurity"]', "str"), (",", "p")],
    [("  stack", "key"), (": ", "p"), ('["React", "Vue", "Python", "Bun", "PostgreSQL", "Docker"]', "str"), (",", "p")],
    [("  learning", "key"), (": ", "p"), ('["PCAP", "Cloud Fundamentals", "Ciberseguridad"]', "str"), (",", "p")],
    [("  openToWork", "key"), (": ", "p"), ("true", "kw"), (",", "p")],
    [("  hire", "fn"), ("(idea) { ", "p"), ("return", "kw"), (" build(idea).ship(); }", "text")],
    [("};", "p")],
    [("// ¿Tienes una idea ambiciosa? → hablemos.", "p")],
]


def codecard(t, c):
    col = {"text": c["text"], "p": c["dim"], "kw": c["a3"], "str": c["a1"], "key": c["a2"], "fn": c["warn"]}
    W, top, lh = 1000, 76, 27
    H = top + lh * len(CODE) + 20
    body = f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="{c["card2"]}" stroke="{c["border"]}"/>'
    body += f'<path d="M.5 14.5 a14 14 0 0 1 14-14 H{W-14.5} a14 14 0 0 1 14 14 V44 H.5Z" fill="{c["chip"]}"/><line x1="0" y1="44" x2="{W}" y2="44" stroke="{c["border"]}"/>'
    for i, cc in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        body += f'<circle cx="{28+i*22}" cy="22" r="6.5" fill="{cc}"/>'
    body += f'<g transform="translate(110 9)"><rect width="104" height="26" rx="7" fill="{c["card2"]}" stroke="{c["border"]}"/><circle cx="14" cy="13" r="4" fill="{c["a2"]}"/><text x="26" y="17.5" font-family="{MONO}" font-size="12.5" fill="{c["text"]}">roy.ts</text></g>'
    for i, line in enumerate(CODE):
        y = top + i * lh
        spans = "".join(f'<tspan fill="{col[k]}">{esc(tx)}</tspan>' for tx, k in line)
        body += (f'<text x="24" y="{y}" font-family="{MONO}" font-size="13" fill="{c["dim"]}" opacity=".6">{i+1:>2}</text>'
                 f'<text x="64" y="{y}" font-family="{MONO}" font-size="15" xml:space="preserve" opacity="0">{spans}'
                 f'<animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="{0.3+i*0.3:.1f}s" fill="freeze"/></text>')
    return svg(W, H, body, "", "roy.ts")


def orbit(t, c):
    W, H = 1000, 470
    cx, cy = 500, 235
    rings = [
        (82, 24, 1, ["Python", "TypeScript", "React", "Docker"]),
        (142, 36, -1, ["Flask", "Vue.js", "Bun", "PostgreSQL", "Git", "Linux", "Hono"]),
        (202, 52, 1, ["Next.js", "Tailwind CSS", "Node.js", "MongoDB", "RabbitMQ", "Java", "PHP", "GitHub Actions", "JavaScript", "MySQL"]),
    ]
    defs = (f'<radialGradient id="core" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{c["a1"]}" stop-opacity=".9"/><stop offset="1" stop-color="{c["a2"]}" stop-opacity=".15"/></radialGradient>'
            f'<filter id="gl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="14"/></filter>')
    body = f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="18" fill="{c["card2"]}" stroke="{c["border"]}"/>'
    for r, *_ in rings:
        body += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c["border"]}" stroke-dasharray="3 7"/>'
    body += f'<circle cx="{cx}" cy="{cy}" r="46" fill="{c["a1"]}" opacity=".35" filter="url(#gl)"><animate attributeName="r" values="40;58;40" dur="4s" repeatCount="indefinite"/></circle>'
    for r, dur, d, items in rings:
        T = dur * 1.6
        g = f'<g><animateTransform attributeName="transform" type="rotate" from="{0 if d>0 else 360} {cx} {cy}" to="{360 if d>0 else 0} {cx} {cy}" dur="{T}s" repeatCount="indefinite"/>'
        for i, name in enumerate(items):
            a = 2 * math.pi * i / len(items) + (r % 7)
            x, y = cx + r * math.cos(a), cy + r * math.sin(a)
            br = BRAND.get(name, c["a1"])
            g += (f'<g transform="translate({x:.1f} {y:.1f})"><g><animateTransform attributeName="transform" type="rotate" from="{0 if d>0 else 360}" to="{-360 if d>0 else 0}" dur="{T}s" repeatCount="indefinite"/>'
                  f'<title>{esc(name)}</title><circle r="22" fill="{c["card"]}" stroke="{br}" stroke-width="2"/><circle r="22" fill="{br}" opacity=".12"/>'
                  f'<text y="4.5" text-anchor="middle" font-family="{MONO}" font-size="12.5" font-weight="800" fill="{c["text"]}">{ABBR.get(name, name[:2])}</text></g></g>')
        body += g + "</g>"
    body += (f'<circle cx="{cx}" cy="{cy}" r="38" fill="url(#core)" stroke="{c["a1"]}" stroke-opacity=".6"/>'
             f'<text x="{cx}" y="{cy+2}" text-anchor="middle" font-family="{SANS}" font-size="22" font-weight="800" fill="{c["text"]}">ROY</text>'
             f'<text x="{cx}" y="{cy+19}" text-anchor="middle" font-family="{MONO}" font-size="10" fill="{c["text"]}" opacity=".8">full stack</text>')
    return svg(W, H, body, defs, "Órbita de tecnologías")


def arch(t, c):
    W = 1000
    names = ["Identidad", "Catálogo", "Disponibilidad", "Reservas", "Pagos", "Notificaciones", "Reportes"]
    subs = ["login · Google · roles", "destinos · galería", "cupos por fecha", "ciclo de reserva", "pago simulado", "avisos al cliente", "métricas admin"]
    top, step, bh = 36, 62, 46
    H = top + step * len(names) + 22
    gy = H / 2
    body = f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="18" fill="{c["card2"]}" stroke="{c["border"]}"/>'

    def box(x, y, w, h, title, sub, col):
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{c["card"]}" stroke="{col}" stroke-opacity=".7"/>'
                f'<text x="{x+14}" y="{y+h/2-1}" font-family="{SANS}" font-size="14.5" font-weight="800" fill="{c["text"]}">{esc(title)}</text>'
                f'<text x="{x+14}" y="{y+h/2+14}" font-family="{SANS}" font-size="11" fill="{c["muted"]}">{esc(sub)}</text>')
    body += f'<line x1="154" y1="{gy}" x2="236" y2="{gy}" stroke="{c["a2"]}" stroke-opacity=".5" stroke-width="2"/>'
    body += f'<circle r="4" fill="{c["a2"]}"><animateMotion dur="1.6s" repeatCount="indefinite" path="M154,{gy} L236,{gy}"/></circle>'
    for i, n in enumerate(names):
        yc = top + i * step + bh / 2
        pth = f"M376,{gy} C426,{gy} 426,{yc} 476,{yc}"
        body += f'<path d="{pth}" fill="none" stroke="{c["a2"]}" stroke-opacity=".35" stroke-width="2"/>'
        body += f'<circle r="3.5" fill="{c["a2"]}"><animateMotion dur="2.8s" begin="{i*.4:.1f}s" repeatCount="indefinite" path="{pth}"/></circle>'
        ev = f"M716,{yc} L788,{yc}"
        body += f'<line x1="716" y1="{yc}" x2="788" y2="{yc}" stroke="{c["warn"]}" stroke-opacity=".4" stroke-width="2" stroke-dasharray="4 5"/>'
        body += f'<circle r="3.5" fill="{c["warn"]}"><animateMotion dur="2.2s" begin="{i*.33+.8:.2f}s" repeatCount="indefinite" path="{ev}"/></circle>'
    for i, n in enumerate(names):
        y = top + i * step
        body += box(476, y, 240, bh, n, subs[i], c["a1"])
        body += (f'<g transform="translate(636 {y+bh/2-9})"><rect width="68" height="18" rx="9" fill="{c["a3"]}" fill-opacity=".16"/>'
                 f'<text x="34" y="12.5" text-anchor="middle" font-family="{MONO}" font-size="10" font-weight="700" fill="{c["a3"]}">PG propio</text></g>')
    body += box(24, gy - 32, 130, 64, "Cliente", "React · Vite", c["a2"])
    body += box(236, gy - 32, 140, 64, "Pasarela", "API Gateway", c["a1"])
    body += (f'<rect x="788" y="28" width="36" height="{H-56}" rx="18" fill="{c["warn"]}" fill-opacity=".14" stroke="{c["warn"]}" stroke-opacity=".7"/>'
             f'<text transform="translate(812 {H/2}) rotate(-90)" text-anchor="middle" font-family="{MONO}" font-size="13" font-weight="800" fill="{c["warn"]}" letter-spacing="2">RABBITMQ · EVENT BUS</text>')
    lx = 852
    body += (f'<text x="{lx}" y="{gy-48}" font-family="{MONO}" font-size="12" fill="{c["dim"]}" letter-spacing="1.5">LEYENDA</text>'
             f'<circle cx="{lx+5}" cy="{gy-24}" r="4" fill="{c["a2"]}"/><text x="{lx+18}" y="{gy-20}" font-family="{SANS}" font-size="12.5" fill="{c["text"]}">HTTP / REST</text>'
             f'<circle cx="{lx+5}" cy="{gy}" r="4" fill="{c["warn"]}"/><text x="{lx+18}" y="{gy+4}" font-family="{SANS}" font-size="12.5" fill="{c["text"]}">Eventos async</text>'
             f'<rect x="{lx}" y="{gy+18}" width="10" height="10" rx="2" fill="{c["a3"]}" fill-opacity=".6"/><text x="{lx+18}" y="{gy+28}" font-family="{SANS}" font-size="12.5" fill="{c["text"]}">BD por servicio</text>')
    body += f'<text x="24" y="{H-20}" font-family="{MONO}" font-size="11.5" fill="{c["dim"]}">plataforma-reservas-turisticas · arquitectura</text>'
    return svg(W, H, body, "", "Arquitectura de microservicios")


def pipeline(t, c):
    W, H = 1000, 190
    steps = [("01", "Idea", "requisitos"), ("02", "Diseño", "arquitectura"), ("03", "Código", "clean code"), ("04", "Pruebas", "QA · review"), ("05", "Deploy", "Docker · CI/CD")]
    n = len(steps)
    x0, x1 = 90, 910
    gap = (x1 - x0) / (n - 1)
    body = f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="18" fill="{c["card2"]}" stroke="{c["border"]}"/>'
    body += f'<line x1="{x0}" y1="80" x2="{x1}" y2="80" stroke="{c["border"]}" stroke-width="3" stroke-dasharray="6 6"/>'
    dur = n * 1.5
    for i, (num, ti, sub) in enumerate(steps):
        x = x0 + i * gap
        a, b = i / n, (i + 1) / n
        kt = f"0;{a:.3f};{a+.01:.3f};{b:.3f};{min(b+.01,1):.3f};1"
        body += (f'<circle cx="{x}" cy="80" r="26" fill="{c["card"]}" stroke="{c["a1"]}" stroke-width="2"/>'
                 f'<circle cx="{x}" cy="80" r="26" fill="{c["a1"]}" opacity="0"><animate attributeName="opacity" values="0;0;.35;.35;0;0" keyTimes="{kt}" dur="{dur}s" repeatCount="indefinite"/></circle>'
                 f'<text x="{x}" y="85" text-anchor="middle" font-family="{MONO}" font-size="14" font-weight="800" fill="{c["a1"]}">{num}</text>'
                 f'<text x="{x}" y="132" text-anchor="middle" font-family="{SANS}" font-size="16" font-weight="800" fill="{c["text"]}">{ti}</text>'
                 f'<text x="{x}" y="152" text-anchor="middle" font-family="{MONO}" font-size="11.5" fill="{c["muted"]}">{esc(sub)}</text>')
    body += (f'<circle r="6" fill="{c["a2"]}"><animateMotion dur="{dur}s" repeatCount="indefinite" path="M{x0},80 L{x1},80"/></circle>'
             f'<circle r="12" fill="{c["a2"]}" opacity=".25"><animateMotion dur="{dur}s" repeatCount="indefinite" path="M{x0},80 L{x1},80"/></circle>')
    return svg(W, H, body, "", "Cómo entrego")


def principles(t, c):
    W, H = 1000, 176
    items = [("</>", "Clean Code", "Código legible, modular y con revisiones de pares.", "a1"),
             ("#!", "Seguridad primero", "Validación, roles y trazabilidad desde el diseño.", "a3"),
             ("→", "Entregas pequeñas", "Scrum, iteraciones cortas y feedback constante.", "a2"),
             ("§", "Todo documentado", "READMEs, APIs y decisiones que cualquiera entiende.", "warn")]
    body = ""
    for i, (ic, ti, tx, k) in enumerate(items):
        x = i * 257
        col = c[k]
        body += (f'<g transform="translate({x} 0)"><rect x=".5" y=".5" width="228" height="{H-1}" rx="14" fill="{c["card2"]}" stroke="{c["border"]}"/>'
                 f'<rect x="20" y="20" width="46" height="46" rx="12" fill="{col}" fill-opacity=".14" stroke="{col}" stroke-opacity=".5"/>'
                 f'<text x="43" y="49" text-anchor="middle" font-family="{MONO}" font-size="17" font-weight="800" fill="{col}">{esc(ic)}'
                 f'<animate attributeName="opacity" values="1;.55;1" dur="{3+i*.5}s" repeatCount="indefinite"/></text>'
                 f'<text x="20" y="98" font-family="{SANS}" font-size="16" font-weight="800" fill="{c["text"]}">{esc(ti)}</text>')
        for j, l in enumerate(wrap(tx, 26)):
            body += f'<text x="20" y="{120+j*18}" font-family="{SANS}" font-size="12.5" fill="{c["muted"]}">{esc(l)}</text>'
        body += "</g>"
    return svg(W, H, body, "", "Principios")


def loading(t, c):
    items = [("PCAP", "Python Institute · Certified Associate", "a2"), ("Cloud Fundamentals", "AWS / Microsoft Learn", "a3"),
             ("Ciberseguridad", "defensa · buenas prácticas · ética", "a1")]
    W, rh = 1000, 74
    H = 58 + rh * len(items)
    defs = ""
    body = f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="{c["card2"]}" stroke="{c["border"]}"/>'
    body += f'<text x="28" y="36" font-family="{MONO}" font-size="13" fill="{c["dim"]}">$ npm run learn --watch</text>'
    for i, (ti, sub, k) in enumerate(items):
        y = 58 + i * rh
        col = c[k]
        defs += (f'<linearGradient id="sh{i}" x1="0" x2="1"><stop offset="0" stop-color="{col}" stop-opacity="0"/><stop offset=".5" stop-color="{col}"/><stop offset="1" stop-color="{col}" stop-opacity="0"/></linearGradient>'
                 f'<clipPath id="cp{i}"><rect x="28" y="{y+26}" width="{W-56}" height="10" rx="5"/></clipPath>')
        body += (f'<text x="28" y="{y+14}" font-family="{SANS}" font-size="16" font-weight="800" fill="{c["text"]}">{esc(ti)}</text>'
                 f'<text x="{28+tw(ti,16)+14:.0f}" y="{y+14}" font-family="{MONO}" font-size="12" fill="{c["muted"]}">{esc(sub)}</text>'
                 f'<text x="{W-28}" y="{y+14}" text-anchor="end" font-family="{MONO}" font-size="12" font-weight="700" fill="{col}">[ loading... ]</text>'
                 f'<rect x="28" y="{y+26}" width="{W-56}" height="10" rx="5" fill="{c["chip"]}" stroke="{c["border"]}"/>'
                 f'<g clip-path="url(#cp{i})"><rect x="-300" y="{y+26}" width="300" height="10" fill="url(#sh{i})"><animate attributeName="x" from="-300" to="{W}" dur="{2.4+i*.5}s" repeatCount="indefinite"/></rect></g>')
    return svg(W, H, body, defs, "Aprendiendo")


def quote(t, c):
    W, H = 1000, 170
    defs = (f'<linearGradient id="qg" x1="0" x2="1"><stop offset="0" stop-color="{c["name1"]}"/><stop offset=".5" stop-color="{c["name2"]}"/><stop offset="1" stop-color="{c["name3"]}"/></linearGradient>')
    q = wrap("El software no solo se programa — se diseña, se estructura y se construye para resolver problemas reales.", 62)
    body = '<text x="40" y="100" font-family="Georgia, serif" font-size="120" fill="url(#qg)" opacity=".4">“</text>'
    for i, l in enumerate(q):
        body += f'<text x="500" y="{74+i*36}" text-anchor="middle" font-family="Georgia, \'Times New Roman\', serif" font-size="26" font-style="italic" fill="{c["text"]}">{esc(l)}</text>'
    body += f'<text x="500" y="{74+len(q)*36+8}" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{c["a1"]}" letter-spacing="2">— ROY BARRERA</text>'
    return svg(W, H, body, defs, "Cita")


OTHER = [("gestor-tareas-estudio", "TypeScript", "Gestor de tareas de estudio"), ("agenda-citas", "PHP", "Agenda de citas"),
         ("roy-portfolio", "JavaScript", "Portafolio personal (Next.js) · [en vivo](https://roy-portfolio-peach.vercel.app)"),
         ("qaLabMcpv2", "Python", "Laboratorio MCP — herramientas de QA"), ("2026-1GS241-barrera-roy", "TypeScript", "Trabajo universitario"),
         ("Lab5SFTVI", "Java", "Laboratorio Java"), ("EjemploValidacionesRoy", "PHP", "Validaciones en PHP"),
         ("apiSemestralIV", "C#", "API semestral"), ("frontendSoftwareV", "CSS", "Frontend de Software V")]


# ───────────────────────────── README ─────────────────────────────
def pic(name, alt, width=None, href=None):
    w = f' width="{width}"' if width else ""
    img = (f'<picture>\n  <source media="(prefers-color-scheme: dark)" srcset="./assets/{name}-dark.svg"/>\n'
           f'  <source media="(prefers-color-scheme: light)" srcset="./assets/{name}-light.svg"/>\n'
           f'  <img alt="{alt}"{w} src="./assets/{name}-dark.svg"/>\n</picture>')
    return f'<a href="{href}">\n{img}\n</a>' if href else img


RAW = "https://raw.githubusercontent.com/Roy-x24/Roy-x24/output"


def ext_pic(light, dark, alt, extra=""):
    return (f'<picture>\n  <source media="(prefers-color-scheme: dark)" srcset="{dark}"/>\n'
            f'  <source media="(prefers-color-scheme: light)" srcset="{light}"/>\n  <img {extra} alt="{alt}" src="{dark}"/>\n</picture>')


def section(*parts):
    return '<br/>\n\n<div align="center">\n\n' + "\n\n".join(parts) + '\n\n</div>\n'


def readme():
    U = "https://github.com/Roy-x24"
    S = []
    S.append('<div align="center">\n\n' + pic("hero", "Roy Barrera — Full Stack Developer", "100%") + '\n\n'
             '<a href="https://roy-portfolio-peach.vercel.app"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-Visitar-10b981?style=for-the-badge&logo=vercel&logoColor=white&labelColor=0f172a"/></a>\n'
             '<a href="https://www.linkedin.com/in/roy-barrera-0077b1340"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0f172a"/></a>\n'
             '<a href="mailto:roybarrera508@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-Contactar-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0f172a"/></a>\n<br/>\n'
             f'<a href="{U}"><img alt="Profile Views" src="https://komarev.com/ghpvc/?username=Roy-x24&style=for-the-badge&color=10b981&label=PROFILE+VIEWS"/></a>\n'
             f'<a href="{U}?tab=followers"><img alt="Followers" src="https://img.shields.io/github/followers/Roy-x24?style=for-the-badge&logo=github&color=0ea5e9&labelColor=0f172a"/></a>\n</div>\n')
    S.append(section(pic("terminal", "whoami", "100%"), pic("numbers", "Números", "100%")))
    S.append(section(pic("h-about", "About"), pic("codecard", "roy.ts", "100%")))
    S.append(section(pic("h-stack", "Tech Stack"), pic("orbit", "Órbita de tecnologías", "100%"), pic("stack", "Tech stack", "100%")))
    cards = ""
    for i, (slug, *_r) in enumerate(PROJECTS):
        cards += pic(f"card-{slug}", slug, "49%", f"{U}/{PROJ_URL[slug]}") + "\n"
        if i % 2 == 1:
            cards += "<br/>\n"
    cards += f'\n<a href="{U}?tab=repositories"><img alt="Ver todos" src="https://img.shields.io/badge/Ver_todos_los_repositorios-→-10b981?style=for-the-badge&labelColor=0f172a"/></a>'
    S.append(section(pic("h-projects", "Featured Repositories"), cards))
    S.append(section(pic("h-arch", "Under the Hood"), pic("arch", "Arquitectura", "100%", f"{U}/plataforma-reservas-turisticas")))
    S.append(section(pic("h-exp", "Experience"), pic("exp-ditic", "DITIC", "49%") + "\n" + pic("exp-ayudinga", "Ayudinga", "49%")))
    S.append(section(pic("h-edu", "Education"), pic("education", "Educación", "100%")))
    S.append(section(pic("h-flow", "How I Ship"), pic("pipeline", "Pipeline", "100%"), pic("principles", "Principios", "100%")))
    S.append(section(pic("h-loading", "Now Loading"), pic("loading", "Aprendiendo", "100%")))
    streak = "https://streak-stats.demolab.com?user=Roy-x24&background={bg}&border={bd}&stroke={bd}&ring={ring}&fire=f59e0b&currStreakNum={n}&sideNums={sn}&currStreakLabel={ring}&sideLabels={sn}&dates=64748b&border_radius=14"
    sd = streak.format(bg="0d1117", bd="1f2937", ring="10b981", n="22d3ee", sn="e2e8f0")
    sl = streak.format(bg="ffffff", bd="e2e8f0", ring="059669", n="0891b2", sn="0f172a")
    S.append(section(pic("h-stats", "Analytics"),
                     ext_pic(f"{RAW}/stats-light.svg", f"{RAW}/stats-dark.svg", "GitHub Stats", 'height="175"') + "\n" +
                     ext_pic(f"{RAW}/top-langs-light.svg", f"{RAW}/top-langs-dark.svg", "Top Languages", 'height="175"'),
                     ext_pic(sl, sd, "GitHub Streak")))
    S.append(section(pic("h-skills", "Skills"), pic("skills", "Skill calibration", "100%")))
    S.append(section(pic("h-snake", "Commit Snake"),
                     ext_pic(f"{RAW}/github-contribution-grid-snake.svg", f"{RAW}/github-contribution-grid-snake-dark.svg", "Snake animation")))
    rows = "\n".join(f"| [`{n}`]({U}/{n}) | {l} | {d} |" for n, l, d in OTHER)
    S.append('<br/>\n\n<details>\n<summary><b>📂 Más repositorios</b> — laboratorios, prácticas y proyectos académicos</summary>\n\n<br/>\n\n'
             '| Repositorio | Lenguaje | Descripción |\n|:---|:---:|:---|\n' + rows + '\n\n</details>\n')
    S.append(section(pic("quote", "Cita", "100%"), pic("contact", "Contacto", "100%", "mailto:roybarrera508@gmail.com") + "\n\n" +
                     '<a href="mailto:roybarrera508@gmail.com"><img alt="Gmail" src="https://img.shields.io/badge/Gmail-roybarrera508@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0f172a"/></a>\n'
                     '<a href="https://www.linkedin.com/in/roy-barrera-0077b1340"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Roy%20Barrera-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0f172a"/></a>\n'
                     '<a href="https://roy-portfolio-peach.vercel.app"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-roy--portfolio-10b981?style=for-the-badge&logo=vercel&logoColor=white&labelColor=0f172a"/></a>\n'
                     f'<a href="{U}"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-Roy--x24-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=0f172a"/></a>'))
    S.append(pic("footer", "Roy Barrera", "100%") + "\n")
    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(S))


EXP = [("ditic", "DITIC — UTP", "DESARROLLADOR WEB · PRÁCTICA PROFESIONAL",
        "Migración de sistemas legacy a arquitectura moderna Flask + Vue.js, con validación end-to-end y documentación técnica.",
        ["Flask", "Vue.js", "Python", "Docker"],
        ["Arquitectura MVC / API REST", "Componentes Vue.js modulares", "Ciclo completo de despliegue", "Documentación y control de versiones"], "a2"),
       ("ayudinga", "Fundación Ayudinga", "DESARROLLADOR FRONTEND · VOLUNTARIADO",
        "Interfaces modernas con React + Tailwind CSS bajo metodología Scrum, enfocadas en mantenibilidad y calidad.",
        ["React", "Tailwind CSS", "Git"],
        ["Metodología Scrum / Agile", "UI/UX responsivo y accesible", "Clean Code & Code Reviews", "Trabajo colaborativo remoto"], "a1")]

HEADS = [("about", "00", "About", "// sobre mí, en código"), ("stack", "01", "Tech Stack", "// herramientas con las que construyo"),
         ("projects", "02", "Featured Repositories", "// proyectos destacados"), ("arch", "03", "Under the Hood", "// así funciona por dentro"),
         ("exp", "04", "Transmission Log", "// experiencia"), ("edu", "05", "Knowledge Base", "// formación y certificaciones"),
         ("flow", "06", "How I Ship", "// de la idea al deploy"), ("loading", "07", "Now Loading", "// aprendiendo ahora"),
         ("stats", "08", "System Analytics", "// actividad en GitHub"), ("skills", "09", "Skill Calibration", "// nivel autoevaluado"),
         ("snake", "10", "Commit Snake", "// contribuciones")]


def main():
    for t, c in THEMES.items():
        for fn, nm in [(hero, "hero"), (terminal, "terminal"), (stack, "stack"), (education, "education"), (skills, "skills"),
                       (contact, "contact"), (footer, "footer"), (numbers, "numbers"), (codecard, "codecard"), (orbit, "orbit"),
                       (arch, "arch"), (pipeline, "pipeline"), (principles, "principles"), (loading, "loading"), (quote, "quote")]:
            save(nm, t, fn(t, c))
        for key, num, title, sub in HEADS:
            save(f"h-{key}", t, header(num, title, sub, c))
        mh = max(card_final(a, b, g, d, e, c, accent=f)[1] for a, b, g, d, e, f in PROJECTS)
        for slug, title, tag, desc, chips, acc in PROJECTS:
            sv, _ = card_final(slug, title, tag, desc, chips, c, accent=acc, minH=mh)
            save(f"card-{slug}", t, sv)
        mh2 = max(card_final(a, b, g, d, e, c, bullets=f, link=None, accent=h)[1] for a, b, g, d, e, f, h in EXP)
        for a, b, g, d, e, f, h in EXP:
            sv, _ = card_final(a, b, g, d, e, c, bullets=f, link=None, accent=h, minH=mh2)
            save(f"exp-{a}", t, sv)
    readme()
    print("ok")


if __name__ == "__main__":
    main()

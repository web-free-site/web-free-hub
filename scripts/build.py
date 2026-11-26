#!/usr/bin/env python3
"""Generate static hub pages, sitemap, favicon, and Open Graph image."""
from __future__ import annotations

import json
import html
import re
import sys
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from content_blocks import (
    ABOUT_BODY,
    CATEGORY_FAQ,
    CATEGORY_GUIDES,
    CONTACT_BODY,
    HOME_FAQ,
    HOME_GUIDES,
    HOME_INTRO,
    TOOL_FAQ,
    TOOL_STEPS,
    privacy_html,
    terms_html,
)

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data/tools.json").read_text(encoding="utf-8"))
CAT_PAGES = json.loads((ROOT / "data/category-pages.json").read_text(encoding="utf-8"))[
    "pages"
]
PUBLIC = ROOT / "public"

SITE = "https://web-free.site"
TITLE_EN = "Web Free — Free Online Tools"
TITLE_FR = "Web Free — Outils en ligne gratuits"
DESC_EN = (
    "Browse 50 free online tools on web-free.site: PDF editor, image compressor, "
    "JSON formatter, QR codes, speech-to-text, calculators, and video utilities. "
    "No sign-up, runs in your browser."
)
DESC_FR = (
    "Annuaire d’outils en ligne gratuits sur web-free.site : PDF, CV, devises, "
    "QR codes, images, factures et plus. Sans inscription."
)
HERO_EN = "Free online tools — PDF, images, video, and more"
HERO_FR = "Des outils en ligne gratuits, sans inscription."
INTRO_FR = (
    "Web Free rassemble des utilitaires gratuits qui s’utilisent dans le navigateur. "
    "Chaque outil vit sur son propre sous-domaine de web-free.site."
)
SEARCH_LABEL_EN = "Search all tools"
SEARCH_PLACEHOLDER_EN = "Search tools…"
NO_RESULTS_EN = "No tools match that search."
FOOT_FR = (
    "Tous les outils listés ici sont gratuits et s’utilisent dans le navigateur. "
    "Cette page renvoie vers chaque utilitaire en ligne sur web-free.site."
)
NOT_FOUND_EN = "This page does not exist."
NOT_FOUND_FR = "Cette page n’existe pas."
HOME_LINK_EN = "Back to home"
HOME_FR = "Retour aux outils"

POPULAR_SLUGS = [
    "free-pdf-converter",
    "free-word-counter",
    "free-image-resizer",
    "free-qr-code-creator",
    "free-background-remover",
    "free-password-generator",
    "free-currency-converter",
    "free-json-formatter",
]

CF_BEACON = (
    "<!-- Cloudflare Web Analytics -->"
    "<script defer src='https://static.cloudflareinsights.com/beacon.min.js' "
    "data-cf-beacon='{\"token\": \"3e2f5f96ab32442ebb6e6f650615b58a\"}'>"
    "</script><!-- End Cloudflare Web Analytics -->"
)
REF_JS = '<script src="https://ref.web-free.site/r.js" defer></script>'
GA_MEASUREMENT_ID = "G-8DG5MK8YPM"
GTAG = (
    "<!-- Google tag (gtag.js) -->"
    f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>'
    "<script>"
    "window.dataLayer = window.dataLayer || [];"
    "function gtag(){dataLayer.push(arguments);}"
    "gtag('js', new Date());"
    f"gtag('config', '{GA_MEASUREMENT_ID}');"
    "</script>"
)

ALL_TOOLS: list[dict] = []
TOOL_BY_SLUG: dict[str, dict] = {}
TOOL_CAT: dict[str, dict] = {}
CAT_BY_ID: dict[str, dict] = {c["id"]: c for c in DATA["categories"]}

for cat in DATA["categories"]:
    for tool in cat["tools"]:
        ALL_TOOLS.append(tool)
        TOOL_BY_SLUG[tool["slug"]] = tool
        TOOL_CAT[tool["slug"]] = cat

SLUG_TO_CAT_PAGE: dict[str, str] = {}
for page in CAT_PAGES:
    for cid in page.get("category_ids", []):
        for t in CAT_BY_ID.get(cid, {}).get("tools", []):
            SLUG_TO_CAT_PAGE[t["slug"]] = page["slug"]


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def tool_href(tool: dict, lang: str = "en") -> str:
    href = tool["url"]
    ref = "ref=hub-fr" if lang == "fr" else "ref=hub"
    if "ref=" not in href:
        href = href + ("&" if "?" in href else "?") + ref
    return href


def depth_prefix(depth: int) -> str:
    return "/" if depth == 0 else "../" * depth


def head_block(
    *,
    title: str,
    description: str,
    canonical: str,
    depth: int = 0,
    lang: str = "en",
    extra_json_ld: str | None = None,
    robots: str = "index,follow",
) -> str:
    p = depth_prefix(depth)
    lines = [
        "<head>",
        '  <meta charset="utf-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1">',
        f"  <title>{esc(title)}</title>",
        f'  <meta name="description" content="{esc(description)}">',
        f'  <link rel="canonical" href="{esc(canonical)}">',
    ]
    if lang == "en" and depth == 0 and canonical.rstrip("/") == SITE:
        lines += [
            f'  <link rel="alternate" hreflang="en" href="{SITE}/">',
            f'  <link rel="alternate" hreflang="fr" href="{SITE}/fr/">',
            f'  <link rel="alternate" hreflang="x-default" href="{SITE}/">',
        ]
    lines += [
        f'  <meta name="robots" content="{robots}">',
        '  <meta property="og:type" content="website">',
        '  <meta property="og:site_name" content="Web Free">',
        f'  <meta property="og:title" content="{esc(title)}">',
        f'  <meta property="og:description" content="{esc(description)}">',
        f'  <meta property="og:url" content="{esc(canonical)}">',
        f'  <meta property="og:image" content="{SITE}/og.png">',
        '  <meta property="og:image:width" content="1200">',
        '  <meta property="og:image:height" content="630">',
        '  <meta name="twitter:card" content="summary_large_image">',
        f'  <meta name="twitter:title" content="{esc(title)}">',
        f'  <meta name="twitter:description" content="{esc(description)}">',
        f'  <meta name="twitter:image" content="{SITE}/og.png">',
        f'  <link rel="icon" href="{p}favicon.svg" type="image/svg+xml">',
        f'  <link rel="icon" href="{p}favicon.ico" sizes="any">',
        f'  <link rel="apple-touch-icon" href="{p}apple-touch-icon.png">',
        f'  <link rel="stylesheet" href="{p}styles.css">',
    ]
    if extra_json_ld:
        lines.append('  <script type="application/ld+json">')
        lines.append(extra_json_ld)
        lines.append("  </script>")
    lines.append(f"  {GTAG}")
    lines.append(f"  {REF_JS}")
    lines.append("</head>")
    return "\n".join(lines)


def header_nav(depth: int = 0, lang: str = "en") -> str:
    p = depth_prefix(depth)
    home = f"{p}fr/" if lang == "fr" else (p if depth else "/")
    lang_link = (
        f'<a href="{p if lang == "fr" else p}fr/" lang="fr" hreflang="fr">Français</a>'
        if lang == "en"
        else f'<a href="{p if depth else "/"}">English</a>'
    )
    cat_prefix = "/category/" if depth == 0 else f"{p}category/"
    if lang == "en":
        nav_tools = (
            f'<a href="{cat_prefix}text-writing/">Writing</a> '
            f'<a href="{cat_prefix}image/">Image</a> '
            f'<a href="{cat_prefix}calculators/">Calculators</a> '
            f'<a href="{p}about/">About</a>'
        )
    else:
        nav_tools = ""
    return (
        '  <header class="site-header">\n'
        '    <div class="inner">\n'
        f'      <a class="wordmark" href="{home}">Web <span>Free</span></a>\n'
        f'      <nav class="site-nav" aria-label="{"Primary" if lang == "en" else "Langue"}">{nav_tools} {lang_link}</nav>\n'
        "    </div>\n"
        "  </header>\n"
    )


def footer_block(depth: int = 0, lang: str = "en") -> str:
    p = depth_prefix(depth)
    foot = (
        "All tools on web-free.site are free to use in your browser. "
        "This hub lists every live utility on the network."
        if lang == "en"
        else FOOT_FR
    )
    if lang == "en":
        fine = (
            f'<p class="fine">'
            f'<a href="{SITE}/">web-free.site</a> · '
            f'<a href="{p}about/">About</a> · '
            f'<a href="{p}contact/">Contact</a> · '
            f'<a href="{p}privacy/">Privacy</a> · '
            f'<a href="{p}terms/">Terms</a> · '
            f'<a href="{p}sitemap.xml">Sitemap</a>'
            f"</p>"
        )
    else:
        fine = (
            f'<p class="fine"><a href="{SITE}/">web-free.site</a> · '
            f'<a href="{p}privacy/">Privacy</a> · '
            f'<a href="{p}terms/">Terms</a> · '
            f'<a href="{p}sitemap.xml">Sitemap</a></p>'
        )
    return (
        '  <footer class="site-footer">\n'
        '    <div class="inner">\n'
        f"      <p>{esc(foot)}</p>\n"
        f"      {fine}\n"
        '      <p class="founded-by">Founded by '
        '<a href="https://gentil.quevvy.com" rel="author">Gentil M.</a></p>\n'
        "    </div>\n"
        "  </footer>\n"
    )


def breadcrumbs_ld(items: list[tuple[str, str]]) -> str:
    elements = []
    for i, (name, url) in enumerate(items, start=1):
        elements.append(
            {
                "@type": "ListItem",
                "position": i,
                "name": name,
                "item": url,
            }
        )
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": elements,
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def faq_ld(qas: list[tuple[str, str]]) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in qas
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def privacy_note(tool: dict) -> str:
    d = tool["desc_en"].lower()
    local_markers = (
        "no upload",
        "stays on your device",
        "never leave",
        "nothing is uploaded",
        "browser-only",
        "client-side",
        "not sent",
        "secrets never leave",
        "images stay",
        "data stays",
    )
    if any(m in d for m in local_markers) or (
        "in your browser" in d and "upload" not in d.replace("no upload", "")
    ):
        return (
            "For typical use, this tool is designed so your files or text are processed "
            "in your browser and are not uploaded to Web Free servers. Downloads may still "
            "remain on your device—close the tab when you finish with sensitive material."
        )
    return (
        "This tool may use your browser and network connections to complete its task "
        "(for example public exchange rates or loading scripts). Review the live tool "
        "before submitting confidential information."
    )


def tool_long_copy(tool: dict) -> str:
    name = tool["name"]
    base = tool["desc_en"]
    cat = TOOL_CAT[tool["slug"]]["name_en"]
    extra = (
        f"{name} is part of the Web Free {cat.lower()} collection on web-free.site. "
        f"You can open it without creating an account and use it from any modern browser. "
        f"The interface is kept focused so you can finish one job—export, download, or copy—"
        f"and move on. If you arrived from the hub, your link includes ?ref=hub for traffic attribution only. "
        f"For network-wide privacy and advertising practices, see the hub Privacy Policy."
    )
    text = f"{base} {extra}"
    words = text.split()
    if len(words) < 120:
        pad = (
            "The tool is maintained as a standalone subdomain so updates can ship without "
            "disrupting other utilities. When processing stays local, your content remains on "
            "your device for that session. Always keep backups of important originals before "
            "converting or editing files online, even when no upload is required."
        )
        text = f"{text} {pad}"
    return " ".join(text.split()[:200])


def tool_faqs(tool: dict) -> list[tuple[str, str]]:
    slug = tool["slug"]
    if slug in TOOL_FAQ:
        return TOOL_FAQ[slug]
    short = re.sub(r"^Free ", "", tool["name"])
    qas: list[tuple[str, str]] = [
        (
            f"Is {short} free to use?",
            "Yes. You can open the tool without creating a Web Free account. There is no paid tier on the hub listing.",
        ),
        (
            f"Does {short} require an install?",
            "No. It runs in a modern browser on its own web-free.site subdomain. Bookmark the live tool page if you use it often.",
        ),
    ]
    note = privacy_note(tool)
    if "in your browser" in tool["desc_en"].lower():
        qas.append(
            (
                "Where is my data processed?",
                note,
            )
        )
    return qas[:3]


def tool_steps(tool: dict) -> list[str]:
    custom = TOOL_STEPS.get(tool["slug"])
    if custom:
        return custom
    return [
        f"Open {tool['name']} using the button below (opens the live tool in a new context).",
        "Choose the option or mode that matches your task in the on-screen controls.",
        "Add your text, file, or settings and wait for the preview or result.",
        "Download, copy, or export the output, then close the tab on shared devices if needed.",
    ]


def tool_features(tool: dict) -> list[str]:
    desc = tool["desc_en"]
    parts = re.split(r"[.;]", desc)
    feats = [p.strip() for p in parts if len(p.strip()) > 8]
    if not feats:
        feats = ["Runs in the browser", "Free to use", "No hub account required"]
    return feats[:5]


def tools_for_page(page: dict) -> list[dict]:
    if page.get("tool_slugs"):
        return [TOOL_BY_SLUG[s] for s in page["tool_slugs"]]
    out = []
    for cid in page.get("category_ids", []):
        out.extend(CAT_BY_ID[cid]["tools"])
    return out


def related_tools(tool: dict, limit: int = 4) -> list[dict]:
    cat = TOOL_CAT[tool["slug"]]
    sibs = [t for t in cat["tools"] if t["slug"] != tool["slug"]]
    return sibs[:limit]


def other_categories(current_slug: str) -> list[dict]:
    return [p for p in CAT_PAGES if p["slug"] != current_slug]


def homepage_en() -> str:
    ld = []
    items = []
    for i, t in enumerate(ALL_TOOLS, start=1):
        items.append(
            {
                "@type": "ListItem",
                "position": i,
                "name": t["name"],
                "url": f"{SITE}/tools/{t['slug']}/",
            }
        )
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "name": "Web Free",
                "url": SITE + "/",
                "description": DESC_EN,
                "inLanguage": "en",
            },
            {
                "@type": "Organization",
                "name": "Web Free",
                "url": SITE + "/",
                "founder": {
                    "@type": "Person",
                    "name": "Gentil M.",
                    "url": "https://gentil.quevvy.com",
                },
            },
            {"@type": "ItemList", "name": "Free online tools", "numberOfItems": len(ALL_TOOLS), "itemListElement": items},
            json.loads(faq_ld(HOME_FAQ)),
        ],
    }
    extra_ld = json.dumps(graph, ensure_ascii=False, indent=2)

    popular_cards = []
    for slug in POPULAR_SLUGS:
        t = TOOL_BY_SLUG[slug]
        popular_cards.append(
            f'      <a class="card tool-card" href="/tools/{esc(t["slug"])}/">'
            f'<strong>{esc(t["name"])}</strong>'
            f'<span>{esc(t["desc_en"][:90])}…</span></a>'
        )

    cat_cards = []
    for page in CAT_PAGES:
        n = len(tools_for_page(page))
        cat_cards.append(
            f'      <a class="card cat-card" href="/category/{esc(page["slug"])}/">'
            f'<strong>{esc(page["title"])}</strong>'
            f'<span>{n} tools</span></a>'
        )

    directory = []
    for t in ALL_TOOLS:
        hay = f"{t['name']} {t['desc_en']} {TOOL_CAT[t['slug']]['name_en']}"
        directory.append(
            f'      <li class="tool hub-search-item" data-search="{esc(hay)}">'
            f'<a href="/tools/{esc(t["slug"])}/">{esc(t["name"])}</a>'
            f'<span class="desc">{esc(t["desc_en"])}</span></li>'
        )

    faq_html = []
    for q, a in HOME_FAQ:
        faq_html.append(f"      <details class=\"faq-item\"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>")

    guide_blocks = []
    for gtitle, gbody in HOME_GUIDES:
        guide_blocks.append(f"      <h3>{esc(gtitle)}</h3>")
        guide_blocks.append(f"      <p>{esc(gbody)}</p>")

    intro_paras = "".join(f"<p>{esc(p)}</p>" for p in HOME_INTRO.strip().split("\n\n"))

    return "\n".join(
        [
            "<!DOCTYPE html>",
            '<html lang="en">',
            head_block(
                title=TITLE_EN,
                description=DESC_EN,
                canonical=f"{SITE}/",
                extra_json_ld=extra_ld,
            ),
            "<body>",
            '  <a class="skip" href="#main">Skip to content</a>',
            header_nav(0, "en"),
            '  <main id="main">',
            '    <section class="hero">',
            f'      <p class="kicker">{len(ALL_TOOLS)} free tools</p>',
            f"      <h1>{esc(HERO_EN)}</h1>",
            '      <p class="lede">Search, browse categories, or open a popular tool—no account required.</p>',
            "    </section>",
            '    <form class="filter" role="search" action="#" method="get">',
            f'      <label for="tool-filter">{esc(SEARCH_LABEL_EN)}</label>',
            f'      <input id="tool-filter" type="search" name="q" placeholder="{esc(SEARCH_PLACEHOLDER_EN)}" autocomplete="off">',
            "    </form>",
            f'    <p id="no-results" hidden>{esc(NO_RESULTS_EN)}</p>',
            '    <section class="panel" aria-labelledby="h-popular">',
            '      <h2 id="h-popular">Popular tools</h2>',
            '      <div class="card-grid">',
            *popular_cards,
            "      </div>",
            "    </section>",
            '    <section class="panel" aria-labelledby="h-cats">',
            '      <h2 id="h-cats">Browse by category</h2>',
            '      <div class="card-grid category-grid">',
            *cat_cards,
            "      </div>",
            "    </section>",
            '    <section class="prose intro-block">',
            intro_paras,
            "    </section>",
            '    <section class="panel prose how-to-guides" aria-labelledby="h-guides">',
            '      <h2 id="h-guides">How-to guides</h2>',
            *guide_blocks,
            "    </section>",
            '    <section class="panel directory" aria-labelledby="h-all">',
            '      <h2 id="h-all">All tools</h2>',
            '      <ul class="tool-list directory-list">',
            *directory,
            "      </ul>",
            "    </section>",
            '    <section class="panel faq" aria-labelledby="h-faq">',
            '      <h2 id="h-faq">Frequently asked questions</h2>',
            *faq_html,
            "    </section>",
            "  </main>",
            footer_block(0, "en"),
            '  <script src="/filter.js" defer></script>',
            f"  {CF_BEACON}",
            "</body>",
            "</html>",
            "",
        ]
    )


def tool_page(tool: dict) -> str:
    slug = tool["slug"]
    cat = TOOL_CAT[slug]
    cat_page_slug = SLUG_TO_CAT_PAGE.get(slug, cat["id"])
    short = re.sub(r"^Free ", "", tool["name"])
    title = f"Free {short} — online browser tool, no sign-up"
    meta = tool["desc_en"]
    if len(meta) > 155:
        meta = meta[:152] + "…"
    canonical = f"{SITE}/tools/{slug}/"
    crumbs = [
        ("Home", f"{SITE}/"),
        (cat["name_en"], f"{SITE}/category/{cat_page_slug}/"),
        (tool["name"], canonical),
    ]
    crumbs_html = '    <nav class="breadcrumbs" aria-label="Breadcrumb">'
    crumbs_html += '<a href="/">Home</a> <span aria-hidden="true">/</span> '
    crumbs_html += f'<a href="/category/{esc(cat_page_slug)}/">{esc(cat["name_en"])}</a> '
    crumbs_html += f'<span aria-hidden="true">/</span> <span>{esc(tool["name"])}</span></nav>'

    steps = tool_steps(tool)
    feats = tool_features(tool)
    rel = related_tools(tool)
    body = tool_long_copy(tool)
    short_name = short

    graph_nodes: list = [
        json.loads(breadcrumbs_ld(crumbs)),
        {
            "@type": "SoftwareApplication",
            "name": tool["name"],
            "url": tool_href(tool),
            "applicationCategory": "UtilitiesApplication",
            "operatingSystem": "Web Browser",
                "description": tool["desc_en"],
                "isAccessibleForFree": True,
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
            },
    ]
    tool_qas = tool_faqs(tool)
    if tool_qas:
        graph_nodes.append(json.loads(faq_ld(tool_qas)))
    app_ld = {"@context": "https://schema.org", "@graph": graph_nodes}
    extra_ld = json.dumps(app_ld, ensure_ascii=False, indent=2)

    rel_html = []
    for r in rel:
        rel_html.append(
            f'        <a class="card tool-card" href="/tools/{esc(r["slug"])}/">{esc(r["name"])}</a>'
        )

    faq_section: list[str] = []
    if tool_qas:
        faq_items = []
        for q, a in tool_qas:
            faq_items.append(
                f'      <details class="faq-item"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>'
            )
        faq_section = [
            '    <section class="panel faq" aria-labelledby="h-tfaq">',
            '      <h2 id="h-tfaq">FAQ</h2>',
            *faq_items,
            "    </section>",
        ]

    hub_links = (
        f'      <p>Part of the <a href="/">Web Free hub</a> — '
        f'<a href="/category/{esc(cat_page_slug)}/">{esc(cat["name_en"])}</a> '
        f'(<a href="/tools/{esc(slug)}/">this page</a>).</p>'
    )

    return "\n".join(
        [
            "<!DOCTYPE html>",
            '<html lang="en">',
            head_block(title=title, description=meta, canonical=canonical, depth=2, extra_json_ld=extra_ld),
            "<body>",
            '  <a class="skip" href="#main">Skip to content</a>',
            header_nav(2, "en"),
            '  <main id="main" class="tool-detail">',
            crumbs_html,
            f"    <h1>{esc(tool['name'])}</h1>",
            '    <p class="lede">',
            f'      <a class="btn btn-primary" href="{esc(tool_href(tool))}">Open {esc(short_name)}</a>',
            "</p>",
            '    <section class="prose">',
            f"      <p>{esc(body)}</p>",
            "      <h2>How to use</h2>",
            "      <ol>",
            *[f"        <li>{esc(s)}</li>" for s in steps],
            "      </ol>",
            "      <h2>Key features</h2>",
            "      <ul>",
            *[f"        <li>{esc(f)}</li>" for f in feats],
            "      </ul>",
            "      <h2>Privacy note</h2>",
            f"      <p>{esc(privacy_note(tool))}</p>",
            hub_links,
            "    </section>",
            *faq_section,
            '    <section class="panel" aria-labelledby="h-related">',
            '      <h2 id="h-related">Related tools</h2>',
            '      <div class="card-grid">',
            *rel_html,
            "      </div>",
            "    </section>",
            "  </main>",
            footer_block(2, "en"),
            f"  {CF_BEACON}",
            "</body>",
            "</html>",
            "",
        ]
    )


def category_page(page: dict) -> str:
    slug = page["slug"]
    title = f"{page['title']} | Web Free"
    tools = tools_for_page(page)
    desc = f"Free {slug.replace('-', ' ')} tools in your browser—{len(tools)} utilities on web-free.site. No sign-up."
    canonical = f"{SITE}/category/{slug}/"
    qas = CATEGORY_FAQ.get(slug, [
        (
            "Are these tools free?",
            "Yes. Every tool listed here is free to open and does not require a Web Free account.",
        ),
        (
            "Where do the tools run?",
            "Each tool opens on its own web-free.site subdomain. Most are built for browser use; see each tool page for privacy details.",
        ),
    ])
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            json.loads(breadcrumbs_ld([("Home", f"{SITE}/"), (page["title"], canonical)])),
            json.loads(faq_ld(qas)),
        ],
    }
    extra_ld = json.dumps(graph, ensure_ascii=False, indent=2)

    cards = []
    for t in tools:
        cards.append(
            f'      <a class="card tool-card" href="/tools/{esc(t["slug"])}/">'
            f"<strong>{esc(t['name'])}</strong>"
            f'<span>{esc(t["desc_en"])}</span></a>'
        )

    intro = "".join(f"<p>{esc(para)}</p>" for para in page["intro"].strip().split("\n\n"))

    guide_bits = []
    for para in CATEGORY_GUIDES.get(slug, []):
        guide_bits.append(f"<p>{esc(para)}</p>")
    guide_section = []
    if guide_bits:
        guide_section = [
            '    <section class="panel prose" aria-labelledby="h-cguide">',
            '      <h2 id="h-cguide">Quick picks</h2>',
            "".join(guide_bits),
            "    </section>",
        ]

    other = []
    for p in other_categories(slug)[:6]:
        other.append(f'        <a href="/category/{esc(p["slug"])}/">{esc(p["title"])}</a>')

    faq_html = []
    for q, a in qas:
        faq_html.append(f"      <details class=\"faq-item\"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>")

    return "\n".join(
        [
            "<!DOCTYPE html>",
            '<html lang="en">',
            head_block(title=title, description=desc, canonical=canonical, depth=2, extra_json_ld=extra_ld),
            "<body>",
            '  <a class="skip" href="#main">Skip to content</a>',
            header_nav(2, "en"),
            '  <main id="main">',
            '    <nav class="breadcrumbs" aria-label="Breadcrumb">',
            '      <a href="/">Home</a> <span aria-hidden="true">/</span>',
            f"      <span>{esc(page['title'])}</span>",
            "    </nav>",
            f"    <h1>{esc(page['title'])}</h1>",
            f'    <section class="prose">{intro}</section>',
            *guide_section,
            '    <section class="panel" aria-labelledby="h-tools">',
            '      <h2 id="h-tools">Tools in this category</h2>',
            '      <div class="card-grid">',
            *cards,
            "      </div>",
            "    </section>",
            '    <section class="panel faq" aria-labelledby="h-cfaq">',
            '      <h2 id="h-cfaq">FAQ</h2>',
            *faq_html,
            "    </section>",
            '    <section class="panel" aria-labelledby="h-other">',
            '      <h2 id="h-other">Other categories</h2>',
            '      <p class="cat-links">',
            " · ".join(other),
            "</p>",
            "    </section>",
            "  </main>",
            footer_block(2, "en"),
            f"  {CF_BEACON}",
            "</body>",
            "</html>",
            "",
        ]
    )


def simple_page(
    *,
    title: str,
    h1: str,
    description: str,
    path: str,
    body_html: str,
    depth: int = 1,
) -> str:
    canonical = f"{SITE}/{path.strip('/')}/"
    return "\n".join(
        [
            "<!DOCTYPE html>",
            '<html lang="en">',
            head_block(title=title, description=description, canonical=canonical, depth=depth),
            "<body>",
            '  <a class="skip" href="#main">Skip to content</a>',
            header_nav(depth, "en"),
            '  <main id="main" class="prose legal-page">',
            f"    <h1>{esc(h1)}</h1>",
            body_html,
            "  </main>",
            footer_block(depth, "en"),
            f"  {CF_BEACON}",
            "</body>",
            "</html>",
            "",
        ]
    )


def page_fr() -> str:
    """French tool listing (legacy layout, updated footer)."""
    is_fr = True
    canonical = f"{SITE}/fr/"
    title = TITLE_FR
    desc = DESC_FR
    hero = HERO_FR
    intro = INTRO_FR
    foot = FOOT_FR
    tools_label = "outils gratuits"
    search_label = "Filtrer les outils"
    search_ph = "Rechercher un outil…"
    no_results = "Aucun outil ne correspond à cette recherche."
    cats_nav = "Catégories"

    toc_links = []
    sections = []
    for cat in DATA["categories"]:
        cat_name = cat["name_fr"]
        toc_links.append(
            f'      <a href="#{esc(cat["id"])}" data-cat="{esc(cat["id"])}">{esc(cat_name)}</a>'
        )
        rows = []
        for tool in cat["tools"]:
            tdesc = tool["desc_fr"]
            hay = f"{tool['name']} {tdesc}"
            rows.append(
                "      <li class=\"tool\" data-search=\"{hay}\">\n"
                "        <a href=\"{url}\">{name}</a>\n"
                "        <span class=\"desc\">{desc}</span>\n"
                "      </li>".format(
                    hay=esc(hay),
                    url=esc(tool_href(tool, "fr")),
                    name=esc(tool["name"]),
                    desc=esc(tdesc),
                )
            )
        sections.append(
            "  <section class=\"category\" id=\"{cid}\" aria-labelledby=\"h-{cid}\">\n"
            "    <h2 id=\"h-{cid}\">{cname}</h2>\n"
            "    <ul class=\"tool-list\">\n{rows}\n    </ul>\n"
            "  </section>".format(cid=esc(cat["id"]), cname=esc(cat_name), rows="\n".join(rows))
        )

    items = []
    for i, t in enumerate(ALL_TOOLS, start=1):
        items.append(
            {
                "@type": "ListItem",
                "position": i,
                "name": t["name"],
                "url": t["url"],
                "description": t["desc_fr"],
            }
        )
    json_ld_str = json.dumps(
        {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "WebSite",
                    "name": "Web Free",
                    "url": SITE + "/",
                    "description": desc,
                    "inLanguage": "fr",
                },
                {
                    "@type": "ItemList",
                    "name": "Outils en ligne gratuits",
                    "numberOfItems": len(ALL_TOOLS),
                    "itemListElement": items,
                },
            ],
        },
        ensure_ascii=False,
        indent=2,
    )

    return "\n".join(
        [
            "<!DOCTYPE html>",
            '<html lang="fr">',
            head_block(title=title, description=desc, canonical=canonical, extra_json_ld=json_ld_str),
            "<body>",
            '  <a class="skip" href="#main">Aller au contenu</a>',
            header_nav(0, "fr"),
            '  <main id="main">',
            '    <section class="hero">',
            f'      <p class="kicker">{len(ALL_TOOLS)} {esc(tools_label)}</p>',
            f"      <h1>{esc(hero)}</h1>",
            f'      <p class="lede">{esc(intro)}</p>',
            "    </section>",
            f'    <nav class="toc" aria-label="{esc(cats_nav)}">',
            *toc_links,
            "    </nav>",
            '    <form class="filter" role="search" action="#" method="get">',
            f'      <label for="tool-filter">{esc(search_label)}</label>',
            f'      <input id="tool-filter" type="search" name="q" placeholder="{esc(search_ph)}" autocomplete="off">',
            "    </form>",
            f'    <p id="no-results" hidden>{esc(no_results)}</p>',
            *sections,
            "  </main>",
            footer_block(0, "fr"),
            '  <script src="/filter.js" defer></script>',
            f"  {CF_BEACON}",
            "</body>",
            "</html>",
            "",
        ]
    )


def not_found() -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page not found — Web Free</title>
  <meta name="robots" content="noindex">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/styles.css">
  {GTAG}
  {REF_JS}
</head>
<body>
  {header_nav(0, "en").strip()}
  <main class="hero" id="main">
    <p class="kicker">404</p>
    <h1>{esc(NOT_FOUND_EN)}</h1>
    <p class="lede">{esc(NOT_FOUND_FR)}</p>
    <p><a class="home-link" href="/">{esc(HOME_LINK_EN)}</a> · <a class="home-link" href="/fr/">{esc(HOME_FR)}</a></p>
  </main>
  {footer_block(0, "en").strip()}
  {CF_BEACON}
</body>
</html>
"""


def sitemap_xml(urls: list[str]) -> str:
    today = date.today().isoformat()
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for loc in urls:
        pri = "1.0" if loc in (f"{SITE}/",) else "0.7"
        if "/tools/" in loc:
            pri = "0.8"
        parts += [
            "  <url>",
            f"    <loc>{loc}</loc>",
            f"    <lastmod>{today}</lastmod>",
            "    <changefreq>weekly</changefreq>",
            f"    <priority>{pri}</priority>",
        ]
        if loc == f"{SITE}/":
            parts += [
                f'    <xhtml:link rel="alternate" hreflang="en" href="{SITE}/"/>',
                f'    <xhtml:link rel="alternate" hreflang="fr" href="{SITE}/fr/"/>',
            ]
        parts.append("  </url>")
    parts.append("</urlset>")
    return "\n".join(parts) + "\n"


def robots() -> str:
    return "User-agent: *\nAllow: /\n\nSitemap: {}/sitemap.xml\n".format(SITE)


# --- favicon / og (unchanged logic) ---

def write_favicon_svg() -> str:
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" role="img" aria-label="Web Free">
  <rect width="32" height="32" rx="7" fill="#0c6b4d"/>
  <text x="16" y="23" text-anchor="middle" font-family="Georgia, 'IBM Plex Serif', serif" font-size="18" font-weight="700" fill="#f4efe6">W</text>
</svg>
'''


def font(path_candidates, size: int) -> ImageFont.FreeTypeFont:
    for p in path_candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size=size)
    return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size=size)


def make_og():
    w, h = 1200, 630
    img = Image.new("RGB", (w, h), "#f4efe6")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, w, 16], fill="#0c6b4d")
    draw.rectangle([0, h - 16, w, h], fill="#0c6b4d")
    serif = font(
        [
            "/usr/share/fonts/truetype/sand-box/google/IBM Plex Serif/IBMPlexSerif-SemiBold.ttf",
            "/usr/share/fonts/truetype/sand-box/google/IBM Plex Serif/IBMPlexSerif-Bold.ttf",
        ],
        96,
    )
    sans = font(
        [
            "/usr/share/fonts/truetype/inter/Inter-Regular.ttf",
            "/usr/share/fonts/truetype/inter/Inter[opsz,wght].ttf",
        ],
        36,
    )
    small = font(
        [
            "/usr/share/fonts/truetype/inter/Inter-Regular.ttf",
            "/usr/share/fonts/truetype/inter/Inter[opsz,wght].ttf",
        ],
        28,
    )
    draw.text((80, 150), "Web Free", font=serif, fill="#171614")
    draw.text((80, 280), "Free online tools, no sign-up.", font=sans, fill="#0c6b4d")
    draw.text((80, 360), f"{len(ALL_TOOLS)} browser utilities on web-free.site", font=small, fill="#5f5a52")
    img.save(PUBLIC / "og.png", "PNG", optimize=True)

    mark = Image.new("RGB", (180, 180), "#0c6b4d")
    mdraw = ImageDraw.Draw(mark)
    wfont = font(
        [
            "/usr/share/fonts/truetype/sand-box/google/IBM Plex Serif/IBMPlexSerif-Bold.ttf",
            "/usr/share/fonts/truetype/sand-box/google/IBM Plex Serif/IBMPlexSerif-SemiBold.ttf",
        ],
        120,
    )
    bbox = mdraw.textbbox((0, 0), "W", font=wfont)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    mdraw.text(((180 - tw) / 2 - bbox[0], (180 - th) / 2 - bbox[1] - 4), "W", font=wfont, fill="#f4efe6")
    mark.save(PUBLIC / "apple-touch-icon.png", "PNG", optimize=True)
    ico = mark.resize((32, 32), Image.Resampling.LANCZOS)
    ico.save(PUBLIC / "favicon.ico", format="ICO", sizes=[(32, 32)])


def collect_urls() -> list[str]:
    urls = [f"{SITE}/", f"{SITE}/fr/", f"{SITE}/about/", f"{SITE}/contact/", f"{SITE}/privacy/", f"{SITE}/terms/"]
    for page in CAT_PAGES:
        urls.append(f"{SITE}/category/{page['slug']}/")
    for t in ALL_TOOLS:
        urls.append(f"{SITE}/tools/{t['slug']}/")
    return urls


def check_internal_links() -> int:
    """Return number of broken relative links in generated HTML."""
    errors = []
    for path in PUBLIC.rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        depth = len(path.relative_to(PUBLIC).parts) - 1
        for m in re.finditer(r'href="([^"#?]+)"', text):
            href = m.group(1)
            if href.startswith(("http", "mailto:", "javascript:")):
                continue
            if href.startswith("/"):
                rel = href.lstrip("/")
                target = PUBLIC / rel
            else:
                target = (path.parent / href).resolve()
            if href.endswith("/") or not target.suffix:
                if target.is_dir() or href.endswith("/"):
                    target = target / "index.html"
            if not target.exists():
                errors.append((str(path.relative_to(PUBLIC)), href))
    if errors:
        for p, h in errors[:30]:
            print(f"broken link: {p} -> {h}", file=sys.stderr)
    return len(errors)


def main() -> None:
    PUBLIC.mkdir(parents=True, exist_ok=True)
    (PUBLIC / "fr").mkdir(parents=True, exist_ok=True)
    (PUBLIC / "category").mkdir(parents=True, exist_ok=True)
    (PUBLIC / "tools").mkdir(parents=True, exist_ok=True)
    for sub in ("about", "contact", "privacy", "terms"):
        (PUBLIC / sub).mkdir(parents=True, exist_ok=True)

    (PUBLIC / "index.html").write_text(homepage_en(), encoding="utf-8")
    (PUBLIC / "fr/index.html").write_text(page_fr(), encoding="utf-8")
    (PUBLIC / "404.html").write_text(not_found(), encoding="utf-8")

    for page in CAT_PAGES:
        out = PUBLIC / "category" / page["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(category_page(page), encoding="utf-8")

    for tool in ALL_TOOLS:
        out = PUBLIC / "tools" / tool["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(tool_page(tool), encoding="utf-8")

    (PUBLIC / "about/index.html").write_text(
        simple_page(
            title="About Web Free — free browser tools directory",
            h1="About Web Free",
            description="What the web-free.site hub is, how the tool network works, and how we list free browser utilities.",
            path="about",
            body_html=(
                "<p>" + esc(ABOUT_BODY).replace("\n\n", "</p><p>") + "</p>"
                "<p>web-free.site was founded by "
                '<a href="https://gentil.quevvy.com" rel="author">Gentil M.</a>, '
                "a full-stack developer based in Kigali, Rwanda.</p>"
            ),
        ),
        encoding="utf-8",
    )
    (PUBLIC / "contact/index.html").write_text(
        simple_page(
            title="Contact — Web Free",
            h1="Contact",
            description="How to reach the maintainers of the web-free.site free tools network.",
            path="contact",
            body_html="<p>" + esc(CONTACT_BODY).replace("\n\n", "</p><p>") + "</p>",
        ),
        encoding="utf-8",
    )
    (PUBLIC / "privacy/index.html").write_text(
        simple_page(
            title="Privacy Policy — web-free.site network",
            h1="Privacy Policy",
            description="Privacy practices for web-free.site and all *.web-free.site tool subdomains: ads, analytics, browser processing, and cookies.",
            path="privacy",
            body_html=privacy_html(SITE),
        ),
        encoding="utf-8",
    )
    (PUBLIC / "terms/index.html").write_text(
        simple_page(
            title="Terms of Use — web-free.site network",
            h1="Terms of Use",
            description="Terms governing use of web-free.site and every free tool subdomain on the network.",
            path="terms",
            body_html=terms_html(),
        ),
        encoding="utf-8",
    )

    urls = collect_urls()
    (PUBLIC / "sitemap.xml").write_text(sitemap_xml(urls), encoding="utf-8")
    (PUBLIC / "robots.txt").write_text(robots(), encoding="utf-8")
    (PUBLIC / "favicon.svg").write_text(write_favicon_svg(), encoding="utf-8")
    shutil_copy_tools_json()
    make_og()

    broken = check_internal_links()
    page_count = len(list(PUBLIC.rglob("index.html"))) + 1  # +404
    print(f"built {len(ALL_TOOLS)} tools, {page_count} HTML pages, {len(urls)} sitemap URLs → {PUBLIC}")
    if broken:
        sys.exit(1)


def shutil_copy_tools_json() -> None:
    (PUBLIC / "tools.json").write_text(
        json.dumps(DATA, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
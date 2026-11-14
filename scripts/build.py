#!/usr/bin/env python3
"""Generate static hub pages, sitemap, favicon, and Open Graph image."""
from __future__ import annotations

import json
import html
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data/tools.json").read_text(encoding="utf-8"))
PUBLIC = ROOT / "public"

SITE = "https://web-free.site"
TITLE_EN = "Web Free — Free Online Tools"
TITLE_FR = "Web Free — Outils en ligne gratuits"
DESC_EN = (
    "A directory of free browser tools on web-free.site — PDF, CV, currency, "
    "QR codes, images, invoices, and more. No sign-up required."
)
DESC_FR = (
    "Annuaire d’outils en ligne gratuits sur web-free.site : PDF, CV, devises, "
    "QR codes, images, factures et plus. Sans inscription."
)
HERO_EN = "Free online tools, no sign-up."
HERO_FR = "Des outils en ligne gratuits, sans inscription."
INTRO_EN = (
    "Web Free is a set of free utilities that run in your browser. "
    "Each tool lives on its own subdomain of web-free.site."
)
INTRO_FR = (
    "Web Free rassemble des utilitaires gratuits qui s’utilisent dans le navigateur. "
    "Chaque outil vit sur son propre sous-domaine de web-free.site."
)
OPEN_EN = "Open tool"
OPEN_FR = "Ouvrir l’outil"
FOOT_EN = (
    "All tools listed here are free to use in your browser. "
    "This page links every live utility on web-free.site."
)
FOOT_FR = (
    "Tous les outils listés ici sont gratuits et s’utilisent dans le navigateur. "
    "Cette page renvoie vers chaque utilitaire en ligne sur web-free.site."
)
TOOLS_LABEL_EN = "free tools"
TOOLS_LABEL_FR = "outils gratuits"
NOT_FOUND_EN = "This page does not exist."
NOT_FOUND_FR = "Cette page n’existe pas."
HOME_EN = "Back to all tools"
HOME_FR = "Retour aux outils"

ALL_TOOLS = [t for c in DATA["categories"] for t in c["tools"]]


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def json_ld(lang: str) -> str:
    desc = DESC_FR if lang == "fr" else DESC_EN
    url = f"{SITE}/fr/" if lang == "fr" else f"{SITE}/"
    items = []
    for i, t in enumerate(ALL_TOOLS, start=1):
        items.append(
            {
                "@type": "ListItem",
                "position": i,
                "name": t["name"],
                "url": t["url"],
                "description": t["desc_fr"] if lang == "fr" else t["desc_en"],
            }
        )
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "name": "Web Free",
                "url": SITE + "/",
                "description": desc,
                "inLanguage": "fr" if lang == "fr" else "en",
            },
            {
                "@type": "ItemList",
                "name": "Free online tools" if lang == "en" else "Outils en ligne gratuits",
                "numberOfItems": len(ALL_TOOLS),
                "itemListElement": items,
            },
        ],
    }
    return json.dumps(graph, ensure_ascii=False, indent=2)


def page(lang: str) -> str:
    is_fr = lang == "fr"
    canonical = f"{SITE}/fr/" if is_fr else f"{SITE}/"
    title = TITLE_FR if is_fr else TITLE_EN
    desc = DESC_FR if is_fr else DESC_EN
    hero = HERO_FR if is_fr else HERO_EN
    intro = INTRO_FR if is_fr else INTRO_EN
    open_label = OPEN_FR if is_fr else OPEN_EN
    foot = FOOT_FR if is_fr else FOOT_EN
    tools_label = TOOLS_LABEL_FR if is_fr else TOOLS_LABEL_EN
    og_locale = "fr_FR" if is_fr else "en_US"
    nav_other = (
        '<a href="/" lang="en" hreflang="en">English</a>'
        if is_fr
        else '<a href="/fr/" lang="fr" hreflang="fr">Français</a>'
    )

    sections = []
    for cat in DATA["categories"]:
        cat_name = cat["name_fr"] if is_fr else cat["name_en"]
        cards = []
        for t in cat["tools"]:
            tdesc = t["desc_fr"] if is_fr else t["desc_en"]
            cards.append(
                f'''    <a class="card" href="{esc(t["url"])}">
      <h3>{esc(t["name"])}</h3>
      <p>{esc(tdesc)}</p>
      <span class="go">{esc(open_label)} <span aria-hidden="true">→</span></span>
    </a>'''
            )
        sections.append(
            f'''  <section class="category" id="{esc(cat["id"])}" aria-labelledby="h-{esc(cat["id"])}">
    <h2 id="h-{esc(cat["id"])}">{esc(cat_name)}</h2>
    <div class="grid">
{chr(10).join(cards)}
    </div>
  </section>'''
        )

    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <link rel="canonical" href="{esc(canonical)}">
  <link rel="alternate" hreflang="en" href="{SITE}/">
  <link rel="alternate" hreflang="fr" href="{SITE}/fr/">
  <link rel="alternate" hreflang="x-default" href="{SITE}/">
  <meta name="robots" content="index,follow">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Web Free">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{esc(canonical)}">
  <meta property="og:image" content="{SITE}/og.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:locale:alternate" content="{"en_US" if is_fr else "fr_FR"}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(desc)}">
  <meta name="twitter:image" content="{SITE}/og.png">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="stylesheet" href="/styles.css">
  <script type="application/ld+json">
{json_ld(lang)}
  </script>
</head>
<body>
  <a class="skip" href="#main">{"Aller au contenu" if is_fr else "Skip to content"}</a>
  <header class="site-header">
    <div class="inner">
      <a class="wordmark" href="{ "/fr/" if is_fr else "/" }">Web <span>Free</span></a>
      <nav aria-label="{"Langue" if is_fr else "Language"}">{nav_other}</nav>
    </div>
  </header>
  <main id="main">
    <section class="hero">
      <p class="kicker">{len(ALL_TOOLS)} {esc(tools_label)}</p>
      <h1>{esc(hero)}</h1>
      <p class="lede">{esc(intro)}</p>
    </section>
{chr(10).join(sections)}
  </main>
  <footer class="site-footer">
    <div class="inner">
      <p>{esc(foot)}</p>
      <p class="fine"><a href="{SITE}/">web-free.site</a> · <a href="/sitemap.xml">Sitemap</a></p>
    </div>
  </footer>
</body>
</html>
'''


def not_found() -> str:
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page not found — Web Free</title>
  <meta name="robots" content="noindex">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
  <header class="site-header">
    <div class="inner">
      <a class="wordmark" href="/">Web <span>Free</span></a>
    </div>
  </header>
  <main class="hero">
    <p class="kicker">404</p>
    <h1>{esc(NOT_FOUND_EN)}</h1>
    <p class="lede">{esc(NOT_FOUND_FR)}</p>
    <p><a class="home-link" href="/">{esc(HOME_EN)}</a> · <a class="home-link" href="/fr/">{esc(HOME_FR)}</a></p>
  </main>
</body>
</html>
'''


def sitemap() -> str:
    urls = [
        (f"{SITE}/", "1.0"),
        (f"{SITE}/fr/", "0.8"),
    ]
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for loc, pri in urls:
        parts.append("  <url>")
        parts.append(f"    <loc>{loc}</loc>")
        parts.append("    <changefreq>weekly</changefreq>")
        parts.append(f"    <priority>{pri}</priority>")
        parts.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{SITE}/"/>')
        parts.append(f'    <xhtml:link rel="alternate" hreflang="fr" href="{SITE}/fr/"/>')
        parts.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/"/>')
        parts.append("  </url>")
    parts.append("</urlset>")
    return "\n".join(parts) + "\n"


def robots() -> str:
    return (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        f"Sitemap: {SITE}/sitemap.xml\n"
    )


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
    # top accent bar
    draw.rectangle([0, 0, w, 16], fill="#0c6b4d")
    draw.rectangle([0, h - 16, w, h], fill="#0c6b4d")
    serif = font(
        [
            "/usr/share/fonts/truetype/ibm-plex/IBMPlexSerif-SemiBold.ttf",
            "/usr/share/fonts/truetype/ibm-plex/IBMPlexSerif-Bold.ttf",
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
    draw.text((80, 360), "14 browser utilities on web-free.site", font=small, fill="#5f5a52")
    img.save(PUBLIC / "og.png", "PNG", optimize=True)

    # apple touch + ico from a simple mark
    mark = Image.new("RGB", (180, 180), "#0c6b4d")
    mdraw = ImageDraw.Draw(mark)
    wfont = font(
        [
            "/usr/share/fonts/truetype/ibm-plex/IBMPlexSerif-Bold.ttf",
            "/usr/share/fonts/truetype/ibm-plex/IBMPlexSerif-SemiBold.ttf",
        ],
        120,
    )
    # center W
    bbox = mdraw.textbbox((0, 0), "W", font=wfont)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    mdraw.text(((180 - tw) / 2 - bbox[0], (180 - th) / 2 - bbox[1] - 4), "W", font=wfont, fill="#f4efe6")
    mark.save(PUBLIC / "apple-touch-icon.png", "PNG", optimize=True)
    ico = mark.resize((32, 32), Image.Resampling.LANCZOS)
    ico.save(PUBLIC / "favicon.ico", format="ICO", sizes=[(32, 32)])


def main() -> None:
    PUBLIC.mkdir(parents=True, exist_ok=True)
    (PUBLIC / "fr").mkdir(parents=True, exist_ok=True)
    (PUBLIC / "index.html").write_text(page("en"), encoding="utf-8")
    (PUBLIC / "fr/index.html").write_text(page("fr"), encoding="utf-8")
    (PUBLIC / "404.html").write_text(not_found(), encoding="utf-8")
    (PUBLIC / "sitemap.xml").write_text(sitemap(), encoding="utf-8")
    (PUBLIC / "robots.txt").write_text(robots(), encoding="utf-8")
    (PUBLIC / "favicon.svg").write_text(write_favicon_svg(), encoding="utf-8")
    make_og()
    print(f"built {len(ALL_TOOLS)} tools → {PUBLIC}")


if __name__ == "__main__":
    main()

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
SEARCH_LABEL_EN = "Filter tools"
SEARCH_LABEL_FR = "Filtrer les outils"
SEARCH_PLACEHOLDER_EN = "Search tools…"
SEARCH_PLACEHOLDER_FR = "Rechercher un outil…"
NO_RESULTS_EN = "No tools match that search."
NO_RESULTS_FR = "Aucun outil ne correspond à cette recherche."
CATS_NAV_EN = "Categories"
CATS_NAV_FR = "Catégories"
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
    foot = FOOT_FR if is_fr else FOOT_EN
    tools_label = TOOLS_LABEL_FR if is_fr else TOOLS_LABEL_EN
    og_locale = "fr_FR" if is_fr else "en_US"
    nav_other = (
        '<a href="/" lang="en" hreflang="en">English</a>'
        if is_fr
        else '<a href="/fr/" lang="fr" hreflang="fr">Français</a>'
    )
    search_label = SEARCH_LABEL_FR if is_fr else SEARCH_LABEL_EN
    search_ph = SEARCH_PLACEHOLDER_FR if is_fr else SEARCH_PLACEHOLDER_EN
    no_results = NO_RESULTS_FR if is_fr else NO_RESULTS_EN
    cats_nav = CATS_NAV_FR if is_fr else CATS_NAV_EN

    toc_links = []
    sections = []
    for cat in DATA["categories"]:
        cat_name = cat["name_fr"] if is_fr else cat["name_en"]
        toc_links.append(
            f'      <a href="#{esc(cat["id"])}" data-cat="{esc(cat["id"])}">{esc(cat_name)}</a>'
        )
        rows = []
        for tool in cat["tools"]:
            tdesc = tool["desc_fr"] if is_fr else tool["desc_en"]
            hay = f"{tool['name']} {tdesc}"
            rows.append(
                "      <li class=\"tool\" data-search=\"{hay}\">\n"
                "        <a href=\"{url}\">{name}</a>\n"
                "        <span class=\"desc\">{desc}</span>\n"
                "      </li>".format(
                    hay=esc(hay),
                    url=esc(tool["url"]),
                    name=esc(tool["name"]),
                    desc=esc(tdesc),
                )
            )
        sections.append(
            "  <section class=\"category\" id=\"{cid}\" aria-labelledby=\"h-{cid}\">\n"
            "    <h2 id=\"h-{cid}\">{cname}</h2>\n"
            "    <ul class=\"tool-list\">\n"
            "{rows}\n"
            "    </ul>\n"
            "  </section>".format(
                cid=esc(cat["id"]),
                cname=esc(cat_name),
                rows="\n".join(rows),
            )
        )

    html_out = []
    html_out.append("<!DOCTYPE html>")
    html_out.append(f'<html lang="{lang}">')
    html_out.append("<head>")
    html_out.append('  <meta charset="utf-8">')
    html_out.append('  <meta name="viewport" content="width=device-width, initial-scale=1">')
    html_out.append(f"  <title>{esc(title)}</title>")
    html_out.append(f'  <meta name="description" content="{esc(desc)}">')
    html_out.append(f'  <link rel="canonical" href="{esc(canonical)}">')
    html_out.append(f'  <link rel="alternate" hreflang="en" href="{SITE}/">')
    html_out.append(f'  <link rel="alternate" hreflang="fr" href="{SITE}/fr/">')
    html_out.append(f'  <link rel="alternate" hreflang="x-default" href="{SITE}/">')
    html_out.append('  <meta name="robots" content="index,follow">')
    html_out.append('  <meta property="og:type" content="website">')
    html_out.append('  <meta property="og:site_name" content="Web Free">')
    html_out.append(f'  <meta property="og:title" content="{esc(title)}">')
    html_out.append(f'  <meta property="og:description" content="{esc(desc)}">')
    html_out.append(f'  <meta property="og:url" content="{esc(canonical)}">')
    html_out.append(f'  <meta property="og:image" content="{SITE}/og.png">')
    html_out.append('  <meta property="og:image:width" content="1200">')
    html_out.append('  <meta property="og:image:height" content="630">')
    html_out.append(f'  <meta property="og:locale" content="{og_locale}">')
    alt_locale = "en_US" if is_fr else "fr_FR"
    html_out.append(f'  <meta property="og:locale:alternate" content="{alt_locale}">')
    html_out.append('  <meta name="twitter:card" content="summary_large_image">')
    html_out.append(f'  <meta name="twitter:title" content="{esc(title)}">')
    html_out.append(f'  <meta name="twitter:description" content="{esc(desc)}">')
    html_out.append(f'  <meta name="twitter:image" content="{SITE}/og.png">')
    html_out.append('  <link rel="icon" href="/favicon.svg" type="image/svg+xml">')
    html_out.append('  <link rel="icon" href="/favicon.ico" sizes="any">')
    html_out.append('  <link rel="apple-touch-icon" href="/apple-touch-icon.png">')
    html_out.append('  <link rel="stylesheet" href="/styles.css">')
    html_out.append('  <script type="application/ld+json">')
    html_out.append(json_ld(lang))
    html_out.append("  </script>")
    html_out.append('  <script src="https://ref.web-free.site/r.js" defer></script>')
    html_out.append("</head>")
    html_out.append("<body>")
    skip = "Aller au contenu" if is_fr else "Skip to content"
    html_out.append(f'  <a class="skip" href="#main">{skip}</a>')
    html_out.append('  <header class="site-header">')
    html_out.append('    <div class="inner">')
    home = "/fr/" if is_fr else "/"
    html_out.append(f'      <a class="wordmark" href="{home}">Web <span>Free</span></a>')
    lang_label = "Langue" if is_fr else "Language"
    html_out.append(f'      <nav aria-label="{lang_label}">{nav_other}</nav>')
    html_out.append("    </div>")
    html_out.append("  </header>")
    html_out.append('  <main id="main">')
    html_out.append('    <section class="hero">')
    html_out.append(f'      <p class="kicker">{len(ALL_TOOLS)} {esc(tools_label)}</p>')
    html_out.append(f"      <h1>{esc(hero)}</h1>")
    html_out.append(f'      <p class="lede">{esc(intro)}</p>')
    html_out.append("    </section>")
    html_out.append(f'    <nav class="toc" aria-label="{esc(cats_nav)}">')
    html_out.extend(toc_links)
    html_out.append("    </nav>")
    html_out.append('    <form class="filter" role="search" action="#" method="get">')
    html_out.append(f'      <label for="tool-filter">{esc(search_label)}</label>')
    html_out.append(
        f'      <input id="tool-filter" type="search" name="q" placeholder="{esc(search_ph)}" autocomplete="off" enterkeyhint="search">'
    )
    html_out.append("    </form>")
    html_out.append(f'    <p id="no-results" hidden>{esc(no_results)}</p>')
    html_out.extend(sections)
    html_out.append("  </main>")
    html_out.append('  <footer class="site-footer">')
    html_out.append('    <div class="inner">')
    html_out.append(f"      <p>{esc(foot)}</p>")
    html_out.append(
        f'      <p class="fine"><a href="{SITE}/">web-free.site</a> · <a href="/sitemap.xml">Sitemap</a></p>'
    )
    html_out.append('      <p class="twelve-tools-badge">')
    html_out.append(
        '        <a href="https://twelve.tools" target="_blank">'
        '<img src="https://twelve.tools/badge0-light.svg" '
        'alt="Featured&#0032;on&#0032;Twelve&#0032;Tools" width="200" height="54"></a>'
    )
    html_out.append("      </p>")
    html_out.append("    </div>")
    html_out.append("  </footer>")
    html_out.append('  <script src="/filter.js" defer></script>')
    html_out.append(
        "<!-- Cloudflare Web Analytics --><script defer "
        "src='https://static.cloudflareinsights.com/beacon.min.js' "
        "data-cf-beacon='{\"token\": \"3e2f5f96ab32442ebb6e6f650615b58a\"}'>"
        "</script><!-- End Cloudflare Web Analytics -->"
    )
    html_out.append("</body>")
    html_out.append("</html>")
    html_out.append("")
    return "\n".join(html_out)


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
  <script src="https://ref.web-free.site/r.js" defer></script>
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
<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "3e2f5f96ab32442ebb6e6f650615b58a"}}'></script><!-- End Cloudflare Web Analytics -->
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

    # apple touch + ico from a simple mark
    mark = Image.new("RGB", (180, 180), "#0c6b4d")
    mdraw = ImageDraw.Draw(mark)
    wfont = font(
        [
            "/usr/share/fonts/truetype/sand-box/google/IBM Plex Serif/IBMPlexSerif-Bold.ttf",
            "/usr/share/fonts/truetype/sand-box/google/IBM Plex Serif/IBMPlexSerif-SemiBold.ttf",
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

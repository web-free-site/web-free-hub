# Web Free hub

Apex homepage for [web-free.site](https://web-free.site), listing every live free utility on `*.web-free.site`.

French version: [web-free.site/fr/](https://web-free.site/fr/).

## Stack

- Static HTML/CSS in `public/`, generated from `data/tools.json`, `data/category-pages.json`, and `scripts/build.py`
- Hub pages: home (search, categories, FAQ), category and tool detail URLs, About/Contact/Privacy/Terms
- Reusable `public/legal-links.html` snippet for tool subdomains
- Cloudflare Worker with static assets (`wrangler.toml`)
- `www.web-free.site` redirects to the apex with HTTP 301

## Development

```bash
python3 scripts/build.py
npx serve public -p 4173
```

## Deploy

Deploy is done with Wrangler against the Cloudflare account that owns the `web-free.site` zone.

```bash
npm install
npm run deploy
```

## License

MIT. See `LICENSE`.

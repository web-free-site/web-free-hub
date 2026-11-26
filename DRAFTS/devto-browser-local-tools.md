# dev.to draft — Why I ship fifty browser-local micro-tools on one domain

**Tags:** `webdev`, `privacy`, `wasm`, `showdev`

**Title:** Fifty free utilities, one hub, zero installs

**Body:**

Most “free online tool” sites follow the same pattern: upload your file, wait in a queue, download the result. That is fine for cat photos, painful for invoices, and unacceptable for anything regulated.

I run [web-free.site](https://web-free.site/?ref=devto), a hub that links **fifty** single-purpose tools on `*.web-free.site` subdomains—PDF helpers, image compressors, JSON formatters, speech-to-text, video compressors, and everyday calculators. Each tool is its own deploy so I can ship fixes without breaking the rest of the network.

### Design principles

1. **No hub account** — open the tool and work.
2. **Local-first when possible** — WASM and in-browser APIs for PDF, images, and JSON.
3. **Honest privacy notes** — each tool’s hub page states whether data stays on-device.
4. **Attribution, not lock-in** — `?ref=` query params track which listings send traffic, nothing else.

### Examples worth bookmarking

- [PDF converter](https://free-pdf-converter.web-free.site/?ref=devto) — merge/split/compress without a desktop suite
- [Background remover](https://free-background-remover.web-free.site/?ref=devto) — ONNX in the browser
- [JSON formatter](https://free-json-formatter.web-free.site/?ref=devto) — fast config debugging

### How we generate the hub

The apex site is static HTML built from `data/tools.json` and a Python generator—sitemap, JSON-LD, FAQs, and category landings included. Deploy is Cloudflare Workers + assets (maintainers run Wrangler).

If you are building a similar network, invest in **discoverability** (search, categories, internal links) as much as the tools themselves. Traffic compounds when Google can understand what each subdomain does.

Feedback welcome on the [contact page](https://web-free.site/contact/).
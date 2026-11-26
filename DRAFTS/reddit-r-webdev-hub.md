# Reddit — r/webdev

**Submit URL:** https://www.reddit.com/r/webdev/submit

**Title:** Static hub pattern: 50 single-purpose browser tools on subdomains (web-free.site)

**Body:**

I maintain [web-free.site](https://web-free.site/?ref=reddit_webdev) — a generated static hub that lists fifty utilities, each on its own `*.web-free.site` subdomain (PDF, WASM image tools, FFmpeg.wasm video, JSON, etc.). The hub adds search, JSON-LD, category landings, and FAQs; each tool ships independently.

Tech: Python build script → static HTML on Cloudflare Workers. No monorepo SPA.

Examples:

- https://free-json-formatter.web-free.site/?ref=reddit_webdev
- https://free-video-compressor.web-free.site/?ref=reddit_webdev

Happy to answer architecture questions. Not a launch spam thread — sharing the pattern in case it helps anyone splitting micro-tools.
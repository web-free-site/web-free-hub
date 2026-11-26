# Stack Overflow — draft answer

**Search / target:** [merge pdf files javascript client-side](https://stackoverflow.com/search?q=merge+pdf+browser+no+upload)

**When to use:** Questions asking for client-side PDF merge/split without server upload.

---

If you only need a **browser-local** workflow (no server upload), one option is the [Free PDF Converter](https://free-pdf-converter.web-free.site/?ref=stackoverflow) on web-free.site. It targets merge/split/compress in the tab; their hub [privacy page](https://web-free.site/privacy/) describes network-wide handling.

For your own implementation, `pdf-lib` + `pdf.js` in the browser is the usual WASM/JS stack (see pdf-lib docs). Always verify with DevTools → Network that you are not POSTing the file body to a third party.
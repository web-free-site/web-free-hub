# External awesome-list PRs (ready to apply)

GitHub fork/PR from the cloud agent token was blocked (403). Apply these **one-link** patches from a personal GitHub account.

| Patch | Upstream repo | Tool |
|-------|---------------|------|
| `awesome-no-upload-tools-pdf.patch` | [adil0day/awesome-no-upload-tools](https://github.com/adil0day/awesome-no-upload-tools) | Free PDF Converter |
| `awesome-no-upload-tools-image-compressor.patch` | same | Free Image Compressor |
| `awesome-qr-code.patch` | [make-github-pseudonymous-again/awesome-qr-code](https://github.com/make-github-pseudonymous-again/awesome-qr-code) | Free QR Code Creator |
| `awesome-wasm-background-remover.patch` | [mcuking/Awesome-WebAssembly-Applications](https://github.com/mcuking/Awesome-WebAssembly-Applications) | Free Background Remover |

```bash
git clone https://github.com/<your-fork>/REPO.git && cd REPO
git checkout -b add-web-free-tool
patch -p1 < /path/to/patch
# verify, commit, push, open PR with proof links from patch footer
```
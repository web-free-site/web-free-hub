"""Static English copy for generated hub pages."""

LAST_UPDATED = "November 26, 2026"

HOME_INTRO = """Web Free is a directory of fifty free browser tools, each hosted on its own subdomain of web-free.site.
There is no master app to install and no account to create before you start. Pick a category, open the tool you need, and work in a normal browser tab on your phone, tablet, or computer.

The collection spans documents and PDFs, images and QR codes, calculators, audio and video conversion, developer utilities, generators for test data, password tools, and small everyday helpers such as ZIP archives and time zones.
Most utilities are built for privacy-conscious use: many process files or text locally in your browser so drafts, photos, and clips never have to be uploaded to our servers.
Where a tool uses server-side steps or third-party scripts, its hub detail page states that clearly.

This main site is the map of the network. Every tool keeps its own interface and feature set; the hub helps you discover options, compare categories, and read how each utility handles your data.
Use the search box to filter all fifty tools by name or keyword, browse categories below, or open a popular tool directly.
When you follow a link to a live tool, we append ?ref=hub so we can understand traffic from this directory—nothing else changes on the destination site.

All tools are free to use. The hub and individual tools may show advertising and use analytics described in our Privacy Policy and Terms of Use, which apply to the entire web-free.site network."""

HOME_FAQ = [
    (
        "Do I need an account to use Web Free tools?",
        "No. Every tool in the directory is free to open and does not require sign-up through the hub. Individual tools may ask for browser permissions (for example microphone access for recording) but not for a Web Free account.",
    ),
    (
        "Are my files uploaded to your servers?",
        "It depends on the tool. Many utilities process files entirely in your browser and never send your content to us. Others may use network requests for features such as live exchange rates. Each tool's hub page includes a privacy note describing typical behavior—check that page before working with sensitive files.",
    ),
    (
        "Why does each tool have its own subdomain?",
        "Separate subdomains keep tools independent, fast to update, and easy to bookmark. The hub at web-free.site ties them together with search, categories, and documentation while each tool keeps its own URL.",
    ),
    (
        "Does Web Free cost anything?",
        "The tools are free to use. The site is supported by advertising (including third-party ad networks) and may use privacy-focused analytics. There are no paid tiers on the hub itself.",
    ),
    (
        "Which languages are supported?",
        "This hub listing is in English. The directory page is also available in French at /fr/. Individual tools may offer multiple languages within their interface.",
    ),
    (
        "How do I report a problem with a tool?",
        "The Contact page on this hub describes how to reach us. Include the tool name and what happened so we can route feedback appropriately. We do not operate phone support.",
    ),
    (
        "Is web-free.site safe for sensitive documents?",
        "Many tools process PDFs, images, and text locally in your browser, which keeps content on your device for that session. Always read the privacy note on each tool's hub page before you use contracts, IDs, or medical records. Close the tab when you finish on shared computers.",
    ),
    (
        "Can I use Web Free tools on mobile?",
        "Yes. Each tool runs in a modern mobile browser. Heavy jobs such as video compression or background removal may be slower on low-memory phones because work stays on the device.",
    ),
    (
        "How do I find a specific tool quickly?",
        "Use the search box on the homepage to filter all fifty tools by name or keyword, or open a category page such as image, video, or developer tools for grouped listings with FAQs.",
    ),
]

# Short how-to guides surfaced on the homepage (English only).
HOME_GUIDES = [
    (
        "Compress a video for email or messaging",
        "Open the Free Video Compressor from the video category. Choose a target size preset if offered, drop your file, and wait for the browser to finish processing. Download the output and compare file size in your file manager before you send. For audio-only exports, try Free Video to MP3 or the audio converter.",
    ),
    (
        "Remove a photo background without uploading",
        "Use Free Background Remover from the image category. Load a JPG or PNG, let the in-browser model process the image, then download a transparent PNG. Pair with Free Image Compressor if you need a smaller file for the web.",
    ),
    (
        "Format and validate JSON in seconds",
        "Paste minified JSON into Free JSON Formatter, choose pretty-print or minify, and fix syntax errors highlighted in the editor. Nothing is stored on Web Free servers when processing stays client-side. Use Free Diff Checker when you need to compare two config files.",
    ),
    (
        "Create a QR code for a URL or Wi-Fi network",
        "Open Free QR Code Creator, enter your link or connection details, pick colors or style if you want, and download PNG or SVG. Scan with your phone before you print. Styled codes still need enough contrast for reliable scanning.",
    ),
    (
        "Merge or split PDFs in the browser",
        "Start at Free PDF Converter for merge, split, compress, and convert actions without installing Acrobat. Work on one task at a time and keep a backup of the original. If you only need images from a PDF, check the image category for OCR and conversion tools.",
    ),
    (
        "Record your screen for a tutorial",
        "Use Free Screen Recorder from the video category. Allow browser permissions for screen and microphone when prompted. Trim the capture if the tool offers it, then export WebM. Compress with Free Video Compressor if the file is too large for email.",
    ),
    (
        "Build a CV that passes ATS filters",
        "Open Free CV Maker, choose a clean template, fill sections in plain language, and export PDF. Avoid complex tables that parsers misread. Proofread dates and job titles before you send. Pair with Free Word Counter if you need to trim a summary.",
    ),
    (
        "Extract MP3 from a video clip",
        "Free Video to MP3 accepts local MP4, MOV, or WebM files in the browser. Pick a bitrate, run the conversion, and download. For trimming first, use Free MP3 Cutter in the audio category.",
    ),
    (
        "Generate a secure password",
        "Open Free Password Generator, set length and character classes, copy the result, and paste into your password manager—never reuse the same secret across sites.",
    ),
    (
        "Transcribe a meeting or voice memo",
        "Free Speech to Text can take microphone input or an audio file. Pick the language, wait for the transcript, then export TXT or SRT for captions.",
    ),
]

# Per-tool how-to steps (overrides generic steps on hub detail pages).
TOOL_STEPS: dict[str, list[str]] = {
    "free-pdf-converter": [
        "Open Free PDF Converter and allow the page to load fully.",
        "Drag one or more PDFs into the tool or use the file picker.",
        "Pick merge, split, compress, or convert from the available modes.",
        "Download the result and verify the page count or file size before you delete your backup.",
    ],
    "free-json-formatter": [
        "Copy JSON from your editor or API response.",
        "Paste into Free JSON Formatter and choose pretty-print or minify.",
        "Fix any syntax errors the highlighter reports.",
        "Copy the formatted output back to your project or config file.",
    ],
    "free-qr-code-creator": [
        "Enter the URL, text, or Wi-Fi details you want encoded.",
        "Adjust colors or style if needed while keeping strong contrast.",
        "Preview the code and scan it with your phone camera.",
        "Download PNG or SVG for print or web.",
    ],
    "free-background-remover": [
        "Upload a JPG or PNG portrait or product photo.",
        "Wait for the in-browser model to finish segmentation.",
        "Preview the cutout on a checkerboard or solid color.",
        "Download transparent PNG and compress if needed for the web.",
    ],
    "free-video-compressor": [
        "Select a video file within the size limits shown in the tool.",
        "Choose a target preset (messaging, email, or custom bitrate).",
        "Start compression and keep the tab open until export completes.",
        "Compare output size and quality, then download.",
    ],
    "free-image-compressor": [
        "Add one or many images to the batch queue.",
        "Pick output format and quality target.",
        "Run compress and review before/after size.",
        "Download individually or as a ZIP if offered.",
    ],
    "free-speech-to-text": [
        "Choose microphone, file upload, or video source.",
        "Select the spoken language.",
        "Start transcription and wait for the progress bar.",
        "Export TXT or SRT and edit in your editor.",
    ],
    "free-word-counter": [
        "Paste or type your draft into the text area.",
        "Review word, character, and reading-time stats live.",
        "Adjust content to hit your target length.",
        "Copy text out when finished; clear the field on shared PCs.",
    ],
    "free-cv-maker": [
        "Pick a template suited to ATS parsing.",
        "Fill experience, education, and skills in order.",
        "Preview layout and export PDF.",
        "Save a copy locally before you apply online.",
    ],
    "free-invoice-generator": [
        "Enter your business details and client information.",
        "Add line items, tax, and currency (RWF, FCFA, USD, EUR, etc.).",
        "Preview totals and export PDF or print.",
        "Store a copy for your records.",
    ],
    "free-screen-recorder": [
        "Click record and grant screen, mic, or webcam permissions.",
        "Capture the workflow you need to demonstrate.",
        "Stop recording and trim silence or mistakes if available.",
        "Download WebM and compress if you need a smaller share file.",
    ],
    "free-video-to-mp3": [
        "Load a local video file (MP4, MOV, WebM).",
        "Select MP3 bitrate or quality preset.",
        "Run extraction and wait for processing in the tab.",
        "Download the audio file.",
    ],
    "free-heic-to-jpg": [
        "Select HEIC or HEIF photos from your phone or camera.",
        "Start conversion in the browser.",
        "Download JPG files for upload to sites that reject HEIC.",
    ],
    "free-diff-checker": [
        "Paste original text in the left pane and revised text on the right.",
        "Review highlighted additions and deletions.",
        "Merge or copy the cleaned version as needed.",
    ],
    "free-zip-tool": [
        "Drop a ZIP to inspect contents or add files to create a new archive.",
        "Preview filenames before you extract.",
        "Download the new ZIP or extracted files to your device.",
    ],
}

# Optional per-tool FAQ (English). Used on hub detail pages and FAQPage JSON-LD.
TOOL_FAQ: dict[str, list[tuple[str, str]]] = {
    "free-pdf-converter": [
        (
            "Does the PDF converter upload my files?",
            "The tool is built for browser-side PDF work so your documents are not meant to be uploaded to Web Free servers for typical merge, split, and compress tasks. Keep a local backup before you edit important contracts.",
        ),
        (
            "What PDF tasks are supported?",
            "Common jobs include merge, split, compress, convert, and light editing. Open the live tool for the latest format list and limits.",
        ),
    ],
    "free-json-formatter": [
        (
            "Is my JSON sent to a server?",
            "Formatting is designed to run in your browser tab. Do not paste production secrets on a shared computer.",
        ),
        (
            "Can it fix invalid JSON?",
            "The formatter highlights syntax problems so you can correct them before you copy or export.",
        ),
    ],
    "free-qr-code-creator": [
        (
            "Do styled QR codes still scan?",
            "Yes when contrast and quiet zone are preserved. Always test with your phone camera before printing posters or packaging.",
        ),
        (
            "Can I download vector QR codes?",
            "Export options depend on the live tool; PNG and SVG are common when you need print quality.",
        ),
    ],
    "free-background-remover": [
        (
            "What image formats work?",
            "Typical inputs include JPG and PNG. The model runs in your browser; very large images may take longer on older hardware.",
        ),
        (
            "Is the output transparent?",
            "Downloads are usually PNG with transparency so you can place the subject on any background.",
        ),
    ],
    "free-image-compressor": [
        (
            "Can I compress multiple images?",
            "Batch queue and ZIP download are supported according to the tool description. Processing stays local when the browser handles the job.",
        ),
        (
            "Which formats are supported?",
            "JPG, PNG, WebP, and AVIF are listed. Pick the codec that fits your website or email size limit.",
        ),
    ],
    "free-speech-to-text": [
        (
            "What audio sources can I transcribe?",
            "Microphone, uploaded audio, and some video sources work in the browser with Whisper-based models.",
        ),
        (
            "Which export formats are available?",
            "TXT and SRT are common when you need captions or plain text for editing.",
        ),
    ],
    "free-video-compressor": [
        (
            "Why compress in the browser?",
            "Local processing avoids long uploads for large clips. Very big files may stress low-memory devices.",
        ),
        (
            "Will quality stay acceptable?",
            "Choose a preset that matches your destination (messaging, web, email). Preview when the tool offers it.",
        ),
    ],
    "free-password-generator": [
        (
            "Are generated passwords stored online?",
            "Secrets are created in your browser and are not sent to Web Free servers.",
        ),
        (
            "How long should a password be?",
            "Use at least 12–16 random characters for important accounts and store them in a dedicated password manager.",
        ),
    ],
    "free-word-counter": [
        (
            "Does pasted text leave my device?",
            "Word counting runs in the tab; text is not uploaded for typical use.",
        ),
        (
            "What counts toward the total?",
            "Words, characters, sentences, and estimated reading time are shown together for writers and students.",
        ),
    ],
    "free-currency-converter": [
        (
            "Are exchange rates live?",
            "Rates are fetched from the network when you convert. Other calculator tools often work offline in the tab.",
        ),
        (
            "Which currencies are supported?",
            "Major codes including RWF, CFA, USD, and EUR are included for everyday travel and business estimates.",
        ),
    ],
    "free-image-resizer": [
        (
            "Can I resize for social media dimensions?",
            "Set width and height or use presets when available, then export. Processing typically stays on your device.",
        ),
        (
            "Will resizing reduce quality?",
            "Enlarging beyond the original resolution softens detail; compress after resize if file size matters.",
        ),
    ],
    "free-video-to-mp3": [
        (
            "Is video uploaded to convert to MP3?",
            "Extraction is designed to run in the browser with FFmpeg.wasm-style local processing for supported formats.",
        ),
        (
            "Which video formats work?",
            "MP4, MOV, and WebM are listed in the tool description.",
        ),
    ],
    "free-heic-to-jpg": [
        (
            "Why convert HEIC to JPG?",
            "Many websites and older apps only accept JPG; conversion lets you share iPhone photos everywhere.",
        ),
        (
            "Are originals kept on my phone?",
            "Conversion happens in the tab; your camera roll is unchanged unless you replace files yourself.",
        ),
    ],
    "free-image-to-text": [
        (
            "Which languages does OCR support?",
            "English, French, and Swahili are noted in the tool listing.",
        ),
        (
            "Can I OCR a PDF scan?",
            "Supported image and PDF inputs are described on the live tool page.",
        ),
    ],
    "free-screen-recorder": [
        (
            "Is there a watermark?",
            "The tool description states exports without a watermark—confirm in the UI before publishing.",
        ),
        (
            "What format is the recording?",
            "WebM export is standard for browser capture; convert with Free Video Converter if you need MP4.",
        ),
    ],
    "free-cv-maker": [
        (
            "Will employers' ATS read the PDF?",
            "Templates aim for ATS-friendly structure; avoid text in images and verify with your target job portal.",
        ),
        (
            "Can I update the CV later?",
            "Reopen the tool, adjust content, and export a fresh PDF; keep backups on your device.",
        ),
    ],
    "free-diff-checker": [
        (
            "Can I compare files without uploading?",
            "Text and file comparison is designed for client-side use per the tool description.",
        ),
        (
            "Does it show line-by-line diffs?",
            "Side-by-side highlighting is typical; open the tool for merge and export options.",
        ),
    ],
    "free-mp3-cutter": [
        (
            "Which audio formats can I trim?",
            "MP3, WAV, and M4A are listed with a waveform editor in the browser.",
        ),
        (
            "Is the trimmed file uploaded?",
            "Editing is intended to stay local on your device for supported workflows.",
        ),
    ],
    "free-zip-tool": [
        (
            "Are ZIP contents uploaded?",
            "Unpacking and building archives runs in the browser when supported; previews help before extract.",
        ),
        (
            "Can I password-protect ZIP files?",
            "Check the live tool for encryption options; not all browser ZIP libraries support passwords.",
        ),
    ],
    "free-seo-generator": [
        (
            "Do SEO tools improve rankings automatically?",
            "No. The generator outputs meta tags, sitemaps, and JSON-LD you still need to implement well on your site.",
        ),
        (
            "Is generated markup stored?",
            "Markup is produced in your session; copy it into your project or CMS.",
        ),
    ],
    "free-text-to-speech": [
        (
            "Which voices are available?",
            "English and French Piper voices are listed with speed control and WAV download.",
        ),
        (
            "Is text sent to a cloud API?",
            "Synthesis runs in the browser for the described setup; review the live tool for current behavior.",
        ),
    ],
    "free-passport-photo-maker": [
        (
            "Are country sizes official?",
            "The tool lists official size presets and a print sheet; always confirm with your issuing authority.",
        ),
        (
            "Is there a watermark?",
            "The description states no watermark on exports.",
        ),
    ],
    "free-unit-converter": [
        (
            "Does unit conversion work offline?",
            "Math runs in the tab; no account is required for standard conversions.",
        ),
        (
            "How many unit types are covered?",
            "Length, mass, temperature, volume, and more than a dozen categories are included.",
        ),
    ],
    "free-loan-calculator": [
        (
            "Can I export an amortization table?",
            "CSV and PDF export are noted in the description.",
        ),
        (
            "Is this financial advice?",
            "No. Use results as estimates and consult a professional for major borrowing decisions.",
        ),
    ],
    "free-whiteboard": [
        (
            "Can I collaborate live?",
            "The tool focuses on solo sketching in the browser with PNG or SVG export.",
        ),
        (
            "Is my drawing stored in the cloud?",
            "Work typically stays in the session until you download.",
        ),
    ],
}

# Optional short guides on category hub pages (slug → paragraphs).
CATEGORY_GUIDES: dict[str, list[str]] = {
    "image": [
        "Start with Free Image Compressor when file size is the problem and Free Image Resizer when dimensions matter.",
        "For marketplace listings, run Background Remover first, then compress WebP or AVIF for faster page loads.",
        "HEIC from iPhones should go through Free HEIC to JPG before uploading to sites that reject Apple formats.",
    ],
    "video": [
        "Compress with Free Video Compressor before WhatsApp or email attachments; extract audio with Free Video to MP3 if only sound is needed.",
        "Convert exotic containers to MP4 with Free Video Converter before editing elsewhere.",
    ],
    "developer": [
        "Paste API responses into Free JSON Formatter, then diff configs with Free Diff Checker before deploy.",
        "Use Free Speech to Text for interview notes; export SRT when you need captions.",
    ],
    "calculators": [
        "Use Free Currency Converter for live RWF, CFA, and major pairs; use Free Loan Calculator for amortization exports.",
        "Free Percentage Calculator helps with VAT-style math and margin checks.",
    ],
    "text-writing": [
        "Draft in Word Counter, build invoices with Free Invoice Generator, and export signed PDFs via Signature Generator.",
    ],
    "utilities": [
        "Generate passwords locally, unpack ZIPs in-browser, and schedule calls with the time-zone converter.",
    ],
}

CATEGORY_FAQ = {
    "text-writing": [
        (
            "Can I edit PDFs without uploading them?",
            "The Free PDF Converter is built for browser-side PDF work. Check its hub page for the latest behavior and limits before processing confidential documents.",
        ),
        (
            "Are CV exports suitable for ATS systems?",
            "The CV Maker focuses on ATS-friendly structure, but you should still proofread content and verify formatting with your target employer's guidance.",
        ),
        (
            "How do I count words for an essay deadline?",
            "Use Free Word Counter on the hub; paste text and read word count and reading time instantly in the browser.",
        ),
    ],
    "image": [
        (
            "Which image formats are supported?",
            "Most image tools accept common formats such as JPG, PNG, and WebP; some add HEIC, AVIF, or SVG. Open the specific tool page for format details.",
        ),
        (
            "Does background removal run locally?",
            "The background remover uses in-browser models; see its detail page for privacy notes and device requirements.",
        ),
    ],
    "calculators": [
        (
            "Are exchange rates live?",
            "The currency converter fetches current rates from the network. Other calculators generally run offline in the tab.",
        ),
        (
            "Can I use these for medical or financial decisions?",
            "Calculators provide estimates only. Consult qualified professionals for health, legal, or major financial choices.",
        ),
    ],
    "developer": [
        (
            "Do SEO tools guarantee rankings?",
            "No. Generators and checklists help you produce markup and ideas; search results depend on many factors outside any single tool.",
        ),
        (
            "Is JSON data stored after I leave?",
            "The JSON formatter is designed for client-side use. Avoid pasting production secrets you would not want on a shared computer.",
        ),
    ],
    "video": [
        (
            "What video sizes can I compress?",
            "The compressor targets common limits such as messaging attachments; very large files may be slow on low-memory devices because processing stays local.",
        ),
        (
            "Can I record my screen without a watermark?",
            "The screen recorder exports without a watermark according to its description; confirm in the tool before publishing.",
        ),
    ],
    "audio": [
        (
            "Which audio formats can I convert?",
            "The audio converter supports common formats such as MP3, WAV, M4A, OPUS, OGG, and AAC.",
        ),
    ],
    "utilities": [
        (
            "Are generated passwords stored online?",
            "The password generator creates secrets in your browser; they are not sent to Web Free servers.",
        ),
    ],
    "generators": [
        (
            "Can I use fake data for real registrations?",
            "No. Fake names and addresses are for testing and demos only—not for bypassing identity checks or violating site terms.",
        ),
        (
            "Can I export test data as CSV?",
            "Fake name and address generators typically support CSV or JSON export for QA fixtures.",
        ),
    ],
    "design": [
        (
            "What can I export from the whiteboard?",
            "You can typically export PNG or SVG from the whiteboard tool; open it for the current export options.",
        ),
    ],
}

ABOUT_BODY = """Web Free is an independent directory of free, browser-based utilities published under the web-free.site domain.
Each tool lives on its own subdomain so you can bookmark exactly what you need—PDF helpers, image editors, calculators, and the rest—without installing an app store package or creating a hub account.

We built the hub to solve a simple problem: fifty useful sites are hard to remember. The main site adds search, categories, short guides, and links to live tools with clear privacy notes.
We do not claim ratings, download counts, or awards; the directory lists live tools we operate on this domain.

The hub is available in English here and in French at /fr/ for the tool listing.
Legal terms and privacy practices for the whole network—including every subdomain—are on the Terms and Privacy pages linked in the footer."""

CONTACT_BODY = """We do not operate a support call center or live chat on the hub.

If you have a question about how a specific tool works, a broken link, or feedback about the web-free.site network, mention the tool name and your browser when you write to us.
You can reach the project maintainers through the contact channel published on the live web-free.site deployment (this static hub does not embed a mail form to reduce spam).

For privacy-related requests, refer to the Privacy Policy. For rules governing use of the tools, see the Terms of Use.
We aim to read reasonable reports but cannot guarantee individual responses to every message."""

def privacy_html(site: str) -> str:
    return f"""<p><strong>Last updated:</strong> {LAST_UPDATED}</p>
<p>This Privacy Policy describes how the <strong>web-free.site</strong> network handles information when you use the hub at <a href="{site}/">web-free.site</a> and any associated tool site on a <code>*.web-free.site</code> subdomain (collectively, the \"Site\" or \"network\"). It applies to all tools listed in the hub directory unless a specific tool page states otherwise for a narrow feature.</p>

<h2>What we collect</h2>
<p>Most Web Free tools are designed to work <strong>without user accounts</strong>. We do not sell personal data. We do not offer a signup form on the hub that stores profiles in our database.</p>
<p>Depending on the tool and your browser, processing may happen entirely on your device (for example compressing an image or formatting JSON). When work stays in the browser, file contents often never reach our servers. Tools that need live data (such as currency rates) may fetch public information over the network without storing your inputs long term.</p>
<p>We may still receive limited technical information because the network is hosted online.</p>

<h2>Advertising (Adsterra)</h2>
<p>Some pages in the network display advertisements served through <strong>Adsterra</strong> or similar ad partners. Those companies may use cookies, device identifiers, and similar technologies to serve ads, measure performance, and limit repeat impressions. Their use of data is governed by their own policies. You can manage cookies in your browser settings and through consent tools where offered by the ad provider.</p>

<h2>Hosting, security, and analytics</h2>
<p>The Site is delivered through <strong>Cloudflare</strong> and related infrastructure. Cloudflare may process IP addresses, request timestamps, URLs, and security signals in server and firewall logs to provide caching, DDoS protection, and delivery. We also use <strong>Cloudflare Web Analytics</strong> (or comparable lightweight analytics) on some pages to understand aggregate traffic without relying on invasive third-party trackers for core measurements. Log data is retained for a limited period consistent with hosting practices.</p>
<p>We use a small reference script (<code>ref.web-free.site</code>) on some pages to understand when visitors arrive from the hub; this is part of operating the directory.</p>
<p>We also use <strong>Google Analytics 4</strong> on the hub and on tool subdomains (*.web-free.site) to measure aggregate traffic and usage. Google may set cookies such as <code>_ga</code> and <code>_ga_*</code>, and similar identifiers, to distinguish visitors and sessions. Because the tools share the parent domain, those cookies can work across subdomains. Google processes this data under its own terms. You can opt out with the <a href="https://tools.google.com/dlpage/gaoptout">Google Analytics opt-out browser add-on</a> or by blocking cookies in your browser settings.</p>

<h2>Children</h2>
<p>The network is intended for a general audience. We do not knowingly collect personal information from children under 13. If you believe a child has provided personal information through the network, contact us using the details on the <a href="/contact/">Contact</a> page and we will take reasonable steps to delete it.</p>

<h2>Your choices</h2>
<ul>
  <li>Use browser privacy modes and block third-party cookies if you prefer fewer ad-related identifiers.</li>
  <li>Close tools after use on shared devices so local files or clipboard data are not left behind.</li>
  <li>Read each tool's hub description for whether it keeps processing on your device.</li>
</ul>

<h2>Changes</h2>
<p>We may update this policy to reflect new tools, hosting, or legal requirements. The \"Last updated\" date at the top will change when we do. Continued use of the network after an update means you accept the revised policy.</p>

<h2>Contact</h2>
<p>Questions about privacy should be directed as described on our <a href="/contact/">Contact</a> page. This policy is published on the hub so every tool subdomain can link here for a single network-wide statement.</p>"""


def terms_html() -> str:
    return f"""<p><strong>Last updated:</strong> {LAST_UPDATED}</p>
<p>These Terms of Use (\"Terms\") govern your access to the <strong>web-free.site</strong> hub and every free tool served on a <code>*.web-free.site</code> subdomain (together, the \"network\"). By using any part of the network, you agree to these Terms. If you do not agree, do not use the services.</p>

<h2>The service</h2>
<p>Web Free provides browser-based utilities and a directory that links to them. Tools are offered <strong>free of charge</strong>, <strong>as-is</strong>, and <strong>as available</strong>. We may add, change, or remove tools without notice.</p>

<h2>No warranty</h2>
<p>We do not warrant that any tool will be error-free, uninterrupted, secure, or fit for a particular purpose. Results (converted files, calculations, generated text, etc.) may be inaccurate or incomplete. You are responsible for verifying outputs before relying on them for business, legal, medical, financial, or safety decisions.</p>

<h2>Acceptable use</h2>
<p>You agree not to misuse the network. Prohibited conduct includes, without limitation:</p>
<ul>
  <li>Violating applicable law or third-party rights.</li>
  <li>Uploading or processing unlawful, infringing, harassing, or malicious content.</li>
  <li>Attempting to break, scrape, or overload our systems or bypass reasonable rate limits.</li>
  <li>Using generators or fake data tools to defraud, impersonate real people, or evade security controls.</li>
  <li>Interfering with ads, analytics, or security features where they are part of a page.</li>
</ul>
<p>We may restrict access if we believe use threatens the network or others.</p>

<h2>Your content and copyright</h2>
<p>You retain responsibility for files, text, recordings, and other material you submit to a tool. You must have the rights needed to process that material (including copyright and privacy rights). We do not claim ownership of your inputs or outputs. You grant only the technical permissions required for your browser to run the tool locally or for minimal network operations the tool requires.</p>

<h2>Third-party ads and links</h2>
<p>Pages may display advertisements from third parties such as <strong>Adsterra</strong> and may link to external sites. We do not control third-party content and are not responsible for their terms, privacy practices, or products. Your dealings with advertisers are solely between you and them.</p>

<h2>Limitation of liability</h2>
<p>To the fullest extent permitted by law, the network and its operators will not be liable for indirect, incidental, special, consequential, or punitive damages, or for loss of data, profits, or goodwill, arising from your use of the tools. Our total liability for any claim related to the network shall not exceed the greater of (a) the amount you paid us for the use giving rise to the claim (typically zero) or (b) one hundred U.S. dollars.</p>
<p>Some jurisdictions do not allow certain limitations; in those cases our liability is limited to the maximum permitted by law.</p>

<h2>Privacy</h2>
<p>Our <a href="/privacy/">Privacy Policy</a> explains how data is handled across the network and is incorporated into these Terms by reference.</p>

<h2>Changes</h2>
<p>We may modify these Terms at any time. The updated date will appear at the top of this page. Your continued use after changes constitutes acceptance.</p>

<h2>General</h2>
<p>These Terms are a straightforward agreement for operating a free public tool network; they are not legal advice. If a provision is unenforceable, the remainder stays in effect. No waiver of a term is a continuing waiver.</p>

<h2>Contact</h2>
<p>See the <a href="/contact/">Contact</a> page on the hub for how to reach us about these Terms.</p>"""
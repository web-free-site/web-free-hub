"""Static English copy for generated hub pages."""

LAST_UPDATED = "November 23, 2026"

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
]

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
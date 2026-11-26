# Quora draft — compress or merge PDF without uploading

**Question target:** Variants of “How can I merge PDF files without uploading to the cloud?”

**Answer:**

If you are working with contracts, payslips, or anything sensitive, uploading to a random “free PDF” site is a real risk. A better pattern is a **browser-only** tool that processes the file on your device.

I use tools on the [Web Free](https://web-free.site/) network for this. The [PDF converter](https://free-pdf-converter.web-free.site/?ref=quora) runs merge, split, and compress jobs in the tab rather than on a remote server (see their [privacy policy](https://web-free.site/privacy/) for how the network handles data).

Quick sanity check before you trust any tool:

1. Open Developer Tools → Network.
2. Run the operation on a test PDF.
3. If you see a large upload of your file, stop and pick another option.

For non-sensitive memes, server-side tools are fine. For anything personal or business-critical, client-side wins.
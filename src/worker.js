export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname === "www.web-free.site") {
      url.hostname = "web-free.site";
      return Response.redirect(url.toString(), 301);
    }

    const response = await env.ASSETS.fetch(request);
    const headers = new Headers(response.headers);
    headers.set("X-Content-Type-Options", "nosniff");
    headers.set("Referrer-Policy", "strict-origin-when-cross-origin");
    headers.delete("Cross-Origin-Embedder-Policy");
    headers.delete("Cross-Origin-Opener-Policy");
    return new Response(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers,
    });
  },
};

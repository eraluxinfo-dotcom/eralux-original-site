export async function onRequestPost(context) {
  try {
    const request = context.request;
    const env = context.env;

    const contentType = request.headers.get("content-type") || "";
    let data = {};

    if (contentType.includes("application/json")) {
      data = await request.json();
    } else if (contentType.includes("form")) {
      const form = await request.formData();
      data = Object.fromEntries(form.entries());
    } else {
      return json({ ok: false, error: "Unsupported content type" }, 415);
    }

    const name = clean(data.name || data.username || data.user_name || "");
    const phone = clean(data.phone || data.tel || data.phone_number || "");
    const message = clean(data.message || data.comment || data.text || "");
    const page = clean(data.page || data.url || request.headers.get("referer") || "");
    const lang = clean(data.lang || "");
    const source = clean(data.source || "ERALUX website form");

    const trap = clean(data.website || data.company || "");
    if (trap) {
      return json({ ok: true, skipped: true });
    }

    if (!phone && !message) {
      return json({ ok: false, error: "Phone or message is required" }, 400);
    }

    const token = env.TELEGRAM_BOT_TOKEN;
    const chatId = env.TELEGRAM_CHAT_ID;

    if (!token || !chatId) {
      return json({ ok: false, error: "Telegram bot is not configured" }, 500);
    }

    const ip =
      request.headers.get("CF-Connecting-IP") ||
      request.headers.get("x-forwarded-for") ||
      "unknown";

    const text = [
      "New ERALUX lead",
      "",
      `Source: ${source}`,
      name ? `Name: ${name}` : null,
      phone ? `Phone: ${phone}` : null,
      message ? `Message: ${message}` : null,
      lang ? `Language: ${lang}` : null,
      page ? `Page: ${page}` : null,
      "",
      `IP: ${ip}`,
      `Time: ${new Date().toLocaleString("uk-UA", { timeZone: "Europe/Kyiv" })}`
    ].filter(Boolean).join("\n");

    const tgResponse = await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
      method: "POST",
      headers: {
        "content-type": "application/json"
      },
      body: JSON.stringify({
        chat_id: chatId,
        text,
        disable_web_page_preview: true
      })
    });

    const tgResult = await tgResponse.json();

    if (!tgResponse.ok || !tgResult.ok) {
      return json({ ok: false, error: "Telegram send failed", details: tgResult }, 502);
    }

    return json({ ok: true, message: "Lead sent" });
  } catch (error) {
    return json({ ok: false, error: error.message || "Server error" }, 500);
  }
}

export async function onRequestGet() {
  return json({ ok: true, endpoint: "/api/lead", method: "POST" });
}

function clean(value) {
  return String(value || "")
    .replace(/[<>]/g, "")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, 1200);
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store"
    }
  });
}

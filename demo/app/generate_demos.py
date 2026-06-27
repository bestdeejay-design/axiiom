#!/usr/bin/env python3
"""BROKEN: This file is incomplete — the TEMPLATE variable was never defined in the original source.
All 14 demo pages exist as static HTML and have been updated manually. This generator needs
the TEMPLATE HTML structure restored before it can regenerate demo pages."""

import os
import re

# ── Shared configuration ────────────────────────────────────────────────
CONFIG = {
    "company": {
        "name": "MOBIAP",
        "domain": "mobiap.com",
        "siteUrl": "https://mobiap.com/",
        "ogImage": "https://mobiap.com/og-image.png",
        "copyrightStart": 2024,
    },
    "contact": {
        "email": "hello@mobiap.com",
        "phone": "+1 (XXX) XXX-XXXX",
        "phoneLink": "+1XXXXXXXXXX",
        "telegram": "https://t.me/mobiap",
    },
    "analytics": {
        "googleAnalytics": "G-HFS4BDGTV4",
    },
}
# ─────────────────────────────────────────────────────────────────────────

# NOTE: This is a template showing one demo entry. To regenerate all 14
# demos, add the full DEMOS list from the original generator.
# After adding entries, run: python3 generate_demos.py
# This will recreate all demo/index.html files from the TEMPLATE below.

DEMOS = [
    {
        "slug": "payment-gateway",
        "title": "Payment Gateway",
        "desc": "Universal payment gateway with multi-acquiring, split payments, and escrow. PCI DSS compliant.",
        "meta_desc": "Demo payment gateway: card payments, tokenization, split payments, escrow. PCI DSS compliant. Integration code examples.",
        "code": """// Initialize payment gateway
const gateway = new PaymentGateway({
  apiKey: 'your_api_key',
  merchantId: 'merchant_123',
  environment: 'sandbox' // sandbox | production
});

// Create payment
const payment = await gateway.createPayment({
  amount: 1500.00,
  currency: 'USD',
  description: 'Order #4281',
  split: [
    { merchant: 'submerchant_1', amount: 1200.00 },
    { merchant: 'submerchant_2', amount: 300.00 }
  ],
  escrow: { holdPeriod: 3 } // days
});

// Redirect to payment page
window.location.href = payment.paymentUrl;""",
        "features": ["Multi-acquiring (Visa, MC, Amex)", "Split payments & escrow", "Card tokenization (PCI DSS)", "Holds & refunds", "Webhook notifications", "Merchant dashboard"],
        "tags": ["PHP", "Go", "Node.js", "PostgreSQL", "PCI DSS"],
        "gradient": "#6c5ce7,#a29bfe",
        "widget_html": """<div class="pg-card">
  <div class="pg-header">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--clr-accent)" stroke-width="1.8"><rect x="1" y="4" width="22" height="16" rx="2"/><line x1="1" y1="10" x2="23" y2="10"/><line x1="7" y1="15" x2="11" y2="15"/></svg>
    <span>Card Payment</span>
  </div>
  <div class="pg-body">
    <div class="pg-fld">
      <label class="pg-lbl">Card Number</label>
      <div class="pg-inp-wrap">
        <input class="pg-inp" id="w1n" placeholder="0000 0000 0000 0000" maxlength="19">
        <svg class="pg-card-icon" width="22" height="16" viewBox="0 0 24 16" fill="none">
          <rect x="1" y="1" width="22" height="14" rx="2" stroke="var(--clr-faint)" stroke-width="1.2" fill="none"/>
          <line x1="1" y1="6" x2="23" y2="6" stroke="var(--clr-faint)" stroke-width="1.2"/>
          <circle cx="9" cy="10" r="2.5" stroke="var(--clr-accent)" stroke-width="1.2" fill="none" opacity=".5"/>
          <circle cx="15" cy="10" r="2.5" stroke="var(--clr-accent)" stroke-width="1.2" fill="none" opacity=".5"/>
        </svg>
      </div>
    </div>
    <div class="pg-row">
      <div class="pg-fld">
        <label class="pg-lbl">Expiry</label>
        <input class="pg-inp" id="w1e" placeholder="MM / YY" maxlength="7">
      </div>
      <div class="pg-fld">
        <label class="pg-lbl">CVV</label>
        <div class="pg-inp-wrap">
          <input class="pg-inp" id="w1c" placeholder="***" maxlength="4" type="password">
          <svg class="pg-cvv-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--clr-faint)" stroke-width="1.5"><rect x="3" y="7" width="18" height="12" rx="1.5"/><line x1="7" y1="11" x2="9" y2="11"/><line x1="7" y1="14" x2="11" y2="14"/></svg>
        </div>
      </div>
      <div class="pg-fld">
        <label class="pg-lbl">Amount</label>
        <div class="pg-inp-wrap">
          <span class="pg-currency">$</span>
          <input class="pg-inp pg-inp-amt" id="w1a" type="number" value="1500">
        </div>
      </div>
    </div>
    <button class="pg-btn" id="w1b">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/><circle cx="12" cy="16" r="1"/></svg>
      Pay $1,500
    </button>
    <div class="pg-secure">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--clr-faint)" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Secured by PCI DSS
    </div>
    <div class="pg-result" id="w1x">
      <div class="pg-spinner" id="w1sp"></div>
      <div class="pg-success" id="w1ok">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#00b894" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="16 8 10 16 7 12"/></svg>
        <span class="pg-success-t">Payment Successful</span>
        <span class="pg-success-sub">Thank you! Your payment has been processed.</span>
      </div>
    </div>
  </div>
</div>
<style>
.pg-card{margin:12px 0;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:20px;overflow:hidden}
.pg-header{display:flex;align-items:center;gap:10px;padding:18px 24px 0;font-size:15px;font-weight:600;color:var(--clr-heading)}
.pg-body{display:flex;flex-direction:column;gap:18px;padding:20px 24px 24px}
.pg-fld{display:flex;flex-direction:column;gap:5px}
.pg-lbl{font-size:12px;color:var(--clr-faint);font-weight:500;letter-spacing:.3px;text-transform:uppercase}
.pg-inp-wrap{position:relative;display:flex;align-items:center}
.pg-inp{width:100%;padding:12px 14px;background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:12px;color:var(--clr-text);font-size:15px;font-family:'SF Mono','Fira Code',monospace;box-sizing:border-box;transition:border-color .25s,box-shadow .25s;letter-spacing:.5px}
.pg-inp:focus{outline:none;border-color:var(--clr-accent);box-shadow:0 0 0 3px color-mix(in srgb,var(--clr-accent) 18%,transparent)}
.pg-inp::placeholder{color:var(--clr-faint);opacity:.5;letter-spacing:0}
.pg-card-icon{position:absolute;right:12px;pointer-events:none;opacity:.6}
.pg-cvv-icon{position:absolute;right:12px;pointer-events:none;opacity:.5}
.pg-currency{position:absolute;left:14px;color:var(--clr-faint);font-size:14px;font-weight:500;pointer-events:none}
.pg-inp-amt{padding-left:28px}
.pg-row{display:grid;grid-template-columns:1fr 80px 1fr;gap:12px}
.pg-btn{display:flex;align-items:center;justify-content:center;gap:10px;padding:14px;background:var(--clr-accent);border:none;border-radius:14px;color:#fff;font-size:16px;font-weight:600;cursor:pointer;transition:opacity .25s,transform .15s;font-family:inherit}
.pg-btn:hover{opacity:.9;transform:translateY(-1px)}
.pg-btn:active{transform:translateY(0)}
.pg-secure{display:flex;align-items:center;justify-content:center;gap:6px;font-size:11px;color:var(--clr-faint);opacity:.6}
.pg-result{text-align:center;padding:8px 0 0}
.pg-spinner{display:none;width:32px;height:32px;border:2px solid var(--clr-border);border-top-color:var(--clr-accent);border-radius:50%;animation:pgs .7s linear infinite;margin:0 auto}
.pg-success{display:none;flex-direction:column;align-items:center;gap:4px;padding:8px 0}
.pg-success-t{color:#00b894;font-weight:600;font-size:15px}
.pg-success-sub{color:var(--clr-faint);font-size:12px;opacity:.6}
@keyframes pgs{to{transform:rotate(360deg)}}
@media (min-width:768px){.pg-card{max-width:460px;margin-left:auto;margin-right:auto}}
@media (max-width:500px){.pg-row{grid-template-columns:1fr 1fr}.pg-row .pg-fld:last-child{grid-column:1/-1}}
</style>
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{GA_ID}');</script>
</body>
</html>"""
    },
]

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 6:
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    elif len(hex_color) == 3:
        r, g, b = int(hex_color[0]*2, 16), int(hex_color[1]*2, 16), int(hex_color[2]*2, 16)
    else:
        return 100, 80, 220
    return r, g, b


def make_tags(tags):
    return "\n".join(f'        <span class="tag-item">{t}</span>' for t in tags)


def make_features(features, color):
    rows = []
    for f in features:
        rows.append(f"""      <div class="feature-item">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#{color}" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
        <span>{f}</span>
      </div>""")
    return "\n".join(rows)


def main():
    base = os.path.dirname(os.path.abspath(__file__))

    for demo in DEMOS:
        slug = demo["slug"]
        color = demo["gradient"].split(",")[0].strip("#")
        r, g, b = hex_to_rgb(demo["gradient"].split(",")[0].strip())

        html = TEMPLATE.format(
            SLUG=slug,
            TITLE=demo["title"],
            DESC=demo["desc"],
            META_DESC=demo["meta_desc"],
            CODE=demo["code"],
            TAGS=make_tags(demo["tags"]),
            FEATURES=make_features(demo["features"], color),
            DEMO_WIDGET=demo.get("widget_html", ""),
            COLOR=color,
            R=r, G=g, B=b,
            CONTACT_EMAIL=CONFIG["contact"]["email"],
            CONTACT_PHONE=CONFIG["contact"]["phone"],
            CONTACT_PHONE_LINK=CONFIG["contact"]["phoneLink"],
            GA_ID=CONFIG["analytics"]["googleAnalytics"],
        )

        dir_path = os.path.join(base, slug)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, "index.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✓ {slug}/index.html")

    print(f"\nTotal pages generated: {len(DEMOS)}")


if __name__ == "__main__":
    main()

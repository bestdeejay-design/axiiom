#!/usr/bin/env python3
"""Generate 14 fintech demo pages with code examples and SEO metadata."""

import os
import re

# ── Shared configuration ────────────────────────────────────────────────
CONFIG = {
    "company": {
        "name": "AXIIOM",
        "nameRu": "ООО Аксиома",
        "shortName": "Аксиома",
        "domain": "axiiom.ru",
        "siteUrl": "https://axiiom.ru/",
        "ogImage": "https://axiiom.ru/og-image.png",
        "copyrightStart": 2024,
    },
    "contact": {
        "email": "hello@axiiom.ru",
        "phone": "+7 (812) 928-74-78",
        "phoneLink": "+78129287478",
        "telegram": "https://t.me/axiiom",
    },
    "analytics": {
        "yandexMetrika": "109391253",
        "googleAnalytics": "G-HFS4BDGTV4",
    },
}
# ─────────────────────────────────────────────────────────────────────────

DEMOS = [
    {
        "slug": "payment-gateway",
        "title": "Платёжный шлюз",
        "desc": "Универсальный платёжный шлюз с поддержкой мультиэквайринга, сплитования платежей и escrow-счетов. Соответствие 161-ФЗ и PCI DSS.",
        "meta_desc": "Демо платёжного шлюза: приём платежей по картам, SBP, токенизация, сплитование. Соответствие 161-ФЗ и PCI DSS. Примеры кода интеграции.",
        "code": """// Инициализация платёжного шлюза
const gateway = new PaymentGateway({
  apiKey: 'your_api_key',
  merchantId: 'merchant_123',
  environment: 'sandbox' // sandbox | production
});

// Создание платежа
const payment = await gateway.createPayment({
  amount: 1500.00,
  currency: 'RUB',
  description: 'Заказ №4281',
  split: [
    { merchant: 'submerchant_1', amount: 1200.00 },
    { merchant: 'submerchant_2', amount: 300.00 }
  ],
  escrow: { holdPeriod: 3 } // дней
});

// Перенаправление на платёжную страницу
window.location.href = payment.paymentUrl;""",
        "features": ["Мультиэквайринг (Visa, MC, Мир, SBP)", "Сплитование платежей и escrow", "Токенизация карт (PCI DSS)", "Холдирование и возвраты", "Webhook-уведомления", "Личный кабинет мерчанта"],
        "tags": ["PHP", "Go", "Node.js", "PostgreSQL", "PCI DSS"],
        "gradient": "#6c5ce7,#a29bfe",
        "widget_html": """<div class="pg-card">
  <div class="pg-header">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--clr-accent)" stroke-width="1.8"><rect x="1" y="4" width="22" height="16" rx="2"/><line x1="1" y1="10" x2="23" y2="10"/><line x1="7" y1="15" x2="11" y2="15"/></svg>
    <span>Оплата картой</span>
  </div>
  <div class="pg-body">
    <div class="pg-fld">
      <label class="pg-lbl">Номер карты</label>
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
        <label class="pg-lbl">Срок действия</label>
        <input class="pg-inp" id="w1e" placeholder="MM / YY" maxlength="7">
      </div>
      <div class="pg-fld">
        <label class="pg-lbl">CVV</label>
        <div class="pg-inp-wrap">
          <input class="pg-inp" id="w1c" placeholder="•••" maxlength="4" type="password">
          <svg class="pg-cvv-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--clr-faint)" stroke-width="1.5"><rect x="3" y="7" width="18" height="12" rx="1.5"/><line x1="7" y1="11" x2="9" y2="11"/><line x1="7" y1="14" x2="11" y2="14"/></svg>
        </div>
      </div>
      <div class="pg-fld">
        <label class="pg-lbl">Сумма</label>
        <div class="pg-inp-wrap">
          <span class="pg-currency">₽</span>
          <input class="pg-inp pg-inp-amt" id="w1a" type="number" value="1500">
        </div>
      </div>
    </div>
    <button class="pg-btn" id="w1b">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/><circle cx="12" cy="16" r="1"/></svg>
      Оплатить 1 500 ₽
    </button>
    <div class="pg-secure">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--clr-faint)" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Защищено PCI DSS
    </div>
    <div class="pg-result" id="w1x">
      <div class="pg-spinner" id="w1sp"></div>
      <div class="pg-success" id="w1ok">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#00b894" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="16 8 10 16 7 12"/></svg>
        <span class="pg-success-t">Платёж выполнен</span>
        <span class="pg-success-sub">Спасибо! Ваш платёж прошёл успешно.</span>
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
<script>(function(){
function fm(id,fn){var el=document.getElementById('w1'+id);if(el)el.addEventListener('input',fn)}
fm('n',function(e){e.target.value=e.target.value.replace(/\D/g,'').replace(/(.{4})/g,'$1 ').trim()});
fm('e',function(e){var v=e.target.value.replace(/[^\d\/]/g,'');if(v.length===2&&!v.includes('/'))v=v+' / ';e.target.value=v});
fm('c',function(e){e.target.value=e.target.value.replace(/\D/g,'')});
document.getElementById('w1b').addEventListener('click',function(){var b=this,x=document.getElementById('w1x'),sp=document.getElementById('w1sp'),ok=document.getElementById('w1ok');b.style.display='none';x.style.display='block';sp.style.display='block';ok.style.display='none';setTimeout(function(){sp.style.display='none';ok.style.display='flex'},1800)});
})();</script>""",
        "widget_css": "",
        "widget_js": ""
    },
    {
        "slug": "loyalty-program",
        "title": "Программа лояльности",
        "desc": "White-label платформа лояльности LOVII: баллы, уровни, кэшбэк, промокоды и геймификация. Готовая экосистема для любого бизнеса.",
        "meta_desc": "Демо white-label платформы лояльности: балльная система, уровни, кэшбэк, промокоды, push-уведомления. Интеграция с iiko и r_keeper.",
        "code": """// Начисление баллов
await loyalty.accruePoints({
  userId: 'user_456',
  amount: 350,
  source: 'purchase',
  orderId: 'ORD-2024-8912'
});

// Проверка уровня пользователя
const level = await loyalty.getUserLevel('user_456');
// { level: 'gold', multiplier: 1.5, benefits: [...] }

// Активация промокода
const promo = await loyalty.applyPromo({
  code: 'WELCOME25',
  userId: 'user_456'
});""",
        "features": ["Балльно-бонусная система с уровнями", "Промокоды и персональные офферы", "Push и Email-уведомления", "Интеграция с iiko, r_keeper, 1С", "Аналитика LTV и когорт", "White Label под ваш бренд"],
        "tags": ["React", "Node.js", "PostgreSQL", "Redis", "Kafka"],
        "gradient": "#fd79a8,#e84393",
        "widget_html": """<div class="dw">
  <h3 class="dw-t">🏆 Программа лояльности</h3>
  <div class="dw-b" style="text-align:center">
    <div style="font-size:13px;color:var(--clr-muted);margin-bottom:4px">Ваш баланс</div>
    <div id="loy-bal" style="font-size:42px;font-weight:700;color:var(--clr-heading);font-variant-numeric:tabular-nums;transition:all .3s">2 450</div>
    <div style="font-size:13px;color:var(--clr-muted);margin-bottom:12px">баллов</div>
    <div id="loy-lvl" style="display:inline-block;padding:4px 14px;border-radius:20px;font-size:13px;font-weight:600;margin-bottom:12px;background:linear-gradient(135deg,#f6d365,#fda085);color:#1a1a2e">Silver</div>
    <div style="margin:12px 0 16px">
      <div style="display:flex;justify-content:space-between;font-size:12px;color:var(--clr-muted);margin-bottom:4px"><span>Silver</span><span>Gold</span></div>
      <div style="height:6px;background:var(--clr-bg);border-radius:3px;overflow:hidden"><div id="loy-bar" style="height:100%;width:45%;background:linear-gradient(90deg,var(--clr-accent),#f6d365);border-radius:3px;transition:width .5s ease"></div></div>
    </div>
    <button class="dw-btn" id="loy-btn">Начислить 100 баллов</button>
  </div>
</div>
<style>.dw{margin:12px 0;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:16px;padding:24px}.dw-t{font-size:16px;font-weight:600;margin:0 0 16px;color:var(--clr-heading)}.dw-b{display:flex;flex-direction:column;gap:2px}.dw-btn{padding:12px 20px;background:var(--clr-accent);border:none;border-radius:10px;color:#fff;font-size:14px;font-weight:600;cursor:pointer;transition:opacity .2s;display:inline-block;margin:0 auto}.dw-btn:hover{opacity:.85}@media(min-width:768px){.dw{max-width:480px;margin-left:auto;margin-right:auto}}</style>
<script>(function(){var bal=2450,lvlEl=document.getElementById('loy-lvl'),bar=document.getElementById('loy-bar'),balEl=document.getElementById('loy-bal'),lvls=[{n:'Silver',m:0},{n:'Gold',m:1000},{n:'Platinum',m:3000}];document.getElementById('loy-btn').addEventListener('click',function(){var t=this;t.disabled=1;var st=setInterval(function(){bal++;balEl.textContent=bal.toLocaleString('ru');var p=bal%1000/10;bar.style.width=p+'%';var cl=lvls.filter(function(l){return bal>=l.m});var cu=cl[cl.length-1];if(cu){lvlEl.textContent=cu.n;lvlEl.style.background=cu.n==='Platinum'?'linear-gradient(135deg,#a18cd1,#fbc2eb)':cu.n==='Gold'?'linear-gradient(135deg,#f6d365,#fda085)':'linear-gradient(135deg,#a8edea,#fed6e3)'}if(bal>=2550||bal%100===0&&bal>=2550||bal===2550){clearInterval(st);t.disabled=0}},30);});})();</script>""",
        "widget_css": "",
        "widget_js": ""
    },
    {
        "slug": "credit-conveyor",
        "title": "Кредитный конвейер",
        "desc": "Автоматизированный кредитный конвейер: скоринг, принятие решений, выдача. Интеграция с БКИ и банковскими системами.",
        "meta_desc": "Демо кредитного конвейера: скоринг-модели, ML-принятие решений, интеграция с БКИ. От заявки до выдачи за 5 минут.",
        "code": """// Создание заявки на кредит
const application = await credit.createApplication({
  client: {
    firstName: 'Иван',
    lastName: 'Петров',
    passport: '4010 123456',
    income: 120000
  },
  product: 'consumer_loan',
  amount: 500000,
  term: 12
});

// Запуск скоринга
const decision = await credit.score(application.id);
// { status: 'approved', rate: 15.9, limit: 500000 }

// Выдача
await credit.issue(application.id);""",
        "features": ["Скоринг-модели (ML + правила)", "Интеграция с 4+ БКИ", "Андеррайтинг в реальном времени", "Конвейерная обработка заявок", "Личный кабинет заёмщика", "Соответствие 161-ФЗ, 152-ФЗ"],
        "tags": ["Python", "ML", "PostgreSQL", "Kubernetes", "161-ФЗ"],
        "gradient": "#00b894,#55efc4",
        "widget_html": """<div class="dw">
  <h3 class="dw-t">📊 Кредитный калькулятор</h3>
  <div class="dw-b">
    <div class="dw-f"><label class="dw-l">Сумма кредита: <strong id="cc-a">500 000</strong> ₽</label><input class="dw-i" id="cc-as" type="range" min="100000" max="5000000" step="10000" value="500000" style="accent-color:var(--clr-accent);width:100%"></div>
    <div class="dw-f"><label class="dw-l">Срок: <strong id="cc-t">12</strong> мес.</label><input class="dw-i" id="cc-ts" type="range" min="3" max="24" step="1" value="12" style="accent-color:var(--clr-accent);width:100%"></div>
    <div style="padding:16px;background:var(--clr-bg);border-radius:12px;margin:8px 0;text-align:center">
      <div style="font-size:12px;color:var(--clr-muted)">Ежемесячный платёж</div>
      <div id="cc-pm" style="font-size:28px;font-weight:700;color:var(--clr-heading);font-variant-numeric:tabular-nums">43 124 ₽</div>
      <div style="font-size:12px;color:var(--clr-muted);margin-top:4px">Ставка: 12.9% годовых</div>
    </div>
    <div style="display:flex;align-items:center;justify-content:center;gap:8px;color:#00b894;font-weight:600;font-size:14px"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00b894" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Предварительное одобрение</div>
  </div>
</div>
<style>.dw{margin:12px 0;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:16px;padding:24px}.dw-t{font-size:16px;font-weight:600;margin:0 0 16px;color:var(--clr-heading)}.dw-b{display:flex;flex-direction:column;gap:10px}.dw-f{display:flex;flex-direction:column;gap:3px}.dw-l{font-size:13px;color:var(--clr-text);font-weight:500}.dw-i{background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:10px;color:var(--clr-text);font-size:14px;box-sizing:border-box}.dw-i[type=range]{border:none;background:none;padding:4px 0}@media(min-width:768px){.dw{max-width:520px;margin-left:auto;margin-right:auto}}</style>
<script>(function(){var as=document.getElementById('cc-as'),ts=document.getElementById('cc-ts'),pm=document.getElementById('cc-pm'),ae=document.getElementById('cc-a'),te=document.getElementById('cc-t');function calc(){var a=parseFloat(as.value),t=parseInt(ts.value),r=0.129/12;if(r===0){pm.textContent=Math.round(a/t).toLocaleString('ru')+' ₽'}else{var mp=a*r*Math.pow(1+r,t)/(Math.pow(1+r,t)-1);pm.textContent=Math.round(mp).toLocaleString('ru')+' ₽'}ae.textContent=Math.round(a).toLocaleString('ru');te.textContent=t}as.addEventListener('input',calc);ts.addEventListener('input',calc);calc()})();</script>""",
        "widget_css": "",
        "widget_js": ""
    },
    {
        "slug": "marketplace",
        "title": "Маркетплейс",
        "desc": "Готовая платформа маркетплейса: каталог, корзина, оплата, доставка, отзывы и личный кабинет продавца.",
        "meta_desc": "Демо маркетплейс-платформы: каталог товаров, корзина, мультиэквайринг, доставка, личный кабинет продавца. Full-stack решение.",
        "widget_html": """<div class="dw">
  <h3 class="dw-t" style="display:flex;justify-content:space-between;align-items:center">🛒 Маркетплейс <span id="mp-cnt-badge" style="background:var(--clr-accent);color:#fff;font-size:11px;font-weight:600;min-width:20px;height:20px;border-radius:10px;display:none;align-items:center;justify-content:center">0</span></h3>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:10px">
    <div class="mp-c"><div class="mp-img" style="background:linear-gradient(135deg,#6c5ce7,#a29bfe)">📱</div><div class="mp-n">Phone X Pro</div><div class="mp-p">79 990 ₽</div><button class="dw-btn mp-b" data-n="Phone X Pro" data-p="79990">В корзину</button></div>
    <div class="mp-c"><div class="mp-img" style="background:linear-gradient(135deg,#00b894,#55efc4)">💻</div><div class="mp-n">NoteBook Air</div><div class="mp-p">129 990 ₽</div><button class="dw-btn mp-b" data-n="NoteBook Air" data-p="129990">В корзину</button></div>
    <div class="mp-c"><div class="mp-img" style="background:linear-gradient(135deg,#fd79a8,#e84393)">🎧</div><div class="mp-n">Headphones Pro</div><div class="mp-p">14 990 ₽</div><button class="dw-btn mp-b" data-n="Headphones Pro" data-p="14990">В корзину</button></div>
    <div class="mp-c"><div class="mp-img" style="background:linear-gradient(135deg,#fdcb6e,#f39c12)">⌚</div><div class="mp-n">Watch Ultra</div><div class="mp-p">49 990 ₽</div><button class="dw-btn mp-b" data-n="Watch Ultra" data-p="49990">В корзину</button></div>
  </div>
  <div id="mp-cart" style="display:none;margin-top:16px;padding:16px;background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:12px">
    <div style="font-size:14px;font-weight:600;color:var(--clr-heading);margin-bottom:8px">Корзина</div>
    <div id="mp-items"></div>
    <div style="display:flex;justify-content:space-between;padding-top:8px;border-top:1px solid var(--clr-border);margin-top:8px;font-weight:700;color:var(--clr-heading)"><span>Итого:</span><span id="mp-total">0 ₽</span></div>
    <button class="dw-btn" id="mp-checkout-btn" style="margin-top:12px;width:100%">Оформить заказ</button>
  </div>
</div>
<div id="mp-modal" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.7);z-index:99999;align-items:center;justify-content:center">
  <div style="background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:16px;padding:32px;max-width:400px;width:90%;text-align:center">
    <h3 style="color:var(--clr-heading);margin-bottom:16px">Оформление заказа</h3>
    <div id="mp-modal-items" style="font-size:13px;color:var(--clr-muted);margin-bottom:16px;text-align:left"></div>
    <div id="mp-modal-total" style="font-size:18px;font-weight:700;color:var(--clr-heading);margin-bottom:20px"></div>
    <button class="dw-btn" id="mp-confirm" style="width:100%;margin-bottom:8px">Подтвердить заказ</button>
    <button class="dw-btn" id="mp-cancel" style="background:transparent;border:1px solid var(--clr-border);color:var(--clr-muted)">Отмена</button>
    <div id="mp-success" style="display:none;padding:20px"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#00b894" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><h3 style="color:#00b894;margin-top:12px">Заказ оформлен!</h3><p style="font-size:13px;color:var(--clr-muted);margin-top:4px">Номер: MK-<span id="mp-order-year"></span>-<span id="mp-order-num"></span></p></div>
  </div>
</div>
<style>.dw{margin:12px 0;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:16px;padding:24px}.dw-t{font-size:16px;font-weight:600;margin:0 0 16px;color:var(--clr-heading)}.dw-btn{padding:8px 12px;background:var(--clr-accent);border:none;border-radius:8px;color:#fff;font-size:13px;font-weight:600;cursor:pointer;transition:opacity .2s;width:100%}.dw-btn:hover{opacity:.85}.mp-c{background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:12px;padding:12px;text-align:center}.mp-img{width:100%;height:80px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:32px;margin-bottom:8px}.mp-n{font-size:13px;font-weight:500;color:var(--clr-text);margin-bottom:4px}.mp-p{font-size:15px;font-weight:700;color:var(--clr-heading);margin-bottom:8px}.mp-ci{display:flex;justify-content:space-between;padding:4px 0;font-size:13px;color:var(--clr-text)}.mp-ci button{background:none;border:none;color:var(--clr-muted);cursor:pointer;font-size:11px;text-decoration:underline;padding:0}@media(min-width:768px){.dw{max-width:640px;margin-left:auto;margin-right:auto}}</style>
<script>(function(){
var items={},badge=document.getElementById('mp-cnt-badge'),cart=document.getElementById('mp-cart'),list=document.getElementById('mp-items'),total=document.getElementById('mp-total'),modal=document.getElementById('mp-modal'),mItems=document.getElementById('mp-modal-items'),mTotal=document.getElementById('mp-modal-total');
function render(){var html='',t=0,c=0;for(var k in items){var it=items[k];html+='<div class="mp-ci"><span>'+it.n+' × '+it.q+'</span><span>'+((it.p*it.q).toLocaleString('ru'))+' ₽ <button class="mp-rm" data-k="'+k+'">✕</button></span></div>';t+=it.p*it.q;c+=it.q}list.innerHTML=html;total.textContent=t.toLocaleString('ru')+' ₽';badge.textContent=c;badge.style.display=c?'flex':'none';cart.style.display=c?'block':'none';Array.from(list.querySelectorAll('.mp-rm')).forEach(function(b){b.addEventListener('click',function(){var k=this.dataset.k;delete items[k];render()})})};
document.querySelectorAll('.mp-b').forEach(function(b){b.addEventListener('click',function(){var n=this.dataset.n,p=parseInt(this.dataset.p);if(!items[n])items[n]={n:n,p:p,q:0};items[n].q++;render();this.textContent='✓ '+n;var t=this;setTimeout(function(){t.textContent='В корзину'},800)})});
document.getElementById('mp-checkout-btn').addEventListener('click',function(){var h='';for(var k in items){h+='<div style="display:flex;justify-content:space-between;padding:2px 0"><span>'+items[k].n+' × '+items[k].q+'</span><span>'+((items[k].p*items[k].q).toLocaleString('ru'))+' ₽</span></div>'}mItems.innerHTML=h;var t=0;for(var k in items)t+=items[k].p*items[k].q;mTotal.textContent='Итого: '+t.toLocaleString('ru')+' ₽';modal.style.display='flex'});
document.getElementById('mp-confirm').addEventListener('click',function(){var s=document.getElementById('mp-success');s.style.display='block';s.querySelector('h3').textContent='Заказ оформлен!';document.getElementById('mp-order-year').textContent=new Date().getFullYear();document.getElementById('mp-order-num').textContent=Math.floor(100000+Math.random()*900000);document.querySelector('#mp-modal > div > h3').style.display='none';document.getElementById('mp-modal-items').style.display='none';document.getElementById('mp-modal-total').style.display='none';this.style.display='none';document.getElementById('mp-cancel').style.display='none';items={};render();setTimeout(function(){modal.style.display='none';location.reload()},2500)});
document.getElementById('mp-cancel').addEventListener('click',function(){modal.style.display='none'});
modal.addEventListener('click',function(e){if(e.target===modal)modal.style.display='none'});
})();</script>""",
        "code": """// Добавление товара продавцом
await marketplace.addProduct({
  sellerId: 'seller_789',
  name: 'Смартфон X Pro',
  price: 79990,
  category: 'electronics',
  stock: 50
});

// Оформление заказа покупателем
const order = await marketplace.checkout({
  items: [
    { productId: 'prod_123', quantity: 1 },
    { productId: 'prod_456', quantity: 2 }
  ],
  delivery: 'cdek',
  paymentMethod: 'card'
});

// Сплитование выплаты продавцу
await marketplace.settle(order.id);""",
        "features": ["Каталог с фильтрацией и поиском", "Мультиэквайринг и сплитование", "Личный кабинет продавца", "Интеграция с СДЭК, Почтой России", "Система отзывов и рейтингов", "Аналитика продаж"],
        "tags": ["Vue.js", "Node.js", "PostgreSQL", "Elasticsearch", "Redis"],
        "gradient": "#0984e3,#74b9ff"
    },
    {
        "slug": "payment-terminal",
        "title": "Платёжный терминал",
        "desc": "POS-терминал для приёма платежей: карты, NFC, QR-коды, SBP. Работает на Android и iOS.",
        "meta_desc": "Демо мобильного POS-терминала: приём платежей по картам, NFC, SBP, QR. Соответствие PCI DSS. Примеры интеграции.",
        "code": """// Инициализация терминала
const terminal = new PaymentTerminal({
  merchantId: 'merchant_456',
  terminalId: 'T-001',
  apiKey: 'sk_live_***'
});

// Приём платежа по карте
const payment = await terminal.processCard({
  amount: 3500.00,
  currency: 'RUB',
  cardPresent: true // чип/NFC
});

// Оплата по QR (SBP)
const qrPayment = await terminal.processSBP({
  amount: 1299.00,
  bank: 'sbp'
});

// Печать чека
await terminal.printReceipt(payment.id);""",
        "features": ["Приём карт, NFC, QR, SBP", "Онлайн-касса (ФНС/ККТ)", "Печать чеков (Bluetooth)", "Возвраты и отмены", "Офлайн-режим", "Аналитика и отчёты"],
        "tags": ["Swift", "Kotlin", "Flutter", "PCI DSS", "54-ФЗ"],
        "gradient": "#fdcb6e,#f39c12",
        "widget_html": """<div class="dw">
  <h3 class="dw-t">💳 POS-терминал</h3>
  <div style="display:flex;flex-direction:column;align-items:center;gap:12px">
    <div style="background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:12px;padding:16px;width:100%;text-align:center">
      <div style="font-size:12px;color:var(--clr-muted);margin-bottom:4px">Сумма к оплате</div>
      <div id="pt-amt" style="font-size:36px;font-weight:700;color:var(--clr-heading);font-variant-numeric:tabular-nums;min-height:44px">0 ₽</div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;width:100%;max-width:280px">
      <button class="pt-k" data-v="1">1</button><button class="pt-k" data-v="2">2</button><button class="pt-k" data-v="3">3</button>
      <button class="pt-k" data-v="4">4</button><button class="pt-k" data-v="5">5</button><button class="pt-k" data-v="6">6</button>
      <button class="pt-k" data-v="7">7</button><button class="pt-k" data-v="8">8</button><button class="pt-k" data-v="9">9</button>
      <button class="pt-k" data-v="00">00</button><button class="pt-k" data-v="0">0</button><button class="pt-k pt-clr" id="pt-clr">C</button>
    </div>
    <button class="dw-btn" id="pt-pay" style="width:100%;max-width:280px">Оплатить</button>
    <div id="pt-st" style="display:none;text-align:center;padding:12px">
      <div class="dw-sp" id="pt-sp"></div>
      <div id="pt-ok" style="display:none;color:#00b894;font-weight:600;font-size:15px">✅ Оплата принята</div>
    </div>
  </div>
</div>
<style>.dw{margin:12px 0;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:16px;padding:24px}.dw-t{font-size:16px;font-weight:600;margin:0 0 16px;color:var(--clr-heading)}.dw-btn{padding:12px;background:var(--clr-accent);border:none;border-radius:10px;color:#fff;font-size:15px;font-weight:600;cursor:pointer;transition:opacity .2s}.dw-btn:hover{opacity:.85}.dw-sp{width:28px;height:28px;border:2px solid var(--clr-border);border-top-color:var(--clr-accent);border-radius:50%;animation:dws .7s linear infinite;margin:0 auto}.pt-k{padding:14px;background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:10px;color:var(--clr-text);font-size:20px;font-weight:600;cursor:pointer;transition:all .15s;text-align:center}.pt-k:hover{background:var(--clr-surface);border-color:var(--clr-accent)}.pt-k:active{transform:scale(.95)}.pt-clr{color:#e17055;border-color:#e1705544}@keyframes dws{to{transform:rotate(360deg)}}@media(min-width:768px){.dw{max-width:400px;margin-left:auto;margin-right:auto}}</style>
<script>(function(){var amt=0,e=document.getElementById('pt-amt'),b=document.getElementById('pt-pay'),st=document.getElementById('pt-st'),sp=document.getElementById('pt-sp'),ok=document.getElementById('pt-ok');document.querySelectorAll('.pt-k').forEach(function(k){k.addEventListener('click',function(){if(this.id==='pt-clr'){amt=0}else{var v=this.dataset.v;amt=amt*100+parseInt(v)}e.textContent=Math.round(amt).toLocaleString('ru')+' ₽'});});b.addEventListener('click',function(){if(amt<=0)return;b.style.display='none';st.style.display='block';sp.style.display='block';ok.style.display='none';setTimeout(function(){sp.style.display='none';ok.style.display='block'},1500);});})();</script>""",
        "widget_css": "",
        "widget_js": ""
    },
    {
        "slug": "chatbot-support",
        "title": "Чат-бот техподдержки",
        "desc": "AI-чат-бот техподдержки с NLP: ответы на вопросы, создание тикетов, эскалация на оператора. Интеграция с Telegram, WhatsApp, VK.",
        "meta_desc": "Демо AI-чат-бота техподдержки: NLP, создание тикетов, эскалация, интеграция с Telegram/WhatsApp/VK. Примеры кода.",
        "code": """// Обработка входящего сообщения
const response = await chatbot.handleMessage({
  channel: 'telegram',
  userId: 'tg_123456',
  text: 'Как пополнить баланс?'
});

// Ответ бота
// { type: 'text', text: 'Пополнить баланс можно...' }

// Создание тикета (эскалация)
const ticket = await chatbot.createTicket({
  userId: 'tg_123456',
  reason: 'Не прошёл платёж',
  priority: 'high',
  assignTo: 'support_team'
});

// Отправка уведомления оператору
await chatbot.notifyOperator(ticket.id);""",
        "features": ["NLP-движок с кастомизацией", "Интеграция с Telegram, WhatsApp, VK", "Создание и эскалация тикетов", "База знаний (FAQ)", "Аналитика диалогов", "Передача оператору с контекстом"],
        "tags": ["Python", "Node.js", "NLP/LLM", "Redis", "WebSocket"],
        "gradient": "#e17055,#fab1a0",
        "widget_html": """<div class="dw">
  <h3 class="dw-t">💬 Чат техподдержки</h3>
  <div style="border:1px solid var(--clr-border);border-radius:12px;overflow:hidden;background:var(--clr-bg)">
    <div id="ch-msgs" style="height:220px;overflow-y:auto;padding:12px;display:flex;flex-direction:column;gap:8px">
      <div style="align-self:flex-start;background:var(--clr-surface);padding:10px 14px;border-radius:12px 12px 12px 4px;max-width:80%;font-size:14px;color:var(--clr-text);border:1px solid var(--clr-border)">Здравствуйте! Чем могу помочь?</div>
    </div>
    <div style="display:flex;gap:8px;padding:10px 12px;border-top:1px solid var(--clr-border)">
      <input id="ch-inp" placeholder="Напишите сообщение..." class="dw-i" style="flex:1" onkeydown="if(event.key==='Enter')chSend()">
      <button class="dw-btn" id="ch-btn" style="padding:10px 16px;font-size:13px" onclick="chSend()">→</button>
    </div>
  </div>
  <div style="margin-top:10px;display:flex;flex-wrap:wrap;gap:6px">
    <button class="dw-btn ch-q" style="padding:6px 12px;font-size:12px" data-q="Привет">Привет</button>
    <button class="dw-btn ch-q" style="padding:6px 12px;font-size:12px" data-q="Как пополнить?">Как пополнить?</button>
    <button class="dw-btn ch-q" style="padding:6px 12px;font-size:12px" data-q="Проблема с платежом">Проблема с платежом</button>
  </div>
</div>
<style>.dw{margin:12px 0;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:16px;padding:24px}.dw-t{font-size:16px;font-weight:600;margin:0 0 16px;color:var(--clr-heading)}.dw-i{width:100%;padding:10px 14px;background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:10px;color:var(--clr-text);font-size:14px;box-sizing:border-box}.dw-i:focus{outline:none;border-color:var(--clr-accent)}.dw-btn{padding:12px;background:var(--clr-accent);border:none;border-radius:10px;color:#fff;font-size:15px;font-weight:600;cursor:pointer;transition:opacity .2s}.dw-btn:hover{opacity:.85}@media(min-width:768px){.dw{max-width:520px;margin-left:auto;margin-right:auto}}</style>
<script>var chMsgs=document.getElementById('ch-msgs'),chInp=document.getElementById('ch-inp');var chRes={'привет':'Привет! Чем могу помочь?','как пополнить':'Пополнить баланс можно через личный кабинет или приложение. Выберите способ: карта, SBP или кошелёк.','проблема с платежом':'Опишите проблему подробнее. Возможно, потребуется проверить статус транзакции. Напишите номер операции.','по умолчанию':'Передаю ваш вопрос специалисту. Пожалуйста, ожидайте.'};function chAdd(m,u){var d=document.createElement('div');d.style.cssText='align-self:'+(u?'flex-end':'flex-start')+';background:'+(u?'var(--clr-accent)':'var(--clr-surface)')+';padding:10px 14px;border-radius:'+(u?'4px 12px 12px 12px':'12px 12px 12px 4px')+';max-width:80%;font-size:14px;color:'+(u?'#fff':'var(--clr-text)')+';'+(u?'':'border:1px solid var(--clr-border)');d.textContent=m;chMsgs.appendChild(d);chMsgs.scrollTop=chMsgs.scrollHeight}function chSend(){var t=chInp.value.trim();if(!t)return;chAdd(t,1);chInp.value='';var r=t.toLowerCase();var a=chRes[r]||Object.keys(chRes).filter(function(k){return r.includes(k)}).map(function(k){return chRes[k]})[0]||chRes['по умолчанию'];setTimeout(function(){chAdd(a,0)},500)}document.querySelectorAll('.ch-q').forEach(function(b){b.addEventListener('click',function(){chInp.value=this.dataset.q;chSend()})});</script>""",
        "widget_css": "",
        "widget_js": ""
    },
    {
        "slug": "analytics-dashboard",
        "title": "Аналитическая панель",
        "desc": "Real-time дашборд с метриками бизнеса: DAU/MAU, LTV, конверсии, когортный анализ, funnel report.",
        "meta_desc": "Демо аналитической панели: real-time метрики, когорты, воронки, LTV. Примеры кода построения дашбордов и API.",
        "code": """// Получение метрик за период
const metrics = await analytics.getMetrics({
  period: 'last_30_days',
  metrics: ['dau', 'mau', 'conversion', 'ltv'],
  groupBy: 'day'
});

// Построение воронки
const funnel = await analytics.buildFunnel({
  steps: ['visit', 'register', 'deposit', 'purchase'],
  startDate: '2024-01-01',
  endDate: '2024-06-30'
});

// Когортный анализ
const cohorts = await analytics.cohortAnalysis({
  period: 'monthly',
  metric: 'retention'
});""",
        "features": ["Real-time метрики (WebSocket)", "Когортный анализ", "Воронки конверсий", "Custom report builder", "Экспорт в PDF/Excel", "Alerting и аномалии"],
        "tags": ["React", "D3.js", "ClickHouse", "Go", "Kafka"],
        "gradient": "#74b9ff,#0984e3",
        "widget_html": """<div class="dw">
  <h3 class="dw-t">📈 Аналитическая панель</h3>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
    <div class="an-c"><div class="an-l">DAU</div><div class="an-v" id="an-dau">0</div></div>
    <div class="an-c"><div class="an-l">MAU</div><div class="an-v" id="an-mau">0</div></div>
    <div class="an-c"><div class="an-l">LTV</div><div class="an-v" id="an-ltv">0 ₽</div></div>
    <div class="an-c"><div class="an-l">Конверсия</div><div class="an-v" id="an-conv">0%</div></div>
  </div>
  <div style="margin-top:12px;padding:12px;background:var(--clr-bg);border-radius:10px">
    <div style="font-size:12px;color:var(--clr-muted);margin-bottom:8px">Активность за неделю</div>
    <div style="display:flex;gap:4px;align-items:flex-end;height:60px">
      <div class="an-bar" style="height:60%"></div><div class="an-bar" style="height:45%"></div><div class="an-bar" style="height:70%"></div><div class="an-bar" style="height:55%"></div><div class="an-bar" style="height:85%"></div><div class="an-bar" style="height:65%"></div><div class="an-bar" style="height:50%"></div>
    </div>
  </div>
</div>
<style>.dw{margin:12px 0;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:16px;padding:24px}.dw-t{font-size:16px;font-weight:600;margin:0 0 16px;color:var(--clr-heading)}.an-c{background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:10px;padding:14px;text-align:center}.an-l{font-size:12px;color:var(--clr-muted);margin-bottom:4px;font-weight:500}.an-v{font-size:22px;font-weight:700;color:var(--clr-heading);font-variant-numeric:tabular-nums}.an-bar{flex:1;background:linear-gradient(to top,var(--clr-accent),transparent);border-radius:3px 3px 0 0;min-height:8px;opacity:.7;transition:height .5s}@media(min-width:768px){.dw{max-width:640px;margin-left:auto;margin-right:auto}}</style>
<script>(function(){function an(e,v){var el=document.getElementById(e),s=0,i=setInterval(function(){s++;var d=Math.round(v*s/60);el.textContent=d+(e==='an-ltv'?' ₽':e==='an-conv'?'.'+(d%10)+'%':'');if(s>=60){clearInterval(i);el.textContent=v+(e==='an-ltv'?' ₽':e==='an-conv'?'.'+String(v).split('.')[1]+'%':'')}},20)}an('an-dau',12450);an('an-mau',45200);an('an-ltv',12500);setTimeout(function(){an('an-conv',32)},200);})();</script>""",
        "widget_css": "",
        "widget_js": ""
    },
    {
        "slug": "incident-monitoring",
        "title": "Мониторинг инцидентов",
        "desc": "Система мониторинга и оповещения: сбор метрик, алерты, on-call, postmortem, SLA-дашборд.",
        "meta_desc": "Демо системы мониторинга инцидентов: сбор метрик, алерты, on-call, postmortem, SLA-дашборд. Примеры кода интеграции.",
        "code": """// Создание алерта
await monitoring.createAlert({
  name: 'High CPU Usage',
  metric: 'cpu_usage',
  condition: '> 90',
  duration: '5m',
  severity: 'critical',
  channels: ['telegram', 'email', 'sms']
});

// Регистрация инцидента
const incident = await monitoring.incident({
  alertId: 'alert_789',
  status: 'firing',
  value: 94.5,
  threshold: 90
});

// Аcknowledge
await monitoring.acknowledge(incident.id, {
  assignee: 'devops_team',
  note: 'Начинаем диагностику' 
});""",
        "features": ["Сбор метрик (Prometheus/StatsD)", "Гибкие алерты с эскалацией", "On-call scheduling", "Postmortem и RCA", "SLA/SLO дашборд", "Интеграция с PagerDuty, Telegram"],
        "tags": ["Go", "Prometheus", "Grafana", "Kubernetes", "ClickHouse"],
        "gradient": "#2d3436,#636e72",
        "widget_html": """<div class="dw">
  <h3 class="dw-t">🔍 Мониторинг сервисов</h3>
  <div style="display:flex;flex-direction:column;gap:8px">
    <div class="im-r" data-s="ok"><span class="im-d im-g"></span><span class="im-n">API Gateway</span><span class="im-s">Operational</span></div>
    <div class="im-r" data-s="ok"><span class="im-d im-g"></span><span class="im-n">Database</span><span class="im-s">Operational</span></div>
    <div class="im-r" data-s="warn"><span class="im-d im-y"></span><span class="im-n">Cache (Redis)</span><span class="im-s">Degraded</span></div>
    <div class="im-r" data-s="ok"><span class="im-d im-g"></span><span class="im-n">Message Queue</span><span class="im-s">Operational</span></div>
    <div class="im-r" data-s="ok"><span class="im-d im-g"></span><span class="im-n">Frontend CDN</span><span class="im-s">Operational</span></div>
  </div>
  <div id="im-alert" style="display:none;margin-top:10px;padding:10px 14px;background:#e1705522;border:1px solid #e1705544;border-radius:10px;color:#e17055;font-size:13px;font-weight:500">⚠️ Инцидент: сервис недоступен</div>
  <div style="margin-top:10px;font-size:11px;color:var(--clr-muted)">Нажмите на сервис, чтобы переключить статус</div>
</div>
<style>.dw{margin:12px 0;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:16px;padding:24px}.dw-t{font-size:16px;font-weight:600;margin:0 0 16px;color:var(--clr-heading)}.im-r{display:flex;align-items:center;gap:10px;padding:10px 14px;background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:10px;cursor:pointer;transition:all .2s}.im-r:hover{border-color:var(--clr-accent)}.im-d{width:10px;height:10px;border-radius:50%;flex-shrink:0}.im-g{background:#00b894;box-shadow:0 0 6px #00b89466}.im-y{background:#fdcb6e;box-shadow:0 0 6px #fdcb6e66}.im-red{background:#e17055;box-shadow:0 0 6px #e1705566}.im-n{flex:1;font-size:14px;font-weight:500;color:var(--clr-text)}.im-s{font-size:12px;color:var(--clr-muted)}@media(min-width:768px){.dw{max-width:640px;margin-left:auto;margin-right:auto}}</style>
<script>(function(){var st={0:'ok',1:'ok',2:'warn',3:'ok',4:'ok'},al=document.getElementById('im-alert');document.querySelectorAll('.im-r').forEach(function(r,i){r.addEventListener('click',function(){var sts=['ok','warn','down'];var ci=sts.indexOf(st[i]);st[i]=sts[(ci+1)%3];var d=r.querySelector('.im-d');d.className='im-d';if(st[i]==='ok'){d.classList.add('im-g');r.querySelector('.im-s').textContent='Operational'}else if(st[i]==='warn'){d.classList.add('im-y');r.querySelector('.im-s').textContent='Degraded'}else{d.classList.add('im-red');r.querySelector('.im-s').textContent='Down'}var hasDown=Object.values(st).some(function(s){return s==='down'});al.style.display=hasDown?'block':'none';al.textContent=hasDown?'⚠️ Инцидент: требуется внимание':'✅ Все сервисы работают';al.style.color=hasDown?'#e17055':'#00b894'});});})();</script>""",
        "widget_css": "",
        "widget_js": ""
    },
    {
        "slug": "user-onboarding",
        "title": "Онбординг пользователей",
        "desc": "White-label решение для онбординга: KYC, верификация, скоринг, интеграция с госуслугами и БКИ.",
        "meta_desc": "Демо системы онбординга: KYC, верификация документов, биометрия, интеграция с Госуслугами. Соответствие 115-ФЗ и 161-ФЗ.",
        "code": """// Начало онбординга
const session = await onboarding.createSession({
  userId: 'user_789',
  steps: ['passport', 'selfie', 'phone', 'address']
});

// Верификация паспорта
const passport = await onboarding.verifyPassport({
  sessionId: session.id,
  series: '4010',
  number: '123456',
  issuedBy: 'УФМС...'
});

// Биометрическая верификация
const biometric = await onboarding.verifyBiometric({
  sessionId: session.id,
  selfie: fileBuffer,
  passportPhoto: fileBuffer
});""",
        "features": ["KYC и AML-проверки", "Верификация документов (AI)", "Биометрия (liveness detection)", "Интеграция с Госуслугами", "Скоринг и фрод-мониторинг", "Соответствие 115-ФЗ, 161-ФЗ"],
        "tags": ["Python", "React", "PostgreSQL", "ML/AI", "115-ФЗ"],
        "gradient": "#a29bfe,#6c5ce7",
        "widget_html": """<div class="dw">
  <h3 class="dw-t">🚀 Онбординг</h3>
  <div style="display:flex;align-items:center;gap:8px;margin-bottom:20px;position:relative">
    <div class="ub s" data-s="1"><div class="ub-n">1</div><div class="ub-lb">Данные</div></div><div class="ub-l"></div>
    <div class="ub" data-s="0"><div class="ub-n">2</div><div class="ub-lb">Документы</div></div><div class="ub-l"></div>
    <div class="ub" data-s="0"><div class="ub-n">3</div><div class="ub-lb">Биометрия</div></div><div class="ub-l"></div>
    <div class="ub" data-s="0"><div class="ub-n">4</div><div class="ub-lb">Готово</div></div>
  </div>
  <div id="ub-c" style="padding:16px;background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:12px;min-height:80px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;transition:all .3s">
    <div style="font-size:14px;color:var(--clr-text);text-align:center" id="ub-t">Заполните личные данные для регистрации</div>
    <div id="ub-f" style="width:100%;max-width:280px;display:flex;flex-direction:column;gap:8px">
      <input class="dw-i" placeholder="Имя" value="Иван" style="padding:10px 14px;font-size:14px">
      <input class="dw-i" placeholder="Телефон" value="+7 (999) 123-45-67" style="padding:10px 14px;font-size:14px">
    </div>
  </div>
  <button class="dw-btn" id="ub-btn" style="margin-top:12px;width:100%">Далее</button>
</div>
<style>.dw{margin:12px 0;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:16px;padding:24px}.dw-t{font-size:16px;font-weight:600;margin:0 0 16px;color:var(--clr-heading)}.dw-i{background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:10px;color:var(--clr-text);box-sizing:border-box;width:100%}.dw-i:focus{outline:none;border-color:var(--clr-accent)}.dw-btn{padding:12px;background:var(--clr-accent);border:none;border-radius:10px;color:#fff;font-size:15px;font-weight:600;cursor:pointer;transition:opacity .2s}.dw-btn:hover{opacity:.85}.ub{display:flex;flex-direction:column;align-items:center;gap:4px;flex:1}.ub-n{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;background:var(--clr-bg);border:2px solid var(--clr-border);color:var(--clr-muted);transition:all .3s}.ub.s .ub-n{background:var(--clr-accent);border-color:var(--clr-accent);color:#fff}.ub-l{height:2px;flex:1;background:var(--clr-border);margin-bottom:22px}.ub-lb{font-size:11px;color:var(--clr-muted);white-space:nowrap}@media(min-width:768px){.dw{max-width:520px;margin-left:auto;margin-right:auto}}</style>
<script>(function(){var s=1,btn=document.getElementById('ub-btn'),ct=document.getElementById('ub-c'),tt=document.getElementById('ub-t'),ff=document.getElementById('ub-f'),steps=['Заполните личные данные для регистрации','Загрузите скан паспорта','Пройдите биометрию','Регистрация завершена!'],cont=[true,true,true,false];function upd(){document.querySelectorAll('.ub').forEach(function(el,i){var idx=parseInt(el.dataset.s);el.classList.toggle('s',i+1<=s);});tt.textContent=steps[s-1];if(cont[s-1]){ff.style.display='flex';btn.textContent=s<4?'Далее':'Завершить'}else{ff.style.display='none';btn.style.display='none';ct.innerHTML='<div style=\"font-size:42px;margin-bottom:8px\">✅</div><div style=\"font-size:16px;font-weight:600;color:#00b894\">'+steps[s-1]+'</div>';}}btn.addEventListener('click',function(){if(s<4){s++;upd()}else{ct.innerHTML='<div style=\"font-size:42px;margin-bottom:8px\">✅</div><div style=\"font-size:16px;font-weight:600;color:#00b894\">Добро пожаловать!</div>';btn.style.display='none'}});upd()})();</script>""",
        "widget_css": "",
        "widget_js": ""
    },
    {
        "slug": "telegram-storefront",
        "title": "Витрина в Telegram",
        "desc": "Telegram Mini App — витрина товаров/услуг с оплатой прямо в мессенджере. Каталог, корзина, платежи, уведомления.",
        "meta_desc": "Демо Telegram Mini App: витрина товаров с оплатой внутри Telegram, каталог, корзина, уведомления. Примеры кода создания Mini App.",
        "code": """// Инициализация Telegram Mini App
const tg = window.Telegram.WebApp;
tg.ready();
tg.expand();

// Получение данных пользователя
const user = tg.initDataUnsafe.user;
// { id: 123456, first_name: 'Иван', ... }

// Загрузка каталога товаров
const products = await store.getProducts({
  category: 'electronics',
  page: 1,
  limit: 20
});

// Оформление заказа
const order = await store.createOrder({
  userId: user.id,
  items: cart,
  delivery: 'pickup'
});

// Закрытие Mini App
tg.close();""",
        "features": ["Telegram Mini App (TWA)", "Каталог с поиском и фильтрацией", "Оплата через Telegram Stars", "Push-уведомления через бота", "История заказов", "Аналитика продаж"],
        "tags": ["React", "Node.js", "Telegram API", "PostgreSQL"],
        "gradient": "#55efc4,#00b894",
        "widget_html": """<div class="dw">
  <h3 class="dw-t">📱 Telegram Shop</h3>
  <div style="border:2px solid var(--clr-border);border-radius:20px;padding:12px;max-width:300px;margin:0 auto;position:relative">
    <div style="height:20px;width:120px;background:var(--clr-bg);border-radius:0 0 10px 10px;margin:0 auto 12px;border:1px solid var(--clr-border);border-top:none"></div>
    <div style="display:flex;flex-direction:column;gap:10px">
      <div class="ts-c"><div style="background:linear-gradient(135deg,#6c5ce7,#a29bfe);width:40px;height:40px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:20px">📱</div><div style="flex:1"><div style="font-size:13px;font-weight:500;color:var(--clr-text)">Phone X</div><div style="font-size:14px;font-weight:700;color:var(--clr-heading)">79 990 ₽</div></div><button class="ts-b">Купить</button></div>
      <div class="ts-c"><div style="background:linear-gradient(135deg,#00b894,#55efc4);width:40px;height:40px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:20px">🎧</div><div style="flex:1"><div style="font-size:13px;font-weight:500;color:var(--clr-text)">Buds Pro</div><div style="font-size:14px;font-weight:700;color:var(--clr-heading)">14 990 ₽</div></div><button class="ts-b">Купить</button></div>
      <div class="ts-c"><div style="background:linear-gradient(135deg,#fdcb6e,#f39c12);width:40px;height:40px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:20px">⌚</div><div style="flex:1"><div style="font-size:13px;font-weight:500;color:var(--clr-text)">Watch</div><div style="font-size:14px;font-weight:700;color:var(--clr-heading)">49 990 ₽</div></div><button class="ts-b">Купить</button></div>
    </div>
    <div style="display:flex;justify-content:space-between;align-items:center;margin-top:12px;padding-top:10px;border-top:1px solid var(--clr-border)">
      <span style="font-size:12px;color:var(--clr-muted)">Итого:</span>
      <span id="ts-tot" style="font-size:16px;font-weight:700;color:var(--clr-heading)">0 ₽</span>
      <span style="background:var(--clr-accent);color:#fff;font-size:11px;font-weight:600;padding:2px 8px;border-radius:10px" id="ts-cnt">0</span>
    </div>
  </div>
</div>
<style>.dw{margin:12px 0;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:16px;padding:24px}.dw-t{font-size:16px;font-weight:600;margin:0 0 16px;color:var(--clr-heading)}.ts-c{display:flex;align-items:center;gap:10px;padding:8px;background:var(--clr-bg);border-radius:10px;border:1px solid var(--clr-border)}.ts-b{padding:6px 14px;background:var(--clr-accent);border:none;border-radius:8px;color:#fff;font-size:12px;font-weight:600;cursor:pointer;transition:opacity .2s;white-space:nowrap}.ts-b:hover{opacity:.85}@media(min-width:768px){.dw{max-width:400px;margin-left:auto;margin-right:auto}}</style>
<script>(function(){var tc=0,tt=0,ce=document.getElementById('ts-cnt'),te=document.getElementById('ts-tot');document.querySelectorAll('.ts-b').forEach(function(b,i){var ps=[79990,14990,49990];b.addEventListener('click',function(){tc++;tt+=ps[i];ce.textContent=tc;te.textContent=tt.toLocaleString('ru')+' ₽';var t=this;t.textContent='✓';setTimeout(function(){t.textContent='Купить'},1000);});});})();</script>""",
        "widget_css": "",
        "widget_js": ""
    },
    {
        "slug": "loyalty-system",
        "title": "Система лояльности",
        "desc": "Гибкая система лояльности с правилами, сегментацией, A/B-тестами и аналитикой в реальном времени.",
        "meta_desc": "Демо конструктора систем лояльности: правила, сегментация, A/B-тесты, аналитика. Гибкая настройка под любой бизнес.",
        "code": """// Создание правила лояльности
const rule = await loyalty.createRule({
  name: '3+1 бесплатно',
  trigger: 'purchase',
  condition: {
    category: 'coffee',
    minItems: 3
  },
  reward: {
    type: 'free_product',
    productId: 'coffee_any'
  }
});

// Сегментация пользователей
const segment = await loyalty.createSegment({
  name: 'VIP осень 2024',
  filters: [
    { spent: { gt: 50000 } },
    { visits: { gt: 10 } }
  ]
});

// Запуск A/B-теста
const ab = await loyalty.startABTest({
  name: 'Кешбэк 5% vs 10%',
  segments: ['A', 'B'],
  duration: 14
});""",
        "features": ["Конструктор правил и триггеров", "Сегментация аудитории", "A/B-тестирование механик", "Real-time аналитика", "Персонализированные офферы", "API для внешних систем"],
        "tags": ["Node.js", "React", "PostgreSQL", "Redis", "Kafka"],
        "gradient": "#e84393,#fd79a8",
        "widget_html": """<div class="dw">
  <h3 class="dw-t">⭐ Система лояльности</h3>
  <div style="text-align:center">
    <div style="display:flex;justify-content:center;gap:16px;margin-bottom:16px">
      <div style="text-align:center"><div style="font-size:12px;color:var(--clr-muted);margin-bottom:4px">Текущий</div><div id="ls-cur" style="padding:6px 16px;border-radius:20px;font-size:14px;font-weight:600;background:linear-gradient(135deg,#a8edea,#fed6e3);color:#1a1a2e">Silver</div></div>
      <div style="text-align:center"><div style="font-size:12px;color:var(--clr-muted);margin-bottom:4px">Следующий</div><div id="ls-nxt" style="padding:6px 16px;border-radius:20px;font-size:14px;font-weight:600;background:linear-gradient(135deg,#f6d365,#fda085);color:#1a1a2e">Gold</div></div>
    </div>
    <div style="margin-bottom:8px"><span style="font-size:13px;color:var(--clr-muted)">Прогресс: </span><strong id="ls-pct" style="color:var(--clr-heading)">67%</strong></div>
    <div style="height:8px;background:var(--clr-bg);border-radius:4px;overflow:hidden;margin-bottom:16px"><div id="ls-bar" style="height:100%;width:67%;background:linear-gradient(90deg,var(--clr-accent),#f6d365);border-radius:4px;transition:width .4s ease"></div></div>
    <div style="font-size:28px;font-weight:700;color:var(--clr-heading);font-variant-numeric:tabular-nums" id="ls-pt">1 340</div>
    <div style="font-size:13px;color:var(--clr-muted);margin-bottom:12px">баллов / 2 000 для Gold</div>
    <button class="dw-btn" id="ls-btn">Начислить +50 баллов</button>
  </div>
</div>
<style>.dw{margin:12px 0;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:16px;padding:24px}.dw-t{font-size:16px;font-weight:600;margin:0 0 16px;color:var(--clr-heading)}.dw-btn{padding:12px 20px;background:var(--clr-accent);border:none;border-radius:10px;color:#fff;font-size:14px;font-weight:600;cursor:pointer;transition:opacity .2s}.dw-btn:hover{opacity:.85}@media(min-width:768px){.dw{max-width:520px;margin-left:auto;margin-right:auto}}</style>
<script>(function(){var pts=1340,tg=2000,next='Gold',lvs=[{n:'Silver',t:1000,next:'Gold',g:'linear-gradient(135deg,#a8edea,#fed6e3)'},{n:'Gold',t:3000,next:'Platinum',g:'linear-gradient(135deg,#f6d365,#fda085)'},{n:'Platinum',t:99999,next:'MAX',g:'linear-gradient(135deg,#a18cd1,#fbc2eb)'}];var ce=document.getElementById('ls-cur'),ne=document.getElementById('ls-nxt'),pe=document.getElementById('ls-pct'),be=document.getElementById('ls-bar'),pe2=document.getElementById('ls-pt');document.getElementById('ls-btn').addEventListener('click',function(){var t=this;t.disabled=1;var si=setInterval(function(){pts++;if(pts<=tg){var pc=Math.round((pts-1000)/(tg-1000)*100);pe.textContent=pc+'%';be.style.width=pc+'%'}pe2.textContent=pts.toLocaleString('ru');var cl=lvs.filter(function(l){return pts>=l.t});var cu=cl[cl.length-1];if(cu){ce.textContent=cu.n;ce.style.background=cu.g;if(cu.next){ne.textContent=cu.next;tg=lvs.filter(function(l){return l.t>pts})[0]?.t||99999;ne.style.background=lvs.filter(function(l){return l.t>pts})[0]?.g||'#333'}}if(pts>=tg+30||pts%50===0){clearInterval(si);t.disabled=0}},25);});})();</script>""",
        "widget_css": "",
        "widget_js": ""
    },
    {
        "slug": "fintech-constructor",
        "title": "Финтех-конструктор",
        "desc": "Low-code конструктор финтех-продуктов: собирайте платёжные сценарии, rules-engine, workflow из готовых блоков.",
        "meta_desc": "Демо low-code конструктора финтех-продуктов: визуальный редактор сценариев, rules-engine, workflow. API-first архитектура.",
        "code": """// Создание платёжного сценария
const scenario = await constructor.createScenario({
  name: 'Пополнение+P2P-перевод',
  blocks: [
    { type: 'payment_method', params: { methods: ['card', 'sbp'] } },
    { type: 'commission', params: { percent: 0.5, min: 10 } },
    { type: 'split', params: { receivers: ['merchant', 'partner'] } },
    { type: 'notification', params: { channels: ['sms', 'push'] } }
  ]
});

// Деплой сценария
await constructor.deploy(scenario.id, 'production');

// Тестирование
const test = await constructor.testScenario(scenario.id, {
  amount: 1000,
  method: 'card'
});""",
        "features": ["Drag-and-drop редактор сценариев", "Rules-engine с версионированием", "API-first архитектура", "Песочница для тестирования", "Audit log всех изменений", "Готовые шаблоны"],
        "tags": ["React", "Node.js", "GraphQL", "Docker", "PostgreSQL"],
        "gradient": "#8B5CF6,#c4b5fd",
        "widget_html": """<div class="dw">
  <h3 class="dw-t">🧩 Pipeline сценария</h3>
  <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:16px">
    <div id="fc-s0" class="fc-step"><span class="fc-ic">💳</span><span class="fc-l">Приём платежа</span><span class="fc-st"></span></div>
    <div id="fc-s1" class="fc-step"><span class="fc-ic">💰</span><span class="fc-l">Расчёт комиссии</span><span class="fc-st"></span></div>
    <div id="fc-s2" class="fc-step"><span class="fc-ic">🔔</span><span class="fc-l">Уведомление</span><span class="fc-st"></span></div>
  </div>
  <div style="display:flex;gap:8px">
    <button class="dw-btn" id="fc-deploy">🚀 Deploy</button>
    <button class="dw-btn dw-btn-o" id="fc-reset">↺ Reset</button>
  </div>
  <div id="fc-info" style="display:none;margin-top:12px;padding:12px 14px;background:#00b89414;border:1px solid #00b89444;border-radius:10px;font-size:14px;font-weight:600;color:#00b894;text-align:center">✅ Сценарий выполнен успешно</div>
</div>
<style>.dw{margin:12px 0;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:16px;padding:24px}.dw-t{font-size:16px;font-weight:600;margin:0 0 16px;color:var(--clr-heading)}.dw-btn{padding:10px 20px;border:none;border-radius:10px;font-size:14px;font-weight:600;cursor:pointer;transition:opacity .2s;flex:1}.dw-btn:hover{opacity:.85}.dw-btn-o{background:transparent;border:1px solid var(--clr-border);color:var(--clr-text)}.fc-step{display:flex;align-items:center;gap:10px;padding:12px 14px;background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:10px;transition:all .4s}.fc-step.done{border-color:#00b894;background:#00b8940a}.fc-step.active{border-color:var(--clr-accent);box-shadow:0 0 0 2px var(--clr-accent)33}.fc-ic{font-size:20px;width:32px;text-align:center}.fc-l{flex:1;font-size:14px;font-weight:500;color:var(--clr-text)}.fc-st{width:20px;height:20px;border-radius:50%;flex-shrink:0;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center}.fc-step.active .fc-st{border:2px solid var(--clr-accent);border-top-color:transparent;animation:fcSpin .6s linear infinite;color:transparent}.fc-step.done .fc-st{border:none;background:none;color:#00b894}.fc-step.done .fc-st::after{content:'\\2713'}@keyframes fcSpin{to{transform:rotate(360deg)}}@media(min-width:768px){.dw{max-width:480px;margin-left:auto;margin-right:auto}}</style>
<script>(function(){var deploy=document.getElementById('fc-deploy'),reset=document.getElementById('fc-reset'),info=document.getElementById('fc-info'),steps=[document.getElementById('fc-s0'),document.getElementById('fc-s1'),document.getElementById('fc-s2')],running=false,timer;function r(){running=false;clearTimeout(timer);steps.forEach(function(s){s.className='fc-step';});info.style.display='none';deploy.disabled=false}reset.addEventListener('click',r);deploy.addEventListener('click',function(){if(running)return;r();running=true;deploy.disabled=true;var i=0;(function n(){if(i>=3){running=false;deploy.disabled=false;info.style.display='block';return}var s=steps[i];s.classList.add('active');timer=setTimeout(function(){s.classList.remove('active');s.classList.add('done');i++;n()},800);})();});})();</script>""",
        "widget_css": "",
        "widget_js": ""
    },
    {
        "slug": "project-portfolio",
        "title": "Портфель проектов",
        "desc": "Dashboard управления портфелем IT-проектов: сроки, ресурсы, бюджеты, риски. Иерархия: портфель → программа → проект.",
        "meta_desc": "Демо системы управления портфелем проектов: dashboard, Gantt, ресурсы, бюджеты, риски. PMO-инструмент для IT-компаний.",
        "code": """// Создание портфеля проектов
const portfolio = await pmo.createPortfolio({
  name: 'Финтех-направление 2024',
  budget: 50000000,
  strategicGoal: 'Рост доли финтех-продуктов'
});

// Добавление проекта
const project = await pmo.addProject({
  portfolioId: portfolio.id,
  name: 'Маркетплейс V2',
  type: 'product',
  startDate: '2024-09-01',
  endDate: '2025-03-01',
  budget: 15000000,
  resources: [
    { role: 'backend', count: 3 },
    { role: 'frontend', count: 2 }
  ]
});

// Оценка рисков
const risk = await pmo.assessRisk(project.id, {
  type: 'technical',
  probability: 0.3,
  impact: 'high',
  mitigation: 'Proof of Concept'
});""",
        "features": ["Иерархия: портфель → программа → проект", "Gantt-диаграммы и вехи", "Управление ресурсами", "Бюджетный контроль", "Риск-менеджмент", "Power BI-отчёты"],
        "tags": ["React", "Python", "PostgreSQL", "D3.js", "Docker"],
        "gradient": "#D4A574,#8b5e3c",
        "widget_html": """<div class="dw">
  <h3 class="dw-t">📊 Портфель проектов</h3>
  <div style="display:flex;flex-direction:column;gap:10px">
    <div class="pp-p" data-i="0"><div style="flex:1"><div style="font-size:14px;font-weight:500;color:var(--clr-text)">Маркетплейс V2</div><div style="font-size:12px;color:var(--clr-muted);margin-top:2px">Сен 2024 — Мар 2025</div></div><div class="pp-bar"><div class="pp-fill" style="width:70%;background:linear-gradient(90deg,#6c5ce7,#a29bfe)"></div><div class="pp-today"></div></div><div style="font-size:12px;color:var(--clr-muted);min-width:50px;text-align:right">70%</div></div>
    <div class="pp-p" data-i="1"><div style="flex:1"><div style="font-size:14px;font-weight:500;color:var(--clr-text)">Кредитный конвейер</div><div style="font-size:12px;color:var(--clr-muted);margin-top:2px">Янв 2025 — Июн 2025</div></div><div class="pp-bar"><div class="pp-fill" style="width:35%;background:linear-gradient(90deg,#00b894,#55efc4)"></div><div class="pp-today"></div></div><div style="font-size:12px;color:var(--clr-muted);min-width:50px;text-align:right">35%</div></div>
    <div class="pp-p" data-i="2"><div style="flex:1"><div style="font-size:14px;font-weight:500;color:var(--clr-text)">Mobile App</div><div style="font-size:12px;color:var(--clr-muted);margin-top:2px">Май 2025 — Авг 2025</div></div><div class="pp-bar"><div class="pp-fill" style="width:15%;background:linear-gradient(90deg,#fdcb6e,#f39c12)"></div><div class="pp-today"></div></div><div style="font-size:12px;color:var(--clr-muted);min-width:50px;text-align:right">15%</div></div>
  </div>
  <div id="pp-d" style="display:none;margin-top:12px;padding:14px;background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:10px;font-size:13px;color:var(--clr-text);animation:fcIn .3s ease"></div>
</div>
<style>.dw{margin:12px 0;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:16px;padding:24px}.dw-t{font-size:16px;font-weight:600;margin:0 0 16px;color:var(--clr-heading)}.pp-p{display:flex;align-items:center;gap:12px;padding:10px 14px;background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:10px;cursor:pointer;transition:all .2s}.pp-p:hover{border-color:var(--clr-accent)}.pp-bar{flex:2;height:28px;background:var(--clr-surface);border-radius:6px;position:relative;overflow:hidden}.pp-fill{height:100%;border-radius:6px;position:relative}.pp-today{position:absolute;top:0;bottom:0;width:2px;background:#e17055;left:50%;box-shadow:0 0 4px #e1705566}@keyframes fcIn{from{opacity:0;transform:translateY(-5px)}to{opacity:1;transform:translateY(0)}}@media(min-width:768px){.dw{max-width:640px;margin-left:auto;margin-right:auto}}</style>
<script>(function(){var details=[{n:'Маркетплейс V2',s:'Статус: Active\nБюджет: 15 млн ₽\nКоманда: 5 чел.\nРиски: низкие'},{n:'Кредитный конвейер',s:'Статус: Active\nБюджет: 8 млн ₽\nКоманда: 4 чел.\nРиски: средние'},{n:'Mobile App',s:'Статус: Planning\nБюджет: 6 млн ₽\nКоманда: 3 чел.\nРиски: высокие'}],dEl=document.getElementById('pp-d');document.querySelectorAll('.pp-p').forEach(function(p,i){p.addEventListener('click',function(){dEl.style.display='block';dEl.innerHTML='<strong>'+details[i].n+'</strong><br>'+details[i].s.replace(/\\n/g,'<br>')});});})();</script>""",
        "widget_css": "",
        "widget_js": ""
    },
    {
        "slug": "payment-page",
        "title": "Платёжная страница",
        "desc": "Кастомизируемая платёжная страница (Checkout Page) с мультиэквайрингом, скинами под бренд и умной маршрутизацией.",
        "meta_desc": "Демо платёжной страницы: кастомизируемый checkout, мультиэквайринг, скины, умная маршрутизация. Примеры кода встраивания.",
        "code": """// Встраивание платёжной страницы
&lt;iframe src="https://pay.axiiom.ru/checkout/{session_id}" 
        width="100%" height="600" frameborder="0"&gt;
&lt;/iframe&gt;

// Создание сессии checkout
const session = await checkout.createSession({
  merchantId: 'merchant_789',
  amount: 5499.00,
  currency: 'RUB',
  skin: 'dark_theme',
  methods: ['card', 'sbp', 'wallet'],
  successUrl: 'https://example.com/success',
  failUrl: 'https://example.com/fail'
});

// Умная маршрутизация
const route = await checkout.smartRoute({
  sessionId: session.id,
  amount: 5499.00,
  method: 'card',
  bin: '4276******1234'
});
// Выбирает оптимальный эквайринг""",
        "features": ["Кастомизация под бренд (скины)", "Умная маршрутизация платежей", "Мультиэквайринг на одной странице", "Invoice-ссылки", "Антифрод (3DS 2.0)", "Аналитика конверсий"],
        "tags": ["React", "Node.js", "PCI DSS", "3DS 2.0", "PostgreSQL"],
        "gradient": "#0984e3,#74b9ff",
        "widget_html": """<div class="pc-card">
  <div class="pc-head">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--clr-accent)" stroke-width="1.8"><rect x="1" y="4" width="22" height="16" rx="2"/><line x1="1" y1="10" x2="23" y2="10"/><line x1="6" y1="15" x2="10" y2="15"/></svg>
    <span>Checkout Page</span>
  </div>
  <div class="pc-body">
    <div class="pc-grid">
      <div class="pc-form">
        <div class="pc-fld">
          <label class="pc-lbl">Email</label>
          <input class="pc-inp" id="pp-email" value="user@example.com">
        </div>
        <div class="pc-fld">
          <label class="pc-lbl">Номер карты</label>
          <div class="pc-iw">
            <input class="pc-inp pc-mono" id="pp-card" placeholder="0000 0000 0000 0000" maxlength="19">
            <svg class="pc-ci" width="22" height="16" viewBox="0 0 24 16"><rect x="1" y="1" width="22" height="14" rx="2" stroke="var(--clr-faint)" stroke-width="1.2" fill="none"/><line x1="1" y1="6" x2="23" y2="6" stroke="var(--clr-faint)" stroke-width="1.2"/><circle cx="9" cy="10" r="2.5" stroke="var(--clr-accent)" stroke-width="1.2" fill="none" opacity=".5"/><circle cx="15" cy="10" r="2.5" stroke="var(--clr-accent)" stroke-width="1.2" fill="none" opacity=".5"/></svg>
          </div>
        </div>
        <div class="pc-fld">
          <label class="pc-lbl">Имя на карте</label>
          <input class="pc-inp pc-mono" id="pp-name" value="IVAN PETROV">
        </div>
        <button class="pc-btn" id="pp-btn">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          Оплатить 5 499 ₽
        </button>
      </div>
      <div class="pc-order">
        <div class="pc-order-hdr">Ваш заказ</div>
        <div class="pc-order-row"><span>Смартфон X Pro × 1</span><span>79 990 ₽</span></div>
        <div class="pc-order-row"><span>Страховка +1 год</span><span>3 990 ₽</span></div>
        <div class="pc-order-row"><span>Доставка</span><span class="pc-free">Бесплатно</span></div>
        <div class="pc-order-row pc-order-total"><span>Итого</span><span>83 980 ₽</span></div>
        <div class="pc-order-badge">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          Безопасная оплата
        </div>
      </div>
    </div>
    <div class="pc-3ds" id="pp-modal">
      <div class="pc-3ds-box">
        <div class="pc-3ds-icon">🔐</div>
        <div class="pc-3ds-t">3D Secure</div>
        <div class="pc-3ds-sub">Подтвердите оплату через ваш банк</div>
        <div class="pc-3ds-actions">
          <button class="pc-btn pc-btn-sm" id="pp-confirm">Подтвердить</button>
          <button class="pc-btn pc-btn-sm pc-btn-ghost" id="pp-cancel">Отмена</button>
        </div>
      </div>
    </div>
    <div class="pc-ok" id="pp-ok">
      <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#00b894" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="16 8 10 16 7 12"/></svg>
      <div class="pc-ok-t">Оплата подтверждена</div>
      <div class="pc-ok-sub">Спасибо! Ваш платёж прошёл успешно.</div>
    </div>
  </div>
</div>
<style>
.pc-card{margin:12px 0;background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:20px;overflow:hidden}
.pc-head{display:flex;align-items:center;gap:10px;padding:20px 24px 0;font-size:15px;font-weight:600;color:var(--clr-heading)}
.pc-body{padding:20px 24px 24px;display:flex;flex-direction:column;gap:0}
.pc-grid{display:flex;flex-direction:column;gap:18px}
.pc-order{margin-top:0}
.pc-form{display:flex;flex-direction:column;gap:14px}
.pc-fld{display:flex;flex-direction:column;gap:5px}
.pc-lbl{font-size:11px;color:var(--clr-faint);font-weight:500;letter-spacing:.4px;text-transform:uppercase}
.pc-iw{position:relative;display:flex;align-items:center}
.pc-inp{width:100%;padding:12px 14px;background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:12px;color:var(--clr-text);font-size:14px;box-sizing:border-box;transition:border-color .25s,box-shadow .25s}
.pc-inp:focus{outline:none;border-color:var(--clr-accent);box-shadow:0 0 0 3px color-mix(in srgb,var(--clr-accent) 18%,transparent)}
.pc-mono{font-family:'SF Mono','Fira Code',monospace;letter-spacing:.5px}
.pc-mono::placeholder{color:var(--clr-faint);opacity:.4;letter-spacing:0}
.pc-ci{position:absolute;right:12px;pointer-events:none;opacity:.6}
.pc-btn{display:flex;align-items:center;justify-content:center;gap:10px;padding:14px;background:var(--clr-accent);border:none;border-radius:14px;color:#fff;font-size:15px;font-weight:600;cursor:pointer;transition:opacity .25s,transform .15s;font-family:inherit;width:100%;margin-top:2px}
.pc-btn:hover{opacity:.9;transform:translateY(-1px)}
.pc-btn:active{transform:translateY(0)}
.pc-btn-sm{padding:12px 20px;width:auto;font-size:13px}
.pc-btn-ghost{background:var(--clr-bg);color:var(--clr-text);border:1px solid var(--clr-border)}
.pc-order{background:var(--clr-bg);border:1px solid var(--clr-border);border-radius:14px;padding:16px}
.pc-order-hdr{font-size:13px;font-weight:600;color:var(--clr-heading);margin-bottom:12px}
.pc-order-row{display:flex;justify-content:space-between;font-size:13px;color:var(--clr-text);padding:5px 0;border-bottom:1px solid var(--clr-border)}
.pc-order-row:last-of-type{border-bottom:none}
.pc-order-total{font-weight:700;color:var(--clr-heading);padding-top:8px!important;font-size:14px;border-top:1px solid var(--clr-border)!important;margin-top:4px}
.pc-free{color:#00b894;font-weight:500}
.pc-order-badge{display:flex;align-items:center;justify-content:center;gap:5px;font-size:10px;color:var(--clr-faint);opacity:.6;margin-top:12px;padding-top:8px;border-top:1px solid var(--clr-border)}
.pc-3ds{display:none;position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:99999;align-items:center;justify-content:center}
.pc-3ds-box{background:var(--clr-surface);border:1px solid var(--clr-border);border-radius:20px;padding:32px;text-align:center;max-width:340px;width:90%;animation:pcf .3s ease}
.pc-3ds-icon{font-size:36px;margin-bottom:12px}
.pc-3ds-t{font-size:16px;font-weight:600;color:var(--clr-heading);margin-bottom:6px}
.pc-3ds-sub{font-size:13px;color:var(--clr-muted);margin-bottom:18px}
.pc-3ds-actions{display:flex;gap:10px;justify-content:center}
.pc-ok{display:none;flex-direction:column;align-items:center;gap:6px;padding:20px 0 8px;text-align:center}
.pc-ok-t{color:#00b894;font-weight:600;font-size:16px;margin-top:4px}
.pc-ok-sub{color:var(--clr-faint);font-size:12px;opacity:.6}
@keyframes pcf{from{opacity:0;transform:scale(.95)}to{opacity:1;transform:scale(1)}}
@media (min-width:768px){.pc-card{max-width:520px;margin-left:auto;margin-right:auto}}
@media (max-width:640px){.pc-head{padding:16px 18px 0}.pc-body{padding:16px 18px 20px}.pc-order{padding:14px}}
</style>
<script>
(function(){
document.getElementById('pp-card').addEventListener('input',function(e){e.target.value=e.target.value.replace(/\D/g,'').replace(/(.{4})/g,'$1 ').trim();});
document.getElementById('pp-btn').addEventListener('click',function(){document.getElementById('pp-modal').style.display='flex';});
document.getElementById('pp-confirm').addEventListener('click',function(){document.getElementById('pp-modal').style.display='none';document.getElementById('pp-ok').style.display='flex';var b=document.getElementById('pp-btn');b.textContent='✓ Оплачено';b.disabled=1;b.style.cursor='default';b.style.transform='none'});
document.getElementById('pp-cancel').addEventListener('click',function(){document.getElementById('pp-modal').style.display='none';});
document.getElementById('pp-modal').addEventListener('click',function(e){if(e.target===this)this.style.display='none';});
})();</script>""",
        "widget_css": "",
        "widget_js": ""
    }
]

TEMPLATE = """<!doctype html>
<html lang="ru" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <meta name="theme-color" content="#0A0A0F">
  <title>{TITLE} — Демо-версия | AXIIOM</title>
  <meta name="description" content="{META_DESC}">
  <link rel="canonical" href="https://axiiom.ru/demo/app/{SLUG}/">

  <meta property="og:type" content="website">
  <meta property="og:url" content="https://axiiom.ru/demo/app/{SLUG}/">
  <meta property="og:title" content="{TITLE} — Демо | AXIIOM">
  <meta property="og:description" content="{META_DESC}">
  <meta property="og:image" content="https://axiiom.ru/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="ru_RU">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="https://axiiom.ru/demo/app/{SLUG}/">
  <meta name="twitter:title" content="{TITLE} — Демо | AXIIOM">
  <meta name="twitter:description" content="{META_DESC}">
  <meta name="twitter:image" content="https://axiiom.ru/og-image.png">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "{TITLE} — AXIIOM Demo",
    "description": "{META_DESC}",
    "url": "https://axiiom.ru/demo/app/{SLUG}/",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web",
    "author": {{
      "@type": "Organization",
      "name": "AXIIOM"
    }},
    "offers": {{
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "RUB"
    }}
  }}
  </script>

  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path fill='%23{COLOR}' d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z'/></svg>" type="image/svg+xml">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" as="style">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/styles.css">
  <link rel="stylesheet" href="/preloader.css">
  <style>
    .demo-page-hero {{
      min-height: 60vh; display: flex; align-items: center; justify-content: center;
      text-align: center; position: relative; overflow: hidden; padding-top: 100px;
      background: radial-gradient(ellipse 60% 40% at 30% 20%, rgba({R},{G},{B},.12), transparent),
                  radial-gradient(ellipse 50% 35% at 70% 80%, rgba({R},{G},{B},.05), transparent),
                  var(--clr-bg);
    }}
    .code-block {{
      background: rgba(255,255,255,.03); border: 1px solid var(--clr-border);
      border-radius: 16px; padding: 24px; overflow-x: auto; margin: 20px 0;
      font-family: 'SF Mono','Fira Code','Consolas',monospace; font-size: 13px; line-height: 1.7;
    }}
    .code-block code {{ white-space: pre; }}
    .feature-grid {{
      display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 16px; margin: 32px 0;
    }}
    .feature-item {{
      display: flex; align-items: center; gap: 12px; padding: 16px 20px;
      background: rgba(255,255,255,.02); border: 1px solid var(--clr-border);
      border-radius: 12px; font-size: 14px; color: var(--clr-text);
    }}
    .feature-item svg {{ flex-shrink: 0; width: 20px; height: 20px; }}
    .tag-list {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }}
    .tag-item {{
      display: inline-block; padding: 4px 14px; border: 1px solid var(--clr-border);
      border-radius: 20px; font-size: 12px; color: var(--clr-muted);
    }}
    .demo-nav-back {{
      position: fixed; top: 12px; left: 16px; z-index: 99999;
      display: inline-flex; align-items: center; gap: 6px;
      padding: 8px 16px; background: rgba(10,10,15,.9);
      color: #C7C7CC; border: 1px solid rgba(255,255,255,.08);
      border-radius: 20px; text-decoration: none;
      font-family: Inter,sans-serif; font-size: 13px; transition: all .2s;
    }}
    .demo-nav-back:hover {{ background: rgba(10,10,15,1); color: #F5F5F7; }}
    @media (max-width: 768px) {{
      .demo-page-hero {{ min-height: 50vh; padding-top: 80px; }}
      .feature-grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
<div id="preloader">
<script>(function(){{var p=document.getElementById('preloader');if(!p)return;if(sessionStorage.getItem('_seen')){{p.style.display='none';return}}sessionStorage.setItem('_seen','1');var t=Date.now();p._start=t;setTimeout(function(){{p.classList.add('_rdy')}},500);window.addEventListener('load',function(){{var e=Date.now()-t;if(e<2000){{setTimeout(function(){{p.classList.add('hidden');setTimeout(function(){{p.classList.add('hidden-done')}},500)}},2000-e)}}else{{p.classList.add('hidden');setTimeout(function(){{p.classList.add('hidden-done')}},500)}}}})}})()</script>
  <svg class="preloader-svg" viewBox="0 0 36 36" width="80" height="80">
    <rect class="pr1" x="2" y="2" width="14" height="14" rx="2"/>
    <rect class="pr2" x="20" y="2" width="14" height="14" rx="2"/>
    <rect class="pr3" x="2" y="20" width="14" height="14" rx="2"/>
    <rect class="pr4" x="20" y="20" width="14" height="14" rx="2"/>
    <circle class="pc" cx="27" cy="27" r="3"/>
  </svg>
</div>

<div class="noise"></div>
<div class="grid-overlay"></div>

<header class="header" id="header">
  <div class="container">
    <nav class="nav">
      <a href="/" class="logo">
        <svg width="30" height="30" viewBox="0 0 36 36" fill="none">
          <rect x="2" y="2" width="14" height="14" rx="2" stroke="currentColor" stroke-width="1.5" opacity=".4"/>
          <rect x="20" y="2" width="14" height="14" rx="2" stroke="currentColor" stroke-width="1.5" opacity=".4"/>
          <rect x="2" y="20" width="14" height="14" rx="2" stroke="currentColor" stroke-width="1.5" opacity=".4"/>
          <rect x="20" y="20" width="14" height="14" rx="2" stroke="currentColor" stroke-width="1.5"/>
          <circle cx="27" cy="27" r="3" fill="currentColor" opacity=".8"/>
        </svg>
        <span>AXIIOM</span>
      </a>
      <ul class="nav-links nav-links--desktop" id="desktopNav"></ul>
      <div class="nav-actions">
        <a href="/#contact" class="btn btn-nav">Обсудить проект</a>
        <button class="theme-btn" id="themeToggle" aria-label="Сменить тему">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg>
        </button>
        <button class="nav-toggle" id="navToggle" aria-label="Меню"><span></span><span></span><span></span></button>
      </div>
    </nav>
  </div>
</header>

<div class="nav-overlay" id="navOverlay"><ul class="nav-links" id="mobileNav"></ul></div>
<nav class="breadcrumbs" id="breadcrumbs" aria-label="Breadcrumb"><div class="container"></div></nav>

<a href="/demo/app/" class="demo-nav-back">← Все демо AXIIOM</a>

<section class="demo-page-hero">
  <div class="container">
    <div class="hero-content">
      <p class="badge">AXIIOM Demo</p>
      <h1>{TITLE}</h1>
      <p class="hero-desc">{DESC}</p>
      <div class="tag-list" style="justify-content:center;">
{TAGS}
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <p class="label">Интерактивное демо</p>
    <h2>Попробуйте прямо сейчас</h2>
    {DEMO_WIDGET}
  </div>
</section>

<section class="section">
  <div class="container">
    <p class="label">Пример кода</p>
    <h2>Интеграция за 5 минут</h2>
    <div class="code-block"><code>{CODE}</code></div>
  </div>
</section>

<section class="section dark">
  <div class="container">
    <p class="label">Возможности</p>
    <h2>Ключевые функции</h2>
    <div class="feature-grid">
{FEATURES}
    </div>
  </div>
</section>

<section class="section cta-section">
  <div class="container">
    <div class="glass-card" style="padding:48px 32px;text-align:center;border-radius:24px;">
      <h2 style="margin-bottom:16px;">Хотите такое решение?</h2>
      <p style="color:var(--clr-text);margin-bottom:24px;max-width:480px;margin-left:auto;margin-right:auto;">Обсудим ваш проект, покажем демо и рассчитаем стоимость.</p>
      <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;">
        <a href="mailto:{CONTACT_EMAIL}" class="btn">{CONTACT_EMAIL}</a>
        <a href="tel:{CONTACT_PHONE_LINK}" class="btn btn-outline">{CONTACT_PHONE}</a>
      </div>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="container">
    <div id="footerCopy"></div>
  </div>
</footer>

<script>
var header = document.getElementById('header');
window.addEventListener('scroll', function() {{
  header.classList.toggle('scrolled', window.scrollY > 40);
}}, {{ passive: true }});

var reveals = document.querySelectorAll('.reveal');
var ro = new IntersectionObserver(function(e) {{
  e.forEach(function(entry) {{
    if (entry.isIntersecting) entry.target.classList.add('visible');
  }});
}}, {{ threshold: 0.15 }});
reveals.forEach(function(r) {{ ro.observe(r); }});
</script>

<script src="/config.js"></script>
<script src="/nav.js"></script>
<script>Nav.init({{ cta: true, breadcrumbs: true }});</script>
<script src="/theme.js"></script>
<script src="/preloader.js"></script>

<script>
(function() {{
  var t = document.getElementById('navToggle');
  var o = document.getElementById('navOverlay');
  if (!t || !o) return;
  t.addEventListener('click', function(e) {{
    e.stopPropagation();
    o.classList.toggle('open');
    t.classList.toggle('active');
    document.body.style.overflow = o.classList.contains('open') ? 'hidden' : '';
  }});
}})();
</script>

<!-- Yandex.Metrika counter -->
<script type="text/javascript">(function(m,e,t,r,i,k,a){{m[i]=m[i]||function(){{(m[i].a=m[i].a||[]).push(arguments)}};m[i].l=1*new Date();for(var j=0;j<document.scripts.length;j++){{if(document.scripts[j].src===r){{return}}}}k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)}})(window,document,"script","https://mc.yandex.ru/metrika/tag.js?id={YM_ID}","ym");ym({YM_ID},"init",{{clickmap:true,trackLinks:true,accurateTrackBounce:true}});</script>
<noscript><div><img src="https://mc.yandex.ru/watch/{YM_ID}" style="position:absolute;left:-9999px" alt=""></div></noscript>
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{GA_ID}');</script>
</body>
</html>"""


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
            YM_ID=CONFIG["analytics"]["yandexMetrika"],
            GA_ID=CONFIG["analytics"]["googleAnalytics"],
        )

        dir_path = os.path.join(base, slug)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, "index.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✓ {slug}/index.html")

    print(f"\nВсего создано: {len(DEMOS)} страниц")


if __name__ == "__main__":
    main()

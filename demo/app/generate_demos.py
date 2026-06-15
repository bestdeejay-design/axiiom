#!/usr/bin/env python3
"""Generate 14 fintech demo pages with code examples and SEO metadata."""

import os
import re

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
        "gradient": "#6c5ce7,#a29bfe"
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
        "gradient": "#fd79a8,#e84393"
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
        "gradient": "#00b894,#55efc4"
    },
    {
        "slug": "marketplace",
        "title": "Маркетплейс",
        "desc": "Готовая платформа маркетплейса: каталог, корзина, оплата, доставка, отзывы и личный кабинет продавца.",
        "meta_desc": "Демо маркетплейс-платформы: каталог товаров, корзина, мультиэквайринг, доставка, личный кабинет продавца. Full-stack решение.",
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
        "gradient": "#fdcb6e,#f39c12"
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
        "gradient": "#e17055,#fab1a0"
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
        "gradient": "#74b9ff,#0984e3"
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
        "gradient": "#2d3436,#636e72"
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
        "gradient": "#a29bfe,#6c5ce7"
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
        "gradient": "#55efc4,#00b894"
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
        "gradient": "#e84393,#fd79a8"
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
        "gradient": "#8B5CF6,#c4b5fd"
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
        "gradient": "#D4A574,#8b5e3c"
    },
    {
        "slug": "payment-page",
        "title": "Платёжная страница",
        "desc": "Кастомизируемая платёжная страница (Checkout Page) с мультиэквайрингом, скинами под бренд и умной маршрутизацией.",
        "meta_desc": "Демо платёжной страницы: кастомизируемый checkout, мультиэквайринг, скины, умная маршрутизация. Примеры кода встраивания.",
        "code": """// Встраивание платёжной страницы
<iframe src="https://pay.axiiom.ru/checkout/{session_id}" 
        width="100%" height="600" frameborder="0">
</iframe>

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
        "gradient": "#0984e3,#74b9ff"
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
        <a href="mailto:hello@axiiom.ru" class="btn">hello@axiiom.ru</a>
        <a href="tel:+78129287478" class="btn btn-outline">+7 (812) 928-74-78</a>
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
<script type="text/javascript">(function(m,e,t,r,i,k,a){{m[i]=m[i]||function(){{(m[i].a=m[i].a||[]).push(arguments)}};m[i].l=1*new Date();for(var j=0;j<document.scripts.length;j++){{if(document.scripts[j].src===r){{return}}}}k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)}})(window,document,"script","https://mc.yandex.ru/metrika/tag.js?id=109391253","ym");ym(109391253,"init",{{clickmap:true,trackLinks:true,accurateTrackBounce:true}});</script>
<noscript><div><img src="https://mc.yandex.ru/watch/109391253" style="position:absolute;left:-9999px" alt=""></div></noscript>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-HFS4BDGTV4"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-HFS4BDGTV4');</script>
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
            COLOR=color,
            R=r, G=g, B=b
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

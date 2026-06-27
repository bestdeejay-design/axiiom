#!/usr/bin/env python3
from string import Template
import os

base_html = Template('''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#0A0A0F">
<title>${title} — AXIIOM</title>
<meta name="description" content="${desc}">
<link rel="canonical" href="https://axiiom.ru/industries/${slug}.html">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" as="style">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<meta property="og:type" content="website">
<meta property="og:url" content="https://axiiom.ru/industries/${slug}.html">
<meta property="og:title" content="${title} — AXIIOM">
<meta property="og:description" content="${desc}">
<meta property="og:image" content="https://axiiom.ru/og-image.png">
<meta property="og:locale" content="ru_RU">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:url" content="https://axiiom.ru/industries/${slug}.html">
<meta name="twitter:title" content="${title} — AXIIOM">
<meta name="twitter:description" content="${desc}">
<meta name="twitter:image" content="https://axiiom.ru/og-image.png">
<link rel="stylesheet" href="/styles.css">
<style>.breadcrumbs{padding:16px 0 0;border-bottom:1px solid var(--clr-border);background:var(--clr-bg)}.breadcrumbs ol{list-style:none;display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:0;margin:0}.breadcrumbs li{font-size:.8125rem;color:var(--clr-faint)}.breadcrumbs li+li:before{content:"›";margin-right:8px;color:var(--clr-faint);opacity:.5}.breadcrumbs a{color:var(--clr-accent);text-decoration:none}.breadcrumbs a:hover{text-decoration:underline}}</style>
</head>
<body>
<div class="noise"></div><div class="grid-overlay"></div>
<header class="header" id="header">
<div class="container">
<nav class="nav">
<a href="/" class="logo"><svg width="30" height="30" viewBox="0 0 36 36" fill="none"><rect x="2" y="2" width="14" height="14" rx="2" stroke="currentColor" stroke-width="1.5" opacity=".4"/><rect x="20" y="2" width="14" height="14" rx="2" stroke="currentColor" stroke-width="1.5" opacity=".4"/><rect x="2" y="20" width="14" height="14" rx="2" stroke="currentColor" stroke-width="1.5" opacity=".4"/><rect x="20" y="20" width="14" height="14" rx="2" stroke="currentColor" stroke-width="1.5"/><circle cx="27" cy="27" r="3" fill="currentColor" opacity=".8"/></svg><span>AXIIOM</span></a>
<ul class="nav-links nav-links--desktop industries-nav-links" id="industriesNav"></ul>
<div class="nav-actions">
<button class="theme-btn" id="themeToggle" aria-label="Сменить тему"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg></button>
<button class="nav-toggle industries-nav-toggle" id="navToggle" aria-label="Меню"><span></span><span></span><span></span></button>
</div>
</nav></div></header>
<nav class="breadcrumbs" aria-label="Breadcrumb">
<div class="container">
<ol itemscope itemtype="https://schema.org/BreadcrumbList">
<li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"><a itemprop="item" href="/"><span itemprop="name">Главная</span></a><meta itemprop="position" content="1"></li>
<li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"><a itemprop="item" href="/industries/"><span itemprop="name">Отраслевые решения</span></a><meta itemprop="position" content="2"></li>
<li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"><span itemprop="name">${title}</span><meta itemprop="position" content="3"></li>
</ol></div></nav>
<div class="nav-overlay" id="navOverlay"><ul class="nav-links" id="industriesNavMobile"></ul></div>
<section class="hero industries-hero">
<div class="container"><div class="hero-content">
<div class="hero-bg-svg"><svg width="800" height="600" viewBox="0 0 800 600" fill="none"><circle cx="400" cy="300" r="280" stroke="rgba(255,255,255,0.03)" stroke-width="1"/><circle cx="400" cy="300" r="200" stroke="rgba(255,255,255,0.04)" stroke-width="1"/><circle cx="400" cy="300" r="120" stroke="rgba(255,255,255,0.06)" stroke-width="1"/><line x1="50" y1="300" x2="750" y2="300" stroke="rgba(255,255,255,0.03)" stroke-width="1"/><line x1="400" y1="20" x2="400" y2="580" stroke="rgba(255,255,255,0.03)" stroke-width="1"/><path d="M200 300 L400 100 L600 300 L400 500 Z" stroke="rgba(255,255,255,0.04)" stroke-width="1" fill="none"/><circle cx="400" cy="300" r="4" fill="rgba(255,255,255,0.1)"/></svg></div>
<div class="badge-row"><p class="badge">Отраслевые решения</p></div>
<h1>${h1}</h1>
<p class="hero-desc">${hero}</p></div></div></section>
<section class="section"><div class="container"><h2>Решения</h2><p class="content-wrapper">${desc}</p><div style="text-align:center;margin-top:40px"><a href="/industries/" class="btn btn-outline">Все отрасли</a></div></div></section>
<footer class="footer"><div class="container"><div id="footerCopy"></div></div></footer>
<script>const header=document.getElementById("header");window.addEventListener("scroll",()=>{ header.classList.toggle("scrolled",window.scrollY>40); },{passive:true});</script>
<script src="/industries/nav.js"></script>
<script>initIndustriesNav("${slug}.html");</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-HFS4BDGTV4"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag("js",new Date());gtag("config","G-HFS4BDGTV4");</script>
<script src="/theme.js"></script>
<script src="/footer.js"></script>
</body>
</html>''')

with open('industries/industries.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        parts = line.split('|')
        if len(parts) < 4: continue
        slug = parts[0]
        title = parts[1]
        desc = parts[2]
        h1 = title
        hero = parts[3] if len(parts) > 3 else title
        html = base_html.substitute(slug=slug, title=title, desc=desc, h1=h1, hero=hero)
        with open(f'industries/{slug}.html', 'w', encoding='utf-8') as fw:
            fw.write(html)
print('Pages generated')
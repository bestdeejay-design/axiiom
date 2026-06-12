# SPA Demo Template

Vanilla JS SPA with mobile app shell and SVG icons (MDI-style).

## Features

- Dark/light theme toggle with persistence
- Landing page with animated hero
- Student/graduate mode toggle
- Mobile app shell with phone frame, bottom nav, back navigation
- SVG icon system (30+ icons defined inline)
- State persistence via localStorage (theme, user mode, last page)

## How to Use

1. **Edit data** — Replace the demo data in `js/app.js` (the `appData` object) with your own content. The render functions read from this single data object.

2. **Add/remove SVG icons** — Icons are defined as `<symbol>` elements in `index.html`. Reference them with `<use href="#icon-name"/>`. Browse [Material Design Icons](https://pictogrammers.com/library/mdi/) for additional icons — copy the `<path>` into a new `<symbol>`.

3. **Customize styles** — Edit `css/app.css` to change colors, spacing, or layout. CSS variables are used for theming.

4. **Demo data file** — `demo-data/template-data.js` contains a minimal standalone data object for reference. Not loaded at runtime; copy relevant parts into `js/app.js`.

## File Structure

```
index.html          — Entry point with SVG icon library and page shell
js/app.js           — Data model, render functions, navigation, theme logic
js/main.js          — Landing page GSAP animations (optional dependency)
css/app.css         — App shell styles, theme variables, component CSS
css/main.css        — Landing page styles
demo-data/          — Reference data (not loaded at runtime)
images/             — Image assets placeholder
```

## Browser Support

Modern browsers (ES6+). No build step required — open `index.html` directly or serve with any static file server.

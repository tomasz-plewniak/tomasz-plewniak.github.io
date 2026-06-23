# tomasz-plewniak.github.io

Personal portfolio website for Tomasz Plewniak — Lead Software Engineer
specializing in .NET, C#, and Azure.

## Tech Stack
- Vanilla HTML/CSS/JS (no frameworks, no build step)
- Google Fonts (Plus Jakarta Sans, JetBrains Mono)
- Google Analytics (gtag.js)

## Features
- Responsive single-page layout with mobile hamburger navigation
- Scroll-reveal animations with no-JS fallback
- Print stylesheet for PDF export
- Skip-to-content link for keyboard navigation
- SEO: Open Graph tags, Twitter Cards, JSON-LD structured data, sitemap, robots.txt
- Optimized font loading (preload + noscript fallback)
- Compressed OG image (28KB)

## Local Development
Open `index.html` in a browser. No build step required.

## Structure
- `index.html` — Single-page portfolio (hero, skills, experience, education, languages)
- `style.css` — All styling (dark theme, responsive, print, accessibility)
- `og-image.png` — Open Graph social share image (1200x630, 28KB)
- `og-image.svg` — SVG source for the OG image
- `sitemap.xml` / `robots.txt` — SEO files

## Deployment
Automatically deployed via GitHub Pages from the `main` branch.

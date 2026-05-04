# Bhardwaj &amp; Sons — house site

Static single-page brand site. One HTML file, custom CSS, no framework, no build step.

## Files

| File | Purpose |
|---|---|
| `index.html` | The site itself — single-page scroll, 5 sections |
| `favicon.svg` | Inline SVG favicon (italic B, saffron mark) |
| `og-image.png` | 1200×630 social preview, Hermès-aesthetic |
| `_build_og.py` | Regenerate the OG image after editing copy |
| `robots.txt` | Allow all crawlers; point to sitemap |
| `sitemap.xml` | Single-URL sitemap for SEO |
| `vercel.json` | Vercel security headers + clean URLs |
| `DEPLOY.md` | Step-by-step Vercel deployment guide |

## Local preview

```bash
cd ~/Desktop/bhardwaj_site
open index.html
```

Or for a proper local server:

```bash
python3 -m http.server 8080
# then visit http://localhost:8080
```

## Architecture decisions

- **No framework** — pure HTML + CSS. Loads in <200ms anywhere in the world. Easy to maintain. Easy to inspect for security. No JavaScript supply-chain risk.
- **No build step** — what you see in `index.html` is what ships. No bundler magic.
- **System fonts only** — Garamond / Helvetica / Devanagari fonts that already exist on the user's machine. No web-font requests. Zero external dependencies.
- **Premium serif typography** — Garamond stack with italic accent for the headline word. Helvetica Neue for eyebrows and meta. Devanagari for the epigraph.
- **Earthy, restrained palette** — warm ivory paper, deep saffron accent, gold ornament. No bright colours. No gradients.
- **Generous whitespace** — sections are 8rem tall with 60rem max width. Designed for breath, not density.

## Updating copy

All copy lives in `index.html`. Find the section by its `<section id="...">` anchor, edit the prose, save, refresh the browser.

After changing the headline or tagline, regenerate the OG image:

```bash
python3 _build_og.py
```

## Style edits

The full design system is in CSS variables at the top of `<style>` in `index.html`:

```css
--paper:#f3eee5;        /* warm ivory background */
--paper-deep:#ebe4d6;   /* slightly deeper sections */
--ink:#1c1611;          /* near-black with warmth */
--ink-soft:#3d342a;
--ink-faint:#7a6f63;
--rule:#cbbfa8;
--accent:#9c4a1a;       /* deep saffron */
--accent-deep:#5e2a0e;
--gold:#9d8147;         /* secondary ornament */
```

Change one variable, the whole site re-themes consistently.

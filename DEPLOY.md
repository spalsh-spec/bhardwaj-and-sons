# Deploy guide — Bhardwaj &amp; Sons (Vercel)

Total time: ~25 min once you have your domain. The site itself is one HTML file plus assets — there's nothing to build.

---

## 1. Register the domain (5 min, ~$20/year)

You don't have a domain yet. Pick one. Recommended order of preference:

1. **bhardwajandsons.com** — first choice, the brand
2. **bhardwajandsons.org** — fits the "trust" framing if .com is taken
3. **bhardwaj.house** — premium, expensive (~$70/yr), brand-tier
4. **bhardwajco.com** — fallback

Register at **Cloudflare Registrar** (cloudflare.com/products/registrar) — they sell at cost, no markup, no upsells, no privacy fee. Cheapest and most ethical.

Backup: **Namecheap** (~$15/yr first year, ~$20/yr after).

---

## 2. Push the site to a GitHub repo (5 min)

```bash
cd ~/Desktop/bhardwaj_site
git init -q
git add .
git -c user.email=sparshsharma219@gmail.com -c user.name="Sparsh Sharma" \
    commit -q -m "feat: initial Bhardwaj & Sons house site"
git branch -M main

# Create the GitHub repo (private — this is the brand house)
gh repo create bhardwaj-and-sons --private --source=. --remote=origin --push \
  --description "Bhardwaj & Sons — house of standards. https://bhardwajandsons.com"
```

---

## 3. Connect to Vercel (5 min, free for hobby tier)

1. Go to **vercel.com**, sign in with GitHub (use the spalsh-spec account)
2. Click **"Add New" → "Project"**
3. Select the **bhardwaj-and-sons** repo from the list
4. Framework Preset: **Other** (it's static HTML, no framework)
5. Root Directory: **./** (leave default)
6. Build Command: **leave blank**
7. Output Directory: **./** (leave default)
8. Click **Deploy**

In ~30 seconds Vercel gives you a URL like `bhardwaj-and-sons-xyz.vercel.app`. Click it — the site is live.

---

## 4. Connect your domain (10 min)

Once the Vercel deploy is green:

1. In Vercel project → **Settings → Domains**
2. Type `bhardwajandsons.com` and click **Add**
3. Vercel shows you DNS records to add (typically: an A record `76.76.21.21` and a CNAME `cname.vercel-dns.com`)
4. Go to your registrar (Cloudflare) → DNS settings for `bhardwajandsons.com`
5. Add the records Vercel told you about. **Set Cloudflare's proxy mode to "DNS only" (grey cloud)** for these records — Vercel handles SSL itself; Cloudflare proxying conflicts with that.
6. Wait 5-30 min for DNS propagation
7. Vercel auto-issues an SSL certificate via Let's Encrypt

The site is then live at **https://bhardwajandsons.com**.

---

## 5. Verify (2 min)

```bash
# Should all return 200
curl -sIL https://bhardwajandsons.com/ -o /dev/null -w "%{http_code}\n"
curl -sIL https://bhardwajandsons.com/og-image.png -o /dev/null -w "%{http_code}\n"
curl -sIL https://bhardwajandsons.com/favicon.svg -o /dev/null -w "%{http_code}\n"
curl -sIL https://bhardwajandsons.com/robots.txt -o /dev/null -w "%{http_code}\n"
```

Then paste your URL into the **Facebook OG debugger** (https://developers.facebook.com/tools/debug/) to confirm the share preview renders correctly with the og-image.png. LinkedIn caches aggressively; if the share preview is wrong, re-debug after editing.

---

## What you have at end of step 5

- A live domain you own, controlled by you
- A 12-second-load static site at that domain
- Auto-SSL via Vercel
- Auto-deploy on every git push to the bhardwaj-and-sons repo
- A clean OG share preview when anyone shares the URL

Total cost: $20-25/year for the domain. Vercel hosting at this scale is free indefinitely.

---

## Updating the site

```bash
cd ~/Desktop/bhardwaj_site
# edit index.html or any other file
git add . && git -c user.email=sparshsharma219@gmail.com -c user.name="Sparsh Sharma" commit -m "feat: ..." && git push
# Vercel auto-deploys. Site updates in ~30 seconds.
```

---

## Two configuration notes I'd recommend within the first month

**(a) Add a Cloudflare Web Analytics tag** — free, privacy-respecting, no cookie banner needed. Lets you see who is visiting from where. Insert one line of JS in `index.html` `<head>` after Cloudflare gives you the snippet.

**(b) Add a Plausible or Fathom analytics alternative** if you want more depth than Cloudflare provides. ~$9/month, also no-cookie. Skip Google Analytics — it's overkill for a brand page and signals "I optimise for clicks" rather than "I optimise for craft."

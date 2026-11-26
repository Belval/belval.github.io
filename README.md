# Tales from the Latent Space

Edouard Belval's personal engineering blog. Markdown posts live in `posts/`;
`scripts/build.py` builds a static site with no client-side framework or external
font service. GitHub Actions publishes `_site/` to GitHub Pages on `master`.

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8080 --directory _site
```

Add a Markdown post with YAML front matter: `title`, `date`, `slug`, `excerpt`,
and `hero` (an absolute `/assets/...` path). Use a unique lowercase slug.
Site metadata is in `site.json`. Assets are local and copied to `_site/assets`.

The visual identity borrows Floft's cream/olive/sage palette and serif/sans
hierarchy. Reusable design tokens, diagrams and the renderer live in
[Belval/skills](https://github.com/Belval/skills/tree/main/diagram-making).
The camera experiment's raw benchmarks and plot generator live in
[Belval/onvif-mcp](https://github.com/Belval/onvif-mcp/tree/main/docs/blog).

The old articles and Jekyll theme were retired in November 2026 and remain
recoverable in Git history.

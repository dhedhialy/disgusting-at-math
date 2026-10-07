# Disgusting at Math

A static self-study site: AP Precalculus through undergraduate math, with a parallel physics track. Black page, white type, KaTeX, no build step.

Open `index.html` to see the ladder. Start at [AP Precalculus](topics/ap-precalc.html). The rules are on [method.html](method.html).

## GitHub Pages

1. Push this repository to GitHub.
2. Settings → Pages → Build and deployment → Source: **Deploy from a branch**.
3. Branch: `main` (or `master`), folder: **`/ (root)`**.
4. Save. The site will be at `https://<user>.github.io/<repo>/`.

There is no build. Pages serves the HTML as it is. `.nojekyll` is here so Jekyll does not touch the files.

## On your machine

Progress stays in this browser. Checklist boxes and each attack’s written work are stored together. An attack is counted only when Check says both the work and the answer pass. Editing either line clears that count until you check again. The official solution stays locked for 20 minutes and is separate from your writeup.

The live site is [https://dhedhialy.github.io/disgusting-at-math/](https://dhedhialy.github.io/disgusting-at-math/).

```bash
python3 -m http.server
```

Then open `http://localhost:8000/`.

Opening the files directly (`file://`) works for reading. Chrome keeps a separate storage jar per file, so a box ticked on one page may not show on the next. Use the server above, or export and import JSON from the progress page.

#!/usr/bin/env python3
"""Write the static site. The HTML in the repo root is what GitHub Pages serves."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
import sys
sys.path.insert(0, str(Path(__file__).parent))
import json

from content import TOPICS
from grades import GRADES  # noqa: E402

STAGES = [
    ("contact", "First contact"),
    ("text", "Main text"),
    ("hard", "Hard problems"),
    ("ceiling", "Ceiling"),
    ("gate", "Mastery gate"),
    ("oral", "Oral pass"),
]


def prefix(depth):
    return "../" * depth


def nav(depth, current):
    p = prefix(depth)
    items = [
        ("index.html", "Map", "map"),
        ("method.html", "Method", "method"),
        ("resources.html", "Resources", "resources"),
        ("progress.html", "Progress", "progress"),
    ]
    links = []
    for href, label, key in items:
        cur = ' aria-current="page"' if key == current else ""
        links.append(f'<a href="{p}{href}"{cur}>{label}</a>')
    return (
        '<nav class="site-nav"><a class="brand" href="'
        + p
        + 'index.html">Disgusting at Math</a>'
        + "".join(links)
        + "</nav>"
    )


def shell(title, body, depth=0, current=""):
    p = prefix(depth)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<link rel="stylesheet" href="{p}css/site.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/contrib/auto-render.min.js"></script>
<script defer src="{p}js/curriculum.js"></script>
<script defer src="{p}js/grades.js"></script>
<script defer src="{p}js/site.js"></script>
<script>
document.addEventListener("DOMContentLoaded", function () {{
  if (window.renderMathInElement) {{
    renderMathInElement(document.body, {{
      delimiters: [
        {{left: "\\\\[", right: "\\\\]", display: true}},
        {{left: "\\\\(", right: "\\\\)", display: false}}
      ],
      throwOnError: false
    }});
  }}
}});
</script>
</head>
<body>
<div class="wrap">
{nav(depth, current)}
{body}
<footer class="colophon">Black page, white type. Progress stays in this browser. No account, no analytics.</footer>
</div>
</body>
</html>
"""


def pager(prev_t, next_t, depth):
    p = prefix(depth)
    left = f'<a href="{p}topics/{prev_t["slug"]}.html">← {escape(prev_t["title"])}</a>' if prev_t else "<span></span>"
    right = f'<a href="{p}topics/{next_t["slug"]}.html">{escape(next_t["title"])} →</a>' if next_t else "<span></span>"
    return f'<div class="pager">{left}{right}</div>'


def resource_block(r):
    paid = ' <span class="paid">PAID</span>' if r.get("paid") else ""
    return (
        f'<p class="resource"><a href="{r["url"]}">{escape(r["title"])}</a>{paid}'
        f'<br><span class="why">{r["why"]}</span></p>'
    )


def topic_page(topic, prev_t, next_t):
    slug = topic["slug"]
    toc = """
<nav class="toc" aria-label="On this page">
<p class="kicker">On this page</p>
<ol>
<li><a href="#attack">Problems first</a></li>
<li><a href="#prereqs">Prerequisites</a></li>
<li><a href="#what">What this actually is</a></li>
<li><a href="#core">Core results</a></li>
<li><a href="#ladder">The ladder</a></li>
<li><a href="#hardest">Hardest questions</a></li>
<li><a href="#gate">Mastery gate</a></li>
<li><a href="#diagrams">Diagrams</a></li>
<li><a href="#sets">Escalating sets</a></li>
<li><a href="#bank">Return bank</a></li>
<li><a href="#oral">Oral pass</a></li>
</ol>
</nav>
"""
    attacks = []
    for i, prob in enumerate(topic["attack"], 1):
        pid = f"{slug}-a{i}"
        attacks.append(f"""
<article class="attack">
<p class="kicker">Attack {i}</p>
{prob["q"]}
<form class="grade" data-grade="{pid}">
<label class="field">Your work
<textarea data-work rows="6" spellcheck="false"></textarea>
</label>
<label class="field">Your answer
<input data-answer type="text" autocomplete="off" spellcheck="false">
</label>
<p><button type="button" data-check="{pid}">Check work and answer</button></p>
<p class="verdict" data-verdict="{pid}"></p>
</form>
<p><button type="button" data-start="{pid}">Start 20-minute attempt</button></p>
<p class="timer" data-clock="{pid}">Timer not started. Twenty minutes of real work before a solution.</p>
<p><button type="button" data-solution="{pid}" disabled>Reveal solution</button></p>
<div class="hidden-block" id="sol-{pid}" hidden>{prob["a"]}</div>
</article>""")

    if topic["prereqs"]:
        pre = "<ul class=\"clean\">" + "".join(
            f'<li><a href="{p["slug"]}.html">{escape(p["title"])}</a></li>'
            for p in topic["prereqs"]
        ) + "</ul>"
    else:
        pre = "<p>None. This is the start.</p>"

    cores = []
    for i, c in enumerate(topic["core"], 1):
        pid = f"proof-{slug}-{i}"
        cores.append(f"""
<li>
<p><strong>{escape(c["name"])}.</strong> {c["statement"]}</p>
<p><button type="button" data-show-proof="{pid}">I wrote a proof. Reveal.</button></p>
<div class="hidden-block" id="{pid}" hidden>{c["proof"]}</div>
</li>""")

    tiers_html = []
    labels = [
        ("0", "Tier 0 / First contact", "Watch or read once. Do not study from this."),
        ("1", "Tier 1 / Main text", "The thing you work through."),
        ("2", "Tier 2 / Hard problems", "The problem book."),
        ("3", "Tier 3 / The ceiling", "The hardest questions that exist at this level."),
    ]
    for key, title, blurb in labels:
        items = topic["tiers"][key]
        body = "".join(resource_block(r) for r in items)
        tiers_html.append(f"<h3>{title}</h3><p class=\"tier-label\">{blurb}</p>{body}")

    hard = []
    for h in topic["hardest"]:
        hard.append(
            f'<li><a href="{h["url"]}">{escape(h["label"])}</a>'
            f'<br><span class="why">{h["why"]}</span></li>'
        )

    batches = []
    for i, batch in enumerate(topic["batches"], 1):
        lis = "".join(f"<li>{item}</li>" for item in batch["items"])
        batches.append(f"<h3>Set {i}. {escape(batch['name'])}</h3><ol>{lis}</ol>")

    bank = []
    for i, item in enumerate(topic["bank"], 1):
        bid = f"{slug}-b{i}"
        bank.append(
            f'<li class="bank-item" data-bank-id="{bid}" data-bank-label="{escape(item)}">'
            f'{item} <button type="button" data-log-review="{bid}">Log a writeup</button></li>'
        )

    checks = f"""
<ul class="checks">
<li><label><input type="checkbox" data-slug="{slug}" data-stage="contact"> Tier 0 done once, then closed.</label></li>
<li><label><input type="checkbox" data-slug="{slug}" data-stage="text"> Main text worked, exercises written.</label></li>
<li><label><input type="checkbox" data-slug="{slug}" data-stage="hard"> Hard-problem set written up.</label></li>
<li><label><input type="checkbox" data-slug="{slug}" data-stage="ceiling"> Ceiling problems attempted under the timer.</label></li>
<li><label><input type="checkbox" data-slug="{slug}" data-stage="gate"> Mastery gate passed.</label></li>
</ul>
"""

    body = f"""
<p class="kicker">{escape(topic["track"])} · {topic["n"]:02d}</p>
<h1>{escape(topic["title"])}</h1>
{pager(prev_t, next_t, 1)}
{toc}
<section id="attack">
<h2>Problems first</h2>
<p>Attempt these before you open a book or a video. Write the argument in the work box and the conclusion in the answer box. Check counts the problem only when both pass, and it does not open the solution. The solution stays locked for twenty minutes after you start the timer.</p>
{''.join(attacks)}
</section>
<section id="prereqs">
<h2>Prerequisites</h2>
{pre}
</section>
<section id="what">
<h2>What this actually is</h2>
{topic["what"]}
</section>
<section id="core">
<h2>Core results</h2>
<p>Statements only. Write the argument before you reveal it. A revealed proof you did not attempt is a paragraph you will not be able to rebuild at 2am.</p>
<ol class="spine">
{''.join(cores)}
</ol>
</section>
<section id="ladder">
<h2>The ladder</h2>
<p>Four rungs, in order. Do not skip a rung because the next one looks more serious.</p>
{''.join(tiers_html)}
{checks}
</section>
<section id="hardest">
<h2>Hardest questions</h2>
<p>Names and links. The problem text stays on the source site. Copyrighted contest problems are not copied here. What follows is where they are and why they hurt.</p>
<ol class="spine">
{''.join(hard)}
</ol>
</section>
<section id="gate">
<h2>Mastery gate</h2>
{topic["gate"]}
<p><label><input type="checkbox" data-slug="{slug}" data-stage="gate"> I passed this gate with written solutions.</label></p>
</section>
<section id="diagrams">
<h2>Diagrams</h2>
<figure class="diagram">
{topic["svg"]}
<figcaption>{topic["caption"]}</figcaption>
</figure>
</section>
<section id="sets">
<h2>Escalating sets</h2>
<p>Five sets. Finish a set before you touch the next. Full sentences, not a circled answer.</p>
{''.join(batches)}
</section>
<section id="bank">
<h2>Return bank</h2>
<p>Ten problems to meet again. Logging a writeup schedules them at 1 day, 7 days, and 30 days in this browser.</p>
<ul id="due-list" class="clean"></ul>
<ol>
{''.join(bank)}
</ol>
</section>
<section id="oral">
<h2>Oral pass</h2>
<p>{topic["oral"]}</p>
<p><label><input type="checkbox" data-slug="{slug}" data-stage="oral"> I explained this from a blank page, out loud, with no notes.</label></p>
</section>
{pager(prev_t, next_t, 1)}
"""
    return shell(topic["title"], body, depth=1, current="")


def index_page(topics):
    rows = []
    for t in topics:
        rows.append(
            f'<li><span class="meta">{t["n"]:02d}</span>'
            f'<span><a href="topics/{t["slug"]}.html">{escape(t["title"])}</a>'
            f'<div class="bar"><span data-topic-bar></span></div></span>'
            f'<span class="pct" data-topic-score="{t["slug"]}">0/6</span></li>'
        )
    # simple dependency graph
    nodes = []
    edges = []
    math = [t for t in topics if t["track"] == "Math"]
    phys = [t for t in topics if t["track"] == "Physics"]
    pos = {}
    for i, t in enumerate(math):
        x, y = 150, 36 + i * 36
        pos[t["slug"]] = (x, y)
        nodes.append(
            f'<a href="topics/{t["slug"]}.html"><text x="{x}" y="{y}" fill="#fff" font-size="13" font-family="Georgia, serif">{escape(t.get("short", t["title"]))}</text></a>'
        )
    for i, t in enumerate(phys):
        x, y = 560, 80 + i * 70
        pos[t["slug"]] = (x, y)
        nodes.append(
            f'<a href="topics/{t["slug"]}.html"><text x="{x}" y="{y}" fill="#fff" font-size="13" font-family="Georgia, serif">{escape(t.get("short", t["title"]))}</text></a>'
        )
    for t in topics:
        x2, y2 = pos[t["slug"]]
        for p in t["prereqs"]:
            x1, y1 = pos[p["slug"]]
            edges.append(
                f'<line x1="{x1+8}" y1="{y1+4}" x2="{x2-8}" y2="{y2-8}" stroke="rgba(255,255,255,0.35)" stroke-width="1"/>'
            )
    h = 36 + len(math) * 36 + 20
    svg = f'''<svg class="map-svg" viewBox="0 0 820 {h}" role="img" aria-label="Prerequisite graph">
<rect width="820" height="{h}" fill="#000"/>
{''.join(edges)}
{''.join(nodes)}
</svg>'''
    body = f"""
<p class="kicker">Curriculum</p>
<h1>Disgusting at math</h1>
<p class="lede">You are at AP Precalculus. The job is not to finish a class. The job is to be able to solve the hardest fair question on each rung, then climb.</p>
<p>Current gate: <strong data-here-label>AP Precalculus</strong></p>
<p class="stat" data-overall>0%</p>
<div class="bar"><span data-overall-bar></span></div>
<p class="meta">Share of checklist boxes across every topic. The map moves when you pass a mastery gate, not when you watch a video.</p>
<p>Attacks with the work and the answer both checked: <strong data-attack-score>0/0</strong></p>
<p id="file-warning" class="note" hidden>This file was opened from disk. Chrome keeps a separate storage jar for each file, so boxes ticked here may not show up on the next page. Serve the folder with <code>python3 -m http.server</code>, or use the export on the progress page. GitHub Pages does not have this problem.</p>
{svg}
<div class="columns">
<div>
<h2>Math</h2>
<ol class="ladder">{''.join(rows[:15])}</ol>
</div>
<div>
<h2>Physics, in parallel</h2>
<ol class="ladder">{''.join(rows[15:])}</ol>
<p class="meta">Physics waits on the math named on each page. It does not wait on topology.</p>
<p><a href="method.html">The rules</a> · <a href="topics/ap-precalc.html">Start today</a></p>
</div>
</div>
"""
    return shell("Disgusting at Math", body, 0, "map")


def method_page():
    body = """
<p class="kicker">Method</p>
<h1>How a circle actually works</h1>
<p>The Soviet <i>kruzhok</i> was a small weekly circle: a few students, a blackboard, a pile of problems, and a teacher who refused to perform the solution. Gelfand’s correspondence school, Kolmogorov’s circle, and the Moscow Center for Continuous Mathematical Education (MCCME) all ran on the same wager. You learn mathematics by being stuck in public, writing a complete argument, and coming back to the same hard problem after you have forgotten the trick.</p>
<p>This site is that wager with the furniture removed. Eight rules. Each one is enforced by the page, not by a pep talk.</p>
<h2>1. Problem before lecture</h2>
<p>Every topic opens with unworked attacks, above the books. You try them cold. Getting stuck is the point of the section. Then you read.</p>
<h2>2. Minimum struggle time</h2>
<p>A solution stays locked for 20 minutes after you start the attempt. The clock survives a reload. If you open it early in your head by hunting a forum, you have broken the rule the button could not see. Write for the whole twenty.</p>
<h2>3. Derive before you are told</h2>
<p>Core results show the statement and hide the proof. The button says “I wrote a proof” because that is the price of looking.</p>
<h2>4. Escalating numbered sets</h2>
<p>Five sets, rising. You do not jump to set 5 because set 2 felt slow. Nothing in a set is optional decoration.</p>
<h2>5. Full writeups, not answers</h2>
<p>The mastery gate asks for a written solution in mathematical prose: hypotheses, construction, estimate, conclusion. An answer key is a check you run after the writeup exists, never instead of it.</p>
<h2>6. Re-solve bank</h2>
<p>Each topic keeps ten problems. When you log a writeup, this browser asks for them again after 1 day, 7 days, and 30 days. A method you cannot redo next month was rented.</p>
<h2>7. Oral pass</h2>
<p>Blank page. No notes. Explain the topic out loud as if the person across the table is sharp and impatient. If you stall on a definition, you do not own it yet.</p>
<h2>8. Video is a preview</h2>
<p>Tier 0 is one resource, labeled watch-once or read-once. It is there to show you the shape of the subject. It is not the study. Close it.</p>
<h2>What I dropped from the community index</h2>
<p><a href="https://learn-anything.xyz/calculus">Learn Anything / calculus</a>, <a href="https://learn-anything.xyz/linear-algebra">linear algebra</a>, and <a href="https://learn-anything.xyz/topology">topology</a> are real pages. I read them. They are unsorted link piles: tensor calculus next to sequent calculus, blog posts next to textbooks. There is no page for precalculus; that slug returns “topic not found.” Where a community link was actually good, it is on the ladder with a reason. Where a free course with problem sets was better, that replaced it. A second public curriculum worth knowing is <a href="https://github.com/donkuri/learn-mathematics">donkuri/learn-mathematics</a>; it is one person’s path, used here as a cross-check, not as orders.</p>
<p><a href="topics/ap-precalc.html">Begin at AP Precalculus</a>.</p>
"""
    return shell("Method", body, 0, "method")


def resources_page(topics):
    rows = []
    options = ['<option value="all">All topics</option>']
    for t in topics:
        options.append(f'<option value="{t["slug"]}">{escape(t["title"])}</option>')
        for key, name in (("0", "Tier 0"), ("1", "Tier 1"), ("2", "Tier 2"), ("3", "Tier 3")):
            for r in t["tiers"][key]:
                paid = "PAID" if r.get("paid") else "free"
                rows.append(
                    f'<tr data-topic="{t["slug"]}" data-tier="{key}">'
                    f'<td>{escape(t["title"])}</td>'
                    f'<td>{name}</td>'
                    f'<td><a href="{r["url"]}">{escape(r["title"])}</a></td>'
                    f'<td>{paid}</td>'
                    f'<td>{r["why"]}</td></tr>'
                )
    body = f"""
<p class="kicker">Index</p>
<h1>Resources</h1>
<p>Every link below was fetched before this site shipped. Contest pages on the Art of Problem Solving wiki sit behind a browser check; they were opened in a browser and the problem pages exist. Paid books are marked. If a famous book has no link, I could not verify a live page, so it is named on the topic page with an ISBN and no URL.</p>
<div class="filters">
<label class="field">Topic<select id="filter-topic">{''.join(options)}</select></label>
<label class="field">Hardness<select id="filter-tier">
<option value="all">All tiers</option>
<option value="0">Tier 0</option>
<option value="1">Tier 1</option>
<option value="2">Tier 2</option>
<option value="3">Tier 3</option>
</select></label>
<label class="field">Search<input id="filter-q" type="search" placeholder="Axler, Irodov, Putnam"></label>
</div>
<table id="resource-table">
<thead><tr><th>Topic</th><th>Tier</th><th>Resource</th><th>Cost</th><th>Why this one</th></tr></thead>
<tbody>
{''.join(rows)}
</tbody>
</table>
"""
    return shell("Resources", body, 0, "resources")


def progress_page(topics):
    blocks = []
    for t in topics:
        boxes = []
        for sid, label in STAGES:
            boxes.append(
                f'<li><label><input type="checkbox" data-slug="{t["slug"]}" data-stage="{sid}"> {label}</label></li>'
            )
        blocks.append(
            f'<h2><a href="topics/{t["slug"]}.html">{escape(t["title"])}</a></h2><ul class="checks">{"".join(boxes)}</ul>'
        )
    body = f"""
<p class="kicker">Checklist</p>
<h1>Progress</h1>
<p class="stat" data-overall>0%</p>
<div class="bar"><span data-overall-bar></span></div>
<p>Boxes live in localStorage on this origin. Export if you switch browsers. Import replaces nothing else; it writes only keys from this site.</p>
<p>
<button type="button" id="export-progress">Export JSON</button>
<button type="button" id="import-progress">Import JSON</button>
<input id="import-file" type="file" accept="application/json" hidden>
</p>
<p id="file-warning" class="note" hidden>Opened via file://. Use a local server if the boxes do not follow you from page to page.</p>
<h2>Work and answers</h2>
<p>An attack is counted only when the written work and the answer both check. The text stays in this browser with the result.</p>
<p class="stat" data-attack-score>0/0</p>
<ul id="attack-log" class="clean"></ul>
{''.join(blocks)}
"""
    return shell("Progress", body, 0, "progress")


def write_grades():
    payload = []
    for g in GRADES:
        payload.append({
            "id": f"{g['slug']}-a{g['n']}",
            "slug": g["slug"],
            "n": g["n"],
            "parts": g["parts"],
            "need": g["need"],
        })
    text = "window.GRADES = " + json.dumps(payload, indent=2) + ";\n"
    (ROOT / "js" / "grades.js").write_text(text, encoding="utf-8")


def main():
    # resolve prereq objects
    by = {t["slug"]: t for t in TOPICS}
    for i, t in enumerate(TOPICS):
        t["n"] = i + 1
        t["prereqs"] = [by[s] for s in t["needs"]]
    write_grades()
    (ROOT / "index.html").write_text(index_page(TOPICS), encoding="utf-8")
    (ROOT / "method.html").write_text(method_page(), encoding="utf-8")
    (ROOT / "resources.html").write_text(resources_page(TOPICS), encoding="utf-8")
    (ROOT / "progress.html").write_text(progress_page(TOPICS), encoding="utf-8")
    out = ROOT / "topics"
    out.mkdir(exist_ok=True)
    for i, t in enumerate(TOPICS):
        prev_t = TOPICS[i - 1] if i else None
        next_t = TOPICS[i + 1] if i + 1 < len(TOPICS) else None
        (out / f"{t['slug']}.html").write_text(topic_page(t, prev_t, next_t), encoding="utf-8")
    print(f"wrote {len(TOPICS)} topics")


if __name__ == "__main__":
    main()

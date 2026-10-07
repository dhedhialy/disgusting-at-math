def R(title, url, why, paid=False):
    return {"title": title, "url": url, "why": why, "paid": paid}


def grid(w=640, h=360, step=40):
    lines = []
    for x in range(0, w + 1, step):
        lines.append(
            f'<line x1="{x}" y1="0" x2="{x}" y2="{h}" stroke="rgba(255,255,255,0.16)"/>'
        )
    for y in range(0, h + 1, step):
        lines.append(
            f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="rgba(255,255,255,0.16)"/>'
        )
    return "".join(lines)


def frame(inner, w=640, h=360, label=""):
    return (
        f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{label}">'
        f'<rect width="{w}" height="{h}" fill="#000"/>'
        + grid(w, h)
        + inner
        + "</svg>"
    )

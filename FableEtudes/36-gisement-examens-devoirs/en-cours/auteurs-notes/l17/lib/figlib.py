# figlib : constructeur de figures SVG « vraies » (coordonnées exactes -> pixels) dans le style des missions publiées.
# Convention : repère mathématique (y vers le haut) -> SVG (y vers le bas), échelle uniforme.
import math

INK = "#0f172a"
ACC = "#0f6e56"
MUTED = "#64748b"


def fnum(v):
    s = f"{v:.2f}"
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def _dist_pt_seg(p, a, b):
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    if L2 < 1e-12:
        return math.hypot(p[0] - ax, p[1] - ay)
    u = max(0.0, min(1.0, ((p[0] - ax) * dx + (p[1] - ay) * dy) / L2))
    return math.hypot(p[0] - (ax + u * dx), p[1] - (ay + u * dy))


def _unit(dx, dy):
    n = math.hypot(dx, dy)
    return (dx / n, dy / n) if n > 1e-12 else (0.0, 0.0)


class Fig:
    def __init__(self, pts, W=300, H=250, margin=30, fit=None, label_off=13.5):
        self.pts = {k: (float(v[0]), float(v[1])) for k, v in pts.items()}
        names = fit if fit is not None else list(self.pts.keys())
        xs = [self.pts[n][0] for n in names]
        ys = [self.pts[n][1] for n in names]
        minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
        dx = max(maxx - minx, 1e-9)
        dy = max(maxy - miny, 1e-9)
        self.s = min((W - 2 * margin) / dx, (H - 2 * margin) / dy)
        self.ox = (W - self.s * dx) / 2 - self.s * minx
        self.oy = (H - self.s * dy) / 2 + self.s * maxy
        self.W, self.H = W, H
        self.label_off = label_off
        self.fills, self.lines, self.marks, self.dots = [], [], [], []
        self.labels = []  # (name, color, forced_dir, text)
        self.inc = {}  # nom de point -> liste de directions (px) des segments incidents
        self.dot_px = []  # centres des points dessinés (px)
        self.edges = []  # segments dessinés (px) : ((x0,y0),(x1,y1))

    # ---- repère
    def P(self, p):
        x, y = self.pts[p] if isinstance(p, str) else (float(p[0]), float(p[1]))
        return (self.ox + self.s * x, self.oy - self.s * y)

    def _note_inc(self, name, other_px):
        if isinstance(name, str):
            px = self.P(name)
            self.inc.setdefault(name, []).append(_unit(other_px[0] - px[0], other_px[1] - px[1]))

    # ---- éléments
    def fill(self, names, color=ACC, opacity=0.1):
        pts = " ".join(f"{fnum(self.P(n)[0])},{fnum(self.P(n)[1])}" for n in names)
        self.fills.append(f'<polygon points="{pts}" fill="{color}" fill-opacity="{opacity}" stroke="none"/>')

    def seg(self, a, b, color=INK, width=2.2, dash=None, ext0=0.0, ext1=0.0):
        """segment [a b] ; ext0/ext1 : prolongement (fraction de la longueur) au-delà de a / de b."""
        pa, pb = self.P(a), self.P(b)
        d = (pb[0] - pa[0], pb[1] - pa[1])
        qa = (pa[0] - ext0 * d[0], pa[1] - ext0 * d[1])
        qb = (pb[0] + ext1 * d[0], pb[1] + ext1 * d[1])
        dd = f' stroke-dasharray="{dash}"' if dash else ""
        self.lines.append(
            f'<path d="M{fnum(qa[0])} {fnum(qa[1])} L{fnum(qb[0])} {fnum(qb[1])}" fill="none" stroke="{color}" '
            f'stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"{dd}/>'
        )
        self._note_inc(a, pb)
        self._note_inc(b, pa)
        self.edges.append((qa, qb))

    def poly(self, names, color=INK, width=2.2, closed=True):
        pts = " ".join(f"{fnum(self.P(n)[0])},{fnum(self.P(n)[1])}" for n in names)
        tag = "polygon" if closed else "polyline"
        self.lines.append(
            f'<{tag} points="{pts}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"/>'
        )
        n = len(names)
        for i in range(n if closed else n - 1):
            self.edges.append((self.P(names[i]), self.P(names[(i + 1) % n])))
        for i, nm in enumerate(names):
            if closed or 0 < i < n - 1:
                self._note_inc(nm, self.P(names[(i - 1) % n]))
                self._note_inc(nm, self.P(names[(i + 1) % n]))
            elif i == 0:
                self._note_inc(nm, self.P(names[1]))
            else:
                self._note_inc(nm, self.P(names[n - 2]))

    def circle(self, c, r, color=INK, width=2.2, dash=None):
        cx, cy = self.P(c)
        dd = f' stroke-dasharray="{dash}"' if dash else ""
        self.lines.append(f'<circle cx="{fnum(cx)}" cy="{fnum(cy)}" r="{fnum(r * self.s)}" fill="none" stroke="{color}" stroke-width="{width}"{dd}/>')

    def arc(self, c, r, a0, a1, color=INK, width=2.2, dash=None):
        """arc de cercle de centre c, rayon r (unités du monde), de l'angle a0 à a1 (degrés, sens trigonométrique)."""
        cx, cy = self.pts[c] if isinstance(c, str) else (float(c[0]), float(c[1]))
        p0 = self.P((cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))))
        p1 = self.P((cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))))
        large = 1 if ((a1 - a0) % 360) > 180 else 0
        dd = f' stroke-dasharray="{dash}"' if dash else ""
        rp = r * self.s
        self.lines.append(
            f'<path d="M{fnum(p0[0])} {fnum(p0[1])} A{fnum(rp)} {fnum(rp)} 0 {large} 0 {fnum(p1[0])} {fnum(p1[1])}" fill="none" '
            f'stroke="{color}" stroke-width="{width}" stroke-linecap="round"{dd}/>'
        )

    def right_angle(self, v, a, b, size=9):
        """marque d'angle droit en v entre les demi-droites vers a et vers b (vérifie que l'angle est droit dans le monde)."""
        wv = self.pts[v]
        wa = self.pts[a] if isinstance(a, str) else a
        wb = self.pts[b] if isinstance(b, str) else b
        dot = (wa[0] - wv[0]) * (wb[0] - wv[0]) + (wa[1] - wv[1]) * (wb[1] - wv[1])
        assert abs(dot) < 1e-6, f"angle non droit en {v}: {dot}"
        pv, pa, pb = self.P(v), self.P(a), self.P(b)
        u = _unit(pa[0] - pv[0], pa[1] - pv[1])
        w = _unit(pb[0] - pv[0], pb[1] - pv[1])
        p1 = (pv[0] + u[0] * size, pv[1] + u[1] * size)
        p3 = (pv[0] + w[0] * size, pv[1] + w[1] * size)
        p2 = (p1[0] + w[0] * size, p1[1] + w[1] * size)
        self.marks.append(
            f'<path d="M{fnum(p1[0])} {fnum(p1[1])} L{fnum(p2[0])} {fnum(p2[1])} L{fnum(p3[0])} {fnum(p3[1])}" fill="none" stroke="{INK}" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
        )

    def ticks(self, a, b, n=1, size=5.5, gap=3.4, t=0.5):
        pa, pb = self.P(a), self.P(b)
        m = (pa[0] + t * (pb[0] - pa[0]), pa[1] + t * (pb[1] - pa[1]))
        d = _unit(pb[0] - pa[0], pb[1] - pa[1])
        nrm = (-d[1], d[0])
        for k in range(n):
            off = (k - (n - 1) / 2) * gap
            c = (m[0] + d[0] * off, m[1] + d[1] * off)
            p0 = (c[0] - nrm[0] * size, c[1] - nrm[1] * size)
            p1 = (c[0] + nrm[0] * size, c[1] + nrm[1] * size)
            self.marks.append(f'<path d="M{fnum(p0[0])} {fnum(p0[1])} L{fnum(p1[0])} {fnum(p1[1])}" fill="none" stroke="{INK}" stroke-width="1.8" stroke-linecap="round"/>')

    def equal_ticks(self, pairs, n=1):
        """marque d'une même série de traits des segments de longueur égale (vérifie l'égalité dans le monde)."""
        ls = []
        for a, b in pairs:
            wa, wb = self.pts[a], self.pts[b]
            ls.append(math.hypot(wb[0] - wa[0], wb[1] - wa[1]))
        assert max(ls) - min(ls) < 1e-6, f"segments inégaux {pairs}: {ls}"
        for a, b in pairs:
            self.ticks(a, b, n)

    def dot(self, name, color=INK, r=None):
        r = r if r is not None else (4.4 if color == ACC else 3.8)
        px = self.P(name)
        self.dots.append(f'<circle cx="{fnum(px[0])}" cy="{fnum(px[1])}" r="{r}" fill="{color}"/>')
        self.dot_px.append(px)

    def label(self, name, color=INK, dir=None, text=None):
        """dir : angle en degrés (0 = à droite, 90 = en haut) pour forcer la position."""
        self.labels.append((name, color, dir, text if text is not None else name))

    # ---- rendu
    def _place_labels(self):
        placed = []  # centres des étiquettes déjà posées
        out = []
        for name, color, forced, text in self.labels:
            px = self.P(name)
            incs = list(self.inc.get(name, []))
            for (e0, e1) in self.edges:
                d0 = math.hypot(e0[0] - px[0], e0[1] - px[1])
                d1 = math.hypot(e1[0] - px[0], e1[1] - px[1])
                if d0 < 2 or d1 < 2:
                    continue
                if _dist_pt_seg(px, e0, e1) < 1.5:
                    incs.append(_unit(e0[0] - px[0], e0[1] - px[1]))
                    incs.append(_unit(e1[0] - px[0], e1[1] - px[1]))
            best, bestscore = None, -1e9
            cands = [forced] if forced is not None else list(range(0, 360, 15))
            for ang in cands:
                dx, dy = math.cos(math.radians(ang)), -math.sin(math.radians(ang))  # px: y vers le bas
                c = (px[0] + dx * self.label_off, px[1] + dy * self.label_off)
                score = 0.0
                if incs:
                    mina = min(math.degrees(math.acos(max(-1, min(1, dx * u[0] + dy * u[1])))) for u in incs)
                    score += min(mina, 100) * 1.0
                else:
                    score += 60
                for q in self.dot_px:
                    if abs(q[0] - px[0]) < 1e-6 and abs(q[1] - px[1]) < 1e-6:
                        continue
                    d = math.hypot(c[0] - q[0], c[1] - q[1])
                    if d < 14:
                        score -= (14 - d) * 6
                for q in placed:
                    d = math.hypot(c[0] - q[0], c[1] - q[1])
                    if d < 16:
                        score -= (16 - d) * 8
                for (e0, e1) in self.edges:
                    dd = _dist_pt_seg(c, e0, e1)
                    if dd < 9:
                        score -= (9 - dd) * 4
                if c[0] < 9 or c[0] > self.W - 9 or c[1] < 11 or c[1] > self.H - 7:
                    score -= 200
                # léger biais vers le haut et la droite (lisibilité)
                score += 0.01 * (dy * -1)
                if score > bestscore:
                    best, bestscore = (c, ang), score
            c, ang = best
            placed.append(c)
            out.append((c, color, text))
        return out

    def svg(self, title):
        parts = [f'<svg viewBox="0 0 {self.W} {self.H}"><title>{title}</title>']
        parts += self.fills + self.lines + self.marks + self.dots
        lab = self._place_labels()
        if lab:
            parts.append('<g font-weight="700" direction="ltr" unicode-bidi="isolate" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">')
            for (c, color, text) in lab:
                parts.append(f'<text x="{fnum(c[0])}" y="{fnum(c[1] + 5.2)}" text-anchor="middle" fill="{color}" font-size="15">{text}</text>')
            parts.append("</g>")
        parts.append("</svg>")
        return "".join(parts)

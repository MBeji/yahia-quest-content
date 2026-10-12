#!/usr/bin/env python3
"""Figures de la mission 2022 ex3 : structures du mébyse (dessin أ = follicule rompu + ovocyte ; ب = follicule mûr ; ج = corps jaune).
Refait d'après le Document 2 du PDF 2022 (C04, p.2). Chiffres/lettres seulement dans le dessin ; l'arabe n'est que dans <title>.
"""
import math, random, sys
sys.path.insert(0, '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/svt-l04-work')
from lib import f, svg, label

DARK = '#0f172a'
ORANGE = '#f97316'
RIM = '#a8929a'      # liseré gris-mauve extérieur
DOT = '#7c2d12'
YELLOW = '#facc15'
YELLOW_D = '#a16207'


def pt(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def dots_on_arc(cx, cy, r, a0, a1, n, seed):
    rnd = random.Random(seed)
    out = []
    for i in range(n):
        a = a0 + (a1 - a0) * (i + 0.5) / n + rnd.uniform(-3, 3)
        rr = r + rnd.uniform(-1.6, 1.6)
        x, y = pt(cx, cy, rr, a)
        out.append('<circle cx="%s" cy="%s" r="0.9" fill="%s"/>' % (f(x), f(y), DOT))
    return ''.join(out)


def oocyte(x, y, r=6.5):
    return ('<circle cx="%s" cy="%s" r="%s" fill="#ffffff" stroke="%s" stroke-width="2.4"/>'
            '<circle cx="%s" cy="%s" r="2.2" fill="%s"/>') % (f(x), f(y), f(r), DARK, f(x), f(y), DARK)


def ring_path(cx, cy, r, start, end):
    """arc de cercle de start à end (degrés, sens horaire en coordonnées SVG), grand arc"""
    x0, y0 = pt(cx, cy, r, start)
    x1, y1 = pt(cx, cy, r, end)
    sweep = (end - start) % 360
    large = 1 if sweep > 180 else 0
    return 'M%s %s A%s %s 0 %d 1 %s %s' % (f(x0), f(y0), f(r), f(r), large, f(x1), f(y1))


def follicle_ruptured(cx, cy, numbers=False):
    R = 29
    g = []
    # paroi : liseré gris-mauve à l'extérieur, paroi orange à l'intérieur, ouverte vers le haut
    d = ring_path(cx, cy, R, -62, -118)
    g.append('<path d="%s" fill="none" stroke="%s" stroke-width="10.5" stroke-linecap="round"/>' % (d, RIM))
    g.append('<path d="%s" fill="none" stroke="%s" stroke-width="8" stroke-linecap="round"/>' % (d, ORANGE))
    g.append(dots_on_arc(cx, cy, R, -52, 232, 26, 7))
    # fins traits pointillés qui jaillissent par l'ouverture
    for dx, k in ((-9, 0), (-3, 1), (4, 2), (10, 3)):
        g.append('<path d="M%s %s q %s %s %s %s" fill="none" stroke="%s" stroke-width="1" stroke-dasharray="2 2"/>' % (
            f(cx + dx * 0.7), f(cy - R + 3), f(-2 + k), f(-6), f(dx * 0.35), f(-14), DARK))
    # la cellule libérée, juste au-dessus de l'ouverture
    ox, oy = cx + 1, cy - R - 20
    g.append(oocyte(ox, oy))
    if numbers:
        # repère 1 : trait court vers la cellule (flèche), repère 2 : trait vers la paroi en bas à droite
        g.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.6"/>' % (f(ox + 24), f(oy), f(ox + 8.5), f(oy), DARK))
        g.append('<polygon points="%s,%s %s,%s %s,%s" fill="%s"/>' % (f(ox + 8), f(oy), f(ox + 14), f(oy - 3), f(ox + 14), f(oy + 3), DARK))
        g.append(label(ox + 31, oy + 4.5, '1', 13))
        ax, ay = pt(cx, cy, R + 4, 38)
        g.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.6"/>' % (f(ax + 17), f(ay + 8), f(ax + 1), f(ay + 1), DARK))
        g.append('<polygon points="%s,%s %s,%s %s,%s" fill="%s"/>' % (f(ax), f(ay), f(ax + 7.5), f(ay + 1.5), f(ax + 4), f(ay + 7), DARK))
        g.append(label(ax + 24, ay + 15, '2', 13))
    return ''.join(g)


def follicle_mature(cx, cy):
    R = 29
    g = []
    g.append('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-width="10.5"/>' % (f(cx), f(cy), f(R), RIM))
    g.append('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-width="8"/>' % (f(cx), f(cy), f(R), ORANGE))
    g.append(dots_on_arc(cx, cy, R, 0, 360, 30, 11))
    # saillie crochue de la paroi vers l'intérieur de la cavité (en haut à droite), porteuse de l'ovocyte
    g.append('<path d="M%s %s C%s %s %s %s %s %s C%s %s %s %s %s %s C%s %s %s %s %s %s Z" fill="%s" stroke="%s" stroke-width="1.6" stroke-linejoin="round"/>' % (
        f(cx + 12), f(cy - 25), f(cx + 8), f(cy - 20), f(cx + 1), f(cy - 14), f(cx - 2), f(cy - 8),
        f(cx - 5), f(cy - 3), f(cx + 4), f(cy + 1), f(cx + 9), f(cy - 5),
        f(cx + 14), f(cy - 11), f(cx + 20), f(cy - 16), f(cx + 23), f(cy - 21), ORANGE, RIM))
    g.append(oocyte(cx + 2, cy - 5, 6.2))
    return ''.join(g)


def corpus_luteum(cx, cy):
    pts = []
    n = 220
    for i in range(n):
        t = 2 * math.pi * i / n
        r = 29 + 3.1 * math.sin(11 * t + 0.6) + 1.2 * math.sin(5 * t)
        pts.append((cx + r * 1.25 * math.cos(t), cy + r * 0.88 * math.sin(t)))
    d = 'M' + ' L'.join('%s %s' % (f(x), f(y)) for x, y in pts) + ' Z'
    g = ['<path d="%s" fill="%s" stroke="%s" stroke-width="2" stroke-linejoin="round"/>' % (d, YELLOW, YELLOW_D)]
    # cavité centrale claire, irrégulière
    cav = []
    for i in range(16):
        t = 2 * math.pi * i / 16
        r = (11 if i % 2 == 0 else 7.5) + 1.2 * math.sin(3 * t)
        cav.append((cx + r * 1.25 * math.cos(t), cy + r * 0.8 * math.sin(t)))
    g.append('<polygon points="%s" fill="#fef9c3" stroke="%s" stroke-width="1.4" stroke-linejoin="round"/>' % (
        ' '.join('%s,%s' % (f(x), f(y)) for x, y in cav), '#eab308'))
    # fentes radiales du pourtour
    for k in range(11):
        t = 2 * math.pi * (k + 0.5) / 11 + 0.05
        r0, r1 = 17, 27.5
        g.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.2"/>' % (
            f(cx + r0 * 1.25 * math.cos(t)), f(cy + r0 * 0.88 * math.sin(t)),
            f(cx + r1 * 1.25 * math.cos(t)), f(cy + r1 * 0.88 * math.sin(t)), YELLOW_D))
    return ''.join(g)


def panel_frame(x, w, h):
    return '<rect x="%s" y="2" width="%s" height="%s" fill="none" stroke="#94a3b8" stroke-width="1"/>' % (f(x), f(w), f(h - 4))


def fig_three(numbers=True):
    """trois dessins côte à côte : أ à droite, ب au milieu, ج à gauche (disposition du sujet)."""
    W, H = 300, 148
    body = []
    pw = W / 3
    for i in range(3):
        body.append(panel_frame(i * pw + 1, pw - 2, H))
    # panneau de droite : أ
    body.append(follicle_ruptured(2 * pw + pw / 2 - 6, 78, numbers=numbers))
    body.append(follicle_mature(pw + pw / 2, 70))
    body.append(corpus_luteum(pw / 2, 70))
    # légendes de bas de panneau : lettres du sujet
    body.append(label(2 * pw + pw / 2, 140, 'أ', 13))
    body.append(label(pw + pw / 2, 140, 'ب', 13))
    body.append(label(pw / 2, 140, 'ج', 13))
    if numbers:
        body.append(label(pw + pw / 2, 116, '3', 13))
        body.append(label(pw / 2, 116, '4', 13))
    t = ('ثلاثة رسوم لبنيات يمكن مشاهدتها في مبيض فتاة بالغة: الرسم أ على اليمين والرسم ب في الوسط والرسم ج على اليسار'
         + ('، مع ترقيم أربعة عناصر من 1 إلى 4' if numbers else ''))
    return svg(W, H, t, ''.join(body))


def fig_event():
    """dessin أ seul, sans numéros"""
    W, H = 150, 148
    body = [panel_frame(1, W - 2, H), follicle_ruptured(W / 2, 88, numbers=False), label(W / 2, 140, 'أ', 13)]
    return svg(W, H, 'الرسم أ: بنية في مبيض فتاة بالغة تظهر فيها خليّة جنسيّة خارج جدار مفتوح', ''.join(body))


if __name__ == '__main__':
    import os
    out = '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/svt-l04-work/render'
    open(out + '/m6_three.svg', 'w', encoding='utf-8').write(fig_three(True))
    open(out + '/m6_event.svg', 'w', encoding='utf-8').write(fig_event())
    print(len(fig_three(True)), len(fig_event()))

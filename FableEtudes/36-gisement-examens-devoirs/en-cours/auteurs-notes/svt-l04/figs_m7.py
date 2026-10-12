#!/usr/bin/env python3
"""Figures de la mission 2021 ex3 : Document 3 (deux cellules sexuelles) et Document 4 (calendrier des règles).
Refaites d'après le PDF 2021 (C05, p.2-3). Document 3 : (أ) ovocyte entouré de la couronne de petites cellules en gouttes,
enveloppe jaune épaisse doublée d'un liseré mauve, plaque sombre oblique (chromosomes) dans un fuseau pointillé à deux pôles,
petit corps ovale noir (globule polaire) dans un renflement de l'enveloppe ; repères 1 (plaque sombre), 2 (zone claire), 3 (corps ovale).
(ب) spermatozoïde : tête noire coiffée d'une calotte jaune (4), point noir, pièce intermédiaire en anneaux empilés (5, deux flèches),
flagelle à double contour recourbé en U qui s'effile (6). Document 4 : calendrier jui./août, jours de règles colorés.
Chiffres/lettres seulement ; l'arabe n'est que dans <title>.
"""
import math, sys
sys.path.insert(0, '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/svt-l04-work')
from lib import f, svg, label

DARK = '#0f172a'
YEL = '#facc15'
MAUVE = '#a855f7'


def arrow(x0, y0, x1, y1, head=6.5, color=DARK):
    a = math.atan2(y1 - y0, x1 - x0)
    bx, by = x1 - head * math.cos(a), y1 - head * math.sin(a)
    px, py = -math.sin(a) * head * 0.45, math.cos(a) * head * 0.45
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.6"/>'
            '<polygon points="%s,%s %s,%s %s,%s" fill="%s"/>') % (
        f(x0), f(y0), f(bx), f(by), color, f(x1), f(y1), f(bx + px), f(by + py), f(bx - px), f(by - py), color)


def oval(cx, cy, rx, ry, ang_deg, fill, stroke=None, n=18):
    a = math.radians(ang_deg)
    pts = []
    for i in range(n):
        t = 2 * math.pi * i / n
        x, y = rx * math.cos(t), ry * math.sin(t)
        pts.append((cx + x * math.cos(a) - y * math.sin(a), cy + x * math.sin(a) + y * math.cos(a)))
    s = ' '.join('%s,%s' % (f(x), f(y)) for x, y in pts)
    return '<polygon points="%s" fill="%s"%s/>' % (s, fill, (' stroke="%s" stroke-width="1"' % stroke) if stroke else '')


# ------------------------------------------------------------------ ovocyte (dessin أ)
def oocyte_body(ox, oy):
    b = []
    N = 40
    for k in range(N):
        a = 2 * math.pi * k / N
        ca, sa = math.cos(a), math.sin(a)
        # repère local : radial (ca,sa), tangent (-sa,ca)
        def P(r, t):
            return ox + r * ca - t * sa, oy + r * sa + t * ca
        p0 = P(39.5, 0)
        p1 = P(44.5, 3.3)
        p2 = P(50.5, 2.4)
        p3 = P(53.5, 0)
        p4 = P(50.5, -2.4)
        p5 = P(44.5, -3.3)
        d = 'M%s %s Q%s %s %s %s Q%s %s %s %s Q%s %s %s %s Q%s %s %s %s Z' % (
            f(p0[0]), f(p0[1]), f(p1[0]), f(p1[1]), f(p2[0]), f(p2[1]),
            f(P(54, 3)[0]), f(P(54, 3)[1]), f(p3[0]), f(p3[1]),
            f(P(54, -3)[0]), f(P(54, -3)[1]), f(p4[0]), f(p4[1]),
            f(p5[0]), f(p5[1]), f(p0[0]), f(p0[1]))
        b.append('<path d="%s" fill="#fef3c7" stroke="%s" stroke-width="0.8" stroke-linejoin="round"/>' % (d, DARK))
        b.append('<circle cx="%s" cy="%s" r="0.9" fill="%s"/>' % (f(P(48, 0)[0]), f(P(48, 0)[1]), DARK))
    # enveloppe jaune épaisse + liseré mauve + cellule claire
    b.append('<circle cx="%s" cy="%s" r="36" fill="none" stroke="%s" stroke-width="7"/>' % (f(ox), f(oy), YEL))
    b.append('<circle cx="%s" cy="%s" r="39.6" fill="none" stroke="%s" stroke-width="0.9"/>' % (f(ox), f(oy), DARK))
    b.append('<circle cx="%s" cy="%s" r="32.5" fill="#fffdf2" stroke="%s" stroke-width="1.3"/>' % (f(ox), f(oy), MAUVE))
    # renflement de l'enveloppe en haut à droite + petit corps ovale noir (globule polaire)
    ang = math.radians(-42)
    bx, by = ox + 36 * math.cos(ang), oy + 36 * math.sin(ang)
    b.append('<circle cx="%s" cy="%s" r="6.2" fill="%s" stroke="%s" stroke-width="0.9"/>' % (f(bx), f(by), YEL, DARK))
    px, py = ox + 33.2 * math.cos(ang), oy + 33.2 * math.sin(ang)
    b.append(oval(px, py, 5.2, 3.3, -42 + 90, DARK))
    # plaque sombre oblique (chromosomes) et fuseau pointillé à deux pôles
    cx, cy = ox - 6, oy - 2
    p1 = (cx + 17, cy - 17)
    p2 = (cx - 17, cy + 17)
    e1 = (cx - 9, cy - 9)
    e2 = (cx + 9, cy + 9)
    for p in (p1, p2):
        for e in (e1, e2):
            b.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#475569" stroke-width="0.9" stroke-dasharray="1.6 2"/>' % (f(p[0]), f(p[1]), f(e[0]), f(e[1])))
        for k in range(8):
            t = 2 * math.pi * k / 8
            b.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#475569" stroke-width="0.8"/>' % (
                f(p[0]), f(p[1]), f(p[0] + 4.2 * math.cos(t)), f(p[1] + 4.2 * math.sin(t))))
    b.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="4.6" stroke-linecap="round"/>' % (f(e1[0]), f(e1[1]), f(e2[0]), f(e2[1]), DARK))
    return ''.join(b), (ox, oy), e2, (px, py)


def fig_oocyte(numbers=True):
    W, H = 200, 176
    ox, oy = 92, 92
    body, O, e2, polar = oocyte_body(ox, oy)
    b = [body]
    if numbers:
        # 1 : extrémité basse de la plaque sombre ; 2 : zone claire sous la plaque ; 3 : petit corps ovale (trait sans flèche large)
        b.append(arrow(176, 98, e2[0] + 4, e2[1] + 1))
        b.append(label(186, 102, '1', 14, DARK, 'start'))
        b.append(arrow(176, 128, ox + 6, oy + 24))
        b.append(label(186, 132, '2', 14, DARK, 'start'))
        b.append(arrow(34, 18, polar[0] - 2, polar[1] - 2))
        b.append(label(26, 20, '3', 14, DARK, 'end'))
    t = ('رسم مبسّط لخليّة جنسيّة أنثويّة: خليّة كرويّة محاطة بغلاف أصفر سميك وبتاج من خلايا صغيرة على شكل قطرات، '
         'في داخلها قضيب أسود مائل وحوله ألياف دقيقة مقطّعة تلتقي في قطبين، وبين الخليّة والغلاف جسم صغير بيضويّ أسود')
    if numbers:
        t += '، مع ترقيم ثلاثة عناصر من 1 إلى 3'
    return svg(W, H, t, ''.join(b))


# ------------------------------------------------------------------ spermatozoïde (dessin ب)
def sperm_body(sx):
    b = []
    # flagelle : double contour, recourbé en U puis s'effilant
    d = 'M%s 92 L%s 128 C%s 176 %s 176 %s 128 L%s 104' % (f(sx), f(sx), f(sx), f(sx + 62), f(sx + 62), f(sx + 62))
    b.append('<path d="%s" fill="none" stroke="%s" stroke-width="6.4" stroke-linecap="round" stroke-linejoin="round"/>' % (d, DARK))
    b.append('<path d="%s" fill="none" stroke="#ffffff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>' % d)
    b.append('<path d="M%s 104 C%s 98 %s 92 %s 84" fill="none" stroke="%s" stroke-width="1.4" stroke-linecap="round"/>' % (f(sx + 62), f(sx + 62), f(sx + 63), f(sx + 66), DARK))
    # pièce intermédiaire : anneaux empilés
    for k in range(7):
        y = 58 + k * 5.2
        b.append('<rect x="%s" y="%s" width="10" height="4" rx="1.8" fill="#ffffff" stroke="%s" stroke-width="1.2"/>' % (f(sx - 5), f(y), DARK))
    # col fin + point noir (centriole)
    b.append('<line x1="%s" y1="50" x2="%s" y2="58" stroke="%s" stroke-width="3"/>' % (f(sx), f(sx), DARK))
    b.append('<circle cx="%s" cy="49.5" r="2.4" fill="%s"/>' % (f(sx), DARK))
    # tête : noyau noir et calotte jaune (acrosome)
    b.append('<ellipse cx="%s" cy="30" rx="13" ry="17" fill="#ffffff" stroke="%s" stroke-width="1.6"/>' % (f(sx), DARK))
    b.append('<ellipse cx="%s" cy="33" rx="10" ry="13.5" fill="#0b0f1a"/>' % f(sx))
    cap = ('M%s 17 C%s 8 %s 8 %s 17 C%s 12 %s 12 %s 18 Z') % (f(sx - 11), f(sx - 6), f(sx + 6), f(sx + 11), f(sx + 5), f(sx - 5), f(sx - 11))
    b.append('<path d="%s" fill="%s" stroke="#a16207" stroke-width="1.2" stroke-linejoin="round"/>' % (cap, YEL))
    return ''.join(b)


def fig_sperm(numbers=True):
    W, H = 170, 176
    sx = 50
    b = [sperm_body(sx)]
    if numbers:
        # 4 : calotte ; 5 : deux anneaux (deux flèches issues du même repère) ; 6 : flagelle sur la branche de droite
        b.append(arrow(104, 22, sx + 7, 17))
        b.append(label(112, 26, '4', 14, DARK, 'start'))
        b.append(arrow(104, 70, sx + 7, 64))
        b.append(arrow(104, 70, sx + 7, 80))
        b.append(label(112, 74, '5', 14, DARK, 'start'))
        b.append(arrow(150, 134, sx + 62 + 5, 134))
        b.append(label(156, 138, '6', 14, DARK, 'start'))
    t = ('رسم مبسّط لخليّة جنسيّة ذكريّة: رأس بيضويّ أسود تعلوه قلنسوة صفراء، يليه عنق دقيق عليه نقطة سوداء، '
         'ثمّ جزء من حلقات صغيرة متراصّة، ثمّ ذيل طويل ذو حدّين ينحني على شكل حرف U وينتهي بخيط دقيق')
    if numbers:
        t += '، مع ترقيم ثلاثة عناصر من 4 إلى 6'
    return svg(W, H, t, ''.join(b))


def fig_pair():
    """les deux dessins du Document 3 côte à côte, sans repères : أ (ovocyte) à droite, ب (spermatozoïde) à gauche."""
    W, H = 360, 190
    body, _, _, _ = oocyte_body(272, 88)
    b = ['<rect x="2" y="2" width="176" height="%s" fill="none" stroke="#94a3b8" stroke-width="1"/>' % f(H - 4),
         '<rect x="182" y="2" width="176" height="%s" fill="none" stroke="#94a3b8" stroke-width="1"/>' % f(H - 4),
         sperm_body(62), body, label(90, 182, 'ب', 14, DARK), label(272, 182, 'أ', 14, DARK)]
    t = ('رسمان مبسّطان لخليّتين جنسيّتين عند الإنسان: الرسم أ على اليمين لخليّة كرويّة محاطة بغلاف وبتاج من خلايا صغيرة، '
         'والرسم ب على اليسار لخليّة ذات رأس وذيل طويل')
    return svg(W, H, t, ''.join(b))


# ------------------------------------------------------------------ calendrier (Document 4)
JULY = [[None, 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25, 26, 27], [28, 29, 30, 31, None, None, None]]
AUG = [[None, None, None, None, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31]]
JULY_ON = {6, 7, 8, 9, 10}
AUG_ON = {1, 2, 3, 4, 5, 27, 28, 29, 30, 31}


def month_block(x0, y0, grid, on, cw=30, ch=17):
    b = []
    for r, row in enumerate(grid):
        for c, d in enumerate(row):
            if d is None:
                continue
            x, y = x0 + c * cw, y0 + r * ch
            hot = d in on
            b.append('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" stroke-width="1"/>' % (
                f(x), f(y), f(cw), f(ch), '#fdba74' if hot else '#ffffff', '#c2410c' if hot else '#cbd5e1'))
            b.append('<text x="%s" y="%s" text-anchor="middle" font-size="11" font-weight="%d" fill="%s">%d</text>' % (
                f(x + cw / 2), f(y + ch - 5), 700 if hot else 500, '#7c2d12' if hot else DARK, d))
    return ''.join(b)


def fig_calendar():
    W, H = 232, 214
    cw, ch = 30, 17
    x0 = (W - 7 * cw) / 2
    b = [month_block(x0, 8, JULY, JULY_ON, cw, ch), month_block(x0, 8 + 5 * ch + 14, AUG, AUG_ON, cw, ch)]
    t = ('روزنامة شهرين متتاليين: جويلية في الأعلى (31 يومًا) ثمّ أوت في الأسفل، وقد لُوّنت بالبرتقاليّ الخانات '
         'التي ظهر فيها الحيض لدى امرأة')
    return svg(W, H, t, ''.join(b))


if __name__ == '__main__':
    out = '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/svt-l04-work/render'
    open(out + '/m7_oocyte.svg', 'w', encoding='utf-8').write(fig_oocyte(True))
    open(out + '/m7_oocyte_plain.svg', 'w', encoding='utf-8').write(fig_oocyte(False))
    open(out + '/m7_sperm.svg', 'w', encoding='utf-8').write(fig_sperm(True))
    open(out + '/m7_calendar.svg', 'w', encoding='utf-8').write(fig_calendar())
    open(out + '/m7_pair.svg', 'w', encoding='utf-8').write(fig_pair())
    print(len(fig_oocyte(True)), len(fig_sperm(True)), len(fig_calendar()))

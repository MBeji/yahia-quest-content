#!/usr/bin/env python3
"""Figure de la mission 2025 ex5 : Document 4 (concentrations des éléments X et Y le long du néphron).
Refait d'après le PDF 2025 (C02, p.4) : quatre zones de largeur égale (glomérule, zone أ, zone ب, canal collecteur),
X (trait plein) = 1 g/L jusqu'au début de la zone ب puis chute à 0 dans la première moitié de la zone ب ;
Y (pointillé) = 0 jusqu'au début de la zone ب puis monte à 0,5 dans la première moitié de la zone ب, reste à 0,5.
Les deux courbes se croisent vers 0,5. Chiffres, X, Y et les lettres أ ب seulement (arabe dans <title>).
"""
import math, sys
sys.path.insert(0, '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/svt-l04-work')
from lib import f, svg, label

DARK = '#0f172a'
GREY = '#64748b'
GREEN = '#0f6e56'

X0, X1 = 46, 286          # abscisses des bornes du tracé
ZW = (X1 - X0) / 4.0      # largeur d'une zone
Y0, Y1 = 150, 50          # ordonnées de 0 et de 1


def zx(i, frac=0.0):
    return X0 + ZW * (i + frac)


def yv(v):
    return Y0 + (Y1 - Y0) * v


def sigmoid(u):
    # chute lisse : 0 -> 1 sur u in [0, 1], valeur 0,5 vers u = 0,55 (croisement avec Y)
    g = lambda t: 1.0 / (1.0 + math.exp(-11.0 * (t - 0.55)))
    return (g(u) - g(0.0)) / (g(1.0) - g(0.0))


def x_curve():
    # X : plateau à 1 jusqu'au début de la zone 3 (index 2), puis chute jusqu'à 0 à mi-zone (0,5 de la zone)
    pts = [(zx(0), yv(1)), (zx(2), yv(1))]
    n = 30
    for k in range(1, n + 1):
        u = k / n
        x = zx(2) + ZW * 0.5 * u
        v = 1 - sigmoid(u)
        pts.append((x, yv(v)))
    pts.append((zx(4), yv(0)))
    return pts


def y_curve():
    # Y : 0 jusqu'au début de la zone 3, puis montée en concave jusqu'à 0,5 (atteint vers 0,42 de la zone), puis plateau
    pts = [(zx(0), yv(0)), (zx(2), yv(0))]
    n = 24
    for k in range(1, n + 1):
        u = k / n
        x = zx(2) + ZW * 0.42 * u
        v = 0.5 * (1 - (1 - u) ** 2.2)
        pts.append((x, yv(v)))
    pts.append((zx(4), yv(0.5)))
    return pts


def poly(pts):
    return ' '.join('%s,%s' % (f(x), f(y)) for x, y in pts)


def fig_curves():
    W, H = 300, 188
    b = []
    # axes
    b.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.6"/>' % (f(X0), f(Y0), f(X1 + 6), f(Y0), GREY))
    b.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.6"/>' % (f(X0), f(Y0 + 6), f(X0), f(30), GREY))
    b.append('<polygon points="%s,%s %s,%s %s,%s" fill="%s"/>' % (f(X0), f(24), f(X0 - 4), f(33), f(X0 + 4), f(33), GREY))
    # graduations de l'axe vertical : 0 ; 0,5 ; 1
    for v, t in ((0, '0'), (0.5, '0,5'), (1, '1')):
        b.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.6"/>' % (f(X0 - 4), f(yv(v)), f(X0), f(yv(v)), GREY))
        b.append(label(X0 - 8, yv(v) + 4, t, 11, DARK, 'end', 600))
    # bornes des zones : repères légers au-dessus de l'axe et graduations sous l'axe
    for i in range(1, 4):
        b.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3 3"/>' % (f(zx(i)), f(Y0 - 2), f(zx(i)), f(Y1 - 8)))
    for i in range(5):
        b.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.8"/>' % (f(zx(i)), f(Y0), f(zx(i)), f(Y0 + 8), DARK))
    # lettres des deux zones à identifier
    b.append(label(zx(1, 0.5), Y0 + 20, 'أ', 14, DARK))
    b.append(label(zx(2, 0.5), Y0 + 20, 'ب', 14, DARK))
    # unité
    b.append(label(X0 + 4, 22, 'g/L', 11, GREY, 'start', 600))
    # courbes
    b.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/>' % (poly(x_curve()), DARK))
    b.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="1.5 4" stroke-linecap="round" stroke-linejoin="round"/>' % (poly(y_curve()), GREEN))
    # légende
    b.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="2.8"/>' % (f(212), f(22), f(238), f(22), DARK))
    b.append(label(246, 26, 'X', 13, DARK, 'start'))
    b.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="3" stroke-dasharray="1.5 4" stroke-linecap="round"/>' % (f(212), f(40), f(238), f(40), GREEN))
    b.append(label(246, 44, 'Y', 13, GREEN, 'start'))
    t = ('منحنيان لتطوّر تركيز العنصرين X وY بوحدة غرام في اللتر عبر أربع مناطق متتالية في الكلية، '
         'من اليسار إلى اليمين: الكبيبة ثمّ المنطقة أ ثمّ المنطقة ب ثمّ القناة الجامعة')
    return svg(W, H, t, ''.join(b))


if __name__ == '__main__':
    out = '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/svt-l04-work/render'
    open(out + '/m2_curves.svg', 'w', encoding='utf-8').write(fig_curves())
    print(len(fig_curves()))

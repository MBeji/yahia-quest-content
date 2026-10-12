#!/usr/bin/env python3
"""Figure de la mission 2024 ex3 : Document 2 (néphron et vaisseaux).
Refait d'après le PDF 2024 (C03, p.2) : artérioles rouges et pelote (glomérule) dans une capsule jaune en coupe (Bowman),
tube urinaire sinueux avec anse en U profonde puis arche haute qui débouche dans le gros canal collecteur vertical
(deux petits embranchements). Repères : 3 = capsule (flèche), 4 = glomérule, 1 = arche du tube (flèche), 2 = canal collecteur (flèche).
Chiffres seulement (arabe dans <title>).
"""
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/svt-l04-work')
from lib import f, svg, label

DARK = '#0f172a'
YEL = '#fde047'
YEL_PALE = '#fef08a'
RED = '#dc2626'
RED_D = '#7f1d1d'

G = (64, 78)   # centre du glomérule / de la capsule
RC = 28        # rayon de la capsule
RG = 15        # rayon de la pelote


def tube(d, outer=9, inner=5.6):
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round" stroke-linecap="butt"/>'
            '<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round" stroke-linecap="butt"/>') % (
        d, DARK, f(outer), d, YEL, f(inner))


def arrow(x0, y0, x1, y1, color=DARK, head=6.5):
    """flèche du point (x0,y0) vers la cible (x1,y1)"""
    import math
    a = math.atan2(y1 - y0, x1 - x0)
    bx, by = x1 - head * math.cos(a), y1 - head * math.sin(a)
    px, py = -math.sin(a) * head * 0.45, math.cos(a) * head * 0.45
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.6"/>'
            '<polygon points="%s,%s %s,%s %s,%s" fill="%s"/>') % (
        f(x0), f(y0), f(bx), f(by), color, f(x1), f(y1), f(bx + px), f(by + py), f(bx - px), f(by - py), color)


def nephron_body():
    gx, gy = G
    b = []
    # branches latérales du canal collecteur (dessinées avant le canal)
    b.append(tube('M252 86 L270 76', 10.5, 7.6))
    b.append(tube('M236 132 L220 140', 10.5, 7.6))
    # tube urinaire : partie sinueuse, descente, anse en U, remontée, arche haute, jonction au canal
    d = ('M%s %s C100 62 110 96 124 80 C132 70 144 58 160 60 L160 150 C160 174 182 174 182 150 L182 70 '
         'C182 46 208 40 224 56 L238 72') % (f(gx + RC - 1), f(gy))
    b.append(tube(d))
    # gros canal collecteur vertical, ouvert en bas
    b.append('<rect x="236" y="24" width="16" height="152" fill="%s" stroke="%s" stroke-width="2.2"/>' % (YEL, DARK))
    b.append('<ellipse cx="244" cy="176" rx="8" ry="3.2" fill="%s" stroke="%s" stroke-width="2"/>' % (YEL_PALE, DARK))
    # capsule : coupe jaune autour de la pelote
    b.append('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="2.4"/>' % (f(gx), f(gy), f(RC), YEL, DARK))
    b.append('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="1.4"/>' % (f(gx), f(gy), f(RC - 6), YEL_PALE, '#ca8a04'))
    # artérioles qui arrivent à la pelote (en haut : ouverte ; en bas : sort)
    b.append('<path d="M10 38 C32 38 44 56 54 70" fill="none" stroke="%s" stroke-width="11.5" stroke-linecap="round"/>' % RED_D)
    b.append('<path d="M10 38 C32 38 44 56 54 70" fill="none" stroke="%s" stroke-width="8.5" stroke-linecap="round"/>' % RED)
    b.append('<path d="M10 124 C32 122 44 102 54 90" fill="none" stroke="%s" stroke-width="11.5" stroke-linecap="round"/>' % RED_D)
    b.append('<path d="M10 124 C32 122 44 102 54 90" fill="none" stroke="%s" stroke-width="8.5" stroke-linecap="round"/>' % RED)
    # pelote de capillaires
    b.append('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="1.8"/>' % (f(gx + 2), f(gy), f(RG), RED, RED_D))
    for dx, dy, rx, ry in ((-4, -5, 4.2, 2.8), (6, -3, 3.6, 2.6), (-2, 5, 4.4, 2.8), (8, 5, 3.4, 2.4)):
        b.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="#ffffff" stroke="%s" stroke-width="1"/>' % (f(gx + 2 + dx), f(gy + dy), f(rx), f(ry), RED_D))
    return ''.join(b)


TITLE = ('رسم توضيحي لوحدة وظيفيّة في عضو من جسم الإنسان: أوعية دمويّة حمراء تلتقي على كبّة داخل كأس صفراء، '
         'يخرج منها أنبوب ملتوٍ ذو انحناء عميق على شكل حرف U، ثمّ قوس يصبّ في قناة عموديّة كبيرة تحمل فرعين جانبيّين قصيرين')


def fig_nephron(numbers=True):
    W, H = 300, 188
    b = [nephron_body()]
    if numbers:
        gx, gy = G
        # 3 : capsule (flèche) ; 4 : glomérule (flèche) ; 1 : arche du tube (flèche) ; 2 : canal collecteur (flèche)
        b.append(arrow(98, 30, 77, 59))
        b.append(label(104, 27, '3', 14))
        b.append(arrow(gx + 2, 126, gx + 2, 93))
        b.append(label(gx + 2, 142, '4', 14))
        b.append(arrow(214, 26, 207, 44))
        b.append(label(218, 22, '1', 14))
        b.append(arrow(284, 148, 255, 148))
        b.append(label(290, 152, '2', 14, DARK, 'start'))
    return svg(W, H, TITLE, ''.join(b))


if __name__ == '__main__':
    out = '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/svt-l04-work/render'
    open(out + '/m3_nephron.svg', 'w', encoding='utf-8').write(fig_nephron(True))
    open(out + '/m3_nephron_plain.svg', 'w', encoding='utf-8').write(fig_nephron(False))
    print(len(fig_nephron(True)), len(fig_nephron(False)))

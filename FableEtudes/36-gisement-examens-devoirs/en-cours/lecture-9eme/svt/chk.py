#!/usr/bin/env python3
"""Contrôle local des lignes : archétype <= 12 mots, piège 5-10 mots (ou '-'), pas de chiffre dans les colonnes de prose, pas de mot-nombre."""
import sys, re, glob
SP = "/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/gisement/9eme-sciences-vie-terre"
NUMW = {"deux","trois","quatre","cinq","six","sept","huit","neuf","dix","onze","douze","vingt","trente","cent","mille","premier","seconde","second","deuxième"}
bad = 0
for f in sorted(glob.glob(f"{SP}/lines/*.tsv")):
    for i, raw in enumerate(open(f, encoding="utf-8").read().splitlines(), 1):
        if not raw.strip(): continue
        c = raw.split("\t")
        if len(c) != 10:
            print(f"{f}:{i} {len(c)} colonnes"); bad += 1; continue
        arche, piege = c[6], c[8]
        wa = len(arche.split()); wp = 0 if piege == "-" else len(piege.split())
        probs = []
        if wa > 12: probs.append(f"archétype {wa} mots")
        if piege != "-" and not (5 <= wp <= 10): probs.append(f"piège {wp} mots")
        for label, t in (("archétype", arche), ("piège", piege)):
            if re.search(r"\d", t): probs.append(f"chiffre dans {label}")
            w = set(re.findall(r"[a-zàâçéèêëîïôûùüÿœ']+", t.lower())) & NUMW
            if w: probs.append(f"mot-nombre dans {label}: {sorted(w)}")
        print(f"{'OK ' if not probs else 'KO '} {f.split('/')[-1]}:{i} exo {c[2]} a={wa} p={wp} {('; '.join(probs))}")
        bad += bool(probs)
print("problèmes :", bad)

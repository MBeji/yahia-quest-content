"""Prépare les fichiers pending d'une livraison à partir de pending-tags/<LOT>.json (écrit par l'auteur) :
   <LOT>-deliver.json  = nouvelles + options du lot + options_id_existant_absent_de_l_arbre (l'id existe sur main, donc dans l'arbre de livraison)
   <LOT>-extras-<NN>.json = une par chapitre pour les placements hors lot (options publiées relues sur main)
Usage : mk-pending.py <LOT>"""
import json, sys
SP = "/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/pending-tags/"
lot = sys.argv[1]
d = json.load(open(SP + lot + ".json", encoding="utf-8"))
opts = list(d.get("options", [])) + list(d.get("options_id_existant_absent_de_l_arbre", []))
json.dump({"lot": lot, "chapitre": d["chapitre"], "nouvelles": d.get("nouvelles", {}), "options": opts},
          open(SP + lot + "-deliver.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
by = {}
for h in d.get("hors_lot", []):
    by.setdefault(h["chapitre"], []).append({k: h[k] for k in ("file", "q", "opt", "id", "texte") if k in h})
for ch, o in by.items():
    json.dump({"lot": lot + "-extras", "chapitre": ch, "nouvelles": {}, "options": o},
              open(SP + "%s-extras-%s.json" % (lot, ch[:2]), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(lot, "deliver:", len(opts), "options ;", {c: len(o) for c, o in by.items()})

# -*- coding: utf-8 -*-
"""Banque de poses de Will + rotation + poses de saison (Journal Débrouya).
Usage : python3 outils/poses.py AAAA-MM-JJ   -> poses à utiliser pour une édition envoyée ce jour-là
Règles :
- 4 emplacements par édition : accueil (salut), relance au milieu, intro méthode, signature.
- Accueil et signature : pose de saison si on est dans une fenêtre de fête, sinon salut / clin.
- Relance et méthode : piochées dans la banque, jamais la même pose que l'édition précédente (historique.json).
"""
import json, os, sys, datetime as dt
HERE=os.path.dirname(os.path.abspath(__file__))
BASE=["menton","pouce","pointe","surpris","bras-croises","telephone","carnet","celebre"]
FIXES={"accueil":"salut","signature":"clin"}
# Fenêtres d'utilisation des poses de saison (dates d'envoi incluses). Sources : calendrier scolaire Martinique 2026-2027, jours gras 2027.
SAISONS=[
    ("noel",      "2026-12-12","2026-12-27","Noël (25 décembre ; vacances aux Antilles dès le 19 décembre)"),
    ("nouvel-an", "2026-12-28","2027-01-08","Nouvel An"),
    ("carnaval",  "2027-01-29","2027-02-10","Carnaval (jours gras 8-10 février 2027)"),
    ("paques",    "2027-03-19","2027-04-02","Pâques (dimanche 28 mars 2027)"),
    ("vacances",  "2027-06-26","2027-07-13","Grandes vacances (fin des cours samedi 3 juillet 2027)"),
    ("rentree",   "2027-08-24","2027-09-10","Rentrée scolaire (date 2027 à confirmer)"),
]
def saison(d):
    for pose,a,b,lab in SAISONS:
        if a<=d<=b: return pose,lab
    return None,None
def choisir(d):
    hist_p=os.path.join(HERE,"avatar","historique.json")
    try: hist=json.load(open(hist_p,encoding="utf-8"))
    except Exception: hist=[]
    dernieres=set(hist[-1]["poses"]) if hist else set()
    avant=set(hist[-2]["poses"]) if len(hist)>1 else set()
    libres=[p for p in BASE if p not in dernieres] or BASE
    libres.sort(key=lambda p:(p in avant, BASE.index(p)))
    s,lab=saison(d)
    return {"accueil":s or FIXES["accueil"],"relance":libres[0],"methode":libres[1],"signature":FIXES["signature"] if s else FIXES["signature"],"fete":lab}
def enregistrer(d,edition,poses):
    hist_p=os.path.join(HERE,"avatar","historique.json")
    try: hist=json.load(open(hist_p,encoding="utf-8"))
    except Exception: hist=[]
    hist.append({"date":d,"edition":edition,"poses":poses}); json.dump(hist,open(hist_p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
if __name__=="__main__":
    print(json.dumps(choisir(sys.argv[1] if len(sys.argv)>1 else dt.date.today().isoformat()),ensure_ascii=False,indent=1))

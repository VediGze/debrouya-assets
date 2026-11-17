# -*- coding: utf-8 -*-
"""Illustrations du Journal Débrouya #154."""
import sys, os, base64, math, json
from playwright.sync_api import sync_playwright
HERE=os.path.dirname(os.path.abspath(__file__))

INK="#1E2A2F"; TEAL="#136D68"; TEAL_D="#0D524E"; TEAL_L="#DDEFEC"; TEAL_M="#8CC5C0"
MANGO="#E57638"; MANGO_D="#C65F25"; MANGO_L="#FDEADB"; CREAM="#FBF5EC"; PEACH="#FFD3AE"
GREY="#8E989C"; GREY_L="#E9E3D9"; WHITE="#FFFFFF"
F="font-family:Inter,Arial,sans-serif"

def txt(x,y,s,size=18,fill=INK,w=700,anchor="middle",ls=0,style=""):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" style="{F};font-size:{size}px;font-weight:{w};letter-spacing:{ls}px;{style}" fill="{fill}">{s}</text>'
def svg(w,h,inner,bg=None):
    b=f'<rect width="{w}" height="{h}" rx="22" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs><clipPath id="c"><rect width="{w}" height="{h}" rx="22"/></clipPath></defs><g clip-path="url(#c)">{b}{inner}</g></svg>'
def rings(x,y,w,color=GREY_L): return "".join(f'<circle cx="{x+w*k/4}" cy="{y}" r="6" fill="{color}"/>' for k in (1,2,3))
def cal(x,y,w,h,head,headfill,body=""):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{WHITE}"/>'
            f'<path d="M{x} {y+14} a14 14 0 0 1 14 -14 h{w-28} a14 14 0 0 1 14 14 v30 h-{w} z" fill="{headfill}"/>'
            + txt(x+w/2,y+31,head,18,WHITE,800) + body)
def house(cx,cy,s=1,col=TEAL,door=WHITE,dash=False):
    st=f'fill="none" stroke="{col}" stroke-width="{4/s:.1f}" stroke-dasharray="{10/s:.0f} {8/s:.0f}"' if dash else f'fill="{col}"'
    g=(f'<polygon points="{cx-46},{cy-6} {cx},{cy-46} {cx+46},{cy-6}" {st}/>'
       f'<rect x="{cx-34}" y="{cy-8}" width="68" height="52" {st}/>')
    if not dash: g+=f'<rect x="{cx-10}" y="{cy+16}" width="20" height="28" fill="{door}"/><rect x="{cx-26}" y="{cy+2}" width="14" height="12" fill="{door}"/><rect x="{cx+12}" y="{cy+2}" width="14" height="12" fill="{door}"/>'
    return f'<g transform="translate({cx} {cy}) scale({s}) translate({-cx} {-cy})">{g}</g>'
def check(cx,cy,col=TEAL,r=13):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}"/><path d="M{cx-6} {cy} l4 5 l8 -10" stroke="{WHITE}" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
def cross(cx,cy,col=MANGO,r=13):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}"/><path d="M{cx-5} {cy-5} l10 10 M{cx+5} {cy-5} l-10 10" stroke="{WHITE}" stroke-width="3.5" stroke-linecap="round"/>'
def heart(cx,cy,s=1,col=MANGO):
    return f'<path transform="translate({cx} {cy}) scale({s})" d="M0 6 C-14 -6 -10 -16 0 -9 C10 -16 14 -6 0 6 Z" fill="{col}"/>'

AV=os.path.join(HERE,"avatar")
def will_panel(pose, lines, h=370, accent_last=True):
    n=len(lines); size=31 if n<=3 else 27; lh=size+9
    bh=lh*n+56; by=(h-bh)/2
    fp=pose if pose.endswith(".png") else os.path.join(AV,f"will-{pose}.png")
    data=base64.b64encode(open(fp,"rb").read()).decode()
    from PIL import Image as _I
    _im=_I.open(fp); _bot=_im.getbbox()[3]/_im.size[1]   # bas réel du personnage : on le colle au bas du cadre
    sz=h-20
    yimg=h-sz*_bot
    ximg=14-sz*_im.getbbox()[0]/_im.size[0]   # jamais coupé à gauche
    top=by+(bh-((n-1)*lh+0.72*size))/2+0.72*size
    t="".join(txt(450, top+k*lh, l, size, TEAL if (accent_last and k==n-1) else INK, 800) for k,l in enumerate(lines))
    return svg(600,h,
        f'<image href="data:image/png;base64,{data}" x="{ximg}" y="{yimg}" width="{sz}" height="{sz}"/>'
        f'<rect x="318" y="{by}" width="264" height="{bh}" rx="28" fill="{WHITE}" stroke="{INK}" stroke-width="3"/>'
        f'<path d="M320 {by+bh/2-14} L284 {by+bh/2+4} L320 {by+bh/2+16}" fill="{WHITE}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
        f'<rect x="316" y="{by+bh/2-12}" width="8" height="26" fill="{WHITE}"/>' + t, TEAL_L)


out={}
P=json.loads(sys.argv[3])
ONLY=P.get("only")
out["00-will-salut"]=will_panel(P["accueil"],["Salut","la famille ! 🔥"],h=330)
out["06-will"]=will_panel(P["relance"],["On achète","loué pour le","garder loué."])
out["09-will-methode"]=will_panel(P["methode"],["C’est parti,","étape par","étape."])
out["17-will-fin"]=will_panel(P["signature"],["C’était Will.","Ciao ! 🔥"],h=330)

def sign_house(cx,cy,s=1,body=WHITE,roof=MANGO,line=INK,sign=TEAL,label="LOUÉ"):
    g=(f'<polygon points="{cx-110},{cy-60} {cx},{cy-140} {cx+110},{cy-60}" fill="{roof}"/>'
       f'<rect x="{cx-90}" y="{cy-62}" width="180" height="140" fill="{body}" stroke="{line}" stroke-width="3"/>'
       f'<rect x="{cx-66}" y="{cy-38}" width="40" height="40" fill="{PEACH}" stroke="{line}" stroke-width="2"/><rect x="{cx+26}" y="{cy-38}" width="40" height="40" fill="{PEACH}" stroke="{line}" stroke-width="2"/>'
       f'<rect x="{cx-18}" y="{cy+20}" width="36" height="58" fill="{TEAL_M}" stroke="{line}" stroke-width="2"/>'
       + ((f'<line x1="{cx+130}" y1="{cy-20}" x2="{cx+130}" y2="{cy+78}" stroke="{line}" stroke-width="5"/>'
       f'<rect x="{cx+86}" y="{cy-64}" width="88" height="46" rx="8" fill="{sign}" stroke="{line}" stroke-width="2"/>'
       + txt(cx+130,cy-33,label,22,WHITE,800)) if label else ""))
    return f'<g transform="translate({cx} {cy}) scale({s}) translate({-cx} {-cy})">{g}</g>'

# 01. COUVERTURE
ban=base64.b64encode(open(sys.argv[2],"rb").read()).decode()
H=560
g=(f'<image href="data:image/jpeg;base64,{ban}" x="0" y="0" width="600" height="229" preserveAspectRatio="xMidYMid slice"/>'
   f'<path d="M0 200 C120 182 240 226 360 206 S540 188 600 204 V{H} H0 Z" fill="{TEAL_M}" opacity="0.55"/>'
   f'<path d="M0 214 C120 196 240 240 360 220 S540 202 600 218 V{H} H0 Z" fill="{TEAL}"/>'
   + txt(300,272,"ÉDITION #154",18,PEACH,800,ls=4)
   + txt(300,320,"Acheter un bien",38,WHITE,800)
   + txt(300,364,"déjà loué.",34,PEACH,800))
g+=sign_house(300,486,s=0.42,body=WHITE,roof=MANGO,line=WHITE,sign=TEAL,label="")
g+=(f'<path d="M0 520 C60 506 120 532 180 520 S300 506 360 520 S480 534 540 520 S600 514 620 520 V{H} H0 Z" fill="{TEAL_D}"/>'
    f'<path d="M0 536 C60 526 120 546 180 536 S300 526 360 536 S480 546 540 536 S600 532 620 536 V{H} H0 Z" fill="#0A403C"/>')
out["01-hero"]=svg(600,H,g,TEAL)

# 02. TU ACHÈTES LIBRE
g=txt(300,50,"TU ACHÈTES LIBRE : LES PREMIERS MOIS",21,TEAL,800,ls=0.5); y=74
for k,l in enumerate(["Tu fais les petits travaux.","Tu publies l’annonce.","Tu fais les visites.","Tu choisis ton locataire."]):
    g+=f'<rect x="24" y="{y}" width="552" height="58" rx="14" fill="{WHITE}"/><circle cx="58" cy="{y+29}" r="18" fill="{MANGO}"/>'+txt(58,y+37,str(k+1),21,WHITE,800)+txt(92,y+37,l,23,INK,700,anchor="start")
    y+=66
g+=f'<rect x="24" y="{y+6}" width="552" height="88" rx="16" fill="{MANGO}"/>'+txt(300,y+44,"Chaque mois, ta mensualité tombe.",23,WHITE,800)+txt(300,y+76,"Et aucun loyer ne rentre.",22,WHITE,700)
out["02-vide"]=svg(600,y+118,g,MANGO_L)

# 03. CE QUE LE LOCATAIRE EN PLACE T'APPORTE
items=[("Un loyer encaissé","dès le premier mois."),("Un locataire dont tu connais","les paiements depuis des mois."),("Un prix souvent","plus bas.")]
g=txt(300,50,"CE QUE LE LOCATAIRE EN PLACE T’APPORTE",21,TEAL,800,ls=0.5); y=74
for a_,b2 in items:
    g+=f'<rect x="24" y="{y}" width="552" height="90" rx="14" fill="{WHITE}"/>'+check(62,y+45,TEAL,r=18)+txt(98,y+40,a_,23,INK,800,anchor="start")+txt(98,y+72,b2,22,INK,600,anchor="start")
    y+=100
out["03-atouts"]=svg(600,y+14,g,TEAL_L)

# 04. DÉCOTE
rows=[("La plupart des logements loués vides","10 à 15 %",0.75),("Studio ou petite surface louée vide","5 à 10 %",0.45)]
g=txt(300,50,"DE COMBIEN LE PRIX BAISSE, EN GÉNÉRAL",21,TEAL,800,ls=0.5); y=80
for lab,val,w in rows:
    g+=txt(30,y+22,lab,22,INK,800,anchor="start")
    g+=f'<rect x="30" y="{y+36}" width="540" height="46" rx="12" fill="{WHITE}"/><rect x="30" y="{y+36}" width="{540*w}" height="46" rx="12" fill="{MANGO}"/>'
    g+=txt(30+540*w+14,y+68,val,23,INK,800,anchor="start")
    y+=110
g+=txt(300,y+20,"Ce sont des repères nationaux,",21,INK,600)+txt(300,y+50,"pas des chiffres antillais.",21,INK,600)
out["04-decote"]=svg(600,y+76,g,TEAL_L)

# 05. LE JOUR OÙ TU ACHÈTES
rows=[("Le bail",["Il continue avec toi, aux mêmes","conditions : loyer, durée, clauses."],"ok"),
      ("Le garant du locataire",["Son engagement reste en principe","valable, sauf clause contraire."],"ok"),
      ("L’assurance impayés du vendeur",["Elle ne te suit pas forcément :","demande le contrat avant de signer."],"warn"),
      ("Le dépôt de garantie",["C’est toi qui le rendras au locataire,","même si tu ne l’as jamais reçu."],"warn")]
g=txt(300,50,"LE JOUR OÙ TU ACHÈTES",21,TEAL,800,ls=1); y=74
for who,what,st in rows:
    h=52+32*len(what)
    g+=f'<rect x="24" y="{y}" width="552" height="{h}" rx="14" fill="{WHITE}"/>'
    g+=(check(60,y+h/2,TEAL,r=18) if st=="ok" else f'<circle cx="60" cy="{y+h/2}" r="18" fill="{MANGO}"/>'+txt(60,y+h/2+8,"!",23,WHITE,800))
    g+=txt(94,y+38,who,22,INK,800,anchor="start")+"".join(txt(94,y+70+j*32,l,21,INK,600,anchor="start") for j,l in enumerate(what))
    y+=h+10
out["05-loi"]=svg(600,y+14,g,TEAL_L)

# 07. DÉLAIS (LOCATION VIDE)
g=txt(300,50,"LOCATION VIDE : LES DÉLAIS APRÈS L’ACHAT",21,TEAL,800,ls=0.5)
cards=[("Pour le vendre libre",["Si le bail finit moins de 3 ans après","ton achat, ton congé ne prend effet","qu’à la fin du bail renouvelé une fois."]),
       ("Pour y habiter ou loger un proche",["Si le bail finit moins de 2 ans après","ton achat, ton congé ne prend effet","que 2 ans après ton achat."])]
y=74
for title,lines in cards:
    h=56+32*len(lines)
    g+=f'<rect x="24" y="{y}" width="552" height="{h}" rx="14" fill="{WHITE}"/><rect x="24" y="{y}" width="10" height="{h}" fill="{MANGO}"/>'
    g+=txt(50,y+38,title,22,MANGO_D,800,anchor="start")+"".join(txt(50,y+72+j*32,l,21,INK,600,anchor="start") for j,l in enumerate(lines))
    y+=h+12
g+=f'<rect x="24" y="{y}" width="552" height="88" rx="14" fill="{TEAL}"/>'+txt(300,y+38,"Dans tous les cas, préviens ton locataire",21,WHITE,800)+txt(300,y+68,"au moins 6 mois avant la fin du bail.",21,WHITE,700)
out["07-delais"]=svg(600,y+112,g,MANGO_L)

# 10. LE DOSSIER À DEMANDER
items=[("Le bail signé","et ses éventuels avenants."),("L’état des lieux d’entrée","signé à l’arrivée du locataire."),("Les paiements des 12 derniers mois :","quittances ou relevés de compte."),("Le montant du dépôt de garantie","versé par le locataire à son entrée."),("L’acte de caution du garant,","s’il y en a un.")]
g=""; y=24
for a_,b2 in items:
    g+=f'<rect x="24" y="{y}" width="552" height="86" rx="14" fill="{WHITE}"/>'+check(60,y+43,TEAL,r=17)+txt(92,y+38,a_,22,INK,800,anchor="start")+txt(92,y+70,b2,21,INK,600,anchor="start")
    y+=96
out["10-dossier"]=svg(600,y+14,g,TEAL_L)

# 11. LIRE LE BAIL : 3 POINTS (numéros dessinés)
rows=[("La date de fin du bail,","pour savoir où tu en es."),("Le type de location :","vide ou meublée, les règles changent."),("Le loyer,","comparé à ceux du quartier.")]
g=""; y=24
for k,(a_,b2) in enumerate(rows):
    g+=f'<rect x="24" y="{y}" width="552" height="90" rx="14" fill="{WHITE}"/><circle cx="64" cy="{y+45}" r="22" fill="{MANGO}"/>'+txt(64,y+54,str(k+1),23,WHITE,800)+txt(102,y+40,a_,23,INK,800,anchor="start")+txt(102,y+72,b2,22,INK,600,anchor="start")
    y+=100
out["11-bail"]=svg(600,y+14,g,MANGO_L)

# 13. EXEMPLE : LIBRE / LOUÉ
def col(x0,title,color,rows,badge,bfill,btxt,rowfill):
    g=txt(x0+135,46,"TU ACHÈTES",18,color,800,ls=1.5)+txt(x0+135,80,title,25,color,800)
    for k,(a_,b2) in enumerate(rows):
        y=102+k*98
        g+=f'<rect x="{x0}" y="{y}" width="270" height="86" rx="14" fill="{rowfill}"/>'+txt(x0+16,y+34,a_,20,INK,700,anchor="start")+txt(x0+16,y+68,b2,23,INK,800,anchor="start",style="font-variant-numeric:tabular-nums")
    g+=f'<rect x="{x0}" y="398" width="270" height="104" rx="16" fill="{bfill}"/>'+txt(x0+135,428,badge[0],19,btxt,700)+txt(x0+135,452,badge[1],19,btxt,700)+txt(x0+135,488,badge[2],30,btxt,800)
    return g
g=(f'<rect x="0" y="0" width="300" height="528" fill="#F1ECE3"/><rect x="300" y="0" width="300" height="528" fill="{TEAL_L}"/>'
   + col(16,"le T3 libre","#5F6B70",[("Prix d’achat","120 000 €"),("Loyers perdus (2 mois)","1 400 €"),("Rentabilité brute","7 %")],("Coût réel","avant le premier loyer","121 400 €"),GREY_L,INK,WHITE)
   + col(314,"le T3 loué",TEAL,[("Prix d’achat","108 000 €"),("Loyers perdus","0 €"),("Rentabilité brute","7,8 %")],("Coût réel","avant le premier loyer","108 000 €"),MANGO,INK,WHITE))
out["13-exemple"]=svg(600,528,g,WHITE)
if ONLY: out={k:v for k,v in out.items() if k in ONLY}
dest=sys.argv[1]; os.makedirs(dest,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(device_scale_factor=2)
    for name,s in out.items():
        pg.set_content(f'<html><body style="margin:0;background:transparent">{s}</body></html>'); pg.wait_for_timeout(120)
        pg.locator("svg").screenshot(path=f"{dest}/{name}.png", omit_background=True)
    b.close()
print(len(out),"images")

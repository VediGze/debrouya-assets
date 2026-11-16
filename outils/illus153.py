# -*- coding: utf-8 -*-
"""Illustrations du Journal Débrouya #153."""
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
    top=by+(bh-((n-1)*lh+0.72*size))/2+0.72*size
    t="".join(txt(450, top+k*lh, l, size, TEAL if (accent_last and k==n-1) else INK, 800) for k,l in enumerate(lines))
    return svg(600,h,
        f'<image href="data:image/png;base64,{data}" x="-8" y="{yimg}" width="{sz}" height="{sz}"/>'
        f'<rect x="318" y="{by}" width="264" height="{bh}" rx="28" fill="{WHITE}" stroke="{INK}" stroke-width="3"/>'
        f'<path d="M320 {by+bh/2-14} L284 {by+bh/2+4} L320 {by+bh/2+16}" fill="{WHITE}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
        f'<rect x="316" y="{by+bh/2-12}" width="8" height="26" fill="{WHITE}"/>' + t, TEAL_L)


out={}
P=json.loads(sys.argv[3])
IJ=P.get("ij_max","42,97 €")
out["00-will-salut"]=will_panel(P["accueil"],["Salut","la famille ! 🔥"],h=330)
out["06-will"]=will_panel(P["relance"],["Tu vois où","je veux en","venir ?"])
out["09-will-methode"]=will_panel(P["methode"],["Prêt ?","On y va."])
out["17-will-fin"]=will_panel(P["signature"],["C’était Will.","Ciao ! 🔥"],h=330)

# 01. COUVERTURE : salaire qui s'arrête, loyers qui continuent
ban=base64.b64encode(open(sys.argv[2],"rb").read()).decode()
H=560
g=(f'<image href="data:image/jpeg;base64,{ban}" x="0" y="0" width="600" height="229" preserveAspectRatio="xMidYMid slice"/>'
   f'<path d="M0 200 C120 182 240 226 360 206 S540 188 600 204 V{H} H0 Z" fill="{TEAL_M}" opacity="0.55"/>'
   f'<path d="M0 214 C120 196 240 240 360 220 S540 202 600 218 V{H} H0 Z" fill="{TEAL}"/>'
   + txt(300,272,"ÉDITION #153",18,PEACH,800,ls=4)
   + txt(300,320,"Ton salaire s’arrête,",38,WHITE,800)
   + txt(300,364,"tes loyers non.",34,PEACH,800))
# mini graphique : 6 mois, salaire qui chute au 3e, loyers constants
x0,x1=150,470; xs=[x0+(x1-x0)*k/5 for k in range(6)]
ysal=[404]*3; yloy=[446]*6
g+=f'<polyline points="{" ".join(f"{x},{y}" for x,y in zip(xs,yloy))}" fill="none" stroke="{PEACH}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
g+=f'<line x1="{xs[0]}" y1="404" x2="{xs[2]+20}" y2="404" stroke="{WHITE}" stroke-width="7" stroke-linecap="round"/><circle cx="{xs[2]+20}" cy="404" r="9" fill="{WHITE}"/>'+cross(xs[2]+48,404,MANGO,r=14)
g+=txt(x0-14,411,"Ton salaire",19,WHITE,800,anchor="end")+txt(x0-14,453,"Tes loyers",19,PEACH,800,anchor="end")
g+=(f'<path d="M0 520 C60 506 120 532 180 520 S300 506 360 520 S480 534 540 520 S600 514 620 520 V{H} H0 Z" fill="{TEAL_D}"/>'
    f'<path d="M0 536 C60 526 120 546 180 536 S300 526 360 536 S480 546 540 536 S600 532 620 536 V{H} H0 Z" fill="#0A403C"/>')
out["01-hero"]=svg(600,H,g,TEAL)

# 02. UN SEUL PILIER
g=txt(300,46,"TON BUDGET AUJOURD’HUI",18,TEAL,800,ls=1.5)
g+=f'<rect x="60" y="74" width="480" height="70" rx="12" fill="{MANGO}"/>'+txt(300,105,"Crédit ou loyer, courses, voiture,",20,WHITE,800)+txt(300,131,"assurances, factures…",20,WHITE,800)
for x in (110,410):
    g+=f'<rect x="{x}" y="160" width="80" height="170" rx="10" fill="none" stroke="{GREY}" stroke-width="3" stroke-dasharray="10 8"/>'+txt(x+40,256,"?",34,GREY,800)
g+=f'<rect x="250" y="160" width="100" height="170" rx="10" fill="{TEAL}"/>'+txt(300,238,"Ton",20,WHITE,800)+txt(300,264,"salaire",20,WHITE,800)
g+=f'<rect x="40" y="338" width="520" height="14" rx="7" fill="{GREY_L}"/>'
g+=txt(300,396,"Un seul pilier : toi.",26,INK,800)
out["02-pilier"]=svg(600,426,g,TEAL_L)

# 03. LES INDEMNITÉS JOURNALIÈRES
rows=[("50 %",["Tu touches la moitié de ton","salaire journalier de base."]),(IJ,["C’est le maximum par jour,","en brut, depuis juillet 2026."]),("3 jours",["Au début, tu ne touches rien :","c’est le délai de carence."])]
g=txt(300,46,"SI TU ES EN ARRÊT MALADIE",18,TEAL,800,ls=1.5); y=72
for big,lines in rows:
    g+=f'<rect x="30" y="{y}" width="540" height="96" rx="16" fill="{WHITE}"/>'
    g+=f'<rect x="30" y="{y}" width="190" height="96" rx="16" fill="{MANGO}"/><rect x="200" y="{y}" width="20" height="96" fill="{MANGO}"/>'
    g+=txt(125,y+59,big,32 if len(big)<8 else 28,WHITE,800)
    g+="".join(txt(240,y+42+j*28,l,19,INK,700,anchor="start") for j,l in enumerate(lines))
    y+=110
out["03-ij"]=svg(600,y+16,g,MANGO_L)

# 05. CE QUE PAIE TON SALAIRE / TON LOYER
g=(txt(300,46,"QUI PAIE QUOI ?",18,TEAL,800,ls=1.5)
   + f'<rect x="210" y="70" width="160" height="74" rx="14" fill="{MANGO}"/>'+txt(290,102,"Ton salaire",20,WHITE,800)+txt(290,128,"dépend de toi",18,WHITE,600)
   + f'<rect x="380" y="70" width="198" height="74" rx="14" fill="{TEAL}"/>'+txt(479,102,"Le loyer encaissé",19,WHITE,800)+txt(479,128,"dépend du logement",18,WHITE,600))
rows=[("Tu travailles",("✓",TEAL),("✓",TEAL)),("Tu es en arrêt",("Il baisse",MANGO),("✓",TEAL)),("Tu es à la retraite",("Il s’arrête",MANGO),("✓",TEAL))]
y=160
for lab,a,b2 in rows:
    g+=f'<rect x="22" y="{y}" width="556" height="64" rx="14" fill="{WHITE}"/>'+txt(36,y+40,lab,19,INK,800,anchor="start")
    for cx,(v,c) in ((290,a),(479,b2)):
        if v=="✓": g+=check(cx,y+32,c,r=17)
        else: g+=f'<rect x="{cx-62}" y="{y+14}" width="124" height="36" rx="18" fill="{c}"/>'+txt(cx,y+39,v,18,WHITE,800)
    y+=74
g+=txt(300,y+30,"Le loyer du mois est dû, quoi qu’il t’arrive.",20,INK,800)
out["05-qui-paie"]=svg(600,y+58,g,TEAL_L)

# 10. LES DEUX COLONNES
g=txt(300,46,"TON MOIS SANS SALAIRE",18,TEAL,800,ls=1.5)
L=["Crédit ou loyer","Courses","Voiture","Assurances","Abonnements"]
g+=f'<rect x="24" y="70" width="268" height="370" rx="16" fill="{WHITE}"/><rect x="24" y="70" width="268" height="84" rx="16" fill="{MANGO}"/><rect x="24" y="130" width="268" height="24" fill="{MANGO}"/>'
g+=txt(158,104,"Ce qui sort",21,WHITE,800)+txt(158,134,"chaque mois",19,WHITE,600)
g+="".join(txt(48,198+k*52,"– "+l,20,INK,700,anchor="start") for k,l in enumerate(L))
g+=f'<rect x="308" y="70" width="268" height="370" rx="16" fill="{WHITE}"/><rect x="308" y="70" width="268" height="84" rx="16" fill="{TEAL}"/><rect x="308" y="130" width="268" height="24" fill="{TEAL}"/>'
g+=txt(442,104,"Ce qui rentre",21,WHITE,800)+txt(442,134,"sans que tu travailles",19,WHITE,600)
g+="".join(f'<line x1="332" y1="{200+k*52}" x2="552" y2="{200+k*52}" stroke="{GREY_L}" stroke-width="3" stroke-dasharray="8 8"/>' for k in range(5))
g+=f'<rect x="402" y="232" width="80" height="92" fill="{WHITE}"/>'+txt(442,302,"?",60,TEAL_M,800)
out["10-colonnes"]=svg(600,466,g,TEAL_L)

# 11. LE TEST DU BIEN QUI TIENT DEBOUT
g=txt(300,46,"AVANT TON OFFRE",18,TEAL,800,ls=1.5)
g+=f'<rect x="24" y="70" width="552" height="62" rx="16" fill="{TEAL}"/>'+txt(300,110,"Le loyer réaliste",23,WHITE,800)
g+=f'<path d="M300 140 v20 M288 150 l12 12 l12 -12" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'+txt(318,160,"doit couvrir",19,INK,800,anchor="start")
g+=f'<rect x="24" y="176" width="268" height="176" rx="16" fill="{WHITE}"/>'+txt(44,214,"Ta mensualité",21,INK,800,anchor="start")+"".join(txt(44,246+k*28,l,18,INK,600,anchor="start") for k,l in enumerate(["de crédit, assurance","emprunteur comprise"]))
g+=f'<rect x="308" y="176" width="268" height="176" rx="16" fill="{WHITE}"/>'+txt(328,214,"+ Tes charges",21,INK,800,anchor="start")+"".join(txt(328,246+k*27,l,18,INK,600,anchor="start") for k,l in enumerate(["taxe foncière, entretien,","assurance du logement,","charges de copropriété","non récupérables"]))
g+=f'<rect x="24" y="372" width="552" height="62" rx="14" fill="{WHITE}"/>'+check(58,403,TEAL,r=16)+txt(88,410,"Il couvre tout : ton bien tient debout.",20,INK,800,anchor="start")
g+=f'<rect x="24" y="444" width="552" height="88" rx="14" fill="{WHITE}"/>'+cross(58,488,MANGO,r=16)+txt(88,482,"Sinon : renégocie le prix,",20,INK,800,anchor="start")+txt(88,510,"ou passe au bien suivant.",20,INK,600,anchor="start")
out["11-test"]=svg(600,556,g,TEAL_L)

# 12. THIERRY / MARYSE : 3 MOIS D'ARRÊT
def col(x0,kick,title,color,rows,badge,bfill,btxt):
    g=txt(x0+135,72,title,28,color,800)
    for k,(a,b2) in enumerate(rows):
        y=112+k*96
        g+=f'<rect x="{x0}" y="{y}" width="270" height="82" rx="14" fill="{WHITE}"/>'+txt(x0+18,y+33,a,19,INK,800,anchor="start")+txt(x0+18,y+62,b2,20,INK,600,anchor="start",style="font-variant-numeric:tabular-nums")
    g+=f'<rect x="{x0}" y="314" width="270" height="86" rx="16" fill="{bfill}"/>'+txt(x0+135,352,badge[0],28,btxt,800)+txt(x0+135,382,badge[1],19,btxt,700)
    return g
g=(f'<rect x="300" y="0" width="300" height="430" fill="{TEAL_L}"/>'
   + col(16,"","Thierry","#5F6B70",[("Loyers encaissés","3 × 650 € = 1 950 €"),("Crédit et charges","3 × 800 € = 2 400 €")],("− 450 €","sortis de sa poche"),GREY_L,INK)
   + col(314,"","Maryse",TEAL,[("Loyers encaissés","3 × 650 € = 1 950 €"),("Crédit et charges","3 × 600 € = 1 800 €")],("+ 150 €","qui lui restent"),MANGO,INK))
out["12-exemple"]=svg(600,430,g,WHITE)
dest=sys.argv[1]; os.makedirs(dest,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(device_scale_factor=2)
    for name,s in out.items():
        pg.set_content(f'<html><body style="margin:0;background:transparent">{s}</body></html>'); pg.wait_for_timeout(120)
        pg.locator("svg").screenshot(path=f"{dest}/{name}.png", omit_background=True)
    b.close()
print(len(out),"images")

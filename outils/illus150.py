# -*- coding: utf-8 -*-
"""Illustrations du Journal Débrouya #150."""
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
out["06-will"]=will_panel(P["relance"],["Et si on","te disait que","c’est gratuit ?"])
out["09-will-methode"]=will_panel(P["methode"],["Une garantie,","ça marche","si tu suis","ses règles."])
out["17-will-fin"]=will_panel(P["signature"],["C’était Will.","Ciao ! 🔥"],h=330)

# 01. COUVERTURE : un bouclier sur la maison
ban=base64.b64encode(open(sys.argv[2],"rb").read()).decode()
H=560
g=(f'<image href="data:image/jpeg;base64,{ban}" x="0" y="0" width="600" height="229" preserveAspectRatio="xMidYMid slice"/>'
   f'<path d="M0 200 C120 182 240 226 360 206 S540 188 600 204 V{H} H0 Z" fill="{TEAL_M}" opacity="0.55"/>'
   f'<path d="M0 214 C120 196 240 240 360 220 S540 202 600 218 V{H} H0 Z" fill="{TEAL}"/>'
   + txt(300,272,"ÉDITION #150",18,PEACH,800,ls=4)
   + txt(300,320,"Zéro loyer impayé,",38,WHITE,800)
   + txt(300,364,"zéro frais.",34,PEACH,800))
cx,cy=300,452
g+=(f'<polygon points="{cx-54},{cy-6} {cx},{cy-50} {cx+54},{cy-6}" fill="{MANGO}"/>'
    f'<rect x="{cx-44}" y="{cy-8}" width="88" height="62" fill="{WHITE}"/><rect x="{cx-10}" y="{cy+20}" width="20" height="34" fill="{TEAL_M}"/>'
    f'<path d="M{cx+52} {cy-30} q34 6 34 6 q0 40 -34 62 q-34 -22 -34 -62 q0 0 34 -6 z" fill="{PEACH}" stroke="{WHITE}" stroke-width="3"/>'
    f'<path d="M{cx+38} {cy+4} l10 10 l20 -22" fill="none" stroke="{TEAL}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>')
g+=(f'<path d="M0 520 C60 506 120 532 180 520 S300 506 360 520 S480 534 540 520 S600 514 620 520 V{H} H0 Z" fill="{TEAL_D}"/>'
    f'<path d="M0 536 C60 526 120 546 180 536 S300 526 360 536 S480 546 540 536 S600 532 620 536 V{H} H0 Z" fill="#0A403C"/>')
out["01-hero"]=svg(600,H,g,TEAL)

# 02. LE SCÉNARIO : 4 mois
months=[("1er mois",True),("2e mois",True),("3e mois",False),("4e mois",False)]
g=""; y=24
for k,(m,ok) in enumerate(months):
    x=24+k*140
    g+=f'<rect x="{x}" y="{y}" width="128" height="200" rx="16" fill="{WHITE}"/>'+txt(x+64,y+38,m,21,INK,800)
    g+=txt(x+64,y+76,"Loyer",19,INK,600)+(check(x+64,y+110,TEAL,r=20) if ok else cross(x+64,y+110,MANGO,r=20))
    g+=txt(x+64,y+158,"Crédit",19,INK,600)+f'<circle cx="{x+64}" cy="{y+180}" r="9" fill="{TEAL}"/>'
g+=f'<rect x="24" y="{y+216}" width="552" height="84" rx="16" fill="{MANGO}"/>'+txt(300,y+252,"Le loyer s’arrête.",23,WHITE,800)+txt(300,y+282,"Pas ta mensualité.",23,WHITE,800)
out["02-scenario"]=svg(600,y+324,g,MANGO_L)

# 03. TROIS FAÇONS DE TE PROTÉGER
rows=[("Un garant",["Un proche signe pour ton locataire.","Encore faut-il qu’il en ait un solide."],GREY),
      ("Une assurance loyers impayés",["Elle te protège, mais elle coûte","en général 2 à 5 % des loyers de l’année."],GREY),
      ("Visale",["Une caution apportée par un organisme.","C’est elle qu’on va décortiquer."],TEAL)]
g=""; y=24
for k,(t,lines,c) in enumerate(rows):
    h=54+32*len(lines); hl_=(k==2)
    g+=f'<rect x="24" y="{y}" width="552" height="{h}" rx="16" fill="{TEAL if hl_ else WHITE}"/>'
    g+=f'<circle cx="62" cy="{y+h/2}" r="20" fill="{WHITE if hl_ else MANGO}"/>'+txt(62,y+h/2+8,str(k+1),22,TEAL if hl_ else WHITE,800)
    g+=txt(98,y+38,t,23,WHITE if hl_ else INK,800,anchor="start")+"".join(txt(98,y+72+j*32,l,20,WHITE if hl_ else INK,600,anchor="start") for j,l in enumerate(lines))
    y+=h+12
out["03-options"]=svg(600,y+12,g,TEAL_L)

# 05. CE QUE COUVRE VISALE
rows=[("Tes loyers et charges impayés",P["couv1"]),("Les dégradations locatives",P["couv2"]),("Le recouvrement",["Action Logement récupère l’argent","auprès du locataire, pas toi."])]
g=""; y=24
for t,lines in rows:
    h=54+32*len(lines)
    g+=f'<rect x="24" y="{y}" width="552" height="{h}" rx="14" fill="{WHITE}"/>'+check(60,y+h/2,TEAL,r=18)
    g+=txt(94,y+38,t,22,INK,800,anchor="start")+"".join(txt(94,y+72+j*32,l,21,INK,600,anchor="start") for j,l in enumerate(lines))
    y+=h+10
out["05-couverture"]=svg(600,y+14,g,TEAL_L)

# 07. QUI Y A DROIT
rows=P["elig"]
g=""; y=24
for t,lines in rows:
    h=54+32*len(lines)
    g+=f'<rect x="24" y="{y}" width="552" height="{h}" rx="14" fill="{WHITE}"/><rect x="24" y="{y}" width="10" height="{h}" fill="{MANGO}"/>'
    g+=txt(50,y+38,t,22,MANGO_D,800,anchor="start")+"".join(txt(50,y+72+j*32,l,21,INK,600,anchor="start") for j,l in enumerate(lines))
    y+=h+12
out["07-eligibilite"]=svg(600,y+12,g,MANGO_L)

# 10. LE BON ORDRE AVANT LE BAIL
steps=[("Ton locataire demande son visa","sur visale.fr."),("Tu saisis son numéro de visa","et les infos du logement."),("Tu valides le contrat","de cautionnement."),("Et seulement ensuite,","tu signes le bail.")]
g=""; y=24
for k,(a_,b2) in enumerate(steps):
    g+=f'<rect x="24" y="{y}" width="552" height="86" rx="14" fill="{TEAL if k==3 else WHITE}"/><circle cx="64" cy="{y+43}" r="22" fill="{WHITE if k==3 else MANGO}"/>'+txt(64,y+52,str(k+1),23,TEAL if k==3 else WHITE,800)
    g+=txt(102,y+38,a_,22,WHITE if k==3 else INK,800,anchor="start")+txt(102,y+70,b2,21,WHITE if k==3 else INK,600,anchor="start")
    y+=96
out["10-ordre"]=svg(600,y+14,g,MANGO_L)

# 11. LES DÉLAIS EN CAS D'IMPAYÉ
steps=P["delais"]
g=""; y=24
g+=f'<line x1="70" y1="{y+40}" x2="70" y2="{y+40+(len(steps)-1)*104}" stroke="{TEAL_M}" stroke-width="5"/>'
for k,(quand,quoi) in enumerate(steps):
    yy=y+k*104
    g+=f'<circle cx="70" cy="{yy+40}" r="24" fill="{MANGO}"/>'+txt(70,yy+49,str(k+1),23,WHITE,800)
    g+=f'<rect x="112" y="{yy}" width="464" height="88" rx="14" fill="{WHITE}"/>'+txt(132,yy+36,quand,21,MANGO_D,800,anchor="start")+txt(132,yy+68,quoi,21,INK,600,anchor="start")
out["11-delais"]=svg(600,y+len(steps)*104+10,g,TEAL_L)

# 13. EXEMPLE : 3 SCÉNARIOS
rows=[("Sans garantie","2 800 €","de loyers qui manquent dans ta trésorerie.",GREY_L,INK),
      ("Avec une assurance loyers impayés","756 €","de cotisations sur 3 ans, impayé ou pas.",WHITE,INK),
      ("Avec Visale","0 €","de cotisation, et l’impayé est couvert.",TEAL,WHITE)]
g=""; y=24
for t,big,small,fill,col in rows:
    g+=f'<rect x="24" y="{y}" width="552" height="120" rx="16" fill="{fill}"/>'+txt(48,y+40,t,21,col,800,anchor="start")
    g+=txt(48,y+90,big,38,MANGO if fill==WHITE else (PEACH if fill==TEAL else INK),800,anchor="start",style="font-variant-numeric:tabular-nums")
    g+=txt(210,y+78,small.split(" ",3)[0]+" "+small.split(" ",3)[1]+" "+small.split(" ",3)[2],20,col,600,anchor="start")+txt(210,y+104,small.split(" ",3)[3],20,col,600,anchor="start")
    y+=132
out["13-exemple"]=svg(600,y+12,g,MANGO_L)
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

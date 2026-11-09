# -*- coding: utf-8 -*-
"""Illustrations du Journal Débrouya #147 (même charte que la #151)."""
import sys, os, base64, math
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
            + txt(x+w/2,y+31,head,16,WHITE,800,ls=1) + body)
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
    data=base64.b64encode(open(os.path.join(AV,f"will-{pose}.png"),"rb").read()).decode()
    sz=h-20
    t="".join(txt(450, by+44+k*lh, l, size, TEAL if (accent_last and k==n-1) else INK, 800) for k,l in enumerate(lines))
    return svg(600,h,
        f'<image href="data:image/png;base64,{data}" x="-8" y="{h-sz}" width="{sz}" height="{sz}"/>'
        f'<rect x="318" y="{by}" width="264" height="{bh}" rx="28" fill="{WHITE}" stroke="{INK}" stroke-width="3"/>'
        f'<path d="M320 {by+bh/2-14} L284 {by+bh/2+4} L320 {by+bh/2+16}" fill="{WHITE}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
        f'<rect x="316" y="{by+bh/2-12}" width="8" height="26" fill="{WHITE}"/>' + t, TEAL_L)

out={}
out["00-will-salut"]=will_panel("salut",["Salut","la famille ! 🔥"],h=330)
out["05-will"]=will_panel("menton",["Tu vois","le schéma ?"],h=340)
out["10-will-pouce"]=will_panel("pouce",["Une feuille.","Quatre étapes.","Dans l’ordre."])
out["17-will-clin"]=will_panel("clin",["C’était Will 🔥","Ciao !"],h=330)

# 01. COUVERTURE ----------------------------------------------------------------
ban=base64.b64encode(open(sys.argv[2],"rb").read()).decode()
H=540
g=(f'<image href="data:image/jpeg;base64,{ban}" x="0" y="0" width="600" height="229" preserveAspectRatio="xMidYMid slice"/>'
   f'<path d="M0 200 C120 182 240 226 360 206 S540 188 600 204 V{H} H0 Z" fill="{TEAL_M}" opacity="0.55"/>'
   f'<path d="M0 214 C120 196 240 240 360 220 S540 202 600 218 V{H} H0 Z" fill="{TEAL}"/>'
   + txt(300,272,"ÉDITION #147",15,PEACH,800,ls=4)
   + txt(300,320,"À la recherche",40,WHITE,800)
   + txt(300,362,"du bien parfait.",34,PEACH,800))
# loupe sur une maison fantôme
g+=(house(255,452,0.95,WHITE,dash=True)
    + f'<circle cx="352" cy="438" r="44" fill="{TEAL_D}" fill-opacity="0.6" stroke="{MANGO}" stroke-width="9"/>'
    + txt(352,455,"?",46,WHITE,800)
    + f'<line x1="384" y1="470" x2="414" y2="500" stroke="{MANGO}" stroke-width="14" stroke-linecap="round"/>')
g+=(f'<path d="M0 512 C60 498 120 524 180 512 S300 498 360 512 S480 526 540 512 S600 506 620 512 V{H} H0 Z" fill="{TEAL_D}"/>'
    f'<path d="M0 526 C60 516 120 536 180 526 S300 516 360 526 S480 536 540 526 S600 522 620 526 V{H} H0 Z" fill="#0A403C"/>')
out["01-hero"]=svg(600,H,g,TEAL)

# 02. FESTIVAL LYANNAJ -------------------------------------------------------------
g=(txt(300,52,"À NOTER DANS TON AGENDA",15,MANGO,800,ls=3)
   + txt(300,98,"Festival Lyannaj",38,INK,800)
   + f'<rect x="150" y="118" width="300" height="38" rx="19" fill="{TEAL}"/>'
   + txt(300,143,"En live sur Zoom · Gratuit",18,WHITE,800))
days=[("VEN. 20 NOV.","Soirée","immobilier",TEAL),("SAM. 21 NOV.","Soirée","business",TEAL),("DIM. 22 NOV.","Bientôt","dévoilée",MANGO_D)]
for k,(d,a,b,c) in enumerate(days):
    x=24+k*192
    g+=cal(x,184,168,150,d,c, txt(x+84,262,a,22,INK,800)+txt(x+84,290,b,22,INK if k<2 else MANGO_D,800)+rings(x,184,168))
g+=txt(300,372,"En soirée, heure de Paris · Antilles, Hexagone ou ailleurs",16,GREY,700)
out["02-festival"]=svg(600,400,g,MANGO_L)

# 03. LES FAVORIS ---------------------------------------------------------------------
g=(f'<rect x="40" y="34" width="190" height="330" rx="28" fill="{INK}"/><rect x="52" y="58" width="166" height="290" rx="14" fill="{WHITE}"/>'
   f'<rect x="110" y="44" width="50" height="6" rx="3" fill="#3A464C"/>')
for k in range(5):
    y=72+k*54
    g+=(f'<rect x="64" y="{y}" width="58" height="42" rx="8" fill="{TEAL_L}"/>'+house(93,y+24,0.36,TEAL_M)
        + f'<rect x="132" y="{y+8}" width="56" height="8" rx="4" fill="{GREY_L}"/><rect x="132" y="{y+24}" width="38" height="8" rx="4" fill="{GREY_L}"/>'
        + heart(203,y+18,0.9))
rows=[("Dans tes favoris",'10 ? 30 ?',INK,WHITE,320),("Analysés jusqu’au bout","?",INK,TEAL_L,280),("Offres faites","0",WHITE,MANGO,240)]
for k,(lab,val,fg,bg,w) in enumerate(rows):
    y=62+k*100; x=262+(320-w)/2
    g+=(f'<rect x="{x}" y="{y}" width="{w}" height="80" rx="16" fill="{bg}"/>'
        + txt(x+w/2,y+32,lab,18,fg,700) + txt(x+w/2,y+66,val,28,fg,800))
    if k<2: g+=f'<path d="M422 {y+84} l0 10 M414 {y+88} l8 8 l8 -8" stroke="{GREY}" stroke-width="3" fill="none" stroke-linecap="round"/>'
out["03-favoris"]=svg(600,400,g,CREAM)

# 04. CHAQUE BIEN A UN TRUC -------------------------------------------------------------
cards=[("Bien placé","Cuisine à refaire"),("Bon loyer","3e étage sans ascenseur"),("Coche presque tout","« Peut-être mieux le mois prochain »")]
g=txt(300,50,"CHAQUE BIEN A « UN TRUC »",17,TEAL,800,ls=2)
for k,(ok,bad) in enumerate(cards):
    y=74+k*112
    g+=(f'<rect x="24" y="{y}" width="552" height="96" rx="16" fill="{WHITE}"/>'
        f'<rect x="24" y="{y}" width="110" height="96" rx="16" fill="{TEAL_L}"/><rect x="118" y="{y}" width="16" height="96" fill="{TEAL_L}"/>'
        + house(79,y+48,0.7,TEAL)
        + check(162,y+30)+txt(186,y+37,ok,20,INK,700,anchor="start")
        + cross(162,y+68)+txt(186,y+75,bad,20,INK,700,anchor="start"))
g+=txt(300,436,"Et le mois prochain, tu recommences.",19,GREY,700)
out["04-un-truc"]=svg(600,462,g,GREY_L)

# 06. LE BIEN PARFAIT N'EXISTE PAS ---------------------------------------------------------
crit=["Vue dégagée","Prix bas","Loyer haut","Zéro travaux","Bien placé","Calme","Parking"]
g=(f'<rect x="34" y="34" width="250" height="356" rx="16" fill="{WHITE}"/>'
   + txt(159,72,"Ma liste du bien idéal",19,TEAL,800))
for k,c in enumerate(crit):
    y=106+k*40
    g+=check(66,y,TEAL,12)+txt(88,y+6,c,18,INK,700,anchor="start")
g+=(house(440,170,1.75,TEAL,dash=True)
    + f'<g transform="rotate(-10 440 300)"><rect x="330" y="270" width="220" height="62" rx="10" fill="none" stroke="{MANGO}" stroke-width="5"/>'
    + txt(440,311,"N’EXISTE PAS",28,MANGO,800,ls=1) + '</g>')
out["06-parfait"]=svg(600,420,g,TEAL_L)

# 07. LE SEUIL (Herbert Simon) -----------------------------------------------------------
g=(txt(300,46,"LA MÉTHODE DU SEUIL",16,TEAL,800,ls=2)
   + txt(300,76,"Herbert Simon · prix Nobel d’économie 1978",17,GREY,700))
hs=[90,115,165,135,185]; base=380; seuil=150
for k,h in enumerate(hs):
    x=70+k*96; ok=h>=seuil; first=(k==2)
    fill = MANGO if first else (TEAL_M if ok else GREY_L)
    g+=f'<rect x="{x}" y="{base-h}" width="70" height="{h}" rx="10" fill="{fill}"/>'
    g+=house(x+35,base-h-26,0.42,MANGO if first else GREY)
g+=(f'<line x1="44" y1="{base-seuil}" x2="556" y2="{base-seuil}" stroke="{INK}" stroke-width="4" stroke-dasharray="12 8"/>'
    + f'<rect x="44" y="{base-seuil-40}" width="132" height="30" rx="15" fill="{INK}"/>' + txt(110,base-seuil-19,"TON SEUIL",15,WHITE,800,ls=1)
    + txt(70+2*96+35,base+34,"Choisi ✓",19,MANGO_D,800)
    + txt(300,base+72,"« Satisficing » = satisfaire + suffire",20,INK,800))
out["07-seuil"]=svg(600,480,g,WHITE)

# 08. MAXIMISATEURS vs SATISFICEURS ---------------------------------------------------------
def colm(x0,title,sub,color,bg,items,mark):
    g=(f'<rect x="{x0}" y="70" width="268" height="300" rx="18" fill="{bg}"/>'
       + txt(x0+134,112,title,24,color,800) + txt(x0+134,140,sub,16,INK,700))
    for k,(a,b) in enumerate(items):
        y=192+k*62
        g+=mark(x0+34,y-6)+txt(x0+58,y,a,19,INK,700,anchor="start")+(txt(x0+58,y+23,b,19,INK,700,anchor="start") if b else "")
    return g
g=(txt(300,44,"CE QU’ONT MESURÉ LES CHERCHEURS",15,TEAL,800,ls=2)
   + colm(22,"Maximisateurs","veulent LA meilleure option",GREY,GREY_L,[("Moins heureux",""),("Moins satisfaits","de leur vie"),("Plus de regrets","")],lambda x,y:cross(x,y,GREY))
   + colm(310,"Satisficeurs","choisissent l’« assez bon »",TEAL,TEAL_L,[("Critères fixés",""),("Décident",""),("Vivent mieux","leurs choix")],lambda x,y:check(x,y)))
g+=txt(300,398,"Barry Schwartz et son équipe, 2002",15,GREY,700)
out["08-max-sat"]=svg(600,420,g,WHITE)

# 11. LES 4 MARCHES ---------------------------------------------------------------------------
g=txt(300,46,"TA MÉTHODE EN 4 ÉTAPES",17,TEAL,800,ls=3)
labels=[("3 critères",""),("Deux","colonnes"),("Règle de","décision"),("Stop au","bien rêvé")]
base=372
for k,(l1,l2) in enumerate(labels):
    hgt=[100,150,200,250][k]; x=26+k*140; y=base-hgt; fill=MANGO if k==3 else TEAL
    g+=f'<rect x="{x}" y="{y}" width="128" height="{hgt+30}" rx="14" fill="{fill}"/>'
    g+=f'<circle cx="{x+64}" cy="{y}" r="24" fill="{WHITE}" stroke="{fill}" stroke-width="5"/>'+txt(x+64,y+9,str(k+1),24,INK,800)
    g+= (txt(x+64,y+58,l1,20,WHITE,800)+txt(x+64,y+84,l2,20,WHITE,800)) if l2 else txt(x+64,y+64,l1,20,WHITE,800)
g+=f'<line x1="530" y1="122" x2="530" y2="62" stroke="{INK}" stroke-width="5" stroke-linecap="round"/><path d="M532 62 L574 76 L532 90 Z" fill="{MANGO}"/>'
out["11-marches"]=svg(600,400,g,TEAL_L)

# 12. LES 3 NON-NÉGOCIABLES ------------------------------------------------------------------
def coin(cx,cy): return f'<circle cx="{cx}" cy="{cy}" r="26" fill="{TEAL}"/>'+txt(cx,cy+10,"€",28,WHITE,800)
def chart(cx,cy): return "".join(f'<rect x="{cx-24+k*18}" y="{cy+20-hh}" width="12" height="{hh}" rx="3" fill="{TEAL}"/>' for k,hh in enumerate([16,28,42]))
def pin(cx,cy): return f'<path d="M{cx} {cy+28} C{cx-26} {cy} {cx-22} {cy-26} {cx} {cy-26} C{cx+22} {cy-26} {cx+26} {cy} {cx} {cy+28} Z" fill="{TEAL}"/><circle cx="{cx}" cy="{cy-6}" r="9" fill="{WHITE}"/>'
cards=[(coin,"Budget max","frais compris"),(chart,"Rentabilité","mini, après charges"),(pin,"La zone","et pourquoi elle")]
g=txt(300,46,"MES 3 NON-NÉGOCIABLES",17,TEAL,800,ls=2)
for k,(ic,a,b) in enumerate(cards):
    x=24+k*192
    g+=(f'<rect x="{x}" y="70" width="168" height="190" rx="16" fill="{WHITE}" stroke="{TEAL}" stroke-width="3"/>'
        + ic(x+84,128) + txt(x+84,198,a,21,INK,800) + txt(x+84,226,b,16,GREY,700))
g+=txt(300,300,"Tout le reste, c’est du bonus :",18,INK,700)
for k,c in enumerate(["la vue","le carrelage","l’étage"]):
    x=96+k*140
    g+=f'<rect x="{x}" y="318" width="128" height="38" rx="19" fill="{GREY_L}"/>'+txt(x+64,343,c,17,GREY,700)
out["12-criteres"]=svg(600,384,g,TEAL_L)

# 13. DEUX COLONNES ---------------------------------------------------------------------------
def col2(x0,title,sub,col,bg,items,mark):
    g=(f'<rect x="{x0}" y="30" width="268" height="330" rx="18" fill="{bg}"/>'
       f'<rect x="{x0}" y="30" width="268" height="62" rx="18" fill="{col}"/><rect x="{x0}" y="70" width="268" height="22" fill="{col}"/>'
       + txt(x0+134,70,title,22,WHITE,800,ls=1))
    for k,(a,b) in enumerate(items):
        y=136+k*60
        g+=mark(x0+36,y-6)+txt(x0+60,y,a,19,INK,700,anchor="start")+(txt(x0+60,y+23,b,19,INK,700,anchor="start") if b else "")
    g+=txt(x0+134,334,sub,17,col,800)
    return g
def wrench(cx,cy): return f'<circle cx="{cx}" cy="{cy}" r="13" fill="{TEAL}"/><path d="M{cx-5} {cy+5} l8 -8" stroke="{WHITE}" stroke-width="4" stroke-linecap="round"/><circle cx="{cx+4}" cy="{cy-4}" r="3.5" fill="{WHITE}"/>'
def lock(cx,cy): return f'<circle cx="{cx}" cy="{cy}" r="13" fill="{MANGO}"/><rect x="{cx-5}" y="{cy-2}" width="10" height="8" rx="2" fill="{WHITE}"/><path d="M{cx-3} {cy-2} v-3 a3 3 0 0 1 6 0 v3" stroke="{WHITE}" stroke-width="2" fill="none"/>'
g=(col2(22,"RÉPARABLE","Ça se chiffre",TEAL,WHITE,[("Cuisine datée",""),("Peinture fatiguée",""),("Salle de bain","à refaire")],wrench)
   + col2(310,"DÉFINITIF","Aucun chantier ne le change",MANGO_D,WHITE,[("L’emplacement",""),("Le bruit de la route",""),("L’exposition","")],lock))
# retire les icônes des lignes de continuation
for x0,ic in [(22,wrench),(310,lock)]:
    pass
out["13-colonnes"]=svg(600,390,g,GREY_L)

# 14. LA RÈGLE DE DÉCISION ----------------------------------------------------------------------
def box(x,y,w,h,t1,t2,fill,fg):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}"/>'+txt(x+w/2,y+h/2-4,t1,19,fg,800)+txt(x+w/2,y+h/2+20,t2,19,fg,800)
def arrow(x1,y1,x2,y2):
    a=math.atan2(y2-y1,x2-x1);
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
            f'<path d="M{x2-12*math.cos(a-0.5):.1f} {y2-12*math.sin(a-0.5):.1f} L{x2} {y2} L{x2-12*math.cos(a+0.5):.1f} {y2-12*math.sin(a+0.5):.1f}" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
g=(box(150,28,300,72,"Le bien passe","mes 3 critères ?",WHITE,INK) + arrow(300,104,300,140)
   + box(150,144,300,72,"Je l’analyse en entier","dans la semaine",TEAL,WHITE)
   + arrow(250,220,160,262) + arrow(350,220,440,262)
   + box(28,266,260,72,"Je fais","une offre",MANGO,WHITE) + box(312,266,260,72,"J’écris pourquoi","je n’en fais pas",WHITE,INK)
   + txt(300,376,"Chaque bien qui mérite ton attention reçoit une réponse.",16,GREY,700))
out["14-regle"]=svg(600,400,g,TEAL_L)

# 15. RÉEL vs IMAGINAIRE ---------------------------------------------------------------------------
g=(txt(150,52,"LE BIEN RÉEL",16,TEAL,800,ls=2) + txt(450,52,"LE BIEN IMAGINAIRE",16,MANGO_D,800,ls=2)
   + f'<line x1="300" y1="30" x2="300" y2="350" stroke="{GREY_L}" stroke-width="3"/>'
   + house(150,150,1.5,TEAL)
   + f'<rect x="196" y="96" width="78" height="34" rx="8" fill="{MANGO}"/>' + txt(235,119,"Prix",17,WHITE,800)
   + txt(150,262,"Un prix, des défauts,",19,INK,700) + txt(150,288,"des chiffres.",19,INK,700)
   + house(450,150,1.5,GREY,dash=True)
   + txt(450,142,"?",40,GREY,800)
   + txt(450,262,"Ni prix, ni défaut,",19,INK,700) + txt(450,288,"ni travaux.",19,INK,700)
   + f'<rect x="120" y="318" width="360" height="40" rx="20" fill="{INK}"/>' + txt(300,345,"Le bien imaginaire gagne toujours.",17,WHITE,800))
out["15-imaginaire"]=svg(600,384,g,WHITE)

# 16. LUDOVIC AVANT / APRÈS ----------------------------------------------------------------------
def colL(x0,title,color,rows,badge,bfill,btxt):
    g=(f'<circle cx="{x0+40}" cy="66" r="18" fill="{color}"/><rect x="{x0+16}" y="88" width="48" height="30" rx="15" fill="{color}"/>'
       + txt(x0+78,82,title[0],15,color,800,anchor="start",ls=2) + txt(x0+78,108,title[1],22,color,800,anchor="start"))
    g+=f'<line x1="{x0+24}" y1="160" x2="{x0+24}" y2="{150+96*3}" stroke="{color}" stroke-width="4"/>'
    for k,(t1,t2) in enumerate(rows):
        y=150+k*96
        g+=f'<circle cx="{x0+24}" cy="{y+10}" r="10" fill="{color}"/>'+txt(x0+46,y+18,t1,20,INK,800,anchor="start")+txt(x0+46,y+46,t2,19,INK,600,anchor="start")
    g+=f'<rect x="{x0}" y="540" width="270" height="78" rx="16" fill="{bfill}"/>'+txt(x0+135,573,badge[0],20,btxt,800)+txt(x0+135,601,badge[1],20,btxt,800)
    return g
g=(f'<rect x="300" y="0" width="300" height="650" fill="{TEAL_L}"/>'
   + colL(18,("AVANT","Bien parfait"),GREY,[("18 mois","de recherche"),("~10 visites","« pas exceptionnel »"),("Aucune offre","toujours un défaut"),("Comparé à un","bien imaginaire")],("Toujours en","recherche"),GREY_L,INK)
   + colL(312,("APRÈS","Critères écrits"),TEAL,[("3 critères","budget, renta, zone"),("Favoris triés","il en reste 2"),("Colonne 1 / 2","un chiffré, un écarté"),("1 semaine","après…")],("1re offre","faite"),MANGO,INK))
out["16-ludovic"]=svg(600,650,g,WHITE)

dest=sys.argv[1]; os.makedirs(dest,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(device_scale_factor=2)
    for name,s in out.items():
        pg.set_content(f'<html><body style="margin:0;background:transparent">{s}</body></html>'); pg.wait_for_timeout(120)
        pg.locator("svg").screenshot(path=f"{dest}/{name}.png", omit_background=True)
    b.close()
print(len(out),"images")

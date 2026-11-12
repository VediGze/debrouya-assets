# -*- coding: utf-8 -*-
"""Illustrations du Journal Débrouya #147 (même charte que la #151)."""
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
P=__import__("json").loads(sys.argv[3])
out["00-will-salut"]=will_panel(P["accueil"],["Salut","la famille ! 🔥"],h=330)
out["06-will"]=will_panel(P["relance"],["Tu vois où","je veux en","venir ?"])
out["09-will-methode"]=will_panel(P["methode"],["Une lettre.","Deux dates.","Et c’est toi","qui décides."])
out["17-will-fin"]=will_panel(P["signature"],["C’était Will 🔥","Ciao !"],h=330)

DPE=[("A","#2E8B57"),("B","#4FA65A"),("C","#9BC23C"),("D","#F2D33A"),("E","#F2A33A"),("F","#E57638"),("G","#D9482B")]
def dpe_scale(x0,y0,w=300,h=34,gap=8,hl=None,label=None,fs=20):
    g=""
    for k,(l,c) in enumerate(DPE):
        y=y0+k*(h+gap); ww=w*0.45+w*0.55*k/6
        g+=f'<path d="M{x0} {y} h{ww-14} l14 {h/2} l-14 {h/2} h-{ww-14} z" fill="{c}"/>'+txt(x0+16,y+h/2+fs*0.36,l,fs,WHITE,800,anchor="start")
        if hl and l in hl:
            g+=f'<path d="M{x0+ww+14} {y+h/2} l18 -12 v24 z" fill="{INK}"/>'+txt(x0+ww+42,y+h/2+7,hl[l],18,INK,800,anchor="start")
    return g

# 01. COUVERTURE
ban=base64.b64encode(open(sys.argv[2],"rb").read()).decode()
H=540
g=(f'<image href="data:image/jpeg;base64,{ban}" x="0" y="0" width="600" height="229" preserveAspectRatio="xMidYMid slice"/>'
   f'<path d="M0 200 C120 182 240 226 360 206 S540 188 600 204 V{H} H0 Z" fill="{TEAL_M}" opacity="0.55"/>'
   f'<path d="M0 214 C120 196 240 240 360 220 S540 202 600 218 V{H} H0 Z" fill="{TEAL}"/>'
   + txt(300,272,"ÉDITION #148",15,PEACH,800,ls=4)
   + txt(300,320,"Chronique d’une",38,WHITE,800)
   + txt(300,362,"interdiction annoncée.",32,PEACH,800))
for k,(l,c) in enumerate(DPE):
    x=96+k*58
    g+=f'<rect x="{x}" y="398" width="50" height="62" rx="10" fill="{c}"/>'+txt(x+25,440,l,30,WHITE,800)
g+=f'<rect x="{96+6*58-6}" y="392" width="62" height="74" rx="13" fill="none" stroke="{WHITE}" stroke-width="5"/>'
g+=(f'<path d="M0 512 C60 498 120 524 180 512 S300 498 360 512 S480 526 540 512 S600 506 620 512 V{H} H0 Z" fill="{TEAL_D}"/>'
    f'<path d="M0 526 C60 516 120 536 180 526 S300 516 360 526 S480 536 540 526 S600 522 620 526 V{H} H0 Z" fill="#0A403C"/>')
out["01-hero"]=svg(600,H,g,TEAL)

# 02. RÉSULTAT DU VOTE
oui,non=P["oui"],P["non"]; pc=round(100*oui/(oui+non))
g=(txt(300,50,"TU AS VOTÉ POUR LE NOUVEAU FORMAT",16,TEAL,800,ls=2)
   + txt(300,140,f"{pc} %",84,MANGO,800) + txt(300,186,"de « oui, j’adore »",24,INK,800)
   + f'<rect x="60" y="216" width="480" height="30" rx="15" fill="{GREY_L}"/>'
   + f'<rect x="60" y="216" width="{480*pc/100:.0f}" height="30" rx="15" fill="{TEAL}"/>'
   + txt(300,286,"Merci à toutes celles et ceux qui ont voté ❤",19,INK,700))
out["02-vote"]=svg(600,316,g,MANGO_L)

# 03. FESTIVAL LYANNAJ
g=(txt(300,46,"LYANNAJ FEST LIVE",15,MANGO,800,ls=4) + txt(300,92,"3 soirées en live, gratuites",30,INK,800)
   + f'<rect x="96" y="112" width="408" height="38" rx="19" fill="{TEAL}"/>' + txt(300,138,"19 h – 23 h Paris · 14 h Antilles · 15 h Guyane",16,WHITE,800))
days=[("VEN. 20 NOV.","Soirée","immobilier",TEAL,INK),("SAM. 21 NOV.","Soirée","business",TEAL,INK),("DIM. 22 NOV.","Soirée","VIP",MANGO_D,MANGO_D)]
for k,(d,a,b,c,fc) in enumerate(days):
    x=24+k*192
    g+=cal(x,176,168,150,d,c, txt(x+84,256,a,22,INK,800)+txt(x+84,284,b,22,fc,800)+rings(x,176,168))
g+=txt(300,360,"La soirée VIP est réservée aux inscrits des deux premières.",15,GREY,700)
out["03-festival"]=svg(600,384,g,MANGO_L)

# 04. CE QUI T'ATTEND
items=[("Will et les coachs","immobilier et business"),("Des experts","financement, aides, IA"),("Environ 100","témoignages en direct"),("Remise des diplômes","le vendredi 20 novembre"),("Tes questions","en direct dans le chat")]
g=txt(300,46,"CE QUI T’ATTEND",16,TEAL,800,ls=3)
for k,(a,b) in enumerate(items):
    y=74+k*66
    g+=(f'<rect x="40" y="{y}" width="520" height="56" rx="14" fill="{WHITE}"/>'+check(74,y+28)
        +txt(102,y+25,a,19,INK,800,anchor="start")+txt(102,y+47,b,17,GREY,700,anchor="start"))
out["04-programme"]=svg(600,422,g,TEAL_L)

# 05. CALENDRIER HEXAGONE vs ANTILLES
g=txt(300,46,"LOUER UNE PASSOIRE : LE CALENDRIER",16,TEAL,800,ls=2)
def lane(y,title,col,marks):
    s=txt(40,y,title,20,col,800,anchor="start")+f'<line x1="60" y1="{y+46}" x2="560" y2="{y+46}" stroke="{GREY_L}" stroke-width="8" stroke-linecap="round"/>'
    for yr,lab,c in marks:
        x=60+(yr-2024)*500/10
        s+=f'<circle cx="{x}" cy="{y+46}" r="16" fill="{c}"/>'+txt(x,y+53,lab,17,WHITE,800)+txt(x,y+90,str(yr),18,INK,800)
    return s
g+=lane(86,"Hexagone",GREY,[(2025,"G","#D9482B"),(2028,"F","#E57638"),(2034,"E","#F2A33A")])
g+=f'<rect x="20" y="200" width="560" height="140" rx="16" fill="{WHITE}"/>'
g+=lane(226,"Guadeloupe et Martinique",TEAL,[(2028,"G","#D9482B"),(2031,"F","#E57638")])
g+=txt(300,376,"Après ces dates, ces logements ne sont plus « décents » pour être loués.",15,GREY,700)
out["05-calendrier"]=svg(600,400,g,TEAL_L)

# 07. LE BAIL SIGNÉ CETTE ANNÉE
g=txt(300,46,"UN BAIL VIDE DE 3 ANS SIGNÉ EN 2026",16,TEAL,800,ls=2)
x0=50; sc=500/5  # 2026..2031
def X(y): return x0+(y-2026)*sc
g+=f'<line x1="{x0}" y1="190" x2="{x0+500}" y2="190" stroke="{GREY_L}" stroke-width="6"/>'
for yr in range(2026,2032): g+=f'<line x1="{X(yr)}" y1="180" x2="{X(yr)}" y2="200" stroke="{GREY}" stroke-width="3"/>'+txt(X(yr),226,str(yr),16,GREY,700)
g+=f'<rect x="{X(2026.08)}" y="104" width="{X(2029.08)-X(2026.08)}" height="48" rx="12" fill="{TEAL}"/>'+txt((X(2026.08)+X(2028))/2,135,"Ton bail",19,WHITE,800)+txt((X(2028)+X(2029.08))/2,135,"→ 2029",17,WHITE,800)
g+=f'<line x1="{X(2028)}" y1="80" x2="{X(2028)}" y2="200" stroke="#D9482B" stroke-width="5" stroke-dasharray="8 6"/>'
g+=f'<rect x="{X(2028)-82}" y="250" width="164" height="56" rx="12" fill="#D9482B"/>'+txt(X(2028),274,"1er janv. 2028",17,WHITE,800)+txt(X(2028),296,"G interdit",17,WHITE,800)
g+=f'<line x1="{X(2028)}" y1="200" x2="{X(2028)}" y2="250" stroke="#D9482B" stroke-width="3"/>'
g+=txt(300,346,"La date limite tombe pendant ce bail-ci.",19,INK,800)
out["07-bail"]=svg(600,372,g,WHITE)

# 08. OÙ EN EST LE PROJET DE LOI
steps=[("Sénat","adopté le 8 juillet 2026",TEAL,"✓"),("Assemblée","encore en discussion",MANGO,"…"),("Loi votée","pas encore",GREY,"?")]
g=txt(300,46,"LE PROJET DE LOI « RELANCE LOGEMENT »",16,TEAL,800,ls=1)
for k,(a,b,c,m) in enumerate(steps):
    x=100+k*200
    if k<2: g+=f'<line x1="{x+36}" y1="120" x2="{x+164}" y2="120" stroke="{GREY_L}" stroke-width="6"/>'
    g+=f'<circle cx="{x}" cy="120" r="34" fill="{c}"/>'+txt(x,132,m,32,WHITE,800)+txt(x,190,a,20,INK,800)+txt(x,216,b,15,GREY,700)
g+=(f'<rect x="40" y="250" width="520" height="64" rx="14" fill="{WHITE}" stroke="{MANGO}" stroke-width="3"/>'
    + txt(300,278,"Tant qu’il n’est pas voté et promulgué,",18,INK,800)+txt(300,302,"c’est la loi actuelle qui s’applique.",18,INK,800))
out["08-projet"]=svg(600,340,g,MANGO_L)

# 10. LES 4 MARCHES
g=""
labels=[("Ton DPE",""),("Ton compte","à rebours"),("Ce qui fait","bouger la","lettre"),("Si tu","achètes")]
base=372
for k,lab in enumerate(labels):
    hgt=[100,150,200,250][k]; x=26+k*140; y=base-hgt; fill=MANGO if k==3 else TEAL
    g+=f'<rect x="{x}" y="{y}" width="128" height="{hgt+30}" rx="14" fill="{fill}"/>'
    g+=f'<circle cx="{x+64}" cy="{y}" r="24" fill="{WHITE}" stroke="{fill}" stroke-width="5"/>'+txt(x+64,y+9,str(k+1),24,INK,800)
    g+="".join(txt(x+64,y+58+n*26,t,20,WHITE,800) for n,t in enumerate([t for t in lab if t]))
g+=f'<line x1="530" y1="122" x2="530" y2="62" stroke="{INK}" stroke-width="5" stroke-linecap="round"/><path d="M532 62 L574 76 L532 90 Z" fill="{MANGO}"/>'
out["10-marches"]=svg(600,400,f'<g transform="translate(0 -24)">{g}</g>',TEAL_L)

# 11. TON DPE : 3 CHOSES À NOTER
g=(f'<rect x="40" y="30" width="250" height="320" rx="12" fill="{WHITE}"/>'+txt(165,66,"Diagnostic de",16,GREY,700)+txt(165,88,"performance énergétique",16,GREY,700)
   + dpe_scale(66,108,190,26,6,fs=16))
notes=[("La classe","la lettre"),("La date","du diagnostic"),("La validité","10 ans")]
for k,(a,b) in enumerate(notes):
    y=70+k*94
    g+=(f'<rect x="312" y="{y}" width="256" height="78" rx="14" fill="{TEAL}"/>'
        + f'<circle cx="346" cy="{y+39}" r="18" fill="{WHITE}"/>'+txt(346,y+46,str(k+1),18,TEAL,800)
        + txt(378,y+34,a,20,WHITE,800,anchor="start")+txt(378,y+60,b,18,PEACH,700,anchor="start"))
out["11-dpe"]=svg(600,380,g,TEAL_L)

# 12. DEUX DATES CÔTE À CÔTE
g=(txt(300,46,"POUR CHAQUE BIEN, DEUX DATES",16,TEAL,800,ls=2)
   + f'<rect x="24" y="76" width="268" height="150" rx="18" fill="{WHITE}"/>'+txt(158,116,"L’échéance",22,INK,800)+txt(158,144,"de ton bail",22,INK,800)+txt(158,172,"en cours",22,INK,800)
   + f'<rect x="308" y="76" width="268" height="150" rx="18" fill="{WHITE}"/>'+txt(442,116,"La date limite",22,INK,800)+txt(442,144,"de ta classe",22,INK,800)
   + f'<rect x="330" y="166" width="104" height="40" rx="10" fill="#D9482B"/>'+txt(382,193,"G : 2028",17,WHITE,800)
   + f'<rect x="446" y="166" width="104" height="40" rx="10" fill="#E57638"/>'+txt(498,193,"F : 2031",17,WHITE,800)
   + f'<rect x="60" y="250" width="480" height="66" rx="16" fill="{MANGO}"/>'+txt(300,278,"Échéance après la date limite ?",19,INK,800)+txt(300,304,"Le sujet tombe pendant ce bail-ci.",18,INK,700))
out["12-dates"]=svg(600,340,g,TEAL_L)

# 13. AVANT / APRÈS
def colL(x0,title,color,rows,badge,bfill,btxt):
    g=(txt(x0+135,52,title[0],15,color,800,ls=2)+txt(x0+135,80,title[1],21,color,800))
    g+=f'<line x1="{x0+24}" y1="120" x2="{x0+24}" y2="{110+96*3}" stroke="{color}" stroke-width="4"/>'
    for k,(t1,t2) in enumerate(rows):
        y=110+k*96
        g+=f'<circle cx="{x0+24}" cy="{y+10}" r="10" fill="{color}"/>'+txt(x0+46,y+18,t1,19,INK,800,anchor="start")+txt(x0+46,y+44,t2,18,INK,600,anchor="start")
    g+=f'<rect x="{x0}" y="500" width="270" height="80" rx="16" fill="{bfill}"/>'+txt(x0+135,534,badge[0],22,btxt,800)+txt(x0+135,562,badge[1],17,btxt,700)
    return g
g=(f'<rect x="300" y="0" width="300" height="610" fill="{TEAL_L}"/>'
   + colL(18,("AVANT","Rien d’anticipé"),GREY,[("Février 2029","impossible de relouer"),("Logement vide","à chercher des artisans"),("5 mois","sans locataire"),("× 750 €","de loyer")],("3 750 €","de loyers perdus"),GREY_L,INK)
   + colL(312,("APRÈS","Compte à rebours"),TEAL,[("Pendant le bail","DPE et devis"),("Au départ","chantier tout de suite"),("2 mois","sans locataire"),("× 750 €","de loyer")],("1 500 €","de loyers perdus"),MANGO,INK))
out["13-exemple"]=svg(600,610,g,WHITE)
dest=sys.argv[1]; os.makedirs(dest,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(device_scale_factor=2)
    for name,s in out.items():
        pg.set_content(f'<html><body style="margin:0;background:transparent">{s}</body></html>'); pg.wait_for_timeout(120)
        pg.locator("svg").screenshot(path=f"{dest}/{name}.png", omit_background=True)
    b.close()
print(len(out),"images")

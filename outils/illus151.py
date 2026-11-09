# -*- coding: utf-8 -*-
"""Illustrations de la #151 (SVG -> PNG 2x). Palette stricte : teal + mangue + neutres."""
import sys, os
from playwright.sync_api import sync_playwright

INK="#1E2A2F"; TEAL="#136D68"; TEAL_D="#0D524E"; TEAL_L="#DDEFEC"; TEAL_M="#8CC5C0"
MANGO="#E57638"; MANGO_D="#C65F25"; MANGO_L="#FDEADB"; CREAM="#FBF5EC"
GREY="#8E989C"; GREY_L="#E9E3D9"; WHITE="#FFFFFF"
F="font-family:Inter,Arial,sans-serif"

def txt(x,y,s,size=18,fill=INK,w=700,anchor="middle",ls=0,style=""):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" style="{F};font-size:{size}px;font-weight:{w};letter-spacing:{ls}px;{style}" fill="{fill}">{s}</text>'

def svg(w,h,inner,bg=None,clip=True):
    cp = f'<clipPath id="c"><rect width="{w}" height="{h}" rx="22"/></clipPath>'
    b = f'<rect width="{w}" height="{h}" rx="22" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs>{cp}</defs><g clip-path="url(#c)">{b}{inner}</g></svg>'

def rings(x,y,w,color=GREY_L):
    return "".join(f'<circle cx="{x+w*k/4}" cy="{y}" r="6" fill="{color}"/>' for k in (1,2,3))

def cal(x,y,w,h,head,headfill,body="",rot=0):
    g=(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{WHITE}"/>'
       f'<path d="M{x} {y+14} a14 14 0 0 1 14 -14 h{w-28} a14 14 0 0 1 14 14 v30 h-{w} z" fill="{headfill}"/>'
       + txt(x+w/2,y+31,head,17,WHITE,800,ls=1) + body)
    if rot: g=f'<g transform="rotate({rot} {x+w/2} {y+h/2})">{g}</g>'
    return g

out = {}

# 1. HERO --------------------------------------------------------------
palm = (f'<path d="M0 372 C60 352 120 392 180 372 S300 352 360 372 S480 392 540 372 S600 362 620 372 V420 H0 Z" fill="{TEAL_D}"/>'
        f'<path d="M0 396 C60 380 120 412 180 396 S300 380 360 396 S480 412 540 396 S600 388 620 396 V420 H0 Z" fill="#0A403C"/>')
hero = (palm +
  f'<circle cx="528" cy="78" r="40" fill="{MANGO}"/>' +
  txt(300,58,"ÉDITION #151",15,"#FFD3AE",800,ls=4) +
  txt(300,118,"Ton année 2027",42,WHITE,800) +
  txt(300,164,"commence maintenant.",34,"#FFD3AE",800) +
  cal(130,200,155,150,"NOV. 2026",TEAL_D, txt(207.5,286,"Tu prépares",22,INK,800) + rings(130,200,155)) +
  cal(315,200,155,150,"JANV. 2027",MANGO_D, txt(392.5,286,"Tu es prêt",22,INK,800) + rings(315,200,155)) +
  f'<path d="M288 270 C295 258 303 258 309 268" stroke="{MANGO}" stroke-width="5" fill="none" stroke-linecap="round"/>'
  f'<path d="M300 262 l9 8 l-12 3" stroke="{MANGO}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
out["01-hero"] = svg(600,410,hero,TEAL)

# 2. 1er JANVIER -------------------------------------------------------
def burst(cx,cy,r,col,n=10):
    import math
    return "".join(f'<line x1="{cx+r*0.45*math.cos(2*math.pi*k/n):.1f}" y1="{cy+r*0.45*math.sin(2*math.pi*k/n):.1f}" x2="{cx+r*math.cos(2*math.pi*k/n):.1f}" y2="{cy+r*math.sin(2*math.pi*k/n):.1f}" stroke="{col}" stroke-width="4" stroke-linecap="round"/>' for k in range(n))
jan = (burst(70,58,34,MANGO)+burst(232,42,24,TEAL_M,8)+burst(560,300,22,MANGO,8) +
  cal(40,82,190,210,"JANVIER",TEAL, txt(135,236,"1",110,INK,800) + rings(40,82,190)) +
  f'<rect x="262" y="66" width="306" height="196" rx="26" fill="{WHITE}" stroke="{INK}" stroke-width="3"/>'
  f'<path d="M264 168 L240 186 L266 196" fill="{WHITE}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
  f'<rect x="262" y="170" width="8" height="24" fill="{WHITE}"/>' +
  txt(415,116,"« Cette année,",25,INK,700,style="font-style:italic") +
  txt(415,148,"c’est la bonne.",25,INK,700,style="font-style:italic") +
  txt(415,190,"Cette année,",25,TEAL,800,style="font-style:italic") +
  txt(415,222,"j’investis. »",25,TEAL,800,style="font-style:italic") +
  txt(300,336,"La phrase qu’on se répète chaque 1er janvier",20,GREY,700))
out["02-janvier"] = svg(600,360,jan,MANGO_L)

# 3. LE PROJET QUI GLISSE ---------------------------------------------
def briefcase(cx,cy):
    return (f'<rect x="{cx-14}" y="{cy-30}" width="28" height="16" rx="6" fill="none" stroke="{TEAL}" stroke-width="5"/>'
            f'<rect x="{cx-32}" y="{cy-18}" width="64" height="44" rx="8" fill="{TEAL}"/>'
            f'<rect x="{cx-32}" y="{cy-2}" width="64" height="4" fill="{TEAL_D}"/>')
def mask(cx,cy):
    return (f'<path d="M{cx+20} {cy-22} C{cx+34} {cy-46} {cx+46} {cy-46} {cx+52} {cy-40} C{cx+40} {cy-36} {cx+32} {cy-30} {cx+26} {cy-18}" fill="{MANGO}"/>'
            f'<path d="M{cx-40} {cy-8} Q{cx-40} {cy-28} {cx-18} {cy-24} Q{cx} {cy-20} {cx+18} {cy-24} Q{cx+40} {cy-28} {cx+40} {cy-8} Q{cx+38} {cy+20} {cx+14} {cy+16} Q{cx} {cy+6} {cx-14} {cy+16} Q{cx-38} {cy+20} {cx-40} {cy-8} Z" fill="{TEAL}"/>'
            f'<ellipse cx="{cx-17}" cy="{cy-6}" rx="9" ry="6" fill="{WHITE}"/><ellipse cx="{cx+17}" cy="{cy-6}" rx="9" ry="6" fill="{WHITE}"/>')
def bank(cx,cy):
    cols="".join(f'<rect x="{cx-30+k*22}" y="{cy-8}" width="10" height="30" fill="{TEAL}"/>' for k in range(3))
    return (f'<polygon points="{cx-40},{cy-12} {cx},{cy-38} {cx+40},{cy-12}" fill="{TEAL}"/>' + cols +
            f'<rect x="{cx-42}" y="{cy+24}" width="84" height="8" rx="2" fill="{TEAL}"/>')
cards=[("JANVIER",briefcase,"Retour","au boulot"),("FÉVRIER",mask,"Carnaval,","on verra"),("MARS",bank,"Enfin la","banque")]
g=txt(300,48,"LE PROJET QUI GLISSE",17,TEAL,800,ls=3)
for k,(m,ic,l1,l2) in enumerate(cards):
    x=26+k*190; y=78+k*52
    g+=f'<rect x="{x+4}" y="{y+6}" width="168" height="206" rx="16" fill="{GREY_L}"/>'
    g+=cal(x,y,168,206,m,GREY, ic(x+84,y+104) + txt(x+84,y+164,l1,22,INK,800) + txt(x+84,y+191,l2,22,INK,800))
g+=(f'<path d="M40 420 C220 432 380 448 560 454" stroke="{MANGO}" stroke-width="5" fill="none" stroke-dasharray="2 12" stroke-linecap="round"/>'
    f'<path d="M548 444 l14 10 l-15 7" stroke="{MANGO}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
g+=txt(300,404,"",1)
out["03-glisse"] = svg(600,480,g,WHITE)

# 4. LES PAPIERS -------------------------------------------------------
def paper(x,y,rot,kind):
    lines="".join(f'<rect x="{x+18}" y="{y+56+k*22}" width="{[110,80,100,70,95][k]}" height="8" rx="4" fill="{GREY_L}"/>' for k in range(5))
    extra=""
    if kind==0: extra=f'<rect x="{x+18}" y="{y+100}" width="124" height="12" rx="4" fill="{MANGO}" opacity="0.55"/>'
    if kind==1: extra=f'<circle cx="{x+120}" cy="{y+150}" r="20" fill="{TEAL}"/>'+txt(x+120,y+158,"€",22,WHITE,800)
    if kind==2: extra=f'<rect x="{x+18}" y="{y+160}" width="124" height="14" rx="4" fill="{TEAL_L}"/>'
    g=(f'<rect x="{x}" y="{y}" width="160" height="196" rx="12" fill="{WHITE}"/>'
       f'<rect x="{x+18}" y="{y+22}" width="70" height="12" rx="4" fill="{TEAL}"/>'+lines+extra)
    return f'<g transform="rotate({rot} {x+80} {y+98})">{g}</g>'
labels=[("Relevés","de compte"),("Avis","d’imposition"),("Bulletins","de salaire")]
g=""
for k,(rot,(a,b)) in enumerate(zip((-5,0,5),labels)):
    x=30+k*190
    g+=paper(x,34,rot,k)+txt(x+80,270,a,22,INK,800)+txt(x+80,298,b,22,INK,800)
out["04-papiers"] = svg(600,326,g,TEAL_L)

# 5. PANNEAU WILL ------------------------------------------------------
will=(f'<rect x="38" y="250" width="232" height="200" rx="110" fill="{TEAL}"/>'
      f'<circle cx="154" cy="172" r="66" fill="{TEAL}"/>'
      f'<rect x="56" y="34" width="196" height="34" rx="17" fill="{MANGO}"/>' + txt(154,57,"AVATAR DE WILL ICI",14,INK,800,ls=1) +
      f'<rect x="300" y="78" width="270" height="176" rx="28" fill="{WHITE}" stroke="{INK}" stroke-width="3"/>'
      f'<path d="M302 168 L262 186 L302 198" fill="{WHITE}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
      f'<rect x="298" y="170" width="8" height="26" fill="{WHITE}"/>' +
      txt(435,140,"Tu vois où",31,INK,800)+txt(435,180,"je veux en",31,INK,800)+txt(435,220,"venir ?",31,TEAL,800))
out["05-will"] = svg(600,370,will,TEAL_L)

# 6. PAGE BLANCHE vs PAGES D'AVANT -------------------------------------
pb=(f'<rect x="56" y="58" width="176" height="226" rx="12" fill="{CREAM}" stroke="#D8D0C2" stroke-width="3"/>'
    + txt(144,98,"1er janvier",21,GREY,700) +
    f'<circle cx="300" cy="172" r="27" fill="{INK}"/>' + txt(300,178,"VS",16,WHITE,800) +
    f'<rect x="404" y="30" width="170" height="214" rx="12" fill="{WHITE}" stroke="{TEAL_M}" stroke-width="3"/>' + txt(440,49,"OCT.",13,TEAL,800) +
    f'<rect x="384" y="52" width="170" height="214" rx="12" fill="{WHITE}" stroke="{TEAL_M}" stroke-width="3"/>' + txt(420,70,"NOV.",13,TEAL,800) +
    f'<rect x="364" y="74" width="170" height="214" rx="12" fill="{WHITE}" stroke="{TEAL}" stroke-width="3"/>' + txt(400,102,"DÉC.",15,TEAL,800) +
    "".join(f'<rect x="382" y="{120+k*24}" width="{[120,90,110,70,100,84][k]}" height="9" rx="4" fill="{TEAL_L}"/>' for k in range(6)) +
    f'<rect x="382" y="168" width="110" height="9" rx="4" fill="{MANGO}"/>' +
    f'<circle cx="474" cy="186" r="44" fill="{WHITE}" fill-opacity="0.35" stroke="{TEAL}" stroke-width="10"/>'
    f'<line x1="506" y1="218" x2="548" y2="262" stroke="{TEAL}" stroke-width="15" stroke-linecap="round"/>' +
    txt(144,330,"CE QUE TU CROIS",15,GREY,800,ls=2) + txt(144,362,"Une page blanche",23,INK,800) +
    txt(456,330,"CE QUE LIT TON BANQUIER",15,TEAL,800,ls=1) + txt(456,362,"Les pages d’avant",23,INK,800))
out["06-pages"] = svg(600,394,pb,WHITE)

# 7. CE QUE REGARDE LE BANQUIER ----------------------------------------
import math
th=math.radians(180-0.35*180); cx,cy,r=500,128,56
ex,ey=cx+r*math.cos(th),cy-r*math.sin(th); nx,ny=cx+40*math.cos(th),cy-40*math.sin(th)
g=(cal(45,56,110,104,"CET HIVER",TEAL,"".join(f'<rect x="61" y="{106+k*16}" width="{[78,60,70][k]}" height="7" rx="3" fill="{GREY_L}"/>' for k in range(3))) +
   f'<ellipse cx="296" cy="112" rx="50" ry="37" fill="{MANGO}"/><ellipse cx="344" cy="114" rx="12" ry="11" fill="{MANGO_D}"/>'
   f'<polygon points="272,82 284,62 296,80" fill="{MANGO_D}"/><rect x="268" y="140" width="13" height="20" rx="4" fill="{MANGO_D}"/><rect x="308" y="140" width="13" height="20" rx="4" fill="{MANGO_D}"/>'
   f'<circle cx="320" cy="100" r="4.5" fill="{INK}"/><rect x="282" y="78" width="26" height="6" rx="3" fill="{INK}"/>'
   f'<circle cx="296" cy="48" r="16" fill="{TEAL}"/>' + txt(296,55,"€",19,WHITE,800) +
   f'<path d="M{cx-r} {cy} A{r} {r} 0 0 1 {cx+r} {cy}" stroke="{WHITE}" stroke-width="18" fill="none"/>'
   f'<path d="M{cx-r} {cy} A{r} {r} 0 0 1 {ex:.1f} {ey:.1f}" stroke="{TEAL}" stroke-width="18" fill="none"/>'
   f'<line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="{INK}" stroke-width="5" stroke-linecap="round"/><circle cx="{cx}" cy="{cy}" r="7" fill="{INK}"/>' +
   txt(cx,cy+40,"35 %",32,INK,800) +
   txt(100,216,"Tes relevés",21,INK,800)+txt(100,244,"de cet hiver",21,INK,800) +
   txt(300,216,"Ton épargne",21,INK,800)+txt(300,244,"= une habitude",21,INK,800) +
   txt(500,216,"Tes crédits :",21,INK,800)+txt(500,244,"35 % max*",21,INK,800) +
   txt(300,292,"* en général, de tes revenus nets, assurance comprise",16,GREY,700))
out["07-banquier"] = svg(600,318,g,TEAL_L)

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"illus151_suite.py"),encoding="utf-8").read())
dest=sys.argv[1]; os.makedirs(dest,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(device_scale_factor=2)
    for name,s in out.items():
        pg.set_content(f'<html><body style="margin:0;background:transparent">{s}</body></html>')
        pg.wait_for_timeout(150)
        pg.locator("svg").screenshot(path=f"{dest}/{name}.png", omit_background=True)
        print(name)
    b.close()

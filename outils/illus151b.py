# -*- coding: utf-8 -*-
"""Illustrations du Journal Débrouya #151 (version du 23/11)."""
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
out["06-will"]=will_panel(P["relance"],["Tu vois où","je veux en","venir ?"])
out["09-will-methode"]=will_panel(P["methode"],["Prêt ?","On fait ça","proprement."])
out["17-will-fin"]=will_panel(P["signature"],["C’était Will.","Ciao ! 🔥"],h=330)
def bank(cx,cy):
    cols="".join(f'<rect x="{cx-30+k*22}" y="{cy-8}" width="10" height="30" fill="{TEAL}"/>' for k in range(3))
    return (f'<polygon points="{cx-40},{cy-12} {cx},{cy-38} {cx+40},{cy-12}" fill="{TEAL}"/>' + cols +
            f'<rect x="{cx-42}" y="{cy+24}" width="84" height="8" rx="2" fill="{TEAL}"/>')
def burst(cx,cy,r,col,n=10):
    return "".join(f'<line x1="{cx+r*0.45*math.cos(2*math.pi*k/n):.1f}" y1="{cy+r*0.45*math.sin(2*math.pi*k/n):.1f}" x2="{cx+r*math.cos(2*math.pi*k/n):.1f}" y2="{cy+r*math.sin(2*math.pi*k/n):.1f}" stroke="{col}" stroke-width="4" stroke-linecap="round"/>' for k in range(n))
# 2. 1er JANVIER -------------------------------------------------------
def _burst_old(cx,cy,r,col,n=10):
    import math
    return "".join(f'<line x1="{cx+r*0.45*math.cos(2*math.pi*k/n):.1f}" y1="{cy+r*0.45*math.sin(2*math.pi*k/n):.1f}" x2="{cx+r*math.cos(2*math.pi*k/n):.1f}" y2="{cy+r*math.sin(2*math.pi*k/n):.1f}" stroke="{col}" stroke-width="4" stroke-linecap="round"/>' for k in range(n))
jan = (burst(70,58,34,MANGO)+burst(232,42,24,TEAL_M,8)+burst(560,286,20,MANGO,8) +
  cal(40,82,190,210,"JANVIER",TEAL, txt(135,236,"1",110,INK,800) + rings(40,82,190)) +
  f'<rect x="262" y="66" width="306" height="196" rx="26" fill="{WHITE}" stroke="{INK}" stroke-width="3"/>'
  f'<path d="M264 168 L240 186 L266 196" fill="{WHITE}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'
  f'<rect x="262" y="170" width="8" height="24" fill="{WHITE}"/>' +
  txt(415,116,"« Cette année,",25,INK,700,style="font-style:italic") +
  txt(415,148,"c’est la bonne.",25,INK,700,style="font-style:italic") +
  txt(415,190,"Cette année,",25,TEAL,800,style="font-style:italic") +
  txt(415,222,"j’investis. »",25,TEAL,800,style="font-style:italic"))
out["02-janvier"] = svg(600,318,jan,MANGO_L)

# 3. LE PROJET QUI GLISSE ---------------------------------------------
def briefcase(cx,cy):
    return (f'<rect x="{cx-14}" y="{cy-30}" width="28" height="16" rx="6" fill="none" stroke="{TEAL}" stroke-width="5"/>'
            f'<rect x="{cx-32}" y="{cy-18}" width="64" height="44" rx="8" fill="{TEAL}"/>'
            f'<rect x="{cx-32}" y="{cy-2}" width="64" height="4" fill="{TEAL_D}"/>')
def mask(cx,cy):
    return (f'<path d="M{cx+20} {cy-22} C{cx+34} {cy-46} {cx+46} {cy-46} {cx+52} {cy-40} C{cx+40} {cy-36} {cx+32} {cy-30} {cx+26} {cy-18}" fill="{MANGO}"/>'
            f'<path d="M{cx-40} {cy-8} Q{cx-40} {cy-28} {cx-18} {cy-24} Q{cx} {cy-20} {cx+18} {cy-24} Q{cx+40} {cy-28} {cx+40} {cy-8} Q{cx+38} {cy+20} {cx+14} {cy+16} Q{cx} {cy+6} {cx-14} {cy+16} Q{cx-38} {cy+20} {cx-40} {cy-8} Z" fill="{TEAL}"/>'
            f'<ellipse cx="{cx-17}" cy="{cy-6}" rx="9" ry="6" fill="{WHITE}"/><ellipse cx="{cx+17}" cy="{cy-6}" rx="9" ry="6" fill="{WHITE}"/>')
def _bank_old(cx,cy):
    cols="".join(f'<rect x="{cx-30+k*22}" y="{cy-8}" width="10" height="30" fill="{TEAL}"/>' for k in range(3))
    return (f'<polygon points="{cx-40},{cy-12} {cx},{cy-38} {cx+40},{cy-12}" fill="{TEAL}"/>' + cols +
            f'<rect x="{cx-42}" y="{cy+24}" width="84" height="8" rx="2" fill="{TEAL}"/>')
cards=[("JANVIER",briefcase,"Tu reprends","le boulot."),("FÉVRIER",mask,"C’est carnaval,","on verra après."),("MARS",bank,"Tu vas enfin","à la banque.")]
g=""
for k,(m,ic,l1,l2) in enumerate(cards):
    x=26+k*190; y=34+k*52
    g+=f'<rect x="{x+4}" y="{y+6}" width="168" height="206" rx="16" fill="{GREY_L}"/>'
    g+=cal(x,y,168,206,m,GREY, ic(x+84,y+104) + txt(x+84,y+164,l1,20,INK,800) + txt(x+84,y+190,l2,20,INK,800))
g+=(f'<path d="M40 376 C220 388 380 404 560 410" stroke="{MANGO}" stroke-width="5" fill="none" stroke-dasharray="2 12" stroke-linecap="round"/>'
    f'<path d="M548 400 l14 10 l-15 7" stroke="{MANGO}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
g+=txt(300,404,"",1)
out["03-glisse"] = svg(600,436,g,WHITE)

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

# 6. PAGE BLANCHE vs PAGES D'AVANT -------------------------------------
pb=(f'<rect x="56" y="58" width="176" height="226" rx="12" fill="{CREAM}" stroke="#D8D0C2" stroke-width="3"/>'
    + txt(144,98,"1<tspan dy='-8' font-size='13'>er</tspan><tspan dy='8'> janvier</tspan>",21,GREY,700) +
    f'<circle cx="300" cy="172" r="27" fill="{INK}"/>' + txt(300,178,"VS",16,WHITE,800) +
    f'<rect x="404" y="30" width="170" height="214" rx="12" fill="{WHITE}" stroke="{TEAL_M}" stroke-width="3"/>' + txt(446,49,"OCT.",15,TEAL,800) +
    f'<rect x="384" y="52" width="170" height="214" rx="12" fill="{WHITE}" stroke="{TEAL_M}" stroke-width="3"/>' + txt(426,71,"NOV.",15,TEAL,800) +
    f'<rect x="364" y="74" width="170" height="214" rx="12" fill="{WHITE}" stroke="{TEAL}" stroke-width="3"/>' + txt(400,102,"DÉC.",15,TEAL,800) +
    "".join(f'<rect x="382" y="{120+k*24}" width="{[120,90,110,70,100,84][k]}" height="9" rx="4" fill="{TEAL_L}"/>' for k in range(6)) +
    f'<rect x="382" y="168" width="110" height="9" rx="4" fill="{MANGO}"/>' +
    f'<circle cx="474" cy="186" r="44" fill="{WHITE}" fill-opacity="0.35" stroke="{TEAL}" stroke-width="10"/>'
    f'<line x1="506" y1="218" x2="548" y2="262" stroke="{TEAL}" stroke-width="15" stroke-linecap="round"/>' +
    txt(144,330,"TOI",18,GREY,800,ls=2) + txt(144,362,"Tu crois tourner la page.",20,INK,800) +
    txt(456,330,"TON BANQUIER",18,TEAL,800,ls=1) + txt(456,362,"Il lit les pages d’avant.",20,INK,800))
out["06-pages"] = svg(600,394,pb,WHITE)

# 7. CE QUE REGARDE LE BANQUIER ----------------------------------------
import math
th=math.radians(180-0.35*180); cx,cy,r=500,128,56
ex,ey=cx+r*math.cos(th),cy-r*math.sin(th); nx,ny=cx+40*math.cos(th),cy-40*math.sin(th)
g=(cal(45,56,110,104,"RELEVÉS",TEAL,"".join(f'<rect x="61" y="{106+k*16}" width="{[78,60,70][k]}" height="7" rx="3" fill="{GREY_L}"/>' for k in range(3))) +
   f'<ellipse cx="296" cy="112" rx="50" ry="37" fill="{MANGO}"/><ellipse cx="344" cy="114" rx="12" ry="11" fill="{MANGO_D}"/>'
   f'<polygon points="272,82 284,62 296,80" fill="{MANGO_D}"/><rect x="268" y="140" width="13" height="20" rx="4" fill="{MANGO_D}"/><rect x="308" y="140" width="13" height="20" rx="4" fill="{MANGO_D}"/>'
   f'<circle cx="320" cy="100" r="4.5" fill="{INK}"/><rect x="282" y="78" width="26" height="6" rx="3" fill="{INK}"/>'
   f'<circle cx="296" cy="48" r="16" fill="{TEAL}"/>' + txt(296,55,"€",19,WHITE,800) +
   f'<path d="M{cx-r} {cy} A{r} {r} 0 0 1 {cx+r} {cy}" stroke="{WHITE}" stroke-width="18" fill="none"/>'
   f'<path d="M{cx-r} {cy} A{r} {r} 0 0 1 {ex:.1f} {ey:.1f}" stroke="{TEAL}" stroke-width="18" fill="none"/>'
   f'<line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="{INK}" stroke-width="5" stroke-linecap="round"/><circle cx="{cx}" cy="{cy}" r="7" fill="{INK}"/>' +
   txt(cx,cy+40,"35 %",32,INK,800) +
   txt(100,214,"Il lit tes",20,INK,800)+txt(100,240,"relevés des",20,INK,800)+txt(100,266,"derniers mois.",20,INK,800) +
   txt(300,214,"Il regarde",20,INK,800)+txt(300,240,"si tu épargnes",20,INK,800)+txt(300,266,"chaque mois.",20,INK,800) +
   txt(500,214,"Il vérifie que",19,INK,800)+txt(500,240,"tes crédits restent",19,INK,800)+txt(500,266,"sous 35 %.*",19,INK,800) +
   txt(300,314,"* En général, nouveau prêt compris, sur tes revenus",18,GREY,700)+txt(300,338,"nets avant impôt, assurance comprise.",18,GREY,700))
out["07-banquier"] = svg(600,364,g,TEAL_L)

# 10. LA FEUILLE DE BILAN --------------------------------------------------
rows=["Ce que tu as fait","Ce qui t’a bloqué","Ce que tu as mis de côté"]
g=(f'<g transform="rotate(-2 300 180)"><rect x="96" y="40" width="380" height="290" rx="10" fill="{WHITE}"/>'
   + "".join(f'<line x1="96" y1="{120+k*64}" x2="476" y2="{120+k*64}" stroke="{TEAL_L}" stroke-width="2"/>' for k in range(4))
   + f'<line x1="140" y1="40" x2="140" y2="330" stroke="{MANGO_L}" stroke-width="3"/>'
   + txt(300,92,"Ton bilan 2026",28,TEAL,800)
   + "".join(f'<rect x="160" y="{132+k*64}" width="26" height="26" rx="5" fill="none" stroke="{INK}" stroke-width="3"/>'
             + txt(200,{0:153,1:217,2:281}[k],row,21,INK,700,anchor="start") for k,row in enumerate(rows))
   + '</g>'
   + f'<g transform="rotate(35 520 220) translate(10 0)"><rect x="500" y="110" width="30" height="190" rx="4" fill="{MANGO}"/>'
     f'<rect x="500" y="110" width="30" height="22" fill="{INK}" opacity="0.25"/>'
     f'<polygon points="500,300 530,300 515,336" fill="#F3D2B4"/><polygon points="509,321 521,321 515,336" fill="{INK}"/></g>')
out["10-bilan"] = svg(600,370,g,MANGO_L)

# 11. ENVIE vs OBJECTIF DATÉ ------------------------------------------------
g=(txt(150,62,"UNE ENVIE",18,GREY,800,ls=2) +
   f'<circle cx="104" cy="196" r="48" fill="{GREY_L}"/><circle cx="160" cy="168" r="62" fill="{GREY_L}"/><circle cx="210" cy="200" r="44" fill="{GREY_L}"/>'
   f'<rect x="70" y="196" width="168" height="48" rx="24" fill="{GREY_L}"/>' +
   txt(156,196,"Investir",23,GREY,700,style="font-style:italic") + txt(156,226,"en 2027",23,GREY,700,style="font-style:italic") +
   f'<path d="M258 200 L298 200" stroke="{MANGO}" stroke-width="6" stroke-linecap="round"/><path d="M286 188 l14 12 l-14 12" stroke="{MANGO}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' +
   txt(448,62,"DES ÉTAPES DATÉES",18,TEAL,800,ls=1))
for k,(d,m,t) in enumerate([("15","JANV.","Voir la banque"),("31","MARS","Avoir ton apport"),("30","JUIN","Faire une offre")]):
    y=82+k*92
    g+=(f'<rect x="318" y="{y}" width="260" height="78" rx="14" fill="{WHITE}" stroke="{TEAL_L}" stroke-width="3"/>'
        f'<path d="M318 {y+14} a14 14 0 0 1 14 -14 h70 v78 h-70 a14 14 0 0 1 -14 -14 z" fill="{TEAL}"/>'
        + txt(360,y+40,d,28,WHITE,800) + txt(360,y+64,m,15,WHITE,800,ls=1) + txt(490,y+46,t,18,INK,800))
out["11-objectif"] = svg(600,370,g,WHITE)

# 12. LE DOSSIER ---------------------------------------------------------------
items=["Bulletins de salaire","Avis d’imposition","Relevés de compte","Épargne et apport"]
g=(f'<path d="M34 92 h70 l18 20 h118 a12 12 0 0 1 12 12 v170 h-218 z" fill="{MANGO_D}"/>'
   + "".join(f'<rect x="{52+k*10}" y="{82+k*8}" width="170" height="150" rx="6" fill="{WHITE}" transform="rotate({-6+k*4} {137+k*10} {157+k*8})"/>' for k in range(3))
   + f'<rect x="28" y="152" width="230" height="148" rx="12" fill="{MANGO}"/>'
   + f'<rect x="64" y="208" width="158" height="36" rx="8" fill="{WHITE}"/>' + txt(143,233,"TON DOSSIER",17,INK,800,ls=1))
for k,it in enumerate(items):
    y=88+k*58
    g+=(f'<circle cx="294" cy="{y}" r="16" fill="{TEAL}"/><path d="M286 {y} l6 6 l10 -12" stroke="{WHITE}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
        + txt(322,y+7,it,21,INK,700,anchor="start"))
out["12-dossier"] = svg(600,330,g,TEAL_L)

# 14. LE CALENDRIER JANVIER -> JUIN ---------------------------------------------
def sc(cx,cy,inner,f=0.62): return f'<g transform="translate({cx} {cy}) scale({f}) translate({-cx} {-cy})">{inner}</g>'
def house(cx,cy,col=TEAL):
    return (f'<polygon points="{cx-38},{cy-4} {cx},{cy-36} {cx+38},{cy-4}" fill="{col}"/><rect x="{cx-28}" y="{cy-6}" width="56" height="40" fill="{col}"/>'
            f'<rect x="{cx-9}" y="{cy+12}" width="18" height="22" fill="{WHITE}"/>')
def clip(cx,cy,col=TEAL):
    return (f'<rect x="{cx-26}" y="{cy-34}" width="52" height="68" rx="6" fill="{col}"/><rect x="{cx-12}" y="{cy-40}" width="24" height="12" rx="4" fill="{INK}"/>'
            + "".join(f'<rect x="{cx-16}" y="{cy-18+k*14}" width="32" height="6" rx="3" fill="{WHITE}"/>' for k in range(3)))
def flag(cx,cy):
    return (f'<line x1="{cx-14}" y1="{cy+32}" x2="{cx-14}" y2="{cy-32}" stroke="{WHITE}" stroke-width="6" stroke-linecap="round"/>'
            f'<path d="M{cx-12} {cy-32} L{cx+26} {cy-18} L{cx-12} {cy-4} Z" fill="{WHITE}"/>')
pts=[(78,"JANV.",lambda x,y: sc(x,y,bank(x,y+4),0.58),["Tu vois","ta banque."]),
     (226,"FÉV.-MARS",lambda x,y: sc(x,y,house(x,y),0.62),["Tu choisis","ta zone et","ton budget."]),
     (374,"AVR.-MAI",lambda x,y: sc(x,y,clip(x,y),0.62),["Tu visites","et tu analyses","les biens."]),
     (522,"JUIN",flag,["Tu fais ta","1<tspan dy='-7' font-size='12'>re</tspan><tspan dy='7'> offre</tspan>","écrite."])]
g=f'<line x1="78" y1="170" x2="522" y2="170" stroke="{TEAL_M}" stroke-width="8" stroke-linecap="round"/>'
for k,(x,m,ic,LL) in enumerate(pts):
    last = k==3
    g+=(f'<rect x="{x-68}" y="54" width="136" height="38" rx="19" fill="{MANGO if last else TEAL}"/>' + txt(x,79,m,17,WHITE,800,ls=1) +
        f'<circle cx="{x}" cy="170" r="46" fill="{MANGO if last else WHITE}" stroke="{MANGO if last else TEAL}" stroke-width="5"/>' +
        ic(x,170) + "".join(txt(x,254+j*26,l,19,INK,800) for j,l in enumerate(LL)))
out["14-calendrier"] = svg(600,340,g,WHITE)

# 15. FABRICE vs NADIA -------------------------------------------------------------
def col(x0, name, color, rows, badge, badge_fill, badge_txt):
    g=(f'<circle cx="{x0+40}" cy="66" r="18" fill="{color}"/><rect x="{x0+16}" y="88" width="48" height="30" rx="15" fill="{color}"/>'
       + txt(x0+78,94,name,26,color,800,anchor="start"))
    g+=f'<line x1="{x0+24}" y1="160" x2="{x0+24}" y2="{150+104*3}" stroke="{color}" stroke-width="4"/>'
    for k,(m,t1,t2) in enumerate(rows):
        y=150+k*104
        g+=(f'<circle cx="{x0+24}" cy="{y+10}" r="10" fill="{color}"/>'
            + txt(x0+46,y+16,m,18,color,800,anchor="start",ls=1) + txt(x0+46,y+44,t1,22,INK,700,anchor="start") + txt(x0+46,y+70,t2,22,INK,700,anchor="start"))
    g+=f'<rect x="{x0}" y="572" width="270" height="78" rx="16" fill="{badge_fill}"/>'
    g+=txt(x0+135,605,badge[0],20,badge_txt,800)+txt(x0+135,633,badge[1],20,badge_txt,800)
    return g
g=(f'<rect x="300" y="0" width="300" height="680" fill="{TEAL_L}"/>' +
   col(18,"Fabrice",GREY,[("JANVIER","Il prend","sa résolution."),("FÉVRIER","Il cherche","ses papiers."),("AVRIL","Son épargne","va et vient."),("DÉC. 2027","« L’an","prochain… »")],
       ("Une année de plus","à attendre"),GREY_L,INK) +
   col(312,"Nadia",TEAL,[("DÉBUT DÉC.","Elle fait","son bilan."),("AVANT NOËL","Elle programme","son épargne."),("JANVIER","Elle arrive","prête à la banque."),("AVRIL-MAI","Elle visite,","budget en tête.")],
       ("Prête à faire","une offre"),MANGO,INK))
out["15-fabrice-nadia"] = svg(600,680,g,WHITE)

# 01. COUVERTURE (bannière + bandeau de l'édition) -----------------------------
import base64 as _b64
_ban=_b64.b64encode(open("/home/claude/debrouya-151-v3/img/00-banniere.jpg","rb").read()).decode()
_H=540
cov=(f'<image href="data:image/jpeg;base64,{_ban}" x="0" y="0" width="600" height="229" preserveAspectRatio="xMidYMid slice"/>'
     f'<path d="M0 200 C120 182 240 226 360 206 S540 188 600 204 V{_H} H0 Z" fill="{TEAL_M}" opacity="0.55"/>'
     f'<path d="M0 214 C120 196 240 240 360 220 S540 202 600 218 V{_H} H0 Z" fill="{TEAL}"/>'
     + txt(300,272,"ÉDITION #151",15,"#FFD3AE",800,ls=4)
     + txt(300,320,"Ton année 2027",40,WHITE,800)
     + txt(300,362,"commence maintenant.",32,"#FFD3AE",800)
     + cal(128,392,150,104,"MAINTENANT",TEAL_D, txt(203,468,"Tu prépares",22,INK,800) + rings(128,392,150))
     + cal(322,392,150,104,"JANV. 2027",MANGO_D, txt(397,468,"Tu es prêt",22,INK,800) + rings(322,392,150))
     + f'<line x1="286" y1="444" x2="312" y2="444" stroke="{MANGO}" stroke-width="5" stroke-linecap="round"/>'
       f'<path d="M302 434 L313 444 L302 454" stroke="{MANGO}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
     + f'<path d="M0 512 C60 498 120 524 180 512 S300 498 360 512 S480 526 540 512 S600 506 620 512 V{_H} H0 Z" fill="{TEAL_D}"/>'
       f'<path d="M0 526 C60 516 120 536 180 526 S300 516 360 526 S480 536 540 526 S600 522 620 526 V{_H} H0 Z" fill="#0A403C"/>')
out["01-hero"] = svg(600,_H,cov,TEAL)

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

# -*- coding: utf-8 -*-
"""Illustrations du Journal Débrouya #149."""
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
out["00-will-salut"]=will_panel(P["accueil"],["Salut","la famille ! 🔥"],h=330)
out["06-will"]=will_panel(P["relance"],["Tu vois où","je veux en","venir ?"])
out["09-will-methode"]=will_panel(P["methode"],["Prends","une feuille.","On avance","dans l’ordre."])
out["17-will-fin"]=will_panel(P["signature"],["C’était Will.","Ciao ! 🔥"],h=330)

def shut_house(cx,cy,s=1,body=WHITE,roof=MANGO,shut=GREY,line=INK):
    g=(f'<polygon points="{cx-110},{cy-60} {cx},{cy-140} {cx+110},{cy-60}" fill="{roof}"/>'
       f'<rect x="{cx-90}" y="{cy-62}" width="180" height="140" fill="{body}" stroke="{line}" stroke-width="3"/>')
    for wx in (cx-70,cx+26):
        g+=f'<rect x="{wx}" y="{cy-40}" width="44" height="46" fill="{shut}"/>'+"".join(f'<line x1="{wx+4}" y1="{cy-34+k*9}" x2="{wx+40}" y2="{cy-34+k*9}" stroke="{WHITE}" stroke-width="2"/>' for k in range(5))
    g+=f'<rect x="{cx-18}" y="{cy+20}" width="36" height="58" fill="{shut}"/>'
    g+="".join(f'<path d="M{cx-120+k*26} {cy+80} q4 -18 8 0 q4 -14 8 0" fill="none" stroke="#6E9B5A" stroke-width="3"/>' for k in range(10))
    return f'<g transform="translate({cx} {cy}) scale({s}) translate({-cx} {-cy})">{g}</g>'
def bubble(x,y,w,lines,size=19,fill=WHITE,col=INK):
    h=24+len(lines)*(size+8)
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="{INK}" stroke-width="2.5"/>'
            + "".join(txt(x+w/2,y+12+(j+1)*(size+8)-6,l,size,col,800 if j==0 else 600) for j,l in enumerate(lines)))


# 03. FESTIVAL LYANNAJ (rappel)
g=(txt(300,48,"LYANNAJ FEST LIVE",20,MANGO,800,ls=3) + txt(300,96,"3 soirées en live, gratuites",30,INK,800)
   + f'<rect x="30" y="114" width="540" height="110" rx="20" fill="{TEAL}"/>' + txt(300,146,"14 h – 18 h aux Antilles",22,WHITE,800)+txt(300,177,"15 h – 19 h en Guyane",22,WHITE,800)+txt(300,207,"19 h – 23 h dans l’Hexagone",20,PEACH,700))
days=[("VEN. 20 NOV.","Soirée","immobilier",TEAL,INK),("SAM. 21 NOV.","Soirée","business",TEAL,INK),("DIM. 22 NOV.","Soirée","VIP",MANGO_D,MANGO_D)]
for k,(dd,a,b2,c,fc) in enumerate(days):
    x=24+k*192
    g+=cal(x,246,168,150,dd,c, txt(x+84,326,a,22,INK,800)+txt(x+84,354,b2,22,fc,800)+rings(x,246,168))
g+=txt(300,434,"Pour la soirée VIP, les conditions d’accès sont",20,INK,700)+txt(300,462,"envoyées aux inscrits des deux premières soirées.",20,INK,700)
out["03-festival"]=svg(600,488,g,MANGO_L)

# 04. CE QUI T'ATTEND
items=[["Will et les coachs","immobilier et business"],["Des experts du financement,","des aides et de l’IA"],["La remise des diplômes en live,","avec près de cent membres","qui racontent leur projet"],["Tes questions, en direct","dans le chat"]]
g=txt(300,48,"CE QUI T’ATTEND",20,TEAL,800,ls=1.5); y=74
for lines in items:
    h=34+30*len(lines)
    g+=f'<rect x="36" y="{y}" width="528" height="{h}" rx="14" fill="{WHITE}"/>'+check(70,y+h/2)
    g+="".join(txt(98,y+38+j*30,l,21,INK,800 if j==0 else 600,anchor="start") for j,l in enumerate(lines))
    y+=h+10
out["04-programme"]=svg(600,y+22,g,TEAL_L)

# 01. COUVERTURE
ban=base64.b64encode(open(sys.argv[2],"rb").read()).decode()
H=560
g=(f'<image href="data:image/jpeg;base64,{ban}" x="0" y="0" width="600" height="229" preserveAspectRatio="xMidYMid slice"/>'
   f'<path d="M0 200 C120 182 240 226 360 206 S540 188 600 204 V{H} H0 Z" fill="{TEAL_M}" opacity="0.55"/>'
   f'<path d="M0 214 C120 196 240 240 360 220 S540 202 600 218 V{H} H0 Z" fill="{TEAL}"/>'
   + txt(300,272,"ÉDITION #149",18,PEACH,800,ls=4)
   + txt(300,320,"Ce qu’il restera",38,WHITE,800)
   + txt(300,364,"après toi.",34,PEACH,800))
g+=shut_house(300,468,s=0.5,body=WHITE,roof=MANGO,shut=TEAL_M,line=WHITE)
g+=(f'<path d="M0 520 C60 506 120 532 180 520 S300 506 360 520 S480 534 540 520 S600 514 620 520 V{H} H0 Z" fill="{TEAL_D}"/>'
    f'<path d="M0 536 C60 526 120 546 180 536 S300 526 360 536 S480 546 540 536 S600 532 620 536 V{H} H0 Z" fill="#0A403C"/>')
out["01-hero"]=svg(600,H,g,TEAL)

# 02. LA MAISON AUX VOLETS FERMÉS
g=txt(300,48,"CE QUI BLOQUE",20,TEAL,800,ls=1.5)
g+=shut_house(300,230)
g+=bubble(16,74,176,["Un frère veut","la garder."])
g+=bubble(408,74,176,["Une sœur","veut vendre."])
g+=bubble(60,330,480,["Un cousin dans l’Hexagone","ne répond plus aux messages."])
g+=txt(300,448,"Et pendant ce temps,",20,INK,800)+txt(300,476,"la maison se dégrade.",20,MANGO_D,800)
out["02-volets"]=svg(600,502,g,TEAL_L)

# 03. SANS TESTAMENT, QUI HÉRITE ?
rows=[("Tes enfants",["À parts égales."],TEAL),
      ("Ton conjoint marié",["Un quart en pleine propriété,","ou l’usufruit de tout,","selon ta famille."],TEAL),
      ("Ton compagnon,","même pacsé",MANGO)]
g=txt(300,48,"SANS TESTAMENT, QUI HÉRITE ?",20,TEAL,800,ls=1.5); y=70
for who,what,c in [("Tes enfants",["À parts égales."],TEAL),("Ton conjoint marié",["Si tous vos enfants sont communs :","un quart de tes biens ou l’usufruit","de tout, au choix. Si l’un est né","d’une autre union : un quart."],TEAL),("Ton partenaire pacsé",["Rien. Seulement le droit de rester","un an, gratuitement, dans votre logement."],MANGO),("Ton concubin",["Rien du tout."],MANGO)]:
    h=40+30*len(what)+30
    g+=f'<rect x="24" y="{y}" width="552" height="{h}" rx="16" fill="{WHITE}"/><rect x="24" y="{y}" width="10" height="{h}" fill="{c}"/>'
    g+=txt(52,y+38,who,21,c if c==MANGO else TEAL,800,anchor="start")
    g+="".join(txt(52,y+72+j*30,l,20,INK,700,anchor="start") for j,l in enumerate(what))
    y+=h+12
out["03-loi"]=svg(600,y+14,g,TEAL_L)

# 05. MÊME BIEN, DEUX HÉRITAGES
def col(x0,title,color,rows,badge,bfill,btxt,rowfill):
    g=txt(x0+135,62,title,24,color,800)
    for k,lines in enumerate(rows):
        y=86+k*96
        g+=f'<rect x="{x0}" y="{y}" width="270" height="84" rx="14" fill="{rowfill}"/>'+"".join(txt(x0+18,y+34+j*28,l,19,INK,700 if j==0 else 600,anchor="start") for j,l in enumerate(lines))
    g+=f'<rect x="{x0}" y="384" width="270" height="88" rx="16" fill="{bfill}"/>'+txt(x0+135,420,badge[0],23,btxt,800)+txt(x0+135,450,badge[1],19,btxt,700)
    return g
g=(f'<rect x="300" y="0" width="300" height="500" fill="{TEAL_L}"/>'
   + col(16,"Rien d’organisé","#5F6B70",[["Les papiers sont","introuvables."],["Personne ne connaît","tes souhaits."],["Tes héritiers ne","se parlent plus."]],("Un conflit","avec un toit dessus"),GREY_L,INK,"#F4F1EC")
   + col(314,"Tout est organisé",TEAL,[["Les papiers sont","en ordre."],["Chacun sait ce","que tu voulais."],["Tes héritiers savent","quoi en faire."]],("Un revenu","pour ceux d’après"),MANGO,INK,WHITE))
out["05-heritages"]=svg(600,500,g,WHITE)

# 10. LE DOSSIER « SI JE PARS DEMAIN »
items=[("La liste de tes biens","avec leur adresse"),("Tes titres de propriété","et tes actes notariés"),("Tes crédits en cours,","avec le nom de chaque banque"),("Tes baux, tes locataires,","et qui gère chaque bien")]
g=""; y=24
for a,b2 in items:
    g+=f'<rect x="24" y="{y}" width="552" height="78" rx="14" fill="{WHITE}"/>'+check(62,y+39,TEAL,r=16)+txt(94,y+34,a,20,INK,800,anchor="start")+txt(94,y+62,b2,19,INK,600,anchor="start")
    y+=88
out["10-dossier"]=svg(600,y+14,g,TEAL_L)

# 11. LA RÉSERVE HÉRÉDITAIRE
g=txt(300,48,"SELON LE NOMBRE D’ENFANTS",20,TEAL,800,ls=1.5); y=74
for lab,num,den,frac in [("1 enfant",1,2,"la moitié"),("2 enfants",2,3,"les deux tiers"),("3 enfants ou plus",3,4,"les trois quarts")]:
    g+=txt(24,y+20,lab,20,INK,800,anchor="start")
    w=552*num/den
    g+=f'<rect x="24" y="{y+32}" width="552" height="46" rx="12" fill="{TEAL_M}"/><rect x="24" y="{y+32}" width="{w}" height="46" rx="12" fill="{MANGO}"/><rect x="{24+w-12}" y="{y+32}" width="12" height="46" fill="{MANGO}"/>'
    g+=txt(24+w/2,y+62,frac,19,WHITE,800)
    y+=104
g+=f'<rect x="24" y="{y+4}" width="22" height="22" rx="5" fill="{MANGO}"/>'+txt(56,y+22,"Réservée à tes enfants, quoi que dise ton testament.",19,INK,700,anchor="start")
g+=f'<rect x="24" y="{y+40}" width="22" height="22" rx="5" fill="{TEAL_M}"/>'+txt(56,y+60,"La quotité disponible : tu la donnes à qui tu veux.",19,INK,700,anchor="start")
out["11-reserve"]=svg(600,y+90,g,WHITE)

# 12. JOSETTE : SANS / AVEC ORGANISATION
def col2(x0,title,color,rows,badge,bfill,btxt,rowfill):
    g=txt(x0+135,46,title[0],20,color,800)+txt(x0+135,74,title[1],20,color,800)
    for k,lines in enumerate(rows):
        y=96+k*96
        g+=f'<rect x="{x0}" y="{y}" width="270" height="84" rx="14" fill="{rowfill}"/>'+"".join(txt(x0+16,y+34+j*28,l,19,INK,700 if j==0 else 600,anchor="start") for j,l in enumerate(lines))
    g+=f'<rect x="{x0}" y="394" width="270" height="88" rx="16" fill="{bfill}"/>'+"".join(txt(x0+135,430+j*30,l,20,btxt,800 if j==0 else 700) for j,l in enumerate(badge))
    return g
g=(f'<rect x="300" y="0" width="300" height="508" fill="{TEAL_L}"/>'
   + col2(16,("Si rien","n’est organisé"),"#5F6B70",[["Les papiers dorment","dans une armoire."],["Ses enfants ignorent","le crédit du T2."],["Marc tient à la maison,","ses sœurs veulent vendre."]],["La maison attend,","volets fermés."],GREY_L,INK,"#F4F1EC")
   + col2(314,("Si Josette","s’est organisée"),TEAL,[["Elle a fait un dossier,","et tous savent où il est."],["Elle a réuni la famille,","chacun a dit ce qu’il veut."],["Avec son notaire, elle a","prévu qui reçoit quoi."]],["Chacun sait ce","que Josette voulait."],MANGO,INK,WHITE))
out["12-josette"]=svg(600,508,g,WHITE)
out={k:v for k,v in out.items() if k in ("03-festival","04-programme")}
dest=sys.argv[1]; os.makedirs(dest,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(device_scale_factor=2)
    for name,s in out.items():
        pg.set_content(f'<html><body style="margin:0;background:transparent">{s}</body></html>'); pg.wait_for_timeout(120)
        pg.locator("svg").screenshot(path=f"{dest}/{name}.png", omit_background=True)
    b.close()
print(len(out),"images")

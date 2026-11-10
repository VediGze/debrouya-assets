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
P=json_poses = __import__("json").loads(sys.argv[3])
out["00-will-salut"]=will_panel(P["accueil"],["Salut","la famille ! 🔥"],h=330)
out["05-will"]=will_panel(P["relance"],["Tu vois","le changement ?"],h=340)
out["10-will-methode"]=will_panel(P["methode"],["Ça se fait","dans les règles,","ou ça ne se","fait pas."])
out["17-will-fin"]=will_panel(P["signature"],["C’était Will 🔥","Ciao !"],h=330)

def key(cx,cy,col=PEACH,s=1):
    return (f'<g transform="translate({cx} {cy}) scale({s})"><circle cx="0" cy="0" r="18" fill="none" stroke="{col}" stroke-width="8"/>'
            f'<rect x="16" y="-4" width="46" height="8" rx="3" fill="{col}"/><rect x="44" y="4" width="8" height="12" rx="2" fill="{col}"/><rect x="56" y="4" width="6" height="9" rx="2" fill="{col}"/></g>')

# 01. COUVERTURE -----------------------------------------------------------------------
ban=base64.b64encode(open(sys.argv[2],"rb").read()).decode()
H=540
g=(f'<image href="data:image/jpeg;base64,{ban}" x="0" y="0" width="600" height="229" preserveAspectRatio="xMidYMid slice"/>'
   f'<path d="M0 200 C120 182 240 226 360 206 S540 188 600 204 V{H} H0 Z" fill="{TEAL_M}" opacity="0.55"/>'
   f'<path d="M0 214 C120 196 240 240 360 220 S540 202 600 218 V{H} H0 Z" fill="{TEAL}"/>'
   + txt(300,272,"ÉDITION #152",15,PEACH,800,ls=4)
   + txt(300,320,"Louer sans t’engager",38,WHITE,800)
   + txt(300,362,"pour 3 ans.",34,PEACH,800))
# frise 10 mois avec la clé qui revient
for k in range(10):
    x=110+k*38; on=k<8
    g+=f'<rect x="{x}" y="420" width="30" height="40" rx="7" fill="{WHITE if on else TEAL_D}" opacity="{1 if on else 0.6}"/>'
g+=key(110+8*38+44,440,PEACH,0.9)+txt(250,486,"Tu choisis la durée · tu récupères ton bien",15,PEACH,700)
g+=(f'<path d="M0 512 C60 498 120 524 180 512 S300 498 360 512 S480 526 540 512 S600 506 620 512 V{H} H0 Z" fill="{TEAL_D}"/>'
    f'<path d="M0 526 C60 516 120 536 180 526 S300 516 360 526 S480 536 540 526 S600 522 620 526 V{H} H0 Z" fill="#0A403C"/>')
out["01-hero"]=svg(600,H,g,TEAL)

# 02. LE LOGEMENT FERMÉ QUI COÛTE --------------------------------------------------------
g=(txt(300,50,"LOGEMENT FERMÉ « EN ATTENDANT »",16,TEAL,800,ls=2)
   + house(150,190,2.0,GREY)
   + "".join(f'<rect x="{104+k*24}" y="{176}" width="18" height="22" fill="{GREY_L}"/>' for k in range(0))
   + f'<rect x="110" y="170" width="28" height="26" fill="{INK}" opacity="0.55"/><rect x="162" y="170" width="28" height="26" fill="{INK}" opacity="0.55"/>'
   + f'<rect x="64" y="292" width="172" height="44" rx="22" fill="{INK}"/>' + txt(150,321,"Rapporte : 0 €",19,WHITE,800))
costs=["Taxe foncière","Assurance","Charges","Entretien"]
g+=txt(445,98,"Mais il continue de coûter :",17,INK,700)
for k,c in enumerate(costs):
    y=124+k*58
    g+=(f'<rect x="318" y="{y}" width="254" height="44" rx="12" fill="{WHITE}"/>'
        + f'<circle cx="342" cy="{y+22}" r="13" fill="{MANGO}"/>'+txt(342,y+29,"−",20,WHITE,800)
        + txt(366,y+29,c,19,INK,700,anchor="start"))
out["02-ferme"]=svg(600,370,g,GREY_L)

# 03. DURÉES D'ENGAGEMENT ------------------------------------------------------------------
g=txt(300,48,"COMBIEN DE TEMPS TU T’ENGAGES",16,TEAL,800,ls=2)
rows=[("Location vide","3 ans minimum (particulier)",500,GREY,"36 mois"),
      ("Meublé classique","1 an, reconduit tout seul",168,GREY,"12 mois"),
      ("Bail mobilité","1 à 10 mois, au choix",140,MANGO,"1 à 10 mois")]
for k,(t,sub,w,col,lab) in enumerate(rows):
    y=86+k*96
    g+=(txt(40,y+4,t,20,INK,800,anchor="start")+txt(40,y+28,sub,16,GREY,700,anchor="start")
        + f'<rect x="40" y="{y+40}" width="520" height="24" rx="12" fill="{WHITE}"/>'
        + f'<rect x="40" y="{y+40}" width="{w*520/500:.0f}" height="24" rx="12" fill="{col}"/>')
g+=txt(300,384,"Le bail mobilité s’arrête tout seul à la date prévue.",17,MANGO_D,800)
out["03-durees"]=svg(600,408,g,TEAL_L)

# 04. LE BAIL MOBILITÉ EN 4 POINTS ----------------------------------------------------------
def sofa(cx,cy): return (f'<rect x="{cx-28}" y="{cy-6}" width="56" height="22" rx="6" fill="{TEAL}"/><rect x="{cx-34}" y="{cy-14}" width="12" height="30" rx="5" fill="{TEAL}"/>'
                         f'<rect x="{cx+22}" y="{cy-14}" width="12" height="30" rx="5" fill="{TEAL}"/><rect x="{cx-24}" y="{cy-20}" width="48" height="16" rx="5" fill="{TEAL_M}"/>')
def calic(cx,cy): return (f'<rect x="{cx-26}" y="{cy-22}" width="52" height="46" rx="8" fill="{TEAL}"/><rect x="{cx-26}" y="{cy-22}" width="52" height="14" rx="6" fill="{TEAL_D}"/>'
                          + txt(cx,cy+18,"1-10",16,WHITE,800))
def stop(cx,cy): return (f'<circle cx="{cx}" cy="{cy}" r="26" fill="{TEAL}"/><rect x="{cx-10}" y="{cy-10}" width="20" height="20" rx="3" fill="{WHITE}"/>')
def norep(cx,cy): return (f'<circle cx="{cx}" cy="{cy}" r="26" fill="{TEAL}"/><path d="M{cx-12} {cy+4} a12 12 0 1 1 6 8" stroke="{WHITE}" stroke-width="4" fill="none" stroke-linecap="round"/>'
                          f'<line x1="{cx-18}" y1="{cy-18}" x2="{cx+18}" y2="{cy+18}" stroke="{MANGO}" stroke-width="5" stroke-linecap="round"/>')
cards=[(sofa,"Logement","meublé"),(calic,"1 à 10 mois,","au choix"),(stop,"S’arrête","tout seul"),(norep,"Ni renouvelé,","ni reconduit")]
g=txt(300,46,"LE BAIL MOBILITÉ",17,TEAL,800,ls=3)+txt(300,74,"créé par la loi ELAN en 2018",16,GREY,700)
for k,(ic,a,b) in enumerate(cards):
    x=24+(k%2)*282; y=98+(k//2)*138
    g+=(f'<rect x="{x}" y="{y}" width="270" height="122" rx="16" fill="{WHITE}" stroke="{TEAL}" stroke-width="3"/>'
        + ic(x+56,y+61) + txt(x+102,y+56,a,21,INK,800,anchor="start") + txt(x+102,y+84,b,21,INK,800,anchor="start"))
out["04-bail"]=svg(600,384,g,TEAL_L)

# 06. QUI PEUT LOUER -------------------------------------------------------------------------
who=[("Formation","professionnelle"),("Études","supérieures"),("Contrat","d’apprentissage"),("Stage",""),("Service","civique"),("Mutation","professionnelle"),("Mission","temporaire")]
g=txt(300,46,"TON LOCATAIRE, AU MOMENT DE SIGNER",16,TEAL,800,ls=2)
for k,(a,b) in enumerate(who):
    col=k%2; row=k//2; x=24+col*282; y=70+row*78
    if k==6: x=24+141
    g+=(f'<rect x="{x}" y="{y}" width="270" height="64" rx="14" fill="{WHITE}"/>' + check(x+34,y+32)
        + (txt(x+60,y+28,a,19,INK,800,anchor="start")+txt(x+60,y+50,b,17,INK,600,anchor="start") if b else txt(x+60,y+39,a,19,INK,800,anchor="start")))
g+=txt(300,388,"Le motif doit exister à la signature, et être écrit dans le bail.",16,GREY,700)
out["06-qui"]=svg(600,410,g,TEAL_L)

# 08. LES 4 ÉTAPES (marches, sans titre) -------------------------------------------------------
g=""
labels=[("Meublé","complet"),("Le bon","locataire"),("Bail","écrit"),("Charges et","sécurité")]
base=372
for k,(l1,l2) in enumerate(labels):
    hgt=[100,150,200,250][k]; x=26+k*140; y=base-hgt; fill=MANGO if k==3 else TEAL
    g+=f'<rect x="{x}" y="{y}" width="128" height="{hgt+30}" rx="14" fill="{fill}"/>'
    g+=f'<circle cx="{x+64}" cy="{y}" r="24" fill="{WHITE}" stroke="{fill}" stroke-width="5"/>'+txt(x+64,y+9,str(k+1),24,INK,800)
    g+=txt(x+64,y+58,l1,20,WHITE,800)+txt(x+64,y+84,l2,20,WHITE,800)
g+=f'<line x1="530" y1="122" x2="530" y2="62" stroke="{INK}" stroke-width="5" stroke-linecap="round"/><path d="M532 62 L574 76 L532 90 Z" fill="{MANGO}"/>'
out["08-marches"]=svg(600,400,f'<g transform="translate(0 -24)">{g}</g>',TEAL_L)

# 09. LA LISTE DU MEUBLÉ ------------------------------------------------------------------------
items=["Literie + couette","Rideaux ou volets","Plaques de cuisson","Four ou micro-ondes","Frigo + congélateur","Vaisselle","Ustensiles de cuisine","Table et sièges","Étagères","Luminaires","Matériel d’entretien"]
g=txt(300,46,"LA LISTE MINIMUM DU MEUBLÉ",16,TEAL,800,ls=2)
for k,it in enumerate(items):
    col=0 if k<6 else 1; row=k if k<6 else k-6; x=24+col*290; y=88+row*50
    g+=f'<rect x="{x}" y="{y-18}" width="26" height="26" rx="6" fill="none" stroke="{TEAL}" stroke-width="3"/>'+txt(x+38,y+2,it,18,INK,700,anchor="start")
g+=txt(300,404,"Il manque quelque chose ? Complète avant de louer.",17,MANGO_D,800)
out["09-meuble"]=svg(600,428,g,WHITE)

# 11. LES MENTIONS DU BAIL -----------------------------------------------------------------------
g=(f'<rect x="60" y="30" width="300" height="330" rx="10" fill="{WHITE}"/>'
   + f'<rect x="60" y="30" width="300" height="56" rx="10" fill="{TEAL}"/><rect x="60" y="70" width="300" height="16" fill="{TEAL}"/>'
   + txt(210,66,"BAIL MOBILITÉ",19,WHITE,800,ls=2))
ments=[("La durée",""),("Le motif",""),("« Bail mobilité »,","titre Ier ter, loi de 1989"),("Aucun dépôt de","garantie exigé")]
for k,(a,b) in enumerate(ments):
    y=126+k*58
    g+=check(92,y-6)+txt(116,y,a,19,INK,800,anchor="start")+(txt(116,y+22,b,(19 if k==3 else 16),(INK if k==3 else GREY),(800 if k==3 else 700),anchor="start") if b else "")
g+=(f'<rect x="384" y="70" width="190" height="250" rx="14" fill="{TEAL_L}"/>' + txt(479,108,"À joindre :",18,TEAL,800)
    + txt(479,160,"État des lieux",18,INK,700) + txt(479,214,"Inventaire",18,INK,700) + txt(479,238,"du mobilier",18,INK,700) + txt(479,292,"Diagnostics",18,INK,700))
out["11-mentions"]=svg(600,390,g,GREY_L)

# 12. LE PRÉAVIS, PAS SYMÉTRIQUE --------------------------------------------------------------------
g=(txt(300,46,"QUI PEUT METTRE FIN AU BAIL ?",16,TEAL,800,ls=2)
   + f'<rect x="24" y="70" width="268" height="190" rx="18" fill="{TEAL}"/>' + txt(158,112,"TON LOCATAIRE",16,PEACH,800,ls=2)
   + txt(158,158,"À tout moment",24,WHITE,800) + txt(158,192,"avec 1 mois",20,WHITE,700) + txt(158,218,"de préavis",20,WHITE,700)
   + f'<rect x="308" y="70" width="268" height="190" rx="18" fill="{WHITE}"/>' + txt(442,112,"TOI",16,MANGO_D,800,ls=2)
   + txt(442,158,"Pas avant la fin",24,INK,800) + txt(442,192,"sauf faute",20,INK,700) + txt(442,218,"du locataire",20,INK,700))
out["12-preavis"]=svg(600,290,g,TEAL_L)

# 13. MURIELLE : 3 OPTIONS ---------------------------------------------------------------------------
def opt(x,title,big,line1,line2,col,bg,fg):
    return (f'<rect x="{x}" y="96" width="180" height="300" rx="18" fill="{bg}"/>'
            + txt(x+90,134,title[0],15,col,800,ls=1)+txt(x+90,156,title[1],15,col,800,ls=1)
            + txt(x+90,224,big,32,fg,800) + txt(x+90,280,line1,17,fg,700)+txt(x+90,304,line2,17,fg,700))
g=(txt(300,40,"MURIELLE · T2 MEUBLÉ À SCHŒLCHER",16,TEAL,800,ls=1)
   + txt(300,68,"Retour prévu dans 8 mois · loyer possible 650 € / mois",16,GREY,700)
   + opt(16,("OPTION 1","LOGEMENT VIDE"),"0 €","et les frais","tombent quand même",GREY,GREY_L,INK)
   + opt(210,("OPTION 2","BAIL CLASSIQUE"),"1 an","des loyers, mais","retour bloqué",GREY,WHITE,INK)
   + opt(404,("OPTION 3","BAIL MOBILITÉ"),"5 200 €","et retour","à la date prévue",PEACH,TEAL,WHITE)
   + f'<rect x="404" y="96" width="180" height="300" rx="18" fill="none" stroke="{MANGO}" stroke-width="5"/>'
   + txt(494,250,"8 × 650 €",16,PEACH,700))
out["13-murielle"]=svg(600,420,g,TEAL_L)
dest=sys.argv[1]; os.makedirs(dest,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(device_scale_factor=2)
    for name,s in out.items():
        pg.set_content(f'<html><body style="margin:0;background:transparent">{s}</body></html>'); pg.wait_for_timeout(120)
        pg.locator("svg").screenshot(path=f"{dest}/{name}.png", omit_background=True)
    b.close()
print(len(out),"images")

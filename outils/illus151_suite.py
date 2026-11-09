# -*- coding: utf-8 -*-
# Suite des illustrations #151 (exécuté dans le contexte de illus151.py : txt, svg, cal, bank, palette, out)

import base64
AV=os.path.join(os.path.dirname(os.path.abspath(__file__)),"avatar")
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

out["00-will-salut"] = will_panel("salut", ["Salut","la famille ! 🔥"], h=330)
out["05-will"] = will_panel("menton", ["Tu vois où","je veux en","venir ?"])
out["08-will-pouce"] = will_panel("pouce", ["Quatre étapes.","On fait ça","proprement."])
out["16-will-clin"] = will_panel("clin", ["C’était Will 🔥","Ciao !"], h=330)

# 09. LES 4 MARCHES ------------------------------------------------------
g = txt(300,46,"TA MÉTHODE EN 4 ÉTAPES",17,TEAL,800,ls=3)
labels=[("Bilan",""),("Objectif","daté"),("Dossier",""),("Calendrier","")]
base=372
for k,(l1,l2) in enumerate(labels):
    hgt=[100,150,200,250][k]; x=26+k*140; y=base-hgt
    fill = MANGO if k==3 else TEAL
    g+=f'<rect x="{x}" y="{y}" width="128" height="{hgt+30}" rx="14" fill="{fill}"/>'
    g+=f'<circle cx="{x+64}" cy="{y}" r="24" fill="{WHITE}" stroke="{fill}" stroke-width="5"/>'+txt(x+64,y+9,str(k+1),24,INK,800)
    if l2: g+=txt(x+64,y+58,l1,21,WHITE,800)+txt(x+64,y+84,l2,21,WHITE,800)
    else:  g+=txt(x+64,y+64,l1,20 if len(l1)>8 else 21,WHITE,800)
g+=(f'<line x1="530" y1="122" x2="530" y2="62" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M532 62 L574 76 L532 90 Z" fill="{MANGO}"/>')

out["09-marches"] = svg(600,400,g,TEAL_L)

# 10. LA FEUILLE DE BILAN --------------------------------------------------
rows=["Ce que j’ai fait","Ce qui m’a bloqué","Ce que j’ai mis de côté"]
g=(f'<g transform="rotate(-2 300 180)"><rect x="96" y="40" width="380" height="290" rx="10" fill="{WHITE}"/>'
   + "".join(f'<line x1="96" y1="{120+k*64}" x2="476" y2="{120+k*64}" stroke="{TEAL_L}" stroke-width="2"/>' for k in range(4))
   + f'<line x1="140" y1="40" x2="140" y2="330" stroke="{MANGO_L}" stroke-width="3"/>'
   + txt(300,92,"Mon bilan 2026",28,TEAL,800)
   + "".join(f'<rect x="160" y="{132+k*64}" width="26" height="26" rx="5" fill="none" stroke="{INK}" stroke-width="3"/>'
             + txt(200,{0:153,1:217,2:281}[k],row,21,INK,700,anchor="start") for k,row in enumerate(rows))
   + '</g>'
   + f'<g transform="rotate(35 520 220)"><rect x="500" y="110" width="30" height="190" rx="4" fill="{MANGO}"/>'
     f'<rect x="500" y="110" width="30" height="22" fill="{INK}" opacity="0.25"/>'
     f'<polygon points="500,300 530,300 515,336" fill="#F3D2B4"/><polygon points="509,321 521,321 515,336" fill="{INK}"/></g>')
out["10-bilan"] = svg(600,370,g,MANGO_L)

# 11. ENVIE vs OBJECTIF DATÉ ------------------------------------------------
g=(txt(150,62,"UNE ENVIE",15,GREY,800,ls=2) +
   f'<circle cx="104" cy="196" r="48" fill="{GREY_L}"/><circle cx="160" cy="168" r="62" fill="{GREY_L}"/><circle cx="210" cy="200" r="44" fill="{GREY_L}"/>'
   f'<rect x="70" y="196" width="168" height="48" rx="24" fill="{GREY_L}"/>' +
   txt(156,196,"Investir",23,GREY,700,style="font-style:italic") + txt(156,226,"en 2027",23,GREY,700,style="font-style:italic") +
   f'<path d="M258 200 L298 200" stroke="{MANGO}" stroke-width="6" stroke-linecap="round"/><path d="M286 188 l14 12 l-14 12" stroke="{MANGO}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' +
   txt(448,62,"UN OBJECTIF DATÉ",15,TEAL,800,ls=2))
for k,(d,m,t) in enumerate([("31","JANV.","RDV banque"),("31","MARS","Apport prêt"),("30","JUIN","1re offre")]):
    y=82+k*92
    g+=(f'<rect x="318" y="{y}" width="260" height="78" rx="14" fill="{WHITE}" stroke="{TEAL_L}" stroke-width="3"/>'
        f'<path d="M318 {y+14} a14 14 0 0 1 14 -14 h70 v78 h-70 a14 14 0 0 1 -14 -14 z" fill="{TEAL}"/>'
        + txt(360,y+40,d,28,WHITE,800) + txt(360,y+62,m,13,WHITE,800,ls=1) + txt(498,y+48,t,21,INK,800))
out["11-objectif"] = svg(600,370,g,WHITE)

# 12. LE DOSSIER ---------------------------------------------------------------
items=["Bulletins de salaire","Avis d’imposition","Relevés de compte","Épargne et apport"]
g=(f'<path d="M34 92 h70 l18 20 h118 a12 12 0 0 1 12 12 v170 h-218 z" fill="{MANGO_D}"/>'
   + "".join(f'<rect x="{52+k*10}" y="{82+k*8}" width="170" height="150" rx="6" fill="{WHITE}" transform="rotate({-6+k*4} {137+k*10} {157+k*8})"/>' for k in range(3))
   + f'<rect x="28" y="152" width="230" height="148" rx="12" fill="{MANGO}"/>'
   + f'<rect x="64" y="208" width="158" height="36" rx="8" fill="{WHITE}"/>' + txt(143,233,"MON DOSSIER",17,INK,800,ls=1))
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
pts=[(78,"JANV.",lambda x,y: sc(x,y,bank(x,y+4),0.58),"RDV","banque"),
     (226,"FÉV.-MARS",lambda x,y: sc(x,y,house(x,y),0.62),"Zone et","visites"),
     (374,"AVR.-MAI",lambda x,y: sc(x,y,clip(x,y),0.62),"Analyse","des biens"),
     (522,"JUIN",flag,"1re offre","écrite")]
g=f'<line x1="78" y1="170" x2="522" y2="170" stroke="{TEAL_M}" stroke-width="8" stroke-linecap="round"/>'
for k,(x,m,ic,l1,l2) in enumerate(pts):
    last = k==3
    g+=(f'<rect x="{x-62}" y="56" width="124" height="34" rx="17" fill="{MANGO if last else TEAL}"/>' + txt(x,79,m,15,INK if last else WHITE,800,ls=1) +
        f'<circle cx="{x}" cy="170" r="46" fill="{MANGO if last else WHITE}" stroke="{MANGO if last else TEAL}" stroke-width="5"/>' +
        ic(x,170) + txt(x,254,l1,20,INK,800) + txt(x,280,l2,20,INK,800))
out["14-calendrier"] = svg(600,320,g,WHITE)

# 15. FABRICE vs NADIA -------------------------------------------------------------
def col(x0, name, color, rows, badge, badge_fill, badge_txt):
    g=(f'<circle cx="{x0+40}" cy="66" r="18" fill="{color}"/><rect x="{x0+16}" y="88" width="48" height="30" rx="15" fill="{color}"/>'
       + txt(x0+78,94,name,26,color,800,anchor="start"))
    g+=f'<line x1="{x0+24}" y1="160" x2="{x0+24}" y2="{150+104*3}" stroke="{color}" stroke-width="4"/>'
    for k,(m,t1,t2) in enumerate(rows):
        y=150+k*104
        g+=(f'<circle cx="{x0+24}" cy="{y+10}" r="10" fill="{color}"/>'
            + txt(x0+46,y+16,m,16,color,800,anchor="start",ls=1) + txt(x0+46,y+44,t1,22,INK,700,anchor="start") + txt(x0+46,y+70,t2,22,INK,700,anchor="start"))
    g+=f'<rect x="{x0}" y="572" width="270" height="78" rx="16" fill="{badge_fill}"/>'
    g+=txt(x0+135,605,badge[0],20,badge_txt,800)+txt(x0+135,633,badge[1],20,badge_txt,800)
    return g
g=(f'<rect x="300" y="0" width="300" height="680" fill="{TEAL_L}"/>' +
   col(18,"Fabrice",GREY,[("JANVIER","Il attend","le 1er janvier"),("FÉVRIER","Il lui manque","des papiers"),("AVRIL","Épargne","irrégulière"),("DÉC. 2027","« L’an","prochain… »")],
       ("Une année de plus","à attendre"),GREY_L,INK) +
   col(312,"Nadia",TEAL,[("FIN NOVEMBRE","Elle fait","son bilan"),("DÉCEMBRE","Virement","automatique"),("JANVIER","RDV banque,","dossier complet"),("PRINTEMPS","Elle visite,","budget connu")],
       ("Prête à faire","une offre"),MANGO,INK))
out["15-fabrice-nadia"] = svg(600,680,g,WHITE)

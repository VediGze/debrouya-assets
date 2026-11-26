exec(open("/tmp/claude-0/-home-claude/901306cc-9835-5f2f-8144-8b453c5d989e/scratchpad/_head.py").read())
exec(open("/tmp/claude-0/-home-claude/901306cc-9835-5f2f-8144-8b453c5d989e/scratchpad/_common.py").read())
out={}
P=json.loads(sys.argv[3]); ONLY=P.get("only")
out["00-will-salut"]=will_panel(P["accueil"],["Salut","la famille ! 🔥"],h=330)
out["05-will"]=will_panel(P["relance"],["Tu vois ce","qui change ?"])
out["10-will-methode"]=will_panel(P["methode"],["Ça se fait","dans les règles,","ou ça ne se","fait pas."])
out["17-will-fin"]=will_panel(P["signature"],["C’était Will.","Ciao ! 🔥"],h=330)

def key(cx,cy,col=PEACH,s=1):
    return (f'<g transform="translate({cx} {cy}) scale({s})"><circle cx="0" cy="0" r="18" fill="none" stroke="{col}" stroke-width="8"/>'
            f'<rect x="16" y="-4" width="46" height="8" rx="3" fill="{col}"/><rect x="44" y="4" width="8" height="12" rx="2" fill="{col}"/><rect x="56" y="4" width="6" height="9" rx="2" fill="{col}"/></g>')

# 01 COUVERTURE
ban=base64.b64encode(open(sys.argv[2],"rb").read()).decode()
H=540
g=(f'<image href="data:image/jpeg;base64,{ban}" x="0" y="0" width="600" height="229" preserveAspectRatio="xMidYMid slice"/>'
   f'<path d="M0 200 C120 182 240 226 360 206 S540 188 600 204 V{H} H0 Z" fill="{TEAL_M}" opacity="0.55"/>'
   f'<path d="M0 214 C120 196 240 240 360 220 S540 202 600 218 V{H} H0 Z" fill="{TEAL}"/>'
   + txt(300,272,"ÉDITION #152",18,PEACH,800,ls=4) + txt(300,320,"Louer sans t’engager",38,WHITE,800) + txt(300,362,"pour 3 ans.",34,PEACH,800))
for k in range(10):
    x=110+k*38; on=k<8
    g+=f'<rect x="{x}" y="412" width="30" height="40" rx="7" fill="{WHITE if on else TEAL_D}" opacity="{1 if on else 0.6}"/>'
g+=key(110+8*38+44,432,PEACH,0.9)+txt(300,486,"Tu choisis la durée, et tu récupères ton bien.",18,PEACH,700)
g+=(f'<path d="M0 512 C60 498 120 524 180 512 S300 498 360 512 S480 526 540 512 S600 506 620 512 V{H} H0 Z" fill="{TEAL_D}"/>'
    f'<path d="M0 526 C60 516 120 536 180 526 S300 516 360 526 S480 536 540 526 S600 522 620 526 V{H} H0 Z" fill="#0A403C"/>')
out["01-hero"]=svg(600,H,g,TEAL)

# 02 LE LOGEMENT FERMÉ QUI COÛTE
def house(cx,cy,col=GREY):
    return (f'<polygon points="{cx-76},{cy-10} {cx},{cy-80} {cx+76},{cy-10}" fill="{col}"/><rect x="{cx-60}" y="{cy-12}" width="120" height="96" fill="{col}"/>'
            f'<rect x="{cx-38}" y="{cy+6}" width="24" height="22" fill="{INK}"/><rect x="{cx+14}" y="{cy+6}" width="24" height="22" fill="{INK}"/>'
            f'<rect x="{cx-16}" y="{cy+40}" width="32" height="44" fill="{WHITE}"/>')
g=(txt(300,46,"TON LOGEMENT FERMÉ « EN ATTENDANT »",17,TEAL,800,ls=1)+house(140,170)
   +f'<rect x="56" y="268" width="168" height="44" rx="22" fill="{INK}"/>'+txt(140,297,"Il rapporte 0 €.",19,WHITE,800)
   +txt(432,96,"Mais il te coûte toujours",20,INK,800))
for k,t in enumerate(["la taxe foncière,","l’assurance,","les charges,","et l’entretien."]):
    y=116+k*50
    g+=f'<rect x="300" y="{y}" width="268" height="40" rx="10" fill="{WHITE}"/><circle cx="324" cy="{y+20}" r="11" fill="{MANGO}"/><rect x="318" y="{y+18}" width="12" height="4" fill="{WHITE}"/>'+txt(346,y+27,t,19,INK,700,anchor="start")
out["02-ferme"]=svg(600,340,g,GREY_L)

# 03 COMBIEN DE TEMPS TU T'ENGAGES
g=txt(300,46,"AVEC UN BAIL CLASSIQUE, TU T’ENGAGES",17,TEAL,800,ls=1)
for k,(t,l,w,col) in enumerate([("En location vide","pour 3 ans minimum, si tu es un particulier.",552,GREY),("En meublé","pour 1 an, et le bail repart tout seul.",190,GREY)]):
    y=80+k*112
    g+=txt(24,y+4,t,21,INK,800,anchor="start")+txt(24,y+34,l,19,INK,600,anchor="start")
    g+=f'<rect x="24" y="{y+52}" width="552" height="18" rx="9" fill="{WHITE}"/><rect x="24" y="{y+52}" width="{w}" height="18" rx="9" fill="{col}"/>'
g+=txt(300,330,"Et pour récupérer ton logement, il faut attendre",19,MANGO_D,800)+txt(300,356,"la fin du bail.",19,MANGO_D,800)
out["03-durees"]=svg(600,380,g,TEAL_L)

# 04 LE BAIL MOBILITÉ
def ic4(cx,cy,k,h):
    if k==0: return f'<rect x="{cx-22}" y="{cy-6}" width="44" height="20" rx="5" fill="{TEAL}"/><rect x="{cx-16}" y="{cy-16}" width="32" height="12" rx="4" fill="{TEAL_M}"/>'
    if k==1: return f'<rect x="{cx-22}" y="{cy-20}" width="44" height="40" rx="6" fill="{TEAL}"/><rect x="{cx-22}" y="{cy-20}" width="44" height="12" rx="4" fill="{TEAL_D}"/>'+txt(cx,cy+14,"1-10",13,WHITE,800)
    if k==2: return f'<circle cx="{cx}" cy="{cy}" r="21" fill="{TEAL}"/><rect x="{cx-8}" y="{cy-8}" width="16" height="16" rx="2" fill="{WHITE}"/>'
    return f'<circle cx="{cx}" cy="{cy}" r="21" fill="{MANGO}"/>'+txt(cx,cy+8,"0 €",15,WHITE,800)
rows=[("",["C’est pour un logement meublé."]),("",["Tu choisis la durée, de 1 à 10 mois."]),("",["Il s’arrête tout seul à la date prévue."]),("",["Aucun dépôt de garantie n’est demandé."])]
out["04-bail"]=rowcards(rows,TEAL_L,icon_fn=ic4,head="LE BAIL MOBILITÉ, CRÉÉ EN 2018")

# 06 À QUI TU PEUX LOUER
items=["en études supérieures","en apprentissage","en stage","en service civique","muté pour son travail","en mission temporaire","en formation professionnelle"]
g=txt(300,46,"QUAND IL ENTRE DANS LES LIEUX, TON LOCATAIRE EST…",17,TEAL,800,ls=1)
for k,it in enumerate(items):
    col=k%2; row=k//2; x=24+col*282; y=70+row*62
    w=270
    if k==6: x=130; w=340
    g+=f'<rect x="{x}" y="{y}" width="{w}" height="50" rx="12" fill="{WHITE}"/>'+check(x+28,y+25,TEAL,r=13)+txt(x+52,y+32,it,18,INK,700,anchor="start")
g+=txt(300,346,"Et ce motif doit être écrit dans le bail.",19,MANGO_D,800)
out["06-qui"]=svg(600,372,g,TEAL_L)

# 09 LA LISTE DU MEUBLÉ
items=["Literie avec couverture","Rideaux ou volets","Plaques de cuisson","Four ou micro-ondes","Frigo avec congélation","Vaisselle","Ustensiles de cuisine","Table et sièges","Étagères","Luminaires","Matériel d’entretien"]
g=txt(300,46,"LA LISTE MINIMUM DU MEUBLÉ",17,TEAL,800,ls=2)
for k,it in enumerate(items):
    col=0 if k<6 else 1; row=k if k<6 else k-6; x=24+col*290; y=88+row*50
    g+=f'<rect x="{x}" y="{y-18}" width="26" height="26" rx="6" fill="none" stroke="{TEAL}" stroke-width="3"/>'+txt(x+38,y+2,it,19,INK,700,anchor="start")
g+=txt(300,404,"Il manque quelque chose ? Complète avant de louer.",19,MANGO_D,800)
out["09-meuble"]=svg(600,428,g,WHITE)

# 11 CE QUE TON BAIL DOIT DIRE
rows=[("",["La durée du bail."]),("",["Le motif de ton locataire (stage, mutation…)."]),("",["Que c’est un bail mobilité, avec le texte de loi","qui l’encadre."]),("",["Qu’aucun dépôt de garantie n’est demandé."]),("",["Le montant forfaitaire des charges."])]
g0=rowcards(rows,GREY_L,icon_fn=lambda cx,cy,k,h: check(cx,cy,TEAL,r=16),size_l=20,head="CE QUE TON BAIL DOIT DIRE")
out["11-mentions"]=g0

# 12 QUI PEUT METTRE FIN AU BAIL
g=txt(300,46,"QUI PEUT METTRE FIN AU BAIL ?",17,TEAL,800,ls=2)
for k,(t,lines,fill,col) in enumerate([("TON LOCATAIRE",["Il peut partir","quand il veut,","en te prévenant","1 mois avant."],TEAL,WHITE),("TOI",["Tu ne peux pas","le faire partir","avant la fin, sauf","faute de sa part."],WHITE,INK)]):
    x=24+k*282
    g+=f'<rect x="{x}" y="70" width="270" height="206" rx="16" fill="{fill}"/>'+txt(x+135,106,t,16,PEACH if fill==TEAL else MANGO_D,800,ls=2)
    g+="".join(txt(x+135,148+j*30,l,21,col,800) for j,l in enumerate(lines))
out["12-preavis"]=svg(600,300,g,TEAL_L)

# 13 MURIELLE
rows=[("Si elle laisse son T2 vide","0 €",["de loyers, et les frais tombent quand même."],GREY_L,INK),
      ("Avec un bail meublé classique","1 an",["d’engagement, alors qu’elle rentre dans 8 mois."],WHITE,INK),
      ("Avec un bail mobilité de 8 mois","5 200 €",["de loyers (8 mois à 650 €), et son T2 est","libre le jour de son retour."],TEAL,WHITE)]
out["13-murielle"]=bigcards(rows,MANGO_L)

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

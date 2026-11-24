exec(open("/tmp/claude-0/-home-claude/901306cc-9835-5f2f-8144-8b453c5d989e/scratchpad/_head.py").read())
exec(open("/tmp/claude-0/-home-claude/901306cc-9835-5f2f-8144-8b453c5d989e/scratchpad/_common.py").read())
out={}
P=json.loads(sys.argv[3]); ONLY=P.get("only")
out["00-will-salut"]=will_panel(P["accueil"],["Salut","la famille ! 🔥"],h=330)
out["06-will"]=will_panel(P["relance"],["Et puis…","plus rien."])
out["09-will-methode"]=will_panel(P["methode"],["On suit","l’ordre,","étape","par étape."])
out["17-will-fin"]=will_panel(P["signature"],["C’était Will.","Ciao ! 🔥"],h=330)

def helmet(cx,cy,s=1,col=MANGO):
    g=(f'<path d="M{cx-58} {cy} a58 54 0 0 1 116 0 z" fill="{col}"/>'
       f'<rect x="{cx-76}" y="{cy-4}" width="152" height="16" rx="8" fill="{col}"/>'
       f'<rect x="{cx-8}" y="{cy-60}" width="16" height="56" rx="6" fill="{MANGO_D}"/>')
    return f'<g transform="translate({cx} {cy}) scale({s}) translate({-cx} {-cy})">{g}</g>'
def shield(cx,cy,col=PEACH):
    return (f'<path d="M{cx} {cy-36} q34 6 34 6 q0 40 -34 62 q-34 -22 -34 -62 q0 0 34 -6 z" fill="{col}" stroke="{WHITE}" stroke-width="3"/>'
            f'<path d="M{cx-14} {cy-2} l10 10 l20 -22" fill="none" stroke="{TEAL}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>')

# 01 COUVERTURE
ban=base64.b64encode(open(sys.argv[2],"rb").read()).decode()
out["01-hero"]=hero(ban,156,"Ton chantier peut ruiner","ton investissement.",helmet(286,470,1.0)+shield(390,446))

# 02 CE QUE ÇA COÛTE
def coin(cx,cy): return f'<circle cx="{cx}" cy="{cy}" r="34" fill="{MANGO}"/>'+txt(cx,cy+12,"€",34,WHITE,800)
def clock(cx,cy): return f'<circle cx="{cx}" cy="{cy}" r="34" fill="{TEAL}"/><path d="M{cx} {cy-20} v22 l14 10" stroke="{WHITE}" stroke-width="6" fill="none" stroke-linecap="round"/>'
def moon(cx,cy): return f'<circle cx="{cx}" cy="{cy}" r="34" fill="{INK}"/><path d="M{cx+8} {cy-22} a22 22 0 1 0 14 30 a18 18 0 0 1 -14 -30 z" fill="{PEACH}"/>'
g=""
for k,(ic,l1,l2) in enumerate([(coin,"Des loyers","perdus."),(clock,"Du temps","gaspillé."),(moon,"Des nuits","blanches.")]):
    x=110+k*190
    g+=ic(x,76)+txt(x,152,l1,22,INK,800)+txt(x,180,l2,22,INK,800)
out["02-cout"]=svg(600,206,g,MANGO_L)

# 03 LES TROIS GARANTIES DE LA RÉCEPTION
rows=[("Parfait achèvement","1 an",48,["Les défauts notés à la réception,","et ceux qui apparaissent dans l’année."]),
      ("Bon fonctionnement","2 ans",96,["Les équipements qu’on peut enlever","sans abîmer le bâti."]),
      ("Décennale","10 ans",480,["Les dommages graves, qu’on ne","pouvait pas voir à la réception."])]
g=(f'<rect x="40" y="22" width="150" height="34" rx="17" fill="{INK}"/>'+txt(115,45,"RÉCEPTION",16,WHITE,800,ls=2)
   +f'<line x1="60" y1="56" x2="60" y2="{56+3*136}" stroke="{INK}" stroke-width="3" stroke-dasharray="6 6"/>')
for k,(t,d,w,lines) in enumerate(rows):
    y=74+k*136
    g+=(txt(76,y+18,t,21,INK,800,anchor="start")+txt(560,y+18,d,22,MANGO_D,800,anchor="end")
        +f'<rect x="60" y="{y+30}" width="{w}" height="18" rx="9" fill="{TEAL if k==2 else MANGO}"/>'
        +"".join(txt(76,y+78+j*28,l,19,INK,600,anchor="start") for j,l in enumerate(lines)))
out["03-garanties"]=svg(600,74+3*136+4,g,WHITE)

# 05 LA RETENUE DE GARANTIE
steps=[("Jusqu’à 5 %","du prix TTC","mis de côté."),("Bloqués","chez un tiers","choisi à deux."),("1 an","après réception,","rendus à l’artisan.")]
g=""
for k,(big,l1,l2) in enumerate(steps):
    x=24+k*188
    g+=f'<rect x="{x}" y="24" width="176" height="176" rx="16" fill="{WHITE}"/>'
    g+=txt(x+88,82,big,30 if len(big)<9 else 25,MANGO_D,800)+txt(x+88,128,l1,18,INK,700)+txt(x+88,154,l2,18,INK,700)
g+=txt(300,234,"Mais si les réserves ne sont pas levées d’ici là,",19,INK,600)+txt(300,260,"tu peux t’opposer à leur restitution par une lettre",19,INK,600)+txt(300,286,"recommandée motivée, envoyée au tiers qui les garde.",19,INK,600)
out["05-retenue"]=svg(600,310,g,TEAL_L)

# 10 VÉRIFIER L'ARTISAN
rows=[("Son numéro SIRET,",["vérifié sur l’Annuaire des entreprises."]),("Son attestation décennale,",["en cours, et pour les travaux confiés."]),("Un devis écrit et détaillé,",["poste par poste, avec les délais."])]
out["10-verif"]=rowcards(rows,TEAL_L,icon_fn=lambda cx,cy,k,h: check(cx,cy,TEAL,r=18))

# 11 PAYER AU RYTHME DU CHANTIER
steps=[("À la commande","tu verses un acompte raisonnable."),("À chaque étape visible","tu paies ce qui est fait."),("Après la réception","tu paies le solde."),("1 an après la réception","les 5 % retenus sont rendus.")]
g=""; y=24
g+=f'<line x1="70" y1="{y+40}" x2="70" y2="{y+40+3*104}" stroke="{TEAL_M}" stroke-width="5"/>'
for k,(quand,quoi) in enumerate(steps):
    yy=y+k*104
    g+=f'<circle cx="70" cy="{yy+40}" r="14" fill="{TEAL}" stroke="{WHITE}" stroke-width="4"/>'
    g+=f'<rect x="112" y="{yy}" width="464" height="88" rx="14" fill="{WHITE}"/>'+txt(132,yy+36,quand,21,MANGO_D,800,anchor="start")+txt(132,yy+68,quoi,21,INK,600,anchor="start")
out["11-paiements"]=svg(600,y+4*104+10,g,MANGO_L)

# 12 LA RÉCEPTION
items=["Ouvre les robinets.","Teste chaque prise.","Manœuvre chaque fenêtre.","Regarde les joints de près."]
g=""
for k,t in enumerate(items):
    x=24+(k%2)*282; y=24+(k//2)*96
    g+=f'<rect x="{x}" y="{y}" width="270" height="84" rx="14" fill="{WHITE}"/>'+check(x+36,y+42,TEAL,r=16)
    words=t.split(" ");
    if len(t)>18:
        cut=len(words)//2 if len(words)>2 else 1
        g+=txt(x+64,y+38,(" ".join(words[:cut])),19,INK,700,anchor="start")+txt(x+64,y+64," ".join(words[cut:]),19,INK,700,anchor="start")
    else:
        g+=txt(x+64,y+50,t,19,INK,700,anchor="start")
g+=f'<rect x="24" y="224" width="552" height="70" rx="14" fill="{MANGO}"/>'+txt(300,256,"Et note chaque défaut dans le procès-verbal,",19,WHITE,800)+txt(300,282,"avec des photos datées.",19,WHITE,800)
out["12-reception"]=svg(600,318,g,TEAL_L)

# 13 LE DOSSIER CHANTIER
items=["Le devis signé","L’attestation d’assurance","Les factures","Les photos","Le procès-verbal de réception"]
g=(f'<path d="M60 52 h120 l20 22 h340 v270 h-480 z" fill="{MANGO}"/>'
   f'<rect x="60" y="80" width="480" height="264" rx="8" fill="{WHITE}" stroke="{MANGO}" stroke-width="4"/>'
   + txt(300,120,"Ton dossier chantier",25,TEAL,800))
for k,t in enumerate(items):
    y=160+k*36
    g+=check(104,y-7,TEAL,r=12)+txt(128,y,t,20,INK,700,anchor="start")
out["13-dossier"]=svg(600,368,g,MANGO_L)

# 14 L'EXEMPLE
rows=[("Si tu paies la moitié au départ","8 000 €",["versés pour des travaux jamais faits."],GREY_L,INK),
      ("Si tu paies au rythme du chantier","1 000 €",["versés pour des travaux jamais faits."],TEAL,WHITE)]
out["14-exemple"]=bigcards(rows,MANGO_L)

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

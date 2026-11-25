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

# 03 CE QUE L'ARTISAN TE DOIT APRÈS LA RÉCEPTION
def dur(cx,cy,k,h):
    t=["1 an","2 ans","10 ans"][k]
    return f'<rect x="{cx-42}" y="{cy-30}" width="84" height="60" rx="12" fill="{[MANGO,MANGO,TEAL][k]}"/>'+txt(cx,cy+8,t,22,WHITE,800)
rows=[("Il répare tous les défauts,",["ceux notés à la réception et ceux","qui apparaissent dans l’année."]),
      ("Il répare les équipements posés",["pendant les travaux, s’ils","tombent en panne."]),
      ("Son assurance décennale paie",["si un dommage grave apparaît."])]
g=txt(300,48,"APRÈS LA RÉCEPTION, L’ARTISAN RESTE RESPONSABLE",17,TEAL,800,ls=1)
y=70
for k,(t,lines) in enumerate(rows):
    hh=54+30*len(lines)
    g+=f'<rect x="24" y="{y}" width="552" height="{hh}" rx="14" fill="{WHITE}"/>'+dur(84,y+hh/2,k,False)
    g+=txt(146,y+38,t,21,INK,800,anchor="start")+"".join(txt(146,y+68+jj*28,l,19,INK,600,anchor="start") for jj,l in enumerate(lines))
    y+=hh+12
out["03-garanties"]=svg(600,y+12,g,TEAL_L)

# 05 LA RETENUE DE GARANTIE
def ic5(cx,cy,k,h):
    if k==0: return f'<rect x="{cx-16}" y="{cy-4}" width="32" height="24" rx="4" fill="{TEAL}"/><path d="M{cx-10} {cy-4} v-8 a10 10 0 0 1 20 0 v8" stroke="{TEAL}" stroke-width="5" fill="none"/>'
    if k==1: return check(cx,cy,MANGO,r=20)
    if k==2: return f'<circle cx="{cx}" cy="{cy}" r="20" fill="{TEAL}"/>'+txt(cx,cy+8,"€",22,WHITE,800)
    return f'<circle cx="{cx}" cy="{cy}" r="20" fill="{INK}"/><path d="M{cx-9} {cy-9} l18 18 M{cx+9} {cy-9} l-18 18" stroke="{WHITE}" stroke-width="5" stroke-linecap="round"/>'
rows=[("L’argent ne reste pas chez toi.",["Il est bloqué chez un intermédiaire choisi","ensemble, par exemple un notaire."]),
      ("Pendant ce temps,",["l’artisan corrige les réserves."]),
      ("Au plus tard 1 an après la réception,",["l’argent lui est versé."]),
      ("Défauts toujours là ?",["Écris en recommandé à cet intermédiaire, en","expliquant ce qui n’est pas réparé. L’argent","reste alors bloqué."])]
out["05-retenue"]=rowcards(rows,TEAL_L,icon_fn=ic5,size_t=20,size_l=19)

# 10 VÉRIFIER L'ARTISAN
rows=[("Son numéro SIRET,",["l’identité de son entreprise, à vérifier","sur le site Annuaire des entreprises."]),("Son attestation d’assurance décennale,",["encore valable, et qui couvre bien","tes travaux."]),("Un devis écrit et détaillé,",["poste par poste, avec les délais."])]
out["10-verif"]=rowcards(rows,TEAL_L,icon_fn=lambda cx,cy,k,h: check(cx,cy,TEAL,r=18))

# 11 PAYER AU RYTHME DU CHANTIER
steps=[("À la commande","un petit acompte, pas la moitié."),("À chaque étape visible","tu paies ce qui est fait."),("Après la réception","le reste, moins les 5 % retenus."),("1 an après la réception","l’artisan reçoit ces 5 %.")]
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
rows=[("Si tu as versé la moitié au départ","8 000 €",["payés pour rien, puisque tu as versé","10 000 € pour 2 000 € de travaux."],GREY_L,INK),
      ("Si tu as payé au fur et à mesure","1 000 €",["payés pour rien, puisque tu as versé","3 000 € pour 2 000 € de travaux."],TEAL,WHITE)]
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

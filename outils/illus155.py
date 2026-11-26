exec(open(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)),"_head.py")).read())
exec(open(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)),"_common.py")).read())
out={}
P=json.loads(sys.argv[3]); ONLY=P.get("only")
out["00-will-salut"]=will_panel(P["accueil"],["Salut","la famille ! 🔥"],h=330)
out["06-will"]=will_panel(P["relance"],["Tu vois où","je veux en","venir ?"])
out["09-will-methode"]=will_panel(P["methode"],["Il te faut","juste le","bon ordre."])
out["17-will-fin"]=will_panel(P["signature"],["C’était Will.","Ciao ! 🔥"],h=330)

def unfinished(cx,cy,s=1,wall=WHITE,rebar=GREY_L):
    g=(f'<rect x="{cx-70}" y="{cy-30}" width="140" height="80" fill="{wall}"/>'
       f'<rect x="{cx-80}" y="{cy-40}" width="160" height="12" fill="{GREY}"/>'
       f'<rect x="{cx-14}" y="{cy+10}" width="28" height="40" fill="{TEAL_D}"/>'
       f'<rect x="{cx-56}" y="{cy-8}" width="26" height="22" fill="{TEAL_M}"/><rect x="{cx+30}" y="{cy-8}" width="26" height="22" fill="{TEAL_M}"/>')
    for k in range(6):
        x=cx-70+k*28
        g+=f'<path d="M{x} {cy-40} v-44 q0 -8 8 -8" stroke="{rebar}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    return f'<g transform="translate({cx} {cy}) scale({s}) translate({-cx} {-cy})">{g}</g>'
def pause(cx,cy,r=30,col=MANGO):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}"/><rect x="{cx-r*0.33}" y="{cy-r*0.4}" width="{r*0.22}" height="{r*0.8}" rx="2" fill="{WHITE}"/><rect x="{cx+r*0.11}" y="{cy-r*0.4}" width="{r*0.22}" height="{r*0.8}" rx="2" fill="{WHITE}"/>'

# 01 COUVERTURE
ban=base64.b64encode(open(sys.argv[2],"rb").read()).decode()
out["01-hero"]=hero(ban,155,"Ta maison inachevée","te coûte cher.",unfinished(286,478,0.9,WHITE,PEACH)+f'<path d="M380 392 h36 l-18 26 l18 26 h-36 l18 -26 z" fill="{MANGO}"/><rect x="376" y="386" width="44" height="7" rx="3" fill="{PEACH}"/><rect x="376" y="441" width="44" height="7" rx="3" fill="{PEACH}"/>')

# 02 CE QUE FAIT TON ARGENT PENDANT CE TEMPS
rows=[("",["Ton argent ne te rapporte aucun loyer."]),("",["Il ne t’apporte ni confort, ni toit."]),("",["Il vieillit avec le chantier, au soleil,","sous la pluie et dans l’air marin."])]
out["02-dort"]=rowcards(rows,MANGO_L,icon_fn=lambda cx,cy,k,h: cross(cx,cy,MANGO,r=18),size_l=21)

# 03 LE PERMIS
g=txt(300,50,"TON PERMIS N’EST PLUS VALABLE DANS DEUX CAS",18,MANGO_D,800,ls=1)
cas=[("1","Les travaux n’ont pas commencé","dans les 3 ans qui suivent son obtention."),
     ("2","Passé ces 3 ans, le chantier s’arrête","pendant plus d’un an d’affilée.")]
for k,(n,l1,l2) in enumerate(cas):
    y=74+k*112
    g+=(f'<rect x="24" y="{y}" width="552" height="98" rx="16" fill="{WHITE}"/>'
        + f'<circle cx="66" cy="{y+49}" r="22" fill="{TEAL}"/>' + txt(66,y+57,n,23,WHITE,800)
        + txt(106,y+42,l1,21,INK,800,anchor="start")+txt(106,y+72,l2,20,INK,600,anchor="start"))
out["03-permis"]=svg(600,74+2*112+14,g,MANGO_L)

# 04 À L'ABRI OU À L'ARRÊT
def piggy(cx,cy,col=GREY):
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="54" ry="40" fill="{col}"/><circle cx="{cx+50}" cy="{cy-4}" r="14" fill="{col}"/>'
            f'<rect x="{cx-34}" y="{cy+30}" width="14" height="22" rx="4" fill="{col}"/><rect x="{cx+18}" y="{cy+30}" width="14" height="22" rx="4" fill="{col}"/>'
            f'<rect x="{cx-14}" y="{cy-36}" width="28" height="7" rx="3" fill="{WHITE}"/><circle cx="{cx+28}" cy="{cy-12}" r="4" fill="{WHITE}"/>')
g=(piggy(150,130)+pause(450,130,52)
   + f'<circle cx="300" cy="130" r="26" fill="{INK}"/>'+txt(300,138,"VS",18,WHITE,800)
   + txt(150,238,"CE QU’ON CROIT",18,GREY,800,ls=2)+txt(150,272,"Ton argent est à l’abri.",21,INK,800)
   + txt(450,238,"EN RÉALITÉ",18,MANGO_D,800,ls=2)+txt(450,272,"Ton argent est à l’arrêt.",21,INK,800))
out["04-abri"]=svg(600,304,g,WHITE)

# 10 LA FEUILLE DU COMPTE
g=(f'<rect x="60" y="24" width="480" height="300" rx="10" fill="{WHITE}" transform="rotate(-1.5 300 174)"/>'
   + txt(300,76,"Ce qui dort dans ton chantier",25,TEAL,800))
for k,(lab,val,col) in enumerate([("Ce que tu as mis, hors terrain","……… €",INK),("Depuis combien d’années","……… ans",INK),("Ce que ça t’a rapporté","0 €",MANGO)]):
    y=124+k*66
    g+=f'<line x1="90" y1="{y+24}" x2="510" y2="{y+24}" stroke="{GREY_L}" stroke-width="2"/>'+txt(96,y,lab,19,INK,700,anchor="start")+txt(504,y,val,21,col,800,anchor="end")
out["10-compte"]=svg(600,346,g,MANGO_L)

# 11 PROLONGER LE PERMIS
g=(txt(300,4,"",1)+f'<rect x="30" y="30" width="270" height="44" rx="10" fill="{TEAL}"/>'+txt(165,59,"Ton permis",20,WHITE,800)
   + f'<rect x="306" y="30" width="128" height="44" rx="10" fill="{WHITE}" stroke="{MANGO}" stroke-width="3" stroke-dasharray="8 6"/>'+txt(370,59,"+ 1 an",20,MANGO_D,800)
   + f'<rect x="440" y="30" width="128" height="44" rx="10" fill="{WHITE}" stroke="{MANGO}" stroke-width="3" stroke-dasharray="8 6"/>'+txt(504,59,"+ 1 an",20,MANGO_D,800)
   + f'<path d="M272 80 v34" stroke="{MANGO}" stroke-width="4"/><path d="M272 76 l-8 12 h16 z" fill="{MANGO}"/>'
   + txt(272,142,"Ta demande, au moins",20,MANGO_D,800)+txt(272,168,"2 mois avant la fin.",20,MANGO_D,800)
   + txt(300,216,"Tu peux le prolonger d’un an, jusqu’à 2 fois,",20,INK,600)
   + txt(300,244,"si les règles de construction de ta commune",20,INK,600)+ txt(300,270,"n’ont pas changé.",20,INK,600))
out["11-prolonger"]=svg(600,298,g,TEAL_L)

# 12 LA PARTIE QUI PEUT RAPPORTER EN PREMIER
def ic12(cx,cy,k,h):
    if k==0: return unfinished(cx,cy+10,0.36,TEAL,GREY)
    if k==1: return f'<rect x="{cx-22}" y="{cy-18}" width="44" height="38" fill="{TEAL}"/><polygon points="{cx-28},{cy-16} {cx},{cy-36} {cx+28},{cy-16}" fill="{TEAL}"/><rect x="{cx-7}" y="{cy}" width="14" height="20" fill="{WHITE}"/>'
    return f'<rect x="{cx-26}" y="{cy-30}" width="52" height="28" fill="{GREY_L}" stroke="{GREY}" stroke-width="2" stroke-dasharray="5 4"/><rect x="{cx-26}" y="{cy}" width="52" height="28" fill="{TEAL}"/>'
rows=[("Un rez-de-chaussée",["dont les murs et la dalle sont faits."]),("Un studio",["avec sa propre entrée."]),("Un étage entier,",["pendant que l’autre étage attend."])]
out["12-parties"]=rowcards(rows,TEAL_L,icon_fn=ic12,head="CE QUI PEUT SE LOUER EN PREMIER")

# 14 RODRIGUE
rows=[("S’il continue comme avant","0 €",["de loyers sur les 3 prochaines années."],GREY_L,INK),
      ("S’il met le rez-de-chaussée au travail","18 000 €",["de loyers sur 3 ans, soit 30 mois à 600 €,","après 6 mois de travaux."],TEAL,WHITE)]
out["14-rodrigue"]=bigcards(rows,MANGO_L)

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

# -*- coding: utf-8 -*-
"""#151 v3 : édition complète, couleurs de la bannière (teal + orange + neutres)."""
import sys, re
BG="#FBF5EC"; INK="#1E2A2F"; MUTED="#6B767B"; TEAL="#136D68"; TEAL_L="#DDEFEC"; ORANGE="#E57638"; ORANGE_L="#FDEADB"; PEACH="#FFD3AE"; GREY_L="#E9E3D9"
FONT="Arial,Helvetica,sans-serif"
LINK_SUB="https://www.mouvementlyannaj.com/lm-journal-debrouya-v2/"
LINK_IG="https://www.instagram.com/william.synesius?igsh=MXBzM2V3eWV2MHppOQ=="
LINK_YT="https://youtube.com/@williamsynesius?si=BuRt8bjDLE6m0Dnf"

def p(t,size=18,color=INK,w="normal",align="left",mb=18):
    return f'<p style="margin:0 0 {mb}px 0;font-family:{FONT};font-size:{size}px;line-height:1.6;color:{color};font-weight:{w};text-align:{align};">{t}</p>'
def _phrases(t):
    """Découpe en phrases, sans couper à l'intérieur d'une balise HTML ni de guillemets « ».""" 
    out=[];cur="";depth=0;guil=0;i=0
    while i<len(t):
        c=t[i];cur+=c
        if t.startswith("<",i):
            j=t.index(">",i); tag=t[i:j+1]; cur+=t[i+1:j+1]; i=j+1
            if tag.startswith("</"): depth-=1
            elif not tag.endswith("/>") and not tag.startswith("<br"): depth+=1
            continue
        if c=="«": guil+=1
        if c=="»": guil-=1
        if c in ".!?…" and depth==0 and guil==0:
            k=i+1
            while k<len(t) and t[k] in ".!?…»)": cur+=t[k]; k+=1
            if k<len(t) and t[k]==" " and k+1<len(t) and (t[k+1].isupper() or t[k+1] in "«(<"):
                out.append(cur.strip()); cur=""; i=k+1; continue
            i=k; continue
        i+=1
    if cur.strip(): out.append(cur.strip())
    return out
def P(t,size=18,color=INK,w="normal",align="left",mb=18,maxc=170):
    """Paragraphe aéré : 1 à 2 phrases courtes par bloc, comme dans le doc d'origine."""
    if "|" in t:
        blocs=[x.strip() for x in t.split("|")]
        return "".join(p(x,size,color,w,align,mb if k==len(blocs)-1 else 18) for k,x in enumerate(blocs))
    ph=_phrases(t); blocs=[]; cur=""
    vis=lambda s: len(re.sub(r"<[^>]+>","",s))
    for s_ in ph:
        if cur and (vis(cur)>=90 or vis(s_)>=90 or vis(cur)+vis(s_)>140 or cur.count(". ")+cur.count("? ")+cur.count("! ")>=1):
            blocs.append(cur); cur=s_
        else: cur=(cur+" "+s_).strip()
    if cur: blocs.append(cur)
    return "".join(p(x,size,color,w,align,mb if k==len(blocs)-1 else 18) for k,x in enumerate(blocs))
def b(t): return f'<strong>{t}</strong>'
def gap(h): return f'<div style="height:{h}px;line-height:{h}px;font-size:1px;">&nbsp;</div>'
def img(name, alt, mb=26, ext="png", radius=0):
    r=f"border-radius:{radius}px;" if radius else ""
    return f'<img src="img/{name}.{ext}" alt="{alt}" width="600" style="display:block;width:100%;max-width:600px;height:auto;border:0;{r}margin:0 0 {mb}px 0;">'
def card(inner,bg="#FFFFFF",pad=22,mb=24,bl=None):
    l=f"border-left:5px solid {bl};" if bl else ""
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:separate;margin:0 0 {mb}px 0;"><tr><td style="background:{bg};{l}border-radius:18px;padding:{pad}px;">{inner}</td></tr></table>'
def kicker(t,c=TEAL): return f'<p style="margin:0 0 6px 0;font-family:{FONT};font-size:13px;letter-spacing:3px;text-transform:uppercase;color:{c};font-weight:bold;">{t}</p>'
def h3(t): return f'<h3 style="margin:0 0 20px 0;font-family:{FONT};font-size:28px;line-height:1.2;color:{INK};font-weight:bold;">{t}</h3>'
def punch(t,size=24,align="center",mb=26): return f'<p style="margin:6px 0 {mb}px 0;font-family:{FONT};font-size:{size}px;line-height:1.35;color:{INK};font-weight:bold;text-align:{align};">{t}</p>'
def hl(t): return f'<span style="background:{ORANGE_L};box-shadow:0 0 0 3px {ORANGE_L};">{t}</span>'
def btn(label, href, bg, fg, border=None):
    bd=f"border:2px solid {border};" if border else f"border:2px solid {bg};"
    return (f'<a href="{href}" target="_blank" style="display:inline-block;background:{bg};{bd}color:{fg};text-decoration:none;'
            f'font-family:{FONT};font-size:16px;font-weight:bold;line-height:1.2;border-radius:30px;padding:12px 22px;margin:0 6px 10px 6px;">{label}</a>')
ICON_BASE="img/"
def social_btn(label, href, icon):
    return (f'<a href="{href}" target="_blank" style="display:inline-block;background:#FFFFFF;border:2px solid {TEAL};color:{TEAL};text-decoration:none;'
            f'font-family:{FONT};font-size:16px;font-weight:bold;line-height:22px;border-radius:30px;padding:11px 20px 11px 16px;margin:0 6px 10px 6px;min-width:118px;text-align:center;">'
            f'<img src="{ICON_BASE}{icon}.png" width="22" height="22" alt="" style="display:inline-block;width:22px;height:22px;border:0;vertical-align:middle;margin:0 8px 2px 0;">'
            f'<span style="vertical-align:middle;">{label}</span></a>')
def step(n,title):
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;margin:10px 0 16px 0;"><tr>'
            f'<td width="60" valign="middle" nowrap style="width:60px;min-width:60px;white-space:nowrap;padding:0 14px 0 0;"><div style="width:46px;height:46px;border-radius:23px;background:{ORANGE};color:{INK};text-align:center;font-family:{FONT};font-size:22px;line-height:46px;font-weight:bold;">{n}</div></td>'
            f'<td valign="middle"><h4 style="margin:0;font-family:{FONT};font-size:22px;line-height:1.25;color:{INK};font-weight:bold;">{title}</h4></td></tr></table>')
def warn(t): return (f'<tr><td width="30" valign="top" nowrap style="width:30px;min-width:30px;white-space:nowrap;padding:0 12px 10px 0;font-family:{FONT};font-size:18px;color:{ORANGE};font-weight:bold;">✕</td>'
                     f'<td valign="top" style="padding:0 0 10px 0;font-family:{FONT};font-size:17px;line-height:1.5;color:{INK};">{t}</td></tr>')

H=[]; A=H.append
def i(t): return f"<em>{t}</em>"
def ikicker(icon,t,c=TEAL):
    # icône dans sa colonne : la 2e ligne du titre s'aligne sous le texte, pas sous l'icône
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;margin:0 0 10px 0;"><tr>'
            f'<td width="30" valign="top" nowrap style="width:30px;min-width:30px;white-space:nowrap;padding:0 8px 0 0;font-size:18px;line-height:20px;">{icon}</td>'
            f'<td valign="top" style="font-family:{FONT};font-size:13px;line-height:20px;letter-spacing:3px;text-transform:uppercase;color:{c};font-weight:bold;">{t}</td></tr></table>')
def bullets(items, mark="→", color=None):
    color=color or TEAL
    rows="".join(f'<tr><td width="28" valign="top" nowrap style="width:28px;min-width:28px;white-space:nowrap;padding:0 10px 12px 0;font-family:{FONT};font-size:18px;font-weight:bold;color:{color};">{mark}</td><td valign="top" style="padding:0 0 12px 0;font-family:{FONT};font-size:18px;line-height:1.55;color:{INK};">{t}</td></tr>' for t in items)
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 6px 0;">{rows}</table>'
JPG={"01-hero","00-will-salut","06-will","09-will-methode","17-will-fin"}
def png(name,alt,mb=26): return img(name,alt,mb=mb,ext="jpg" if name in JPG else "png")


import json, os
CFG=json.load(open(sys.argv[2],encoding="utf-8")) if len(sys.argv)>2 else {}
NB=CFG.get("abonnes")
TEM=CFG.get("temoignage")          # {"prenom":..., "paras":[...]}
PH=lambda t: f'<span style="background:#FFF3A0;color:#B00020;font-weight:bold;">{t}</span>'

T_=CFG.get("textes",{})
X=lambda k,d: T_.get(k,d)
# ---------------- EN-TÊTE ----------------
A(png("01-hero","Le Journal Débrouya, édition #154 : acheter un bien déjà loué.",mb=20))
A(png("00-will-salut","Will : Salut la famille !",mb=20))
nb=b(NB) if NB else PH("[NB ABONNÉS]")
A(P(f"Bienvenue aux {nb} nouveaux abonnés qui nous ont rejoints depuis la dernière édition ! Si tu en fais partie, on est très heureux de te compter parmi les membres de la communauté des Débrouya.",size=17,mb=14))
A(P("Si le contenu te plaît, partage-le : c’est la plus belle façon de nous soutenir.",size=17,mb=12))
A(f'<p style="margin:0 0 18px 0;text-align:center;">{btn("Invite tes amis à&nbsp;s’abonner&nbsp;→",LINK_SUB,ORANGE,INK)}</p>')
A(P("📲 Tu veux accéder à nos derniers contenus avant tout le monde ? Rejoins-nous sur :",size=16,color=MUTED,align="center",mb=10))
A(f'<p style="margin:0 0 28px 0;text-align:center;">{social_btn("Instagram",LINK_IG,"instagram")}{social_btn("YouTube",LINK_YT,"youtube")}</p>')

T1="L'annonce que tu fais défiler trop&nbsp;vite"; T2="Le locataire en place, un atout pour l'investisseur"; T3="Ce que la loi dit vraiment"; T4="Ta méthode en 4&nbsp;étapes pour acheter&nbsp;loué"; T5="L'exemple chiffré, pour que ce soit&nbsp;clair"
prog=[T1,T2,T3,T4,T5]
rows="".join(f'<tr><td width="38" valign="top" nowrap style="width:38px;min-width:38px;white-space:nowrap;padding:0 12px 12px 0;font-family:{FONT};font-size:20px;font-weight:bold;color:{PEACH};">{k+1}.</td><td valign="top" style="padding:1px 0 12px 0;font-family:{FONT};font-size:17px;line-height:1.45;color:#FFFFFF;">{t}</td></tr>' for k,t in enumerate(prog))
A(card(kicker("Au programme aujourd'hui",PEACH)+gap(6)+f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table>',bg=TEAL))

if TEM:
    paras=TEM["paras"]
    q="".join(f'<p style="margin:0 0 {14 if k<len(paras)-1 else 0}px 0;font-family:Georgia,serif;font-size:18px;line-height:1.55;color:{INK};font-style:italic;">{t}</p>' for k,t in enumerate(paras))
    q+=f'<p style="margin:14px 0 0 0;font-family:{FONT};font-size:18px;font-weight:bold;color:{INK};">{TEM["prenom"]}</p>'
    tem=(p(f"Merci à {b(TEM['prenom'])} pour son témoignage ! {TEM['prenom']}, c'est un plaisir de t'avoir avec nous et de partager avec toi nos meilleures ressources chaque semaine. Son message :",size=16,mb=16)+
         f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;margin:0 0 16px 0;"><tr><td style="border-left:4px solid {ORANGE};padding:2px 0 2px 16px;">{q}</td></tr></table>')
else:
    tem=p(PH("[TÉMOIGNAGE À AJOUTER]"),size=16,mb=16)
A(card(kicker("Le témoignage de la semaine")+tem+
       p("(Tu veux toi aussi apparaître dans Le Journal Débrouya ? Envoie-nous ton témoignage en réponse à ce mail. Chaque semaine, on en sélectionne un que l’on partage avec la communauté ❤️)",size=14,color=MUTED,mb=0),bl=TEAL))

# ---------------- PARTIE 1 ----------------
A(gap(14)+kicker("Partie 1")+h3(T1))
A(P(f"Tu cherches un bien pour investir. Tu fais défiler les annonces.|Et d'un coup, tu tombes sur cette mention : {i('« vendu loué »')}.|Ton premier réflexe, c'est peut-être de passer à la suivante. Parce que dans ta tête, un locataire déjà dedans, c'est une contrainte :",mb=10))
A(bullets([i("« Je ne vais pas pouvoir choisir mon locataire. »"),i("« Et si c'est un mauvais payeur ? »")],color=ORANGE))
A(P("Ces craintes sont légitimes. On va y répondre.|Mais avant, je veux que tu regardes le problème dans l'autre sens."))
A(P(f"Quand tu achètes un bien {b('libre')} pour le louer, qu'est-ce qui se passe le lendemain de la signature ?",mb=18))
A(png("02-vide","Tu achètes libre, les premiers mois : tu fais les petits travaux, tu publies l’annonce, tu fais les visites, tu choisis ton locataire. Chaque mois, ta mensualité tombe. Et aucun loyer ne rentre.",mb=34))

# ---------------- PARTIE 2 ----------------
A(kicker("Partie 2")+h3(T2))
A(P(f"Voilà le changement de regard.|Pour quelqu'un qui veut habiter le logement, un locataire en place, c'est un obstacle.|Mais toi, tu n'achètes pas pour habiter. Tu achètes pour {b('louer')}. Et pour toi, tout s'inverse :",mb=18))
A(png("03-atouts","Ce que le locataire en place t’apporte : un loyer encaissé dès le premier mois ; un locataire dont tu connais les paiements depuis des mois ; un prix souvent plus bas.",mb=24))
A(P("Pourquoi moins cher ? Parce que celui qui veut y vivre ne peut pas s'y installer tout de suite. Le bien intéresse donc moins d'acheteurs."))
A(P(X("decote_intro",f"Une étude notariale l'explique simplement : {i('« Le plus souvent, le prix de vente d’un logement occupé est inférieur à celui d’un bien vide. »')} Elle donne des ordres de grandeur :"),mb=18))
A(png("04-decote",X("decote_alt","De combien le prix baisse, en général : la plupart des logements loués vides, 10 à 15 % ; petite surface louée vide, 5 à 10 % ; logement loué meublé, en général 0 %. Ordres de grandeur d'une étude notariale, qui dépendent du bail, du loyer et du locataire."),mb=24))
A(P(f"En meublé, les repères varient davantage d'une source à l'autre.|Tu vois l'idée : ce que les autres prennent pour un défaut, {b('toi, tu t’en sers pour négocier')}.",mb=34))

# ---------------- PARTIE 3 ----------------
A(kicker("Partie 3")+h3(T3))
A(P("Avant de foncer, il faut connaître les règles du jeu :",mb=18))
A(png("05-loi",X("loi_alt","Le jour où tu achètes : le bail continue avec toi, aux mêmes conditions (loyer, durée, clauses) ; la caution du locataire reste en principe engagée, sauf clause contraire ; l'assurance loyers impayés du vendeur ne se transfère pas ; le dépôt de garantie, c'est toi qui le rendras au locataire, même si tu ne l'as jamais reçu."),mb=24))
A(P(f"Autre point : {b('tu ne pourras pas reprendre le logement quand bon te semble')}.|Et si le logement est loué vide, la loi te fait patienter :",mb=18))
A(png("07-delais",X("delais_alt","Si un jour tu veux récupérer le logement. Pour le vendre libre : si le bail finit moins de 3 ans après ton achat, ton congé ne joue qu'à la fin du bail renouvelé une fois. Pour y habiter ou loger un proche : si le bail finit moins de 2 ans après ton achat, ton congé ne joue que 2 ans après ton achat. Et toujours prévenir à l'avance : 6 mois avant la fin du bail en location vide, 3 mois en meublé."),mb=18))
A(P(X("meuble","En meublé, les règles ne sont pas tout à fait les mêmes. Fais-toi confirmer ta situation par ton notaire ou par l'ADIL de ton département."),mb=24))
A(png("06-will","Will : On achète loué pour le garder loué.",mb=24))
A(punch(f"Pas pour le reprendre {hl('l’année prochaine')}.",size=21,mb=34))

# ---------------- PARTIE 4 ----------------
A(kicker("Partie 4")+h3(T4))
A(png("09-will-methode","Will : C’est parti, étape par étape.",mb=30))
A(step("1","Demande le dossier locatif complet avant ton offre"))
A(P("Ne fais pas d'offre à l'aveugle sur un bien loué. Le vendeur ou l'agence doit pouvoir te fournir :",mb=18))
A(png("10-dossier","Le bail signé et ses éventuels avenants ; l’état des lieux d’entrée ; les paiements des 12 derniers mois, quittances ou relevés de compte ; le montant du dépôt de garantie versé par le locataire à son entrée ; l’acte de caution du garant, s’il y en a un.",mb=18))
A(P(f"Un vendeur sérieux n'a aucune raison de refuser. {b('S’il bloque, pose-toi des questions.')}",mb=32))

A(step("2","Lis le bail comme si tu allais le signer toi-même"))
A(P("Parce que c'est un peu le cas : ce bail devient le tien. Regarde trois choses en priorité :",mb=18))
A(png("11-bail","À vérifier : la date de fin du bail, pour savoir où tu en es ; le type de location : vide ou meublée, les règles changent ; le loyer, comparé à ceux du quartier.",mb=18))
A(P(X("loyer",f"Un loyer trop bas, tu ne pourras pas le remonter comme tu veux en cours de bail. Alors fais ton calcul de rentabilité avec {b('le loyer réel')}, pas avec celui que tu espères."),mb=32))

A(step("3","Négocie le prix avec le dossier en main"))
A(P("Maintenant que tu as le dossier, tu sais sur quoi négocier le prix :",mb=10))
A(bullets(["le bien est occupé, donc il intéresse moins d’acheteurs ;","le loyer est en dessous du marché, si c’est le cas ;","l’historique montre des retards de paiement, s’il y en a."],color=TEAL))
A(P(X("depot_nego",f"Et surtout, règle la question du {b('dépôt de garantie')} noir sur blanc. Demande au notaire que son montant te soit remis le jour de la vente, par le vendeur."),mb=32))

A(step("4","Prends le relais proprement le jour de la signature"))
A(P("Ce jour-là, aie ces réflexes :",mb=10))
A(bullets(X("relais",[f"envoie tes {b('coordonnées')} au locataire : c'est une obligation pour le nouveau propriétaire ;",
                    "donne-lui par écrit le nouveau compte sur lequel verser le loyer ;",
                    f"vérifie ton {b('assurance')} de propriétaire : en copropriété, elle est obligatoire ;",
                    "et si tu veux une protection contre les impayés, mets-la en place : celle du vendeur ne te suit pas."]),color=TEAL))
A(P("Bref : tu n'achètes pas qu'un bien, tu reprends aussi une relation.",mb=10))
A(punch("Commence-la bien.",size=21,align="left",mb=34))

# ---------------- PARTIE 5 ----------------
A(kicker("Partie 5")+h3(T5))
A(P("Prenons un T3 en Martinique, loué vide à 700 € par mois hors charges. Le même type de T3, vendu libre dans le quartier, se négocie autour de 120 000 €.",mb=8))
A(P("(Un exemple fictif aux chiffres ronds, pas une moyenne du marché.)",size=14,color=MUTED))
A(P(f"Celui-ci est vendu loué. Après négociation, tu l'obtiens avec {b('10 % de décote')}, soit 108 000 €.|Compare avec le même T3 acheté libre, en comptant 2 mois sans loyer, le temps de le préparer et de trouver ton locataire :",mb=18))
A(png("13-exemple","Tu achètes le T3 libre : prix d’achat 120 000 € ; loyers perdus pendant 2 mois, 1 400 € ; rentabilité brute 7 % ; coût réel avant le premier loyer, 121 400 €. Tu achètes le T3 loué : prix d’achat 108 000 € ; loyers perdus, 0 € ; rentabilité brute 7,8 % ; coût réel avant le premier loyer, 108 000 €.",mb=18))
A(P("La rentabilité brute, ce sont les loyers de l'année (700 € × 12 = 8 400 €) divisés par le prix : <span style=\"white-space:nowrap;\">8 400 € ÷ 120 000 €</span>, contre <span style=\"white-space:nowrap;\">8 400 € ÷ 108 000 €</span>.",size=15,color=MUTED,mb=20))
A(card(p(f"Résultat : tu engages {b('13 400 €')} de moins pour le même loyer, et tu gagnes près de {b('0,8 point')} de rentabilité brute.",size=18,color="#FFFFFF",mb=8)+
       p("Sans compter les frais de notaire, qui baissent eux aussi avec le prix.",size=15,color=PEACH,mb=0),bg=TEAL,pad=22))
A(P(X("depot_ex",f"Et n'oublie pas le dépôt de garantie. En location vide, il est d'un mois de loyer hors charges au maximum, ici 700 €.|Si tu obtiens qu'il te soit remis chez le notaire, tu verses {b('700 € de moins')} le jour de la vente. Et le jour du départ du locataire, tu rends un argent que tu as déjà récupéré.")))
A(P("Bien sûr, ça marche seulement si le dossier tient la route. La décote ne compense pas tout, par exemple :",mb=10))
A(bullets(["un locataire qui paie mal ;","un loyer très en dessous du marché ;","un bail qui ne te convient pas."],color=TEAL))
A(P("C'est pour ça que l'étape 1 n'est pas optionnelle.",mb=24))
A(card(p(f"Quand le dossier est bon, {i('« vendu loué »')} n'est plus une mention à fuir.",size=17,color=PEACH,align="center",mb=10)+
       p("C'est le signe d'un bien qui travaille pour toi dès le premier mois.",size=22,color="#FFFFFF",w="bold",align="center",mb=0),bg=TEAL,pad=28,mb=30))

# ---------------- MENTORAT + SIGNATURE ----------------
A(card(kicker("Tu veux être accompagné ?")+
       p("Je te propose un programme de mentorat personnalisé :",mb=10)+bullets(["On regarde ta situation.","On définit ta stratégie.","On met en place un plan d'action sur mesure."],color=ORANGE)+
       p(b("Et surtout, on avance ensemble.")) +
       p("Intéressé ? Réponds simplement à ce mail avec le mot :",mb=12)+
       f'<p style="margin:0 0 14px 0;text-align:center;"><span style="display:inline-block;background:{ORANGE};color:{INK};border-radius:30px;padding:14px 30px;font-family:{FONT};font-size:22px;letter-spacing:2px;font-weight:bold;">MENTORAT</span></p>'+
       p("…et je te recontacterai pour en discuter. <em>Aucun engagement. Juste une conversation.</em>",size=15,color=MUTED,align="center",mb=0),bl=ORANGE,pad=22,mb=28))
A(png("17-will-fin","C'était Will. Ciao !",mb=22))
A(f'<div style="border-top:1px solid #E3DBCF;margin:0 0 16px 0;"></div>')
A(P("Qu'as-tu pensé de cette édition ? Dis-le-nous en répondant à ce mail (on lit tout !).",size=14,color=MUTED,align="center"))

body="\n".join(H)
def _txt(m):
    t=m.group(1).replace("'","’")
    t=re.sub(r"(\d) (?=\d{3}\b)",r"\1&nbsp;",t)
    t=re.sub(r"(\d) (?=[^\W\d_])",r"\1&nbsp;",t)
    t=re.sub(r"\b(\w+(?:-\w+)+)\b",r'<span style="white-space:nowrap;">\1</span>',t)
    t=re.sub(r" ([\u2600-\u27BF\U0001F300-\U0001FAFF][\u2600-\u27BF\U0001F300-\U0001FAFF\uFE0F\U0001F3FB-\U0001F3FF]*)",r'&nbsp;<span style="white-space:nowrap;">\1</span>',t)
    return ">"+t+"<"
body=re.sub(r">([^<]+)<",_txt,body)
body=re.sub(r'alt="([^"]*)"',lambda m:'alt="'+m.group(1).replace("'","’")+'"',body)
body=re.sub(r"(\d) ([€%])",r"\1&nbsp;\2",body)
body=re.sub(r" ([?!:;»])",r"&nbsp;\1",body).replace("« ","«&nbsp;")
html=f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light"><title>Journal Débrouya #154</title></head>
<body style="margin:0;padding:0;background:{BG};">
<!-- ===== DÉBUT DU BLOC À COLLER DANS LE BLOC HTML DE LEARNYBOX ===== -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{BG}" style="background:{BG};"><tr><td align="center" style="padding:14px 14px 30px 14px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;"><tr><td>
{body}
</td></tr></table></td></tr></table>
<!-- ===== FIN DU BLOC ===== -->
</body></html>'''
open(sys.argv[1],"w",encoding="utf-8").write(html); print(len(html.encode()),"octets")

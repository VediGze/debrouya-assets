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
JPG={"00-will-salut","06-will","09-will-methode","17-will-fin"}
def png(name,alt,mb=26): return img(name,alt,mb=mb,ext="jpg" if name in JPG else "png")


import json, os
CFG=json.load(open(sys.argv[2],encoding="utf-8")) if len(sys.argv)>2 else {}
NB=CFG.get("abonnes")
TEM=CFG.get("temoignage")          # {"prenom":..., "paras":[...]}
IJ=CFG.get("ij_max","42,97 €")
EMPLOYEUR=CFG.get("employeur","Alors oui, si tu as au moins <strong>un an d’ancienneté</strong>, ton employeur doit compléter tes indemnités à partir du 8<sup>e</sup> jour d'arrêt. Tu touches :")
PH=lambda t: f'<span style="background:#FFF3A0;color:#B00020;font-weight:bold;">{t}</span>'

# ---------------- EN-TÊTE ----------------
A(png("01-hero","Le Journal Débrouya, édition #153 : ton salaire s'arrête, tes loyers non.",mb=20))
A(png("00-will-salut","Will : Salut la famille !",mb=20))
nb=b(NB) if NB else PH("[NB ABONNÉS]")
A(P(f"Bienvenue aux {nb} nouveaux abonnés qui nous ont rejoints depuis la dernière édition ! Si tu en fais partie, on est très heureux de te compter parmi les membres de la communauté des Débrouya.",size=17,mb=14))
A(P("Si le contenu te plaît, partage-le : c’est la plus belle façon de nous soutenir.",size=17,mb=12))
A(f'<p style="margin:0 0 18px 0;text-align:center;">{btn("Invite tes amis à&nbsp;s’abonner&nbsp;→",LINK_SUB,ORANGE,INK)}</p>')
A(P("📲 Tu veux accéder à nos derniers contenus avant tout le monde ? Rejoins-nous sur :",size=16,color=MUTED,align="center",mb=10))
A(f'<p style="margin:0 0 28px 0;text-align:center;">{social_btn("Instagram",LINK_IG,"instagram")}{social_btn("YouTube",LINK_YT,"youtube")}</p>')

prog=["La question que personne n'aime se poser","Ce que ton salaire ne te dit&nbsp;pas","Un deuxième revenu, pas une deuxième dépense","Ta méthode en 4 étapes pour construire ta deuxième jambe","Concrètement, à quoi ça ressemble ?"]
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
A(gap(14)+kicker("Partie 1")+h3("La question que personne n'aime se poser"))
A(P("Je vais te poser une question. Et je te demande d'y répondre honnêtement, dans ta tête."))
A(punch(f"Si demain matin tu ne pouvais plus aller travailler pendant {hl('trois&nbsp;mois')}…<br>qu'est-ce qui continuerait de tomber sur ton compte&nbsp;?",size=22))
A(P(f"Je ne parle pas de ce que tu as déjà de côté. Je parle de l'argent qui {b('rentre')}."))
A(P(f"Si ta réponse, c'est {i('« pas grand-chose »')}, tu n'as rien à te reprocher."))
A(P(f"On a grandi avec un modèle simple.|{b('Tu travailles, tu es payé.<br>Tu arrêtes de travailler, tu n’es plus payé.')}|C'est le modèle de nos parents. Souvent celui de nos grands-parents aussi."))
A(P("Il marche très bien… tant que tout va bien. Mais le jour où ça coince, on se rend compte d'une chose :",mb=18))
A(png("02-pilier","Aujourd'hui, tout ton budget (crédit ou loyer, courses, voiture, assurances, factures) repose sur un seul pilier : ton salaire. Autrement dit, sur toi.",mb=34))

# ---------------- PARTIE 2 ----------------
A(kicker("Partie 2")+h3("Ce que ton salaire ne te dit&nbsp;pas"))
A(P(f"Ton salaire a une particularité qu'on oublie : il paie {b('ton temps')}. Ta présence. Ton énergie.|Et le jour où ton temps n'est plus disponible, le salaire suit."))
A(P(f"Prenons un exemple très concret : l'arrêt maladie. Quand tu es salarié du privé et que tu tombes malade, la Sécurité sociale te verse des {b('indemnités journalières')}. Mais regarde bien comment elles sont calculées :",mb=18))
A(png("03-ij",f"Si tu es en arrêt maladie : tu touches la moitié de ton salaire journalier de base ; c'est au maximum {IJ} brut par jour depuis juillet 2026 ; et au début, tu ne touches rien pendant 3 jours : c'est le délai de carence.",mb=18))
A(P(EMPLOYEUR,mb=10))
A(bullets(["90 % de ton salaire brut pendant 30 jours ;","puis les deux tiers pendant 30 jours (plus longtemps avec l’ancienneté)."],color=TEAL))
A(P("Et ta convention collective peut prévoir mieux. Renseigne-toi, c'est important."))
A(P(f"Mais le principe reste le même : {b('quand tu t’arrêtes, ton revenu baisse.')}|Et si tu es fonctionnaire, les règles sont différentes, mais toi aussi, tu perds une partie de ton traitement."))
A(P("L'arrêt maladie n'est qu'un exemple. Il y a aussi :",mb=10))
A(bullets(["une fin de contrat ;","une entreprise qui ferme ;","un proche dont il faut s’occuper ;","et puis un jour, la retraite : en général, ta pension ne remplace pas tout ton dernier salaire."],color=TEAL)+gap(10))
A(png("06-will","Will : Tu vois où je veux en venir ?",mb=24))
A(punch(f"Le problème n'est pas d'avoir un&nbsp;salaire.<br>C'est d'avoir {hl('seulement')} un&nbsp;salaire.",size=22,mb=34))

# ---------------- PARTIE 3 ----------------
A(kicker("Partie 3")+h3("Un deuxième revenu, pas une deuxième dépense"))
A(P(f"Voilà le changement de regard que je te propose aujourd'hui. Arrête de voir l'investissement comme une façon de devenir riche. Vois-le comme une façon de construire une {b('deuxième jambe')} : un revenu qui ne dépend pas de ta présence au travail."))
A(P("Un loyer, c'est exactement ça :",mb=18))
A(png("05-qui-paie","Qui paie quoi ? Ton salaire dépend de toi, le loyer encaissé dépend du logement. Quand tu travailles, les deux arrivent sur ton compte. Quand tu es en arrêt, ton salaire baisse, mais le loyer continue d'arriver. Quand tu es à la retraite, ton salaire s'arrête, mais le loyer continue d'arriver. Le loyer du mois est dû, quoi qu'il t'arrive.",mb=24))
A(P("Mais attention. Je veux être très honnête avec toi sur un point :",mb=16))
A(card(p("Un bien qui a besoin de ton salaire pour être payé n'est pas un deuxième revenu.",size=19,color="#FFFFFF",w="bold",align="center",mb=8)+
       p("C'est une deuxième dépense.",size=22,color=PEACH,w="bold",align="center",mb=0),bg=TEAL,pad=24))
A(P(f"Si le loyer de ton bien ne couvre pas ta mensualité et tes charges, c'est toi qui complètes chaque mois.|Et le jour où ton salaire baisse, ce bien-là ne t'aide pas. {b('Il te tire vers le bas.')}"))
A(P("Et un loyer, ce n'est pas magique non plus :",mb=10))
A(bullets(["un logement peut rester vide entre deux locataires ;","un locataire peut payer en retard."],color=TEAL))
A(P(f"Donc la vraie question n'est pas : {i('« Est-ce que j’ai un bien ? »')}",mb=10))
A(punch("C'est : « Est-ce que ce bien tient debout tout seul ? »",size=22,mb=34))

# ---------------- PARTIE 4 : MÉTHODE ----------------
A(kicker("Partie 4")+h3("Ta méthode en 4 étapes pour construire ta deuxième jambe"))
A(P("Alors, par où commencer ?",mb=18))
A(png("09-will-methode","Will : Prêt ? On y va.",mb=30))

A(step("1","Fais le test du mois sans salaire"))
A(P("Prends une feuille et trace deux colonnes :",mb=18))
A(png("10-colonnes","Ton mois sans salaire : à gauche, ce qui sort chaque mois (crédit ou loyer, courses, voiture, assurances, abonnements) ; à droite, ce qui rentre sans que tu travailles.",mb=18))
A(P("Si la colonne de droite est vide, ne panique pas. C'est justement pour ça qu'on en parle aujourd'hui. Mais maintenant, tu le sais noir sur blanc. Et c'est ton point de départ.",mb=32))

A(step("2","Sécurise d'abord ton matelas"))
A(P("Avant d'acheter quoi que ce soit, regarde combien de mois tu tiendrais avec ton épargne si ton salaire s'arrêtait. Fixe-toi un objectif. Et construis ce matelas avant de te lancer."))
A(p("Pourquoi ? Parce qu'un investissement lancé sans matelas, c'est un investissement qui peut te mettre en difficulté au premier imprévu."))
A(punch(f"Le matelas protège ta vie.<br>Le bien construit ton avenir.<br>{hl('Dans cet ordre.')}",size=21,mb=32))

A(step("3","Choisis un bien qui se paie tout seul"))
A(P("C'est l'étape la plus importante. Et elle tient en un calcul :",mb=18))
A(png("11-test","Avant ton offre : le loyer réaliste doit couvrir ta mensualité de crédit, assurance emprunteur comprise, plus tes charges (taxe foncière, entretien, assurance du logement, charges de copropriété non récupérables). S'il couvre tout, ton bien tient debout. Sinon, renégocie le prix, ou passe au bien suivant.",mb=32))

A(step("4","Protège ta deuxième jambe"))
A(P(f"Un bien qui se paie tout seul, c'est bien. Un bien qui se paie tout seul {b('même quand ça se passe mal')}, c'est mieux."))
A(card(ikicker("🛡️","Tes trois protections",TEAL)+
       bullets([f"Mets de côté une petite {b('réserve pour le bien')} : un mois vide, une réparation, ça arrive.",
                f"Pense à une {b('garantie contre les loyers impayés')}. On a parlé récemment de Visale : elle est gratuite si ton locataire y a droit.",
                f"Regarde de près ton {b('assurance emprunteur')} : selon les garanties choisies, elle peut payer tout ou partie de ton crédit si un coup dur t'arrive.<br><span style=\"display:block;height:10px;line-height:10px;font-size:1px;\">&nbsp;</span>Attention, pour un arrêt maladie, elle ne démarre souvent qu'après un {b('délai de franchise')} de plusieurs mois. On l'a vu il y a quelques semaines."],color=TEAL),bg=TEAL_L,mb=20))
A(P(f"Bref. Une deuxième jambe, ça se construit. {b('Et ça s’entretient.')}",mb=34))

# ---------------- PARTIE 5 : EXEMPLE ----------------
A(kicker("Partie 5")+h3("Concrètement, à quoi ça ressemble ?"))
A(P(f"Prenons deux collègues, Thierry et Maryse. Même travail, même salaire, en Martinique. Il y a quelques années, ils ont tous les deux acheté un T2 pour le louer 650 € par mois. Mais pas de la même façon.",mb=8))
A(P("(Un exemple fictif aux chiffres ronds, juste pour illustrer.)",size=14,color=MUTED))
A(P(f"{b('Thierry')} a acheté vite, sans trop calculer. Sa mensualité et ses charges font 800 € par mois. {b('Maryse')} a pris le temps de négocier et de chiffrer : pour son T2, c'est 600 € par mois."))
A(P(f"Imaginons qu'un jour, tous les deux tombent malades. {b('Trois mois d’arrêt')} chacun. Leur salaire baisse. Regardons ce que leur bien fait pendant ces trois mois :",mb=18))
A(png("12-exemple","Thierry : loyers encaissés 3 × 650 € = 1 950 €, crédit et charges 3 × 800 € = 2 400 €, soit 450 € sortis de sa poche. Maryse : loyers encaissés 3 × 650 € = 1 950 €, crédit et charges 3 × 600 € = 1 800 €, soit 150 € qui lui restent.",mb=18))
A(P(f"{b('Même loyer. Même arrêt. Même&nbsp;île.')}|Pour Thierry, le bien est un poids de plus pendant la tempête.|Pour Maryse, il continue de rapporter, au moment où son salaire baisse."))
A(P("Et quand Maryse aura fini de rembourser son crédit, le loyer de son T2, une fois les charges payées, restera là chaque mois. Que son salaire tombe ou pas.",mb=24))
A(card(p("C'est ça, une deuxième jambe.",size=17,color=PEACH,align="center",mb=10)+
       p("Ton salaire peut s'arrêter.<br>Tes loyers, eux, peuvent continuer.",size=22,color="#FFFFFF",w="bold",align="center",mb=0),bg=TEAL,pad=28,mb=30))

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
    t=re.sub(r"(\d) (?=[^\W\d_])",r"\1&nbsp;",t)
    t=re.sub(r"\b(\w+(?:-\w+)+)\b",r'<span style="white-space:nowrap;">\1</span>',t)
    t=re.sub(r" ([\u2600-\u27BF\U0001F300-\U0001FAFF][\u2600-\u27BF\U0001F300-\U0001FAFF\uFE0F\U0001F3FB-\U0001F3FF]*)",r'&nbsp;<span style="white-space:nowrap;">\1</span>',t)
    return ">"+t+"<"
body=re.sub(r">([^<]+)<",_txt,body)
body=re.sub(r"(\d) ([€%])",r"\1&nbsp;\2",body)
body=re.sub(r" ([?!:;»])",r"&nbsp;\1",body).replace("« ","«&nbsp;")
html=f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light"><title>Journal Débrouya #153</title></head>
<body style="margin:0;padding:0;background:{BG};">
<!-- ===== DÉBUT DU BLOC À COLLER DANS LE BLOC HTML DE LEARNYBOX ===== -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{BG}" style="background:{BG};"><tr><td align="center" style="padding:14px 14px 30px 14px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;"><tr><td>
{body}
</td></tr></table></td></tr></table>
<!-- ===== FIN DU BLOC ===== -->
</body></html>'''
open(sys.argv[1],"w",encoding="utf-8").write(html); print(len(html.encode()),"octets")

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


PH=lambda t: f'<span style="background:#FFF3A0;color:#B00020;font-weight:bold;">{t}</span>'
T_=CFG.get("textes",{})
P_LOI_ALT=T_.get("loi_alt","Sans testament, qui hérite ? Tes enfants, à parts égales. Ton conjoint marié : un quart de tes biens en pleine propriété, ou l'usufruit de tout, selon ta situation familiale. Ton partenaire pacsé ou ton concubin : rien du tout.")
P_INDIVISION=T_.get("indivision","Et tous tes héritiers deviennent propriétaires de tes biens <strong>ensemble</strong>. C'est ce qu'on appelle l'<strong>indivision</strong> : chacun a sa part, mais personne ne possède un morceau précis. Et pour vendre un bien en indivision, il faut en principe l'accord de <strong>tout le monde</strong>.")
P_LOI2018=T_.get("loi2018","Et le sujet est tellement présent chez nous qu'en <strong>2018</strong>, le Parlement a voté une loi spécialement pour l'outre-mer, pour faciliter la sortie de ces indivisions familiales. Quand il faut une loi spéciale pour débloquer des maisons de famille, c'est qu'il y a un gros problème.")
P_TESTAMENT=T_.get("testament","Tu peux le garder chez toi, ou le confier à un notaire. Le notaire peut le faire inscrire au <strong>Fichier central des dispositions de dernières volontés</strong>, pour qu'il soit retrouvé le jour venu. Tu peux aussi faire un <strong>testament authentique</strong>, directement chez le notaire. Le tarif réglementé de sa rédaction est de <strong>113,19 € HT</strong>.")
P_COUPLE_LISTE=T_.get("couple_liste",[])
P_COUPLE=T_.get("couple","Et si tu es en couple sans être marié, cette étape est la plus urgente de toutes. Avec, en plus, une vraie discussion à avoir avec ton notaire sur la fiscalité, parce que tout ne se règle pas avec un testament.")

LINK_FEST="https://lynj.fr/festoptin"
# ---------------- EN-TÊTE ----------------
A(png("01-hero","Le Journal Débrouya, édition #149 : ce qu'il restera après toi.",mb=20))
A(png("00-will-salut","Will : Salut la famille !",mb=20))
nb=b(NB) if NB else PH("[NB ABONNÉS]")
A(P(f"Bienvenue aux {nb} nouveaux abonnés qui nous ont rejoints depuis la dernière édition ! Si tu en fais partie, on est très heureux de te compter parmi les membres de la communauté des Débrouya.",size=17,mb=14))
A(P("Si le contenu te plaît, partage-le : c’est la plus belle façon de nous soutenir.",size=17,mb=12))
A(f'<p style="margin:0 0 18px 0;text-align:center;">{btn("Invite tes amis à&nbsp;s’abonner&nbsp;→",LINK_SUB,ORANGE,INK)}</p>')
A(P("📲 Tu veux accéder à nos derniers contenus avant tout le monde ? Rejoins-nous sur :",size=16,color=MUTED,align="center",mb=10))
A(f'<p style="margin:0 0 28px 0;text-align:center;">{social_btn("Instagram",LINK_IG,"instagram")}{social_btn("YouTube",LINK_YT,"youtube")}</p>')

# ---------------- FESTIVAL (rappel) ----------------
A(kicker("Cette semaine",ORANGE)+h3("Le Lyannaj Fest Live commence ce vendredi"))
A(P("On t'en parlait dans la dernière édition : on y est presque ! Aux Antilles, en Guyane, dans l'Hexagone ou ailleurs, tu peux suivre le live depuis chez toi.",mb=18))
A(png("03-festival","Lyannaj Fest Live, 3 soirées en live et gratuites, de 14 h à 18 h aux Antilles, de 15 h à 19 h en Guyane, de 19 h à 23 h dans l'Hexagone : vendredi 20 novembre, soirée immobilier ; samedi 21 novembre, soirée business ; dimanche 22 novembre, soirée VIP, dont les conditions d'accès sont envoyées aux inscrits.",mb=18))
A(P("Au programme de ces trois soirées :",mb=12))
A(bullets([f"{b('Vendredi')} : premier achat, construction, terrain familial, investir à distance.",
           f"{b('Samedi')} : gagner du temps et de la marge, déléguer, l'IA, le marketing local, la reprise d'entreprise.",
           f"{b('Dimanche')} : en petit comité, avec un expert par thème."],color=ORANGE)+gap(10))
A(png("04-programme","Ce qui t'attend : Will et les coachs immobilier et business ; des experts du financement, des aides et de l'IA ; vendredi, la remise des diplômes, où une centaine de membres racontent leur projet ; tes questions en direct dans le chat.",mb=18))
A(card(p(f"Pour y accéder, {b('il suffit de t’inscrire')} : tu reçois ensuite ton lien par e-mail et sur WhatsApp.",size=17,mb=12)+p("Déjà inscrit ? Garde un œil sur tes messages.",size=17,mb=16)+
       f'<p style="margin:0;text-align:center;">{btn("Je réserve ma place gratuite&nbsp;→",LINK_FEST,ORANGE,INK)}</p>',bg=ORANGE_L,pad=22,mb=34))

T1="La maison aux volets fermés"; T2="Ce qui se passe vraiment quand on n'a rien organisé"; T3="Un héritage, ça se construit de ton vivant"; T4="Ta méthode en 4 étapes pour transmettre un patrimoine, pas un conflit"; T5="Ce que ça change, concrètement"
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
A(P("Tu la connais, cette maison. Elle est peut-être au bord d'une route de ta commune, ou même dans ta propre famille."))
A(P("Une belle case, ou une maison en béton construite à la sueur de son front. Avec les volets fermés depuis des années.|La peinture s'en va.<br>Les herbes gagnent la cour.<br>Le toit commence à fatiguer."))
A(P(f"Et quand tu demandes à qui elle est, on te fait toujours la même réponse : {i('« C’est la maison de la famille. Mais tu sais… ils ne sont pas d’accord. »')}|{b('Pourquoi ?')}",mb=18))
A(png("02-volets","Ce qui bloque : un frère veut la garder, une sœur veut vendre, un cousin dans l'Hexagone ne répond plus aux messages. Et pendant ce temps, la maison se dégrade.",mb=24))
A(P("Maintenant, pose-toi une question. La personne qui a construit cette maison, est-ce qu'elle voulait ça ? Bien sûr que non."))
A(P("Elle a travaillé toute sa vie. Elle a mis de côté, sou après sou, pour que ses enfants aient un toit. Quelque chose de solide.",mb=26))
A(punch(f"Elle voulait laisser un {b('héritage')}.<br>Et elle a laissé un {hl('problème')}.",size=22,mb=16))
A(P(f"Pas parce qu'elle a mal investi. Mais parce qu'elle n'a {b('rien organisé')}.",mb=34))

# ---------------- PARTIE 2 ----------------
A(kicker("Partie 2")+h3(T2))
A(P("Toi qui lis ce journal, pourquoi as-tu envie d'investir ? Pour tes loyers, ta retraite, ta liberté ? Ce sont toutes de bonnes raisons."))
A(P(f"Mais il y a une question qu'on se pose rarement au moment d'acheter : {i('« Ce bien, il devient quoi le jour où je ne suis plus là ? »')}"))
A(P(f"Elle est importante. Pourtant, on l'évite, parce que penser à sa propre mort, ça ne fait plaisir à personne. Alors on se dit : {i('« Les enfants se débrouilleront. »')}"))
A(P(f"Sauf que sans rien d'écrit, ce n'est pas toi qui décides comment ça se passe. C'est la loi. Et la loi applique une règle générale, pas ta volonté :",mb=18))
A(png("03-loi",P_LOI_ALT,mb=18))
A(P(P_INDIVISION,mb=24))
A(png("06-will","Will : Tu vois où je veux en venir ?",mb=24))
A(P("La maison aux volets fermés, ce n'est pas un accident. C'est souvent ce qui arrive quand on laisse la loi décider à sa place."))
A(P(P_LOI2018[0],mb=12))
A(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;margin:0 0 18px 0;"><tr><td style="border-left:4px solid {TEAL};padding:2px 0 2px 14px;">{P(P_LOI2018[1],mb=0)}</td></tr></table>')
A(P(P_LOI2018[2],mb=34))

# ---------------- PARTIE 3 ----------------
A(kicker("Partie 3")+h3(T3))
A(P(f"Un patrimoine, ce n'est pas seulement ce que tu possèdes. C'est aussi ce que tu laisses {b('en état de marche')}. Prends un appartement, et imagine deux façons de le transmettre : sur le papier, sa valeur est la même dans les deux cas. Ce qui change, c'est ce que tu as préparé :",mb=18))
A(png("05-heritages","Même bien, deux héritages. Rien d'organisé : les papiers sont introuvables, personne ne connaît tes souhaits, tes héritiers ne se parlent plus ; c'est un conflit avec un toit dessus. Tout est organisé : les papiers sont en ordre, chacun sait ce que tu voulais, tes héritiers savent quoi en faire ; c'est un revenu pour ceux d'après.",mb=24))
A(P(f"Et la différence ne se joue pas le jour de l'enterrement. Elle se joue {b('aujourd’hui')}, pendant que tu peux encore décider, expliquer et organiser."))
A(P("Mais attention, je ne te demande pas de devenir notaire, ni de passer tes week-ends dans la paperasse. Je te demande juste d'ajouter une question à ta façon d'investir :",mb=10))
A(punch("« Ce que je construis pourra-t-il continuer sans moi ? »",size=22,mb=34))

# ---------------- PARTIE 4 ----------------
A(kicker("Partie 4")+h3(T4))
A(png("09-will-methode","Will : Prends une feuille. On avance dans l'ordre.",mb=30))
A(step("1","Fais ton dossier « si je pars demain »"))
A(P("Accorde-toi une heure, pas plus, et rassemble au même endroit :",mb=18))
A(png("10-dossier","À rassembler : la liste de tes biens avec leur adresse ; tes titres de propriété et tes actes notariés ; tes crédits en cours, avec le nom de chaque banque ; tes baux, tes locataires, et qui gère chaque bien.",mb=18))
A(P(f"Puis dis à une personne de confiance {b('où')} se trouve ce dossier. Parce qu'un patrimoine que personne ne retrouve, c'est un patrimoine qui commence déjà à se perdre.",mb=32))

A(step("2","Écris ta volonté au lieu de laisser la règle générale décider"))
A(P(f"Le testament, ce n'est pas réservé aux gens riches. C'est juste un papier qui dit ce que {b('toi')}, tu veux."))
A(P(f"Le plus simple, c'est le {b('testament olographe')}. Il doit être :",mb=10))
A(bullets(["écrit de ta main du début à la fin ;","daté précisément (jour, mois, année) ;","signé."],color=TEAL))
A(P(b("Rien de tapé à l’ordinateur.")))
A(P(P_TESTAMENT))
A(P("Seule limite : un testament ne permet pas de tout faire. En France, une partie de ton patrimoine revient obligatoirement à tes enfants :",mb=18))
A(png("11-reserve","Selon le nombre d'enfants, la part réservée : la moitié de ta succession avec 1 enfant, les deux tiers avec 2 enfants, les trois quarts à partir de 3 enfants. Le reste, la quotité disponible, tu la donnes à qui tu veux.",mb=18))
A(P(P_COUPLE,mb=10))
A(bullets(P_COUPLE_LISTE,color=TEAL)+gap(14))

A(step("3","Parle à ta famille de ton vivant"))
A(P("C'est l'étape la plus difficile. Et c'est peut-être la plus importante. Pas besoin d'annoncer ce qu'il y a sur tes comptes."))
A(P("Tes proches ont juste besoin de savoir trois choses :",mb=10))
A(bullets(["ce qui existe ;","où sont les papiers ;","ce que tu souhaites."],color=TEAL))
A(P(f"Et surtout, {b('écoute-les')}.|Parce que peut-être que ton fils installé dans l'Hexagone ne veut pas de la maison.|Peut-être que ta fille, elle, rêve de la reprendre."))
A(P(f"Ces choses-là, mieux vaut les découvrir {b('autour d’une table, avec toi')}, que dans le bureau du notaire, sans toi.",mb=32))

A(step("4","À chaque achat, pense « transmissible »"))
A(P("Avant ton prochain investissement, ajoute cette question à ton analyse, en version concrète :",mb=10))
A(punch("« Si je pars dans dix ans, ce bien sera-t-il facile à transmettre, ou facile à disputer ? »",size=20,mb=20))
A(P("Un exemple : une grande maison pour trois enfants, ça se partage mal. Trois petits logements, beaucoup mieux."))
A(P(f"Je ne te dis pas que c'est la seule règle. Je te dis que c'est une question à te poser {b('avant')} de signer, pas après. Et pour les outils plus poussés, comme la donation-partage, c'est avec ton notaire que ça se calibre, en fonction de ta famille.",mb=34))

# ---------------- PARTIE 5 ----------------
A(kicker("Partie 5")+h3(T5))
A(P("Prenons un exemple fictif, pour que tu visualises. Imagine Josette, 62 ans, qui vit à Sainte-Anne, en Guadeloupe. Elle a sa maison, et un T2 en location au Gosier, qu'elle n'a pas fini de rembourser."))
A(P("Elle a aussi trois enfants : Marc, qui habite à deux pas de chez elle, et deux filles installées dans l'Hexagone. Le jour où elle part, voici ce qui change selon qu'elle s'est organisée ou non :",mb=18))
A(png("12-josette","Si rien n'est organisé : les papiers dorment dans une armoire, ses enfants ignorent le crédit du T2, Marc tient à la maison et ses sœurs veulent vendre ; la maison attend, volets fermés. Si Josette s'est organisée : elle a fait un dossier, et tous savent où il est ; elle a réuni la famille, chacun a dit ce qu'il veut ; avec son notaire, elle a prévu qui reçoit quoi ; chacun sait ce que Josette voulait.",mb=18))
A(P(f"{b('Sans rien d’organisé')}, ses trois enfants héritent à parts égales, en indivision, de la maison et du T2. Personne n'a tort. Mais personne ne peut trancher."))
A(P(f"{b('Si elle s’est organisée')}, elle sait déjà que ses filles ne comptent pas revenir vivre en Guadeloupe et que Marc tient à la maison. Et ce qu'elle a prévu respecte la part que la loi réserve à chacun de ses enfants."))
A(P("Est-ce que ça garantit zéro tension ? Non, je ne vais pas te mentir. Mais une famille qui devine et une famille qui sait, c'est toute la différence entre une maison qui vit et une maison qui ferme.",mb=24))
A(card(p("Bref. Tu n'investis pas seulement pour tes vieux jours. Tu investis aussi pour ceux qui viendront après toi.",size=17,color=PEACH,align="center",mb=10)+
       p("Alors fais en sorte qu'ils reçoivent un héritage.<br>Pas&nbsp;un&nbsp;problème.",size=22,color="#FFFFFF",w="bold",align="center",mb=0),bg=TEAL,pad=28,mb=30))

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
html=f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light"><title>Journal Débrouya #149</title></head>
<body style="margin:0;padding:0;background:{BG};">
<!-- ===== DÉBUT DU BLOC À COLLER DANS LE BLOC HTML DE LEARNYBOX ===== -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{BG}" style="background:{BG};"><tr><td align="center" style="padding:14px 14px 30px 14px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;"><tr><td>
{body}
</td></tr></table></td></tr></table>
<!-- ===== FIN DU BLOC ===== -->
</body></html>'''
open(sys.argv[1],"w",encoding="utf-8").write(html); print(len(html.encode()),"octets")

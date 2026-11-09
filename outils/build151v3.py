# -*- coding: utf-8 -*-
"""#151 v3 : édition complète, couleurs de la bannière (teal + orange + neutres)."""
import sys, re
BG="#FBF5EC"; INK="#1E2A2F"; MUTED="#6B767B"; TEAL="#136D68"; TEAL_L="#DDEFEC"; ORANGE="#E57638"; ORANGE_L="#FDEADB"; PEACH="#FFD3AE"; GREY_L="#E9E3D9"
FONT="Arial,Helvetica,sans-serif"
LINK_SUB="https://www.mouvementlyannaj.com/lm-journal-debrouya-v2/"
LINK_IG="https://www.instagram.com/william.synesius?igsh=MXBzM2V3eWV2MHppOQ=="
LINK_YT="https://youtube.com/@williamsynesius?si=BuRt8bjDLE6m0Dnf"
POLL_URL="https://script.google.com/macros/s/AKfycbz038iP5TC4JOXZ353QKSBCp43KTOQqPiNyGzO8SUYna9CABBY1rs8KcDcyO-H4Pvu7/exec"  # URL de l'application Web Apps Script, à renseigner
def poll_link(v,pos): return POLL_URL if POLL_URL=="#" else f"{POLL_URL}?v={v}&s=format-151-{pos}"

def p(t,size=18,color=INK,w="normal",align="left",mb=20):
    return f'<p style="margin:0 0 {mb}px 0;font-family:{FONT};font-size:{size}px;line-height:1.6;color:{color};font-weight:{w};text-align:{align};">{t}</p>'
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
def poll(pos, titre, texte):
    return card(kicker("Nouveau format",ORANGE)+p(b(titre),size=21,mb=10)+p(texte,size=16,mb=16)+
        f'<p style="margin:0;text-align:center;">{btn("👍 Oui, j’adore",poll_link("oui",pos),TEAL,"#FFFFFF")}{btn("👎 Non, je préfère l’ancien",poll_link("non",pos),"#FFFFFF",TEAL,TEAL)}</p>',
        bg="#FFFFFF",bl=ORANGE,pad=22,mb=28)
def step(n,title):
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;margin:10px 0 16px 0;"><tr>'
            f'<td width="60" valign="middle" nowrap style="width:60px;min-width:60px;white-space:nowrap;padding:0 14px 0 0;"><div style="width:46px;height:46px;border-radius:23px;background:{ORANGE};color:{INK};text-align:center;font-family:{FONT};font-size:22px;line-height:46px;font-weight:bold;">{n}</div></td>'
            f'<td valign="middle"><h4 style="margin:0;font-family:{FONT};font-size:22px;line-height:1.25;color:{INK};font-weight:bold;">{title}</h4></td></tr></table>')
def warn(t): return (f'<tr><td width="30" valign="top" nowrap style="width:30px;min-width:30px;white-space:nowrap;padding:0 12px 10px 0;font-family:{FONT};font-size:18px;color:{ORANGE};font-weight:bold;">✕</td>'
                     f'<td valign="top" style="padding:0 0 10px 0;font-family:{FONT};font-size:17px;line-height:1.5;color:{INK};">{t}</td></tr>')

H=[]; A=H.append
# ---------------- EN-TÊTE ----------------
A(img("01-hero","Le Journal Débrouya, édition #151 : ton année 2027 commence maintenant. Maintenant, tu prépares. Janvier 2027, tu es prêt.",mb=20))
A(img("00-will-salut","Will : Salut la famille !",ext="jpg",mb=20))
A(p(f"Bienvenue aux {b('40')} nouveaux abonnés qui nous ont rejoints depuis vendredi. On est très heureux de te compter parmi les membres de la communauté des Debrouya.",size=17,mb=14))
A(p("Si le contenu te plaît, partage-le : c’est la plus belle façon de nous soutenir.",size=17,mb=12))
A(f'<p style="margin:0 0 18px 0;text-align:center;">{btn("👉 Invite tes amis à s’abonner ici",LINK_SUB,ORANGE,INK)}</p>')
A(p("📲 Tu veux accéder à nos derniers contenus avant tout le monde ? Rejoins-nous sur :",size=16,color=MUTED,align="center",mb=10))
A(f'<p style="margin:0 0 28px 0;text-align:center;">{btn("Instagram",LINK_IG,"#FFFFFF",TEAL,TEAL)}{btn("YouTube",LINK_YT,"#FFFFFF",TEAL,TEAL)}</p>')

A(poll("haut","Tu aimes ce nouveau Journal ?","On a refait le Journal pour qu’il soit plus agréable à lire. Il est fait pour toi, alors c’est toi qui décides : un clic suffit."))
prog=["La phrase qu'on répète tous les mois de janvier","Pourquoi ton année 2027 commence avant le 1er janvier","Ta méthode en 4 étapes pour arriver prêt en janvier","Le calendrier qui transforme une envie en projet"]
rows="".join(f'<tr><td width="38" valign="top" nowrap style="width:38px;min-width:38px;white-space:nowrap;padding:0 12px 12px 0;font-family:{FONT};font-size:20px;font-weight:bold;color:{PEACH};">{k+1}.</td><td valign="top" style="padding:1px 0 12px 0;font-family:{FONT};font-size:17px;line-height:1.45;color:#FFFFFF;">{t}</td></tr>' for k,t in enumerate(prog))
A(card(kicker("Au programme aujourd'hui",PEACH)+gap(6)+f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table>',bg=TEAL))

A(card(kicker("Le témoignage de la semaine")+
       p(f"Merci à {b('Silla')} pour son témoignage, c'est un plaisir de t'avoir avec nous et de te partager nos meilleures ressources chaque semaine :",size=16,mb=16)+
       img("temoignage","Message de Silla : nous sommes aujourd'hui devenus propriétaires de 2 appartements. Merci pour ton accompagnement, l'aventure ne fait que commencer.",ext="jpg",radius=14,mb=16)+
       p("(Tu veux toi aussi apparaître dans Le Journal Debrouya ? Envoie-nous ton témoignage en réponse à ce mail. Chaque semaine, on en sélectionne un que l’on partage avec la communauté ❤)",size=14,color=MUTED,mb=0),bl=TEAL))

# ---------------- PARTIE 1 ----------------
A(gap(14)+kicker("Partie 1")+h3("La phrase de janvier"))
A(p("On entre dans la dernière ligne droite de l'année. Bientôt les chanté Nwèl, les repas en famille, le boudin, le pâté cochon."))
A(p("Et puis le 1er janvier. Et là, je suis prêt à parier que tu vas te dire une phrase. La même que l'année dernière :"))
A(img("02-janvier","« Cette année, c'est la bonne. Cette année, j'investis. »"))
A(p("Je ne me moque pas. On est nombreux à l'avoir dite. Le problème, ce n'est pas la phrase."))
A(punch("Le problème, c'est ce qui se passe après."))
A(img("03-glisse","Le projet qui glisse — janvier : retour au boulot ; février : carnaval, on verra ; mars : enfin la banque."))
A(p("Et en mars, au rendez-vous, on te demande des papiers."))
A(img("04-papiers","Relevés de compte, avis d'imposition, bulletins de salaire"))
A(p("Et tu réalises que ce que la banque regarde, ce n'est pas ta motivation de janvier.",mb=8))
A(punch(f"C'est {hl('ce que tu as fait les mois d’avant')}."))
A(img("05-will","Will : Tu vois où je veux en venir ?",ext="jpg",mb=34))

# ---------------- PARTIE 2 ----------------
A(kicker("Partie 2")+h3("Ton année 2027 a déjà commencé"))
A(p("On a tous été élevés avec cette idée : une nouvelle année, c'est une page blanche. On remet les compteurs à zéro, et on repart."))
A(p(b("Mais pour un projet immobilier, ça ne marche pas comme ça.")))
A(img("06-pages","Ce que tu crois : une page blanche. Ce que lit ton banquier : les pages d'avant."))
A(p("Concrètement ? Quand tu déposeras ton dossier, en mars ou en avril, les relevés qu'on te demandera pourront très bien être ceux de décembre, janvier et février. Et ton épargne, ton banquier ne la verra pas comme un chiffre : il la verra comme une habitude, ou une absence d'habitude."))
A(img("07-banquier","Tes relevés de décembre à février ; ton épargne comme habitude ; tes crédits à 35 % maximum de tes revenus nets en général, assurance comprise."))
A(p("Donc la vraie question n'est pas :",size=16,color=MUTED,mb=6))
A(p("<s>« Est-ce que j'investis en 2027 ? »</s>",size=19,color=MUTED,mb=18))
A(p("La vraie question, c'est :",size=16,color=TEAL,w="bold",mb=6))
A(card(p("« Est-ce que mon dossier sera prêt quand je voudrai investir en 2027 ? »",size=21,color="#FFFFFF",w="bold",mb=0),bg=TEAL,pad=24))
A(punch(f"Et ça, ça se décide {hl('maintenant')}.<br>Pas le 1er janvier.",size=22))
A(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;margin:0 0 34px 0;"><tr><td style="border-left:6px solid {ORANGE};padding:4px 0 4px 18px;">'
  f'<p style="margin:0;font-family:Georgia,serif;font-size:21px;line-height:1.5;color:{INK};font-style:italic;">Une année d\'investissement ne commence pas le jour où tu changes de calendrier. Elle commence le jour où tu arrêtes d\'en parler et où tu <strong>prépares le terrain</strong>.</p></td></tr></table>')

# ---------------- PARTIE 3 ----------------
A(kicker("Partie 3")+h3("Ta méthode en 4 étapes"))
A(img("08-will-pouce","Will : Quatre étapes. On fait ça proprement.",ext="jpg",mb=16))
A(p("Pas besoin d'y passer tes week-ends.",size=17,color=MUTED,align="center"))
A(img("09-marches","Les 4 étapes : 1. Bilan, 2. Objectif daté, 3. Dossier, 4. Calendrier",mb=30))

A(step("1","Fais ton bilan 2026, sans te mentir"))
A(p("Prends une feuille. Pas ton téléphone, une vraie feuille. Et réponds à trois questions :"))
A(img("10-bilan","Mon bilan 2026 : ce que j'ai fait, ce qui m'a bloqué, ce que j'ai mis de côté.",mb=20))
A(p(f"Note {b('tout ce que tu as fait')}, même les petits pas : un rendez-vous, une visite, une simulation. Pour {b('ce qui t’a bloqué')} : pas l'excuse polie, la vraie raison. Et pour {b('l’épargne')} : le vrai chiffre, mois par mois."))
A(p(f"Ce bilan n'est pas là pour te faire culpabiliser. Il est là pour que tu partes de {b('là où tu es')}, et pas de là où tu aimerais être.",mb=30))

A(step("2","Remplace « investir » par un objectif daté"))
A(p(f"« Investir en 2027 », ce n'est pas un objectif. C'est une envie. Un objectif, ça a une {b('action précise')} et une {b('date')}. Par exemple :"))
A(img("11-objectif","Une envie : investir en 2027. Des objectifs datés : 31 janvier, rendez-vous banque ; 31 mars, apport prêt ; 30 juin, première offre.",mb=20))
A(p(f"Choisis {b('un seul')} objectif principal. Pas cinq. Et écris-le quelque part où tu le verras tous les jours.",mb=30))

A(step("3","Prépare ton dossier dès décembre"))
A(p("C'est l'étape qu'on a le plus tendance à zapper. Et c'est celle qui peut te faire gagner le plus de temps. Commence à rassembler ce qu'on demande généralement pour un crédit immobilier :"))
A(img("12-dossier","Mon dossier : bulletins de salaire, avis d'imposition, relevés de compte, épargne et apport.",mb=14))
A(p("(Tu es à ton compte ? Tes bilans remplacent les bulletins de salaire.) Chaque banque a sa liste, mais si tu as déjà tout ça dans un dossier propre, tu gagnes des semaines.",size=16,color=MUTED))
A(p(b("Et surtout, regarde tes relevés avec les yeux de ton banquier :"),mb=12))
A(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 14px 0;">'
  + warn("les découverts à répétition") + warn("les dépenses qui partent dans tous les sens") + warn("les virements d'épargne qui s'arrêtent un mois sur deux") + '</table>')
A(p(f"Je sais, décembre, c'est le mois des fêtes. Fais-toi plaisir. Mais {b('garde un œil sur ton relevé')} : dans trois mois, il fera peut-être partie de ton dossier."))
A(card(kicker("💡 L'astuce",ORANGE)+
       p(f"Mets en place un {b('virement automatique')} vers ton épargne, le jour où tu reçois ton salaire. Même petit.",mb=10)+
       p(f"Ce n'est pas le montant qui compte le plus. C'est la {b('régularité')}. C'est elle qui montre que tu sais gérer.",mb=0),bg=ORANGE_L,mb=32))

A(step("4","Bloque ton calendrier maintenant"))
A(p("Un projet sans date, ça glisse. Toujours. Alors pose les grandes étapes dans ton agenda, dès cette semaine. Par exemple :"))
A(img("14-calendrier","Janvier : rendez-vous banque. Février-mars : zone, budget, critères et visites. Avril-mai : analyse des biens. Juin : première offre écrite.",mb=12))
A(p("Ce n'est pas un calendrier magique. C'est un exemple, à adapter à ta situation.",size=15,color=MUTED,align="center"))
A(p("La différence entre quelqu'un qui investit et quelqu'un qui en parle, c'est souvent ça :",align="center",mb=4))
A(punch(f"l'un a des dates, l'autre a des {hl('envies')}.",size=23,mb=34))

# ---------------- PARTIE 4 ----------------
A(kicker("Partie 4")+h3("Concrètement, à quoi ça ressemble ?"))
A(p("Prenons deux personnes. Mêmes revenus, même envie d'investir en Guadeloupe.",mb=6))
A(p("(Un exemple fictif, juste pour illustrer.)",size=14,color=MUTED))
A(img("15-fabrice-nadia","Fabrice attend janvier, cherche ses papiers en février, voit la banque en avril et se redit la même phrase en décembre 2027. Nadia fait son bilan début décembre, met un virement automatique avant Noël, voit la banque en janvier avec un dossier complet et visite en mars-avril en connaissant son budget.",mb=22))
A(p("Même salaire. Même île. Même envie.",size=19,w="bold",align="center",mb=8))
A(p(f"La seule différence ? {b('Le moment où chacun a commencé.')} Fabrice a commencé en janvier. Nadia a commencé en décembre.",align="center"))
A(p(f"Et ces quelques semaines d'avance, c'est souvent ce qui fait la différence entre {b('une année de plus à attendre')} et {b('une première offre signée')}."))
A(card(p("Bref. 2027 n'est pas encore là.",size=17,color=PEACH,align="center",mb=8)+
       p("Mais ton année 2027, elle, se joue déjà.",size=25,color="#FFFFFF",w="bold",align="center",mb=0),bg=TEAL,pad=28,mb=30))

# ---------------- MENTORAT + SIGNATURE ----------------
A(poll("bas","Alors, ce nouveau format ?","Maintenant que tu l’as lu en entier, dis-nous s’il te plaît. Un clic suffit."))
A(card(kicker("Tu veux être accompagné ?")+
       p("Je propose un programme de mentorat personnalisé. On regarde ta situation. On définit ta stratégie. On met en place un plan d'action sur mesure.")+
       p(b("Et surtout, on avance ensemble.")) +
       p("Intéressé ? Réponds simplement à ce mail avec le mot :",mb=12)+
       f'<p style="margin:0 0 14px 0;text-align:center;"><span style="display:inline-block;background:{ORANGE};color:{INK};border-radius:30px;padding:14px 30px;font-family:{FONT};font-size:22px;letter-spacing:2px;font-weight:bold;">MENTORAT</span></p>'+
       p("...et je te recontacterai pour en discuter. <em>Aucun engagement. Juste une conversation.</em>",size=15,color=MUTED,align="center",mb=0),bl=ORANGE,pad=22,mb=28))
A(img("16-will-clin","C'était Will. Ciao !",ext="jpg",mb=22))
A(f'<div style="border-top:1px solid #E3DBCF;margin:0 0 16px 0;"></div>')
A(p("Qu'as-tu pensé de cette édition ? Si tu apprécies le Journal Debrouya, pense à le partager autour de toi. Dis-nous ce que tu en penses en répondant à ce mail. (On lit tous les mails !)",size=14,color=MUTED,align="center"))

body="\n".join(H)
body=re.sub(r" ([?!:;»])",r"&nbsp;\1",body).replace("1er janvier","1&zwnj;er janvier").replace("« ","«&nbsp;")
html=f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light"><title>Journal Débrouya #151</title></head>
<body style="margin:0;padding:0;background:{BG};">
<!-- ===== DÉBUT DU BLOC À COLLER DANS LE BLOC HTML DE LEARNYBOX ===== -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{BG}" style="background:{BG};"><tr><td align="center" style="padding:14px 14px 30px 14px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;"><tr><td>
{body}
</td></tr></table></td></tr></table>
<!-- ===== FIN DU BLOC ===== -->
</body></html>'''
open(sys.argv[1],"w",encoding="utf-8").write(html); print(len(html.encode()),"octets")

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
def poll_link(v,pos): return f"{POLL_URL}?v={v}&s=format-147-{pos}"
def i(t): return f"<em>{t}</em>"
JPG={"00-will-salut","05-will","10-will-pouce","17-will-clin"}
def png(name,alt,mb=26): return img(name,alt,mb=mb,ext="jpg" if name in JPG else "png")
def bullets(items, mark="→", color=None):
    color=color or TEAL
    rows="".join(f'<tr><td width="28" valign="top" nowrap style="width:28px;min-width:28px;white-space:nowrap;padding:0 10px 12px 0;font-family:{FONT};font-size:18px;font-weight:bold;color:{color};">{mark}</td><td valign="top" style="padding:0 0 12px 0;font-family:{FONT};font-size:18px;line-height:1.55;color:{INK};">{t}</td></tr>' for t in items)
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 14px 0;">{rows}</table>'

# ---------------- EN-TÊTE ----------------
A(png("01-hero","Le Journal Débrouya, édition #147 : à la recherche du bien parfait.",mb=20))
A(png("00-will-salut","Will : Salut la famille !",mb=20))
A(p(f"Bienvenue aux {b('28')} nouveaux abonnés qui nous ont rejoints depuis vendredi. On est très heureux de te compter parmi les membres de la communauté des Debrouya.",size=17,mb=14))
A(p("Si le contenu te plaît, partage-le : c’est la plus belle façon de nous soutenir.",size=17,mb=12))
A(f'<p style="margin:0 0 18px 0;text-align:center;">{btn("👉 Invite tes amis à s’abonner ici",LINK_SUB,ORANGE,INK)}</p>')
A(p("📲 Tu veux accéder à nos derniers contenus avant tout le monde ? Rejoins-nous sur :",size=16,color=MUTED,align="center",mb=10))
A(f'<p style="margin:0 0 28px 0;text-align:center;">{btn("Instagram",LINK_IG,"#FFFFFF",TEAL,TEAL)}{btn("YouTube",LINK_YT,"#FFFFFF",TEAL,TEAL)}</p>')

# ---------------- FESTIVAL LYANNAJ ----------------
A(kicker("Rappel",ORANGE)+h3("Bloque tes soirées du 20, 21 et 22 novembre"))
A(p("Avant d’entrer dans le sujet du jour, une date à garder dans ton agenda :"))
A(png("02-festival","Festival Lyannaj, en live sur Zoom et gratuit : vendredi 20 novembre, soirée immobilier ; samedi 21 novembre, soirée business ; dimanche 22 novembre, soirée dévoilée bientôt. En soirée, heure de Paris.",mb=20))
A(p("Pourquoi ce rendez-vous compte ? Parce que c’est le moment de l’année où on fait le point ensemble, avec des acteurs de la Caraïbe qui font avancer le mouvement."))
A(p("Si tu as avancé cette année, on va célébrer ce que tu as accompli. Et si ton projet n’a pas bougé pendant que d’autres avançaient, c’est ta dernière occasion de l’année pour rattraper le train : récupérer nos dernières stratégies et repartir avec un plan clair."))
A(card(p(f"Pour l’instant, une seule chose à faire : {b('bloque ces trois soirées')}. Les infos pour t’inscrire arrivent très vite, ici même, dans le Journal.",size=17,mb=0),bg=ORANGE_L,pad=20,mb=30))

A(poll("haut","Tu aimes ce nouveau Journal ?","On a refait le Journal pour qu’il soit plus agréable à lire. Il est fait pour toi, alors c’est toi qui décides : un clic suffit."))

prog=["Le bien que tu cherches depuis des mois (et pourquoi tu ne le trouveras pas)","Ce qu'un prix Nobel a compris sur la façon dont on prend nos décisions","Le changement de regard : chercher le bon bien, pas le bien parfait","Ta méthode en 4 étapes pour arrêter de chercher et commencer à choisir"]
rows="".join(f'<tr><td width="38" valign="top" nowrap style="width:38px;min-width:38px;white-space:nowrap;padding:0 12px 12px 0;font-family:{FONT};font-size:20px;font-weight:bold;color:{PEACH};">{k+1}.</td><td valign="top" style="padding:1px 0 12px 0;font-family:{FONT};font-size:17px;line-height:1.45;color:#FFFFFF;">{t}</td></tr>' for k,t in enumerate(prog))
A(card(kicker("Au programme aujourd'hui",PEACH)+gap(6)+f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table>',bg=TEAL))

A(card(kicker("Le témoignage de la semaine")+
       p(f"Merci à {b('Clara')} pour son témoignage, c'est un plaisir de t'avoir avec nous et de te partager nos meilleures ressources chaque semaine :",size=16,mb=16)+
       img("temoignage","Témoignage de Clara : OS est plus qu'une simple formation, c'est un accompagnement complet. Un gros Big Up à William et Yin pour la vision qu'ils ont eu.",ext="jpg",radius=14,mb=16)+
       p("(Tu veux toi aussi apparaître dans Le Journal Debrouya ? Envoie-nous ton témoignage en réponse à ce mail. Chaque semaine, on en sélectionne un que l’on partage avec la communauté ❤)",size=14,color=MUTED,mb=0),bl=TEAL))

# ---------------- PARTIE 1 ----------------
A(gap(14)+kicker("Partie 1")+h3("Combien d'annonces dans tes favoris ?"))
A(p("Petite question, et réponds honnêtement. Sur ton téléphone, sur les sites, dans tes captures d'écran :"))
A(png("03-favoris","Dans tes favoris : 10 ? 30 ? Analysés jusqu'au bout : ? Offres faites : 0."))
A(p(f"Si ta dernière ligne affiche « zéro », {b('cette édition est pour toi')}."))
A(p("Parce que tu n'as pas un problème de motivation. Tu cherches. Tu cherches même beaucoup. Ton problème est ailleurs :"))
A(png("04-un-truc","Chaque bien a un truc : bien placé mais cuisine à refaire ; bon loyer mais 3e étage sans ascenseur ; coche presque tout, mais peut-être mieux le mois prochain."))
A(png("05-will","Will : Tu vois le schéma ?",mb=24))
A(p(f"Tu n'es pas en train de chercher {b('un')} bien. Tu es en train de chercher {b('le')} bien. Celui qui n'a aucun défaut."))
A(png("06-parfait","Ma liste du bien idéal : vue dégagée, prix bas, loyer haut, zéro travaux, bien placé, calme, parking. Ce bien n'existe pas.",mb=18))
A(p("Mais je vais te dire une chose que tu sais déjà, au fond.",align="center",mb=4))
A(punch(f"Ce bien-là {hl('n’existe pas')}.",mb=34))

# ---------------- PARTIE 2 ----------------
A(kicker("Partie 2")+h3("Ce qu'un prix Nobel a compris"))
A(p(f"Dans les années 1950, un chercheur américain, {b('Herbert Simon')}, s'est intéressé à la façon dont on prend vraiment nos décisions. Pas dans les manuels. Dans la vraie vie."))
A(p(f"Son constat : on n'a jamais toutes les informations, ni tout le temps du monde, pour comparer toutes les options possibles. Donc dans la vraie vie, on ne cherche pas l'option parfaite. On fixe un {b('seuil')}, et on retient une option qui le dépasse."))
A(png("07-seuil","La méthode du seuil, Herbert Simon, prix Nobel d'économie 1978 : on retient la première option qui dépasse le seuil. Satisficing = satisfaire + suffire.",mb=20))
A(p(f"Il a appelé ça le {i('satisficing')}. Bien plus tard, le psychologue {b('Barry Schwartz')} et son équipe ont comparé deux profils :"))
A(png("08-max-sat","Maximisateurs : moins heureux, moins satisfaits de leur vie, plus de regrets. Satisficeurs : critères fixés, décident, vivent mieux leurs choix. Barry Schwartz et son équipe, 2002.",mb=20))
A(p("Dans une de leurs études, les maximisateurs étaient même moins satisfaits de leurs propres achats. Ils cherchaient plus. Mais ils vivaient moins bien leurs choix."))
A(card(p(i("Et concrètement, pour ton projet immobilier, ça veut dire quoi ?"),size=16,color=PEACH,mb=10)+
       p("Ta recherche du bien parfait ne te protège pas. Elle te donne l’impression d’être prudent.",color="#FFFFFF",mb=8)+
       p("Mais en vrai, elle te garde sur le banc de touche.",size=21,color="#FFFFFF",w="bold",mb=0),bg=TEAL,pad=24,mb=34))

# ---------------- PARTIE 3 ----------------
A(kicker("Partie 3")+h3("Chercher le bon bien, pas le bien parfait"))
A(p(f"Un investissement immobilier, ce n'est pas un concours de beauté. Ce n'est pas « le plus bel appartement de l'île » qui gagne. C'est celui qui {b('fait le travail')} que tu lui demandes."))
A(p("Et quel travail tu lui demandes ? Ça, c'est toi qui le décides. Avant même de chercher. Tant que tu n'as pas écrit tes critères, chaque annonce devient une comparaison avec la précédente. Et avec la suivante. Et ça ne s'arrête jamais."))
A(p("Alors que si tu as tes critères sous les yeux, la question change :",mb=10))
A(p("<s>« Est-ce que c’est le meilleur ? »</s>",size=19,color=MUTED,mb=12))
A(card(p("« Est-ce que ça passe mon seuil ? »",size=21,color="#FFFFFF",w="bold",mb=6)+p("Une question à laquelle on peut répondre. Par oui ou par non.",size=16,color=PEACH,mb=0),bg=TEAL,pad=22))
A(p(f"Attention, je ne te dis pas de baisser tes exigences. Je te dis de les {b('écrire')}."))
A(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;margin:0 0 34px 0;"><tr><td style="border-left:6px solid {ORANGE};padding:4px 0 4px 18px;">'
  f'<p style="margin:0;font-family:Georgia,serif;font-size:21px;line-height:1.5;color:{INK};font-style:italic;">Un critère écrit, c\'est une règle. Un critère flou, c\'est une excuse pour ne jamais décider.</p></td></tr></table>')

# ---------------- PARTIE 4 : MÉTHODE ----------------
A(kicker("Partie 4")+h3("Ta méthode en 4 étapes"))
A(png("10-will-pouce","Will : Une feuille. Quatre étapes. Dans l'ordre.",mb=16))
A(png("11-marches","Les 4 étapes : 1. Tes 3 critères, 2. Deux colonnes, 3. Règle de décision, 4. Stop au bien rêvé.",mb=30))

A(step("1","Écris tes 3 non-négociables"))
A(p(f"Avant de rouvrir la moindre annonce, écris les {b('trois')} critères sans lesquels tu ne signes pas. Par exemple :"))
A(png("12-criteres","Mes 3 non-négociables : budget maximum frais compris ; rentabilité minimale après charges ; la zone, et pourquoi elle. Tout le reste est du bonus : la vue, le carrelage, l'étage.",mb=18))
A(p(f"Trois. Pas douze. Le reste est agréable si tu l'as, {b('pas disqualifiant')} si tu ne l'as pas.",mb=32))

A(step("2","Trie les défauts en deux colonnes"))
A(p("Parce que tous les défauts ne se valent pas."))
A(png("13-colonnes","Réparable, ça se chiffre : cuisine datée, peinture fatiguée, salle de bain à refaire. Définitif, aucun chantier ne le change : l'emplacement, le bruit de la route, l'exposition.",mb=18))
A(p(f"Le perfectionniste fuit tous les défauts. L'investisseur, lui, {b('chiffre')} ceux de la colonne 1 et se méfie de ceux de la colonne 2."))
A(card(kicker("💡 L'opportunité",ORANGE)+p("Parfois, un défaut réparable que les autres acheteurs fuient, c'est justement là que se trouve ton opportunité.",mb=0),bg=ORANGE_L,mb=32))

A(step("3","Donne-toi une règle de décision"))
A(p("C'est l'étape qui change tout. Fixe-toi une règle simple. Par exemple :"))
A(png("14-regle","Le bien passe mes 3 critères ? Je l'analyse en entier dans la semaine. Puis je fais une offre, ou j'écris pourquoi je n'en fais pas.",mb=18))
A(p(f"Tu ne laisses plus un bien flotter dans tes favoris pendant trois mois. Chaque bien qui mérite ton attention reçoit une {b('réponse')}."))
A(p("Et si tu dis non, tu sais pourquoi. La raison est écrite. Pas « j'ai un doute ». Une vraie raison.",mb=32))

A(step("4","Arrête de comparer avec le bien imaginaire"))
A(p("Quand tu hésites, demande-toi avec quoi tu compares. Si c'est un autre bien réel, disponible, avec des chiffres : c'est une vraie comparaison. Continue."))
A(p(f"Mais si tu compares avec « celui qui va peut-être sortir le mois prochain », tu compares avec un bien {b('qui n’existe pas')}.",mb=18))
A(png("15-imaginaire","Le bien réel a un prix, des défauts, des chiffres. Le bien imaginaire n'a ni prix, ni défaut, ni travaux : il gagne toujours.",mb=18))
A(gap(8))

# ---------------- PARTIE 5 : LUDOVIC ----------------
A(kicker("Partie 5")+h3("Ce que ça change, concrètement"))
A(p("Imagine Ludovic. Il vit au Lamentin, il a mis de côté un apport, et il veut acheter un appartement à louer."))
A(png("16-ludovic","Avant, à la recherche du bien parfait : 18 mois de recherche, une dizaine de visites, aucune offre, toujours comparé à un bien imaginaire. Après, avec ses critères écrits : 3 critères, favoris triés, il en reste 2, un chiffré et un écarté, première offre une semaine après.",mb=22))
A(p("Ses deux finalistes ? Le premier a une salle de bain à refaire : réparable, il fait chiffrer. Le deuxième est au bord d'une route très passante : définitif, il l'écarte."))
A(p("Est-ce que c'est le bien parfait ? Non.",size=19,w="bold",align="center",mb=6))
A(p(f"Est-ce que c'est un bien qui passe son seuil, avec des défauts connus et chiffrés ? {b('Oui.')}",align="center"))
A(p(f"Rien n'a changé dans son budget. Ce qui a changé, c'est qu'il sait enfin {b('ce qu’il cherche')}. Et sa recherche a enfin une {b('fin')}."))
A(p("Je ne vais pas te raconter d'histoire : son offre peut être refusée. Et ce ne sera peut-être pas l'affaire du siècle. Je te dis juste que sans critères, tu ne peux même pas savoir si c'est une bonne affaire. Tu peux seulement savoir que ce n'est pas parfait.",size=16,color=MUTED))
A(card(p("Bref. Le bien parfait n'existe pas. Mais le bien qui te convient existe peut-être déjà dans tes favoris.",size=17,color=PEACH,align="center",mb=10)+
       p("Il attend juste que tu décides de quoi tu as vraiment besoin.",size=23,color="#FFFFFF",w="bold",align="center",mb=0),bg=TEAL,pad=28,mb=30))

# ---------------- MENTORAT + SIGNATURE ----------------
A(poll("bas","Alors, ce nouveau format ?","Maintenant que tu l’as lu en entier, dis-nous s’il te plaît. Un clic suffit."))
A(card(kicker("Tu veux être accompagné ?")+
       p("Je propose un programme de mentorat personnalisé. On regarde ta situation. On définit ta stratégie. On met en place un plan d'action sur mesure.")+
       p(b("Et surtout, on avance ensemble.")) +
       p("Intéressé ? Réponds simplement à ce mail avec le mot :",mb=12)+
       f'<p style="margin:0 0 14px 0;text-align:center;"><span style="display:inline-block;background:{ORANGE};color:{INK};border-radius:30px;padding:14px 30px;font-family:{FONT};font-size:22px;letter-spacing:2px;font-weight:bold;">MENTORAT</span></p>'+
       p("...et je te recontacterai pour en discuter. <em>Aucun engagement. Juste une conversation.</em>",size=15,color=MUTED,align="center",mb=0),bl=ORANGE,pad=22,mb=28))
A(png("17-will-clin","C'était Will. Ciao !",mb=22))
A(f'<div style="border-top:1px solid #E3DBCF;margin:0 0 16px 0;"></div>')
A(p("Qu'as-tu pensé de cette édition ? Si tu apprécies le Journal Debrouya, pense à le partager autour de toi. Dis-nous ce que tu en penses en répondant à ce mail. (On lit tous les mails !)",size=14,color=MUTED,align="center"))

body="\n".join(H)
body=re.sub(r" ([?!:;»])",r"&nbsp;\1",body).replace("1er janvier","1&zwnj;er janvier").replace("« ","«&nbsp;")
for d in ["20, 21 et 22 novembre","20 novembre","21 novembre","22 novembre"]:
    body=body.replace(d,d.replace(" novembre","&zwnj; novembre"))
html=f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light"><title>Journal Débrouya #147</title></head>
<body style="margin:0;padding:0;background:{BG};">
<!-- ===== DÉBUT DU BLOC À COLLER DANS LE BLOC HTML DE LEARNYBOX ===== -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{BG}" style="background:{BG};"><tr><td align="center" style="padding:14px 14px 30px 14px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;"><tr><td>
{body}
</td></tr></table></td></tr></table>
<!-- ===== FIN DU BLOC ===== -->
</body></html>'''
open(sys.argv[1],"w",encoding="utf-8").write(html); print(len(html.encode()),"octets")

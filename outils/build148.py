# -*- coding: utf-8 -*-
"""#151 v3 : édition complète, couleurs de la bannière (teal + orange + neutres)."""
import sys, re
BG="#FBF5EC"; INK="#1E2A2F"; MUTED="#6B767B"; TEAL="#136D68"; TEAL_L="#DDEFEC"; ORANGE="#E57638"; ORANGE_L="#FDEADB"; PEACH="#FFD3AE"; GREY_L="#E9E3D9"
FONT="Arial,Helvetica,sans-serif"
LINK_SUB="https://www.mouvementlyannaj.com/lm-journal-debrouya-v2/"
LINK_IG="https://www.instagram.com/william.synesius?igsh=MXBzM2V3eWV2MHppOQ=="
LINK_YT="https://youtube.com/@williamsynesius?si=BuRt8bjDLE6m0Dnf"

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
ICON_BASE="img/"
def social_btn(label, href, icon):
    return (f'<a href="{href}" target="_blank" style="display:inline-block;background:#FFFFFF;border:2px solid {TEAL};color:{TEAL};text-decoration:none;'
            f'font-family:{FONT};font-size:16px;font-weight:bold;line-height:22px;border-radius:30px;padding:11px 20px 11px 16px;margin:0 6px 10px 6px;">'
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
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0;">{rows}</table>'
JPG={"00-will-salut","06-will","09-will-methode","17-will-fin"}
def png(name,alt,mb=26): return img(name,alt,mb=mb,ext="jpg" if name in JPG else "png")

LINK_FEST="https://lynj.fr/festoptin"

# ---------------- EN-TÊTE ----------------
A(png("01-hero","Le Journal Débrouya, édition #148 : chronique d'une interdiction annoncée.",mb=20))
A(png("00-will-salut","Will : Salut la famille !",mb=20))
A(p(f"Bienvenue aux {b('76')} nouveaux abonnés qui nous ont rejoints depuis mardi ! Si tu en fais partie, on est très heureux de te compter parmi les membres de la communauté des Débrouya.",size=17,mb=14))
A(p("Si le contenu te plaît, partage-le : c’est la plus belle façon de nous soutenir.",size=17,mb=12))
A(f'<p style="margin:0 0 18px 0;text-align:center;">{btn("👉 Invite tes amis à s’abonner ici",LINK_SUB,ORANGE,INK)}</p>')
A(p("📲 Tu veux accéder à nos derniers contenus avant tout le monde ? Rejoins-nous sur :",size=16,color=MUTED,align="center",mb=10))
A(f'<p style="margin:0 0 28px 0;text-align:center;">{social_btn("Instagram",LINK_IG,"instagram")}{social_btn("YouTube",LINK_YT,"youtube")}</p>')

# ---------------- FESTIVAL ----------------
A(kicker("À ne pas manquer",ORANGE)+h3("Le Lyannaj Fest Live, c'est dans une semaine"))
A(p("Vendredi prochain, on se retrouve en live, depuis chez toi. Aux Antilles, en Guyane, dans l'Hexagone ou ailleurs : tu peux y être.",mb=18))
A(png("03-festival","Lyannaj Fest Live, 3 soirées en live et gratuites, de 19 h à 23 h heure de Paris, soit 14 h aux Antilles et 15 h en Guyane : vendredi 20 novembre, soirée immobilier ; samedi 21 novembre, soirée business ; dimanche 22 novembre, soirée VIP, dont les conditions d'accès sont envoyées aux inscrits.",mb=18))
A(p(f"Vendredi, on parle {b('immobilier')} : premier achat, construction, terrain familial, investir à distance. Samedi, place au {b('business')} : gagner du temps et de la marge, déléguer, l'IA, le marketing local, la reprise d'entreprise. Et dimanche, la soirée {b('VIP')} se fait en petit comité, avec un expert par thème."))
A(png("04-programme","Ce qui t'attend : Will et les coachs immobilier et business ; des experts du financement, des aides et de l'IA ; vendredi, la remise des diplômes en direct, où une centaine de membres racontent leur projet ; tes questions en direct dans le chat.",mb=18))
A(card(p(f"C'est gratuit, mais {b('uniquement sur inscription')} : une fois inscrit, tu reçois ton lien d'accès par e-mail et sur WhatsApp.",size=17,mb=16)+
       f'<p style="margin:0;text-align:center;">{btn("Je réserve ma place gratuite&nbsp;→",LINK_FEST,ORANGE,INK)}</p>',bg=ORANGE_L,pad=22,mb=34))

# ---------------- MERCI POUR LES VOTES ----------------
A(kicker("Le nouveau format")+h3("Votre verdict"))
A(p("Mardi, on vous a demandé si vous aimiez le nouveau format du Journal. Vous avez été nombreux à répondre, et le verdict est clair :",mb=18))
A(png("02-vote","Vous avez voté pour le nouveau format : 88 % de « oui, j'adore ». Merci à toutes celles et ceux qui ont voté.",mb=18))
A(p(f"Le nouveau format est donc là pour rester, et on va continuer à l'améliorer.",mb=34))

prog=["La date que tout propriétaire bailleur aux Antilles devrait avoir dans son agenda","Ce que dit vraiment la loi chez nous (et pourquoi notre calendrier n'est pas celui de l'Hexagone)","Ta méthode en 4 étapes pour ne pas te faire surprendre","L'exemple chiffré : anticiper ou subir"]
rows="".join(f'<tr><td width="38" valign="top" nowrap style="width:38px;min-width:38px;white-space:nowrap;padding:0 12px 12px 0;font-family:{FONT};font-size:20px;font-weight:bold;color:{PEACH};">{k+1}.</td><td valign="top" style="padding:1px 0 12px 0;font-family:{FONT};font-size:17px;line-height:1.45;color:#FFFFFF;">{t}</td></tr>' for k,t in enumerate(prog))
A(card(kicker("Au programme aujourd'hui",PEACH)+gap(6)+f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table>',bg=TEAL))

A(card(kicker("Le témoignage de la semaine")+
       p(f"Merci à {b('Annick')} pour son témoignage ! Annick, c'est un plaisir de t'avoir avec nous et de te partager nos meilleures ressources chaque semaine :",size=16,mb=16)+
       img("temoignage","Témoignage d'Annick : aujourd'hui, je viens de signer mon acte authentique de vente. C'est ma première acquisition et ce ne sera pas la dernière.",ext="jpg",radius=14,mb=16)+
       p("(Tu veux toi aussi apparaître dans Le Journal Débrouya ? Envoie-nous ton témoignage en réponse à ce mail. Chaque semaine, on en sélectionne un que l’on partage avec la communauté ❤)",size=14,color=MUTED,mb=0),bl=TEAL))

# ---------------- PARTIE 1 ----------------
A(gap(14)+kicker("Partie 1")+h3("Une mauvaise nouvelle, annoncée à l'avance"))
A(p(f"Imagine qu'on t'annonce une mauvaise nouvelle. Mais avec {b('plusieurs années d’avance')} et la date exacte, écrite noir sur blanc. Tu ferais quoi ? Normalement, tu t'organises. Tu prends de l'avance."))
A(p(f"Eh bien c'est exactement ce que la loi a fait avec les propriétaires bailleurs des Antilles. Et ça se joue sur une lettre de A à G : l'étiquette du {b('DPE')}, le diagnostic de performance énergétique."))
A(p(f"Pendant longtemps, chez nous, on a vu ça comme un sujet de l'Hexagone. Des histoires de chauffage et d'hiver. Sauf que depuis le {b('1er juillet 2024')}, en Guadeloupe et en Martinique, les règles du DPE s'appliquent à la vente, à la location et aux annonces."))
A(p("Et derrière cette lettre, il y a un calendrier, écrit dans la loi depuis 2021. Ce n'est pas un piège caché. C'est une interdiction annoncée."))
A(p(f"Le problème, c'est qu'une interdiction annoncée, on a vite fait de la ranger dans la case {i('« plus tard »')}. Jusqu'au jour où plus tard, c'est maintenant.",mb=34))

# ---------------- PARTIE 2 ----------------
A(kicker("Partie 2")+h3("Ce que dit la loi chez nous"))
A(p(f"La loi Climat et Résilience du {b('22 août 2021')} a ajouté un critère à la définition du logement décent : un niveau minimal de performance énergétique. Et chez nous, le calendrier est {b('décalé')} par rapport à l'Hexagone :",mb=18))
A(png("05-calendrier","La lettre de ton DPE va de A, très économe, à G, passoire énergétique. À partir de quand tu ne peux plus louer : dans l'Hexagone, G interdit en 2025, F en 2028, E en 2034 ; en Guadeloupe et en Martinique, G interdit en 2028, F en 2031. Les interdictions s'additionnent : en 2031, F et G sont interdits.",mb=18))
A(p(f"Ça concerne les logements loués comme {b('résidence principale')}, vides ou meublés. Et ça s'applique aux nouveaux baux, mais aussi aux baux {b('renouvelés')} ou {b('reconduits tacitement')} après ces dates."))
A(p("Concrètement : tu ne pourras plus signer un nouveau bail sur un logement qui n'atteint pas le niveau exigé. Et si ton locataire est déjà en place, une fois son bail reconduit après ces dates, il pourra te demander de mettre le logement aux normes. S'il n'obtient rien, il peut saisir le juge, qui peut ordonner les travaux, réduire le loyer ou en suspendre le paiement."))
A(p("2028, ça paraît loin. Mais regarde :",mb=18))
A(png("07-bail","Un bail vide de 3 ans signé en 2026 court jusqu'en 2029. Le 1er janvier 2028, la classe G est interdite : en 2029, à la fin de ce bail, un logement classé G ne pourra plus être reloué.",mb=24))
A(png("06-will","Will : Tu vois où je veux en venir ?",mb=24))
A(punch(f"Le compte à rebours a déjà commencé.<br>Pour certains biens, il se joue {hl('sur le bail que tu signes cette année')}.",size=21,mb=34))

# ---------------- PARTIE 3 ----------------
A(kicker("Partie 3")+h3("Et le projet de loi dont tout le monde parle ?"))
A(p(f"Tu as peut-être vu passer des titres du genre {i('« les passoires thermiques vont pouvoir être relouées »')}. Je préfère être clair avec toi, parce que c'est là qu'on peut se faire avoir."))
A(p(f"Dans la version votée par le Sénat, un propriétaire pourrait continuer à louer un logement mal classé, à condition de {b('s’engager formellement dans des travaux')} de rénovation. Mais le texte peut encore changer :",mb=18))
A(png("08-projet","Le projet de loi relance logement : adopté par le Sénat le 8 juillet 2026, encore en discussion à l'Assemblée nationale, pas encore voté. Tant qu'il n'est pas voté et promulgué, c'est la loi actuelle qui s'applique.",mb=18))
A(p(f"Et regarde bien la condition, même dans la version la plus souple : il faudrait s'engager dans des travaux. Le sujet ne disparaît pas. Au mieux, il se décale. La bonne attitude, ce n'est pas d'attendre de voir. C'est de {b('savoir où tu en es')}.",mb=34))

# ---------------- PARTIE 4 : MÉTHODE ----------------
A(kicker("Partie 4")+h3("Ta méthode en 4 étapes"))
A(png("09-will-methode","Will : Une lettre. Deux dates. Et c'est toi qui décides.",mb=30))

A(step("1","Ressors ton DPE et lis-le vraiment"))
A(p("Retrouve le DPE de chacun de tes biens, et note trois choses :",mb=18))
A(png("11-dpe","Sur ton DPE, note trois choses : sa classe, la lettre de A à G ; la date du diagnostic ; sa durée de validité, 10 ans.",mb=18))
A(p(f"Si tu as acheté après le 1er juillet 2024, il est normalement dans le dossier de diagnostics remis à l'achat. Avant cette date, il n'était pas obligatoire chez nous : tu n'en as peut-être pas. Dans ce cas, ou s'il n'est plus valable, fais-en réaliser un par un {b('diagnostiqueur certifié')}. De toute façon, tu en as besoin pour louer : la classe énergie doit figurer dans tes annonces, et le DPE fait partie des documents à remettre à ton locataire avec le bail.",mb=32))

A(step("2","Calcule ton compte à rebours, bail par bail"))
A(png("12-dates","Pour chaque bien, deux dates : l'échéance de ton bail en cours, et la date limite de ta classe, 2028 pour G, 2031 pour F. Si l'échéance tombe après la date limite, fais tes travaux avant la fin de ce bail.",mb=18))
A(p(f"Et si ton logement est classé {b('E ou mieux')}, tu es tranquille pour ce calendrier-là. Note-le quand même : c'est un vrai plus pour la valeur de ton bien.",mb=32))

A(step("3","Demande ce qui fait vraiment bouger ta lettre"))
A(p("Ne te lance pas dans des travaux au hasard. Demande d'abord au diagnostiqueur quels travaux feraient changer ta classe, et dans quel ordre les faire."))
A(p(f"Ensuite, fais faire plusieurs {b('devis')}. Et pose à chaque artisan la seule question qui compte : {i('« Avec ces travaux, je passe à quelle classe ? »')}"))
A(card(ikicker("💡","Les bons réflexes",ORANGE)+
       bullets([f"Tu peux te faire conseiller gratuitement par {b('France Rénov’')}, le service public de la rénovation de l'habitat",
                f"Programme le chantier {b('entre deux locataires')}, pour ne pas faire de travaux dans un logement occupé"],color=ORANGE),bg=ORANGE_L,mb=32))

A(step("4","Si tu achètes, regarde la lettre avant de faire ton offre"))
A(p(f"Un logement classé G ou F, ce n'est pas forcément un mauvais achat. Mais c'est un achat qui arrive {b('avec des travaux')}, dans un délai fixé par la loi. Donc avant de faire une offre, intègre ces travaux dans ton calcul de rentabilité. Avec des devis, pas au doigt mouillé."))
A(p("Et si les chiffres ne tiennent plus une fois les travaux comptés, tu as ta réponse.",mb=34))

# ---------------- PARTIE 5 : EXEMPLE ----------------
A(kicker("Partie 5")+h3("L'exemple chiffré, pour que ce soit clair"))
A(p(f"Tu possèdes un T2 en Martinique, classé {b('G')}, loué vide {b('750 €')} par mois. Le bail a été signé le 1er février 2026, pour 3 ans : il arrive à échéance le 31 janvier 2029. Ton locataire te prévient qu'il part à cette date.",mb=8))
A(p("(Un exemple fictif aux chiffres ronds : la durée d'un chantier et le temps pour relouer dépendent de ton bien et de tes artisans.)",size=14,color=MUTED))
A(png("13-exemple","Avant, tu n'as rien anticipé : en février 2029 tu ne peux plus relouer, tu cherches des artisans et le logement reste vide, au total 5 mois sans locataire, 3 750 € de loyers perdus. Après, tu as anticipé : pendant le bail tu fais faire ton DPE et tes devis, quand ton locataire part le chantier démarre tout de suite, au total 2 mois sans locataire, 1 500 € de loyers perdus.",mb=18))
A(card(p(f"{b('2 250 €')} de loyers préservés, juste en t'y prenant à l'avance. Et un logement qui repart en location au bon niveau.",size=18,color="#FFFFFF",mb=0),bg=TEAL,pad=22))
A(card(ikicker("⚠️","Un dernier piège",ORANGE)+
       p(f"Si ton T2 sort de ces travaux classé {b('F')}, ce n'est pas fini : ton prochain bail de 3 ans arrivera à échéance en 2032, donc après le 1er janvier 2031. Si c'est possible, vise directement {b('E ou mieux')}, pour ne pas refaire un chantier quelques années plus tard.",mb=0),bl=ORANGE,mb=24))
A(card(p("Bref. Une interdiction annoncée, ce n'est pas une mauvaise nouvelle. C'est une information.",size=17,color=PEACH,align="center",mb=10)+
       p("Et une information ne vaut quelque chose que si tu t'en sers avant qu'il soit trop tard.",size=22,color="#FFFFFF",w="bold",align="center",mb=0),bg=TEAL,pad=28,mb=30))

# ---------------- MENTORAT + SIGNATURE ----------------
A(card(kicker("Tu veux être accompagné ?")+
       p("Je propose un programme de mentorat personnalisé. On regarde ta situation. On définit ta stratégie. On met en place un plan d'action sur mesure.")+
       p(b("Et surtout, on avance ensemble.")) +
       p("Intéressé ? Réponds simplement à ce mail avec le mot :",mb=12)+
       f'<p style="margin:0 0 14px 0;text-align:center;"><span style="display:inline-block;background:{ORANGE};color:{INK};border-radius:30px;padding:14px 30px;font-family:{FONT};font-size:22px;letter-spacing:2px;font-weight:bold;">MENTORAT</span></p>'+
       p("...et je te recontacterai pour en discuter. <em>Aucun engagement. Juste une conversation.</em>",size=15,color=MUTED,align="center",mb=0),bl=ORANGE,pad=22,mb=28))
A(png("17-will-fin","C'était Will. Ciao !",mb=22))
A(f'<div style="border-top:1px solid #E3DBCF;margin:0 0 16px 0;"></div>')
A(p("Qu'as-tu pensé de cette édition ? Dis-le-nous en répondant à ce mail (on lit tous les mails !). Et si tu apprécies le Journal Débrouya, pense à le partager autour de toi.",size=14,color=MUTED,align="center"))

body="\n".join(H)
body=re.sub(r" ([?!:;»])",r"&nbsp;\1",body).replace("« ","«&nbsp;")
for d in ["1er juillet 2024","1er janvier 2028","1er janvier 2031","1er février 2026","31 janvier 2029","22 août 2021","20, 21 et 22 novembre","20 novembre","21 novembre","22 novembre"]:
    body=body.replace(d,d.replace("1er","1&zwnj;er").replace(" ","&zwnj; ",1) if not d.startswith("1er") else d.replace("1er","1&zwnj;er"))
html=f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light"><title>Journal Débrouya #148</title></head>
<body style="margin:0;padding:0;background:{BG};">
<!-- ===== DÉBUT DU BLOC À COLLER DANS LE BLOC HTML DE LEARNYBOX ===== -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{BG}" style="background:{BG};"><tr><td align="center" style="padding:14px 14px 30px 14px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;"><tr><td>
{body}
</td></tr></table></td></tr></table>
<!-- ===== FIN DU BLOC ===== -->
</body></html>'''
open(sys.argv[1],"w",encoding="utf-8").write(html); print(len(html.encode()),"octets")

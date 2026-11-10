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
def bullets(items, mark="→", color=None):
    color=color or TEAL
    rows="".join(f'<tr><td width="28" valign="top" nowrap style="width:28px;min-width:28px;white-space:nowrap;padding:0 10px 12px 0;font-family:{FONT};font-size:18px;font-weight:bold;color:{color};">{mark}</td><td valign="top" style="padding:0 0 12px 0;font-family:{FONT};font-size:18px;line-height:1.55;color:{INK};">{t}</td></tr>' for t in items)
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 14px 0;">{rows}</table>'
JPG={"00-will-salut","05-will","10-will-methode","17-will-fin"}
def png(name,alt,mb=26): return img(name,alt,mb=mb,ext="jpg" if name in JPG else "png")

# ---------------- EN-TÊTE ----------------
A(png("01-hero","Le Journal Débrouya, édition #152 : louer sans t'engager pour 3 ans.",mb=20))
A(png("00-will-salut","Will : Salut la famille !",mb=20))
A(p(f"Bienvenue aux {b('[NB ABONNÉS]')} nouveaux abonnés qui nous ont rejoints depuis mardi. On est très heureux de te compter parmi les membres de la communauté des Debrouya.",size=17,mb=14))
A(p("Si le contenu te plaît, partage-le : c’est la plus belle façon de nous soutenir.",size=17,mb=12))
A(f'<p style="margin:0 0 18px 0;text-align:center;">{btn("👉 Invite tes amis à s’abonner ici",LINK_SUB,ORANGE,INK)}</p>')
A(p("📲 Tu veux accéder à nos derniers contenus avant tout le monde ? Rejoins-nous sur :",size=16,color=MUTED,align="center",mb=10))
A(f'<p style="margin:0 0 28px 0;text-align:center;">{social_btn("Instagram",LINK_IG,"instagram")}{social_btn("YouTube",LINK_YT,"youtube")}</p>')

prog=["Le dilemme du propriétaire qui veut récupérer son bien","Le bail fait pour louer quelques mois seulement","Ta méthode en 4 étapes pour le mettre en place","L'exemple chiffré : logement vide, bail classique ou bail court"]
rows="".join(f'<tr><td width="38" valign="top" nowrap style="width:38px;min-width:38px;white-space:nowrap;padding:0 12px 12px 0;font-family:{FONT};font-size:20px;font-weight:bold;color:{PEACH};">{k+1}.</td><td valign="top" style="padding:1px 0 12px 0;font-family:{FONT};font-size:17px;line-height:1.45;color:#FFFFFF;">{t}</td></tr>' for k,t in enumerate(prog))
A(card(kicker("Au programme aujourd'hui",PEACH)+gap(6)+f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table>',bg=TEAL))

A(card(kicker("Le témoignage de la semaine")+
       p(f"Merci à {b('[Prénom]')} pour son témoignage, c'est un plaisir de t'avoir avec nous et de te partager nos meilleures ressources chaque semaine :",size=16,mb=16)+
       f'<div style="border:2px dashed #C9C2B6;border-radius:14px;padding:28px 16px;margin:0 0 16px 0;text-align:center;font-family:{FONT};font-size:16px;color:{MUTED};">[TÉMOIGNAGE À AJOUTER : capture ou texte]</div>'+
       p("(Tu veux toi aussi apparaître dans Le Journal Debrouya ? Envoie-nous ton témoignage en réponse à ce mail. Chaque semaine, on en sélectionne un que l’on partage avec la communauté ❤)",size=14,color=MUTED,mb=0),bl=TEAL))

# ---------------- PARTIE 1 ----------------
A(gap(14)+kicker("Partie 1")+h3("Le dilemme qui laisse des logements vides"))
A(p("Je vais te parler d'une situation que beaucoup d'entre nous connaissent. Tu as un appartement. Il est meublé, il est propre. Mais tu sais que tu vas en avoir besoin dans quelques mois."))
A(p("Peut-être que tu rentres au pays l'année prochaine. Peut-être que tu veux le vendre. Peut-être qu'un de tes enfants va s'y installer."))
A(p(f"Alors tu te poses la question : {i('« Je le loue, ou pas ? »')} Et souvent, la réponse, c'est non. Parce que dans ta tête, louer, ça veut dire {b('s’engager')} :",mb=18))
A(png("03-durees","Combien de temps tu t'engages : location vide, 3 ans minimum pour un particulier ; meublé classique, 1 an reconduit tout seul ; bail mobilité, 1 à 10 mois au choix, qui s'arrête tout seul.",mb=18))
A(p("Et pour récupérer ton bien avec un bail classique, tu ne peux pas faire ça quand tu veux : il faut attendre la fin du bail, donner congé dans les délais, avec un motif prévu par la loi."))
A(p(f"Donc tu te dis : {i('« Trop risqué. Je préfère le laisser fermé. »')}",mb=18))
A(png("02-ferme","Logement fermé en attendant : il rapporte 0 €, mais continue de coûter la taxe foncière, l'assurance, les charges et l'entretien.",mb=34))

# ---------------- PARTIE 2 ----------------
A(kicker("Partie 2")+h3("Le bail fait pour louer quelques mois"))
A(p(f"Et si je te disais qu'il existe un bail fait exactement pour cette situation ? Il s'appelle le {b('bail mobilité')}. Il existe depuis plusieurs années, et pourtant, on n'y pense pas forcément."))
A(png("04-bail","Le bail mobilité, créé par la loi ELAN en 2018 : logement meublé ; 1 à 10 mois au choix ; s'arrête tout seul ; ni renouvelé ni reconduit.",mb=18))
A(p("Avec un bail classique, c'est la loi qui fixe la durée de ton engagement. Avec le bail mobilité, c'est toi qui choisis la durée, dans la limite de 10 mois. Pas de congé à donner, pas de motif à justifier."))
A(png("05-will","Will : Tu vois le changement ?",mb=24))
A(punch(f"Ton bien n'est plus « fermé en attendant ».<br>Il {hl('travaille en attendant')}.",size=22))
A(p(f"{i('Mais à qui tu peux le louer ?')} Pas à n'importe qui :",mb=18))
A(png("06-qui","Au moment de signer, ton locataire doit être en formation professionnelle, en études supérieures, en contrat d'apprentissage, en stage, en service civique, en mutation professionnelle ou en mission temporaire. Le motif doit exister à la signature et être écrit dans le bail.",mb=18))
A(p(f"Un étudiant qui vient pour un semestre. Un salarié muté pour quelques mois. Un stagiaire. Bref, des gens qui ont besoin d'un logement {b('pour un temps')}. Exactement comme toi tu as besoin de le louer {b('pour un temps')}.",mb=34))

# ---------------- PARTIE 3 ----------------
A(kicker("Partie 3")+h3("Ta méthode en 4 étapes"))
A(png("10-will-methode","Will : Ça se fait dans les règles, ou ça ne se fait pas.",mb=16))
A(png("08-marches","Les 4 étapes : 1. Meublé complet, 2. Le bon locataire, 3. Bail écrit, 4. Charges et sécurité.",mb=30))

A(step("1","Vérifie que ton logement est vraiment meublé"))
A(p("Le bail mobilité, c'est uniquement pour du meublé. Et « meublé », ce n'est pas un lit et une chaise : la loi fixe une liste minimum. Fais le tour de ton logement avec elle :",mb=18))
A(png("09-meuble","La liste minimum du meublé : literie et couette, rideaux ou volets, plaques de cuisson, four ou micro-ondes, frigo avec congélateur, vaisselle, ustensiles de cuisine, table et sièges, étagères, luminaires, matériel d'entretien.",mb=32))

A(step("2","Vérifie la situation de ton locataire"))
A(p("Demande un justificatif qui correspond à sa situation : une attestation d'inscription, une convention de stage, un contrat d'apprentissage, un ordre de mission, un courrier de mutation…",mb=32))

A(step("3","Rédige un bail avec les bonnes mentions"))
A(p("C'est l'étape à ne pas bâcler. Ton bail mobilité doit être écrit, et contenir notamment :",mb=18))
A(png("11-mentions","Le bail mobilité doit mentionner la durée, le motif, qu'il s'agit d'un bail mobilité régi par le titre Ier ter de la loi de 1989, et qu'aucun dépôt de garantie n'est exigé. À joindre : état des lieux, inventaire du mobilier, diagnostics.",mb=18))
A(p(f"Et oui, tu as bien lu : {b('pas de dépôt de garantie')}, c'est interdit dans ce bail. Sans ces mentions, tu prends le risque que ton contrat ne soit pas considéré comme un bail mobilité.",mb=32))

A(step("4","Fixe tes charges et sécurise-toi"))
A(p(f"Dans un bail mobilité, les charges sont {b('forfaitaires')} : tu fixes un montant dans le bail, sans régularisation ensuite. Donc calcule ton forfait à partir de ce que tu paies vraiment. Pas au doigt mouillé."))
A(card(kicker("💡 Sans dépôt de garantie, sécurise-toi autrement",ORANGE)+
       bullets([f"tu peux demander une {b('caution')}, et la {b('garantie Visale')} peut jouer ce rôle gratuitement si ton locataire y est éligible",
                f"fais un {b('état des lieux')} d'entrée très précis, avec des photos"],color=ORANGE),bg=ORANGE_L,mb=18))
A(p("Dernier point à connaître, le préavis ne joue pas dans les deux sens :",mb=18))
A(png("12-preavis","Ton locataire peut partir à tout moment avec un mois de préavis. Toi, tu ne peux pas le faire partir avant la fin, sauf faute de sa part.",mb=34))

# ---------------- PARTIE 4 ----------------
A(kicker("Partie 4")+h3("L'exemple chiffré, pour que ce soit clair"))
A(p("Murielle vit dans l'Hexagone. Elle a un T2 meublé à Schœlcher, en Martinique, et elle rentre s'y installer dans 8 mois. Un salarié muté pour une mission de quelques mois cherche justement un logement meublé.",mb=8))
A(p("(Un exemple fictif aux chiffres ronds, juste pour illustrer. Ce ne sont pas des chiffres de marché.)",size=14,color=MUTED))
A(png("13-murielle","Murielle, T2 meublé à Schœlcher, retour dans 8 mois, loyer possible 650 € par mois. Option 1, logement vide : 0 € et les frais tombent quand même. Option 2, bail classique d'un an : des loyers, mais retour bloqué. Option 3, bail mobilité : 8 × 650 € = 5 200 € et retour à la date prévue.",mb=18))
A(p(f"Avec le bail classique, elle ne peut donner congé que pour la fin du bail, avec un préavis de 3 mois. Résultat : impossible de récupérer son logement au bout de 8 mois, sauf si le locataire décide de partir. Elle prend le risque de rentrer… {b('sans pouvoir s’installer chez elle')}."))
A(card(kicker("Bon, et les limites ?")+
       p("Je préfère être honnête avec toi, il y en a :",size=17,mb=12)+
       bullets([f"si le locataire part avant la fin, tu dois retrouver quelqu'un : il y a un vrai risque de {b('vacance')}",
                f"plus de {b('rotation')}, donc plus d'états des lieux, plus d'usure, plus de temps passé",
                "pas de dépôt de garantie : l'état des lieux et la caution deviennent tes vraies protections",
                "ce n'est pas fait pour louer à l'année : au-delà de 10 mois, on repasse sur un bail meublé classique"]),bl=TEAL,mb=18))
A(p("Mais pour un logement dont tu auras besoin bientôt, c'est souvent bien mieux que des volets fermés."))
A(card(p("Bref. Un bien vide, ce n'est pas un bien protégé.",size=17,color=PEACH,align="center",mb=10)+
       p("C'est un bien qui te coûte, sans rien te rapporter.",size=23,color="#FFFFFF",w="bold",align="center",mb=0),bg=TEAL,pad=28,mb=30))

# ---------------- MENTORAT + SIGNATURE ----------------
A(card(kicker("Tu veux être accompagné ?")+
       p("Je propose un programme de mentorat personnalisé. On regarde ta situation. On définit ta stratégie. On met en place un plan d'action sur mesure.")+
       p(b("Et surtout, on avance ensemble.")) +
       p("Intéressé ? Réponds simplement à ce mail avec le mot :",mb=12)+
       f'<p style="margin:0 0 14px 0;text-align:center;"><span style="display:inline-block;background:{ORANGE};color:{INK};border-radius:30px;padding:14px 30px;font-family:{FONT};font-size:22px;letter-spacing:2px;font-weight:bold;">MENTORAT</span></p>'+
       p("...et je te recontacterai pour en discuter. <em>Aucun engagement. Juste une conversation.</em>",size=15,color=MUTED,align="center",mb=0),bl=ORANGE,pad=22,mb=28))
A(png("17-will-fin","C'était Will. Ciao !",mb=22))
A(f'<div style="border-top:1px solid #E3DBCF;margin:0 0 16px 0;"></div>')
A(p("Qu'as-tu pensé de cette édition ? Si tu apprécies le Journal Debrouya, pense à le partager autour de toi. Dis-nous ce que tu en penses en répondant à ce mail. (On lit tous les mails !)",size=14,color=MUTED,align="center"))

body="\n".join(H)
body=re.sub(r" ([?!:;»])",r"&nbsp;\1",body).replace("« ","«&nbsp;")
html=f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light"><title>Journal Débrouya #152</title></head>
<body style="margin:0;padding:0;background:{BG};">
<!-- ===== DÉBUT DU BLOC À COLLER DANS LE BLOC HTML DE LEARNYBOX ===== -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{BG}" style="background:{BG};"><tr><td align="center" style="padding:14px 14px 30px 14px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;"><tr><td>
{body}
</td></tr></table></td></tr></table>
<!-- ===== FIN DU BLOC ===== -->
</body></html>'''
open(sys.argv[1],"w",encoding="utf-8").write(html); print(len(html.encode()),"octets")

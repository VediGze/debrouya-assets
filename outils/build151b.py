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
LINK_COACH="https://www.mouvementlyannaj.com/newsletter-devenir-coach/"
def bigbtn(label,href=LINK_COACH,mb=26):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 {mb}px 0;"><tr><td align="center">'
            f'<a href="{href}" target="_blank" style="display:block;background:{ORANGE};border:2px solid {ORANGE};color:{INK};text-decoration:none;font-family:{FONT};font-size:18px;font-weight:bold;line-height:1.25;border-radius:32px;padding:16px 8px;text-align:center;">{label}</a></td></tr></table>')
PRE="Ton année 2027 se joue dès maintenant. Et si tu as déjà bâti un patrimoine locatif, une mission de coach pourrait t’intéresser."
A('<div style="display:none;font-size:1px;line-height:1px;color:'+BG+';max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">'+PRE+"&zwnj;&nbsp;"*60+'</div>')
A(png("01-hero","Le Journal Débrouya, édition #151. Ton année 2027 commence maintenant. Tu prépares dès aujourd’hui, et en janvier 2027, tu es prêt.",mb=20))
A(kicker("Mission de coach · Outsider School",ORANGE)+h3("Et si ton expérience aidait d’autres investisseurs ?"))
A(P("Tu as déjà constitué au moins 500&nbsp;000&nbsp;€ de patrimoine locatif ? Alors on aimerait te présenter une mission.",mb=18))
A(bigbtn("Découvrir la mission de coach&nbsp;→"))
A(card(p("Les hésitations avant de te lancer, les rendez-vous à la banque, les refus, les imprévus de chantier… Tout ça, tu connais. Et peut-être que tu conseilles déjà ta famille ou tes amis.",size=17,mb=14)+
       p(f"Avec {b('MentorExpert Outsider School')}, tu mets cette expérience au service d’autres investisseurs, pour aider la communauté à construire son patrimoine. Et peu importe que ton parcours ait commencé avec nous ou ailleurs.",size=17,mb=14)+
       p("C’est une collaboration indépendante, dans laquelle Outsider School t’apporte :",size=17,mb=10)+
       bullets(["les clients à accompagner ;","sa méthode et ses outils ;","de la formation continue ;","et l’appui de l’équipe."],color=ORANGE)+gap(6)+
       p("De ton côté, tu choisis un rythme qui colle à tes disponibilités.",size=17,mb=14)+
       p("Sur la page, une vidéo te présente la mission, et tu peux réserver un entretien directement.",size=17,mb=16)+
       bigbtn("Découvrir la mission de coach&nbsp;→",mb=0),bg=ORANGE_L,pad=22,mb=34))
A(png("00-will-salut","Will te dit « Salut la famille ! »",mb=20))
nb=b(NB) if NB else PH("[NB ABONNÉS]")
A(P(f"Bienvenue aux {nb} nouveaux abonnés qui nous ont rejoints depuis la dernière édition ! Si tu en fais partie, on est très heureux de te compter parmi les membres de la communauté des Débrouya.",size=17,mb=14))
A(P("Si le contenu te plaît, partage-le, c’est la plus belle façon de nous soutenir.",size=17,mb=12))
A(f'<p style="margin:0 0 18px 0;text-align:center;">{btn("Invite tes amis à&nbsp;s’abonner&nbsp;→",LINK_SUB,"#FFFFFF",TEAL,border=TEAL)}</p>')
A(P("📲 Tu veux accéder à nos derniers contenus avant tout le monde ? Rejoins-nous sur Instagram et YouTube.",size=16,color=MUTED,align="center",mb=10))
A(f'<p style="margin:0 0 28px 0;text-align:center;">{social_btn("Instagram",LINK_IG,"instagram")}{social_btn("YouTube",LINK_YT,"youtube")}</p>')


# ---------------- ARTICLE (depuis le fichier réécrit) ----------------
import re as _re
ALTS={
"02-janvier":"« Cette année, c’est la bonne. Cette année, j’investis. »",
"03-glisse":"En janvier, tu reprends le boulot. En février, c’est carnaval, on verra après. En mars, tu vas enfin à la banque.",
"06-will":"Will te demande « Tu vois où je veux en venir ? »",
"06-pages":"Toi, tu crois tourner la page le 1er janvier. Ton banquier, lui, lit les pages d’avant.",
"07-banquier":"Il lit tes relevés des derniers mois. Il regarde si tu épargnes chaque mois. Il vérifie que tes crédits restent sous 35 %, en général nouveau prêt compris, sur tes revenus nets avant impôt, assurance comprise.",
"09-will-methode":"Will te dit « Prêt ? On fait ça proprement. »",
"10-bilan":"Ton bilan 2026. Ce que tu as fait, ce qui t’a bloqué, ce que tu as mis de côté.",
"11-objectif":"Investir en 2027, c’est une envie. Les étapes datées, c’est voir ta banque le 15 janvier, avoir ton apport le 31 mars et faire une offre le 30 juin.",
"12-dossier":"Tes bulletins de salaire, ton avis d’imposition, tes relevés de compte, ton épargne et ton apport.",
"14-calendrier":"En janvier, tu vois ta banque. En février et mars, tu choisis ta zone et ton budget. En avril et mai, tu visites et tu analyses les biens. En juin, tu fais ta 1re offre écrite.",
"15-fabrice-nadia":"En janvier, Fabrice prend sa résolution. En février, il cherche ses papiers. En avril, son épargne va et vient. Et en décembre 2027, il se dit « l’an prochain ». Une année de plus à attendre. Nadia fait son bilan début décembre et programme son épargne avant Noël. En janvier, elle arrive prête à la banque, puis visite en avril-mai avec son budget en tête. Prête à faire une offre.",
}
def _md(t):
    t=_re.sub(r"\*\*(.+?)\*\*",r"<strong>\1</strong>",t)
    t=_re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])",r"<em>\1</em>",t)
    return t
ART=[l.rstrip() for l in open(sys.argv[3],encoding="utf-8").read().split("\n")]
part=0; listbuf=[]; tem_done=False
def flush():
    global listbuf
    if listbuf: A(bullets(listbuf,color=TEAL)); listbuf=[]
for k,l in enumerate(ART):
    if not l.strip(): continue
    nxt=next((x for x in ART[k+1:] if x.strip()),"")
    if l.startswith("→"):
        listbuf.append(_md(l[1:].strip())); continue
    flush()
    if l.startswith("[PROGRAMME]"):
        prog=[x.strip() for x in l[len("[PROGRAMME]"):].split("|")]
        rows="".join(f'<tr><td width="38" valign="top" nowrap style="width:38px;min-width:38px;white-space:nowrap;padding:0 12px 12px 0;font-family:{FONT};font-size:20px;font-weight:bold;color:{PEACH};">{n+1}.</td><td valign="top" style="padding:1px 0 12px 0;font-family:{FONT};font-size:17px;line-height:1.45;color:#FFFFFF;">{t}</td></tr>' for n,t in enumerate(prog))
        A(card(kicker("Au programme aujourd'hui",PEACH)+gap(6)+f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table>',bg=TEAL))
        if TEM:
            paras=TEM["paras"]
            q="".join(f'<p style="margin:0 0 {14 if k<len(paras)-1 else 0}px 0;font-family:Georgia,serif;font-size:18px;line-height:1.55;color:{INK};font-style:italic;">{t}</p>' for k,t in enumerate(paras))
            q+=f'<p style="margin:14px 0 0 0;font-family:{FONT};font-size:18px;font-weight:bold;color:{INK};">{TEM["prenom"]}</p>'
            tem=(p(f"Merci à {b(TEM['prenom'])} pour son témoignage ! {TEM['prenom']}, c'est un plaisir de t'avoir avec nous et de partager avec toi nos meilleures ressources chaque semaine. Voici son message.",size=16,mb=16)+
                 f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;margin:0 0 16px 0;"><tr><td style="border-left:4px solid {ORANGE};padding:2px 0 2px 16px;">{q}</td></tr></table>')
        else:
            tem=p(PH("[TÉMOIGNAGE À AJOUTER]"),size=16,mb=16)
        A(card(kicker("Le témoignage de la semaine")+tem+
               p("(Tu veux toi aussi apparaître dans Le Journal Débrouya ? Envoie-nous ton témoignage en réponse à ce mail. Chaque semaine, on en sélectionne un que l’on partage avec la communauté ❤️)",size=14,color=MUTED,mb=0),bl=TEAL))
        tem_done=True
    elif l.startswith("## "):
        part+=1; A((gap(14) if part==1 else "")+kicker(f"Partie {part}")+h3(_md(l[3:].strip())))
    elif l.startswith("### "):
        m=_re.match(r"### *Étape *(\d+) *[—-] *(.+)",l); A(step(m.group(1),_md(m.group(2).strip())))
    elif l.startswith("[IMAGE"):
        name=_re.match(r"\[IMAGE ([^\]\s]+)",l).group(1)
        A(png(name,ALTS.get(name,""),mb=24))
    elif l.startswith("!!"):
        A(punch(_md(l[2:].strip()),size=21,mb=36 if (nxt.startswith("##") or nxt.startswith("[FESTIVAL]")) else 24))
    elif l.startswith("[FESTIVAL]"):
        A(gap(8)+card(kicker("Soirée immobilier",ORANGE)+
               p(f"Tu veux aller plus loin sur l’investissement locatif ? C’est justement le thème qui ouvre le {b('Lyannaj Fest Live')}.",size=17,mb=12)+
               p("Rendez-vous à 14 h aux Antilles, 15 h en Guyane et 19 h dans l’Hexagone, et prépare tes questions pour le chat.",size=17,mb=16)+
               bigbtn("Je réserve ma place&nbsp;→",mb=0),bg=ORANGE_L,pad=22,mb=34))
    elif l.startswith("[ENCADRÉ]"):
        A(card(p(_md(l[9:].strip()),size=18,color="#FFFFFF",mb=0),bg=TEAL,pad=22))
    elif l.startswith("§"):
        t=_md(l[1:].strip())
        endlist=nxt.startswith("→"); endpart=nxt.startswith("##") or nxt.startswith("###")
        A(p(t,mb=10 if endlist else (32 if endpart else 18)))
flush()

# ---------------- MENTORAT + SIGNATURE ----------------
A(card(kicker("Tu veux être accompagné ?")+
       p("Je te propose un programme de mentorat personnalisé, en trois temps.",mb=10)+bullets(["On regarde ta situation.","On définit ta stratégie.","On met en place un plan d'action sur mesure."],color=ORANGE)+
       p(b("Et surtout, on avance ensemble.")) +
       p("Intéressé ? Réponds simplement à ce mail avec ce mot.",mb=12)+
       f'<p style="margin:0 0 14px 0;text-align:center;"><span style="display:inline-block;background:{ORANGE};color:{INK};border-radius:30px;padding:14px 30px;font-family:{FONT};font-size:22px;letter-spacing:2px;font-weight:bold;">MENTORAT</span></p>'+
       p("…et je te recontacterai pour en discuter. <em>Aucun engagement. Juste une conversation.</em>",size=15,color=MUTED,align="center",mb=0),bl=ORANGE,pad=22,mb=28))
A(png("17-will-fin","C'était Will. Ciao !",mb=22))
A(card(p(f"{b('P.S.')} Tu as au moins 500&nbsp;000&nbsp;€ de patrimoine locatif, et l’envie de transmettre ce que tu as appris ? La mission de coach est peut-être faite pour toi.",size=17,mb=16)+bigbtn("Découvrir la mission de coach&nbsp;→",mb=0),bg=ORANGE_L,pad=22,mb=26))
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

# Journal Débrouya — règles du format visuel (checklist avant chaque livraison)

Établies avec Steny les 9-10 novembre 2026 (#151 et #147). Chaque règle vient d'une erreur réellement corrigée.

## Texte et images
1. Une image remplace le texte qu'elle montre : ne jamais répéter dans le texte ce que l'image dit déjà, ni l'inverse (ex. « Ce bien-là n'existe pas » sous un tampon « N'EXISTE PAS »).
2. Pas de triplon titre de section + titre dans l'image + bulle de Will qui disent la même chose : le titre de section suffit.
3. Les visuels parlent au lecteur : « ta liste », « tes critères », « tu fais une offre ». Jamais « ma / mes / je », qui ferait croire que c'est la liste de Will.
4. Pas de libellés abrégés ou flous dans les images (« mini » → « Rentabilité minimale · après charges »).
5. Pas de texte barré pour opposer deux idées : deux cartes étiquetées (« Avant : … » / « Maintenant : … »).
6. Texte dans les images : 20 px minimum (image de 600 px réduite à ~360 px sur téléphone). Une seule palette : bleu canard #136D68, orange #E57638, neutres.

## Contenu
7. Lectorat antillais : jamais « printemps / hiver » → des mois (« en mars ou en avril », « décembre à février »).
8. Vérifier la date d'envoi réelle de l'édition et rendre les repères temporels valables à cette date (ex. « dernière ligne droite de l'année » plutôt que « on est fin novembre »).
9. Chiffres et faits vérifiés par recherche web avant livraison.

## Will
10. Banque de 18 poses (dépôt VediGze/debrouya-assets, outils/avatar). Les 4 emplacements tournent (accueil, relance, méthode, signature) via outils/poses.py : pose la moins récemment utilisée, cohérente avec la bulle, jamais la même qu'à l'édition précédente. Mettre à jour historique.json.
11. Quand de nouvelles poses arrivent, les intégrer dans les éditions pas encore envoyées.
12. Fêtes : pose de saison à l'accueil + clin d'œil dans le texte pendant les fenêtres définies dans poses.py (rappels programmés pour Steny). C'est Claude qui gère, pas Steny.

## Technique (téléphone)
13. Toute rangée icône/numéro + texte : `nowrap`, `min-width` et espacement à droite de l'icône ; tester le « pire cas » (largeurs ignorées, écran 320 px).
14. Casser la détection de date d'Apple Mail : « 1&zwnj;er janvier », « 20&zwnj; novembre ».
15. Images hébergées dans le dépôt GitHub, adresses jsDelivr épinglées sur le commit exact (jamais @main : cache périmé).
16. Avant livraison : vérifier que le HTML LearnyBox et le PDF sont identiques (même texte, mêmes images octet pour octet).

## Livraison
17. Claude dépose lui-même dans le Drive, dans un SOUS-DOSSIER « NNN - Journal Débrouya » (numéro en premier) créé dans le même dossier de mois que le Google Doc « LE JOURNAL DÉBROUYA Newsletter #NNN » (pas forcément le mois en cours) : « NNN - Journal Débrouya - aperçu.pdf » + « NNN - Journal Débrouya - code LearnyBox.html ». Le Google Doc de l'édition est DÉPLACÉ dans ce sous-dossier (il ne reste pas à l'extérieur). Anciennes versions à la corbeille.
18. Jamais de manip manuelle pour Steny quand Claude peut la faire (Drive, Sheets, Apps Script, GitHub).
19. Prompts pour ChatGPT : complets, un par bloc, prêts à copier-coller.
20. Sondage « nouveau format » : terminé — utilisé uniquement dans la #147 (votes dans le Sheet « Sondages Journal Débrouya »). Ne plus le mettre dans les éditions suivantes, sauf nouvelle demande de Steny.
21. Boutons réseaux : icônes officielles Instagram et YouTube (dossier commun/ du dépôt) + le nom écrit à côté, liens vers les comptes de Will.
22. Titre de carte avec icône (💡…) : icône dans sa propre colonne (ikicker), pour que la 2e ligne du titre s'aligne sous le texte et sur les puces, pas sous l'icône.
23. Textes dans les visuels : des phrases complètes et naturelles (« Février 2029 : tu ne peux plus relouer. »), jamais du style télégraphique (« Logement vide / pour chercher artisans », « × 750 € / de loyer »).
24. Un visuel doit se comprendre sans connaissance préalable : si l'image repose sur un code (lettres du DPE, sigles…), elle l'explique elle-même (légende « A : très économe… G : passoire énergétique », « G interdit » plutôt que « G » seul).
25. Pas d'image « sommaire » qui ne fait que répéter les titres qui suivent (ex. l'escalier 1-2-3-4 avant les 4 étapes) : on la supprime.
26. Pose « telephone » de Will : l'écran affiche la couverture de l'édition (outils/ecran.py pose + 01-hero → will-telephone-NNN.png), jamais un écran blanc.
27. Accord collectif : avec « nombreux », passer au « vous » (« Vous avez été nombreux à répondre »), même dans un journal au « tu ». Jamais « tu as été nombreux ».
28. Bouton orange : pas d'émoji clair (ticket, 👉 jaune…) qui disparaît sur le fond orange ; préférer une flèche « → » couleur du texte.
29. Ordre des actus en tête : l'actu avec une action à faire et une date limite (événement, inscription) passe avant les actus « pour info » (résultat de vote, remerciements).
30. Témoignage reçu en capture d'écran : Claude lit la capture et retranscrit le texte en citation dans le mail (fautes de frappe et espaces corrigés, mots inchangés), au lieu de coller une image illisible sur téléphone.
31. Avant d'ajouter une actu datée (événement, festival, renvoi « on en a parlé récemment »), vérifier la date d'envoi prévue de l'édition dans les notes de workflow : l'actu doit être encore valable ce jour-là, et l'édition citée doit déjà être partie.
32. Une règle chiffrée (arrêt maladie, retraite, aides…) doit dire à qui elle s'applique (salarié du privé, fonctionnaire, indépendant) : beaucoup de lecteurs antillais sont fonctionnaires.
33. Sommes et pourcentages : espace insécable avant « € » et « % » ; mettre en exposant « 8<sup>e</sup> » ; une seule sorte d'apostrophe dans le mail.
34. Le programme « Au programme aujourd'hui » reprend mot pour mot les titres de toutes les parties, y compris l'exemple.
35. Poses de Will : le personnage est collé au bas du cadre (calcul automatique du bas réel de la pose). Pose « celebre » exclue (bras coupés par les bords de l'image source) ; « nouvel-an » touche aussi les deux bords : vérifier le cadre avant de l'utiliser.
36. Typographie du mail : apostrophes courbes ’ partout (comme dans les images), insécable entre un nombre et son mot (« 10&nbsp;ans », « 4&nbsp;étapes »), mots à trait d'union protégés contre la coupure (peut-être, e-mail, Rejoins-nous…), émojis jamais seuls en début de ligne.
37. Bloc témoignage : « Merci à X pour son témoignage ! X, c'est un plaisir de t'avoir avec nous et de partager avec toi nos meilleures ressources chaque semaine. Son message : » ; témoignage anonymisé (prénom seul, aucun nom ni initiale).
38. Accueil : « depuis la dernière édition » (jamais « depuis vendredi/mardi » quand un autre jour de la semaine est cité plus bas).
39. Aération du texte (lecture sur téléphone) : 1 à 2 phrases par paragraphe, 4-5 lignes maximum à 390 px ; toute énumération de 2 éléments ou plus passe en liste à flèches, introduite par une phrase dont les éléments s'enchaînent grammaticalement ; 1 à 2 mots en gras par bloc maximum, jamais sur ce qu'une image ou un encadré met déjà en avant ; phrases-chocs isolées ; espace identique (18 px) entre paragraphes, et après une liste.
40. Couverture (01-hero) toujours en JPG (~200 Ko) : en PNG elle pèse 1,4 Mo. Aucune image du mail au-dessus de ~300 Ko. Le dépôt d'images doit rester sous ~40 Mo (limite jsDelivr 50 Mo par version) : poses de Will stockées en 900 px.
41. Après chaque publication, tester dans un vrai navigateur que TOUTES les images du mail se chargent depuis jsDelivr (pas seulement comparer les fichiers dans GitHub). Juste après un push, jsDelivr peut répondre 404 « Failed to fetch the requested commit » sur certains fichiers et garder cette erreur en cache : purger chaque fichier en erreur (https://purge.jsdelivr.net/gh/VediGze/debrouya-assets@<SHA>/<fichier>) puis retester jusqu'à 100 % OK avant de livrer.
42. Fluidité : le texte se lit d'une traite, à voix haute, comme Will qui raconte. Chaque partie s'ouvre par une phrase-pont avec la précédente ; chaque image est amenée par une phrase qui donne envie de la regarder et suivie d'une conséquence (sans répéter l'image) ; connecteurs logiques variés ; pas de phrases « d'annonce » creuses (« Les sites spécialisés donnent des ordres de grandeur : ») ; découper pour le téléphone ne doit jamais casser l'enchaînement. Processus : texte de l'article écrit au balisage (article NNN.md : §, →, !!, [IMAGE], [ENCADRÉ], ##, ###), réécriture « transitions » par un sous-agent, puis relecture « à voix haute » par un autre sous-agent qui corrige le fichier, avant les relectures habituelles.
43. Deux-points : Steny les déteste. Aucun deux-points dans le texte du mail, remplacé par un connecteur, une virgule ou un point (« Résultat, … », « Concrètement, … »). Seule exception : la phrase qui introduit une liste à flèches. Même règle dans les textes des images autant que possible.
44. Phrases creuses interdites : pas de phrase qui ne fait qu'annoncer la suite ou une image (« Le dernier point, on s'y arrête une seconde. », « Pour te donner un ordre d'idée : », « Avant de foncer, il faut connaître les règles du jeu. »). Pas de titre d'image qui répète la phrase juste avant (supprimer le titre : la phrase d'amorce suffit). Textes des images en phrases courtes, faciles à lire à voix haute (« Tu veux le vendre libre ? Si le bail se termine… »).
45. Le lecteur est le propriétaire. Quand une image ou une phrase décrit le locataire, parler de lui à la 3e personne (« Ton locataire a 30 ans ou moins »), jamais « Tu as 30 ans ».
46. Mail envoyé le jour d'un événement en ligne : dire « aujourd'hui » plutôt que « ce soir » (19 h à Paris = 14 h aux Antilles) et donner les trois horaires (Antilles, Guyane, Hexagone).
47. Récit continu, pas une suite de constats (reproche répété de Steny, #154 puis #155-156). Chaque phrase découle de la précédente (cause, conséquence, opposition, exemple) ; on regroupe les phrases courtes d'une même idée dans un paragraphe lié au lieu de les empiler (« Prends la route… Et compte… Ces tiges… Peut-être que… ») ; on supprime tout ce qui n'est pas indispensable (idée secondaire, redite d'une image, d'un titre ou d'une phrase-choc, conclusion qui répète). Une phrase « mal formulée » se réécrit simplement (« tes devis serviront aussi à la banque »), sans image forcée. Avant toute livraison : relire chaque partie à voix haute d'un bout à l'autre, puis passe d'un sous-agent « fluidité » qui reçoit la liste des reproches de Steny et les exemples rejetés.
48. Compréhension par un novice (reproche de Steny sur #155-156 : « j'ai rien compris »). Tout mot technique (réception, réserves, retenue de garantie, décennale…) est expliqué en mots simples au moment où il apparaît, jamais utilisé avant d'être expliqué ; on présente d'abord le principe concret (« au lieu de payer 100 %, tu gardes 5 % de côté »), la loi ensuite. Une image se comprend seule : pas de badge chiffré sans phrase (« 3 ans », « 1 an »), pas de jargon (« parfait achèvement », « bon fonctionnement »), et tout chiffre affiché dit d'où il vient (« 10 000 € versés pour 2 000 € de travaux »). Titres complets (pas « en plein milieu » sans dire de quoi). Avant livraison : sous-agent « lecteur novice » qui ouvre chaque image et signale tout ce qu'il ne comprend pas.

## Relecture obligatoire avant de rendre (à refaire jusqu'à ne plus rien trouver)
Passe 1 — Texte : extraire tout le texte du mail dans l'ordre de lecture et le relire phrase par phrase :
- accords tu/vous (« tu » = un lecteur ; groupe = « vous » ; « Bienvenue aux N abonnés… si tu en fais partie »), 3e personne → 2e personne (« Merci à Annick… Annick, c'est un plaisir de t'avoir »)
- phrases bancales (« parce que… mais »), répétitions avec le pied de mail, logique des enchaînements
- orthographe constante du nom (« Débrouya »)
- chaque fait vérifié à la source le jour même (page de l'événement, service-public, ANIL…) ; ne rien affirmer que la source ne dit pas (ex. « réservée aux inscrits » ≠ « conditions envoyées aux inscrits ») ; vérifier qu'une règle s'applique bien à tous les lecteurs (ex. DPE obligatoire aux Antilles seulement depuis le 1er juillet 2024 → les achats plus anciens n'en ont pas)
- chaque chiffre recalculé (multiplications, différences, dates d'échéance)
Passe 2 — Visuels : regarder chaque image en grand, une par une :
- texte ≥ 18-20 px (rien en dessous, y compris pastilles, notes et légendes), aucun chevauchement (traits sur des dates, etc.)
- phrases naturelles, pas de télégraphique ; compréhensible sans connaître le sujet
- pas de redite texte/image, pas d'image qui répète les titres suivants
- « tu »/« vous » correct dans les images aussi
Passe 3 — Rendu : aperçu téléphone 390 px + pire cas 320 px, contrôle de chaque tranche ; boutons lisibles (émoji visible sur la couleur).
Passe 4 — Ordre et cohérence d'ensemble : actu urgente avant l'info, titres de section vs contenu, dates relatives (« mardi », « vendredi prochain ») justes pour la date d'envoi.
Recommencer les passes tant qu'une passe trouve quelque chose.
Passe 5 — Sous-agents : faire relire par des sous-agents indépendants (un pour le texte et les faits, un pour les visuels et le rendu), appliquer ce qui est fondé, puis une contre-relecture finale par un nouveau sous-agent.

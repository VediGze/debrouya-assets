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
17. Claude dépose lui-même dans le Drive, dans un SOUS-DOSSIER « NNN - Journal Débrouya » (numéro en premier) créé dans le même dossier de mois que le Google Doc « LE JOURNAL DÉBROUYA Newsletter #NNN » (pas forcément le mois en cours) : « NNN - Journal Débrouya - aperçu.pdf » + « NNN - Journal Débrouya - code LearnyBox.html ». Le Google Doc reste à sa place. Anciennes versions à la corbeille.
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

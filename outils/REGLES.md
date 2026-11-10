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

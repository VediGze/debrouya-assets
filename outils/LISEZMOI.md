# Outils du Journal Débrouya — format visuel (depuis la #151)

- `illus151.py` + `illus151_suite.py` : illustrations SVG → PNG (palette de la bannière : bleu canard #136D68, orange #E57638, neutres).
- `build151v3.py` : génère le mail HTML (tables, styles en ligne).
- `avatar/will-*.png` : les 4 poses de Will détourées (salut, menton, pouce, clin).
- `detoure.py` : détoure une nouvelle pose (fond blanc → transparent).
- `shot.py` / `shot320.py` : aperçus téléphone (390 px et pire cas 320 px).

Règles d'affichage téléphone (à respecter dans tout nouveau bloc) :
- Toute colonne « icône / numéro » + texte : `nowrap`, `min-width` et un `padding-right` de 12-14 px sur la cellule de l'icône. Ne jamais compter sur `width` seul : certaines messageries l'ignorent.
- Tester systématiquement avec la simulation « pire cas » (largeurs de colonnes ignorées, écran 320 px).
- Casser la détection de date d'Apple Mail : `1&zwnj;er janvier`.
- Texte dans les illustrations : 20 px minimum (image de 600 px réduite à ~360 px sur téléphone).
- Images publiées dans `NNN/` de ce dépôt. Dans le HTML, toujours épingler les adresses sur le commit exact : `https://cdn.jsdelivr.net/gh/VediGze/debrouya-assets@<SHA du commit>/NNN/` — jamais `@main`, que jsDelivr garde en cache plusieurs jours (images périmées).

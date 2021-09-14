---
- GuiCommand:/fr
   Name:PartDesign AdditivePrism
   Name/fr:PartDesign Prisme additif
   MenuLocation:Conception de pièces → Créer une primitive additive → Prisme additif
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Primitives additives](PartDesign_CompPrimitiveAdditive/fr.md), [PartDesign Prisme soustractif](PartDesign_SubtractivePrism/fr.md)
---

## Description

Insére un Prisme primitif dans un corps actif comme fonction de base, ou le fusionne aux fonctions existantes.

<img alt="" src=images/PartDesign_AdditivePrism_example.png  style="width:200px;">

## Utilisation

1.  Presser le bouton **<img src="images/PartDesign_AdditivePrism.svg" width=24px> '''Prisme additif'''**. **Remarque**: le Prisme additif fait partie du menu d\'icônes appelé *Créer une primitive additive*. Après le lancement de FreeCAD, le cube additif est affiché par défaut dans la barre d\'outils. Pour obtenir le Prisme additif, cliquer sur la flèche vers le bas et choisissez <img alt="" src=images/PartDesign_AdditivePrism.png  style="width:24px;"> Prisme additif dans le menu.
2.  Définir les paramètres primitifs et de l\'[ancrage](Part_EditAttachment/fr.md).
3.  Cliquer sur **OK**.
4.  Un prisme apparaît dans le corps actif.

## Options

Il est possible de créer des prismes biaisés en spécifiant des angles par rapport au vecteur normal de l\'ancrage choisi. {{Version/fr|0.19}}

Le Prisme peut être éditée après sa création de deux façons :

-   Double-cliquez le dans l\'arborescence ou faire un clic droit dessus et sélectionnez **Éditer la primitive** dans le menu contextuel. Cela fait apparaître les paramètres des Primitives.
-   Via l\'[Éditeur de propriétés](Property_editor/fr.md).

## Propriétés

-    {{PropertyData/fr|Attachment}}: définit les modes d\'ancrage ainsi que le décalage d\'ancrage. Voir [Part Ancrage](Part_EditAttachment/fr.md).

-    {{PropertyData/fr|Label}}: donne le nom du Prisme. Changez si nécessaire.

-    {{PropertyData/fr|Polygon}}: nombre de cotés de la section du polygone.

-    {{PropertyData/fr|Circumradius}}: [rayon circonscrit](https://fr.wikipedia.org/wiki/Cercle_circonscrit) du polygone de la section du prisme.

-    {{PropertyData/fr|Height}}: hauteur du prisme.

-    {{PropertyData/fr|First Angle}}: angle dans la première direction. {{Version/fr|0.19}}

-    {{PropertyData/fr|Second Angle}}: angle dans la seconde direction. {{Version/fr|0.19}}





{{PartDesign Tools navi

}}  

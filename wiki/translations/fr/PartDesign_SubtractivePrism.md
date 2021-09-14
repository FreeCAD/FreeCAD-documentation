---
- GuiCommand:/fr
   Name:PartDesign SubtractivePrism
   Name/fr:PartDesign Prisme soustractif
   MenuLocation:Conception de pièces → Créer une primitive soustractive → Prisme soustractif
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Primitives soustractives](PartDesign_CompPrimitiveSubtractive/fr.md), [PartDesign Prisme additif](PartDesign_AdditivePrism/fr.md)
---

## Description

Insérer un Prisme Primitif Soustractif dans le Corps actif. Sa forme est soustraite du solide existant.

![](images/PartDesign_SubtractivePrism_example.svg )

À Gauche : le Corps actif est en gris et le prisme soustractif est en rouge transparent ; le résultat final est à droite.

## Utilisation

1.  Presser le bouton **<img src="images/PartDesign_SubtractivePrism.svg" width=24px> '''Prisme soustractif'''**. **Remarque** : Le Prisme soustractif fait partie du menu d\'icônes appelé *Créer une primitive soustractive*. Après le lancement de FreeCAD, le cube soustractif est affiché par défaut dans la barre d\'outils. Pour obtenir le Prisme soustractif, cliquer sur la flèche vers le bas et choisissez <img alt="" src=images/PartDesign_SubtractivePrism.png  style="width:24px;"> Prisme soustractif dans le menu.
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

-    {{PropertyData/fr|Label}}: donne le nom du Prisme, changer si nécessaire.

-    {{PropertyData/fr|Polygon}}: nombre de cotés de la section du polygone.

-    {{PropertyData/fr|Circumradius}}: [rayon circonscrit](https://fr.wikipedia.org/wiki/Cercle_circonscrit) du polygone de la section du prisme.

-    {{PropertyData/fr|Height}}: hauteur du prisme.

-    {{PropertyData/fr|First Angle}}: angle dans la première direction. {{Version/fr|0.19}}

-    {{PropertyData/fr|Second Angle}}: angle dans la deuxième direction. {{Version/fr|0.19}}





{{PartDesign Tools navi

}}  

---
- GuiCommand:/fr
   Name:PartDesign SubtractiveEllipsoid
   Name/fr:PartDesign Ellipsoïde soustractif
   MenuLocation:Conception de pièces → Créer une primitive soustractive → Ellipsoïde soustractif 
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Primitives soustractives](PartDesign_CompPrimitiveSubtractive/fr.md)
---

## Description

Insérer un Ellipsoïde primitif soustractif dans le Corps actif. Sa forme est soustraite du solide existant.

![](images/PartDesign_SubtractiveEllipsoid_example.svg )

*À gauche, le corps actif (A) en gris et l\'ellipsoïde soustractif (B) en rouge transparent ; le résultat final est à droite.*

## Utilisation

1.  Presser le bouton **<img src="images/PartDesign_SubtractiveEllipsoid.svg" width=24px> '''Ellipsoïde additif'''**. **Remarque**: l\'Ellipsoïde soustractif fait partie d\'un menu d\'icônes appelé *Créer une primitive soustractive*. Après le démarrage de FreeCAD, le cube soustractif est celui affiché dans la barre d\'outils. Pour obtenir l\'Ellipsoïde soustractif, cliquez sur la flèche vers le bas à côté de l\'icône visible et sélectionnez \"Ellipsoïde soustractif\" dans le menu.
2.  Définir les paramètres primitifs et de l\'[ancrage](Part_EditAttachment/fr.md).
3.  Cliquer sur **OK**.
4.  Un Ellipsoïde apparaît dans le Corps actif.

## Options

L\'Ellipsoïde peut être édité après sa création de deux façons :

-   Double-cliquez le dans l\'arborescence ou faire un clic droit dessus et sélectionnez **Éditer la primitive** dans le menu contextuel. Cela fait apparaître les paramètres des Primitives.
-   Via l\'[Éditeur de propriétés](Property_editor/fr.md).

## Propriétés

-    {{PropertyData/fr|Attachment}}: définit les modes d\'ancrage ainsi que le décalage d\'ancrage. Voir [Part Ancrage](Part_EditAttachment/fr.md).

-    {{PropertyData/fr|Label}}: donne le nom de l\'Ellipsoïde , changer si nécessaire .

-    {{PropertyData/fr|Radius1}}: rayon de l\'Ellipsoïde dans le sens Z (hauteur) ; par défaut parallèle à l\'axe Z.

-    {{PropertyData/fr|Radius2}}: rayon de l\'Ellipsoïde dans le sens X (longueur) ; par défaut parallèle à l\'axe X.

-    {{PropertyData/fr|Radius3}}: rayon de l\'Ellipsoïde dans le sens Y (largeur) ; par défaut parallèle à l\'axe Y. Si par défaut cette valeur est à zéro, l\'ellipsoïde forme un [sphéroïde oblate (aplati comme un galet)](https://fr.wikipedia.org/wiki/Ellipso%C3%AFde_de_r%C3%A9volution).

-    {{PropertyData/fr|Angle1}}: (désignée *V parameter* dans les paramètres primitifs) troncature inférieure de l\'ellipsoïde, parallèle à la section circulaire (-90 degrés dans un sphéroïde complet)

-    {{PropertyData/fr|Angle2}}: (sans nom) troncature supérieure de l\'ellipsoïde, parallèle à la section circulaire (90 degrés dans un sphéroïde complet).

-    {{PropertyData/fr|Angle3}}: (désignée *U parameter* dans les paramètres primitifs) angle de rotation de la section elliptique (360 degrés dans un sphéroïde complet).





{{PartDesign Tools navi

}}  

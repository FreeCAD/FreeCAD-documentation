---
- GuiCommand:/fr
   Name:PartDesign SubtractiveSphere
   Name/fr:PartDesign Sphère soustractive
   MenuLocation:Conception de pièces → Créer une primitive soustractive → Sphère soustractive
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Primitives soustractives](PartDesign_CompPrimitiveSubtractive/fr.md)
---

# PartDesign SubtractiveSphere/fr

## Description

Insérer une sphère primitive soustractive dans le Corps actif. Sa forme est soustraite du solide existant.

![](images/PartDesign_SubtractiveSphere_example.svg ) *À gauche, le corps actif (A) en gris et le prisme soustractif (B) en rouge transparent ; le résultat final est à droite.*

## Utilisation

1.  Presser le bouton **<img src="images/PartDesign_SubtractiveSphere.svg" width=24px> '''Sphère soustractive'''**. **Remarque**: la sphère soustractive fait partie du menu d\'icônes appelé *Créer une primitive soustractive*. Après le lancement de FreeCAD, le cube soustractif est affiché par défaut dans la barre d\'outils. Pour obtenir la sphère soustractive, cliquer sur la flèche vers le bas et choisissez Sphère soustractive dans le menu.
2.  Définir les paramètres primitifs et de l\'[ancrage](Part_EditAttachment/fr.md).
3.  Cliquer sur **OK**.
4.  Une sphère apparaît dans le corps actif.

## Options

La Sphère peut être éditée après sa création de deux façons :

-   Double-cliquez la dans l\'arborescence ou faire un clic droit dessus et sélectionnez **Éditer la primitive** dans le menu contextuel. Cela fait apparaître les paramètres des Primitives.
-   Via l\'[Éditeur de propriétés](Property_editor/fr.md).

## Propriétés

-    {{PropertyData/fr|Attachment}}: définit les modes d\'ancrage ainsi que le décalage d\'ancrage. Voir [Part Ancrage](Part_EditAttachment/fr.md).

-    {{PropertyData/fr|Label}}: donne le nom de la Sphère, changer si nécessaire.

-    {{PropertyData/fr|Radius}}: rayon de la sphère.

-    {{PropertyData/fr|Angle1}}: (nommé *V parameter* dans les paramètres primitifs) troncature inférieure de la sphère, parallèle à la section circulaire (-90 degrés dans une sphère complète)

-    {{PropertyData/fr|Angle2}}: (sans nom dans Paramètres de la primitive) troncature supérieure de l\'ellipsoïde, parallèle à la section circulaire (90 degrés dans une sphère complète).

-    {{PropertyData/fr|Angle3}}: (nommé *U parameter* dans les paramètres primitifs) angle de rotation de la section transversale (360 degrés dans une sphère complète).





{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveSphere/fr

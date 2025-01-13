---
 GuiCommand:
   Name: PartDesign SubtractiveSphere
   Name/fr: PartDesign Sphère soustractive
   MenuLocation: PartDesign , Créer une primitive soustractive , Sphère soustractive
   Workbenches: PartDesign_Workbench/fr
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveSubtractive/fr, PartDesign_AdditiveSphere/fr
---

# PartDesign SubtractiveSphere/fr

## Description

Insère une sphère primitive soustractive dans le corps actif. Sa forme est soustraite du solide existant.

![](images/PartDesign_SubtractiveSphere_example.svg ) *À gauche, le corps actif (A) en gris et le prisme soustractif (B) en rouge transparent ; le résultat final est à droite.*



## Utilisation

1.  Pressez le bouton **<img src="images/PartDesign_SubtractiveSphere.svg" width=24px> '''Sphère soustractive'''**. **Remarque**: la sphère soustractive fait partie du menu d\'icônes appelé *Créer une primitive soustractive*. Après le lancement de FreeCAD, le cube soustractif est affiché par défaut dans la barre d\'outils. Pour obtenir la sphère soustractive, cliquez sur la flèche vers le bas et choisissez Sphère soustractive dans le menu.
2.  Définir les paramètres primitifs et de l\'[ancrage](Part_EditAttachment/fr.md).
3.  Cliquez sur **OK**.
4.  Une sphère apparaît dans le corps actif.

## Options

La Sphère peut être éditée après sa création de deux façons :

-   Double-cliquez la dans l\'arborescence ou faire un clic droit dessus et sélectionnez **Éditer la primitive** dans le menu contextuel. Cela fait apparaître les paramètres des Primitives.
-   Via l\'[Éditeur de propriétés](Property_editor/fr.md).



## Propriétés

-    **Attachment**: définit les modes d\'ancrage ainsi que le décalage d\'ancrage. Voir [Part Ancrage](Part_EditAttachment/fr.md).

-    **Label**: donne le nom de la sphère, changer si nécessaire.

-    **Radius**: rayon de la sphère.

-    **Angle1**: (nommé *Paramètre V* dans les paramètres de la primitive) troncature inférieure de la sphère, parallèle à la section circulaire (-90 degrés dans une sphère complète).

-    **Angle2**: (sans nom dans Paramètres de la primitive) troncature supérieure de la sphère, parallèle à la section circulaire (90 degrés dans une sphère complète).

-    **Angle3**: (nommé *Paramètre U* dans les paramètres de la primitive) angle de rotation de la section transversale (360 degrés dans une sphère complète).





{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveSphere/fr

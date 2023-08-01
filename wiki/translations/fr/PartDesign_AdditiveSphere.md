---
- GuiCommand:/fr
   Name:PartDesign AdditiveSphere
   Name/fr:PartDesign Sphère additive
   MenuLocation:Part Design → Créer une primitive additive → Sphère additive
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Primitives additives](PartDesign_CompPrimitiveAdditive/fr.md), [PartDesign Sphère soustractif](PartDesign_SubtractiveSphere/fr.md)
---

# PartDesign AdditiveSphere/fr

## Description

Insére une sphère primitive dans un corps actif (body) comme fonction de base, ou la fusionne avec les fonctions existantes.

<img alt="" src=images/PartDesign_AdditiveSphere_example.png  style="width:200px;">



## Utilisation

1.  Presser le bouton **<img src="images/PartDesign_AdditiveSphere.svg" width=24px> '''Sphère additive'''**. **Remarque** : la sphère additive fait partie du menu d\'icônes appelé *Créer une primitive additive*. Après le lancement de FreeCAD, le cube additif est affiché par défaut dans la barre d\'outils. Pour obtenir la sphère additive, cliquer sur la flèche vers le bas et choisissez Sphère additive dans le menu.
2.  Définir les paramètres primitifs et de l\'[ancrage](Part_EditAttachment/fr.md).
3.  Cliquer sur **OK**.
4.  Une sphère apparaît dans le corps actif.

## Options

La Sphère peut être éditée après sa création de deux façons :

-   Double-cliquez la dans l\'arborescence ou faire un clic droit dessus et sélectionnez **Éditer la primitive** dans le menu contextuel. Cela fait apparaître les paramètres des Primitives.
-   Via l\'[Éditeur de propriétés](Property_editor/fr.md).



## Propriétés

-    **Attachment**: définit les modes d\'ancrage ainsi que le décalage d\'ancrage. Voir [Part Ancrage](Part_EditAttachment/fr.md).

-    **Label**: donne le nom de la sphère. Changez si nécessaire.

-    **Radius**: rayon de la sphère.

-    **Angle1**: (nommé *Paramètre V* dans Paramètres de la primitive) troncature inférieure de la sphère, parallèle à la section transversale circulaire (-90 degrés dans une sphère pleine).

-    **Angle2**: (sans nom dans Paramètres de la primitive) troncature supérieure de la sphère, parallèle à la section transversale circulaire (90 degrés dans une sphère pleine).

-    **Angle3**: (nommé *Paramètre U* dans Paramètres de la primitive) angle de rotation de la section (360° pour une sphère entière).





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveSphere/fr

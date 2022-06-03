---
- GuiCommand   */fr
   Name   *PartDesign AdditivePrism
   Name/fr   *PartDesign Prisme additif
   MenuLocation   *Part Design → Créer une primitive additive → Prisme additif
   Workbenches   *[PartDesign](PartDesign_Workbench/fr.md)
   Version   *0.17
   SeeAlso   *[PartDesign Primitives additives](PartDesign_CompPrimitiveAdditive/fr.md), [PartDesign Prisme soustractif](PartDesign_SubtractivePrism/fr.md)
---

# PartDesign AdditivePrism/fr

## Description

Insère un Prisme primitif dans un corps actif comme fonction de base, ou le fusionne aux fonctions existantes.

<img alt="" src=images/PartDesign_AdditivePrism_example.png  style="width   *200px;">

## Utilisation

1.  Presser le bouton **<img src="images/PartDesign_AdditivePrism.svg" width=24px> '''Prisme additif'''**. **Remarque**   * le Prisme additif fait partie du menu d\'icônes appelé *Créer une primitive additive*. Après le lancement de FreeCAD, le cube additif est affiché par défaut dans la barre d\'outils. Pour obtenir le Prisme additif, cliquer sur la flèche vers le bas et choisissez Prisme additif dans le menu.
2.  Définir les paramètres primitifs et de l\'[ancrage](Part_EditAttachment/fr.md).
3.  Cliquer sur **OK**.
4.  Un prisme apparaît dans le corps actif.

## Options

Il est possible de créer des prismes biaisés en spécifiant des angles par rapport au vecteur normal de l\'ancrage choisi. {{Version/fr|0.19}}

Le Prisme peut être éditée après sa création de deux façons    *

-   Double-cliquez le dans l\'arborescence ou faire un clic droit dessus et sélectionnez **Éditer la primitive** dans le menu contextuel. Cela fait apparaître les paramètres des Primitives.
-   Via l\'[Éditeur de propriétés](Property_editor/fr.md).

## Propriétés

-    **Attachment**   * définit les modes d\'ancrage ainsi que le décalage d\'ancrage. Voir [Part Ancrage](Part_EditAttachment/fr.md).

-    **Label**   * donne le nom du Prisme. Changez si nécessaire.

-    **Polygon**   * nombre de cotés de la section du polygone.

-    **Circumradius**   * [rayon circonscrit](https   *//fr.wikipedia.org/wiki/Cercle_circonscrit) du polygone de la section du prisme.

-    **Height**   * hauteur du prisme.

-    **First Angle**   * angle dans la première direction. {{Version/fr|0.19}}

-    **Second Angle**   * angle dans la seconde direction. {{Version/fr|0.19}}





{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditivePrism/fr

---
- GuiCommand:
   Name: PartDesign SubtractiveBox
   Name/fr: PartDesign Cube soustractif
   MenuLocation: Part Design - Créer une primitive soustractive - Cube soustractif
   Workbenches: [PartDesign](PartDesign_Workbench/fr.md)
   Version: 0.17
   SeeAlso: [PartDesign Primitives soustractives](PartDesign_CompPrimitiveSubtractive/fr.md), [PartDesign Cube additif](PartDesign_AdditiveBox/fr.md)
---

# PartDesign SubtractiveBox/fr

## Description

Insère un Cube soustractif dans le corps actif. Sa forme est soustraite du solide existant.

![](images/PartDesign_SubtractiveBox_example.png ) *À gauche : le corps actif (A) est en gris et le cube soustractif (B) est en rouge transparent ; le résultat final est à droite.*

## Utilisation

1.  Presser le bouton **<img src="images/PartDesign_SubtractiveBox.svg" width=24px> '''Cube soustractif'''**. **Remarque**: le Cube soustractif fait partie du menu d\'icônes appelé *Créer une primitive soustractive*. Après le lancement de FreeCAD, le cube soustractif est affiché par défaut dans la barre d\'outils. Si une primitive différente s\'affiche, cliquez sur la flèche vers le bas à côté de l\'icône et sélectionnez Cube soustractive dans le menu.
2.  Définir les paramètres primitifs et de l\'[ancrage](Part_EditAttachment/fr.md).
3.  Cliquer sur **OK**.
4.  Un cube apparaît dans le Corps actif.

## Options

Le Cube peut être édité après sa création de deux façons :

-   Double-cliquez le dans l\'arborescence ou faire un clic droit dessus et sélectionnez **Éditer la primitive** dans le menu contextuel. Cela fait apparaître les paramètres des Primitives.
-   Via l\'[Éditeur de propriétés](Property_editor/fr.md).

## Propriétés

-    **Attachment**: définit les modes d\'ancrage ainsi que le décalage d\'ancrage. Voir [Part Ancrage](Part_EditAttachment/fr.md).

-    **Label**: donne le nom du cube, changer si nécessaire.

-    **Length**: (longueur) dimensions du cube en direction X.

-    **Width**: (largeur) dimensions du cube en direction Y.

-    **Height**: (hauteur) dimensions du cube en direction Z.





{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveBox/fr

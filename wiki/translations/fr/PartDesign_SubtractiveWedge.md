---
- GuiCommand:
   Name: PartDesign SubtractiveWedge
   Name/fr: PartDesign Pyramide tronquée soustractive
   MenuLocation: Part Design - Créer une primitive soustractive - Pyramide tronquée soustractive
   Workbenches: [PartDesign](PartDesign_Workbench/fr.md)
   Version: 0.17
   SeeAlso: [PartDesign Primitives soustractives](PartDesign_CompPrimitiveSubtractive/fr.md), [PartDesign Pyramide tronquée additive](PartDesign_AdditiveWedge/fr.md)
---

# PartDesign SubtractiveWedge/fr

## Description

Insère une Pyramide tronquée soustractive dans le Corps actif. Sa forme est soustraite du solide existant.

![](images/PartDesign_SubtractiveWedge_example.svg ) *À gauche, le Corps actif (A) en gris et le cône soustractif (B) en rouge transparent ; le résultat final est à droite.*

## Utilisation

1.  Pressez le bouton **<img src="images/PartDesign_SubtractiveWedge.svg" width=24px> '''Pyramide tronquée soustractive'''**. **Remarque**: la pyramide tronquée soustractive fait partie du menu d\'icônes appelé *Créer une primitive soustractive*. Après le lancement de FreeCAD, le Cube soustractif est affiché par défaut dans la barre d\'outils. Pour obtenir la pyramide tronquée soustractive, cliquez sur la flèche vers le bas et choisissez pyramide tronquée soustractive dans le menu.
2.  Définissez les paramètres de la Primitive et de l\'[ancrage](Part_EditAttachment/fr.md).
3.  Cliquez sur **OK**.
4.  Une Pyramide tronquée apparaît dans le Corps actif.

## Options

La pyramide tronquée peut être éditée après sa création de deux façons :

-   Double-cliquez la dans l\'arborescence ou faire un clic droit dessus et sélectionnez **Éditer la primitive** dans le menu contextuel. Cela fait apparaître les paramètres des Primitives.
-   Via l\'[Éditeur de propriétés](Property_editor/fr.md).

## Propriétés

En utilisant le placement par défaut, les entrées ci-dessous sont :

-    **X min/max**: Dimension de la base selon l\'axe X

-    **Y min/max**: Hauteur de la pyramide tronquée

-    **Z min/max**: Dimension de la base selon l\'axe Z

-    **X2 min/max**: Dimension de la face du dessus selon l\'axe X

-    **Z2 min/max**: Dimension de la face du dessus selon l\'axe Z

## Pyramides

Les Pyramides tronquées peuvent être utilisées pour créer des pyramides en fixant **X2 min/max** et **Z2 min/max** en sorte que min = max.





{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveWedge/fr

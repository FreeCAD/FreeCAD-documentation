---
- GuiCommand:/fr
   Name:PartDesign AdditiveWedge
   Name/fr:PartDesign Pyramide tronquée additive
   MenuLocation:Conception de pièces → Créer une primitive additive → Pyramide tronquée additive
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[PartDesign Primitives additives](PartDesign_CompPrimitiveAdditive/fr.md), [PartDesign Pyramide tronquée soustractive](PartDesign_SubtractiveWedge/fr.md)
---

## Description

Insère une pyramide tronquée primitive dans un Corps actif comme fonction de base, ou fusionne avec une existante.

<img alt="" src=images/PartDesign_AdditiveWedge_example.png  style="width:200px;">

## Utilisation

1.  Presser le bouton **<img src="images/PartDesign_AdditiveWedge.svg" width=24px> '''Pyramide tronquée additive'''**. **Remarque** : La pyramide tronquée additive fait partie d\'un menu d\'icônes appelé *Créer une primitive additive*. Après démarrage de FreeCAD, le cube additif est la primitive affichée par défaut dans la barre d\'outils. Pour obtenir la pyramide tronquée, cliquer sur la flèche vers le bas et choisir <img alt="" src=images/PartDesign_AdditiveWedge.png  style="width:24px;"> Pyramide tronquée additive dans le menu.
2.  Définir les paramètres de la Primitive et de l\'[ancrage](Part_EditAttachment/fr.md).
3.  Cliquer sur **OK**.
4.  Une pyramide tronquée apparaît dans le Corps actif.

## Options

La Pyramide tronquée peut être éditée après sa création de deux façons :

-   Double-cliquez la dans l\'arborescence ou faire un clic droit dessus et sélectionnez **Éditer la primitive** dans le menu contextuel. Cela fait apparaître les paramètres de la Primitive.
-   Via l\'[Éditeur de propriétés](Property_editor/fr.md).

## Propriétés

En utilisant le placement par défaut, les entrées ci-dessous sont :

-    {{PropertyData/fr|X min/max}}: Dimension de la base selon l\'axe X

-    {{PropertyData/fr|Y min/max}}: Hauteur de la pyramide tronquée

-    {{PropertyData/fr|Z min/max}}: Dimension de la base selon l\'axe Z

-    {{PropertyData/fr|X2 min/max}}: Dimension de la face du dessus selon l\'axe X

-    {{PropertyData/fr|Z2 min/max}}: Dimension de la face du dessus selon l\'axe Z

## Pyramides

Les Pyramides tronquées peuvent être utilisées pour créer des pyramides en fixant {{PropertyData/fr|X2 min/max}} et {{PropertyData/fr|Z2 min/max}} en sorte que min = max.





{{PartDesign Tools navi

}} 

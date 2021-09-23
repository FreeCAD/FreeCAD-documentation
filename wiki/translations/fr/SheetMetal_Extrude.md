---
- GuiCommand:/fr
   Name:SheetMetal Extrude
   Name/fr:SheetMetal Prolonger une face
   MenuLocation:SheetMetal → Extend Face
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**E**
---

## Description

La commande <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> **SheetMetal Extrude** étend une face de tôle.

## Utilisation

Pour prolonger la face:

1.  Commencez par une plaque ou une feuille de base, sélectionnez une face fine représentant l\'épaisseur de la tôle
2.  Cliquez sur le <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> outil **Extrude** pour étendre la face.


**Remarque**

: Pour créer une plaque de base, utilisez un contour 2D fermé - de préférence une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [esquisse](Sketcher_NewSketch/fr.md) - avec <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> [Tôle de base](SheetMetal_AddBase/fr.md).
Au lieu de cela, vous pouvez également générer une plaque de base avec l\'une des méthodes suivantes :

:\* Méthode 1: <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cube](Part_Box/fr.md)

:\* Méthode 2: Un solide extrudé fait avec une <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Part Extrusion](Part_Extrude/fr.md) à partir d\'un:

::\* <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rectangle](Draft_Rectangle/fr.md) ou d\'un

::\* <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Polyligne](Draft_Wire/fr.md) ou d\'une

::\* <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher Nouvelle esquisse](Sketcher_NewSketch/fr.md)

:\* Méthode 3: <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Corps](PartDesign_Body/fr.md) contenant soit un

::\* <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:24px;"> [PartDesign Cube additif](PartDesign_AdditiveBox/fr.md) ou une

::\* <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Protrusion](PartDesign_Pad/fr.md) réalisée à partir d\'une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher Nouvelle esquisse](Sketcher_NewSketch/fr.md).

:   

    :   Si vous commencez avec un <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> PartDesign Corps, vous pouvez mélanger des fonctions de tôlerie avec des fonctions PartDesign telles que <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [PartDesign Cavité](PartDesign_Pocket/fr.md) or <img alt="" src=images/PartDesign_Hole.svg  style="width:24px;"> [PartDesign Perçage](PartDesign_Hole/fr.md).


**Remarque**

: dans une opération d\'extension, définissez `Refine {{:=` true}}.

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Prolonger une face est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Label|String}}: Valeur par défaut : Le nom modifiable par l\'utilisateur de cet objet, il peut être toute chaîne UTF8 arbitraire.

-    {{PropertyData/fr|Base Feature|Link|hidden}}: Fonctionnalité de base. Lien vers la caractéristique parent.

-    {{PropertyData/fr|_Body|LinkHidden|hidden}}: Lien caché vers le corps du parent.


{{Properties_Title|Parameters}}

-    {{PropertyData/fr|base Object|LinkSub}}: \"Objet de base\". Lien vers la face planaire à étendre.

-    {{PropertyData/fr|gap1|Distance}}: \"Ecart par rapport au côté gauche\". Valeur par défaut : {{value|0,00 mm}}.

-    {{PropertyData/fr|gap2|Distance}}: \"Ecart depuis le côté droit\". Valeur par défaut : {{value|0,00 mm}}.

-    {{PropertyData/fr|length|Length}}: \"Longueur de la paroi\". Valeur par défaut : {{value|10,00 mm}}.


{{Properties_Title|Parameters Ext.}}

-    {{PropertyData/fr|Offset|Distance}}: \"Décalage pour la soustraction\". Valeur par défaut : {{value|20,00 µm}}.

-    {{PropertyData/fr|Refine|Bool}}: \"Utiliser le raffinage\". Valeur par défaut : `True`.

-    {{PropertyData/fr|Sketch|Link}}: \"Esquisse de la paroi\".

-    {{PropertyData/fr|Use Substraction|Bool}}: \"Utiliser la soustraction\". Valeur par défaut : `False`.




[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)

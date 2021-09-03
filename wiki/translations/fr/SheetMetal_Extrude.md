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


<div class="mw-translate-fuzzy">


**Remarque**

: L\'atelier ne possède pas d\'outil pour créer une plaque de base, vous devez donc démarrer votre modèle avec l\'une des méthodes suivantes:

:\* Méthode 1: <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cube](Part_Box/fr.md)

:\* Méthode 2: Un solide extrudé fait avec une <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Part Extrusion](Part_Extrude/fr.md) à partir d\'un:

::\* <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rectangle](Draft_Rectangle/fr.md) ou d\'un

::\* <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Polyligne](Draft_Wire/fr.md) ou d\'une

::\* <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher Nouvelle esquisse](Sketcher_NewSketch/fr.md)

:\* Méthode 3: <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Corps](PartDesign_Body/fr.md) contenant soit un

::\* <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:24px;"> [PartDesign Cube additif](PartDesign_AdditiveBox/fr.md) ou une

::\* <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Protrusion](PartDesign_Pad/fr.md) réalisée à partir d\'une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher Nouvelle esquisse](Sketcher_NewSketch/fr.md).


</div>


:   

    :   Si vous commencez avec un <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> PartDesign Corps, vous pouvez mélanger des fonctions de tôlerie avec des fonctions PartDesign telles que <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [PartDesign Cavité](PartDesign_Pocket/fr.md) or <img alt="" src=images/PartDesign_Hole.svg  style="width:24px;"> [PartDesign Perçage](PartDesign_Hole/fr.md).


**Remarque**

: dans une opération d\'extension, définissez `Refine {{:=` true}}.

## Propriétés

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|gap1}}: retrait du côté gauche.

-    {{PropertyData/fr|gap2}}: retrait du côté droit.

-    {{PropertyData/fr|length}}: longueur du côté plié.




[Category:SheetMetal{{\#translation:}}](Category:SheetMetal.md) [Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Command Reference{{\#translation:}}](Category:External_Command_Reference.md)

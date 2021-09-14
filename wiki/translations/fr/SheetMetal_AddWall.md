---
- GuiCommand:/fr
   Name:SheetMetal AddWall
   Name/fr:SheetMetal Tôle pliée
   MenuLocation:SheetMetal → Make Wall
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**W**
---

## Description

La commande <img alt="" src=images/SheetMetal_Bend.svg  style="width:24px;"> **SheetMetal AddWall** crée un pli sur le bord sélectionné.

<img alt="" src=images/PostBend.png  style="width:320px;">

## Utilisation

Pour ajouter un pli:

1.  Basculez vers l\'<img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:22px;"> [atelier SheetMetal](SheetMetal_Workbench/fr.md).
2.  Commencez avec une plaque de base ou une feuille, sélectionnez un ou plusieurs bords pour recevoir un pli.
3.  Cliquez sur l\'outil <img alt="" src=images/SheetMetal_Bend.svg  style="width:24px;"> **Bend** pour ajouter un pli.


<div class="mw-translate-fuzzy">


**Remarque**

: l\'atelier ne possède pas d\'outil pour créer une plaque de base, vous devez donc démarrer votre modèle avec l\'une des méthodes suivantes:

:\* Method 1: <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cube](Part_Box/fr.md)

:\* Method 2: un solide extrudé fait avec <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Part Extrusion](Part_Extrude/fr.md) à partir d\'un :

::\* <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rectangle](Draft_Rectangle/fr.md) ou un

::\* <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Polyligne](Draft_Wire/fr.md) ou une

::\* <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketch Nouvelle esquisse](Sketcher_NewSketch/fr.md)

::\* Utilisez <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Part Évidement](Part_Thickness/fr.md) pour créer une coque (**Typiquement avec la valeur d'épaisseur de la tôle.**)

:\* Method 3: <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Corps](PartDesign_Body/fr.md) contenant soit un

::\* <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:24px;"> [PartDesign Cube additif](PartDesign_AdditiveBox.md) ou une

::\* <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Protrusion](PartDesign_Pad/fr.md) fabriquée à partir d\'une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketch Nouvelle esquisse](Sketcher_NewSketch/fr.md).

::\* Utilisez <img alt="" src=images/PartDesign_Thickness.svg  style="width:24px;"> [PartDesign Epaisseur](PartDesign_Thickness/fr.md) pour créer une coque (**Typiquement avec la valeur d'épaisseur de la tôle.**)


</div>


:   

    :   Si vous commencez avec un <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> PartDesign Corps, vous pouvez mélanger des fonctions de tôlerie avec des fonctions PartDesign telles que <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [PartDesign Cavité](PartDesign_Pocket/fr.md) ou <img alt="" src=images/PartDesign_Hole.svg  style="width:24px;"> [PartDesign Perçages](PartDesign_Hole/fr.md).

## Propriétés

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Label}}: Nom donné par l\'utilisateur à l\'objet dans la [vue en arborescence](tree_view/fr.md).


{{Properties_Title|Parameters}}

-    {{PropertyData/fr|angle}}: angle de pliage.

-    {{PropertyData/fr|extend1}}: prolonge le mur sur le côté gauche.

-    {{PropertyData/fr|extend2}}: prolonge le mur sur le côté droit.

-    {{PropertyData/fr|gap1}}: espace depuis le côté gauche.

-    {{PropertyData/fr|gap2}}: espace depuis le côté droit.

-    {{PropertyData/fr|invert}}: inverse la direction du pli.

-    {{PropertyData/fr|length}}: longueur du mur.

-    {{PropertyData/fr|mitreangle1}}: angle d\'onglet de pliage sur le côté gauche.

-    {{PropertyData/fr|mitreangle2}}: angle d\'onglet de pliage sur le côté droit.

-    {{PropertyData/fr|radius}}: rayon de courbure.

-    {{PropertyData/fr|relief Type}}: rectangle ou Rond. Activé uniquement lorsqu\'une valeur d\'espacement est définie.

-    {{PropertyData/fr|reliefd}}: profondeur du relief. Activé uniquement lorsqu\'une valeur d\'écart est définie.

-    {{PropertyData/fr|reliefw}}: largeur du relief. Activé uniquement lorsqu\'une valeur d\'espacement est définie.

-    {{PropertyData/fr|kfactor}}: facteur K (également appelé facteur neutre) pour le pli. Utilisé pour calculer la tolérance de pliage lors du dépliage.

-    {{PropertyData/fr|unfold}}: False (par défaut) ou True. Si c\'est vrai, déplie le pli.

## Example

<img alt="" src=images/SheetMetal_AddWall-01.png  style="width:300px;"> 
*A simple tray*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Preparation

This tray is made of a rectangular blank with walls added to its outline edges. And so one outline sketch for the blank has to be prepared in advance.

<img alt="" src=images/SheetMetal_AddWall-02.png  style="width:200px;"> 
*Just a rectangular outline*

### Workflow

1.  Create a blank
    1.  Select the outline sketch  <img alt="" src=images/SheetMetal_AddWall-03.png  style="width:240px;">
    2.  Press the  or use the keyboard shortcut:  <img alt="" src=images/SheetMetal_AddWall-04.png  style="width:240px;">  (The blank is padded in z direction  
2.  Add walls to the outline edges
    1.  Select the blank\'s **outline edges**  <img alt="" src=images/SheetMetal_AddWall-05.png  style="width:240px;">
    2.  Press the  or use the keyboard shortcut:  <img alt="" src=images/SheetMetal_AddWall-06.png  style="width:240px;">
    3.  If the fold is 90° down set the value of **invert** property to true to reverse the direction (and **length** to a lower value for smaller walls)  <img alt="" src=images/SheetMetal_AddWall-01.png  style="width:240px;">  
3.  Add some more walls
    1.  Select the tray\'s **upper outside edges**  <img alt="" src=images/SheetMetal_AddWall-08.png  style="width:240px;">
    2.  Press the  or use the keyboard shortcut:  <img alt="" src=images/SheetMetal_AddWall-09.png  style="width:240px;"> 
    3.  The walls are a bit too long (but nicely trimmed) and so the **length** property has to be set to a lower value  <img alt="" src=images/SheetMetal_AddWall-10.png  style="width:240px;">
    4.  If you like the folds swing outward set the **invert** value to true  <img alt="" src=images/SheetMetal_AddWall-11.png  style="width:240px;">

Done!


</div>


</div>




[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)

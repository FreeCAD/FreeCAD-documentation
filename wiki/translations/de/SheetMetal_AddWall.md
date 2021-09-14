---
- GuiCommand:/de
   Name:SheetMetal AddWall
   Name/de:SheetMetal Kante ansetzen
   MenuLocation:SheetMetal → Make Wall
   Workbenches:[Blech (SheetMetal)](SheetMetal_Workbench/de.md)
   Shortcut:**W**
---

## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_AddWall.svg  style="width:24px;"> [Kante ansetzen](SheetMetal_AddWall/de.md) erzeugt am gewählten Flächenrand eine Kante (Umbug).

<img alt="" src=images/PostBend.png  style="width:320px;">

## Anwendung

Um eine Kante hinzuzufügen:

1.  Zur <img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:22px;"> [Blech](SheetMetal_Workbench/de.md)-Arbeitsumgebung wechseln.
2.  Mit einer Basisplatte oder einem Blech starten und eine oder mehrere Randflächen auswählen, die eine Kante (Umbug) erhalten sollen.
3.  Schaltfläche <img alt="" src=images/SheetMetal_AddWall.svg  style="width:24px;"> [Kante anfügen](SheetMetal_AddWall/de.md) drücken, um die Kante(n) hinzuzufügen.


**Note**

: To create a base plate use a closed 2D outline - preferably a <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketch](Sketcher_NewSketch.md) - with the <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> [Make Base Wall](SheetMetal_AddBase.md) command.
Alternatively you can generate a base plate with one of the following methods as well:

:\* Method 1: <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cube](Part_Box.md)

:\* Method 2: An extruded solid made with <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Part Extrude](Part_Extrude.md) from either a:

::\* <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rectangle](Draft_Rectangle.md) or a

::\* <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Wire](Draft_Wire.md) or a

::\* <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketch](Sketcher_NewSketch.md)

::\* Use <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Part Thickness](Part_Thickness.md) to create shell (**Typically with the thickness value of the sheet metal.**)

:\* Method 3: <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Body](PartDesign_Body.md) containing either an

::\* <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:24px;"> [additive box](PartDesign_AdditiveBox.md) or a

::\* <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Pad](PartDesign_Pad.md) made from a <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketch](Sketcher_NewSketch.md).

::\* Use <img alt="" src=images/PartDesign_Thickness.svg  style="width:24px;"> [PartDesign Thickness](PartDesign_Thickness.md) to create shell (**Typically with the thickness value of the sheet metal.**)

:   

    :   Wenn mit <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Körper erstellen](PartDesign_Body/de.md) gestartet wird, können SheetMetal-Werkzeuge mit PartDesign-Werkzeugen wie z.B. <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [Tasche](PartDesign_Pocket/de.md) oder <img alt="" src=images/PartDesign_Hole.svg  style="width:24px;"> [Bohrung](PartDesign_Hole/de.md) gemischt werden.

## Eigenschaften

### Daten


{{Properties_Title|Base}}

-    **Label**: User name of the object in the [Tree view](Tree_view.md).


{{Properties_Title|Parameters}}

-    **angle**: Bend angle.

-    **extend1**: Extends the wall on the left side.

-    **extend2**: Extends the wall on the right side.

-    **gap1**: Gap from the left side.

-    **gap2**: Gap from the right side.

-    **invert**: Invert bend direction.

-    **length**: Length of the wall.

-    **miterangle1**: Bend miter angle on the left side.

-    **miterangle2**: Bend miter angle on the right side.

-    **radius**: Bend radius.

-    **relief Type**: Rectangle or Round. Enabled only when a gap value is set.

-    **reliefd**: Relief depth. Enabled only when a gap value is set.

-    **reliefw**: Relief width. Enabled only when a gap value is set.

-    **kfactor**: K factor (also known as neutral factor) for the bend. Used to calculate bend allowance when unfolding.

-    **unfold**: False (default) or True. If true, unfolds the bend.

## Beispiel

<img alt="" src=images/SheetMetal_AddWall-01.png  style="width:300px;"> 
*Eine einfache Schale*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Vorbereitung

Diese Schale besteht aus einer rechteckigen Platine mit an ihren Umrisskanten (-Linien) angefügten Kanten. Also muss eine Skizze für die Platine vorbereitet werden.

<img alt="" src=images/SheetMetal_AddWall-02.png  style="width:200px;"> 
*Nur eine rechteckige Kontur*

## Arbeitsablauf

1.  Eine Platine erstellen
    1.  Die Konturskizze auswählen  <img alt="" src=images/SheetMetal_AddWall-03.png  style="width:240px;">
    2.  Schaltfläche  oder Tastenkürzel  <img alt="" src=images/SheetMetal_AddWall-04.png  style="width:240px;">  (Die Platine wird in Z-Richtung aufgedickt)  
2.  Kanten an die Umrisskanten anfügen
    1.  Auswahl der **Umrisskanten** der Platine  <img alt="" src=images/SheetMetal_AddWall-05.png  style="width:240px;">
    2.  Schaltfläche  oder Tastenkürzel  <img alt="" src=images/SheetMetal_AddWall-06.png  style="width:240px;">
    3.  Wenn die Kanten mit 90° nach unten zeigen, setzt man den Wert der Eigenschaft **invert** auf true, um die Richtung umzukehren (und den von **length** auf einen niedrigeren Wert für kürzere Kanten)  <img alt="" src=images/SheetMetal_AddWall-01.png  style="width:240px;">  
3.  Noch mehr Kanten hinzufügen
    1.  Die **oberen Umrisskanten** auswählen  <img alt="" src=images/SheetMetal_AddWall-08.png  style="width:240px;">
    2.  Schaltfläche  oder Tastenkürzel  <img alt="" src=images/SheetMetal_AddWall-09.png  style="width:240px;"> 
    3.  Die Kanten sind jetzt ein wenig zu lang (aber schön beschnitten), also muss die Eigenschaft **length** auf einen niedrigeren Wert gesetzt werden  <img alt="" src=images/SheetMetal_AddWall-10.png  style="width:240px;">
    4.  Sollen die Kanten nach außen aufgestellt werden, muss der Wert **invert** auf true gesetzt werden  <img alt="" src=images/SheetMetal_AddWall-11.png  style="width:240px;">

Fertig!


</div>


</div>




[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)

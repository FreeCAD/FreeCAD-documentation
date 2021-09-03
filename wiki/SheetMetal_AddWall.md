---
- GuiCommand:
   Name:SheetMetal AddWall
   MenuLocation:SheetMetal → Make Wall
   Workbenches:[SheetMetal](SheetMetal_Workbench.md)
   Shortcut:**W**
---

## Description

The <img alt="" src=images/SheetMetal_AddWall.svg  style="width:24px;"> **SheetMetal AddWall** command creates a bend on a selected edge.

 <img alt="" src=images/PostBend.png  style="width:320px;"> 

## Usage

To add a Bend:

1.  Switch to the <img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:22px;"> [SheetMetal Workbench](SheetMetal_Workbench.md).
2.  Start with a base plate or sheet, select one or more edges to receive a bend.
3.  Click on the <img alt="" src=images/SheetMetal_Bend.svg  style="width:24px;"> **Bend** tool to add a bend.


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

    :   If you start with a <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> PartDesign Body, you can mix Sheet Metal features with PartDesign features such as <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [pockets](PartDesign_Pocket.md) or <img alt="" src=images/PartDesign_Hole.svg  style="width:24px;"> [holes](PartDesign_Hole.md).

## Properties

### Data


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






[Category:SheetMetal{{\#translation:}}](Category:SheetMetal.md) [Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Command Reference{{\#translation:}}](Category:External_Command_Reference.md)

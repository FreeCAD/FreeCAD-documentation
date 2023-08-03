---
 GuiCommand:
   Name: SheetMetal AddWall
   MenuLocation: SheetMetal , Make Wall
   Workbenches: SheetMetal Workbench
   Shortcut: **W**
---

# SheetMetal AddWall/en

## Description

The <img alt="" src=images/SheetMetal_AddWall.svg  style="width:24px;"> **SheetMetal AddWall** command creates flanges on selected edges of a base plate. By changing the **angle** property a flange it can be turned into a hem.

A **flange** consists of a 90° cylindrical bend and a planar strip (wall).

<img alt="" src=images/SheetMetal_AddWall-12.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddWall-13.png  style="width:200px;"> 
*Two selected edges → two flanges*

Resetting the **angle** property to about 180° in a second step will create a **hem** instead.

<img alt="" src=images/SheetMetal_AddWall-14.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddWall-15.png  style="width:200px;"> 
*Two selected edges → two hems*

## Usage

1.  Select one or more edge(s) of a base plate.
2.  Activate the <img alt="" src=images/SheetMetal_AddWall.svg  style="width:16px;"> **SheetMetal AddWall** command using one of the following:
    -   The **<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall.md)** button.
    -   The **SheetMetal → <img src="images/SheetMetal_AddWall.svg" width=16px> Make Wall** menu option.
    -   The keyboard shortcut: **W**.

## Notes

To create a base plate use a closed 2D outline - preferably a <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Sketch](Sketcher_NewSketch.md) - with the <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Make Base Wall](SheetMetal_AddBase.md) command.

Alternatively a base plate (blank) can be created with commands from the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md) or <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md).

To create a blank with the [Part Workbench](Part_Workbench.md):

1.  Create a solid using either:
    -   <img alt="" src=images/Part_Box.svg  style="width:16px;"> [Part Box](Part_Box.md).
    -   <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Part Extrude](Part_Extrude.md) from:
        -   A <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Draft Rectangle](Draft_Rectangle.md).
        -   A <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Draft Wire](Draft_Wire.md).
        -   A <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Sketch](Sketcher_NewSketch.md).
2.  Make sure one the dimensions of the Box or the extrusion distance equals the sheet metal thickness.

To create a blank with the [PartDesign Workbench](PartDesign_Workbench.md):

1.  Create a solid using either:
    -   <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:16px;"> [Additive Box](PartDesign_AdditiveBox.md).
    -   <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Pad](PartDesign_Pad.md) from a <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Sketch](Sketcher_NewSketch.md).
2.  Make sure one the dimensions of the Box or the **Length** property of the Pad equals the sheet metal thickness.

If you start with a <img alt="" src=images/PartDesign_Body.svg  style="width:16px;"> [PartDesign Body](PartDesign_Body.md), you can mix SheetMetal features with PartDesign features such as <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [PartDesign Pocket](PartDesign_Pocket.md) or <img alt="" src=images/PartDesign_Hole.svg  style="width:16px;"> [PartDesign Hole](PartDesign_Hole.md).

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal Bend object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties and its label has a default value:

### Data


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.

-    **Base Feature|Link|hidden**: Base Feature. Link to the parent feature.

-    **_Body|LinkHidden|hidden**: Hidden link to the parent body.


{{Properties_Title|Parameters}}

-    **Bend Type|Enumeration**: \"Bend Type\". {{value|Material Outside}} (default), {{value|Material Inside}}, {{value|Thickness Outside}}, {{value|Offset}}.

-    **Length Spec|Enumeration**: \"Type of Length Specification\". {{value|Leg}} (default), {{value|Outer Sharp}}, {{value|Inner Sharp}}, {{value|Tangential}}. <small>(v0.21)</small> 

-    **angle|Angle**: \"Bend Angle\". Default angle: {{value|90,00°}}.

-    **base Object|LinkSub**: \"Base Object\". Link to the planar face to receive a bend.

-    **gap1|Distance**: \"Gap from Left side\". Default: {{value|0,00 mm}}.

-    **gap2|Distance**: \"Gap from Right side\". Default: {{value|0,00 mm}}.

-    **invert|Bool**: \"Invert Bend Direction\". Default: `False`.

-    **length|Length**: \"Length of Wall\". Default: {{value|10,00 mm}}.

-    **radius|Length**: \"Bend Radius\". Default: {{value|1,00 mm}}.


{{Properties_Title|Parameters Ex}}

-    **Auto Miter|Bool**: \"Enable Auto Miter\". Default: `True`.

-    **extend1|Distance**: \"Extend from Left Side\". Default: {{value|0,00 mm}}.

-    **extend2|Distance**: \"Extend from Right Side\". Default: {{value|0,00 mm}}.

-    **kfactor|FloatConstraint**: \"Location of Neutral Line. Caution: Using ANSI standards, not DIN.\".  Default: {{value|0,50}}. K factor (also known as neutral factor) for the bend. Used to calculate bend allowance when unfolding.

-    **max Extend Dist|Length**: \"Auto Miter maximum Extend Distance\". Default: {{value|5,00 mm}}.

-    **min Gap|Length**: \"Auto Miter Minimum Gap\". Default: {{value|5,00 mm}}.

-    **miterangle1|Angle**: \"Bend Miter Angle from Left Side\". Default angle: {{value|0,00°}}.

-    **miterangle2|Angle**: \"Bend Miter Angle from Right Side\". Default angle: {{value|0,00°}}.

-    **offset|Distance**: \"Offset Bend\". Default: {{value|0,00 mm}}.

-    **unfold|Bool**: \"Shows Unfold View of Current Bend\". Default:  `True` unfolds the bend.


{{Properties_Title|Parameters Ex2}}

-    **Sketch|Link**: \"Sketch Object\".

-    **sketchflip|Bool**: \"Flip Sketch Direction\". Default: `False`.

-    **sketchinvert|Bool**: \"Invert Sketch Start\". Default: `False`.


{{Properties_Title|Parameters Ex3}}

-    **Length List|FloatList**: \"Length of Wall List\". Default: {{value|[10,00]}}.

-    **bend AList|FloatList**: \"Bend Angle List\". Default: {{value|[90,00]}}.


{{Properties_Title|Parameters Relief}}

-    **Relief Factor|Float**: \"Relief Factor\". Default: {{value|0,70}}.

-    **Use Relief Factor|Bool**: \"Use Relief Factor\". Default: `False`.

-    **min Relief Gap|Length**: \"Minimum Gap to Relief Cut\". Default: {{value|1,00 mm}}.

-    **relief Type|Enumeration**: \"Relief Type\". {{value|Rectangle}} (default), {{value|Round}}. Enabled only when a gap value is set.

-    **reliefd|Length**: \"Relief Depth\". Default: {{value|1,00 mm}}. Enabled only when a gap value is set.

-    **reliefw|Length**: \"Relief Width\". Default: {{value|0,80 mm}}. Enabled only when a gap value is set.

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



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddWall/en

---
- GuiCommand:
   Name: SheetMetal AddFoldWall
   MenuLocation: SheetMetal - Fold a Wall
   Workbenches: [SheetMetal](SheetMetal_Workbench.md)
   Shortcut: **C** **F**
---

# SheetMetal AddFoldWall/pl

## Description

The <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:24px;"> **SheetMetal AddFoldWall** command folds a sheet metal plate (blank) at a chosen line.

It can be used with a pre-cut blank to

-   create a perforated bend zone
-   leave planar sections within the bend area and beyond e.g. tabs. (needs gaps in the bend line)

<img alt="" src=images/SheetMetal_AddFoldWall-13.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddFoldWall-14.png  style="width:300px;">



*Pre-cut blank and bend line with two gaps → perforated bend zone with some still planar geometry*

## Usage

1.  Select the face to be bent.
2.  Hold down the **Ctrl** key (or the **Command** key on macOS).
3.  Select the coplanar <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [sketch](Sketcher_Workbench.md) (i.e. lying on the same plane) containing the **bend line (segments)** (preferably from the [tree view](Tree_view.md)).
4.  Release the **Ctrl** key (or the **Command** key).
5.  Activate the <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:16px;"> **SheetMetal AddFoldWall** command using one of the following:
    -   The **<img src="images/SheetMetal_AddFoldWall.svg" width=16px> [Fold a Wall](SheetMetal_AddFoldWall.md)** button.
    -   The **SheetMetal → <img src="images/SheetMetal_AddFoldWall.svg" width=16px> Fold a Wall** menu option.
    -   The keyboard shortcut: **C** Then **F**.
6.  Change the value of the property **Position** to adjust the position of the bend according to the bend line.

<img alt="" src=images/SheetMetal_AddFoldWall-15.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddFoldWall-14.png  style="width:300px;">



*The bend line(s) lying in the middle of the perforation → to keep the bend centred the same way the property **Position* has to be set to {{value|middle**}}

### Notes

-   The bend line sketch has to be **coplanar** to the selected face.

-   The bend line segments have to be **colinear** to each other.

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal Fold object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.

-    **Base Feature|Link|hidden**: Base Feature. Link to the parent feature.

-    **_Body|LinkHidden|hidden**: Hidden link to the parent body.


{{Properties_Title|Parameters}}

-    **Bend Line|Link**: \"Bend Reference Line List\". Links to the bend line objects.

-    **Position|Enumeration**: \"Bend Line Position\". {{value|forward}} (default), {{value|middle}}, {{value|backward}}.

-    **angle|Angle**: \"Bend Angle\". Default angle: {{value|90,00°}}.

-    **base Object|LinkSub**: \"Base Object\". Link to the planar face to be bent.

-    **invert|Bool**: \"Invert Bend Direction\". Default: `False`

-    **invertbend|Bool**: \"Invert Solid Bend Direction\". Default:  `True` swaps the side of the line to be bent.

-    **kfactor|FloatConstraint**: \"Neutral Axis Position\". Default: {{value|0,50}}.

-    **radius|Length**: \"Bend Radius\". Default: {{value|1,00 mm}}.

-    **unfold|Bool**: \"Unfold Bend\". Default: `False`

## Example

<img alt="" src=images/SheetMetal_AddFoldWall-01.png  style="width:300px;"> 
*A simple clip*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Preparation

This clip is made of a blank that receives three folds and so we need four sketches prepared in advance:

:   \- one for the outline plus slot (blank)
:   \- one for the bend at the tip
:   \- one for the upward bend
:   \- one for the downward bend

Easiest way to guarantee that one face of the blank and all folding lines are coplanar is to create all sketches on the same plane - the **XY_Plane** in this case.

The folding lines could be created with other tools but hey, we have a <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench.md)!

<img alt="" src=images/SheetMetal_AddFoldWall-21.png  style="width:280px;"> <img alt="" src=images/SheetMetal_AddFoldWall-20.png  style="width:200px;"> 
*Sketches on their common plane and their representation in the design tree*

### Workflow

1.  Create a blank
    1.  Select the outline sketch
    2.  Press the  or use the keyboard shortcut:  <img alt="" src=images/SheetMetal_AddFoldWall-02.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-03.png  style="width:280px;"> 
2.  Fold the tip
    1.  Select the blank\'s **bottom face**
    2.  Select the **sketch** named ***Tip Fold line*** (preferably from the tree view)  (and don\'t forget the control/command key )
    3.  Press the  or use the keyboard shortcut: <img alt="" src=images/SheetMetal_AddFoldWall-10.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-04.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-05.png  style="width:280px;">
    4.  The fold should be 90° down and so some values in the properties window need to be set e.g.:  - the **angle** value to 60°  - the **invert** value to true for an upward bend  
3.  Create the downward fold
    1.  Select the blank\'s **bottom face**
    2.  And then the **sketch** named ***Down-Fold line***
    3.  Press the  or use the keyboard shortcut: <img alt="" src=images/SheetMetal_AddFoldWall-11.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-06.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-07.png  style="width:280px;">
    4.  Set the **angle** value to 92°
    5.  If the wrong section of the part moved set the **invertbend** value to true  
4.  To create the upward fold
    1.  select the blank\'s **bottom face**
    2.  and then the **sketch** named ***Up-Fold line***
    3.  Press the  or use the keyboard shortcut: <img alt="" src=images/SheetMetal_AddFoldWall-12.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-08.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-09.png  style="width:280px;">
    4.  Set the **angle** value to 80°
    5.  If the fold is downward set the **invert** value to true
    6.  If needed set the **invertbend** value to true  

Done!

Note!: In real life the upward fold must be done before the downward fold. Only the virtual world of CAD allows us to bend through solid material. This way the orientation of the static section doesn\'t change.  All sketches lie on the same plane to avoid sketches attached to moveable faces.


</div>


</div>



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddFoldWall/pl

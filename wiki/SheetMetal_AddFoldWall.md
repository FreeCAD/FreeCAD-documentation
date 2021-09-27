---
- GuiCommand:
   Name:SheetMetal AddFoldWall
   MenuLocation:SheetMetal → Fold a Wall
   Workbenches:[SheetMetal](SheetMetal_Workbench.md)
   Shortcut:**C** **F**
---

# SheetMetal AddFoldWall

## Description

The <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:24px;"> **SheetMetal AddFoldWall** command folds a wall at a chosen line with a specified bend radius.

## Usage

1.  Select a planar face of the SheetMetal object
2.  Select a coplanar line
3.  Press the  or use the keyboard shortcut: **C** then **F**.

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

Easiest way to guarantee that one face of the blank and all folding lines are coplanar is to create all sketches on the same plane - the **XY\_Plane** in this case.

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






_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal AddFoldWall

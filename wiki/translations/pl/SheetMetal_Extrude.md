---
- GuiCommand:
   Name:SheetMetal Extrude
   MenuLocation:SheetMetal → Extend Face
   Workbenches:[SheetMetal](SheetMetal_Workbench.md)
   Shortcut:**E**
---

# SheetMetal Extrude/pl

## Description

The <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> **SheetMetal Extrude** command extends a sheet metal plate at a selected edge face.

It creates a **simple extension** along the face normal of the selected edge face:

<img alt="" src=images/SheetMetal_Extrude-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-02.png  style="width:200px;">

If an outline sketch is added it creates **interlocking geometry** to close a profile:

<img alt="" src=images/SheetMetal_Extrude-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-04.png  style="width:200px;">



*Three profiles with outline sketches to add -> three results*

## Usage

### Simple Extension 

1.  Select one or more edge face(s) to be extended.
2.  Activate the <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> **SheetMetal Extrude** command using one of the following:
    -   The **<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude.md)** button.
    -   The **SheetMetal → <img src="images/SheetMetal_Extrude.svg" width=16px> Extend Face** menu option.
    -   The keyboard shortcut: **E**.
3.  Change the value of the property **length** to adjust the length of the extension.

### Interlocking Extension 

1.  Select one edge face to be extended.
2.  Activate the <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> **SheetMetal Extrude** command (see above).
3.  Add a coplanar outline sketch to the property **Sketch**.
4.  Set the property **Use Subtraction** to `True` to create cut-outs to make room for the extensions.
5.  Set the property **Offset** to adjust the clearance around the extension.

<img alt="" src=images/SheetMetal_Extrude-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-04.png  style="width:200px;">



*Three profiles -> position of the sketches -> results without cut-outs -> final results*

### Notes

-   A sketch can contain more than one outline.

:   After inserting a sketch, at least one of its outlines must at least touch one opposite face or the tool will fail to create any extension or cut-out.





:   Just one outline touching an opposite face is enough to create extension geometry from all outlines of the sketch.

-   Each cut-out will have a cuboid shape, no matter what shape the corresponding outline sketch is.

-   Shapes other than rectangles may behave little bit strange and even though the object can be unfolded, the result will not turn out as expected.

<img alt="" src=images/SheetMetal_Extrude-07.png  style="width:250px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-08.png  style="width:250px;">



*Three outline sketches and their resulting extensions: separate triangle plate with a rectangular cut-out, circle without clearance -> unfold solid is split at an unexpected position *

-   In an extension operation it is recommended to leave the property **Refine** set to `True` (default).

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal Extend object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.

-    **Base Feature|Link|hidden**: Base Feature. Link to the parent feature.

-    **_Body|LinkHidden|hidden**: Hidden link to the parent body.


{{Properties_Title|Parameters}}

-    **base Object|LinkSub**: \"Base object\". Link to the planar face to be extended.

-    **gap1|Distance**: \"Gap from the left side\". Default: {{value|0,00 mm}}.

-    **gap2|Distance**: \"Gap from the right side\". Default: {{value|0,00 mm}}.

-    **length|Length**: \"Length of Wall\". Default: {{value|10,00 mm}}.


{{Properties_Title|Parameters Ext.}}

-    **Offset|Distance**: \"Offset for subtraction\". Default: {{value|20,00 µm}}.

-    **Refine|Bool**: \"Use Refine\". Default: `True`.

-    **Sketch|Link**: \"Wall Sketch\".

-    **Use Subtraction|Bool**: \"Use Subtraction\". Default: `False`




[<img src="images/Property.png" style="width:16px"> SheetMetal](Category_SheetMetal.md) [<img src="images/Property.png" style="width:16px"> Addons](Category_Addons.md) [<img src="images/Property.png" style="width:16px"> External Command Reference](Category_External_Command_Reference.md)

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal Extrude/pl

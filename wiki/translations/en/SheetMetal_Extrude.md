---
- GuiCommand:
   Name:SheetMetal Extrude
   MenuLocation:SheetMetal → Extend Face
   Workbenches:[SheetMetal](SheetMetal_Workbench.md)
   Shortcut:**E**
---

# SheetMetal Extrude/en

## Description

The <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> **SheetMetal Extrude** command extends a sheet metal face.

## Usage

To Extend the face:

1.  Start with a base plate or sheet, select a thin face representing the thickness of the metal sheet
2.  Click on the <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> **Extrude** tool to extend the face.


**Note**

: To create a base plate use a closed 2D outline - preferably a <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketch](Sketcher_NewSketch.md) - with the <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> [Make Base Wall](SheetMetal_AddBase.md) command.
Alternatively you can generate a base plate with one of the following methods as well:

:\* Method 1: <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cube](Part_Box.md)

:\* Method 2: An extruded solid made with <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Part Extrude](Part_Extrude.md) from either a:

::\* <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rectangle](Draft_Rectangle.md) or a

::\* <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Wire](Draft_Wire.md) or a

::\* <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketch](Sketcher_NewSketch.md)

:\* Method 3: <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Body](PartDesign_Body.md) containing either an

::\* <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:24px;"> [additive box](PartDesign_AdditiveBox.md) or a

::\* <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Pad](PartDesign_Pad.md) made from a <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketch](Sketcher_NewSketch.md).

:   

    :   If you start with a <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> PartDesign Body, you can mix Sheet Metal features with PartDesign features such as <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [pockets](PartDesign_Pocket.md) or <img alt="" src=images/PartDesign_Hole.svg  style="width:24px;"> [holes](PartDesign_Hole.md).


**Note**

: In an extension operation, set `Refine {{:=` true}}.

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

-    **Offset|Distance**: \"Offset for substraction\". Default: {{value|20,00 µm}}.

-    **Refine|Bool**: \"Use Refine\". Default: `True`.

-    **Sketch|Link**: \"Wall Sketch\".

-    **Use Substraction|Bool**: \"Use Substraction\". Default: `False`




[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)

---
[documentation index](../README.md) > [SheetMetal](Category:SheetMetal.md) > SheetMetal Extrude/en

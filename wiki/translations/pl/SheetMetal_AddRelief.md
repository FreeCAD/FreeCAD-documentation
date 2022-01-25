---
- GuiCommand:
   Name:SheetMetal AddRelief
   MenuLocation:SheetMetal → Make Relief
   Workbenches:[SheetMetal](SheetMetal_Workbench.md)
   Shortcut:**S** **R**
   SeeAlso:[SheetMetal AddJunction](SheetMetal_AddJunction.md), [SheetMetal AddBend](SheetMetal_AddBend.md)
---

# SheetMetal AddRelief/pl

## Description

The <img alt="" src=images/SheetMetal_Relief.svg  style="width:16px;"> [SheetMetal AddRelief](SheetMetal_AddRelief.md) command creates corner reliefs, cutouts, at the points where three sections (base plate/walls/flanges) of a sheet metal object meet. Without these reliefs the object will not be unfoldable.

This command is the first of three steps to convert a shell object made with the [Part Workbench](Part_Workbench.md) or [PartDesign Workbench](PartDesign_Workbench.md) into an unfoldable sheet metal object:

1.  [SheetMetal AddRelief](SheetMetal_AddRelief.md)
2.  [SheetMetal AddJunction](SheetMetal_AddJunction.md)
3.  [SheetMetal AddBend](SheetMetal_AddBend.md)

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:100px;"> 
*Make Relief - cut off corners*

## Usage

1.  Select one or more corner vertex(es).
2.  Activate the <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **SheetMetal AddRelief** command using one of the following:
    -   The **<img src="images/SheetMetal_AddRelief.svg" width=16px> [SheetMetal AddRelief](SheetMetal_AddRelief.md)** button.
    -   The **SheetMetal → <img src="images/SheetMetal_AddRelief.svg" width=16px> Make Relief** menu option.
    -   The keyboard shortcut: **S** then **R**

<img alt="" src=images/SheetMetal_ConvertShellObject-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-06.png  style="width:200px;">

## Notes

The commands <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[SheetMetal AddRelief](SheetMetal_AddRelief.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[SheetMetal AddJunction](SheetMetal_AddJunction.md)**, and <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[SheetMetal AddBend](SheetMetal_AddBend.md)** work best with hollow cuboids i.e. shell objects with a constant thickness and only 90° angles between faces.

Shell objects can be created with commands from the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md) or the <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md).

To create a hollow cuboid with the [Part Workbench](Part_Workbench.md):

1.  Create a solid using either:
    -   <img alt="" src=images/Part_Box.svg  style="width:16px;"> [Part Box](Part_Box.md).
    -   <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Part Extrude](Part_Extrude.md) from:
        -   A <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Draft Rectangle](Draft_Rectangle.md).
        -   A <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Draft Wire](Draft_Wire.md).
        -   A <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Sketch](Sketcher_NewSketch.md).
2.  Use <img alt="" src=images/Part_Thickness.svg  style="width:16px;"> [Part Thickness](Part_Thickness.md) to create a shell object from the solid (Typically with the thickness value of the sheet metal).

To create a hollow cuboid with the [PartDesign Workbench](PartDesign_Workbench.md):

1.  Create a solid using either:
    -   <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:16px;"> [Additive Box](PartDesign_AdditiveBox.md).
    -   <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Pad](PartDesign_Pad.md) from a <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Sketch](Sketcher_NewSketch.md).
2.  Use <img alt="" src=images/PartDesign_Thickness.svg  style="width:16px;"> [PartDesign Thickness](PartDesign_Thickness.md) to create a shell object from the solid (Typically with the thickness value of the sheet metal).

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal Relief object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties and its label has a default value:

### Data


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.

-    **Base Feature|Link|hidden**: Base Feature. Link to the parent feature.

-    **_Body|LinkHidden|hidden**: Hidden link to the parent body.


{{Properties_Title|Parameters}}

-    **base Object|LinkSub**: \"Base Object\". Links to the corner vertexes defining relief positions.

-    **relief|Length**: \"Relief Size\". Default: {{value|2,00 mm}}.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddRelief/pl

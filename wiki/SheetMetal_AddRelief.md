---
 GuiCommand:
   Name: SheetMetal AddRelief
   MenuLocation: SheetMetal , Make Relief
   Workbenches: SheetMetal Workbench
   Shortcut: **S** **R**
   SeeAlso: SheetMetal_AddJunction, SheetMetal_AddBend
---

# SheetMetal AddRelief

## Description

The <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> [SheetMetal AddRelief](SheetMetal_AddRelief.md) command creates corner reliefs, cutouts, at the points where three sections (base plate/walls/flanges) of a sheet metal object meet. Without these reliefs the object will not be unfoldable.

This command is the first of three steps to convert a shell object made with the [Part Workbench](Part_Workbench.md) or [PartDesign Workbench](PartDesign_Workbench.md) into an unfoldable sheet metal object:

1.  [SheetMetal AddRelief](SheetMetal_AddRelief.md)
2.  [SheetMetal AddJunction](SheetMetal_AddJunction.md)
3.  [SheetMetal AddBend](SheetMetal_AddBend.md)

 <img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:100px;">  
*Make Relief - cut off corners*

## Usage

1.  Select one or more corner vertex(es).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/SheetMetal_AddRelief.svg" width=16px> [Make Relief](SheetMetal_AddRelief.md)** button.
    -   Select the **SheetMetal → <img src="images/SheetMetal_AddRelief.svg" width=16px> Make Relief** option from the menu.
    -   Right-click in the [Tree view](Tree_view.md) or the [3D view](3D_view.md) and select the **Sheet Metal → <img src="images/SheetMetal_AddRelief.svg" width=16px> Make Relief** option from the context menu.
    -   Use the keyboard shortcut: **S** then **R**.
3.  The **Add Corner Relief on Solid** [Task panel](Task_panel.md) opens (introduced in version 0.5.00).
4.  Optionally press the **Select** button to add more vertices.
    -   Press the **Preview** button to finish the selection and display the changes.
5.  Optionally adjust the parameters in the Task panel.
6.  Press the **OK** button to finish the command and close the Task panel.
7.  A **CornerRelief** object will be created consisting of one new corner relief at each selected vertex.
8.  Optionally adjust the parameters in the [Property editor](Property_editor.md).

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

A SheetMetal Relief object is derived from a [Part Feature](Part_Feature.md) object or, if it is inside a [PartDesign Body](PartDesign_Body.md), from a [PartDesign Feature](PartDesign_Feature.md) object, and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Parameters}}

-    **base Object|LinkSub**: \"Base Object\". Links to the corner vertexes defining relief positions.

-    **relief|Length**: \"Relief Size\". Default: {{value|2,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddRelief

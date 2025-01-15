---
 GuiCommand:
   Name: SheetMetal AddJunction
   MenuLocation: SheetMetal , Make Junction
   Workbenches: SheetMetal_Workbench
   Shortcut: **S** **J**
   SeeAlso: SheetMetal_AddRelief, SheetMetal_AddBend
---

# SheetMetal AddJunction

## Description

The <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:24px;"> [SheetMetal AddJunction](SheetMetal_AddJunction.md) command creates open junctions between two sections (walls/flanges) of a sheet metal object. Without these junctions sheet metal sections connected to the same base will not be unfoldable.

This command is the second of three steps to convert a shell object made with the [Part Workbench](Part_Workbench.md) or [PartDesign Workbench](PartDesign_Workbench.md) into an unfoldable sheet metal object:

1.  [SheetMetal AddRelief](SheetMetal_AddRelief.md)
2.  [SheetMetal AddJunction](SheetMetal_AddJunction.md)
3.  [SheetMetal AddBend](SheetMetal_AddBend.md)

 <img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:100px;">  
*Make Junction - cut edges open*

## Usage

1.  Select one or more edges.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/SheetMetal_AddJunction.svg" width=16px> [Make Junction](SheetMetal_AddJunction.md)** button.
    -   Select the **SheetMetal → <img src="images/SheetMetal_AddJunction.svg" width=16px> Make Junction** option from the menu.
    -   Right-click in the [Tree view](Tree_view.md) or the [3D view](3D_view.md) and select the **SheetMetal → <img src="images/SheetMetal_AddJunction.svg" width=16px> Make Junction** option from the context menu.
    -   Use the keyboard shortcut: **S** then **J**.
3.  The **Add Junction Parameter** [Task panel](Task_panel.md) opens (introduced in version 0.5.00).
4.  Optionally press the **Select** button to add more faces.
    -   Press the **Preview** button to finish the selection and display the changes.
5.  Optionally adjust the parameters in the Task panel.
6.  Press the **OK** button to finish the command and close the Task panel.
7.  A **Junction** object will be created consisting of one opening at each selected edge.
8.  Optionally adjust the parameters in the [Property editor](Property_editor.md).

 <img alt="" src=images/SheetMetal_ConvertShellObject-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-07.png  style="width:200px;"> 

## Notes

-   The commands <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[SheetMetal AddRelief](SheetMetal_AddRelief.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[SheetMetal AddJunction](SheetMetal_AddJunction.md)**, and <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[SheetMetal AddBend](SheetMetal_AddBend.md)** work best with hollow cuboids i.e. shell objects with a constant thickness and only 90° angles between faces.
-   See [SheetMetal AddRelief](SheetMetal_AddRelief#Notes.md) for hints about creating shell objects of cuboids.

-   **Junction** in this case is not the result of this tool, which is a gap between adjacent planar faces, but rather describes the location where two planar faces of the finished real world object meet, to be welded, for example.

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal Junction object is derived from a [Part Feature](Part_Feature.md) object or, if it is inside a [PartDesign Body](PartDesign_Body.md), from a [PartDesign Feature](PartDesign_Feature.md) object, and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Parameters}}

-    **base Object|LinkSub**: \"Base Object\". Links to the edges defining gap/junction positions.

-    **gap|Length**: \"Junction Gap\". Default: {{value|2,00 mm}}.Size of gap/junction to be added.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal AddJunction

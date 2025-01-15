---
 GuiCommand:
   Name: SheetMetal Extrude
   MenuLocation: SheetMetal , Extend Face
   Workbenches: SheetMetal_Workbench
   Shortcut: **E**
---

# SheetMetal Extrude/en

## Description

The <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> **SheetMetal Extrude** command extends a sheet metal plate at a selected edge face.

It creates a **simple extension** along the face normal of the selected edge face:

<img alt="" src=images/SheetMetal_Extrude-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-02.png  style="width:200px;">

If an outline sketch is added it creates **interlocking geometry** to close a profile:

<img alt="" src=images/SheetMetal_Extrude-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-04.png  style="width:200px;">



*Three profiles with outline sketches to add → three results*

## Usage

### Simple Extension 

1.  Select one or more edge face(s) to be extended.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude.md)** button.
    -   Select the **Sheet Metal → <img src="images/SheetMetal_Extrude.svg" width=16px> Extend Face** option from the menu.
    -   Right-click in the [Tree view](Tree_view.md) or the [3D view](3D_view.md) and select the **Sheet Metal → <img src="images/SheetMetal_Extrude.svg" width=16px> Extend Face** option from the context menu.
    -   Use the keyboard shortcut: **E**.
3.  The **Extend Parameters** [Task panel](Task_panel.md) opens (introduced in version 0.5.00).
4.  Optionally press the **Select** button to add more faces.
    -   Press the **Preview** button to finish the selection and display the changes.
5.  Optionally adjust the parameters in the Task panel.
6.  Press the **OK** button to finish the command and close the Task panel.
7.  An **Extend** object will be created consisting of one new face extension at each selected face.
8.  Optionally adjust the parameters in the [Property editor](Property_editor.md).

### Interlocking Extension 

:   (Prepare a <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [sketch](Sketcher_Workbench.md) for interlocking tabs)

1.  Select the edge face to be extended.
2.  Invoke the command as described above.
3.  Press the **OK** button to finish the command and close the Task panel.
4.  In the [Property editor](Property_editor.md) press the **...** button of the **Sketch** property.
5.  The Link dialog window opens.
    -   Select the prepared sketch from the list
    -   Press the **OK** button to close the dialog.
6.  Set the property **Use Subtraction** to `True` to create cut-outs to make room for the extensions.
7.  Set the property **Offset** to adjust the clearance around the extension.

<img alt="" src=images/SheetMetal_Extrude-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-04.png  style="width:200px;">



*Three profiles → position of the sketches → results without cut-outs → final results*

### Notes

-   A sketch can contain more than one outline.

:   After inserting a sketch, at least one of its outlines must at least touch one opposite face or the tool will fail to create any extension or cut-out.





:   Just one outline touching an opposite face is enough to create extension geometry from all outlines of the sketch.

-   Each cut-out will have a cuboid shape, no matter what shape the corresponding outline sketch is.

-   Shapes other than rectangles may behave little bit strange and even though the object can be unfolded, the result will not turn out as expected.

<img alt="" src=images/SheetMetal_Extrude-07.png  style="width:250px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-08.png  style="width:250px;">



*Three outline sketches and their resulting extensions: separate triangle plate with a rectangular cut-out, circle without clearance → unfold solid is split at an unexpected position *

-   In an extension operation it is recommended to leave the property **Refine** set to `True` (default).

-   The extension operation with a linked sketch may fail due to coplanar issues if the face on the sketch side and the face on the opposite side are coplanar, but with opposite orientations. A small offset may help in such a case.

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal Extend object is derived from a [Part Feature](Part_Feature.md) object or, if it is inside a [PartDesign Body](PartDesign_Body.md), from a [PartDesign Feature](PartDesign_Feature.md) object, and inherits all its properties. It also has the following additional properties:

### Data


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



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal Extrude/en

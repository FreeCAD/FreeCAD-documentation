---
 GuiCommand:
   Name: SheetMetal_Unfold
   Name/it: Dispiega
   MenuLocation: SheetMetal , Unfold
   Workbenches: SheetMetal Workbench/it
   Shortcut: None
   Version: 
   SeeAlso: SheetMetal_UnattendedUnfold
---

# SheetMetal Unfold/it


</div>

## Description

The <img alt="" src=images/SheetMetal_Unfold.svg  style="width:24px;"> **SheetMetal Unfold** command unfolds a sheet metal object.

## Usage

1.  Select a planar face of the sheet metal part.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/_SheetMetal_Unfold.svg_" width=16px> [Unfold](SheetMetal_Unfold.md)** button.
    -   Select the **Sheet Metal → <img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold.md)** option from the menu.
    -   Right-click in the [Tree view](Tree_view.md) or the [3D view](3D_view.md) and select the **Sheet Metal → <img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold.md)** option from the context menu.
    -   Use the keyboard shortcut: **U**.
3.  The **Unfold sheet metal object** [Task panel](Task_panel.md) opens.
4.  Adjust unfolding options in the [task panel](Task_panel.md):
    -   Optionally activate the projection options of the unfold sketch and set the colors.
    -   Optionally activate the export option.
    -   If you don\'t use a **Material Definition Sheet** (see [Notes](#Notes.md)):
        1.  Set the **Material Definition Sheet** option to {{Value|Manual K-Factor}}.
        2.  Optionally toggle the ANSI or DIN radio buttons (see [Notes](#Notes.md)).
        3.  Adjust the Manual K-Factor value (see [Notes](#Notes.md)).
    -   Optionally adjust the Unfold object transparency.
5.  Press the **OK** button to finish the command and close the Task panel.
6.  An **Unfold** object will be created.
7.  Optionally adjust the parameters in the [Property editor](Property_editor.md).

## Notes

-   See the [Material Definition Sheet](https://github.com/shaise/FreeCAD_SheetMetal#material-definition-sheet) and [K-factor](https://github.com/shaise/FreeCAD_SheetMetal#physical-material-definitions) sections of the project page for more information.
-   For an explanation of the different value ranges of ISO and ANSI K-factors see the table on [this](https://de.wikipedia.org/wiki/Biegeverkürzung#Korrektur_durch_den_sog._k-Faktor) page (in German).

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal Unfold object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It has no additional properties.

## Limitations

-   The sheet metal should have a constant thickness.
-   Flat faces should not contain split lines.
-   Flat faces must be truly planar and not B-spline approximations.
-   Faces of bend angles must be truly cylindrical and also not B-spline approximations.
-   Versions before 0.5.00: The Unfold feature is not parametric. If the model is modified you have to unfold it again.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal Unfold/it

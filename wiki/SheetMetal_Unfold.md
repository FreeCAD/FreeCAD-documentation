---
- GuiCommand   *
   Name   *SheetMetal Unfold
   MenuLocation   *SheetMetal → Unfold
   Workbenches   *[SheetMetal](SheetMetal_Workbench.md)
   Shortcut   ***U**
   SeeAlso   *[SheetMetal UnattendedUnfold](SheetMetal_UnattendedUnfold.md)
---

# SheetMetal Unfold

## Description

The <img alt="" src=images/SheetMetal_Unfold.svg  style="width   *24px;"> **SheetMetal Unfold** command unfolds a sheet metal object.

## Usage

1.  Select a planar face of the sheet metal part.
2.  Activate the <img alt="" src=images/SheetMetal_Unfold.svg  style="width   *16px;"> [Unfold](SheetMetal_Unfold.md) command using one of the following   *
    -   The **<img src="images/_SheetMetal_Unfold.svg_" width=16px> [Unfold](SheetMetal_Unfold.md)** button.
    -   The **SheetMetal → <img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold.md)** menu option.
    -   The keyboard shortcut   * **U**.
3.  Adjust unfolding options in the [task panel](Task_panel.md) by   *
    -   Selecting the projection options of the unfold sketch.
    -   Selecting the method of bend deduction with K-factor   *
        - Use a [Material Definition Sheet](https   *//github.com/shaise/FreeCAD_SheetMetal#material-definition-sheet).
        - Select a manual [K-factor](https   *//github.com/shaise/FreeCAD_SheetMetal#terminology) then the [ANSI or DIN](https   *//de.wikipedia.org/wiki/Biegeverkürzung#Korrektur_durch_den_sog._k-Faktor) standard to apply

## Properties

See also   * [Property editor](Property_editor.md).

A SheetMetal Unfold object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It has no additional properties, but its label has a default value   *

### Data


{{Properties_Title|Base}}

-    **Label|String**   * Default value   * The user editable name of this object, it may be any arbitrary UTF8 string.

## Limitations

-   Sheet metal should have constant thickness
-   Flat faces should be planar with no split lines
-   Bend angles should be radius with cylindrical faces
-   Unfold feature is not parametric at the moment.






[Category   *SheetMetal](Category_SheetMetal.md) [Category   *Addons](Category_Addons.md) [Category   *External Command Reference](Category_External_Command_Reference.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Unfold

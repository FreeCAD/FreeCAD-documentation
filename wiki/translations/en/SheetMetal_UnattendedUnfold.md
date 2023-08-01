---
- GuiCommand:
   Name:SheetMetal UnattendedUnfold
   MenuLocation:SheetMetal - Unattended Unfold
   Workbenches:[SheetMetal](SheetMetal_Workbench.md)
   Shortcut:**U**
   SeeAlso:[SheetMetal Unfold](SheetMetal_Unfold.md)
---

# SheetMetal UnattendedUnfold/en

## Description

The <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:24px;"> [Unattended Unfold](SheetMetal_UnattendedUnfold.md) command unfolds a sheet metal object.

If the parent body of a selected planar face has been subject to unfolding before, this tool will skip the menu in the task panel. Otherwise it will show an error message asking for either \"set a Manual K-factor\" or \"use a Material Definition Sheet\".

With the first use of the <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Unfold](SheetMetal_Unfold.md) command the parent body\'s label received a suffix (such as *\_material_0.5din*) and after that it is ready to be use with this tool.

## Usage

1.  Select one planar face of a sheet metal part.
2.  Activate the <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:16px;"> [UnattendedUnfold](SheetMetal_UnattendedUnfold.md) command using one of the following:
    -   The **<img src="images/_SheetMetal_UnattendedUnfold.svg_" width=16px> [Unattended Unfold](SheetMetal_UnattendedUnfold.md)** button.
    -   The **SheetMetal → <img src="images/SheetMetal_UnattendedUnfold.svg" width=16px> [Unattended Unfold](SheetMetal_UnattendedUnfold.md)** menu option.
    -   The keyboard shortcut: **U**

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal Unfold object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It has no additional properties, but its label has a default value:

### Data


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.

## Limitations

See <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Unfold](SheetMetal_Unfold.md) for limitations.



---
![](images/Button_right.svg) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal UnattendedUnfold/en

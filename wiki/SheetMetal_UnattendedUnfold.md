---
 GuiCommand:
   Name: SheetMetal UnattendedUnfold
   MenuLocation: SheetMetal , Unattended Unfold
   Workbenches: SheetMetal_Workbench
   Shortcut: **U**
   SeeAlso: SheetMetal_Unfold
---

# SheetMetal UnattendedUnfold

## Description

The <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:24px;"> [Unattended Unfold](SheetMetal_UnattendedUnfold.md) command unfolds a sheet metal object.

This command is not available by default, see [Notes](#Notes.md).

If the parent body of a selected planar face has been subject to unfolding before, this command will skip the menu in the task panel. Otherwise it will show an error message asking for either \"set a Manual K-factor\" or \"use a Material Definition Sheet\".

With the first use of the <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Unfold](SheetMetal_Unfold.md) command the parent body\'s label received a suffix (such as *\_material_0.5din*) and after that it is ready to be used with this command.

## Usage

1.  Select one planar face of a sheet metal part.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/SheetMetal_UnattendedUnfold.svg_" width=16px> [Unattended Unfold](SheetMetal_UnattendedUnfold.md)** button.
    -   Select the **Sheet Metal → <img src="images/SheetMetal_UnattendedUnfold.svg" width=16px> [Unattended Unfold](SheetMetal_UnattendedUnfold.md)** option from the menu.
    -   Right-click in the [Tree view](Tree_view.md) or the [3D view](3D_view.md) and select the **Sheet Metal → <img src="images/SheetMetal_UnattendedUnfold.svg" width=16px> [Unattended Unfold](SheetMetal_UnattendedUnfold.md)** option from the context menu.
    -   Use the keyboard shortcut: **U**.
3.  An **Unfold** object will be created.
4.  Optionally adjust the parameters in the [Property editor](Property_editor.md).

## Notes

To make this command available, first enable Engineering Mode in the preferences. Go to **Edit → Preferences → SheetMetal → General Settings**, and set **Engineering UX Mode** to {{Value|Enabled}}. Changing this preference requires a restart of FreeCAD.

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal Unfold object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It has no additional properties.

## Limitations

See <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Unfold](SheetMetal_Unfold.md) for limitations.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal UnattendedUnfold

---
 GuiCommand:
   Name: SheetMetal UnattendedUnfold
   MenuLocation: SheetMetal , Unattended Unfold
   Workbenches: SheetMetal_Workbench
   Shortcut: **U**
   SeeAlso: SheetMetal_Unfold
---

# SheetMetal UnattendedUnfold/en

## Description

The <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:24px;"> [Unattended Unfold](SheetMetal_UnattendedUnfold.md) command unfolds a sheet metal object.

This command is not available by default, see [Notes](#Notes.md).

If the parent body of a selected planar face has been subject to unfolding before, this command will skip the menu in the task panel. Otherwise it will show an error message asking for either \"set a Manual K-factor\" or \"use a Material Definition Sheet\".

With the first use of the <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Unfold](SheetMetal_Unfold.md) command the parent body\'s label received a suffix (such as *\_material_0.5din*) and after that it is ready to be used with this command.

## Usage

1.  Select one planar face of a sheet metal part.
2.  Activate the <img alt="" src=images/SheetMetal_UnattendedUnfold.svg  style="width:16px;"> [UnattendedUnfold](SheetMetal_UnattendedUnfold.md) command using one of the following:
    -   The **<img src="images/_SheetMetal_UnattendedUnfold.svg_" width=16px> [Unattended Unfold](SheetMetal_UnattendedUnfold.md)** button.
    -   The **SheetMetal → <img src="images/SheetMetal_UnattendedUnfold.svg" width=16px> [Unattended Unfold](SheetMetal_UnattendedUnfold.md)** menu option.
    -   The keyboard shortcut: **U**

## Notes

To make this command available, first enable Engineering Mode in the preferences. Go to **Edit → Preferences → SheetMetal → General Settings**, and set **Engineering UX Mode** to {{Value|Enabled}}. Changing this preference requires a restart of FreeCAD.

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal Unfold object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It has no additional properties, but its label has a default value:

### Data


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.

## Limitations

See <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Unfold](SheetMetal_Unfold.md) for limitations.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal UnattendedUnfold/en

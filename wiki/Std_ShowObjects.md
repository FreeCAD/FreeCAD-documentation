---
- GuiCommand:
   Name: Std ShowObjects
   MenuLocation: View -> Visibility -> Show all objects
   Workbenches: All
   SeeAlso: Std_ToggleVisibility, Std_ShowSelection, Std_HideSelection, Std_ToggleObjects, Std_HideObjects
---

# Std ShowObjects

## Description

The **Std ShowObjects** command shows all objects belonging to the active document in [3D views](3D_view.md). Be careful when you use this command as it will also show sub-elements of [PartDesign bodies](PartDesign_Body.md) and objects used for [Part Booleans](Part_Boolean.md). In most cases these should stay invisible.

## Usage

1.  Select the **View → Visibility → <img src="images/Std_ShowObjects.svg" width=16px> Show all objects** option from the menu.

## Notes

-   The action of this command cannot be undone with [Std Undo](Std_Undo.md).
-   The visibility of an object can also be changed through its related **Visibility** property in the [Property editor](Property_editor.md) or the [Combo view](Combo_view.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

For a scripting example see [Std ToggleVisibility](Std_ToggleVisibility.md).




 {{Std Base navi}}



---
⏵ [documentation index](../README.md) > Std ShowObjects

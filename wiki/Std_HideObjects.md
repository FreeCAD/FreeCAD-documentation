---
- GuiCommand:
   Name:Std HideObjects
   MenuLocation:View → Visibility → Hide all objects
   Workbenches:All
   SeeAlso:[Std ToggleVisibility](Std_ToggleVisibility.md), [Std ShowSelection](Std_ShowSelection.md), [Std HideSelection](Std_HideSelection.md), [Std ToggleObjects](Std_ToggleObjects.md), [Std ShowObjects](Std_ShowObjects.md)
---

## Description

The **Std HideObjects** command hides all objects belonging to the active document in [3D views](3D_view.md).

## Usage

1.  Select the {{MenuCommand|View → Visibility → <img src="images/Std_HideObjects.svg" width=16px> Hide all objects}} option from the menu.

## Notes

-   Invisible objects are displayed with a greyed out label and a greyed out icon in the [Tree view](Tree_view.md).
-   The action of this command cannot be undone with [Std Undo](Std_Undo.md).
-   The visibility of an object can also be changed through its related **Visibility** property in the [Property editor](Property_editor.md) or the [Combo view](Combo_view.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

For a scripting example see [Std ToggleVisibility](Std_ToggleVisibility.md).




 {{Std Base navi}}  

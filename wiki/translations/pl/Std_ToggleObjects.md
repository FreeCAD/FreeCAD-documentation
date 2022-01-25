---
- GuiCommand:
   Name:Std ToggleObjects
   MenuLocation:View → Visibility → Toggle all objects
   Workbenches:All
   SeeAlso:[Std ToggleVisibility](Std_ToggleVisibility.md), [Std ShowSelection](Std_ShowSelection.md), [Std HideSelection](Std_HideSelection.md), [Std ShowObjects](Std_ShowObjects.md), [Std HideObjects](Std_HideObjects.md)
---

# Std ToggleObjects/pl

## Description

The **Std ToggleObjects** command toggles the visibility of all objects belonging to the active document in [3D views](3D_view.md). Be careful when you use this command as it will also toggle the visibility of sub-elements of [PartDesign bodies](PartDesign_Body.md) and objects used for [Part Booleans](Part_Boolean.md). In most cases these should stay invisible.

## Usage

1.  Select the **View → Visibility → <img src="images/Std_ToggleObjects.svg" width=16px> Toggle all objects** option from the menu.

## Notes

-   Invisible objects are displayed with a greyed out label and a greyed out icon in the [Tree view](Tree_view.md).
-   Objects nested in a [Std Part](Std_Part.md), or a [Std Link](Std_LinkMake.md) to a [Std Group](Std_Group.md), or a LinkGroup, and [features](PartDesign_Feature.md) of a [PartDesign Body](PartDesign_Body.md) will only be visible in [3D views](3D_view.md) if their parent is visible as well. This means that a feature in a PartDesign Body that is nested in a Std Part will only be visible in 3D views if the feature itself, the PartDesign Body, and the Std Part are all visible. And if the Std Part is in turn nested in another Std Part, then that last object must also be visible.
-   If the visibility of a [Std Group](Std_Group.md) (or an object derived from it such as an [Arch BuildingPart](Arch_BuildingPart.md)) is changed, the visibility of its nested objects will change accordingly. But their visibility can be changed independently as well.
-   The action of this command cannot be undone with [Std Undo](Std_Undo.md).
-   The visibility of an object can also be changed through its related **Visibility** property in the [Property editor](Property_editor.md) or the [Combo view](Combo_view.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

For a scripting example see [Std ToggleVisibility](Std_ToggleVisibility.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ToggleObjects/pl

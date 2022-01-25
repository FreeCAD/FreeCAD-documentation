---
- GuiCommand:
   Name:Std HideSelection
   MenuLocation:View → Visibility → Hide selection
   Workbenches:All
   SeeAlso:[Std ToggleVisibility](Std_ToggleVisibility.md), [Std ShowSelection](Std_ShowSelection.md), [Std ToggleObjects](Std_ToggleObjects.md), [Std ShowObjects](Std_ShowObjects.md), [Std HideObjects](Std_HideObjects.md)
---

# Std HideSelection/en

## Description

The **Std HideSelection** command hides selected objects in [3D views](3D_view.md).

## Usage

1.  Select one or more objects.
2.  There are several ways to invoke the command:
    -   Select the **View → Visibility → <img src="images/Std_HideSelection.svg" width=16px> Hide selection** option from the menu.
    -   Select the **<img src="images/Std_HideSelection.svg" width=16px> Hide selection** option from the [Tree view](Tree_view.md) context menu. This option is not available in the [PartDesign Workbench](PartDesign_Workbench.md).

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
![](images/Right_arrow.png) [documentation index](../README.md) > Std HideSelection/en

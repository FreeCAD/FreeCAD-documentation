---
 GuiCommand:
   Name: Std ShowSelection
   MenuLocation: View , Visibility , Show selection
   Workbenches: All
   SeeAlso: Std_ToggleVisibility, Std_HideSelection, Std_ToggleObjects, Std_ShowObjects, Std_HideObjects
---

# Std ShowSelection/en

## Description

The **Std ShowSelection** command shows selected objects in [3D views](3D_view.md).

## Usage

1.  Select one or more objects.
    -   Invisible objects can be selected in the [Tree view](Tree_view.md).
    -   Be careful when you use **Ctrl**+**A** to select all objects in the Tree view. This will also selects sub-elements of [PartDesign bodies](PartDesign_Body.md) and objects used for [Part Booleans](Part_Boolean.md). In most cases these should stay invisible.
    -   Objects used for [Part Booleans](Part_Boolean.md) are also selected when you use **Ctrl**+**A** in a 3D view.
2.  There are several ways to invoke the command:
    -   Select the **View → Visibility → <img src="images/Std_ShowSelection.svg" width=16px> Show selection** option from the menu.
    -   Select the **<img src="images/Std_ShowSelection.svg" width=16px> Show selection** option from the Tree view context menu.

## Notes

See [Std ToggleVisibility](Std_ToggleVisibility#Notes.md).

## Scripting

See [Std ToggleVisibility](Std_ToggleVisibility#Scripting.md).



---
⏵ [documentation index](../README.md) > Std ShowSelection/en

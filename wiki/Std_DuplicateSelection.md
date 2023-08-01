---
- GuiCommand:
   Name: Std DuplicateSelection
   MenuLocation: Edit - Duplicate selected object
   Workbenches: All
   SeeAlso: [Std Cut](Std_Cut.md), [Std Copy](Std_Copy.md), [Std Paste](Std_Paste.md)
---

# Std DuplicateSelection

## Description

The **Std DuplicateSelection** command duplicates objects within the active document.

## Usage

1.  Select one or more objects.
2.  Select the **Edit → Duplicate selected object** option from the menu.
3.  If the objects have dependencies that have not been selected, a dialog box will prompt you to specify which should be included.

## Notes

-   FreeCAD will automatically change the internal names and, depending on the preferences, labels of objects to avoid name conflicts.

## Preferences

-   Duplicate labels are allowed if **Tools → Edit parameters... → BaseApp → Preferences → Document → DuplicateLabels** is set to `True`. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).




 {{Std Base navi}}



---
⏵ [documentation index](../README.md) > Std DuplicateSelection

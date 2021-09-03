---
- GuiCommand:
   Name:Std MergeProjects
   MenuLocation:File → Merge project...
   Workbenches:All
---

## Description

The **Std MergeProjects** command adds the contents of a FreeCAD file into the active document.

## Usage

1.  Select the {{MenuCommand|File → <img src="images/Std_MergeProjects.svg" width=16px> Merge project...}} option from the menu.
2.  Select a FreeCAD file in the dialog box.
3.  Press the **Open** button.

## Options

-   Press **Esc** or the **Cancel** button to abort the command.

## Notes

-   A project cannot be merged with itself, selecting the current file is not allowed.
-   FreeCAD will automatically change the internal names and, depending on the preferences, labels of objects to avoid name conflicts.

## Preferences

-   The last used file location is stored: {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath}}.
-   Duplicate labels are allowed if {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → Document → DuplicateLabels}} is set to `True`. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).




 {{Std Base navi}}  

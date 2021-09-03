---
- GuiCommand:
   Name:Std Paste
   MenuLocation:Edit → Paste
   Workbenches:All
   Shortcut:**Ctrl**+**V**
   SeeAlso:[Std Cut](Std_Cut.md), [Std Copy](Std_Copy.md), [Std DuplicateSelection](Std_DuplicateSelection.md)
---

## Description

The **Std Paste** command pastes objects from the Clipboard into the active document.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_Paste.svg" width=16px> [Std Paste](Std_Paste.md)** button.
    -   Select the {{MenuCommand|Edit → <img src="images/Std_Paste.svg" width=16px> Paste}} option from the menu.
    -   Select the {{MenuCommand|<img src="images/Std_Paste.svg" width=16px> Paste}} option from the [Tree view](Tree_view.md) context menu. Note that this option is only available when an exiting object has been selected.
    -   Use the keyboard shortcut: **Ctrl**+**V**.

## Notes

-   FreeCAD will automatically change the internal names and, depending on the preferences, labels of objects to avoid name conflicts.
-   A spreadsheet cell alias that already exists in the spreadsheet will not be pasted.
-   When you are working in a FreeCAD text window, an input box or a spreadsheet, the standard keyboard shortcut **Ctrl**+**V**, in almost all cases, does not call the **Std Paste** command but uses the Paste function from the OS instead.
-   It is not possible to copy-paste native objects between FreeCAD and other applications.

## Preferences

-   Duplicate labels are allowed if {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → Document → DuplicateLabels}} is set to `True`. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).

## Scripting

The **Std Paste** command can be applied only after running the **[Std Copy](Std_Copy.md)** command:

 
```python
FreeCADGui.runCommand('Std_Copy')
FreeCADGui.runCommand('Std_Paste')
```




 {{Std Base navi}}  

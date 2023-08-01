---
- GuiCommand:
   Name:Std Quit
   MenuLocation:File - Exit
   Workbenches:All
   Shortcut:**Alt**+**F4**
   SeeAlso:[Std Close](Std_CloseActiveWindow.md)
---

# Std Quit

## Description

The **Std Quit** command closes the FreeCAD application and optionally saves unsaved documents.

## Usage

1.  There are several ways to invoke the command:
    -   Select the **File → <img src="images/Std_Quit.svg" width=16px> Exit** option from the menu.
    -   Use the keyboard shortcut: **Alt**+**F4**.
2.  If there are unsaved documents a dialog box will prompt you to save them:
    -   Press the **Save** button to save the active document. If required enter a filename first.
    -   Press the **Discard** button to discard the active document and lose all changes.

## Options

-   If there are multiple unsaved documents: check the {{CheckBox|TRUE|Apply answer to all}} checkbox to avoid being prompted for each unsaved document separately.
-   If there are unsaved documents: press **Esc** or the **Cancel** button to abort the command.

## Preferences

-   The last used file location is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.




 {{Std Base navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std Quit

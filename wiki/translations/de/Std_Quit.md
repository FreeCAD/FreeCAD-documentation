# Std Quit/de
---
- GuiCommand:/de   Name:Std Quit   Name/de:Std Beenden   MenuLocation:[Workbenches:Alle   Shortcut:**Alt**+**F4**   SeeAlso:[[Std Open/de|Std Open](Std_File_Menu/de___Datei]]_→_Beenden.md),[Std Import](Std_Import/de.md)---


</div>

## Beschreibung

The **Std Quit** command closes the FreeCAD application and optionally saves unsaved documents.

## Anwendung

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





{{Std Base navi

}}

---
[documentation index](../README.md) > Std Quit/de

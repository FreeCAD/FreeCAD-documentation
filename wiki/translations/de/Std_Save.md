---
- GuiCommand:/de   Name/de:Std Save   MenuLocation:[Workbenches:Alle   Shortcut:**Strg**+**S**   SeeAlso:[[Std_SaveAs/de|Speichern unter...](Std_File_Menu/de___Datei]]_→_Speichern.md)---


</div>

## Description

The **Std Save** command saves the active document.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_Save.svg" width=16px> [Std Save](Std_Save.md)** button.
    -   Select the {{MenuCommand|File → <img src="images/Std_Save.svg" width=16px> Save}} option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**S**.
2.  For new documents: enter a filename in the dialog box and press the **Save** button.

## Options

-   For new documents: press **Esc** or the **Cancel** button to abort the command.

## Notes

-   This command can also be used to save dependency graphs. See [Std DependencyGraph](Std_DependencyGraph.md).

## Preferences

-   The last used file location is stored: {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath}}.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To save a document use the `save` method of the document object. A new document must first be saved with the `saveAs` method of the document object. For a scripting example see [Std New](Std_New.md).





{{Std Base navi

}}  

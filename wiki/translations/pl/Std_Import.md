---
- GuiCommand:
   Name:Std Import
   MenuLocation:File → Import...
   Workbenches:All
   Shortcut:**Ctrl**+**I**
   SeeAlso:[Std Open](Std_Open.md), [Import Export](Import_Export.md), [Import Export Preferences](Import_Export_Preferences.md)
---

## Description

The **Std Import** command imports geometry from a different file format into the active document. Many file formats are supported and for some formats multiple import options exist. See [Import Export](Import_Export.md) for more information.

## Usage

1.  There are several ways to invoke the command:
    -   Select the **File → <img src="images/Std_Import.svg" width=16px> Import...** option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**I**.
2.  Optionally select the correct file format in the dialog box.
3.  Select a file.
4.  Press the **Open** button.

## Options

-   Press **Esc** or the **Cancel** button to abort the command.

## Notes

-   To convert an imported [mesh object](Mesh_Workbench.md) into a solid see the [Import from STL or OBJ](Import_from_STL_or_OBJ.md) tutorial.
-   To import into a new document you can use the [Std Open](Std_Open.md) command.
-   Some workbenches have additional import commands. See: [Import Export](Import_Export.md).

## Preferences

-   See: [Import Export Preferences](Import_Export_Preferences.md).
-   The last used file location is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.
-   The last used import filter is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileImportFilter**.





{{Std Base navi

}}  

[Category:File\_Formats{{\#translation:}}](Category:File_Formats.md)

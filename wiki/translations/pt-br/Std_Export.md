---
- GuiCommand:
   Name:Std Export
   MenuLocation:File → Export...
   Workbenches:All
   Shortcut:**Ctrl**+**E**
   SeeAlso:[Std PrintPdf](Std_PrintPdf.md), [Import Export](Import_Export.md), [Import Export Preferences](Import_Export_Preferences.md)
---

# Std Export/pt-br

## Description

The **Std Export** command exports selected objects to a different file format. Many file formats are supported and for some formats multiple export options exist. See [Import Export](Import_Export.md) for more information.

## Usage

1.  Select one or more objects. To avoid exporting invisible or duplicate objects:
    -   Be careful when you use **Ctrl**+**A** to select all objects. This will also select invisible objects.
    -   Select a [PartDesign Body](PartDesign_Body.md) by only picking the body itself or its last feature.
    -   Select a [Std Group](Std_Group.md) or a [Std Part](Std_Part.md) by only picking the parent object itself or the objects nested inside it.
    -   Do not use the [Std SelectAll](Std_SelectAll.md) command as it will also select sub-elements of PartDesign Bodies.
    -   For the same reason the [Std BoxSelection](Std_BoxSelection.md) command should be avoided in FreeCAD version 0.18 and earlier.
2.  There are several ways to invoke the command:
    -   Select the **File → <img src="images/Std_Export.svg" width=16px> Export...** option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**E**.
3.  Select the correct file format in the dialog box.
4.  Enter a filename.
5.  Press the **Save** button.

## Options

-   Press **Esc** or the **Cancel** button to abort the command.

## Notes

-   To export a [mesh object](Mesh_Workbench.md) to a solid file format it must first be converted. See the [Import from STL or OBJ](Import_from_STL_or_OBJ.md) tutorial.
-   Some workbenches have additional export commands. See: [Import Export](Import_Export.md).

## Preferences

-   See: [Import Export Preferences](Import_Export_Preferences.md).
-   The last used file location is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.
-   The last used export filter is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileExportFilter**.





{{Std Base navi

}}  

[<img src="images/Property.png" style="width:16px"> File\_Formats](Category_File_Formats.md)

---
[documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Std Export/pt-br

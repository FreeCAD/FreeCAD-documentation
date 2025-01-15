---
 GuiCommand:
   Name: Std Export
   MenuLocation: File , Export...
   Workbenches: All
   Shortcut: **Ctrl**+**E**
   SeeAlso: Std_PrintPdf, Import_Export, Import_Export_Preferences
---

# Std Export/pt-br



## Descrição

O comando **Exportar** exporta objetos selecionados para um formato de arquivo diferente. Muitos formatos de arquivo são suportados e para alguns formatos existem várias opções de exportação. Consulte [Importar Exportar](Import_Export/pt-br.md) para obter mais informações.



## Uso

1.  Select one or more objects. To avoid exporting invisible or duplicate objects:
    -   Be careful when you use **Ctrl**+**A** to select all objects. This will also select invisible objects.
    -   Select a [PartDesign Body](PartDesign_Body.md) by only picking the body itself or its last feature.
    -   Select a [Std Group](Std_Group.md) or a [Std Part](Std_Part.md) by only picking the parent object itself or the objects nested inside it.
    -   Do not use the [Std SelectAll](Std_SelectAll.md) command as it will also select sub-elements of PartDesign Bodies.
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
-   Some workbenches have additional export commands. See [Import Export](Import_Export.md).

## Preferences

-   See [Import Export Preferences](Import_Export_Preferences.md).



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Std Export/pt-br

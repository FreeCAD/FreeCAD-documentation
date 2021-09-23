---
- GuiCommand:/de   Name/de:Std Open
   MenuLocation:[Datei](Std_File_Menu/de.md) → Öffnen...
   Workbenches:Alle
   Shortcut:**Strg**+**O**
   SeeAlso:[Speichern](Std_Save/de.md), [Importieren...](Std_Import/de.md)
---

# Std Open/de


</div>


<div class="mw-translate-fuzzy">

Öffnet und lädt Projektdateien in den Arbeitsplatz und abhängig von den installierten Erweiterungsmodulen werden weitere Dateitypen unterstützt wie [\*.IGES](https://de.wikipedia.org/wiki/IES), [\*.STEP](https://de.wikipedia.org/wiki/Standard_for_the_exchange_of_product_model_data), [\*.BREP](https://de.wikipedia.org/wiki/Boundary_Representation), [\*.STL](https://de.wikipedia.org/wiki/STL-Schnittstelle), [\*.OBJ](https://de.wikipedia.org/wiki/Wavefront_OBJ), [\*.PLY](https://de.wikipedia.org/wiki/Polygon_File_Format), etc.


</div>

The **Std Open** command opens a file. If the file is not a native FreeCAD file (\*.FCStd) its geometry will be imported into a new document. See [Std Import](Std_Import.md) for more information.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_Open.svg" width=16px> [Std Open](Std_Open.md)** button.
    -   Select the **File → <img src="images/Std_Open.svg" width=16px> Open...** option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**O**.
2.  Optionally select the correct file format in the dialog box.
3.  Select a file.
4.  Press the **Open** button.

## Options

-   Press **Esc** or the **Cancel** button to abort the command.

## Preferences

-   The last used file location is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To open a document use the `open(filepath)` method or the `openDocument(filepath, [hidden<nowiki>=</nowiki>False])` method of the FreeCAD application.

These methods create and return a document and load a project file into it. The `filepath` argument must be a string pointing to an existing file. If the file doesn\'t exist or the file cannot be loaded an I/O exception is thrown. In this case the created document is kept, but will be empty. If `hidden<nowiki>=</nowiki>True` is used, the document won\'t be displayed in the GUI and no tab will appear for it. This allows performing automatic operations on a document and closing it without disrupting the user interface.

For a scripting example see [Std New](Std_New#Scripting.md).





{{Std Base navi

}}

---
[documentation index](../README.md) > Std Open/de

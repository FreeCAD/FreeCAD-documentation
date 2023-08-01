---
- GuiCommand:
   Name: Std Export
   Name/ro: Exportul
   Workbenches: All
   MenuLocation: [File](Std_File_Menu/ro.md) - Exportul
   Shortcut: Ctrl + E
   SeeAlso: [Importul](Std_Import/ro.md)
---

# Std Export/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Aceasta este comanda standard pentru a exporta obiecte din interiorul unui document FreeCAD în alte formate de fișiere. O selecție trebuie făcută înainte de lansarea comenzii.


</div>

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Selectați obiectele pentru a fi exportate, fie în arborescența Model sau în vizualizarea 3D utilizând [box selection](Std_BoxSelection.md).
2.  Mergeți în meniu pe traseul File → Export
3.  Selectați tipul de fișier
4.  Tastați un nume
5.  Apăsați butonul **Save**.


</div>

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



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Std Export/ro

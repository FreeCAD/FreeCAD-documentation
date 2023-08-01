# DXF/es
## Historia del fondo 

The Drawing Exchange Format (DXF) is a proprietary CAD data format developed by Autodesk to enable file exchange between their flagship AutoCAD product and other software. There are a number of good software libraries for reading/writing the DXF format.

There are many versions of the DXF format. You will hear of certain key versions, such as R12 (from 1992) or R14 (from 1997 which had splines). Later versions of DXF have 3D elements, but these are rarely used or implemented. How you use DXF to share CAD data between programs depends mainly on the limitations and bugs in the corresponding readers/importers and writers/exporters. These are rarely fully documented and can be a great source of frustration.

If you are editing DXF files and want them to remain almost the same when you save them, we recommend you use [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD) or [QCad](https://en.wikipedia.org/wiki/QCad) because these programs\' internal data structures are compatible with the objects in the DXF file.

In FreeCAD the DXF readers must translate the geometry (e.g., spline shapes) from the DXF file into the specific internal representations of the Workbench.

## Methods for importing DXF to FreeCAD 

If you intend to review the settings frequently, we recommend you go to Edit → Preferences → Import-Export → DXF and tick the box \"\[ \] Show this dialog when importing and exporting\".

More information is on the pages [Draft DXF](Draft_DXF.md) and [FreeCAD and DXF Import](FreeCAD_and_DXF_Import.md).

If you are using the imported geometry to build 3D shapes in the Part Design Workbench, try the [Sketcher Validate](Sketcher_ValidateSketch.md) after you have imported the DXF into a sketch.

### C++ DXF importer 

This implementation of fast, but skips features it doesn\'t recognize, such as DXF splines. It also can only import geometry into the Draft Workbench as individual entries in the Model tree. These can have the colors read from the file if you tick to enable this option. For further information, see [this forum post](https://forum.freecadweb.org/viewtopic.php?f=3&t=32493).

### Python DXF importer 

This importer has to be downloaded and installed before it can be used. See [Dxf Importer Install](Dxf_Importer_Install.md), or use the \"\[ \] Allow FreeCAD to automatically download and update the DXF libraries\" option.

This importer has more features (such as implementing splines), and has the option of loading the DXF shapes into the Sketcher Workbench. However, be warned that all the elements of the sketch will appear individually a second time in the model tree, which can be confusing. You can delete all these individual objects and retain the single sketch (which appears as the second entry in the list of new elements).

Unfortunately, the Sketcher Workbench does not implement colors, so all the geometry will appear on the same level, which is a problem if the file contains many construction lines. One work-around is to open your drawing in LibreCAD, and delete all the geometry you don\'t want to appear before saving a file that contains exactly the geometry that you want to load.

### Macros

Keep an eye out on the FreeCAD forum or in the [Macros recipes](Macros_recipes.md) for alternative implementations of DXF importing and cleaning up as they develop.

## Saving DXF 

In addition to the options under the Edit → Preferences, the [TechDraw Workbench](TechDraw_Workbench.md) can also export drawing pages to DXF using the [TechDraw ExportPageDXF](TechDraw_ExportPageDXF.md) function.



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Draft](Category_Draft.md) > [TechDraw](Category_TechDraw.md) > [File_Formats](Category_File_Formats.md) > DXF/es

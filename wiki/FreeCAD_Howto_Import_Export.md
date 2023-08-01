# FreeCAD Howto Import Export
** "This page is WIP. Please do not translate yet. Thank you. R-Frank" (†2017, r-frank)**

This page attempts to answer the most common questions asked on the FreeCAD forums on import and export of data to/from other programs. If you have a problem or question regarding FreeCAD, check below first.

Then, if you cannot find an answer for your specific question, head to the FreeCAD [forum](http://forum.freecadweb.org/)!




## Import 2D/3D Data 

### Autodesk DWG 

Please refer to the Page [FreeCAD and DWG-Import](FreeCAD_and_DWG_Import.md)

### Autodesk DXF 

Please refer to the Page [FreeCAD and DXF Import](FreeCAD_and_DWG_Import.md)

Tutorial: [DXF Importer Install](Dxf_Importer_Install.md)

### BREP Format 

Todo

### Calculix Result 

Todo

### Collada

Importing Collada files requires an external Python module to be installed on your system. This can be easily added by following the directions found on the [Extra Python modules](Extra_python_modules.md) page under [pyCollada](http://www.freecadweb.org/wiki/index.php?title=Extra_python_modules#pyCollada) in this Wiki. Once the pyCollada Python module is installed, importing Collada files is the same as any standard file import.

See also: [Importing From Sketchup](Importing_From_Sketchup.md)

### Common Airfoil Data 

Please refer to the Page [Common Airfoil Data Import](Common_Airfoil_Data_Import.md)

### Drawing

Todo

### FEM Formats 

Todo

### FreeCAD Material Cards 

Is intended to import Material Cards for use in FreeCAD itself and in the [FEM-Workbench](FEM_Workbench.md).

**Not functional at the moment.**

### IDF emn file 

Todo

### IGES

Currently there is no support for text or annotation import with the IGES format due to lack of support with FreeCAD\'s geometric CAD kernel.

### Image Formats 

Todo

### Industry Foundation Classes IFC 

-   [Import/Export IFC - compiling IfcOpenShell](Import/Export_IFC_-_compiling_IfcOpenShell.md)

### Inventor V2.1 

Todo

### Mesh Formats 

Please refer to the Page [FreeCAD and Mesh Import](FreeCAD_and_Mesh_Import.md)

### Open CAD Format 

Todo

### OpenSCAD CSG Format 

Todo

### OpenSCAD Format 

See [Import OpenSCAD code](Import_OpenSCAD_code.md)

### Point Formats 

Todo

### POVRay Format 

Todo

### Python

Todo

### Step with Colors 

Currently there is no support for text or annotation import with the STEP format due to lack of support with FreeCAD\'s geometric CAD kernel.

### Shapefiles

See [Arch SHP](Arch_SHP.md)

### Spreadsheet

Todo

### SVG as geometry 

Todo

### VRML 2.0 

Todo

## Export 2D/3D Data 

### 3D View (SVG) 

Todo

### Autodesk DWG 

Todo

### Asymptote ASY 

[Export meshes to Asymptote code.](Asymptote.md)

### BREP Format 

Todo

### Collada 

Todo

### Drawing 

Todo

### FEM Formats 

Todo

### Flattened SVG 

Todo

### GL Transmission Format gITF 

-   [glTF](GlTF.md)

### IGES Format 

-   From the 3D-View simply select (in the tree-view) the solid(s) to export and select \"File -\> Export\".
-   Then select your file type (IGES). No need to type in the file extension. FreeCAD will append a \".iges\" automatically

**Tip**
Pressing CTRL-A will select ALL solids in the tree view, even the invisible ones.
Make sure to manually select all the solids you want to export.
Currently there is no support for text or annotation export with the IGES format due to lack of support with FreeCAD\'s geometric CAD kernel.

### Industry Foundation Classes IFC 

-   [Import/Export IFC - compiling IfcOpenShell](Import/Export_IFC_-_compiling_IfcOpenShell.md)

### Inventor V2.1 

Todo

### Mesh Formats 

-   From the 3D-View simply select (in the tree-view) the solid(s) to export and select \"File -\> Export\".
-   Then select your file type. Be sure to type in also the file extension. Since these formats are mesh formats, the solids will be exported with a \"standard\" mesh quality.
-   Use the [Mesh Workbench](Mesh_Workbench.md) to adjust the quality of the mesh if needed.

**Tip**
Pressing CTRL-A will select ALL solids in the tree view, even the invisible ones.
Make sure to manually select all the solids you want to export.

### Open CAD Format 

Todo

### OpenSCAD CSG Format 

Todo

### OpenSCAD Format 

Todo

### Portable Document Format 

Todo

### Step with Colors 

From the 3D-View simply select (in the tree-view) the solid(s) to export and select \"File -\> Export\".

In FreeCAD 0.15 and above, by selecting \"Edit -\> Preferences\" and then \"Import-Export\" in the left column you should have access to Step-Options such as units, scheme and Header Information. Be aware that Step AP203 does not support assembly structures, while Step AP 214 does.

Currently there is no support for text or annotation export with the STEP format due to lack of support with FreeCAD\'s geometric CAD kernel.

### Spreadsheet 

Todo

### TetGen File 

Todo

### VRML 2.0 

Todo

### Wavefront OBJ - Arch Workbench 

Todo

-   Convert STL to OBJ [forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=43543&p=372030#p370843)

### WebGL File 

Todo

## Export Data from third-party programs for import into FreeCAD 

Tips and Tricks with using Third-Party Software

### Inkscape

When exporting SVG-Data from Inkscape to FreeCAD be sure to use the file type \"plain svg\".

### Sketchup

Please refer to the Page [Importing From Sketchup](Importing_From_Sketchup.md)

## Related

-   [Import Export](Import_Export.md)
-   [Import Export Preferences](Import_Export_Preferences.md)



---
⏵ [documentation index](../README.md) > FreeCAD Howto Import Export

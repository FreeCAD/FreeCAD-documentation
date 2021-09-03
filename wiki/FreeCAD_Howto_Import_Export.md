
{{VeryImportantMessage| "This page is WIP. Please do not translate yet. Thank you. R-Frank" (†2017, r-frank)}}

This page attempts to answer the most common questions asked on the FreeCAD forums on import and export of data to/from other programs. If you have a problem or question regarding FreeCAD, check below first.

Then, if you cannot find an answer for your specific question, head to the FreeCAD [forum](http://forum.freecadweb.org/)!


{{TOCright}}

## Import 2D/3D Data {#import_2d3d_data}

### Autodesk DWG {#autodesk_dwg}

Please refer to the Page [FreeCAD and DWG-Import](FreeCAD_and_DWG_Import.md)

### Autodesk DXF {#autodesk_dxf}

Please refer to the Page [FreeCAD and DXF Import](FreeCAD_and_DXF_Import.md)

Tutorial: [DXF Importer Install](Dxf_Importer_Install.md)

### BREP Format {#brep_format}

Todo

### Calculix Result {#calculix_result}

Todo

### Collada

Importing Collada files requires an external Python module to be installed on your system. This can be easily added by following the directions found on the [Extra python modules](Extra_python_modules.md) page under [pyCollada](http://www.freecadweb.org/wiki/index.php?title=Extra_python_modules#pyCollada) in this Wiki. Once the pyCollada Python module is installed, importing Collada files is the same as any standard file import.

See also: [Importing From Sketchup](Importing_From_Sketchup.md)

### Common Airfoil Data {#common_airfoil_data}

Please refer to the Page [Common Airfoil Data Import](Common_Airfoil_Data_Import.md)

### Drawing

Todo

### FEM Formats {#fem_formats}

Todo

### FreeCAD Material Cards {#freecad_material_cards}

Is intended to import Material Cards for use in FreeCAD itself and in the [FEM-Workbench](FEM_Workbench.md).

**Not functional at the moment.**

### IDF emn file {#idf_emn_file}

Todo

### IGES

Currently there is no support for text or annotation import with the IGES format due to lack of support with FreeCAD\'s geometric CAD kernel.

### Image Formats {#image_formats}

Todo

### Industry Foundation Classes IFC {#industry_foundation_classes_ifc}

-   [Export IFC - compiling IfcOpenShell](Export_IFC_-_compiling_IfcOpenShell.md)

### Inventor V2.1 {#inventor_v2.1}

Todo

### Mesh Formats {#mesh_formats}

Please refer to the Page [FreeCAD and Mesh Import](FreeCAD_and_Mesh_Import.md)

### Open CAD Format {#open_cad_format}

Todo

### OpenSCAD CSG Format {#openscad_csg_format}

Todo

### OpenSCAD Format {#openscad_format}

See [Import OpenSCAD code](Import_OpenSCAD_code.md)

### Point Formats {#point_formats}

Todo

### POVRay Format {#povray_format}

Todo

### Python

Todo

### Step with Colors {#step_with_colors}

Currently there is no support for text or annotation import with the STEP format due to lack of support with FreeCAD\'s geometric CAD kernel.

### Shapefiles

See [Arch SHP](Arch_SHP.md)

### Spreadsheet

Todo

### SVG as geometry {#svg_as_geometry}

Todo

### VRML 2.0 {#vrml_2.0}

Todo

## Export 2D/3D Data {#export_2d3d_data}

### 3D View (SVG) {#d_view_svg}

Todo

### Autodesk DWG {#autodesk_dwg_1}

Todo

### Asymptote ASY {#asymptote_asy}

[Export meshes to Asymptote code.](Asymptote.md)

### BREP Format {#brep_format_1}

Todo

### Collada {#collada_1}

Todo

### Drawing {#drawing_1}

Todo

### FEM Formats {#fem_formats_1}

Todo

### Flattened SVG {#flattened_svg}

Todo

### GL Transmission Format gITF {#gl_transmission_format_gitf}

-   [glTF](glTF.md)

### IGES Format {#iges_format}

-   From the 3D-View simply select (in the tree-view) the solid(s) to export and select \"File -\> Export\".
-   Then select your file type (IGES). No need to type in the file extension. FreeCAD will append a \".iges\" automatically

**Tip**
Pressing CTRL-A will select ALL solids in the tree view, even the invisible ones.
Make sure to manually select all the solids you want to export.
Currently there is no support for text or annotation export with the IGES format due to lack of support with FreeCAD\'s geometric CAD kernel.

### Industry Foundation Classes IFC {#industry_foundation_classes_ifc_1}

-   [Import/Export IFC - compiling IfcOpenShell](Import/Export_IFC_-_compiling_IfcOpenShell.md)

### Inventor V2.1 {#inventor_v2.1_1}

Todo

### Mesh Formats {#mesh_formats_1}

-   From the 3D-View simply select (in the tree-view) the solid(s) to export and select \"File -\> Export\".
-   Then select your file type. Be sure to type in also the file extension. Since these formats are mesh formats, the solids will be exported with a \"standard\" mesh quality.
-   Use the [Mesh Workbench](Mesh_Workbench.md) to adjust the quality of the mesh if needed.

**Tip**
Pressing CTRL-A will select ALL solids in the tree view, even the invisible ones.
Make sure to manually select all the solids you want to export.

### Open CAD Format {#open_cad_format_1}

Todo

### OpenSCAD CSG Format {#openscad_csg_format_1}

Todo

### OpenSCAD Format {#openscad_format_1}

Todo

### Portable Document Format {#portable_document_format}

Todo

### Step with Colors {#step_with_colors_1}

From the 3D-View simply select (in the tree-view) the solid(s) to export and select \"File -\> Export\".

In FreeCAD 0.15 and above, by selecting \"Edit -\> Preferences\" and then \"Import-Export\" in the left column you should have access to Step-Options such as units, scheme and Header Information. Be aware that Step AP203 does not support assembly structures, while Step AP 214 does.

Currently there is no support for text or annotation export with the STEP format due to lack of support with FreeCAD\'s geometric CAD kernel.

### Spreadsheet {#spreadsheet_1}

Todo

### TetGen File {#tetgen_file}

Todo

### VRML 2.0 {#vrml_2.0_1}

Todo

### Wavefront OBJ - Arch Workbench {#wavefront_obj___arch_workbench}

Todo

-   Convert STL to OBJ [forum thread](https://forum.freecadweb.org/viewtopic.php?f=22&t=43543&p=372030#p370843)

### WebGL File {#webgl_file}

Todo

## Export Data from third-party programs for import into FreeCAD {#export_data_from_third_party_programs_for_import_into_freecad}

Tips and Tricks with using Third-Party Software

### Inkscape

When exporting SVG-Data from Inkscape to FreeCAD be sure to use the file type \"plain svg\".

### Sketchup

Please refer to the Page [Importing From Sketchup](Importing_From_Sketchup.md)

## Related

-   [Import Export](Import_Export.md)
-   [Import Export Preferences](Import_Export_Preferences.md)









[Category:Common Questions](Category:Common_Questions.md)

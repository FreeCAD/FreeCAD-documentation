 

## Background

DXF is a proprietary CAD data format for 2D drawings that originated with AutoCAD. More details can be found on the [DXF](DXF.md) wiki page.

## Introduction

Since FreeCAD version 0.18 there is a new C++ DXF importer, and since version 0.19 also a new C++ DXF exporter. These new components are installed with FreeCAD.

To use the older, legacy, DXF importer and exporter you need to install several files. These files cannot be included with FreeCAD since they use libraries published under a license that is not compatible with FreeCAD.

## How to install the legacy DXF importer and exporter {#how_to_install_the_legacy_dxf_importer_and_exporter}

### Automatically

If the files are not already installed, go to the menu {{MenuCommand|Edit → Preferences → Import-Export → DXF}} and enable the option {{MenuCommand|Allow FreeCAD to automatically download and update the DXF libraries}} to make FreeCAD automatically download and install them.

For FreeCAD 0.14 or older you have to install manually:

### Manually

1.  Go to [Yorik\'s Github account](https://github.com/yorikvanhavre/Draft-dxf-importer) and download these files (on the right side you can choose \"download as ZIP\").
2.  Put the files in your macro folder.
3.  If you are unsure where this folder is, go to {{MenuCommand|Edit → Preferences → General → Macro}} and check the field named {{MenuCommand|Macro Path}}.

-   In Ubuntu your macro folder is normally (the folder is hidden, you may need to unhide it):

/home/your_user_name/.FreeCAD 

-   In Windows your macro folder is normally:

C:\Users\your_user_name\AppData\Roaming\FreeCAD

See also: [Dxf Importer Install](Dxf_Importer_Install.md)

## Import DXF file as sketch {#import_dxf_file_as_sketch}

There is no direct way to import a DXF file into a sketch, but it is possible via the [Draft Workbench](Draft_Workbench.md).

1.  Import DXF file (*Ctrl-I* or {{MenuCommand|File → Import.. → Select *.DXF}} )

    :   the file will be imported as a shape file. Splines may be missing and you may see control points joint by lines.
2.  If the import created mulipe shapes files select all that should become part of the sketch
3.  Select the [Draft Workbench](Draft_Workbench.md)
4.  <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> Press the [Draft to Sketch](Draft_Draft2Sketch.md) button

    :   an additional sketch icon appears in the tree. You can now delete the original imported object as it is not required any more
5.  done.

This sketch is still a bit different from other sketches. It has no dimensions, no constrains and will be quite unstable if you click and move any of the lines. Also the single line elements are likely not connected (coincident). For further use like extrusions some fixes are required:

-   add dimensions. Be careful with horizontal or vertical dimensions, as the original lines may have been be (slightly) rotated.
-   add constraints
-   make sure all joints are coincident. The tool {{MenuCommand|Sketcher → Validate sketch... }} may fix some for you. Extrusion will not work until all missin coincidences are resolved.
-   add missing splines (for B-Splines with control points you can convert the connecting lines of the imported sketch into blue work geometry. Then add the new spline by clicking the start point and then the original control points one after the other. Finish the new spline by clicking the end connection point to the geometry (white line). This should fully recover the original B-Spline)

In the preferences section [Inport Export](Import_Export_Preferences.md) (DXF Tab) are some settings that affect this use case. To get a decent sketch set

-   Create to: \"Sketches\" (this is a radio button).
-   Scale should be set to: 1.00
-   Join geometry: CHECK
-   Group layers into blocks: CHECK

Tip: This procedure can also be useful to convert parts from other CAD programs that can not be directly imported. If much of the design is in sketches, exporting the sketches to DXF and re-adding constraints and dimensions in FreeCAD can much quicker than re-creating the parts from scratch or using exported STEP files without modifiable creation history.

## Tips and Tricks {#tips_and_tricks}

Sometimes DXF Files don\'t import although they open in other CAD-Programs without problems.

You can try:

1.  Go to {{MenuCommand|Edit → Preferences → Import-Export → DXF}} and untick the option {{MenuCommand|Join geometry}} and try again.
2.  Remember that maybe now you won\'t have coincident endpoints. You will have to make them coincident yourself.
3.  You can do this with the [Sketcher CloseShape](Sketcher_CloseShape.md) command <small>(v0.15)</small>  or you can apply the constraints manually.

You can also try:

1.  Go to {{MenuCommand|Edit → Preferences → Draft → General settings}} and adjust the value of {{MenuCommand|Tolerance}} (default: 0,05) and try again.

For an overview of all DXF related preferences see [Import Export Preferences](Import_Export_Preferences#DXF.md).



[Category:User\_Documentation{{\#translation:}}](Category:User_Documentation.md) [Category:File\_Formats{{\#translation:}}](Category:File_Formats.md)

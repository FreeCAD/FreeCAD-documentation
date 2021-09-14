# Draft DXF/tr










{{TOCright}}

## Description

Draft DXF is a software module used by the <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Open](Std_Open.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Import](Std_Import.md) and <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Export](Std_Export.md) commands to handle the DXF file format.

![](images/Screenshot_qcad.jpg ) *Qcad drawing exported to DXF, which is subsequently opened in FreeCAD*

## Importing

The importer has two modes, settable under **Edit → Preferences → Import/Export → DXF**: One is built-in, C++-based and fast, the other is legacy, coded in Python, slower, and requires the installation of an add-on, but can sometimes handle some entities better and can create more refined FreeCAD objects. Both support all DXF versions starting from R12.

3D objects inside a DXF file are stored under a binary ACIS/SAT blob, which at the moment cannot be read by FreeCAD. Simpler entities like 3DFACEs, though, are supported.

The following DXF objects can be imported:

-   lines
-   polylines (and lwpolylines)
-   circles
-   arcs
-   splines
-   ellipses
-   layers
-   texts and mtexts
-   dimensions
-   blocks (only geometry. texts, dimensions and attributes inside blocks will be skipped)
-   points
-   leaders
-   paper space objects

## Exporting

Files are exported in the R14 DXF format which can be handled by many applications.

The following FreeCAD objects can be exported:

-   all of FreeCAD\'s 2D geometry such as Draft objects or sketches
-   3D objects are exported as a flattened 2D view
-   Compound objects are exported as blocks
-   texts
-   colors are mapped from objects RGB colors to autocad color index (ACI). Black will always be \"by layer\"
-   layers are mapped from group names. When groups are nested, the deepest group gives the layer name.
-   dimensions, which are exported with \"Standard\" dimstyle.

## Installing

For licensing reasons, the required [DXF](DXF.md) import/export libraries needed by the legacy version of the importer are not part of the FreeCAD source code. For more information see: [FreeCAD and DXF Import](FreeCAD_and_DXF_Import.md).

## Preferences

For more information see: [Import Export Preferences](Import_Export_Preferences.md).

## Scripting


**See also:**

[Draft API](Draft_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

You can export elements to DXF by using the following function: 
```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

Example: 
```python
import Draft, importDXF

Polygon1 = Draft.makePolygon(3, radius=500)
Polygon2 = Draft.makePolygon(5, radius=1500)

objects = [Polygon1, Polygon2]

importDXF.export(objects, "/home/user/Pictures/myfile.dxf")
```





 

[Category:File Formats](Category:File_Formats.md)

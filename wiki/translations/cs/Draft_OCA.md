
{{Page in progress}}







{{TOCright}}

## Description

Draft OCA is a software module used by the <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Open](Std_Open.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Import](Std_Import.md) and <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Export](Std_Export.md) commands to handle the [OCA file format](http://groups.google.com/group/open_cad_format).

The OCA file format is community effort to create a free, simple and open CAD file format. OCA is largely based on the GCAD file format generated from [gCAD3D](http://www.gcad3d.org/). Both formats can be imported in FreeCAD, and the OCA files exported by FreeCAD can be opened in gCAD3D.

## Importing

The following OCA objects can be imported:

-   Lines
-   Arcs and Circles
-   Closed areas

## Exporting

The following FreeCAD objects can be exported:

-   Lines and wires (polylines)
-   Arcs and circles
-   Faces

## Preferences

For more information see: [Import Export Preferences](Import_Export_Preferences.md).

## Scripting


**See also:**

[Draft API](Draft_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

You can export elements to OCA by using the following function: 
```python
importOCA.export(exportList, filename)
```

Example: 
```python
import FreeCAD, Draft, importOCA

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(1000, 1000, 0)
p3 = FreeCAD.Vector(2200, 1500, 0)
p4 = FreeCAD.Vector(2500, -100, 0)

obj1 = Draft.makeWire([p1, p2, p3, p4])
obj2 = Draft.makeWire([p1, -2.3*p2, -0.8*p3, -1.8*p4])

objects = [obj1, obj2]

importOCA.export(objects, "/home/user/Pictures/myfile.oca")
```


<div class="mw-translate-fuzzy">


</div>


 

[Category:User Documentation/cs](Category:User_Documentation/cs.md) [Category:File Formats{{\#translation:}}](Category:File_Formats.md)

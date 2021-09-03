








{{TOCright}}

## Description

Draft SVG is a software module used by the <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Open](Std_Open.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Import](Std_Import.md) and <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Export](Std_Export.md) commands to handle the [SVG](SVG.md) file format.

![](images/Screenshot_inkscape.jpg ) *Inkscape drawing exported to SVG, which is subsequently opened in FreeCAD*

## Importing

The following SVG objects can be imported:

-   PATH objects
-   LINE objects
-   RECT objects
-   CIRCLE objects
-   ELLIPSE objects
-   POLYGON objects
-   POLYLINE objects

### Limitations

FreeCAD will not import path objects that have only one point ([forum discussion](https://forum.freecadweb.org/viewtopic.php?f=3&t=43856)).

## Exporting

The following FreeCAD objects can be exported:

-   Lines and wires (polylines)
-   Arcs and circles
-   Faces
-   Texts
-   Dimensions

### Limitations 

SVG is a 2D format, so all Z information will be disregarded (all objects will be flattened).

## Unit Handling 

When exporting, a User Unit (px) equals one millimeter.

When importing, the width, height and viewBox attributes are respected. All elements are scaled to their size in millimeter, which is FreeCAD internal unit. If the SVG does not contain information on its physical size, it is assumed to have 90 DPI resolution. Using absoulte units in attributes inside the SVG should be avoided. Relative units like em,ex and % are currently not supported.

The [Inkscape](https://inkscape.org/) SVG Editor currently works only with **90 DPI** documents. No matter which unit is selected in Inkscape. All the output has to be considered converted to 90 DPI and **rounded** to 6 decimal places. As FreeCAD (and the SVG standard) is agnostic to the precision of rounding done in Inkscape these values will not be rounded on input. And odd values in millimeter will remain. If you need the SVG import not to be rounded, work on User Units (px) in Inkscape. Scaling can be done after the import to FreeCAD or by changing the width, height and viewbox attributes.

## Preferences

For more information see: [Import Export Preferences](Import_Export_Preferences.md).

## Scripting


**See also:**

[Draft API](Draft_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

You can export elements to SVG by using the following function: 
```python
importSVG.export(exportList, filename)
```

Example: 
```python
import Draft, importSVG

Polygon1 = Draft.makePolygon(3, radius=500)
Polygon2 = Draft.makePolygon(5, radius=1500)

objects = [Polygon1, Polygon2]

importSVG.export(objects, "/home/user/Pictures/myfile.svg")
```


<div class="mw-translate-fuzzy">


</div>


 

[Category:User Documentation/ru](Category:User_Documentation/ru.md) [Category:File Formats{{\#translation:}}](Category:File_Formats.md)

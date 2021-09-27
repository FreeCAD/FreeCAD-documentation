# Draft DXF/es
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Descripción

El borrador DXF es un módulo de software utilizado por el <img alt="" src=images/Std_Open.svg  style="width:24px;"> _ y <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Exportar](Std_Export/es.md) para manejar el formato de archivo DXF.

![](images/Screenshot_qcad.jpg ) *Dibujo Qcad exportado a DXF, que posteriormente se abre en FreeCAD*

## Importación

Two importers are available, which one is used can be specified under **Edit → Preferences... → Import-Export → DXF**. One is built-in, C++-based and fast, the other is legacy, coded in Python, slower, and requires the installation of an add-on, but can handle some entities better and can create more refined FreeCAD objects. Both support all DXF versions starting from R12.


<div class="mw-translate-fuzzy">

Los objetos 3D dentro de un archivo DXF se almacenan bajo un blob binario ACIS/SAT, que por el momento no puede ser leído por FreeCAD. Sin embargo, entidades más sencillas como los 3DFACEs son soportados.


</div>

### C++ importer 

This importer can import the following DXF objects:

-   lines
-   polylines (and lwpolylines)
-   arcs
-   circles
-   ellipses
-   splines
-   points
-   texts and mtexts
-   dimensions
-   leaders
-   blocks (only geometry, texts, dimensions and attributes inside blocks are skipped)
-   layers
-   paper space objects

### Legacy importer 

This importer can import the following DXF objects:

-   lines
-   polylines (and lwpolylines)
-   arcs
-   circles
-   ellipses
-   splines
-   3D faces
-   texts and mtexts
-   leaders
-   layers

## Exportación


<div class="mw-translate-fuzzy">

Los archivos se exportan en el formato DXF R14, que puede ser manejado por muchas aplicaciones.


</div>

### C++ exporter 

Some of the features and limitations of this exporter are:

-   All FreeCAD 2D geometry is exported, except [Draft CubicBezCurves](Draft_CubicBezCurve.md), [Draft BezCurves](Draft_BezCurve.md) and [Draft Points](Draft_Point.md).
-   Straight edges from faces of 3D objects are exported, but curved edges only if they are on a plane parallel to the XY plane of the global coordinate system. Note that a DXF created from 3D objects will contain duplicate lines.
-   Texts and dimensions are not exported.
-   Colors are ignored.
-   Layers are mapped from object names.

### Legacy exporter 

Some of the features and limitations of this exporter are:

-   All FreeCAD 2D geometry is exported, except [Draft Points](Draft_Point.md). But ellipses, B-splines and Bézier curves are not exported properly.
-   3D objects are exported as flattened 2D views.
-   Compound objects are exported as blocks.
-   Texts and dimensions are exported.
-   The colors in the DXF are based on the line color of objects. Black is mapped to \"ByBlock\", other colors are mapped using AutoCAD Color Index (ACI) colors.
-   Layers are mapped from layer and group names. When groups are nested, the deepest group gives the layer name.

## Instalación

Por razones de licencia, las librerías de importación/exportación _.

## Preferencias


<div class="mw-translate-fuzzy">

Para más información, consulte: [Preferencias de exportación](Import_Export_Preferences/es.md).


</div>

## Scripting

See also: _.

To export objects to DXF use the `export` method of the importDXF module.


```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

-   For the Windows OS: use a {{FileName|/}} (forward slash) as the path separator in {{Incode|filename}}.

Ejemplo:


```python
import FreeCAD as App
import Draft
import importDXF

doc = App.newDocument()

polygon1 = Draft.make_polygon(3, radius=500)
polygon2 = Draft.make_polygon(5, radius=1500)

doc.recompute()

objects = [polygon1, polygon2]
importDXF.export(objects, "/home/user/Pictures/myfile.dxf")
```


<div class="mw-translate-fuzzy">





</div>


 

_

---
[documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Draft](Draft_Workbench.md) > Draft DXF/es

# Draft DXF/es







<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Descripción

El borrador DXF es un módulo de software utilizado por el <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Abrir](Std_Open/es.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Importar](Std_Import/es.md) y <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Exportar](Std_Export/es.md) para manejar el formato de archivo DXF.

![](images/Screenshot_qcad.jpg ) *Dibujo Qcad exportado a DXF, que posteriormente se abre en FreeCAD*

## Importación

The importer has two modes, settable under **Edit → Preferences → Import/Export → DXF**: One is built-in, C++-based and fast, the other is legacy, coded in Python, slower, and requires the installation of an add-on, but can sometimes handle some entities better and can create more refined FreeCAD objects. Both support all DXF versions starting from R12.

Los objetos 3D dentro de un archivo DXF se almacenan bajo un blob binario ACIS/SAT, que por el momento no puede ser leído por FreeCAD. Sin embargo, entidades más sencillas como los 3DFACEs son soportados.

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

## Exportación

Los archivos se exportan en el formato DXF R14, que puede ser manejado por muchas aplicaciones.

The following FreeCAD objects can be exported:

-   all of FreeCAD\'s 2D geometry such as Draft objects or sketches
-   3D objects are exported as a flattened 2D view
-   Compound objects are exported as blocks
-   texts
-   colors are mapped from objects RGB colors to autocad color index (ACI). Black will always be \"by layer\"
-   layers are mapped from group names. When groups are nested, the deepest group gives the layer name.
-   dimensions, which are exported with \"Standard\" dimstyle.

## Instalación

Por razones de licencia, las librerías de importación/exportación [DXF](DXF/es.md) necesarias para la versión antigua del importador no forman parte del código fuente de FreeCAD. Para más información ver: [Importación FreeCAD y DXF](FreeCAD_and_DXF_Import/es.md).

## Preferencias

Para más información, consulte: [Preferencias de exportación](Import_Export_Preferences/es.md).

## Scripting


**See also:**

[Draft API](Draft_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

You can export elements to DXF by using the following function: 
```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

Ejemplo: 
```python
import Draft, importDXF

Polygon1 = Draft.makePolygon(3, radius=500)
Polygon2 = Draft.makePolygon(5, radius=1500)

objects = [Polygon1, Polygon2]

importDXF.export(objects, "/home/user/Pictures/myfile.dxf")
```


<div class="mw-translate-fuzzy">





</div>


 

[Category:File Formats](Category:File_Formats.md)

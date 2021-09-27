# Draft DXF/sv
{{TOCright}}

## Description

Draft DXF is a software module used by the <img alt="" src=images/Std_Open.svg  style="width:24px;"> _ and <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Export](Std_Export.md) commands to handle the DXF file format.

![](images/Screenshot_qcad.jpg ) *Qcad drawing exported to DXF, which is subsequently opened in FreeCAD*


<div class="mw-translate-fuzzy">

### Öppna

Denna funktion öppnar en DXF fil (alla versioner från 12 till 2007) i en ny ritning. Följande DXF objekttyper stöds för närvarande:

-   lines
-   polylines och lwpolylines
-   circles
-   arcs
-   layers (layers som innehåller objekt konverteras till FreeCAD Grupper)
-   texts och mtexts
-   dimensions
-   blocks (endast geometri. texter, dimensioner och attribut inuti block behandlas inte)

Andra DXF föremål importeras för närvarande inte eftersom det inte finns något motsvarande FreeCAD objekt. Allteftersom ny funktionalitet utvecklas, så kommer det att vara möjligt att importera fler föremålstyper.


</div>

Two importers are available, which one is used can be specified under **Edit → Preferences... → Import-Export → DXF**. One is built-in, C++-based and fast, the other is legacy, coded in Python, slower, and requires the installation of an add-on, but can handle some entities better and can create more refined FreeCAD objects. Both support all DXF versions starting from R12.

3D solids inside a DXF file are stored under a binary ACIS/SAT blob, which at the moment cannot be read by FreeCAD.

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


<div class="mw-translate-fuzzy">

### Exportera

Den exporterade DXF filen är kompatibel med Autocad version 12 och upp, så den ska kunna öppnas i så gott som alla applikationer som stöder dxf formatet. För närvarande så exporteras följande FreeCAD objekt:

-   linje och trådar (polylines)
-   cirkelbågar och cirklar
-   texter
-   Färger konverteras från objektens RGB färger till autocad color index (ACI). Svart komme alltid att vara \"by layer\"
-   lager konverteras från gruppnamn. När grupper är nästlade, så kommer lagret att får namnet på den djupaste gruppen.
-   dimensioner, vilka exporteras med \"Standard\" dimensioneringsstil


</div>

There are also two exporters. The legacy exporter exports to the R12 DXF format, the C++ exporter to the R14 DXF format. Both formats can be handled by many applications.

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

## Installing

For licensing reasons, the required _.

## Preferences


<div class="mw-translate-fuzzy">

### Alternativ

Följande parametrar kan specificeras i [Skissalternativ](Draft_Preferences/sv.md) tabben (meny Redigera -\> Alternativ -\> Draft):

-   Import stil: Detta låter dig välja på vilket sätt som objekt från dxf filen kommer att ritas i FreeCAD. Du kan välja mellan:
    -   None: detta är den snabbare sättet, ingen konvertering sker, alla objekt kommer att vara svarta med 2 pixels bredd (FreeCAD standard)
    -   Use default color and linewidth: Alla importerade dxf objekt kommer at anta nuvarande linjebredd/färg från Skisskommandolådan
    -   Original color and linewidth: Objekten kommer att behålla den färg och linjebredd (om det är specificerat) de har i dxf filen
    -   Colors mapped to linewidth: Om detta alternativ väljs så används kartfilen nedan.
-   Color mapping file: Denna tillåter dig att specificera en kartfil som ska användas för översättning av dxf färger till färg och linjebredd, på samma sätt som en plottningsstil fungerar i Autocad. Kartfilen måste vara en tabb-separerad textfil. Det finns ett bra fritt program som heter _ tillgängliga här.
-   Import texts: Detta tillåter dig att specificera om du vill importera dxf text och dimensioner eller inte. Många texter kan göra ditt arbete i FreeCAD mycket tungrott, så du kanske vill använda detta alternativ ibland.
-   Import layout objects: Sätt på detta om du vill importera paper space objekt. De kommer att infogas i samma dokument som model space objekt.


</div>

## Scripting

See also: _.

To export objects to DXF use the `export` method of the importDXF module.


```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

-   For the Windows OS: use a {{FileName|/}} (forward slash) as the path separator in {{Incode|filename}}.

Example:


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


 

_ _

---
[documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Draft](Draft_Workbench.md) > Draft DXF/sv

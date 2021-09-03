
{{Page in progress}}







{{TOCright}}

## Description

Draft DXF is a software module used by the <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Open](Std_Open.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Import](Std_Import.md) and <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Export](Std_Export.md) commands to handle the DXF file format.

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

The importer has two modes, settable under {{MenuCommand|Edit → Preferences → Import/Export → DXF}}: One is built-in, C++-based and fast, the other is legacy, coded in Python, slower, and requires the installation of an add-on, but can sometimes handle some entities better and can create more refined FreeCAD objects. Both support all DXF versions starting from R12.

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


<div class="mw-translate-fuzzy">

### Alternativ

Följande parametrar kan specificeras i [Skissalternativ](Draft_Preferences/sv.md) tabben (meny Redigera -\> Alternativ -\> Draft):

-   Import stil: Detta låter dig välja på vilket sätt som objekt från dxf filen kommer att ritas i FreeCAD. Du kan välja mellan:
    -   None: detta är den snabbare sättet, ingen konvertering sker, alla objekt kommer att vara svarta med 2 pixels bredd (FreeCAD standard)
    -   Use default color and linewidth: Alla importerade dxf objekt kommer at anta nuvarande linjebredd/färg från Skisskommandolådan
    -   Original color and linewidth: Objekten kommer att behålla den färg och linjebredd (om det är specificerat) de har i dxf filen
    -   Colors mapped to linewidth: Om detta alternativ väljs så används kartfilen nedan.
-   Color mapping file: Denna tillåter dig att specificera en kartfil som ska användas för översättning av dxf färger till färg och linjebredd, på samma sätt som en plottningsstil fungerar i Autocad. Kartfilen måste vara en tabb-separerad textfil. Det finns ett bra fritt program som heter [Plot style viewer](http://www.noliturbare.com/TablePrintGUI.php) som kan konvertera Autocad CTB eller STB (plottstilar) filer till tabb-separerade kartfiler, klara att användas i FreeCAD. Alternativt, så har vi några [hemgjorda kartfiler](Draft_mapping_files/sv.md) tillgängliga här.
-   Import texts: Detta tillåter dig att specificera om du vill importera dxf text och dimensioner eller inte. Många texter kan göra ditt arbete i FreeCAD mycket tungrott, så du kanske vill använda detta alternativ ibland.
-   Import layout objects: Sätt på detta om du vill importera paper space objekt. De kommer att infogas i samma dokument som model space objekt.


</div>

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


<div class="mw-translate-fuzzy">


</div>


 

[Category:User Documentation/sv](Category:User_Documentation/sv.md) [Category:File Formats{{\#translation:}}](Category:File_Formats.md)

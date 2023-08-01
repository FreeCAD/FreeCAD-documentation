# Draft DXF/ro
{{TOCright}}

## Description

Draft DXF is a software module used by the <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Open](Std_Open.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Import](Std_Import.md) and <img alt="" src=images/Std_Export.svg  style="width:24px;"> [Std Export](Std_Export.md) commands to handle the DXF file format.

![](images/Screenshot_qcad.jpg ) 
*Qcad drawing exported to DXF, which is subsequently opened in FreeCAD*


<div class="mw-translate-fuzzy">

### Deschiderea

Această funcție deschide un fișier DXF (orice versiune de la 12 la 2007) într-un nou desen. Următoarele tipuri de obiecte DXF sunt suportate în mod curent:

-   lines
-   polylines and lwpolylines
-   circles
-   arcs
-   layers (layers containing objects are conveted to FreeCAD Groups)
-   texts and mtexts
-   dimensions
-   blocks (only geometry. texts, dims and attributes inside blocks will be skipped)
-   points <small>(v0.13)</small> 
-   leaders <small>(v0.13)</small> 

Alte entități DXF nu sunt importate în prezent deoarece nu există un obiect FreeCAD corespunzător. Odată cu implementarea noii funcționalități, va fi posibil să importați mai multe tipuri de entități.


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

### Export

DXF-ul exportat este compatibil cu versiunea Autocad 12 sau mai recentă, deci ar trebui să se deschidă în orice aplicație care suportă formatul dxf. În prezent, se exportă următoarele obiecte FreeCAD:

-   linii și fire (polilinii)
-   arce și cercuri
-   texte
-   culorile sunt cartografiate de la obiectele RGB culori la indexul de culoare autocad (ACI). Negrul va fi întotdeauna \"după strat\"
-   straturile sunt mapate din numele grupului. Când grupurile sunt imbricate, cel mai adânc grup dă numele stratului.
-   dimensiuni, care sunt exportate cu dimensiune \"Standard\"


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


<div class="mw-translate-fuzzy">

## Instalarea


</div>


<div class="mw-translate-fuzzy">

**Warning**: Din motive de licență, bibliotecile de import / export dxf nu mai fac parte din codul sursă al FreeCAD. Din acest motiv, ele trebuie să fie instalate de dvs., utilizatorul, după ce ați instalat FreeCAD. Există o modalitate de a permite FreeCAD să facă acest lucru în mod automat sau puteți să o faceți manual.


</div>

## Preferences

See [Import Export Preferences](Import_Export_Preferences.md).

## DWG

Because the DWG format is a proprietary, closed and undocumented format it is hard for open-source projects like FreeCAD to support it. That is why FreeCAD relies on external converters to read and write DWG files. To import a DWG file a converter is used to create a DXF first, which can then be processed by the FreeCAD DXF importer. When exporting to DWG the opposite conversion happens: the DXF created by the FreeCAD DXF exporter is turned into a DWG.

Note that the DXF format allows a 1:1 conversion of the DWG format. All applications that can read and write DWG files can do the same with DXF files, with no data loss. So asking for DXF files instead of DWG files, and supplying DXF files in turn, should not cause any problems.

There is built-in support for the following DWG converters:

-   [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, lacks support for some DWG entities).
-   [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (free).
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (commercial). <small>(v0.20)</small> 

See [Import Export Preferences](Import_Export_Preferences#DWG.md) and [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md) for more information.

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To export objects to DXF use the `export` method of the importDXF module.


```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

-   For the Windows OS: use a **/** (forward slash) as the path separator in {{Incode|filename}}.

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



---
![](images/Button_right.svg) [documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Draft](Draft_Workbench.md) > Draft DXF/ro

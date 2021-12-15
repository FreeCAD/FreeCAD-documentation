# Draft DXF/de
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Beschreibung

DXF Entwurf ist ein Softwaremodul, das von den <img alt="" src=images/Std_Open.svg  style="width:24px;"> _ und <img alt="" src=images/Std_Export.svg  style="width:24px;">[Std Export](Std_Export/de.md) Befehlen verwendet wird, um das DXF Dateiformat handzuhaben.

![](images/Screenshot_qcad.jpg ) 
*Qcad-Zeichnung nach DXF exportiert, die anschließend in FreeCAD geöffnet wird*

## Importieren


<div class="mw-translate-fuzzy">

Der Importeur hat zwei Modi, einstellbar unter **Bearbeiten → Einstellungen → Import/Export → DXF**: Der eine ist eingebaut, C++ basiert und schnell, der andere ist eine Altlast, in Python kodiert, langsamer und erfordert die Installation einer Erweiterung, kann aber manche Objekte besser handhaben und kann verfeinerte FreeCAD Objekte erzeugen. Beide unterstützen alle DXF Versionen beginnend ab R12.


</div>


<div class="mw-translate-fuzzy">

3D Objekte innerhalb einer DXF Datei werden unter einem binären ACIS/SAT Klecks gespeichert, der zur Zeit von FreeCAD nicht gelesen werden kann. Einfachere Objekte wie 3DFACEs werden jedoch unterstützt.


</div>

### C++ importer 


<div class="mw-translate-fuzzy">

Die folgenden DXF Objekte können importiert werden:

-   Linien
-   Polylinien und Lwpolylinien
-   Kreise
-   Bögen
-   Lagen
-   Texte und Mtexte
-   Bemaßungen
-   Blöcke (nur Geometrie, Texte, Bemaßungen und Attribute innerhalb von Blöcken werden übersprungen)
-   Punkte
-   Führungen
-   Papierraumobjekte


</div>

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

## Exportieren


<div class="mw-translate-fuzzy">

Dateien werden im R14 DXF Format exportiert, das von vielen Anwendungen verarbeitet werden kann.


</div>

### C++ exporter 

Some of the features and limitations of this exporter are:

-   All FreeCAD 2D geometry is exported, except [Draft CubicBezCurves](Draft_CubicBezCurve.md), [Draft BezCurves](Draft_BezCurve.md) and [Draft Points](Draft_Point.md).
-   Straight edges from faces of 3D objects are exported, but curved edges only if they are on a plane parallel to the XY plane of the global coordinate system. Note that a DXF created from 3D objects will contain duplicate lines.
-   Texts and dimensions are not exported.
-   Colors are ignored.
-   Layers are mapped from object names.

### Legacy exporter 


<div class="mw-translate-fuzzy">

Die folgenden FreeCAD Objekte können exportiert werden:

-   die gesamte 2D Geometrie von FreeCAD, wie z. B. Entwurfsobjekte oder Skizzen
-   3D Objekte werden als verflachte 2D Ansicht exportiert
-   Zusammengesetzte Objekte werden als Blöcke exportiert
-   Texte
-   Farben werden von den RGB Farben der Objekte auf den Autocad Farbindex (ACI) abgebildet. Schwarz wird immer \"nach Lagen\" sein
-   Lagen werden von Gruppennamen abgebildet. Wenn Gruppen verschachtelt sind, gibt die tiefste Gruppe den Lagennamen an.
-   Bemaßungen, die mit dem Dimstyle \"Standard\" exportiert werden.


</div>

## Installieren

Aus lizenzrechtlichen Gründen sind die benötigten _.

## Einstellungen


<div class="mw-translate-fuzzy">

Für weitere Informationen siehe: [Import Export Einstellungen](Import_Export_Preferences/de.md).


</div>

## DWG

Because the DWG format is a proprietary, closed and undocumented format it is hard for open-source projects like FreeCAD to support it. That is why FreeCAD relies on external converters to read and write DWG files. To import a DWG file a converter is used to create a DXF first, which can then be processed by the FreeCAD DXF importer. When exporting to DWG the opposite conversion happens: the DXF created by the FreeCAD DXF exporter is turned into a DWG.

Note that the DXF format allows a 1:1 conversion of the DWG format. All applications that can read and write DWG files can do the same with DXF files, with no data loss. So asking for DXF files instead of DWG files, and supplying DXF files in turn, should not cause any problems.

There is built-in support for the following DWG converters:

-   [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, lacks support for some DWG entities).
-   [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (free).
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (commercial). <small>(v0.20)</small> 

See [Import Export Preferences](Import_Export_Preferences#DWG.md) and [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md) for more information.

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Draft API](Draft_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Elemente können durch die folgende Funktion nach DXF exportiert werden:


</div>


```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

-   For the Windows OS: use a {{FileName|/}} (forward slash) as the path separator in {{Incode|filename}}.

Beispiel:


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
[documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Draft](Draft_Workbench.md) > Draft DXF/de

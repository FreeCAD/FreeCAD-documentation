# Draft DXF/de
## Beschreibung

Draft DXF ist ein Softwaremodul, das von den <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Std Öffnen](Std_Open/de.md), <img alt="" src=images/Std_Import.svg  style="width:24px;"> [Std Import](Std_Import/de.md) und <img alt="" src=images/Std_Export.svg  style="width:24px;">[Std Export](Std_Export/de.md) Befehlen verwendet wird, um das DXF-Dateiformat zu verarbeiten.

![](images/Screenshot_qcad.jpg ) 
*Qcad-Zeichnung nach DXF exportiert, die anschließend in FreeCAD geöffnet wird*



## Importieren

Es stehen zwei Import-Module zur Verfügung, die unter **Bearbeiten → Einstellungen... → Import-Export → DXF** festgelegt werden können: Der eine ist eingebaut, C++ basiert und schnell, der andere ist eine Altlast, in Python kodiert, langsamer und erfordert die Installation einer Erweiterung, kann aber manche Objekte besser verarbeiten und kann feinere FreeCAD-Objekte erstellen. Beide unterstützen alle DXF-Versionen seit R12.

3D-Festkörper innerhalb einer DXF-Datei werden unter einem binären \"ACIS/SAT-Blob\" gespeichert, der zur Zeit von FreeCAD nicht gelesen werden kann.



### C++ Import-Modul 

Dieses Importmodul kann folgende DXF-Objekte importieren:

-   Linien
-   Polylinien und Lwpolylinien
-   Bögen
-   Kreise
-   Splines
-   Punkte
-   Texte und Mtexte
-   Maße
-   Hinweislinien
-   Blöcke (nur Geometrie; Texte, Maße und Attribute innerhalb von Blöcken werden übersprungen)
-   Layer
-   \"paper space objects\"

### Legacy importer 

Dieses Importmodul kann folgende DXF-Objekte importieren:

-   Linien
-   Polylinien und Lwpolylinien
-   Bögen
-   Kreise
-   Ellipsen
-   Splines
-   3D-Flächen
-   Texte und Mtexte
-   Hinweislinien
-   Layer



## Exportieren

Es gibt auch zwei Export-Module: Das Altdaten-Export-Modul exportiert in das DXF-Format R12, Das C++ Export-Modul in das DXF-Format R14. Beide Formate können mit vielen Programmen verarbeitet werden.



### C++ Export-Modul 

Some of the features and limitations of this exporter are:

-   All FreeCAD 2D geometry is exported, except [Draft CubicBezCurves](Draft_CubicBezCurve.md), [Draft BezCurves](Draft_BezCurve.md) and [Draft Points](Draft_Point.md).
-   Straight edges from faces of 3D objects are exported, but curved edges only if they are on a plane parallel to the XY plane of the global coordinate system. Note that a DXF created from 3D objects will contain duplicate lines.
-   Texts and dimensions are not exported.
-   Colors are ignored.
-   Layers are mapped from object names.

### Legacy exporter 

Einige Merkmale und Eischränkungen dieses Exportmoduls sind:

-   Die gesamte 2D-Geometrie von FreeCAD wird exportiert außer [Draft-Punkten](Draft_Point/de.md). Aber Ellipsen, B-Splines und Bézierkurve werden nicht ordentlich exportiert.
-   3D-Objekte werden als objects are exported as eingeebnete 2D-Ansicht exportiert.
-   Verbundobjekte werden als Blöcke exportiert.
-   Texte und Maße werden exportiert.
-   Die Farben im DXF-Dokument basieren auf der Linienfarbe der Objekte. Schwarz wird als \"ByBlock\" zugeordnet, andere Farben verwenden den AutoCAD-Color-Index (ACI) zum Zuordnen.
-   Layer werden nach Layer- und Gruppennamen zugeordnet. Wenn Gruppen verschachtelt sind, gibt die tiefste Gruppe den Layernamen an.



## Installieren

Aus lizenzrechtlichen Gründen sind die benötigten [DXF](DXF/de.md) Import/Export Bibliotheken, die von der Legacy Version des Importeurs benötigt werden, nicht Teil des FreeCAD Quellcodes. Für weitere Informationen siehe: [FreeCAD und DXF Import](FreeCAD_and_DXF_Import/de.md).



## Einstellungen

Siehe [Import-Export-Einstellungen](Import_Export_Preferences/de.md).

## DWG

Because the DWG format is a proprietary, closed and undocumented format it is hard for open-source projects like FreeCAD to support it. That is why FreeCAD relies on external converters to read and write DWG files. To import a DWG file a converter is used to create a DXF first, which can then be processed by the FreeCAD DXF importer. When exporting to DWG the opposite conversion happens: the DXF created by the FreeCAD DXF exporter is turned into a DWG.

Note that the DXF format allows a 1:1 conversion of the DWG format. All applications that can read and write DWG files can do the same with DXF files, with no data loss. So asking for DXF files instead of DWG files, and supplying DXF files in turn, should not cause any problems.

There is built-in support for the following DWG converters:

-   [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, lacks support for some DWG entities).
-   [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (free).
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (commercial).

See [Import Export Preferences](Import_Export_Preferences#DWG.md) and [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md) for more information.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Um Objekte in eine DXF-Datei zu exportieren, wird die Methode `export` des Moduls importDXF verwendet.


```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

-   Für Windows: **/** (forward slash) wird als Pfad-Trennzeichen in {{Incode|filename}} verwendet.

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



---
⏵ [documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Draft](Draft_Workbench.md) > Draft DXF/de

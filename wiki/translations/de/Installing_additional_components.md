# Installing additional components/de
{{TOCright}}

# Einführung

Nach dem installieren von FreeCAD für dein Betriebssystem ([Windows](Installing_on_Windows/de.md), [Linux](Installing_on_Linux/de.md) oder [Mac](Installing_on_Mac/de.md)), solltest du die Installation einer oder mehrerer der folgenden zusätzlichen Komponenten in Betracht ziehen.

# Hilfedateien

Die Offline Dokumentation wird nicht mit allen Installationsprogrammen ausgeliefert, sie ist jedoch als separates Paket verfügbar. Weitere Informationen findest du auf der Seite [Installieren von Hilfedateien](Installing_Helpfile/de.md).

# Externe Arbeitsbereiche 

Abgesehen von den Standard [Arbeitsbereichen](workbenches/de.md), die mit FreeCAD gebündelt sind, gibt es eine große Sammlung nützlicher [externer Arbeitsbereiche](External_workbenches/de.md), erstellt von Gemeinschaftsmitgliedern.

# Drittanbieter Software 

FreeCAD unterstützt von Haus aus einige Softwarepakete von Drittanbietern. In vielen Fällen brauchst du die Software nur zu installieren, und wenn FreeCAD neu gestartet wird, findet es sie automatisch und kann sie verwenden. Dieser Abschnitt soll eine Liste solcher Softwarepakete bereitstellen, zusammen mit einigen Informationen darüber, wo sie in FreeCAD verwendet werden und wo sie heruntergeladen werden können.

## Unterstützung

### GitPython

_ kann diese Bibliothek verwenden. GitPython ist in den FreeCAD Installationsprogrammen für Windows und Mac enthalten.

### GraphViz

_ verwendet.

### OpenCAMLib

_ verwendet. Siehe die [OpenCamLib](OpenCamLib/de.md) Seite zu Installationsanweisungen.

### OpenSCAD

_ ist von dieser Software abhängig und der [ Arbeitsbereich Polygonnetze](Mesh_Workbench/de.md) verwendet sie für ihre booleschen Werkzeuge. Es wird auch für den Import von SCAD Dateien mit dem [Std Import](Std_Import/de.md) Werkzeug benötigt.

## Dateiformate

Die gesamte Software in diesem Abschnitt wird von den [Std Import](Std_Import/de.md) oder [Std Export](Std_Export/de.md) Werkzeugen verwendet.

### CADAustauscher

[CADExchanger](https://cadexchanger.com) ist eine kommerzielle Anwendung zum Austausch von verschiedenen CAD Dateiformaten. Es gibt einen [externen Arbeitsbereich](https://github.com/yorikvanhavre/CADExchanger), um diese Anwendung in FreeCAD zu verwenden.

### DXF Importeur 

FreeCAD hat einen eigenen Importeur und Exporteur für DXF Dateien, programmiert in C++. Derzeit führen sie nicht alle Funktionen des DXF Formats aus. Für diese Funktionen sind der alte Python Importeer und Exporteur weiterhin verfügbar. Diese benötigen die _ Seite für weitere Informationen.

### DWG converters 

FreeCAD cannot directly read and write DWG files. To convert DXF files to DWG files, and vice-versa, FreeCAD relies on external converters. There is built-in support for the following DWG converters:

-   [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, lacks support for some DWG entities).
-   [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (free).
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (commercial). <small>(v0.20)</small> 

See [Import Export Preferences](Import_Export_Preferences#DWG.md) and [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md) for more information.

### IfcOpenShell

_ ({{VersionMinus|0.18}}) und [BIM IfcExplorer](BIM_IfcExplorer/de.md) Werkzeugen verwendet. IfcOpenShell ist in den FreeCAD Installationsprogrammen für Windows und Mac enthalten.

### IfcJson

[IfcJson](https://github.com/buildingSMART/ifcJSON) ist eine Bibliothek, die zum Exportieren in das IFCJSON Dateiformat benötigt wird. IFCJSON ist ein neues IFC Format, das noch nicht von vielen Anwendungen unterstützt wird.

### Pycollada

[Pycollada](https://github.com/pycollada/pycollada/releases), auch bekannt als python-collada ist eine Python Bibliothek zum Lesen und Schreiben von Collada (DAE) Dateien. Pycollada ist in den FreeCAD Installationsprogrammen für Windows und Mac enthalten.

## Bildsynthese

### LuxCoreRender

_ Projekts. Offiziell wird sie nicht von der _ findest du weitere Informationen und Installationsanweisungen.

### LuxRender

_ ist eine der beiden Render Maschinen, die von der _ mit dem Arbeitsbereich Strahlverfolgung funktionieren, es könnte sich lohnen, es auszuprobieren. Siehe die [LuxRender](LuxRender/de.md) Seite für weitere Informationen und Installationsanweisungen, und den [LuxCoreRender](LuxCoreRender/de.md), wenn du eine modernere Software ausprobieren möchtest.

### POVRay

_ unterstützt werden. Siehe die [POV-Ray](POV-Ray/de.md) Seite für weitere Informationen und Installationsanweisungen.

## Finite Elemente 

### CalculiX

_ verwendet.

### Gmsh

_ und [Netz AusPartForm](Mesh_FromPartShape/de.md) Werkzeugen verwendet.

### Elmer

_ Werkzeug verwendet.

### FEniCS

_ verwendet.

### Z88

_ Werkzeug verwendet. FreeCAD benötigt das Open Source Paket Z88OS.

### OpenFOAM

_ und _ verwendet.

# Verwandte Seiten 

-   [Import Export](Import_Export/de.md)
-   [Import Export Einstellungen](Import_Export_Preferences/de.md)
-   [Drittanbieterbibliotheken](Third_Party_Libraries/de.md)




_

---
[documentation index](../README.md) > Installing additional components/de

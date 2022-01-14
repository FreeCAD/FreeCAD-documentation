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

[GitPython](https://github.com/gitpython-developers/GitPython) ist eine Bibliothek zur Interaktion mit Git Repositorien. Der [Erweiterungsverwalter](Std_AddonMgr/de.md) kann diese Bibliothek verwenden. GitPython ist in den FreeCAD Installationsprogrammen für Windows und Mac enthalten.

### GraphViz

[GraphViz](https://www.graphviz.org) ist eine Open Source Software zur Visualisierung von Graphen. Sie wird von dem Werkzeug [Std Abhängigkeitsgraph](Std_DependencyGraph/de.md) verwendet.

### OpenCAMLib

[OpenCAMLib](http://www.anderswallin.net/CAM) ist eine Open Source Bibliothek für Computergestützte Fertigung (engl.: computer aided manufacturing (CAM)) Algorithmen. Sie wird im [Pfad Arbeitsbereich](Path_Workbench/de.md) verwendet. Siehe die [OpenCamLib](OpenCamLib/de.md) Seite zu Installationsanweisungen.

### OpenSCAD

[OpenSCAD](https://www.openscad.org) ist ein 3D Volumenkörper Modellierer. Der [OpenSCAD Arbeitsbereich](OpenSCAD_Workbench/de.md) ist von dieser Software abhängig und der [ Arbeitsbereich Polygonnetze](Mesh_Workbench/de.md) verwendet sie für ihre booleschen Werkzeuge. Es wird auch für den Import von SCAD Dateien mit dem [Std Import](Std_Import/de.md) Werkzeug benötigt.

## Dateiformate

Die gesamte Software in diesem Abschnitt wird von den [Std Import](Std_Import/de.md) oder [Std Export](Std_Export/de.md) Werkzeugen verwendet.

### CADAustauscher

[CADExchanger](https://cadexchanger.com) ist eine kommerzielle Anwendung zum Austausch von verschiedenen CAD Dateiformaten. Es gibt einen [externen Arbeitsbereich](https://github.com/yorikvanhavre/CADExchanger), um diese Anwendung in FreeCAD zu verwenden.

### DXF Importeur 

FreeCAD hat einen eigenen Importeur und Exporteur für DXF Dateien, programmiert in C++. Derzeit führen sie nicht alle Funktionen des DXF Formats aus. Für diese Funktionen sind der alte Python Importeer und Exporteur weiterhin verfügbar. Diese benötigen die [Draft-dxf-importer](https://github.com/yorikvanhavre/Draft-dxf-importer) Python Bibliothek. Siehe die [FreeCAD und DXF Import](FreeCAD_and_DXF_Import/de.md) Seite für weitere Informationen.

### DWG Konverter 


<div class="mw-translate-fuzzy">

FreeCAD kann DWG Dateien weder direkt lesen noch selbst erstellen. Um DXF Dateien in DWG Dateien zu wandeln, und umgekehrt, benötigt FreeCAD externe Konverter. FreeCAD unterstützt standardmäßig folgende Konverter:

-   [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, unterstützt nicht alle DWG Entities).
-   [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (gratis).
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (kostenpflichtig). <small>(v0.20)</small> 


</div>

Siehe [Import Export Einstellungen](Import_Export_Preferences/de#DWG.md), [FreeCAD and DWG Import](FreeCAD_and_DWG_Import/de.md) für mehr Informationen.

### IfcOpenShell

[IfcOpenShell](http://ifcopenshell.org) ist eine Bibliothek ist eine Bibliothek für die Arbeit mit dem Industry Foundation Classes (IFC) Dateiformat, daß in der Architektur Verwendung findet. Die Bibliothek wird auch von den [Arch IfcExplorer](Arch_IfcExplorer/de.md) ({{VersionMinus|0.18}}) und [BIM IfcExplorer](BIM_IfcExplorer/de.md) Werkzeugen verwendet. IfcOpenShell ist in den FreeCAD Installationsprogrammen für Windows und Mac enthalten.

### IfcJson

[IfcJson](https://github.com/buildingSMART/ifcJSON) ist eine Bibliothek, die zum Exportieren in das IFCJSON Dateiformat benötigt wird. IFCJSON ist ein neues IFC Format, das noch nicht von vielen Anwendungen unterstützt wird.

### Pycollada

[Pycollada](https://github.com/pycollada/pycollada/releases), auch bekannt als python-collada ist eine Python Bibliothek zum Lesen und Schreiben von Collada (DAE) Dateien. Pycollada ist in den FreeCAD Installationsprogrammen für Windows und Mac enthalten.

## Bildsynthese

### LuxCoreRender

[LuxCoreRender](https://www.luxcorerender.org) ist eine Render Maschine, ein Neustart des [LuxRender](LuxRender/de.md) Projekts. Offiziell wird sie nicht von der [Arbeitsbereich Strahlverfolgung](Raytracing_Workbench/de.md) unterstützt, aber es könnte sich lohnen, sie auszuprobieren. Es wird offiziell von der neuen [Render Arbeitsbereich](https://github.com/FreeCAD/FreeCAD-render) unterstützt, die als zukünftiger Ersatz für den Arbeitsbereich Strahlverfolgung gedacht ist. Auf der Seite [LuxCoreRender](LuxCoreRender/de.md) findest du weitere Informationen und Installationsanweisungen.

### LuxRender

[https://luxcorerender.org/history/ LuxRender](https://luxcorerender.org/history/_LuxRender.md) ist eine der beiden Render Maschinen, die von der [Arbeitsbereich Strahlverfolgung](Raytracing_Workbench/de.md) unterstützt werden. Im Jahr 2013 wurde das Projekt neu gestartet und wurde zu [LuxCoreRender](LuxCoreRender/de.md), wobei der Code neu geschrieben und die Kompatibilität verbessert wurde. Offiziell unterstützt der Arbeitsbereich Strahlverfolgung nur noch den aufgegebenen [LuxRender](LuxRender/de.md) (letzte Version ist 1.6, 2017-12-28), während der neue [Render Arbeitsbereich](https://github.com/FreeCAD/FreeCAD-render) (gedacht als zukünftiger Ersatz des Arbeitsbereich Strahlverfolgung) stattdessen LuxCoreRender unterstützt und die Unterstützung für LuxRender eingestellt hat. Wie auch immer, auch wenn es offiziell nicht unterstützt wird, kann [LuxCoreRender](LuxCoreRender/de.md) mit dem Arbeitsbereich Strahlverfolgung funktionieren, es könnte sich lohnen, es auszuprobieren. Siehe die [LuxRender](LuxRender/de.md) Seite für weitere Informationen und Installationsanweisungen, und den [LuxCoreRender](LuxCoreRender/de.md), wenn du eine modernere Software ausprobieren möchtest.

### POVRay

[POV-Ray](https://www.povray.org) ist ein sehr bekannter Strahlenverfolger zur Bildsynthese von fotorealistischen Bildern. Er ist einer von zwei Bildsynthese Engines, die derzeit vom [Arbeitsbereich Strahlverfolgung](Raytracing_Workbench/de.md) unterstützt werden. Siehe die [POV-Ray](POV-Ray/de.md) Seite für weitere Informationen und Installationsanweisungen.

## Finite Elemente 

### CalculiX

[CalculiX](http://calculix.de) ist eine Garnitur von zwei Finite Element Paketen: CalculiX CrunchiX, ein FEM Löser, und CalculiX GraphiX, ein GUI Frontend. Nur der Löser wird von FreeCAD unterstützt. Er wird von dem Werkzeug [Löser CalculiX](FEM_SolverCalculiX/de.md) verwendet.

### Gmsh

[Gmsh](http://gmsh.info) ist ein automatischer Finite Element Netzgenerator. Er wird von den [FEM NetzGmshAusForm](FEM_MeshGmshFromShape/de.md) und [Netz AusPartForm](Mesh_FromPartShape/de.md) Werkzeugen verwendet.

### Elmer

[Elmer](https://www.csc.fi/web/elmer) ist eine Multiphysik Simulationssoftware, die 2005 quelloffen wurde. In FreeCAD werden seine Gitter und Löser Module vom [FEM LöserElmer](FEM_SolverElmer/de.md) Werkzeug verwendet.

### FEniCS

[FEniCS](https://fenicsproject.org) ist eine Berechnungsplattform zur Lösung partieller Differentialgleichungen (PDEs), die bei der Lösung von FEM Problemen weit verbreitet sind. Sie wird vom [FEM Arbeitsbereich](FEM_Workbench/de.md) verwendet.

### Z88

[Z88](https://en.z88.de) ist ein weiteres FEM Programm, das einen Netzgenerator, einen Löser und Konverter beinhaltet. Es wird vom [FEM Löser Z88](FEM_SolverZ88/de.md) Werkzeug verwendet. FreeCAD benötigt das Open Source Paket Z88OS.

### OpenFOAM

[OpenFOAM](https://openfoam.org) ist eine große Sammlung von Bibliotheken für numerische Strömungsmechanik (engl.: Computational Fluid Dynamics) (CFD) Simulationen. OpenFOAM wird von [Cfd](Cfd_Workbench/de.md) und [CfdOF](https://github.com/jaheyns/CfdOF) [externe Arbeitsbereiche](external_workbenches/de.md) verwendet.

# Verwandte Seiten 

-   [Import Export](Import_Export/de.md)
-   [Import Export Einstellungen](Import_Export_Preferences/de.md)
-   [Drittanbieterbibliotheken](Third_Party_Libraries/de.md)




[<img src="images/Property.png" style="width:16px"> User Documentation/de](<img src="images/Property.png" style="width:16px"> User_Documentation/de.md)

---
[documentation index](../README.md) > Installing additional components/de

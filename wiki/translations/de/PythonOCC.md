# PythonOCC/de
## Beschreibung

[PythonOCC](PythonOCC/de.md) ist ein Projekt, das darauf abzielt, den gesamten Funktionsumfang der [OpenCASCADE-Technology](OpenCASCADE/de.md)(OCCT)-Funktionen durch das [Python](Python/de.md)-Modul bereitzustellen. Dies ist ein anderer Ansatz als der von FreeCAD, bei dem nur bestimmte Komponenten von OCCT über den Arbeitsbereich [Part](Part_Workbench/de.md) bereitgestellt werden.

PythonOCC hingegen bietet Zugriff auf alle OCCT Klassen und Funktionen, ist also komplex, aber auch sehr mächtig. Wenn du also durch die OCCT Funktionalität von FreeCAD eingeschränkt bist, ist die Verwendung von `OCC` eine gute Alternative.



## Anwendung

Der Arbeitsbereich [Part](Part_Workbench/de.md) enthält die Methoden `Part.__toPythonOCC__()` und `Part.__fromPythonOCC__()` zum Austausch von `TopoDS_Shape`([Part TopoForm](Part_TopoShape/de.md))-Dateneinheiten zu und von PythonOCC. Diese Methoden ermöglichen es, die volle Leistung von OCCT in Python zu nutzen und die resultierenden Formen dann wieder in FreeCAD-Objekte einzufügen.

PythonOCC wird intern vom [IFC](Arch_IFC/de.md) Betrachter verwendet, der in den Bibliotheken [IfcOpenShell](IfcOpenShell/de.md) enthalten ist. IfcOpenShell wird zum Lesen und Schreiben von [IFC](Arch_IFC/de.md) Dokumenten mit FreeCAD verwendet. PythonOCC wird nur benötigt, um den integrierten Betrachter von IfcOpenShell zu starten, ansonsten ist es nicht notwendig.



## Einrichtung

PythonOCC muss aus den Quellen kompiliert werden. Dazu benötigst du die entsprechenden Entwicklungsdateien für [OpenCASCADE Technologie](OpenCASCADE/de.md). (OCCT) und SWIG. Die ältere Version von PythonOCC war dazu gedacht, OCE 0.18, die Gemeinschaftsausgabe von OCCT 6.9.x, die jetzt nicht mehr gewartet wird, zu umhüllen. Die neueste Version von PythonOCC soll nun mit der neuen, offiziellen Version OCCT 7.4 zusammenarbeiten.

Zusammen mit OCCT 7.4 erfordert PythonOCC relativ neue Abhängigkeiten wie Python 3.7, CMake 3.12 und SWIG 3.0.11. Python 2 wird nicht mehr unterstützt.

Es ist auch möglich, vorkompilierte PythonOCC Bibliotheken mit [Conda](Conda/de.md) zu installieren. Weitere Informationen und Kompilierungsanweisungen findest du im Repositorium des Hauptprojekts, [tpaviot/pythonocc-core](https://github.com/tpaviot/pythonocc-core).



## Kompilieren

PythonOCC kann man auch selbst kompilieren (siehe [instructions](https://github.com/tpaviot/pythonocc-core/blob/master/INSTALL.md)). Hierunter findet man den Ablauf für Debian/Ubuntu, der die Opencascade-Pakete der Distribution verwendet:

    git clone git://github.com/tpaviot/pythonocc-core.git pythonocc
    cd pythonocc
    mkdir build
    cd build
    cmake -DOCE_INCLUDE_PATH=/usr/include/opencascade -DOCE_LIB_PATH=/usr/lib/x86_64-linux-gnu ..
    make



## Weitere Informationen 

-   Projektseite: [pythonocc.org](http://www.pythonocc.org/)
-   Neuere Version kompatibel mit OCCT 7.4, [tpaviot/pythonocc-core](https://github.com/tpaviot/pythonocc-core).
-   Ältere Version kompatibel mit OCE 0.18, die Gemeinschaftsausgabe von OCCT 6.9.x, [tpaviot/pythonocc](https://github.com/tpaviot/pythonocc).
-   [IfcPlusPlus kompiliert unter Gentoo - Fragen und Alternativen?](https://forum.freecadweb.org/viewtopic.php?f=39&t=33254)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > PythonOCC/de

# Robot project/de
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}


<div class="mw-translate-fuzzy">

Dies ist der [Projektartikel](project/de.md) für das Roboter Projekt. Es folgt den Regeln des \[<http://en.wikipedia.org/wiki/Getting_Things_Done#GTD_methodology>\| Getting things done\] Prozesses. Die Projekte sind im [Entwicklungsfahrplan](Development_roadmap/de.md) zusammengefasst.


</div>

## Zweck und Grundsätze 

Dieses Projekt soll die grundlegenden Technologien für eine realistische Robotersimulation in FreeCAD festlegen. Im ersten Schritt zielt es auf den 6-achsigen Standard Industrieroboter ab.

## Ergebnis

Robotersimulation

![](images/Robot.jpg )

## Ideenfindung

### Bibliotheken im Feld 

-   [OROCOS](http://www.orocos.org/) tragbare C++ Bibliotheken für fortgeschrittene Maschinen- und Robotersteuerung
-   [ROBOOP](http://roboop.sourceforge.net/) Ein objektorientiertes Robotik Paket in C++
-   [Beremiz](http://www.beremiz.org/) eine OpenSource SPS.

### Normen für die Kommunikation 

-   [OPC UA](http://en.wikipedia.org/wiki/OPC_Unified_Architecture) ein Maschine zu Maschine Kommunikationsprotokoll für die industrielle Automatisierung (SPS)
-   [1](https://www.ipk.fraunhofer.de/de/referenzen/realistic-robot-simulation.html) Deutsche Initiative zur Verbesserung der Genauigkeit von Robotersteuerungen und Optimierung von Offline-Roboterprogrammierung
-   [Realistische Robotersimulation (RRS)](http://www.realistic-robot-simulation.org/) RRS-2, Schnittstelle zur virtuellen Robotersteuerung (VRC)

### Middleware für die Kommunikation 

-   [D-Bus](http://en.wikipedia.org/wiki/D-Bus) einen Software Bus, eine Interprozesskommunikation (IPC) und einen Remote Procedure Call (RPC) Mechanismus, der die Kommunikation zwischen mehreren Computerprogrammen ermöglicht
-   [CORBA](http://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture) ermöglicht die Zusammenarbeit zwischen Systemen mit unterschiedlichen Betriebssystemen, Programmiersprachen und Computerhardware

### Kommerzielle Produkte in diesem Bereich 

-   [Visual Components](http://www.visualcomponents.com/Solutions/Robot-Simulation)
-   [Delmia](http://www.3ds.com/products/delmia/welcome/)
-   [KUKA Sim](http://www.kuka-robotics.com/germany/en/products/software/kuka_sim/start.htm)

### Fachwissen

-   [Kinematic definition](http://prt.fernuni-hagen.de/lehre/KURSE/PRT001/course_main/node15.html) \--\> Verknüpfung veraltet!!!
-   [Denavit--Hartenberg Parameter](https://en.wikipedia.org/wiki/Denavit%E2%80%93Hartenberg_parameters) Parameter, die mit einer bestimmten Konvention zum Anhängen von Bezugsrahmen an die Verbindungen des Robotermanipulators verbunden sind
-   [Roboter VRML modele](http://www.iha.tut.fi/education/IHA-3500/robotlib/) \--\> Verknüpfung veraltet!!!

## Organisieren

-   Visuelle Darstellung von 6-Achsen Robotern (abgeschlossen)
-   Vorwärts und inverse kinematische Berechnung beliebiger Roboter (abgeschlossen)
-   RobotLib, dynamisch lesbare Robotertypen (im Aufbau)
-   Trajektorien Simulation (im Aufbau)
    -   Kollisionssimulation
    -   Erkennung von Konfigurationsänderungen und Singularitäten
    -   Zeitschätzung
    -   verwendetes Volumen (geplant)
-   Postprozessor für Kuka Roboter (im Aufbau)
-   Prozess- und Arbeitszellensteuerung (geplant)
-   Filmerstellung aus Simulation (geplant)

## Nächste Schritte 

-   Trajektorien- und Wegpunktverwaltung.



[<img src="images/Property.png" style="width:16px"> Roadmap](Category_Roadmap.md)

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > [Robot](Robot_Workbench.md) > Robot project/de

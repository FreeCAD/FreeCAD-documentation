# Robot Workbench/de






**Der Roboter Arbeitsbereich ist nicht gewartet. Wenn du Erfahrung mit dem Thema hast und daran interessiert bist, es zu pflegen, gib bitte deine Absicht im Entwicklerbereich des [https://forum.freecadweb.org/index.php FreeCAD Forums] an.

Der Grund dafür, dass sich dieser Arbeitsbereich noch im Master Quellcode befindet, liegt darin, dass dieser Arbeitsbereich in C++ programmiert ist. Wenn dieser Arbeitsbereich in Python programmiert werden könnte, dann könnte sie zu einem[externen Arbeitsbereich](external_workbenches/de.md) gemacht und in ein separates Repositorium verschoben werden.
**

## Einführung

<img alt="Roboter Arbeitsbereichssymbol" src=images/Workbench_Robot.svg  style="width:128px;">

Die <img alt="" src=images/Workbench_Robot.svg  style="width:24px;"> [Roboter Arbeitsbereich](Robot_Workbench/de.md) ist ein Werkzeug zur Simulation eines Standard [6-Achsen Industrieroboters](Robot_6-Axis/de.md), wie [Kuka](http://kuka.com/).

Du kannst die folgenden Aufgaben erledigen:

-   Richten eine Simulationsumgebung mit einem Roboter und Werkstücken ein.
-   Erstellen und Auffüllen von Bewegungstrajektorien.
-   Zerlege die Merkmale eines CAD-Bauteils in eine Trajektorie.
-   Simuliere die Roboterbewegung und das Erreichen der Distanz.
-   Exportiere die Trajektorie in eine Roboterprogrammdatei.

Um loszulegen, versuche es mit dem [Roboter Tutorium](Robot_tutorial/de.md), und sieh Dir die Programmierschnittstelle in der Beispieldatei [RobotExample.py](https://github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py) an.


{{TOCright}}

<img alt="" src=images/Robot_Workbench_example.jpg  style="width:500px;">

## Werkzeuge

Hier die wichtigsten Befehle, mit denen eine Roboteranordnung erstellt werden kann.

### Roboter

Die Werkzeuge zur Erstellung und Verwaltung der 6-Achsen-Roboter

-   <img alt="" src=images/Robot_CreateRobot.svg  style="width:30px;"> [Einen Roboter erstellen](Robot_CreateRobot/de.md): Einen neuen Roboter in die Szene einfügen
-   <img alt="" src=images/Robot_Simulate.svg  style="width:30px;"> [Eine Bewegungsbahn simulieren](Robot_Simulate/de.md): Öffnet den Simulationsdialog und lässt dich Folgendes simulieren
-   <img alt="" src=images/Robot_Export.svg  style="width:30px;"> [Eine Bewegungsbahn exportieren](Robot_Export/de.md): Exportieren einer Roboterprogrammdatei
-   <img alt="" src=images/Robot_SetHomePos.svg  style="width:30px;"> [Ausgangsposition festlegen](Robot_SetHomePos/de.md): Festlegen der Ausgangsposition eines Roboters
-   <img alt="" src=images/Robot_RestoreHomePos.svg  style="width:30px;"> [Ausgangsposition wiederherstellen](Robot_RestoreHomePos/de.md): Bewege den Roboter in seine Ausgangsposition

### Trajektorien

Werkzeuge zum Erstellen und Bearbeiten von Trajektorien. Es gibt zwei Arten, die parametrische und die nicht parametrische.

#### Nicht parametrische Trajektorien 

-   <img alt="" src=images/Robot_CreateTrajectory.svg  style="width:30px;"> [Eine Trajektorie erstellen](Robot_CreateTrajectory/de.md): Fügt ein neues leeres Trajektorienobjekt in die Szene ein
-   <img alt="" src=images/Robot_SetDefaultOrientation.svg  style="width:30px;"> [Lege die Standardausrichtung fest](Robot_SetDefaultOrientation/de.md): Lege die Orientierung fest - Wegpunkte werden standardmäßig erstellt
-   <img alt="" src=images/Robot_SetDefaultValues.svg  style="width:30px;"> [Setze den Standard Geschwindigkeitsparameter](Robot_SetDefaultValues/de.md): Lege die Standardwerte für die Weg-punkt Erstellung fest
-   <img alt="" src=images/Robot_InsertWaypoint.svg  style="width:30px;"> [Einen Wegpunkt einfügen](Robot_InsertWaypoint/de.md): Einfügen eines Wegpunktes von der aktuellen Roboterposition in eine Trajektorie
-   <img alt="" src=images/Robot_InsertWaypointPre.svg  style="width:30px;"> [Einen vorgewählten Wegpunkt einfügen](Robot_InsertWaypointPre/de.md): Einfügen eines Wegpunktes von der aktuellen Mausposition in eine Trajektorie

#### Parametrische Trajektorien 

-   <img alt="" src=images/Robot_Edge2Trac.svg  style="width:30px;"> [Erstellen einer Trajektorie aus Kanten](Robot_Edge2Trac/de.md): Einfügen eines neuen Objekts, das Kanten zu einer Trajektorie zerlegt
-   <img alt="" src=images/Robot_TrajectoryDressUp.svg  style="width:30px;"> [Ankleiden einer Trajektorie](Robot_TrajectoryDressUp/de.md): Erlaubt dir, eine oder mehrere Eigenschaften einer Trajektorie außer Kraft zu setzen
-   <img alt="" src=images/Robot_TrajectoryCompound.svg  style="width:30px;"> [Trajektorienverbund](Robot_TrajectoryCompound/de.md): Erzeugen eines Verbunds aus einigen Einzeltrajektorien

## Skripten

Siehe das [Roboter API Beispiel](Robot_API_example/de.md) für eine Beschreibung der Funktionen, die zur Modellierung der Roboterverschiebungen verwendet werden.

## Tutorien

-   [6-Achsen Roboter](Robot_6-Axis/de.md)
-   [VRML Vorbereitung für Robotersimulation](VRML_Preparation_for_Robot_Simulation/de.md)





{{Robot Tools navi

}} 

[Category:Workbenches](Category:Workbenches.md)

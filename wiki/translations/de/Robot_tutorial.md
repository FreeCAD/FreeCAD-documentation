# Robot tutorial/de
---
- TutorialInfo:/de
   Topic: Roboter Arbeitsbereich
   Level: Anfänger
   Time:
   Author:r-frank
   FCVersion:0.16.6703
   Files:
}}

## Einführung

Dieses Tutorium soll dir beibringen, wie du den <img alt="" src=images/Workbench_Robot.svg  style="width:24px;"> [Roboter Arbeitsbereich](Robot_Workbench/de.md) verwendest, um die Einrichtung einer Roboterzelle zu simulieren.

![](images/Robot_Tutorial_RobotSimulation.gif ) 
*Endergebnis dieses Tutoriums*

## Bevor du beginnst 

Dieses Tutorium wurde für FreeCAD 0.16.6703 oder höher geschrieben. Wenn du also FreeCAD nicht auf deinem Computer hast, gehe auf die [Herunterladen](Download/de.md) Seite und führe die Installation durch.

Dieses Tutorium zielt auf die Verwendung von [Industrieroboter](http://en.wikipedia.org/wiki/Industrial_robot) ab und nicht mobile oder Serviceroboter (siehe Wikipedia Eintrag auf [moderne Roboter](http://en.wikipedia.org/wiki/Robot#Modern_robots)).

## Einrichten der Szenerie 

1.  Wechsle zum <img alt="" src=images/Workbench_Robot.svg  style="width:24px;">[Roboter Arbeitsbereich](Robot_Workbench/de.md)
2.  Erstelle ein neues Dokument, durch auswählen **Datei** → ** Neu** im oberen Menü
3.  Füge einen Kuka IR500 Roboter in die Szene ein, durch auswählen **Roboter** → **Roboter einfügen** → **Kuka IR500** aus dem oberen Menü
4.  Wechsle zur axonometrischen Ansicht, durch anklicken auf die <img alt="" src=images/View-axometric.svg  style="width:24px;"> Schaltfläche
5.  Zoom um alles anzupassen durch Klicken auf <img alt="" src=images/Std_ViewFitAll.svg  style="width:24px;"> [Alle anpassen](Std_ViewFitAll/de.md) Schaltfläche
6.  Speichere deine Datei \...

## Einstellen einer Bewegungsbahn 

1.  Wechsle zum <img alt="" src=images/Workbench_Robot.svg  style="width:24px;"> [Roboter Arbeitsbereich](Robot_Workbench/de.md)
2.  Aktiviere den Modell Reiter in der [Baumansicht](tree_view/de.md), durch Klicken darauf
3.  Erstelle eine neue Bewegungsbahn durch Klick auf die <img alt="" src=images/Robot_CreateTrajectory.svg  style="width:24px;"> [Roboter Erstelle Bewegungsbahn](Robot_CreateTrajectory/de.md) Schaltfläche
4.  Wähle den Roboter in der [Baumansicht](tree_view/de.md)
5.  Lege die Home Position für den Roboter durch Klick auf <img alt="" src=images/Robot_SetHomePos.svg  style="width:24px;"> [Robot_SetzeHomePos](Robot_SetHomePos/de.md)
6.  Wechsle zum [Aufgabenpaneel](Task_Panel/de.md)
7.  Durch Benutzung der Schieber verändere die Roboterposition
8.  Wenn der Roboter und Bewegungsbahn in der [Baumansicht](tree_view/de.md) ausgewählt wurden

klicken auf <img alt="" src=images/Robot_InsertWaypoint.svg  style="width:24px;"> [Roboter EinfügenWegpunkt](Robot_InsertWaypoint/de.md) fügt den Weg-Punkt in die Bewegungsbahn ein

1.  Jeder Weg-Punkt wird mit einem gelben Kreuz markiert und die gesamte Bewegungsbahn wird durch orange Linien dargestellt
2.  Definiere mindestens drei verschiedene Wegpunkte und füge sie in die Bewegungsbahn ein

## Simulieren der Roboter Bewegung 

1.  Wähle den Roboter und die Bewegungsbahn in der [Baumansicht](tree_view/de.md)
2.  Wähle die Simulation durch Klick auf <img alt="" src=images/Robot_Simulate.svg  style="width:24px;">[Roboter Simulieren](Robot_Simulate/de.md)
3.  Klicke auf den Wiedergabe** &#9654;** Knopf
4.  Simulation beobachten


 {{Robot Tools navi}} {{Userdocnavi
---



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Robot](Robot_Workbench.md) > Robot tutorial/de

# <img alt="" src=images/User_hub.png  style="width:64px;"> User hub/de



Dies ist der wichtigste Hilfebereich für FreeCAD-Neueinsteiger.

FreeCAD wird ständig weiterentwickelt, so dass es zu fehlenden oder veralteten Informationen kommen kann. Wenn du die Informationen, die du brauchst, nicht findest, zögere nicht, sie im [FreeCAD-Forum](https://forum.freecad.org) zu erfragen.

Wenn Du zu FreeCAD beitragen möchtest, [spende](donate/de.md) bitte und lies die Seite [FreeCAD Unterstützen](Help_FreeCAD.md) für andere Möglichkeiten, einen Beitrag zu leisten. Wenn Du dieses Wiki bearbeiten möchtest, fordere ein Wiki-Konto mit Bearbeiterberechtigungen [im Forum](https://forum.freecad.org/viewtopic.php?f=21&t=6830) an und lies die [Wiki-Seiten](WikiPages/de.md) für die allgemeinen Richtlinien, die Du befolgen solltest.

Wenn du erfahren möchtest, wie FreeCAD vor Jahren begann, besuche die Seite [Geschichte](History/de.md).



## FreeCAD benutzen 



### Einleitung

-   [Anwendungsübersicht](About_FreeCAD/de.md): Ein allgemeiner Überblick über FreeCAD
-   Wie man FreeCAD auf [Windows](Installing_on_Windows/de.md), [Linux](Installing_on_Linux/de.md) und [Mac](Installing_on_Mac/de.md) installiert.
-   [Einrichtung Hilfedateien](Installing_Helpfile/de.md): wie man die Offline-Dokumentation installiert, die auf diesem Wiki basiert.
-   [Einrichtung zusätzlicher Komponenten](Installing_additional_components/de.md): wie zusätzliche Komponenten von Drittanbietern installieren, die mit FreeCAD zusammenarbeiten können.
-   [Erste Schritte](Getting_started/de.md): Eine kurze Übersicht über die verfügbaren Werkzeuge.
-   [FAQ](Frequently_asked_questions/de.md): Häufig gestellte Fragen.
-   [Tutorien](Tutorials/de.md) decken verschiedene Teile von FreeCAD ab.



#### Umstieg von einer anderen Anwendung? 

-   [Fehlerumgehung](Workarounds/de.md)
-   [Umstieg auf FreeCAD von Fusion360](Migrating_to_FreeCAD_from_Fusion360/de.md)
-   [Umstieg auf FreeCAD von OnShape](Migrating_to_FreeCAD_from_OnShape/de.md)
-   [Umstieg auf FreeCAD von SolidWorks](Migrating_to_FreeCAD_from_SolidWorks/de.md)
-   [Umstieg auf FreeCAD von Revit](Migrating_to_FreeCAD_from_Revit/de.md)
-   [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide)
-   [BIM applications compatibility table](BIM_application_compatibility_table/de.md)



### Grundlegende Anwendung 

-   [Oberfläche](Interface/de.md): Die FreeCAD-Benutzeroberfläche besteht aus verschiedenen grafischen Elementen auf dem Bildschirm, darunter der [3D-Ansicht](3D_view/de.md), der [Baumansicht](Tree_view/de.md), dem [Eigenschafteneditor](Property_editor/de.md), dem [Aufgaben-Fenster](Task_panel/de.md) und der [Python-Konsole](Python_console/de.md).
-   [Mausnavigation](Mouse_navigation/de.md): Die verschiedenen Arten der Verwendung der Maus oder des Trackpads zur Navigation in der 3D-Ansicht.
-   [Auswahlmethoden](Selection_methods/de.md): Die unterschiedlichen Methoden zur Auswahl von Objekten im Programm.
-   [Objektname](Object_name/de.md): Alle Objekte haben einen einzigartigen, nicht veränderbaren `Namen`, der sie eindeutig identifiziert und ein `Label` das vom Anwender beliebig geändert werden kann.
-   [Voreinstellungseditor](Preferences_Editor/de.md): Das System, mit dem viele Eigenschaften des Basissystems und der einzelnen Arbeitsbereiche gesteuert werden können.
-   [Dateiformate](Import_Export/de.md): Die verschiedenen Dateiformate, die FreeCAD lesen und schreiben kann.



### Arbeitsbereiche

[Arbeitsbereiche](Workbenches/de.md) sind Werkzeugsammlungen, die für bestimmte Aufgabe eingesetzt werden. Dies sind die Basis-Arbeitsbereiche, die mit jeder FreeCAD-Installation zur Verfügung gestellt werden:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [ Standard-Werkzeuge](Std_Base/de.md). Diese Befehle und Werkzeuge stehen in allen Arbeitsbereichen zur verfügung.

-   <img alt="" src=images/Workbench_Assembly.svg  style="width:32px;"> Der Arbeitsbereich [Assembly](Assembly_Workbench/de.md) für den Zusammenbau und die Berechnung mechanischer Baugruppen. {{Version/de|1.0}}

-   <img alt="" src=images/Workbench_BIM.svg  style="width:32px;"> Der Arbeitsbereich [BIM](BIM_Workbench/de.md) für die Arbeit mit Bauwerkselementen und die Erstellung von Modellen entsprechend der [Bauwerksdatenmodellierung](https://de.wikipedia.org/wiki/Building_Information_Modeling), also BIM-Modellen (nach engl. [Building Information Modelling](https://en.wikipedia.org/wiki/Building_information_modeling), kurz BIM). Er kombiniert den Arbeitsbereich Arch aus der {{VersionMinus/de|0.21}} und den vormals externen Arbeitsbereich BIM.

-   <img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> Der Arbeitsbereich [CAM](CAM_Workbench/de.md) Wird eingesetzt, um G-Code-Anweisungen zu erstellen. Dieser Arbeitsbereich wurde in {{VersionMinus/de|0.21}} \"Path\" genannt.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> Der Arbeitsbereich [Draft](Draft_Workbench/de.md) enthält 2D-Werkzeuge und grundlegende 2D- und 3D-CAD-Bearbeitungen.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> Der [Arbeitsbereich FEM](FEM_Workbench/de.md) stellt einen Arbeitsablauf für die Finite-Elemente-Analyse (FEA) zur Verfügung.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> Der Arbeitsbereich [Inspection](Inspection_Workbench/de.md) stellt spezielle Werkzeuge für die Untersuchung von Formen zur Verfügung. Er befindet sich noch in einer frühen Phase der Entwicklung.

-   <img alt="" src=images/Workbench_Material.svg  style="width:32px;"> Der Arbeitsbereich [Material](Material_Workbench/de.md) kümmert sich um FreeCADs Materialsystem. {{Version/de|1.0}}

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> Der Arbeitsbereich [Mesh](Mesh_Workbench/de.md) für die Arbeit mit triangulierten Polygonnetzen.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> Der Arbeitsbereich [OpenSCAD](OpenSCAD_Workbench/de.md) für das Zusammenspiel mit OpenSCAD und die Reparatur der Modellhistorie von [konstruktiver Festkörpergeometrie](constructive_solid_geometry/de.md) (Constructive-Solid-Geometry - CSG).

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> Der Arbeitsbereich [Part](Part_Workbench/de.md) für die Arbeit mit geometrischen Grundkörpern und booleschen Verknüpfungen.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> Der Arbeitsbereich [Part Design](PartDesign_Workbench/de.md) zur Erstelllung von Part-Formen aus Skizzen.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> Der Arbeitsbereich [Points](Points_Workbench/de.md) (Punkte) für die Arbeit mit Punktwolken.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> Der Arbeitsbereich [Reverse Engineering](Reverse_Engineering_Workbench/de.md) soll spezielle Werkzeuge zum Konvertieren von Formen, Festkörpern oder (Polygon-)Netzen in parametrische zu FreeCAD kompatible Formelemente bereitstellen.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> Der Arbeitsbereich [Robot](Robot_Workbench/de.md) (Roboter) zur Untersuchung von Roboterbewegungen. Wird zur Zeit nicht gewartet.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> Der Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md) (Skizzierer) für die Arbeit mit durch geometrische Beziehungen bestimmten Skizzen.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> Der Arbeitsbereich [Spreadsheet](Spreadsheet_Workbench/de.md) (Tabellenkalkulation) zur Erstellung und Bearbeitung von Daten in Kalkulations- bzw. Konstruktionstabellen.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> Der Arbeitsbereich [Surface](Surface_Workbench/de.md) (Oberfläche) stellt Werkzeuge zum Erstellen und Ändern von Oberflächen zur Verfügung. Er ähnelt der Option *Fläche aus Kanten* des [Part Form-Generators](Part_Builder/de.md).

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> Der Arbeitsbereich [TechDraw](TechDraw_Workbench/de.md) dient zur Ableitung technischer Zeichnungen von 3D-Modellen.

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> Der Arbeitsbereich [Test Framework](Testing/de.md) ist für die FreeCAD-Fehlersuche.



### Makros

[Makros](Macros/de.md) sind relativ kleine Abschnitte von [Python-Code](Python/de.md), die eine einfache oder eine komplexe Aufgabe erledigen, die in FreeCADs Basis-System nicht zur Verfügung steht.

Erfahrene Anwender haben verschiedene [Makros](macros/de.md) erstellt, um FreeCAD durch weitere Fähigkeiten zu verbessern.

Seit FreeCAD v0.17 können viele Makros mit Hilfe des [Addon-Managers](Std_AddonMgr/de.md) installiert werden. Eine Liste der Makros findet man auf der Seite [Makrorezepte](Macros_recipes/de.md). Für eine manuelle Installation siehe [Wie Makros installiert werden](How_to_install_macros/de.md).



### Externe Arbeitsbereiche 

Wenn viele Makros oder Funktionen gemeinsam entwickelt und in Symbolleisten und Menüs organisiert werden, können sie zu einem neuen Arbeitsbereich werden.

[Externe Arbeitsbereiche](External_workbenches/de.md) sind Sammlungen von Funktionen, die nicht Teil des FreeCAD Basissystems sind, üblicherweise entwickelt von erfahrenen Anwendern und auf einen bestimmten Bedarf abzielend.

Seit FreeCAD 0.17 können viele Arbeitsbereiche mit dem [Addon-Manager](Std_AddonMgr/de.md) installiert werden. Für die manuelle Installation siehe [Wie zusätzliche Arbeitsbereiche installiert werden](How_to_install_additional_workbenches/de.md).



## Referenz

-   [Commands Reference](List_of_Commands.md): Eine vollständige Liste der zur Verfügung stehenden FreeCAD-Befehle in Englisch.
-   [Commands Reference/de](List_of_Commands/de.md): Eine Liste aller zur Verfügung stehenden FreeCAD-Befehle, deren Wiki-Seite ins Deutsche übersetzt ist.



## Online-Hilfe 

Dies ist FreeCADs offizielle Online-Hilfe. Bitte beachten, dass das gesamte Online-Hilfesystem gegenwärtig überarbeitet wird. Sie wird verwendet, um eine .CHM Datei zu erzeugen, die mit den Binärpaketen von FreeCAD verteilt wird. Im Moment fasst die Online-Hilfe einige der vollständigsten Abschnitte dieses Wikis zusammen.

-   [Online-Hilfesystem - Inhaltsverzeichnis](Online_Help_Toc/de.md)



## Mehr

-   Das [Hauptanwenderzentrum](Power_users_hub/de.md) ist die Anlaufstelle, wenn man mehr über die fortgeschrittene Nutzung von FreeCAD sehen möchte.
-   Das [FreeCAD-Gemeinschaftsportal](FreeCAD_Community_Portal/de.md) listet Projekte auf, die von Mitgliedern der Gemeinschaft rund um FreeCAD erstellt wurden.
-   Wird ein Begriff oder eine Beschreibung in FreeCAD nicht verstanden, kann sich ein Blick in das [Glossar](Glossary/de.md) lohnen.



---
⏵ [documentation index](../README.md) > [Hubs](Category_Hubs.md) > User hub/de

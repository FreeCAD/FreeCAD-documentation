# Topological Naming Project/de


Diese Seite ist der Beschreibung der Idee des Google Summer of Code-Projekts bezüglich der topologischen Benennung gewidmet. Für das Thema an sich siehe [Benennungsprojekt](Naming_project/de.md). Die verlinkte Wiki-Seite kann auch als Ausgangspunkt dienen, um in das Benennungsproblem einzusteigen.

## Überblick

FreeCAD ist ein parametrisches Modellierungssystem, daher hängen verschiedene Modellierungsschritte von einem oder mehreren vorherigen Schritten ab. Änderungen, die an einem Objekt vorgenommen werden, übertragen sich durch die Modellierungsgeschichte auf alle abhängigen Objekte. Dies wird durch ein Verbindungssystem erreicht, das mit Eigenschaften implementiert wird. Diese Verknüpfung ist sehr robust, wenn sie auf Objektbasis durchgeführt wird. Viele Verknüpfungen müssen jedoch feinkörniger sein und daher mit Unterpunkten eines bestimmten Objekts verknüpft werden. In der Part Workbench-Umgebung beispielsweise gehen viele Verknüpfungen zu speziellen Topologieeinheiten wie Vertices, Kanten oder Flächen. Die Stabilität dieser Verknüpfungen hängt von der genauen Benennung der Topologieelemente nach einer Neuberechnung ab. Dies ist derzeit innerhalb von freecad nicht gewährleistet, was nach einfachen Änderungen an einem Basisobjekt zu vielen Fehlern in den abhängigen Modellierungsschritten führen kann. Da die aktuelle Entwicklungsrichtung von FreeCAD zu einer stärkeren Verwendung dieser Verknüpfungen zu führen scheint, muss das Benennungsproblem gelöst werden.

Das GSoC Projekt zielt darauf ab, die Grundlage für die Lösung dieses Problems zu schaffen und den gewählten Ansatz an Testfällen zu beweisen. Der bevorzugte Ansatz zur Lösung des Problems wird beschrieben [hier](https://docs.google.com/document/d/1-d2JD8RH13ar7QPh_SpX2H5eiNND4DiCPBmGwA2R9Ug/edit), mit der Umsetzung wird begonnen [hier](https://github.com/ickby/FreeCAD_sf_master/tree/Naming).

## Details

1.  Mache dich mit Opencascade, dem geometrischen Modellierungskern von FreeCAD, vertraut und verstehe, wie die Topologiedatenstruktur funktioniert und wie Algorithmen die Topologie gemeinsam nutzen, ändern und generieren. Es ist wünschenswert, dass der Student bereits mit opencascade gearbeitet hat, da die Bibliothek komplex ist und der Einstieg in die Bibliothek viel Zeit in Anspruch nimmt.
2.  Mache dich mit dem Verknüpfungssystem von FreeCAD vertraut und wie es mit Topologieeinheiten in den Opencascade Datenstrukturen verknüpft ist. Es ist auch wichtig, die Verwendung von Occ in FreeCAD zu verstehen, die Verwendung einer speziellen Topologieklasse in Kombination mit der direkten Verwendung von Occ Algorithmen außerhalb dieser Klasse. Dieser duale Ansatz ist möglicherweise nicht ideal für die Lösung des Benennungsproblems, daher ist ein gutes Verständnis dafür erforderlich.
3.  Beginne mit der Implementierung einer Identifier Klasse, die die Entstehungsgeschichte einer Form speichert. Identifiziere alle Daten, die erforderlich sind, um sie eindeutig zu machen, und beschreibe die Schnittstelle.
4.  Integriere die Identifier Klasse in die Topologiedatenstruktur und portiere einige erste Algorithmen, um sie zu verwenden. Erweitere auch die Python Schnittstelle der Topologieklasse, um die Verwendung der Identifikatoren zum Extrahieren von Unterformen zu ermöglichen.
5.  Erstelle eine Reihe von Testfällen, um die Wirksamkeit der Implementierung zu zeigen.

## Erwartetes Ergebnis 

1.  Eine erste Implementierung innerhalb von FreeCAD, um den funktionierenden Algorithmus zu zeigen
2.  Eine Reihe von Testfällen, die in das verfügbare Testsystem integriert sind und die wichtige Fälle des topologischen Benennungsproblems und deren Lösung durch die Prototyp-Implementierung zeigen.

## Zukunftsmöglichkeiten

Wenn dieses Projekt erfolgreich abgeschlossen ist, kann eine vollständige Integration in den FreeCAD Quellcode Teil eines weiteren Beitrags oder sogar eines eigenen GSoC Projekts sein.

## Projekt Eigenschaften 

### Fähigkeiten

-   Programmiersprache C++
-   Tiefes Verständnis und Nutzung der APIs von FreeCAD und opencascade
-   Lesen und Verstehen von wissenschaftlichen Texten und Arbeiten
-   Kenntnisse der 3D Modellierung, Topologie und Berechnungsgeometrie sind ein Plus

### Schwierigkeit

Hart

### Zusätzliche Informationen 

[Category:Google Summer of Code](Category:Google_Summer_of_Code.md)

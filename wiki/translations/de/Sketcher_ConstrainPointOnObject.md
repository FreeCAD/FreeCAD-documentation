---
- GuiCommand:/de
   Name:Sketcher ConstrainPointOnObject
   Name/de:Sketcher PunktAufObjektFestlegen
   MenuLocation:Sketch → Skizzen-Beschränkungen → Punkt auf Objekt festlegen
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**O**
   SeeAlso:[Sketcher KoinzidentFestlegen](Sketcher_ConstrainCoincident/de.md)
---

# Sketcher ConstrainPointOnObject/de

## Beschreibung

Bringt einen Punkt an einem anderen Objekt an, z.B. einer Linie, einem Bogen oder einer Skizzenachse.

## Anwendung

1.  Einen Punkt und eine Kante in beliebiger Reihenfolge auswählen.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/Sketcher_ConstrainPointOnObject.svg style="width:16px"> [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md)** drücken.
    -   Das Tastaturkürzel **O**.
    -   Den Menüeintrag **Sketch → Skizzen-Beschränkungen → [<img src=images/Sketcher_ConstrainPointOnObject.svg style="width:16px"> Punkt auf Objekt festlegen** auswählen.

## Skripten

Die Randbedingung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus durch den folgenden Befehl erstellt werden:


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`

-    `Sketch`ist ein Skizzenobjekt

-    `LineMoving`ist die Nummer, die die Linie kennzeichnet, die den Punkt enthält, der auf die `LineFixed` (die Linie, die fixiert ist) verschoben werden soll.

-    `PointOfLineMoving`ist die Nummer des Knotens der Linie `LineMoving`, der sich auf die Linie `LineFixed` bewegen soll.

-    `LineFixed`ist die Nummer der Linie, an die der Punkt `PointOfLineMoving` befestigt werden soll.

Die Seite [Sketcher Skripten](Sketcher_scripting/de.md) erklärt, wie man die Zahlen zur Bestimmung von Linien und Punkten erkennt.





{{Sketcher Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject/de

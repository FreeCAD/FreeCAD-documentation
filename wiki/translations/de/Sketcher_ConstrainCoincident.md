---
- GuiCommand:/de
   Name:Sketcher ConstrainCoincident
   Name/de:Skizzierer KoinzidentFestlegen
   MenuLocation:Skizze → Skizzen-Beschränkungen → Koinzidenz festlegen
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**C**
   SeeAlso:[Sketcher Sperren](Sketcher_ConstrainLock/de.md), [Sketcher PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md)
---

# Sketcher ConstrainCoincident/de

## Beschreibung

Affixes a point onto (coincident with) one or more other points. <small>(v1.0)</small> : It acts as a concentric constraint if two or more circles, arcs, ellipses or arcs of ellipses are selected.

## Anwendung

1.  Do one of the following:
    -   Select two or more points.
    -   Select two or more edges of circles, arcs, ellipses or arcs of ellipses.
2.  There are several ways to invoke the command:
    -   Press the **[<img src=images/Sketcher_ConstrainCoincident.svg style="width:16px"> [Constrain coincident](Sketcher_ConstrainCoincident.md)** button in the toolbar.
    -   Use the **C** keyboard shortcut.
    -   Use the **Sketch → Sketcher constraints → [<img src=images/Sketcher_ConstrainCoincident.svg style="width:16px"> Constrain coincident** entry in the top menu.

## Alternativen zu Koinzident festlegen 

Die beiden Elemente einer Randbedingung [KoinzidentFestlegen](Sketcher_ConstrainCoincident/de.md) müssen Startpunkt- oder Endpunkt-Knoten oder Mittelpunkte von Bögen, Kreisen oder Ellipsen sein. Einige Kombinationen, die mit KoinzidentFestlegen nicht möglich sind, können mit anderen Randbedingungen emuliert werden:

-   Die Randbedingung <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [SymmetrieFestlegen](Sketcher_ConstrainSymmetric/de.md) kann verwendet werden, um einen Start-, End- oder Mittelpunkt auf den Mittelpunkt einer geraden Linie zu legen.
-   Eine Randbdingung Mittelpunkt-auf-Mittelpunkt zweier Geraden kann emuliert werden durch das Erstellen eines neuen <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:24px;"> [Punktes](Sketcher_CreatePoint/de.md) und zweimaliger Verwendung der Randbedingung <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [SymmetrischFestlegen](Sketcher_ConstrainSymmetric/de.md), so dass er auf den Mittelpunkten beider Linien liegt.
-   Ein Knoten kann mit einer Randbedingung <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md) so festgelegt werden, dass auf einer Kante liegt. Bei dieser Randbedingung kann der Punkt überall auf der vollen Ausdehnung eines Segments oder einer Kurve liegen (also auch vor dem Startpunkt oder hinter dem Endpunkt).
-   Eine kollineare (fluchtende) Platzierung zweier Geraden erhält man durch Anwendung einer Randbedingung <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> [TangentialFestlegen](Sketcher_ConstrainTangent/de.md) auf sie, oder durch die Kombination der Randbedingungen <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md) und <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;"> [ParallelFestlegen](Sketcher_ConstrainParallel/de.md).
-   Zwei Kanten können deckungsgleich platziert werden, indem die Randbedingung <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [KoinzidentFestlegen](Sketcher_ConstrainCoincident/de.md) zweimal angewendet wird, auf jeweils ein Paar von Extrempunkten (Start- oder Endpunkte).
-   Zwei Kreise können deckungsgleich platziert werden, indem man mit der Randbedingung <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [KoinzidentFestlegen](Sketcher_ConstrainCoincident/de.md) die Mittelpunkte zusammenführt und die Randbedingung <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;"> [GleichheitFestlegen](Sketcher_ConstrainEqual/de.md) auf ihre Kanten anwendet. Bei Bögen stellt dies sicher, dass beide Bögen Teil desselben Kreises sind, während sie unterschiedliche Start- und Endpunkte haben können.

## Skripten

Die Randbedingung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit dem folgenden Befehl erstellt werden:


```pythonSketch.addConstraint(Sketcher.Constraint('Coincident',LineFixed,PointOfLineFixed,LineMoving,PointOfLineMoving)) 
```

wobei :

-    `Sketch`ein Skizzenobjekt ist.

-    `LineFixed`die Nummer der Linie ist, die sich durch die Anwendung der Randbedingung nicht bewegt.

-    `PointOfLineFixed`bestimmt, welcher Knoten der Linie `LineFixed` die Randbedingung erfüllen muss.

-    `LineMoving`die Nummer der Zeile ist, die sich durch Anwendung der Randbedingung bewegt.

-    `PointOfLineMoving`bestimmt, welcher Knoten der Linie `LineMoving`, die Randbedingung erfüllen muss.

Wie die Namen `LineFixed` und `LineMoving` andeuten, bleibt, wenn sich beide beteiligten Knoten frei in jede Richtung bewegen können, der erste (in der GUI zuerst ausgewählte) fest und der andere bewegt sich. Sind jedoch weitere Randbedingungen vorhanden, dürfen sich beide Kanten bewegen.

Die Seite [Sketcher Skripten](Sketcher_scripting/de.md) erklärt die Werte, die für `LineFixed`, `PointOfLineFixed`, `LineMoving` und `PointOfLineMoving` verwendet werden können, und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincident/de

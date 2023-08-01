---
- GuiCommand:
   Name: Sketcher ConstrainCoincident
   Name/de: Skizzierer KoinzidentFestlegen
   MenuLocation: Skizze - Skizzen-Beschränkungen - Koinzidenz festlegen
   Workbenches: [Sketcher](Sketcher_Workbench/de.md)
   Shortcut: **C**
   SeeAlso: [Sketcher Sperren](Sketcher_ConstrainLock/de.md), [Sketcher PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md)
---

# Sketcher ConstrainCoincident/de



## Beschreibung

Verbindet einen Punkt deckungsgleich (koinzident) mit einem oder mehreren anderen Punkten. Neu in {{Version/de|0.21}}: Werden zwei oder mehr Kreise, Bögen, Ellipsen oder Ellipsenbögen ausgewählt, stellt dies eine Randbedingung \"Konzentrisch festlegen\" dar.



## Anwendung

1.  Eine der folgenden Möglichkeiten ausführen:
    -   Zwei oder mehr Punkte auswählen
    -   Zwei oder mehr Kanten von Kreisen, Bögen, Ellipsen oder Ellipsenbögen auswählen.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **[<img src=images/Sketcher_ConstrainCoincident.svg style="width:16px"> [Koinzidenz festlegen](Sketcher_ConstrainCoincident/de.md)** in der Symbolleiste drücken.
    -   Das Tastaturkürzel **C**.
    -   Den Menüeintrag **Skizze → Skizzen-Beschränkungen → [<img src=images/Sketcher_ConstrainCoincident.svg style="width:16px"> Koinzidenz festlegen** auswählen.



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
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincident/de

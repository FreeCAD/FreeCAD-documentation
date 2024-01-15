# Sketcher scripting/de
## Erstellen eines Sketch-Objekts mit Python 

So wird ein Sketch-Objekt erstellt:


```python
import FreeCAD as App
import Part
import Sketcher

doc = App.newDocument()  

sketch = doc.addObject("Sketcher::SketchObject", "Sketch")
sketch.addGeometry(Part.LineSegment(App.Vector(1.2, 1.8, 0),
                                    App.Vector(5.2, 5.3, 0)), False)
sketch.addGeometry(Part.LineSegment(App.Vector(6.5, 1.5, 0),
                                    App.Vector(10.2, 5.0, 0)), False)
sketch.addGeometry(Part.LineSegment(App.Vector(12.2, 1.0, 0),
                                    App.Vector(15.4, 5.0, 0)), False)

doc.recompute()
```

Es werden der neu erstellten Skizze auch noch drei [Linien](Topological_data_scripting/de#Linie.md) hinzugefügt.



## Erstellen einer Randbedingung mit Python 

Die geometrischen Randbedingungen <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> und <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:24px;"> können mit Makros und von der Python-Konsole aus durch Verwendung des folgenden Befehls erstellt werden:


```pythonsketch.addConstraint(Sketcher.Constraint(ConstraintType, EdgeOrPartOfEdge…)) 
```

Die maßlichen Randbedingungen <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:24px;"> und die spezielle Randbedingung <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> [Lichtbrechung (nach Snellius-Gesetz) festlegen](Sketcher_ConstrainSnellsLaw/de.md) können mit Makros und von der Python-Konsole aus durch Verwendung des folgenden Befehls erstellt werden:


```pythonsketch.addConstraint(Sketcher.Constraint(DimensionalConstraintType, EdgeOrPartOfEdge…, App.Units.Quantity("float_value unit"))) 
```

z\. B.


```pythonsketch.addConstraint(Sketcher.Constraint(DimensionalConstraintType, EdgeOrPartOfEdge…, App.Units.Quantity("123.0 mm"))) 
```

Das erste Argument `ConstraintType` wird weiter unten unter [Arten von Randbedingungen](#Arten_von_Randbedingungen.md) beschrieben.

Eine Randbedingung kann bis zu sechs Argumente besitzen; das können Kanten sein oder Angaben, welcher Bestandteil einer Kante von der Randbedingung verwendet wird. In den Dokumentationen der einzelnen Randbedingungen findet man Details zu den Kombinationen von Kanten und Bestandteilen von Kanten, die als Argumente übergeben werden können. Das Hauptproblem bei dieser Funktion besteht darin, die Liniennummer und die Knotennummer der zu bearbeitenden Linien korrekt zu identifizieren. Die folgenden Abschnitte beschreiben, wie man die [Nummerierung einer Linie](#Identifizierung_der_Nummerierung_einer_Linie.md) und die [Nummerierung der Bestandteile einer Linie](#Identifizierung_der_Nummerierung_der_Abschnittsteile_einer_Linie.md) herausfindet.



## Arten von Randbedingungen 

Bei geometrischen Randbedingungen ist das erste Argument eines der folgenden. Die möglichen Kombinationen von Argumenten, die für jede Beschränkung zulässig sind, findet man auf der Referenzseite der zugehörigen Funktion.

++++
| Schlüsselwort              | Symbol                                                                                     | Funktion                                                                    |
+============================+============================================================================================+=============================================================================+
|             | <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;">       | [Koinzidenz festlegen](Sketcher_ConstrainCoincident/de.md)          |
| `"Coincident"`    |                                                                                            |                                                                             |
|                         |                                                                                            |                                                                             |
++++
|             | <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> | [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md) |
| `"PointOnObject"` |                                                                                            |                                                                             |
|                         |                                                                                            |                                                                             |
++++
|             | <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:24px;">           | [Vertikal festlegen](Sketcher_ConstrainVertical/de.md)              |
| `"Vertical"`      |                                                                                            |                                                                             |
|                         |                                                                                            |                                                                             |
++++
|             | <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;">       | [Horizontal festlegen](Sketcher_ConstrainHorizontal/de.md)          |
| `"Horizontal"`    |                                                                                            |                                                                             |
|                         |                                                                                            |                                                                             |
++++
|             | <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;">           | [Parallel festlegen](Sketcher_ConstrainParallel/de.md)              |
| `"Parallel"`      |                                                                                            |                                                                             |
|                         |                                                                                            |                                                                             |
++++
|             | <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:24px;"> | [Rechtwinklig festlegen](Sketcher_ConstrainPerpendicular/de.md)     |
| `"Perpendicular"` |                                                                                            |                                                                             |
|                         |                                                                                            |                                                                             |
++++
|             | <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;">             | [Tangential festlegen](Sketcher_ConstrainTangent/de.md)             |
| `"Tangent"`       |                                                                                            |                                                                             |
|                         |                                                                                            |                                                                             |
++++
|             | <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;">                 | [Gleichheit festlegen](Sketcher_ConstrainEqual/de.md)               |
| `"Equal"`         |                                                                                            |                                                                             |
|                         |                                                                                            |                                                                             |
++++
|             | <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;">         | [Symmetrie festlegen](Sketcher_ConstrainSymmetric/de.md)            |
| `"Symmetric"`     |                                                                                            |                                                                             |
|                         |                                                                                            |                                                                             |
++++
|             | <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:24px;">                 | [Fixieren](Sketcher_ConstrainBlock/de.md)                           |
| `"Block"`         |                                                                                            |                                                                             |
|                         |                                                                                            |                                                                             |
++++

Bei maßlichen Randbedingungen ist das erste Argument eines der folgenden. Die möglichen Kombinationen von Argumenten, die für jede Randbedingung zulässig sind, findet man auf der Referenzseite der zugehörigen Funktion.

++++
| Schlüsselwort              | Symbol                                                                             | Funktion                                                                    |
+============================+====================================================================================+=============================================================================+
|             | <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> | [Horizontalen Abstand festlegen](Sketcher_ConstrainDistanceX/de.md) |
| `"DistanceX"`     |                                                                                    |                                                                             |
|                         |                                                                                    |                                                                             |
++++
|             | <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> | [Vertikalen Abstand festlegen](Sketcher_ConstrainDistanceY/de.md)   |
| `"DistanceY"`     |                                                                                    |                                                                             |
|                         |                                                                                    |                                                                             |
++++
|             | <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;">   | [Abstand festlegen](Sketcher_ConstrainDistance/de.md)               |
| `"Distance"`      |                                                                                    |                                                                             |
|                         |                                                                                    |                                                                             |
++++
|             | <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:24px;">       | [Radius oder Gewicht festlegen](Sketcher_ConstrainRadius/de.md)     |
| `"Radius"`        |                                                                                    |                                                                             |
|                         |                                                                                    |                                                                             |
++++
|             | <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:24px;">   | [Durchmesser festlegen](Sketcher_ConstrainDiameter/de.md)           |
| `"Diameter"`      |                                                                                    |                                                                             |
|                         |                                                                                    |                                                                             |
++++
|             | <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:24px;">         | [Winkel festlegen](Sketcher_ConstrainAngle/de.md)                   |
| `"Angle"`         |                                                                                    |                                                                             |
|                         |                                                                                    |                                                                             |
++++
|             | <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:24px;">         | [Winkel festlegen](Sketcher_ConstrainAngle/de.md)                   |
| `"AngleViaPoint"` |                                                                                    |                                                                             |
|                         |                                                                                    |                                                                             |
++++

Die Randbedingung <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> [Lichtbrechung (nach Snellius-Gesetz) festlegen](Sketcher_ConstrainSnellsLaw/de.md) verhält sich im Zusammenhang mit der Skripterstellung wie eine maßliche Randbedingung. Auch hier findet man auf der zugehörigen Referenzseite die möglichen Kombinationen von Argumenten, die für diese Randbedingung zulässig sind.

++++
| Schlüsselwort          | Symbol                                                                             | Funktion                                                                                    |
+========================+====================================================================================+=============================================================================================+
|         | <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> | [Lichtbrechung (nach Snellius-Gesetz) festlegen](Sketcher_ConstrainSnellsLaw/de.md) |
| `"SnellsLaw"` |                                                                                    |                                                                                             |
|                     |                                                                                    |                                                                                             |
++++

Die Randbedingung <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Sperren](Sketcher_ConstrainLock/de.md) ist ein GUI-Befehl, der die Randbedingungen <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontalen Abstand festlegen](Sketcher_ConstrainDistanceX/de.md) und <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Vertikalen Abstand festlegen](Sketcher_ConstrainDistanceY/de.md) erstellt; sie ist keine eigenständige Randbedingung.



## Identifizierung der Nummerierung einer Linie 

Ich habe drei Linien gezeichnet, wie in der folgenden Abbildung dargestellt.

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure1.jpg  style="width:600px;">

Durch bewegen des Mauszeigers über die Linie, lässt sich die Liniennummer unten links im FreeCAD Fenster anzeigen, siehe nächste Abbildung.

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure2.jpg  style="width:600px;">

Leider beginnt die im FreeCAD-Fenster angezeigte Nummerierung bei 1, während die Nummerierung der Linien, die für das Skript verwendet wird, bei 0 beginnt: Das bedeutet, dass jedes Mal eins abgezogen werden muss, wenn man auf eine Linie verweisen möchte.

Positive Zahlen bezeichnen Skizzenkanten (Geraden, Kreise, Kegelschnitte, B-Splines usw.). Die folgenden Werte können verwendet werden, um Elemente zu kennzeichnen, die keine Skizzenkanten sind:

-    `-1`bezeichnet die horizontale X-Achse

-    `-2`bezeichnet die vertikale Y-Achse

-    `-n`bezeichnet die Nummer des externen Geometrieelements `n-3` (z. B. würde das externe Geometrieelement mit Index 0 in der reduzierten Liste `Sketch.ExternalGeometry` mit -3 bezeichnet, das folgende Element in der reduzierten Liste mit -4 usw.).



## Identifizierung der Nummerierung der Bestandteile einer Linie 

Um festzulegen, welcher Bestandteile einer Linie von einer Randbedingung betroffen ist, können die folgenden Werte verwendet werden:

-    `0`, um anzugeben, dass die Randbedingung die gesamte Kante betrifft.

-    `1`, um anzugeben, dass die Randbedingung den Anfangspunkt der Kante betrifft (ein Vollkreis hat keinen Anfangspunkt).

-    `2`, um anzugeben, dass die Randbedingung den Endpunkt der Kante betrifft.

-    `3`, um anzugeben, dass die Randbedingung den Mittelpunkt der Kante betrifft. Für <img alt="" src=images/Sketcher_CompCreateCircle.png  style="width:" height="24px;"> [Kreise](Sketcher_CompCreateCircle/de.md) und <img alt="" src=images/Sketcher_CompCreateConic.png  style="width:" height="24px;"> [Kegelschnitte](Sketcher_CompCreateConic/de.md) (Ellipsen) ist dies der Mittelpunkt des Kreises bzw. das Zentrum (Schnittpunkt von Haupt- und Nebenachse) der Ellipse. Bei geraden <img alt="" src=images/Sketcher_CreateLine.svg  style="width:" height="24px;"> [Linien](Sketcher_CreateLine/de.md) kann `3` nicht zur Angabe des Mittelpunktes verwendet werden.

-    `n`, um anzugeben, dass die Randbedingung den n-ten Kontrollpunkt eines <img alt="" src=images/Sketcher_CompCreateBSpline.png  style="width:" height="24px;"> [B-Splines](Sketcher_CompCreateBSpline/de.md) betrifft.

Die mit 1 und 2 gekennzeichneten Knoten sind in der Reihenfolge ihrer Erstellung nummeriert. Um die Reihenfolge ihrer Erstellung herauszufinden (sind viele Linien vorhanden, kann es schwierig werden sich zu erinnern, welcher Knoten zuerst erstellt wurde), musst nur der Mauszeiger über die beiden Knoten einer Linie bewegt werden, siehe folgende Abbildung.

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure3.jpg  style="width:600px;">

Liest man z. B. 4 und 5, bedeutet dies, dass der Knoten mit der niedrigeren Nummer (4 in diesem Beispiel) mit der Nummer 1 (zuerst im Skriptbefehl) und der Knoten mit der höheren Nummer (5 in diesem Beispiel) mit der Nummer 2 im Skriptbefehl referenziert wird.



## Beispiel

Nehmen wir das vorherige Beispiel der drei Linien. Die nachfolgende Abbildung zeigt die Nummerierung der einzelnen Linien und ihrer Knoten gemäß der Konvention für die Skripterstellung.

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure3Bis.jpg  style="width:600px;">



*<b>blauer Text:</b> Nummerierung der Linie, <b>schwarzer Text:</b> Nummerierung der Knoten*

Der Befehl `sketch.addConstraint(Sketcher.Constraint("Coincident", 1, 2, 2, 1))` ergibt folgendes Ergebnis:

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure4.jpg  style="width:600px;">

Der gesamte Kode zum Zeichnen der drei Linien und der Anwendung der Randbedingung \"Coincident\" auf zwei Punkte von zwei Linien sieht ungefähr so aus:


```python
import FreeCAD as App
import Part
import Sketcher

doc = App.newDocument()  

sketch = doc.addObject("Sketcher::SketchObject", "Sketch")
sketch.addGeometry(Part.LineSegment(App.Vector(1.2, 1.8, 0),
                                    App.Vector(5.2, 5.3, 0)), False)
sketch.addGeometry(Part.LineSegment(App.Vector(6.5, 1.5, 0),
                                    App.Vector(10.2, 5.0, 0)), False)
sketch.addGeometry(Part.LineSegment(App.Vector(12.2, 1.0, 0),
                                    App.Vector(15.4, 5.0, 0)), False)
sketch.addConstraint(Sketcher.Constraint("Coincident", 1, 2, 2, 1))

doc.recompute()
```


{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher scripting/de

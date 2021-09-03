 {{TOCright}}

## Erstellen einer Beschränkung mit Python 

Eine geometrische Beschränkung <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:24px;"> und die spezielle <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width:24px;"> [InterneAusrichtungsbeschränkungen](Sketcher_ConstrainInternalAlignment/de.md) können von Makros und von der Python Konsole aus durch Verwendung des folgenden Befehls erstellt werden:


```pythonSketch.addConstraint(Sketcher.Constraint(ConstraintType, EdgeOrPartOfEdge…)) 
```

Eine maßliche Beschränkung <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:24px;"> und die spezielle Beschränkung <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> [Snelliusches Gesetz](Sketcher_ConstrainSnellsLaw/de.md) kann von Makros und von der Python Konsole aus durch Verwendung des folgenden Befehls erstellt werden:


```pythonSketch.addConstraint(Sketcher.Constraint(DimensionalConstraintType, EdgeOrPartOfEdge…, App.Units.Quantity('float_value unit'))) 
```


:   e.g.


```pythonSketch.addConstraint(Sketcher.Constraint(DimensionalConstraintType, EdgeOrPartOfEdge…, App.Units.Quantity('123.0 mm'))) 
```

Das erste Argument `Beschränkungstyp` wird weiter unten in [Beschränkungstypen](#Beschränkungstypen.md) beschrieben.

Eine Beschränkung kann bis zu sechs Argumente annehmen, die Kanten sind oder angeben, welches Abschnittsteil einer Kante von der Beschränkung verwendet wird. In der Dokumentation der einzelnen Beschränkungen findest du Details darüber, welche Kombinationen von Kanten und Unterteilen von Kanten als Argumente übergeben werden können. Das Hauptproblem bei dieser Funktion besteht darin, die Zeilennummer und die Knotennummer der zu bearbeitenden Linien korrekt zu identifizieren. Die folgenden Abschnitte beschreiben, wie man [Identifiziere die Nummerierung einer Linie](#Identifizierung_der_Nummerierung_einer_Linie.md)) und wie man [Identifiziere die Nummerierung der Unterteile einer Linie](#Identifizierung_der_Nummerierung_der_Abschnittsteile_einer_Linie.md)).

## Beschränkungstypen

Bei geometrischen Beschränkungen ist das erste Argument eines der folgenden. Die möglichen Kombinationen von Argumenten, die für jede Beschränkung zulässig sind, findest du auf der entsprechenden Funktionsseite.

+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| Code                       | Icon                                                                                       | Feature                                                       |
+============================+============================================================================================+===============================================================+
|             | <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;">       | [Coincident](Sketcher_ConstrainCoincident.md)         |
| `'Coincident'`    |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> | [Point On Object](Sketcher_ConstrainPointOnObject.md) |
| `'PointOnObject'` |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:24px;">           | [Vertical](Sketcher_ConstrainVertical.md)             |
| `'Vertical'`      |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;">       | [Horizontal](Sketcher_ConstrainHorizontal.md)         |
| `'Horizontal'`    |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;">           | [Parallel](Sketcher_ConstrainParallel.md)             |
| `'Parallel'`      |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:24px;"> | [Perpendicular](Sketcher_ConstrainPerpendicular.md)   |
| `'Perpendicular'` |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;">             | [Tangent](Sketcher_ConstrainTangent.md)               |
| `'Tangent'`       |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;">                 | [Equal](Sketcher_ConstrainEqual.md)                   |
| `'Equal'`         |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;">         | [Symmetric](Sketcher_ConstrainSymmetric.md)           |
| `'Symmetric'`     |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:24px;">                 | [Block](Sketcher_ConstrainBlock.md)                   |
| `'Block'`         |                                                                                            |                                                               |
|                         |                                                                                            |                                                               |
+----------------------------+--------------------------------------------------------------------------------------------+---------------------------------------------------------------+

Die <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width:24px;"> [InterneAusrichtungsbeschränkungen](Sketcher_ConstrainInternalAlignment/de.md) verhalten sich für die Zwecke der Skripterstellung wie geometrische Beschränkungen. Auch hier findest du auf der entsprechenden Funktionsseite die möglichen Kombinationen von Argumenten, die für jede Beschränkung zulässig sind.

+-----------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| Code                                                | Icon                                                                                               | Feature                                                             |
+=====================================================+====================================================================================================+=====================================================================+
|                                      | <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width:24px;"> | [InternalAlignment](Sketcher_ConstrainInternalAlignment.md) |
| `'InternalAlignment:EllipseMajorDiameter'` |                                                                                                    |                                                                     |
|                                                  |                                                                                                    |                                                                     |
+-----------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
|                                      | <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width:24px;"> | [InternalAlignment](Sketcher_ConstrainInternalAlignment.md) |
| `'InternalAlignment:EllipseMinorDiameter'` |                                                                                                    |                                                                     |
|                                                  |                                                                                                    |                                                                     |
+-----------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
|                                      | <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width:24px;"> | [InternalAlignment](Sketcher_ConstrainInternalAlignment.md) |
| `'InternalAlignment:EllipseFocus1'`        |                                                                                                    |                                                                     |
|                                                  |                                                                                                    |                                                                     |
+-----------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
|                                      | <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width:24px;"> | [InternalAlignment](Sketcher_ConstrainInternalAlignment.md) |
| `'InternalAlignment:EllipseFocus2'`        |                                                                                                    |                                                                     |
|                                                  |                                                                                                    |                                                                     |
+-----------------------------------------------------+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

Bei Bemaßungsbeschränkungen ist das erste Argument eines der folgenden. Die möglichen Kombinationen von Argumenten, die für jede Beschränkung zulässig sind, findest du auf der entsprechenden Funktionsseite.

+----------------------------+------------------------------------------------------------------------------------+---------------------------------------------------------------+
| Code                       | Icon                                                                               | Feature                                                       |
+============================+====================================================================================+===============================================================+
|             | <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> | [Horizontal distance](Sketcher_ConstrainDistanceX.md) |
| `'DistanceX'`     |                                                                                    |                                                               |
|                         |                                                                                    |                                                               |
+----------------------------+------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> | [Vertical distance](Sketcher_ConstrainDistanceY.md)   |
| `'DistanceY'`     |                                                                                    |                                                               |
|                         |                                                                                    |                                                               |
+----------------------------+------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;">   | [Distance](Sketcher_ConstrainDistance.md)             |
| `'Distance'`      |                                                                                    |                                                               |
|                         |                                                                                    |                                                               |
+----------------------------+------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:24px;">       | [Radius](Sketcher_ConstrainRadius.md)                 |
| `'Radius'`        |                                                                                    |                                                               |
|                         |                                                                                    |                                                               |
+----------------------------+------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:24px;">   | [Diameter](Sketcher_ConstrainDiameter.md)             |
| `'Diameter'`      |                                                                                    |                                                               |
|                         |                                                                                    |                                                               |
+----------------------------+------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:24px;">         | [Angle](Sketcher_ConstrainAngle.md)                   |
| `'Angle'`         |                                                                                    |                                                               |
|                         |                                                                                    |                                                               |
+----------------------------+------------------------------------------------------------------------------------+---------------------------------------------------------------+
|             | <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:24px;">         | [Angle](Sketcher_ConstrainAngle.md)                   |
| `'AngleViaPoint'` |                                                                                    |                                                               |
|                         |                                                                                    |                                                               |
+----------------------------+------------------------------------------------------------------------------------+---------------------------------------------------------------+

Die <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> [Snelliusches Gesetz](Sketcher_ConstrainSnellsLaw/de.md) Beschränkungen verhalten sich für die Zwecke der Skripterstellung wie Bemaßungsbeschränkungen. Auch hier findest du auf der entsprechenden Funktionsseite die möglichen Kombinationen von Argumenten, die für jede Beschränkung zulässig sind.

+------------------------+------------------------------------------------------------------------------------+--------------------------------------------------------+
| Code                   | Icon                                                                               | Feature                                                |
+========================+====================================================================================+========================================================+
|         | <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> | [Snell\'s law](Sketcher_ConstrainSnellsLaw.md) |
| `'SnellsLaw'` |                                                                                    |                                                        |
|                     |                                                                                    |                                                        |
+------------------------+------------------------------------------------------------------------------------+--------------------------------------------------------+

Die <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Schloss](Sketcher_ConstrainLock/de.md) Beschränkung ist ein GUI Befehl, der eine <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> [Horizontaler Abstand](Sketcher_ConstrainDistanceX/de.md) und eine <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> [Vertikaler Abstandsbeschränkung](Sketcher_ConstrainDistanceY/de.md) erzeugt, es ist keine eigene Beschränkung.

## Identifizierung der Nummerierung einer Linie 

Ich habe drei Linien gezeichnet, wie in der folgenden Abbildung dargestellt.

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure1.jpg  style="width:600px;">

Durch bewegen des Mauszeigers über die Linie, kannst du die Zeilennummer unten links im FreeCAD Fenster sehen, siehe nächste Abbildung.

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure2.jpg  style="width:600px;">

Leider beginnt die angezeigte Nummerierung in den FreeCAD Fenstern bei 1, während die Nummerierung der Linie, die für das Skript verwendet wird, bei 0 beginnt: Das bedeutet, dass du jedes Mal, wenn du dich auf eine Zeile beziehen willst, eine Zahl abziehen musst.

Positive Zahlen bezeichnen Skizzenkanten (Geraden, Kreise, Kegel, B-Splines usw.). Die folgenden Werte können verwendet werden, um Elemente zu kennzeichnen, die keine Skizzenkanten sind:

-    `-1`bezeichnet die horizontale x Achse

-    `-2`bezeichnet die vertikale y Achse

-    `-n`bezeichnet die externe Geometrieelementnummer `n-3` (z. B. würde das externe Geometrieelement mit Index 0 in der reduzierten Liste `App.ActiveDocument.Sketch.ExternalGeometry` mit -3 bezeichnet, das folgende Element in der reduzierten Liste mit -4 usw.).

## Identifizierung der Nummerierung der Abschnittsteile einer Linie 

Um festzulegen, welcher Teil einer Linie von einer Beschränkung betroffen ist, kannst du die folgenden Werte verwendet werden:

-    `0`, um anzugeben, dass die Beschränkung die gesamte Kante betrifft.

-    `1`, um anzuzeigen, dass die Beschränkung den Anfangspunkt der Kante betrifft (ein Vollkreis hat keinen Anfangspunkt).

-    `2`, um anzuzeigen, dass die Beschränkung den Endpunkt der Kante betrifft.

-    `3`, um anzuzeigen, dass die Beschränkung den Mittelpunkt der Kante betrifft. Für <img alt="" src=images/Sketcher_CompCreateCircle.png  style="width:24px;">[Kreise](Sketcher_CompCreateCircle/de.md) und <img alt="" src=images/Sketcher_CompCreateConic.png  style="width:24px;">[Kegel](Sketcher_CompCreateConic/de.md) (Ellipsen) ist dies der Mittelpunkt des Kreises bzw. das Zentrum (Schnittpunkt von Haupt- und Nebenachse) der Ellipse. Bei geraden <img alt="" src=images/Sketcher_CreateLine.svg  style="width:24px;">[Linien](Sketcher_CreateLine/de.md) kann `3` nicht zur Angabe des Mittelpunktes verwendet werden.

-    `n`, um anzuzeigen, dass die Beschränkung den n-ten Pol eines <img alt="" src=images/Sketcher_CreateBSpline.png  style="width:24px;">[B-Spline](Sketcher_CompCreateBSpline/de.md) betrifft.

Die mit 1 und 2 gekennzeichneten Knoten sind in der Reihenfolge ihrer Erstellung nummeriert. Um die Reihenfolge ihrer Erstellung herauszufinden (wenn du viele Linien hast, kannst du dich nicht erinnern, welchen Knoten du zuerst erstellt hast), musst du nur den Mauszeiger über die beiden Knoten einer Linie bewegen, siehe folgende Abbildung.

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure3.jpg  style="width:600px;">

Wenn du z. B. 4 und 5 liest, bedeutet dies, dass der Knoten mit der niedrigeren Nummer (4 in diesem Beispiel) mit der Nummer 1 (zuerst im Skriptbefehl) und der Knoten mit der höheren Nummer (5 in diesem Beispiel) mit der Nummer 2 im Skriptbefehl referenziert wird.

## Beispiel

Nehmen wir das vorherige Beispiel der drei Linien. Die nachfolgende Abbildung zeigt die Nummerierung der einzelnen Linien und deren Knoten gemäß der Konvention für die Skripterstellung.

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure3Bis.jpg  style="width:600px;"> 
*<b>blauer Text:</b> Nummerierung der Linie, <b>svhwarzer Text:</b> Nummerierung der Knoten*

Der Befehl `Sketch.addConstraint(Sketcher.Constraint('Coincident',1,2,2,1))` ergibt folgendes Ergebnis:

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure4.jpg  style="width:600px;">

Der Befehl `Sketch.addConstraint(Sketcher.Constraint('Coincident',0,2,2,2))` ergibt folgendes Ergebnis:

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure5.jpg  style="width:600px;">


{{Sketcher Tools navi

}} 

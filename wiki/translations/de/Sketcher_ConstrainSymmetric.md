---
- GuiCommand   */de
   Name   *Sketcher ConstrainSymmetric
   Name/de   *Sketcher SymmetrieFestlegen
   MenuLocation   *Sketch → Skizzen-Beschränkungen → Symmetrie festlegen
   Workbenches   *[Sketcher](Sketcher_Workbench/de.md)
   Shortcut   ***S**
   SeeAlso   *[Sketcher ParallelFestlegen](Sketcher_ConstrainParallel/de.md)
---

# Sketcher ConstrainSymmetric/de

## Beschreibung

Die **symmetrische Beschränkung** zwingt zwei ausgewählte Punkte dazu, symmetrisch um eine gegebene Linie herum zu sein, d.h. beide ausgewählten Punkte müssen auf einer Normalen zu der durch beide Punkte verlaufenden Linie liegen und müssen gleich weit von der Linie entfernt sein. Alternativ können zwei Punkte so eingeschränkt werden, dass sie in Bezug auf einen dritten Punkt symmetrisch sind.

## Anwendung

<img alt="" src=images/SymmetricConstraint1.png  style="width   *500px;">

Nach der Auswahl zweier Punkte (Scheitelpunkte) und einer Linie in der Skizze werden die ausgewählten Punkte und die Linie dunkelgrün dargestellt.

<img alt="" src=images/SymmetricConstraint2.png  style="width   *500px;">

Klicke auf **[<img src=images/Sketcher_ConstrainSymmetric.svg style="width   *16px"> [[Sketcher_ConstrainSymmetric/de|
Beschränke Symmetrisch]]** oder wähle den Menüpunkt Symmetrisch beschränken aus dem Untermenü Skizzierer Beschränkungen des Menübefehls Skizzierer (oder Part Design).

Dadurch wird die Beschränkung auf die ausgewählten Elemente angewendet.

<img alt="" src=images/SymmetricConstraint3.png  style="width   *500px;">


**Note   ***

Vor Version 0.19 (siehe Fix [1](https   *//github.com/FreeCAD/FreeCAD/pull/3746)), wenn du eine Symmetriebeschränkung in Bezug auf einen Punkt definieren willst, ist die Reihenfolge der Auswahl wichtig, je nachdem, ob du das Werkzeug am Anfang oder am Ende auswählst.

-   Wenn du das Werkzeug zuerst anklickst   * Wähle den ersten Punkt, dann den Symmetriereferenzpunkt und schließlich den zweiten Punkt.
-   Wenn du zuletzt auf das Werkzeug klickst   * Wähle den ersten Punkt, dann den zweiten Punkt und zuletzt den Symmetriereferenzpunkt.

Siehe den Tracker [issue#4144](https   *//freecadweb.org/tracker/view.php?id=4144) und [forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=39611).

## Skripten

Zwei Punkte und eine Symmetrielinie   *


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, SymmetryLine))```

Zwei Punkte und ein Symmetriepunkt   *


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line1, PointOfLine1, Line2, PointOfLine2, LineS, PointOfLineS))```

Eine Linie und ein Symmetriepunkt (In der GUI kann man eine Linie und einen Punkt auswählen, aber es wird intern die gleiche Form wie oben verwendet, mit den beiden Endpunkten der gleichen Linie)   *


```pythonSketch.addConstraint(Sketcher.Constraint('Symmetric', Line, 1, Line, 2, LineS, PointOfLineS))```

Die [Skizzierer Skripten](Sketcher_scripting.md) Seite erklärt die Werte, die für `Linie1`, `Linie2`, `LinieS`, `Linie`, `PunktVonLinie1`, `PunktVonLinie2` und `PunktVonLinieS` verwendet werden können, und enthält weitere Beispiele, wie man Beschränkungen aus Python Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSymmetric/de

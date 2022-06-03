---
- GuiCommand   */de
   Name   *Sketcher ConstrainParallel
   Name/de   *Sketcher ParallelFestlegen
   MenuLocation   *Sketch → Skizzen-Beschränkungen → Parallelität erzwingen
   Workbenches   *[Sketcher](Sketcher_Workbench/de.md)
   Shortcut   ***P**
   SeeAlso   *[Sketcher VertikalFestlegen](Sketcher_ConstrainVertical/de.md), [Sketcher HorizontalFestlegen](Sketcher_ConstrainHorizontal/de.md)
---

# Sketcher ConstrainParallel/de

## Beschreibung

Die Randbedingung ParallelFestlegen legt die Parallelität zweier ausgewählter gerader Linien oder Kanten zueinander fest.

## Erstellung

Die Skizze enthält zwei zufällig ausgerichtete Linien.

<img alt="" src=images/ConstrainParallel1.png  style="width   *500px;">



*Wähle beide Linien aus, indem Du nacheinander auf jede von ihnen klickst.*

<img alt="" src=images/ConstrainParallel2.png  style="width   *500px;">


<div class="mw-translate-fuzzy">

Wende die Beschränke Parallelbeschränkung entweder durch   *

-   Drücken der **[<img src=images/Sketcher_ConstrainParallel.svg style="width   *16px"> [Parallel beschränken](Sketcher_ConstrainParallel.md)** Schaltfläche in der Skizzierer Beschränkungen Werkzeugleiste, durch Wahl des Beschränkung Parallel Menüelements im Skizzierer Beschränkungen Untermenü des Skizzierers (Skizzierer Arbeitsbereich ausgewählt) oder Part Design (Part Design Arbeitsbereich ausgewählt) Menüelements.
-   Verwende das Tastaturkürzel **Umschalt** + **P**.
-   Verwende den {{MenuCommand/de|Skizze → Skizzierer Beschränkungen → Parallel beschränken}} Eintrag aus dem oberen Menü.


</div>

<img alt="" src=images/ConstrainParallel3.png  style="width   *500px;">



*Ergebnis   * Die ausgewählten Linien werden gezwungen, parallel zueinander zu verlaufen. Wenn du die Ausrichtung einer Linie änderst, ändert sich die Ausrichtung der anderen Linie, so dass sie gleich bleibt.*

## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Parallel', Line1, Line2))```

Die [Skizzierer Skripten](Sketcher_scripting/de.md)-Seite erklärt die Werte, die für `Line1` und `Line2` verwendet werden können und enthält weitere Beispiele, wie man Beschränkungen aus Python-Skripten erstellt.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainParallel/de

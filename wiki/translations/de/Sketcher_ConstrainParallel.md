---
 GuiCommand:
   Name: Sketcher ConstrainParallel
   Name/de: Sketcher ParallelFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Parallel festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **P**
   SeeAlso: Sketcher_ConstrainVertical/de, Sketcher_ConstrainHorizontal/de
---

# Sketcher ConstrainParallel/de



## Beschreibung

Die Randbedingung ParallelFestlegen legt die Parallelität zweier ausgewählter gerader Linien oder Kanten zueinander fest.



## Erstellung

Die Skizze enthält zwei zufällig ausgerichtete Linien.

<img alt="" src=images/ConstrainParallel1.png  style="width:500px;">



*Wähle beide Linien aus, indem Du nacheinander auf jede von ihnen klickst.*

<img alt="" src=images/ConstrainParallel2.png  style="width:500px;">

Es gibt mehrere Möglichkeiten die Randbedingung ParallelFestlegen aufzurufen:

-   Die Schaltfläche **[<img src=images/Sketcher_ConstrainParallel.svg style="width:16px"> [Parallel festlegen](Sketcher_ConstrainParallel.md)** der Sketcher-Werkzeugleiste Sketcher-Randbedingungen drücken.
-   Das Tastaturkürzel **P**.
-   Den Menüeintrag **Skizze → Sketcher-Randbedingungen → [<img src=images/Sketcher_ConstrainParallel.svg style="width:16px"> Parallel festlegen** auswählen.

<img alt="" src=images/ConstrainParallel3.png  style="width:500px;">



*Ergebnis: Die ausgewählten Linien werden gezwungen, parallel zueinander zu verlaufen. Wird die Ausrichtung einer Linie geändert, ändert sich auch die der anderen Linie, so dass beide Ausrichtungen gleich bleiben.*



## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Parallel', Line1, Line2))```

Die Seite [Sketcher Skripterstellung](Sketcher_scripting/de.md) erklärt die Werte, die für `Line1` und `Line2` verwendet werden können und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainParallel/de

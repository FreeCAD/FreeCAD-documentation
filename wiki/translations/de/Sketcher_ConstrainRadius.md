---
- GuiCommand   */de
   Name   *Sketcher ConstrainRadius
   Name/de   *Sketcher RadiusFestlegen
   MenuLocation   *Sketch → Skizzen-Beschränkungen → Radius oder Gewicht festlegen
   Workbenches   *[Sketcher](Sketcher_Workbench/de.md)
   Shortcut   ***K** **R**
   SeeAlso   *[Sketcher AbstandFestlegen](Sketcher_ConstrainDistance/de.md), [Sketcher XAbstandFestlegen](Sketcher_ConstrainDistanceX/de.md), [Sketcher YAbstandFestlegen](Sketcher_ConstrainDistanceY/de.md)
---

# Sketcher ConstrainRadius/de

## Beschreibung

Diese Randbedingung Legt den Radius eines Kreises oder Bogens auf einen bestimmten Wert fest. Wenn vor dem Start des Befehls mehr als ein Kreis oder Bogen ausgewählt wurde   *

-   Wenn die Beschränkung im \'Referenz\' Modus angewendet wird, wird eine neue Referenz Beschränkung zu jedem Objekt separat gemäß den oben genannten Regeln hinzugefügt.
-   Wird die Beschränkung im \'Normal\' (Fahren) Modus angewendet, werden folgende Regeln angewandt
    -   Ein Referenz Beschränkung wird separat auf jedes Objekt angewendet, das eine externe Geometrie ist

    -   
        **[<img src=images/Sketcher_ConstrainEqual.svg style="width   *16px"> [GleichheitFestlegen](Sketcher_ConstrainEqual.md)**
        
        wird nacheinander auf alle Objekte der realen Geometrie/Konstruktionsgeometrie angewandt, und eine maßliche Randbedingung wird auf das erste ausgewählte Objekt gemäß den obigen Regeln angewandt

NB   * B-Spline-Pole können nicht mit anderen Objekttypen in der Auswahl gemischt werden.

![](images/Sketcher_ConstrainRadius_example.png )

## Anwendung

1.  Einen oder mehrere Kreise oder Bögen auswählen.
2.  Die Schaltfläche **[<img src=images/Sketcher_ConstrainRadius.svg style="width   *16px"> [RadiusFestlegen](Sketcher_ConstrainRadius/de.md)** drücken.
3.  Ein Aufklappdialog öffnet sich, um den Wert zu bearbeiten oder zu bestätigen. Zum Bestätigen **OK** drücken. Falls mehrere Kreise/Bögen ausgewählt wurden, übernehmen alle Randbedingungen diesen Wert. Die einzelnen Werte werden bearbeitet, indem man in der 3D-Ansicht auf die Maßzahl doppelklickt; oder indem man in der Liste der Randbedingungen auf die Bedingung doppelklickt oder rechtsklickt und **Wert ändern** auswählt.
4.  Optional können Maßzahl und Maßlinie in der 3D-Ansicht durch Klicken auf die Maßzahl und Ziehen bei gedrückter linker Maustaste verschoben und gedreht werden.

\'\'\'Hinweis   * \'\'\' Das Beschränkungswerkzeug kann auch ohne vorherige Auswahl gestartet werden. Standardmäßig befindet sich der Befehl im Fortsetzungsmodus, um neue Beschränkungen zu erstellen; drücke die rechte Maustaste oder **Esc** einmal, um den Befehl zu beenden.

## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

Die [Skizzierer Skripten](Sketcher_scripting.md)-Seite erklärt die Werte, die für `ArcOrCircle` verwendet werden können und enthält weitere Beispiele, wie man Beschränkungen aus Python-Skripten erstellt.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadius/de

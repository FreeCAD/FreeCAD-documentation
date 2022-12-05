---
- GuiCommand:/de
   Name:Sketcher ConstrainDiameter
   Name/de:Sketcher DurchmesserFestlegen
   MenuLocation:Sketch → Skizzen-Beschränkungen → Durchmesser festlegen
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**K** **O**
   Version:0.18
   SeeAlso:[Sketcher AbstandFestlegen](Sketcher_ConstrainDistance/de.md), [Sketcher XAbstandFestlegen](Sketcher_ConstrainDistanceX/de.md), [Sketcher YAbstandFestlegen](Sketcher_ConstrainDistanceY/de.md)
---

# Sketcher ConstrainDiameter/de

## Beschreibung

Diese Randbedingung legt den Durchmesser eines Kreises oder Bogens auf einen bestimmten Wert fest. Wenn vor dem Start des Befehls mehr als ein Kreis oder Bogen ausgewählt wurde:

-   Wenn die Beschränkung im \'Referenz\' Modus angewendet wird, wird eine neue Referenz Beschränkung zu jedem Objekt separat gemäß den oben genannten Regeln hinzugefügt.
-   Wird die Beschränkung im \'Normal\' (Fahren) Modus angewendet, werden folgende Regeln angewandt
    -   Ein Referenz Beschränkung wird separat auf jedes Objekt angewendet, das eine externe Geometrie ist

    -   
        **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [GleichheitFestlegen](Sketcher_ConstrainEqual/de.md)**
        
        wird nacheinander auf alle Objekte der realen Geometrie/Konstruktionsgeometrie angewandt, und eine maßliche Randbedingung wird auf das erste ausgewählte Objekt gemäß den obigen Regeln angewandt

NB: B-Spline-Pole können nicht mit anderen Objekttypen in der Auswahl gemischt werden.

## Anwendung

1.  Einen oder mehrere Kreise oder Bögen auswählen.
2.  Die Schaltfläche **[<img src=images/Sketcher_ConstrainDiameter.svg style="width:16px"> [Durchmesser festlegen](Sketcher_ConstrainDiameter.md)** drücken.
3.  Ein Aufklappdialog öffnet sich, um den Wert zu bearbeiten oder zu bestätigen. Zum Bestätigen **OK** drücken. Falls mehrere Kreise/Bögen ausgewählt wurden, werden alle Randbedingungen diesen Wert übernehmen. Die einzelnen Werte werden bearbeitet, indem man in der 3D-Ansicht auf die Maßzahl doppelklickt; oder indem man in der Liste der Randbedingungen auf die Bedingung doppelklickt oder rechtsklickt und **Wert ändern** auswählt.
4.  Optional können Maßzahl und Maßlinie in der 3D-Ansicht durch Klicken auf die Maßzahl und Ziehen bei gedrückter linker Maustaste verschoben und gedreht werden.

**Hinweis:** Das Beschränkungswerkzeug kann auch ohne vorherige Auswahl gestartet werden. Standardmäßig befindet sich der Befehl im Fortsetzungsmodus, um neue Beschränkungen zu erstellen; drücke die rechte Maustaste oder **Esc** einmal, um den Befehl zu beenden.

## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Diameter', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

Die [Skizzierer Skripten](Sketcher_scripting.md)-Seite erklärt die Werte, die für `ArcOrCircle` verwendet werden können und enthält weitere Beispiele, wie man Beschränkungen aus Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDiameter/de

---
 GuiCommand:
   Name: Sketcher ConstrainRadius
   Name/de: Sketcher RadiusFestlegen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Radius festlegen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **K** **R**
   SeeAlso: Sketcher_ConstrainDistance/de, Sketcher_ConstrainDistanceX/de, Sketcher_ConstrainDistanceY/de
---

# Sketcher ConstrainRadius/de



## Beschreibung

Diese Randbedingung Legt den Radius eines Kreises oder Bogens auf einen bestimmten Wert fest. Wenn vor dem Start des Befehls mehr als ein Kreis oder Bogen ausgewählt wurde:

-   Wenn die Randbedingung im \'Referenz\'-Modus angewendet wird, wird eine neue Referenzbedingung zu jedem Objekt separat gemäß den oben genannten Regeln hinzugefügt.
-   Wird die Randbedingung im \'Normal\'-Modus (festlegend) angewendet, werden folgende Regeln angewendet:
    -   Eine Referenzbedingung wird separat auf jedes Objekt angewendet, das eine externe Geometrie ist.

    -   
        **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [GleichheitFestlegen](Sketcher_ConstrainEqual.md)**
        
        wird nacheinander zwischen allen Objekte der realen Geometrie oder Konstruktionsgeometrie angewendet, und eine maßliche Randbedingung wird dem ersten ausgewählten Objekt gemäß den obigen Regeln hinzugefügt.

NB: B-Spline-Pole können nicht mit anderen Objekttypen in der Auswahl gemischt werden.

![](images/Sketcher_ConstrainRadius_example.png )



## Anwendung

1.  Einen oder mehrere Kreise oder Bögen auswählen.
2.  Die Schaltfläche **[<img src=images/Sketcher_ConstrainRadius.svg style="width:16px"> [RadiusFestlegen](Sketcher_ConstrainRadius/de.md)** drücken.
3.  Ein Aufklappdialog öffnet sich, um den Wert zu bearbeiten oder zu bestätigen. Zum Bestätigen **OK** drücken. Falls mehrere Kreise/Bögen ausgewählt wurden, übernehmen alle Randbedingungen diesen Wert. Die einzelnen Werte werden bearbeitet, indem man in der 3D-Ansicht auf die Maßzahl doppelklickt; oder indem man in der Liste der Randbedingungen auf die Bedingung doppelklickt oder rechtsklickt und **Wert ändern** auswählt.
4.  Optional können Maßzahl und Maßlinie in der 3D-Ansicht durch Klicken auf die Maßzahl und Ziehen bei gedrückter linker Maustaste verschoben und gedreht werden.

**Hinweis:** Dieses Werkzeug kann auch ohne vorherige Auswahl gestartet werden. Standardmäßig befindet sich der Befehl im Fortsetzungsmodus, um neue Randbedingungen zu erstellen; ein Druck auf die rechte Maustaste oder auf **Esc** beendet den Befehl.



## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Radius', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

Die Seite [Sketcher Skripten](Sketcher_scripting.md) erklärt die Werte, die für `ArcOrCircle` verwendet werden können und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadius/de

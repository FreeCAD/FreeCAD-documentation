---
- GuiCommand:/de
   Name:Sketcher ConstrainDiameter
   Name/de:Skizzierer BeschränkeDurchmesser
   MenuLocation:Skizze → Skizzierer Beschränkungen → Beschränke Durchmesser
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   SeeAlso:[ Abstand](Sketcher_ConstrainDistance/de.md), [Beschränke Horizontalen Abstand](Sketcher_ConstrainDistanceX/de.md), [Beschränke Vertikalen Abstand](Sketcher_ConstrainDistanceY/de.md)
   Version:0.18
---

# Sketcher ConstrainDiameter/de

## Beschreibung

Diese Beschränkung beschränkt den Wert des Radius eines Kreises oder Bogens um einen bestimmten Wert zu haben. Wenn vor dem Start des Befehls mehr als ein Kreis oder Bogen ausgewählt wurde:

-   Wenn die Beschränkung im \'Referenz\' Modus angewendet wird, wird eine neue Referenz Beschränkung zu jedem Objekt separat gemäß den oben genannten Regeln hinzugefügt.
-   Wird die Beschränkung im \'Normal\' (Fahren) Modus angewendet, werden folgende Regeln angewandt
    -   Ein Referenz Beschränkung wird separat auf jedes Objekt angewendet, das eine externe Geometrie ist

    -   
        **<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Gleiche Beschränkung](Sketcher_ConstrainEqual/de.md)**
        
        werden nacheinander auf alle Objekte der realen Geometrie/Konstruktionsgeometrie angewandt, und eine dimensionale Beschränkung wird auf das erste ausgewählte Objekt gemäß den obigen Regeln angewandt

NB: B-Spline Pole können nicht mit anderen Objekttypen in der Auswahl gemischt werden.

## Anwendung

1.  Wähle einen oder mehrere Kreise oder Bögen.
2.  Drücke die **<img src=images/Sketcher_ConstrainDiameter.svg style="width:16px"> [Durchmesser beschränken](Sketcher_ConstrainDiameter.md)** Taste.
3.  Ein Aufklappdialog öffnet sich, um den Wert zu bearbeiten oder zu bestätigen. Drücke **OK** um zu bestätigen. Falls mehrere Kreise/Bögen ausgewählt wurden, werden alle Beschränkungen diesen Wert übernehmen. Bearbeite die einzelnen Werte durch Doppelklicken auf die Bemaßungsbeschriftung in der 3D Ansicht; oder doppelklicke in der Liste der Beschränkungen auf die Beschränkung oder klicke mit der rechten Maustaste und wählen **Wert ändern**.
4.  Optional können die Bemaßungsbeschriftung und -linie in der 3D Ansicht durch Klicken auf den Wert und Ziehen bei gedrückter linker Maustaste verschoben und gedreht werden.

\'\'\'Hinweis: \'\'\' Das Beschränkungswerkzeug kann auch ohne vorherige Auswahl gestartet werden. Standardmäßig befindet sich der Befehl im Fortsetzungsmodus, um neue Beschränkungen zu erstellen; drücke die rechte Maustaste oder **Esc** einmal, um den Befehl zu beenden.

## Skripten


```pythonSketch.addConstraint(Sketcher.Constraint('Diameter', ArcOrCircle, App.Units.Quantity('123.0 mm')))```

Die [Skizzierer Skripten](Sketcher_scripting.md)-Seite erklärt die Werte, die für `ArcOrCircle` verwendet werden können und enthält weitere Beispiele, wie man Beschränkungen aus Python-Skripten erstellt.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainDiameter/de

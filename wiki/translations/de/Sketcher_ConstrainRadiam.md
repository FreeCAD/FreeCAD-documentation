---
- GuiCommand:
   Name:Sketcher ConstrainRadiam
   Name/de:Sketcher RadiamFestlegen
   MenuLocation:Sketch - Skizzen-Beschränkungen - Automatisch Radius/Durchmesser einschränken
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**K** **S**
   Version:0.20
   SeeAlso:[Sketcher AbstandFestlegen](Sketcher_ConstrainDistance/de.md), [Sketcher XAbstandFestlegen](Sketcher_ConstrainDistanceX/de.md), [Sketcher YAbstandFestlegen](Sketcher_ConstrainDistanceY/de.md)
---

# Sketcher ConstrainRadiam/de



## Beschreibung

Diese Randbedingung legt den Durchmesser eines Kreises oder den Radius eines Bogens auf einen bestimmten Wert fest. Dabei gelten folgende Regeln:

-   Ist das Objekt ein B-Spline-Pol, wird ein Gewicht festgelegt.
-   Ist das Objekt ein Vollkreis, wird ein Durchmesser festgelegt.
-   In anderen Fällen (z. B. Bögen), wird ein Radius festgelegt.

Wenn vor dem Start des Befehls mehr als ein Kreis oder Bogen ausgewählt wurde:

-   Wenn die Beschränkung im \'Referenz\' Modus angewendet wird, wird eine neue Referenz Beschränkung zu jedem Objekt separat gemäß den oben genannten Regeln hinzugefügt.
-   Wird die Beschränkung im \'Normal\' (Fahren) Modus angewendet, werden folgende Regeln angewandt
    -   Ein Referenz Beschränkung wird separat auf jedes Objekt angewendet, das eine externe Geometrie ist

    -   
        **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [GleichheitFestlegen](Sketcher_ConstrainEqual.md)**
        
        wird nacheinander auf alle Objekte der realen Geometrie/Konstruktionsgeometrie angewandt, und eine maßliche Randbedingung wird auf das erste ausgewählte Objekt gemäß den obigen Regeln angewandt

NB: B-Spline-Pole können nicht mit anderen Objekttypen in der Auswahl gemischt werden.



## Anwendung

1.  Einen oder mehrere Kreise oder Bögen auswählen.
2.  Die Schaltfläche **[<img src=images/Sketcher_ConstrainRadiam.svg style="width:16px"> [Automatisch Radius oder Durchmesser festlegen](Sketcher_ConstrainRadiam/de.md)** drücken.
3.  Es öffnet sich ein Aufklappdialog zum Bearbeiten oder Bestätigen des Wertes. Zum Bestätigen **OK** drücken.
4.  Optional können Maßzahl und Maßlinie in der 3D-Ansicht durch Klicken auf die Maßzahl und Ziehen bei gedrückter linker Maustaste verschoben und gedreht werden.

**Hinweis:** Dieses Werkzeug kann auch ohne vorherige Auswahl gestartet werden. Standardmäßig befindet sich der Befehl im Fortsetzungsmodus, um neue Randbedingungen zu erstellen; ein Druck auf die rechte Maustaste oder auf **Esc** beendet den Befehl.



## Skripten

Es gilt kein spezielles Skripten. Siehe die Seite [Sketcher Skripten](Sketcher_scripting/de.md), die die Werte erklärt, die für `ArcOrCircle` und `Circle` verwendet werden können, und weitere Beispiele für die Erstellung von Randbedingungen mit Python-Skripten enthält.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadiam/de

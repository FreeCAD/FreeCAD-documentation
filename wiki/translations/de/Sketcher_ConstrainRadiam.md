---
- GuiCommand:/de
   Name:Sketcher ConstrainRadiam
   Name/de:Skizzierer BeschränkeRadiam
   MenuLocation:Skizze → Skizzierer Beschränkungen → Beschränke Radius/Durchmesser automatisch
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   SeeAlso:[Skizzierer Beschränke Abstand](Sketcher_ConstrainDistance/de.md), [Skizzierer Beschränke horizontalen Abstand](Sketcher_ConstrainDistanceX/de.md), [Skizzierer Abstand vertikalen Abstand](Sketcher_ConstrainDistanceY/de.md)
   Version:0.20
---

# Sketcher ConstrainRadiam/de


</div>

## Beschreibung

Diese Beschränkung beschränkt den Wert des Radius eines Kreises oder Bogens um einen bestimmten Wert zu haben. Wenn vor dem Start des Befehls mehr als ein Kreis oder Bogen ausgewählt wurde:

-   Wenn die Beschränkung im \'Referenz\' Modus angewendet wird, wird eine neue Referenz Beschränkung zu jedem Objekt separat gemäß den oben genannten Regeln hinzugefügt.
-   Wird die Beschränkung im \'Normal\' (Fahren) Modus angewendet, werden folgende Regeln angewandt
    -   Ein Referenz Beschränkung wird separat auf jedes Objekt angewendet, das eine externe Geometrie ist

    -   
        **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Gleiche Beschränkung](Sketcher_ConstrainEqual/de.md)**
        
        werden nacheinander auf alle Objekte der realen Geometrie/Konstruktionsgeometrie angewandt, und eine dimensionale Beschränkung wird auf das erste ausgewählte Objekt gemäß den obigen Regeln angewandt

NB: B-Spline Pole können nicht mit anderen Objekttypen in der Auswahl gemischt werden.


<div class="mw-translate-fuzzy">

## Anwendung


</div>

1.  Nimm einen oder mehrere Kreise oder Bögen.
2.  Drücke die **[<img src=images/Sketcher_ConstrainRadiam.svg style="width:16px"> [Beschränke Radius/Durchmesser automatisch](Sketcher_ConstrainRadiam/de.md)**.
3.  Es öffnet sich ein Aufklappdialog zum Bearbeiten oder Bestätigen des Wertes. Drücken **OK** zum Bestätigen.
4.  Optional können die Bemaßungsbeschriftung und die Linie in der 3D Ansicht verschoben und gedreht werden, durch klicken auf den Wert und ziehen bei gedrückter linker Maustaste.

**Hinweis:** das Beschränkungswerkzeug kann auch ohne vorherige Auswahl gestartet werden. Standardmäßig befindet sich der Befehl im Fortsetzungsmodus, um neue Beschränkungen zu erstellen; drücke die rechte Maustaste oder **Esc** einmal, um den Befehl zu beenden.

## Skripten

Es gilt kein spezielles Skripten. Siehe die Seite [Skizzierer Skripten](Sketcher_scripting/de.md), die die Werte erklärt, die für `ArcOrCircle` und `Circle` verwendet werden können, und weitere Beispiele für die Erstellung von Beschränkungen aus Python Skripten enthält.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainRadiam/de

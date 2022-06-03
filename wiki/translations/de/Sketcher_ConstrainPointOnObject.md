---
- GuiCommand   */de
   Name   *Sketcher ConstrainPointOnObject
   Name/de   *Sketcher PunktAufObjektFestlegen
   MenuLocation   *Sketch → Skizzen-Beschränkungen → Punkt auf Objekt festlegen
   Workbenches   *[Sketcher](Sketcher_Workbench/de.md)
   Shortcut   ***O**
   SeeAlso   *[Sketcher KoinzidentFestlegen](Sketcher_ConstrainCoincident/de.md)
---

# Sketcher ConstrainPointOnObject/de

## Beschreibung

Bringt einen Punkt auf einem anderen Objekt an, z.B. einer Linien-, Bogen- oder Skizzenachse.

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle den Punkt aus, den du auf einer Linie/Bogen/etc. anbringen möchtest. (**Ergebnis   *** Einmal ausgewählt, wird der Punkt grün).
2.  Wähle die Linie, die du an dem soeben ausgewählten Punkt anbringen möchtest (**Ergebnis   *** Einmal ausgewählt, wird die Linie grün).
3.  Rufe das **Punkt auf Objekt beschränken** Werkzeug mit verschiedenen Methoden auf   *
    -   Drücke die **[<img src=images/Sketcher_ConstrainPointOnObject.svg style="width   *16px"> [Point on object](Sketcher_ConstrainPointOnObject.md)** Schaltfläche in der Werkzeugleiste
    -   Verwende die **Shift** + **O** Tastaturkürzel.
    -   Verwende den {{MenuCommand/de|Skizze → Skizzierer Beschränkungen → Punkt auf Objekt beschränken}} Eintrag im oberen Menü.


</div>

## Skripten

Die Beschränkung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus durch den folgenden Befehl erzeugt werden   *


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`

-    `Skizze`ist ein Skizzenobjekt

-    `LinieVerschieben`ist die Nummer, die die Linie kennzeichnet, welche den zu bewegenden Punkt enthält, der auf der `fixiertenLinie ` (die Linie, die fixiert ist).

-    `PointOfLineMoving`ist die Nummer des Linienknotens `LinieVerschieben`, der sich mit dem Punkt auf der `fixierte Linie` bewegen soll.

-    `fixierteLinie`ist die Nummer der Linie, auf die der Punkt `PunktDerLinienbewegung` gesetzt werden soll.

Die [Skizzierer Skripten](Sketcher_scripting/de.md) Seite erklärt, wie man die Zahlen zur Bezeichnung von Linien und Punkten erkennt.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject/de

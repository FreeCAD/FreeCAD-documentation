---
- GuiCommand:/de
   Name:Sketcher ConstrainPointOnObject
   Name/de:Skizzierer BeschränkePunktAufObjekt
   MenuLocation:Skizze → Skizzen Beschränkungen → Beschränke Punkt Auf Objekt
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   Shortcut:**Umschalten** + **O**
   SeeAlso:[Skizzierer Beschränke Deckungsgleich](Sketcher_ConstrainCoincident/de.md)
---

# Sketcher ConstrainPointOnObject/de

## Beschreibung

Bringt einen Punkt auf einem anderen Objekt an, z.B. einer Linien-, Bogen- oder Skizzenachse.

## Anwendung

1.  Wähle den Punkt aus, den du auf einer Linie/Bogen/etc. anbringen möchtest. (**Ergebnis:** Einmal ausgewählt, wird der Punkt grün).
2.  Wähle die Linie, die du an dem soeben ausgewählten Punkt anbringen möchtest (**Ergebnis:** Einmal ausgewählt, wird die Linie grün).
3.  Rufe das **Punkt auf Objekt beschränken** Werkzeug mit verschiedenen Methoden auf:
    -   Drücke die **<img src=images/Sketcher_ConstrainPointOnObject.svg style="width:16px"> [Point on object](Sketcher_ConstrainPointOnObject.md)** Schaltfläche in der Werkzeugleiste
    -   Verwende die **Shift** + **O** Tastaturkürzel.
    -   Verwende den {{MenuCommand/de|Skizze → Skizzierer Beschränkungen → Punkt auf Objekt beschränken}} Eintrag im oberen Menü.

**Hinweis:** Die Reihenfolge wie die Linie und der Punkt ausgewählt wird, spielt keine Rolle. Der Punkt wird sich immer zu der Linie bewegen. Die Linie bleibt fixiert.

## Skripten


<div class="mw-translate-fuzzy">

Die Beschränkung kann von [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole durch den folgenden Befehl erzeugt werden:


</div>


`Sketch.addConstraint(Sketcher.Constraint('PointOnObject',LineMoving,PointOfLineMoving,LineFixed))`

-    `Skizze`ist ein Skizzenobjekt

-    `LinieVerschieben`ist die Nummer, die die Linie kennzeichnet, welche den zu bewegenden Punkt enthält, der auf der `fixiertenLinie ` (die Linie, die fixiert ist).

-    `PointOfLineMoving`ist die Nummer des Linienknotens `LinieVerschieben`, der sich mit dem Punkt auf der `fixierte Linie` bewegen soll.

-    `fixierteLinie`ist die Nummer der Linie, auf die der Punkt `PunktDerLinienbewegung` gesetzt werden soll.

Die [Skizzierer Skripten](Sketcher_scripting/de.md) Seite erklärt, wie man die Zahlen zur Bezeichnung von Linien und Punkten erkennt.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPointOnObject/de

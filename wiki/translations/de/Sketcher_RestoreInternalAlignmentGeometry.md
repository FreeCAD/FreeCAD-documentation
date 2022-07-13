---
- GuiCommand   */de
   Name   *Sketcher RestoreInternalAlignmentGeometry
   Name/de   *Sketcher InterneAusrichtungsgeometrieWiederherstellen
   MenuLocation   *Sketch → Skizzen-Werkzeuge → Interne Geometrie anzeigen / ausblenden
   Workbenches   *[Sketcher](Sketcher_Workbench/de.md)
   Shortcut   ***Z** **I**
   SeeAlso   *[Sketcher EllipseDurchMittelpunktErstellen](Sketcher_CreateEllipseByCenter/de.md), [Sketcher InterneAusrichtungFestlegen](Sketcher_ConstrainInternalAlignment/de.md)
---

# Sketcher RestoreInternalAlignmentGeometry/de

## Beschreibung

Der Befehl löscht unbenutzte Elemente, die an der Innengeometrie ausgerichtet sind, oder erstellt die fehlenden Elemente neu.

## Anwendung

-   Wähle ein Element einer Skizze aus, das die interne Ausrichtung unterstützt (derzeit nur Ellipse/Bogen und B-Spline).
-   Den Befehl aufrufen, durch anklicken von **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width   *16px"> [Interne Geometrie anzeigen / ausblenden](Sketcher_RestoreInternalAlignmentGeometry/de.md)** oder Auswahl des Menüeintrags **Sketch → Skizzen-Werkzeuge → [<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width   *16px"> Interne Geometrie anzeigen / ausblenden** oder Drücken der Tastenkombination.

Sind für das ausgewählte Element mögliche Ausrichtungen ungenutzt, wird neue Konstruktionsgeometrie erstellt und an den verfügbaren Stellen ausgerichtet. Sind (schon) alle Stellen ausgerichtet, wird unbenutzte interne Geometrie gelöscht (das Element wird als unbenutzt behandelt, wenn es an nichts anderes gebunden ist).

## Beispiel

1.  Eine neue Ellipse erstellen. Neue Ellipsen sind timer vollständig bestückt. Man erkennt eine Ellipse und etwas Konstruktionsgeometrie   * Hauptachse, Nebenachse, Brennpunkte.
2.  Nebenachse auswählen und **Del**-Tast drücken. Die Achse ist entfernt, aber die Ellipse ist noch da. Wie bekommt man die Achse zurück?
3.  Ellipse auswählen und den Befehl **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width   *16px"> [Interne Geometrie anzeigen / ausblenden](Sketcher_RestoreInternalAlignmentGeometry/de.md)** aufrufen. Die Achse ist wiederhergestellt.
4.  Jetzt wird der Hauptachse eine Länge zugeordnet. Ellipse auswählen und den Befehl **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width   *16px"> [Interne Geometrie anzeigen / ausblenden](Sketcher_RestoreInternalAlignmentGeometry/de.md)** aufrufen.

**Ergebnis   *** Die Nebenachse und die Brennpunkte sind entfernt, aber die Hauptachse wurde behalten, da sie mit anderen Randbedingungen zusammenhängt. Der Mittelpunkt der Ellipse bleibt ebenso, da er fest vorgegeben ist, wie auch der Mittelpunkt eines Kreises.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RestoreInternalAlignmentGeometry/de

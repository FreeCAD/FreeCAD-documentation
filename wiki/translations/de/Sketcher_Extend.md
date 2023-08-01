---
- GuiCommand:
   Name: Sketcher Extend
   Name/de: Sketcher Verlängern
   MenuLocation: Sketch - Skizzengeometrien - Kante verlängern
   Workbenches: [Sketcher](Sketcher_Workbench/de.md)
   Shortcut: **G** **Q**
   Version: 0.17
   SeeAlso: [Sketcher Zuschneiden](Sketcher_Trimming.md)
---

# Sketcher Extend/de

## Beschreibung

Das Werkzeug **Kante verlängern** verlängert eine Kante bis zu einer beliebigen Stelle in der Skizze oder bis zu einem Zielobjekt wie einer Kante oder einem Punkt.

<img alt="" src=images/Sketcher_Extend_example_01.png  style="width:600px;"> 
*''Auf der linken Seite (1) sind die beiden Skizzenelemente vor der Operation dargestellt; in der Mitte (2) wird die Linie bis zum Bogen verlängert; auf der rechten Seite (3) das Endergebnis.''*

## Anwendung

1.  Die Schaltfläche **[<img src=images/Sketcher_Extend.svg style="width:16px"> [Kante verlängern](Sketcher_Extend/de.md)** drücken.
2.  Eine Linie oder einen Bogen auswählen.
3.  Den Mauszeiger in der 3D-Ansicht in die Richtung bewegen, in die verlängert werden soll.
4.  Auf eine beliebige Stelle im Raum klicken, oder
5.  Um bis zu einer anderen Kante zu verlängern, wird der Mauszeiger auf der Zielkante positioniert; wenn sie markiert ist und das Symbol der Randbedingung <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md) neben dem Mauszeiger erscheint, klickt man zur Bestätigung. Eine Randbedingung Punkt auf Objekt wird hinzugefügt.
6.  Um bis zu einem Punkt in der Skizze zu verlängern, wird der Mauszeiger auf dem Zielpunkt positioniert; wenn er markiert ist und das Symbol der Randbedingung <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [Koinzidenz festlegen](Sketcher_ConstrainCoincident/de.md) neben dem Mauszeiger erscheint, klickt man zur Bestätigung. Eine Randbedingung Koinzidenz festlegen wird hinzugefügt.

## Hinweise

-   Zurzeit können nur Bögen und Linien verlängert werden.
-   Das Zielkanten- bzw. Zielpunktobjekt könnte sich ebenfalls verändern, wenn es nicht vollständig bestimmt ist.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Extend/de

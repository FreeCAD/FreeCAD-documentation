---
- GuiCommand   */de
   Name   *Sketcher Extend
   Name/de   *Sketcher Verlängern
   MenuLocation   *Sketch → Skizzengeometrien → Kante verlängern
   Workbenches   *[Sketcher](Sketcher_Workbench/de.md)
   Shortcut   ***G** **Q**
   Version   *0.17
   SeeAlso   *[Sketcher Zuschneiden](Sketcher_Trimming.md)
---

# Sketcher Extend/de

## Beschreibung


<div class="mw-translate-fuzzy">

Das Werkzeug \"Kante verlängern\" verlängert eine Kante an eine beliebige Stelle in der Skizze oder an eine andere Kante.


</div>

<img alt="" src=images/Sketcher_Extend_example_01.png  style="width   *600px;">


<div class="mw-translate-fuzzy">

*Auf der linken Seite (1) sind die beiden Skizzierelemente vor der Operation dargestellt; in der Mitte (2) wird die Linie bis zum Bogen verlängert; auf der rechten Seite (3) das Endergebnis.*


</div>

## Anwendung


<div class="mw-translate-fuzzy">

1.  Drücke die **[<img src=images/Sketcher_Extend.svg style="width   *16px"> [Kante verlängern](Sketcher_Extend/de.md)** Taste.
2.  Wähle eine Linie oder einen Bogen aus.
3.  Bewege den Mauszeiger in der 3D Ansicht in Richtung in welche verlängert werden soll.
4.  Klicke auf eine beliebige Stelle im Raum, oder
5.  Um zu einer anderen Kante zu verlängern, positioniere den Mauszeiger über die Kante; wenn sie markiert ist und das <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width   *16px;"> [Punkt auf Objekt](Sketcher_ConstrainPointOnObject/de.md) Beschränkungssymbol erscheint neben dem Mauszeiger, klicke zur Bestätigung. Ein Punkt auf Objekt Beschränkung wird hinzugefügt.
6.  Um auf einen Punkt in der Skizze zu verlängern, positioniere den Mauszeiger auf den Punkt; wenn er markiert ist und das <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width   *16px;"> [Deckungsgleiche Beschränkung](Sketcher_ConstrainCoincident/de.md) Symbol erscheint neben dem Mauszeiger, klicke zur Bestätigung. Eine deckungsgleiche Zwangsbedingung wird hinzugefügt.


</div>

## Hinweise

-   Only arcs and lines can be extended at this time.
-   The target edge or point object may be modified as well if it is not fully constrained.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Extend/de

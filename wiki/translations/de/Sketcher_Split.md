---
- GuiCommand:/de
   Name:Sketcher Split
   Name/de:Skizzierer Teilen
   MenuLocation:Skizze → Skizzierer Geometrien → Teilen
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   Version:0.20
   SeeAlso:[Skizzierer Stutzen](Sketcher_Trimming/de.md)
---

# Sketcher Split/de

## Beschreibung

Dieses Werkzeug erlaubt eine Kante in zwei identische Teile zu teilen, wobei die meisten Beschränkungen dupliziert werden, so dass beide Teile bis auf die Teilungspunktlage beschränkt bleiben. Im speziellen Fall eines Kreises wird dieser in einen Bogen mit losen Enden umgewandelt, wobei die bestehenden Kreisbeschränkungen auf den neuen Bogen übertragen werden.

![](images/SketcherSplitExample1.png ) ![](images/SketcherSplitExample2.png ) ![](images/SketcherSplitExample3.png )

## Anwendung

1.  Drücke die **[<img src=images/Sketcher_Split.svg style="width:16px"> [Teilen](Sketcher_Split/de.md)** Taste. Der Mauszeiger verwandelt sich in ein weißes Kreuz mit einem roten Teilen Symbol.
2.  Klicke auf die Kante an der Stelle, an der du sie teilen möchtest.
3.  Aus den Linien- und Bogenkanten werden zwei neue erstellt, die an dem angeklickten Punkt verbunden werden. Ein Kreis wird in einen Bogen umgewandelt, der denselben Mittelpunkt und dieselben Beschränkungen wie der ursprüngliche Kreis hat.
4.  Durch Drücken von **Esc** oder der rechten Maustaste wird die Funktion beendet.

## Begrenzungen

-   Für Ellipse, Parabel, Hyperbel und B-Splines wird der Prozess noch nicht unterstützt.

## Hinweise

-   Alle Deckungsgleicheiten werden übertragen - Startpunkt, Endpunkt und Mittelpunkt (falls zutreffend).
-   Die Punkt auf Objekt Beschränkung wird auf die nähere, neu erstellte Kante übertragen.
-   Vertikale und horizontale Beschränkung werden auf beide Nachkommen kopiert.
-   Parallele und senkrechte Beschränkung werden für beide Liniensegmente kopiert, für Bögen nur einmal, und zwar auf den näheren Teil.
-   Die Gleichheitsbeschränkung wird nur für die resultierenden Bogenkanten übertragen, die Liniensegmente erhalten sie nicht.
-   Die Symmetriebeschränkung wird derzeit nicht übertragen.
-   Die Blockbeschränkung wird derzeit nicht übertragen.
-   Horizontale, vertikale und Längenbeschränkungen zwischen Punkten werden auf die äußeren Punkte der neuen Kanten übertragen.
-   Die Punktabstandsbeschränkung wird nur einmal zugewiesen, und zwar dem näheren Kantensegment.
-   Radius- und Durchmesserbeschränkungen werden auf jeden entstehenden Bogen kopiert.
-   Die Winkelbeschränkung wird derzeit nicht übertragen.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Split/de

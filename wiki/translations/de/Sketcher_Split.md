---
 GuiCommand:
   Name: Sketcher Split
   Name/de: Sketcher Teilen
   MenuLocation: Sketch , Skizzengeometrien , Kante teilen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **Z**
   Version: 0.20
   SeeAlso: Sketcher_Trimming/de
---

# Sketcher Split/de



## Beschreibung

Dieses Werkzeug teilt eine Kante in zwei auf, wobei vorhandene anwendbare Randbedingungen auf die neue Kante kopiert werden. Die Position des Punktes an dem sich beide Kanten treffen ist nicht festgelegt. Geschlossene Kurven (z.B. Kreise, Ellipsen und geschlossene B-splines) werden in entsprechende offene Kurven umgewandelt (Kreisbögen, Ellipsenbögen und offene B-Splines).

![](images/SketcherSplitExample1.png ) ![](images/SketcherSplitExample2.png ) ![](images/SketcherSplitExample3.png )



## Anwendung

1.  Die Schaltfläche **[<img src=images/Sketcher_Split.svg style="width:16px"> [Kante teilen](Sketcher_Split/de.md)** drücken. Der Mauszeiger verwandelt sich in ein weißes Kreuz mit einem roten Teilen-Symbol.
2.  An der Stelle auf eine Kante klicken, an der sie geteilt werden soll.
3.  Aus den Linien- und Bogenkanten werden zwei neue erstellt, die an dem angeklickten Punkt verbunden werden. Ein Kreis wird in einen Bogen umgewandelt, der denselben Mittelpunkt und dieselben Randbedingungen wie der ursprüngliche Kreis hat.
4.  Durch Drücken von **Esc** oder der rechten Maustaste wird die Funktion beendet.



## Einschränkungen

-   In der {{VersionMinus/de|0.20}} wird die Funktion für Ellipsen, Parabeln, Hyperbeln und B-Splines nicht unterstützt.



## Hinweise

-   Die Randbedingung Koinzidenz festlegen wird in allen Fällen übertragen - Startpunkt, Endpunkt und Mittelpunkt (falls zutreffend).
-   Die Randbedingung Punkt auf Objekt festlegen wird auf die nähere, neu erstellte Kante übertragen.
-   Die Randbedingungen Vertikal Festlegen und Horizontal festlegen werden auf beide Nachfolger kopiert.
-   Die Randbedingungen Parallel festlegen und Rechtwinklig festlegen werden auf beide Liniensegmente übertragen, auf Bögen nur einmal, und zwar auf den näheren Teil.
-   Die Randbedingung Gleichheit festlegen wird nur auf die resultierenden Bogenkanten übertragen und nicht auf die Liniensegmente.
-   Die Randbedingung Symmetrie festlegen wird nicht übertragen.
-   Die Randbedingung Fixieren wird derzeit nicht übertragen.
-   Die Randbedingungen Horizontalen Abstand festlegen, Vertikalen Abstand festlegen und Abstand festlegen (zwischen Punkten) werden auf die äußeren Punkte der neuen Kanten übertragen.
-   Die Randbedingungen Abstand festlegen (zwischen Punkt und Kante) wird nur einmal zugewiesen, und zwar dem näheren Kantensegment.
-   Randbedingungen Radius festlegen und Durchmesser festlegen werden auf alle entstehenden Bögen kopiert.
-   Die Randbedingung Winkel festlegen wird derzeit nicht übertragen.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Split/de

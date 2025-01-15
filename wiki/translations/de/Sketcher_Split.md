---
 GuiCommand:
   Name: Sketcher Split
   Name/de: Sketcher Teilen
   MenuLocation: Sketch , Sketcher-Werkzeuge , Kante teilen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **Z**
   Version: 0.20
   SeeAlso: Sketcher_Trimming/de
---

# Sketcher Split/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_Split.svg  style="width:24px;"> [Sketcher Teilen](Sketcher_Split/de.md) teilt eine Kante in zwei auf. Ist die Kante eine geschlossene Kurve (z.B. ein Kreis, eineEllipse oder ein geschlossener B-Spline), wird sie in eine entsprechende offene Kurve umgewandelt (einen Kreisbogen, einen Ellipsenbogen oder einen offenen B-Spline).



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_Split.svg" width=16px> [Kante teilen](Sketcher_Split/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher-Werkzeuge →<img src="images/Sketcher_Split.svg" width=16px> Kante teilen** auswählen.
    -   Das Tastaturkürzel **G** dann **Z**.
2.  Ist eine Vorauswahl vorhanden, wird sie geleert. Das Werkzeug akzeptiert keine Vorauswahl.
3.  Der Mauszeiger wandelt sich in ein Kreuz mit dem Werkzeugsymbol.
4.  Eine Kante andem Punkt anklicken, an dem sie aufgetrennt werden soll.
5.  Ist die originale Kante eine Linie oder eine offene Kurve, werden zwei neue Kanten erstellt und mit einer Randbedingung [Koinzident festlegen](Sketcher_ConstrainCoincident/de.md) verbunden. Für geschlossene Kurven wird eine neue offene Kurve erstellt; die neue Verbindunsstelle erhält diese Randbedingung nicht. Vorhandene anwendbare Randbedingungen werden auf die neue(n) Kante(n) übertragen. Siehe [Hinweise](#Hinweise.md).
6.  Dieses Werkzeug läuft immer im Fortsetzen-Modus: Wahlweise weitere Kanten teilen.
7.  Zum Beenden, in einen leeren Bereich der [3D-Ansicht](3D_view/de.md) klicken, die rechte Maustaste oder **Esc** drücken; oder ein anderes Werkzeug zur Erstellung von Geometrien oder Randbedingungen auswählen.



## Hinweise

-   Eine Randbedingung [Koinzident festlegen](Sketcher_ConstrainCoincident/de.md) wird auf die Mittelpunkte neuer Kreisbögen angewendet.
-   Randbedingungen zum Festlegen von [Radius](Sketcher_ConstrainRadius/de.md) und [Durchmesser](Sketcher_ConstrainDiameter/de.md) werden auf die neuen Randbedingungen kopiert (sie sind im Ergebnis überflüssig).
-   Die Randbedingungen Koinzident festlegen und [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md) werden auf die jeweils nähere neu erstellte Kante übertragen.
-   Die Randbedingungen [Horizontal festlegen](Sketcher_ConstrainHorizontal/de.md) und [Vertikal festlegen](Sketcher_ConstrainVertical/de.md) zwischen Punkten werden auf die jeweils nähere neu erstellte Kante übertragen.
-   Gehören die vorgenannten Randbedingungen zu Linien, werden sie auf die neuen Linienabschnitte kopiert.
-   Die Randbedingungen [Parallel festlegen](Sketcher_ConstrainParallel/de.md) und [Rechtwinklig festlegen](Sketcher_ConstrainPerpendicular/de.md) werden auf die neuen Linienabschnitte kopiert; für neue Kreisbögen werden sie nur jeweils einmal auf den näheren kopiert.
-   Die Randbedingungen [Horizontalen Abstand festlegen](Sketcher_ConstrainDistanceX/de.md), [Vertikalen Abstand festlegen](Sketcher_ConstrainDistanceY/de.md) und [Abstand festlegen](Sketcher_ConstrainDistance/de.md) werden auf die jeweils nähere neu erstellte Kante übertragen.
-   Die Randbedingungen [Winkel festlegen](Sketcher_ConstrainAngle/de.md), [Symmetrisch festlegen](Sketcher_ConstrainSymmetric/de.md) und [Fixieren](Sketcher_ConstrainBlock/de.md) werden derzeit nicht übertragen.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Split/de

---
 GuiCommand:
   Name: Sketcher Extend
   Name/de: Sketcher Verlängern
   MenuLocation: Skizze , Sketcher-Werkzeuge , Kante verlängern
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **Q**
   Version: 0.17
   SeeAlso: Sketcher_Trimming/de
---

# Sketcher Extend/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_Extend.svg  style="width:24px;"> [Sketcher Verlängern](Sketcher_Extend/de.md) verlängert oder kürzt eine Linie oder einen Kreisbogen bis zu einer beliebigen Stelle oder bis zu einer Zielkante oder einem Zielpunkt.

<img alt="" src=images/Sketcher_Extend_example_01.png  style="width:600px;"> 
*''Auf der linken Seite (1) sind die beiden Skizzenelemente vor der Operation dargestellt; in der Mitte (2) wird die Linie bis zum Bogen verlängert; auf der rechten Seite (3) das Endergebnis.''*



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_Extend.svg" width=16px> [Kante verlängern](Sketcher_Extend/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher-Werkzeuge → <img src="images/Sketcher_Extend.svg" width=16px> Kante verlängern** auswählen.
    -   Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_Extend.svg" width=16px> Kante verlängern** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **G** dann **Q**.
2.  Eine vorhandene Auswahl wird gelöscht. Das Werkzeug akzeptiert keine Vorauswahl.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Eine Linie oder einen Kreisbogen auswählen.
5.  Den Mauszeiger in die Richtung zum Verlängern oder Kürzen bewegen.
6.  Eine der folgenden Möglichkeiten auswählen:
    -   Einen beliebigen Punkt anklicken.
    -   Zu Verlängern bzw. Kürzen an einer weiteren Kante müssen ([Automatische Randbedingungen](Sketcher_Workbench/de#Automatische_Randbedingungen.md) aktiviert sein): Den Mauszeiger über die Zielkante bewegen. Wenn diese hervorgehoben wird und das Symbol der Randbedingung <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [Punkt auf Objekt festlegen](Sketcher_ConstrainPointOnObject/de.md) neben dem Mauszeiger erscheint, wird mit einem Klick bestätigt. Die Randbedingung wird hinzugefügt.
    -   Um bis zu einem einem Punkt zu verlängern bzw. zu kürzen (Automatische Randbedingungen müssen aktiviert sein): Den Mauszeiger über den Zielpunkt bewegen. Wenn dieser hervorgehoben wird und das Symbol der Randbedingung <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [Koinzident festlegen](Sketcher_ConstrainCoincident/de.md) neben dem Mauszeiger erscheint, wird mit einem Klick bestätigt. Die Randbedingung wird hinzugefügt.
7.  Wenn das Werkzeug im [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) läuft:
    1.  Wahlweise weitere Kanten verlängern bzw. kürzen.
    2.  Zum Beenden in einen leeren Bereich der [3D-Ansichr](3D_view/de.md) klicken, die rechte Maustaste oder **Esc** drücken oder ein anderes Werkzeug zur Erstellung von Geometrien oder Randbedingungen aufrufen.



## Hinweise

-   Wenn nicht vollständig bestimmt, könnte die Zielkante bzw. der Zielpunkt ebenfalls verändert werden.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Extend/de

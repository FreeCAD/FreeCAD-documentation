---
 GuiCommand:
   Name: Sketcher Trimming
   Name/de: Sketcher Zuschneiden
   MenuLocation: Skizze , Sketcher-Werkzeuge , Kante zuschneiden
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **T**
   Version: 0.12
   SeeAlso: Sketcher_Split/de, Sketcher_Extend/de
---

# Sketcher Trimming/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_Trimming.svg  style="width:24px;"> [Sketcher Zuschneiden](Sketcher_Trimming/de.md) entfern eine Kante bis zu den nächsten Schnittstellen mit anderen Kanten. Schneidet die ausgewählte Kante keine andere Kante, wird sie ganz gelöscht



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_Trimming.svg" width=16px> [Kante zuschneiden](Sketcher_Trimming/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher-Werkzeuge → <img src="images/Sketcher_Trimming.svg" width=16px> Kante zuschneiden** auswählen.
    -   Das Tastaturkürzel **G** dann **T**.
2.  Ist eine Auswahl vorhanden, wird sie geleert. Das Werkzeug akzeptiert keine Vorauswahl.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Es gibt zwei Arbeitsweisen:
    -   Zuschneiden durch Einzelklick:
        1.  Den Mauszeiger auf den Abschnitt einer Kante bewegen, der entfernt werden soll.
        2.  Die Kante wird hervorgehoben und die Zuschnittpositionen werden mit temporären Kreisen markiert.
        3.  Zum Bestätigen klicken.
        4.  Die Kante wird zwischen den markierten Stellen ausgeschnitten.
    -   Zuschneiden durch Halten-und-Ziehen: {{Version/de|1.0}}
        1.  Die linke Maustaste gedrückt halten.
        2.  Mit dem Mauszeiger über die Abschnitte von Kanten fahren, die entfernt werden sollen.
        3.  Die Abschnitte werden sofort entfernt.
        4.  Die linke Maustaste loslassen.
5.  Wird ein Abschnitt ausgeschnitten, werden vorhandene anwendbare Randbedingungen auf eine der resultierenden neuen Kanten übertragen. Zwischen den Enden der zugeschnittenen Kanten und den Schnittkanten wird die Randbedingung [PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md) hinzugefügt.
6.  Dieses Werkzeug läuft immer im Fortsetzen-Modus: Wahlweise weitere Kanten zuschneiden.
7.  Zum Beenden in einen leeren Bereich der [3D-Ansicht](3D_view/de.md) klicken, mit der rechten Maustaste klicken, **Esc** drücken, oder ein anderes Werkzeug zum Erstellen von Geometrie oder Randbedingungen starten.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Trimming/de

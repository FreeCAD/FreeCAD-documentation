---
 GuiCommand:
   Name:  Sketcher Dimension
   Name/de:  Sketcher Bemaßen
   MenuLocation: Skizze , Sketcher-Randbedingungen , Bemaßen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **D**
   Version: 1.0
---

# Sketcher Dimension/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_Dimension.svg  style="width:24px;"> [Sketcher Bemaßen](Sketcher_Dimension/de.md) ist das kontextabhängige Werkzeug zum Erstellen von Randbedingungen des Arbeitsbereichs Sketcher. Basierend auf der aktuellen Auswahl stellt es passende maßliche Randbedingungen zur Verfügung aber auch geometrische Randbedingungen.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

1.  Wähle optional ein oder mehrere Elemente (Kanten oder Punkte) aus. [B-Spline](Sketcher_Workbench#Sketcher_CompCreateBSpline/de.md)-Kanten werden derzeit nicht unterstützt.
2.  Es gibt mehrere Möglichkeiten, das Tool aufzurufen:
    -   Wenn die Einstellung **Dimensioning constraints** [Einstellung](Sketcher_Preferences#General/de.md) auf {{Value|Both}} oder {{Value|Single tool}} (Standard) eingestellt ist: Drücke die Schaltfläche **<img src="images/Sketcher_Dimension.svg" width=16px> [Dimension](Sketcher_Dimension/de.md)**.
    -   Wähle im Menü die Option **Sketch → Sketcher constraints → <img src="images/Sketcher_Dimension.svg" width=16px> Dimension**.
    -   Klicke mit der rechten Maustaste in die [3D-Ansicht](3D_view/de.md) und wähle im Kontextmenü die Option **Dimension → <img src="images/Sketcher_Dimension.svg" width=16px> Dimension**.
    -   Wenn eine Auswahl vorhanden ist: Klicke mit der rechten Maustaste in die 3D-Ansicht und wähle im Kontextmenü die Option **<img src="images/Sketcher_Dimension.svg" width=16px> Dimension**.
    -   Verwende die Tastenkombination: **D**.
3.  Der Cursor verwandelt sich in ein Kreuz mit dem Werkzeugsymbol.
4.  Wenn du noch kein Element ausgewählt hast: Wähle eines aus.
5.  Abhängig von den ausgewählten Elementen wird eine Einschränkung vorgeschlagen.
6.  Wähle optional ein weiteres Element aus.
7.  Hebe die Auswahl eines Elements optional auf, indem du erneut darauf klickst.
8.  Die vorgeschlagene Einschränkung wird nach jeder Auswahländerung aktualisiert.
9.  Drücke optional ein- oder mehrmals die Taste **M**, um durch andere verfügbare Einschränkungen zu blättern, falls vorhanden.
10. Wenn eine geometrische Einschränkung vorgeschlagen wird, können sich ausgewählte Elemente ändern und eine Vorschau des Ergebnisses anzeigen.
11. Führe einen der folgenden Schritte aus:
    -   Klicke zur Bestätigung in einen leeren Bereich in der [3D-Ansicht](3D_view/de.md):
        1.  Wenn eine Dimensionsbeschränkung erstellt wird, bestimmt der angeklickte Punkt ihre Position. Bei einer linearen Dimension bestimmt der angeklickte Punkt auch ihren Typ: <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:16px;"> [Horizontaler Abstand](Sketcher_ConstrainDistanceX/de.md), <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:16px;"> [Vertikaler Abstand](Sketcher_ConstrainDistanceY/de.md) oder <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:16px;"> [Abstand](Sketcher_ConstrainDistance/de.md).
        2.  Wenn eine [FestlegendeRandbedingungUmschalten](Sketcher_ToggleDrivingConstraint/de.md) erstellt wird, öffnet sich, abhängig von den [Einstellungen](Sketcher_Preferences#Display/de.md), ein Dialog, um [ihren Wert zu bearbeiten](Sketcher_Workbench#Edit_constraints/de.md).
        3.  Eine Beschränkung wird hinzugefügt.
        4.  Dieses Tool läuft immer im Fortsetzungsmodus: Optional kannst du mit der Erstellung von Beschränkungen fortfahren.
    -   Zum Beenden rechtsklicken oder **Esc** drücken oder ein anderes Geometrie- oder Beschränkungserstellungstool starten.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Dimension/de

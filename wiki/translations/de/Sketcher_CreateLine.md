---
 GuiCommand:
   Name: Sketcher CreateLine
   Name/de: Sketcher LinieErstellen
   MenuLocation: Sketch , Skizzengeometrien , Linie erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: L
   SeeAlso: Sketcher_CreatePolyline/de
---

# Sketcher CreateLine/de



## Beschreibung

Dieses Werkzeug zeichnet eine Linie durch das Setzen zweier Punkte in der [3D-Ansicht](3D_view/de.md). Beim Starten des Werkzeugs verwandelt sich der Mauszeiger in ein weißes Kreuz mit einem roten Liniensymbol. Die Koordinaten werden in Echtzeit neben dem Mauszeiger angezeigt.

![](images/Sketcher_LineExample1.png‎ )

Das erzeugte Linienobjekt beginnt und endet an den gegebenen Punkten, aber die Linie ist unendlich in Bezug auf die Randbedingungen [TangentialFestlegen](Sketcher_ConstrainTangent/de.md), [PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md) und [WinkelFestlegen](Sketcher_ConstrainAngle/de.md). Das bedeutet zum Beispiel, dass ein Punkt mit der Randbedingung [PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md) nicht unbedingt zwischen den beiden Endpunkten liegen muss, sondern auch außerhalb dieser Punkte auf der Verlängerung der Linie liegen kann.



## Anwendung

-   Die Punkte in einem leeren Bereich der 3D-Ansicht setzen, oder an einem bestehenden Objekt auswählen (Automatische Randbedingungen müssen im [Aufgabenbereich](Task_panel/de.md) aktiviert sein)
-   Das Drücken von **Esc** oder ein Klick mit der rechten Maustaste bricht die Funktion ab.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateLine/de

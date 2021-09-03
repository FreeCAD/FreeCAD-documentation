---
- GuiCommand:/de
   Name:Sketcher CreateLine
   Name/de:Skizzierer Linie
   MenuLocation:Sketch → Skizzengeometrien → Linie erstellen
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:L
   SeeAlso:[Sketcher Polyline](Sketcher_CreatePolyline/de.md)
---

## Beschreibung

Dieses Werkzeug zeichnet eine Linie durch Aufnahme von zwei Punkten: den Start- und den Endpunkt.

Beim starten des Werkzeugs verwandelt sich der Mauszeiger in ein weißes Kreuz mit einem roten Liniensymbol. Die Koordinaten werden neben dem Zeiger in blau in Echtzeit angezeigt.

![](images/Sketcher_LineExample1.png‎ )

Das erzeugte Linienobjekt beginnt und endet an den gegebenen Punkten, aber die Linie ist unendlich in Bezug auf die Beschränkungen [Tangente](Sketcher_ConstrainTangent/de.md), [Punkt auf Objekt](Sketcher_ConstrainPointOnObject/de.md) und [Winkel festlegen](Sketcher_ConstrainAngle/de.md). Das bedeutet zum Beispiel, dass ein Punkt mit der Beschränkung [Punkt auf Objekt](Sketcher_ConstrainPointOnObject/de.md) nicht unbedingt zwischen den beiden Endpunkten liegt, sondern auch außerhalb dieser Punkte auf der Verlängerung der Linie liegen kann.

## Anwendung

-   Wählen Sie die Punkte im freien Feld der 3D-Ansicht, oder an einem bestehenden Objekt (Automatisch Randbedingungen müssen in der Aufgabenleiste aktiviert sein)
-   Durch drücken von **Esc** oder Betätigung der rechten Maustaste wird die Funktion abgebrochen.





{{Sketcher Tools navi

}}  

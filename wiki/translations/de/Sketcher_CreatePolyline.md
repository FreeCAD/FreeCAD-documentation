---
- GuiCommand:/de
   Name:Sketcher CreatePolyline
   Name/de:Sketcher LinienzugErstellen
   MenuLocation:Sketch → Skizzengeometrien → Linienzug erstellen
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**G** **M**
   SeeAlso:[Sketcher LinieErstellen](Sketcher_CreateLine/de.md)
---

# Sketcher CreatePolyline/de

## Beschreibung

Dieses Werkzeug arbeitet wie das Werkzeug [Sketcher LinieErstellen](Sketcher_CreateLine/de.md), erstellt aber kontinuierliche Linien- und Bogensegmente, die durch Knoten miteinander verbunden sind. Beim Starten des Werkzeugs verwandelt sich der Mauszeiger in ein weißes Kreuz mit einem roten Polyliniensymbol. Die Koordinaten werden in Echtzeit in blau neben dem Zeiger angezeigt.

![](images/Sketcher_PolylineExample1.png )



*Polylinie beginnt mit einer Linie, einem tangentialen Bogen, einem senkrechten Bogen und dann einer tangentialen Linie.*

## Anwendung

Die Polylinie beginnt immer mit einem geraden Liniensegment: klicken - die Maus bewegen - klicken. Bewege die Maus erneut. Nachdem das erste Liniensegment platziert wurde, verfügt das Skizzierer Polylinien Werkzeug über mehrere Modi, die mit der **M** Taste umgeschaltet werden können. Zum Beispiel kannst du tangentiale oder senkrechte Bögen zeichnen, die einem Linien- oder Bogensegment folgen. Durch wiederholtes Drücken der Taste **M** schaltet zwischen diesen verschiedenen Modi um:

1.  Drücke die **M** Taste: Das neue Segment ist eine Linie, die senkrecht zum vorherigen Segment verläuft.
2.  Drücke die **M** Taste erneut: das neue Segment ist eine Linie, die tangential zum vorherigen Segment verläuft.
3.  Drücke die **M** Taste erneut: das neue Segment ist ein Bogen, der tangential zum vorherigen Segment verläuft.
4.  Drücke die **M** Taste erneut: das neue Segment ist ein Bogen, der senkrecht (links) zum vorherigen Segment verläuft.
5.  Drücke die **M** Taste erneut: das neue Segment ist ein Bogen, der senkrecht (rechts) zum vorherigen Segment verläuft.
6.  Drücke die **M** Taste erneut: Du befindest dich wieder in dem Zustand, in dem du begonnen hast; die Linie ist nur durch eine Koinzidenz mit dem vorherigen Segment verbunden.

-    <small>(v0.18)</small> Solange in einem der der Bogenmodi, gedrückt halten der **Strg** Taste (MacOS: **CMD** Taste) und bewegen des Mauszeigers bewirkt, dass der Bogen in 45 Grad Abstufungen einrastet, relativ zum zuvor erstellten Polyliniensegment.

-   Punkte wählen auf einem leeren Bereich der 3D Ansicht oder auf einem vorhandenen Objekt (automatische Beschränkungen müssen in AufgabenAnsicht aktiv sein).

-   Drücken von **Esc** oder Klicken der rechten Maustaste *vor* dem Schließen der Polylinie zu einer Schleife beendet die aktuelle Polylinie und du kannst mit einer neuen fortfahren. Drücken von **Esc** oder ein erneuter Klick mit der rechten Maustaste beendet die Polylinienfunktion.

-   Drücken von **Esc** oder das Klicken der rechten Maustaste *nach* dem Schließen des Linienzugs zu einer Schleife beendet die Linienzugfunktion.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePolyline/de

---
- GuiCommand:/de
   Name:Sketcher CreatePoint
   Name/de:Skizzierer ErzeugePunkt
   MenuLocation:Skizze → Skizzengeometrien → Punkt erzeugen
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
---

## Beschreibung

Das Punktwerkzeug erzeugt einen Punkt in der aktuellen Skizze, der für die Konstruktion von geometrischen Elementen genutzt werden kann. Der Punkt ist immer ein Konstruktionselement und erscheint nicht in der 3D-Ansicht.

[480px\|Point in the sketcher](IMAGE:Sketcher_Point_fr_01.png.md) 

## Anwendung

-   Auf die Schaltfläche **<img src="images/Sketcher_Point.svg" width=24px> ErstellePunkt** klicken.
-   Ein Klick in die Skizze erzeugt einen Punkt.
-   Durch Drücken von **Esc** oder Klicken mit der rechten Maustaste wird die Funktion abgebrochen.

## Optionen

Ein Modus zum Fangen an das Gitter kann unter [Skizzierer Einstellungen](Sketcher_Preferences/de.md) eingestellt werden. Der Punkt wird dann an das Gitter gefangen, wenn er weniger als 25% Gitterabstand zu einer Gitterlinie hat. Der Fang Modus fixiert sie nicht am Gitter. Die Punkte können mit der Maus oder mit Zwangsbeschränkungen an andere Stellen verschoben werden.

## Begrenzungen

Der erzeugte Punkt ist außerhalb der Skizze nicht verfügbar. Wird ein Punkt in der 3D Ansicht benötigt, verwende stattdessen den [PartDesign Punkt](PartDesign_Point/de.md) als einen Bezugspunkt oder den [Part Punkt](Part_Point/de.md).





{{Sketcher Tools navi

}}  

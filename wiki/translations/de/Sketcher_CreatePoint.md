---
- GuiCommand:
   Name:Sketcher CreatePoint
   Name/de:Sketcher PunktErstellen
   MenuLocation:Sketch - Skizzengeometrien - Punkt erstellen
   Workbenches:[Sketcher](Sketcher_Workbench/de.md)
   Shortcut:**G** **Y**
---

# Sketcher CreatePoint/de



## Beschreibung

Das Punktwerkzeug erzeugt einen Punkt in der aktuellen Skizze, der für die Konstruktion von geometrischen Elementen genutzt werden kann.

[480px\|Point in the sketcher](IMAGE:Sketcher_Point_fr_01.png.md) 

## Anwendung

-   Auf die Schaltfläche **<img src="images/Sketcher_Point.svg" width=24px> Punkt erstellen** klicken, um die Funktion zu aktivieren.
-   Ein Klick in die Skizze erzeugt einen Punkt.
-   Durch Drücken von **Esc** oder Klicken mit der rechten Maustaste wird die Funktion abgebrochen.



## Optionen

-   Standardmäßig werden Punkte als Konstruktionsgeometrie erstellt und sind daher außerhalb des Bearbeitungsmodus der Skizze nicht sichtbar. Mit dem Werkzeug <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:16px;"> [UmschalterKonstruktion](Sketcher_ToggleConstruction/de.md) lassen sie sich in normale Geometrie umwandeln.
-   Der Modus **Am Raster fangen** kann in den [Sketcher Einstellungen](Sketcher_Preferences/de.md) aktiviert werden. Ein Punkt wird dann am Raster gefangen, wenn sein Abstand zu einer Rasterlinie weniger als 25 % des Abstandes zwischen zwei Rasterlinien beträgt. Der Fangmodus fixiert den Punkt nicht am Raster. Er hat weiterhin zwei nicht bestimmte Freiheitsgrade und kann noch mit der Maus bewegt werden oder mit Randbedingungen anderen Positionen zugeordnet werden.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePoint/de

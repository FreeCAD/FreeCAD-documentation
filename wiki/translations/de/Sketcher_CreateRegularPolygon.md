---
 GuiCommand:
   Name: Sketcher CreateRegularPolygon
   Name/de: Sketcher RegelmäßigesVieleckErstellen
   MenuLocation: Sketch , Skizzengeometrien , Regelmäßiges Vieleck erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **P** **R**
---

# Sketcher CreateRegularPolygon/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:24px;"> [Sketcher RegelmäßigesVieleckErstellen](Sketcher_CreateRegularPolygon/de.md) erstellt ein regelmäßiges Vieleck (Polygon) creates a regular polygon.



## Anwendung

Siehe auch: [Zeichnungshilfen](Sketcher_Workbench/de#Zeichnungshilfen.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences/de#Allgemein.md) (In-Ansicht-Parameter zur Lagebestimmung). {{Version/de|1.0}}
Dim-OVP = Dimensional On-View-Parameters (In-Ansicht-Parameter zur maßlichen Festlegung). {{Version/de|1.0}}

1.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_CreateRegularPolygon.svg" width=16px> [Regelmäßiges Vieleck](Sketcher_CreateRegularPolygon/de.md)** drücken.
    -   Den Menüeintrag **Sketcher → Sketcher geometries → <img src="images/Sketcher_CreateRegularPolygon.svg" width=16px> Regelmäßiges Vieleck erstellen** auswählen.
    -   Das Tastaturkürzel **G** dann **P** dann **R**.
2.  Die **Anzahl der Seiten** im Dialog **Regelmäßiges Vieleck erstellen** eingeben.
3.  Der Mauszeiger wandelt sich zu einem Kreuz mit Werkzeugsymbol.
4.  Der Abschnitt **Vieleckparameter** ({{Version/de|1.0}}) wird im oberen Bereich des [Sketcher-Dialogs](Sketcher_Dialog.md) hinzugefügt.
5.  Wahlweise die **Anzahl der Seiten** ändern (dies kann auch nach der Auswahl des Mittelpunktes geschehen):
    -   Eine Zahl größer als zwei eingeben.
    -   Die **U**-Taste drücken, um die Zahl zu erhöhen.
    -   Die **J**-Taste drücken, um die Zahl zu verringern.
6.  Den Mittelpunkt des Vielecks auswählen. Oder mit Pos-OVP: seine X- und/oder Y\--Koordinate eingeben.
7.  Den ersten Punkt des Vielecks auswählen; dies legtauch den Radius des Umkreises fest. Oder mit Dim-OVP: den Radius des Kreises und/oder den Winkel des ersten Punktes eingeben. Der Winkel bezieht sich auf die X-Achse der Skizze. Für diesen Winkel wird keine Randbedingung erstellt.
8.  Das Vieleck wird erstellt, inklusive eines Hilfsgeometrie-Umkreises und der anwendbaren Pos-OVP- und Dim-OVP-basierten Randbedingungen.
9.  Wenn das Werkzeug im [Fortsetzen-Modus](Sketcher_Workbench/de#Fortsetzen-Modi.md) läuft:
    1.  Wahlweise weitere Vielecke erstellen.
    2.  Zum Beenden die rechte Maustaste oder **Esc** drücken oder ein anderes Werkzeug zur Erstellung von Geometrien oder Randbedingungen aufrufen.



## Hinweise

-   Der Hilfsgeometrie-Kreis ist außerhalb der Skizze nicht sichtbar. Er kann nicht entfernt werden, ohne die Geometrie des Vielecks aufzubrechen.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateRegularPolygon/de

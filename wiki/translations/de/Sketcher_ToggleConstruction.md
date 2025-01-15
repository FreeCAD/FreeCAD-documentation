---
 GuiCommand:
   Name: Sketcher ToggleConstruction
   Name/de: Sketcher HilfsgeometrieUmschalten
   MenuLocation: Skizze , Skizzengeometrien , Hilfsgeometrie umschalten
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **N**
   SeeAlso: 
---

# Sketcher ToggleConstruction/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:24px;"> [Sketcher HilfsgeometrieUmschalten](Sketcher_ToggleConstruction/de.md) aktiviert bzw. deaktiviert den Konstruktionsmodus für alle Werkzeuge zur Geometrieerstellung oder es wandelt ausgewählte normale Geometrie in Hilfsgeometrie und umgekehrt.

Hilfsgeometrie wird mit einer bestimmten [Farbe](Sketcher_Preferences/de#Darstellung.md) (standardmäßig Blau) gekennzeichnet und ({{Version/de|1.0}}) mit einer bestimmten Linienart. Hilfsgeometrie ist außerhalb der Skizze nicht sichtbar; sie ist dafür gedacht, bei der Festlegung von Randbedingungen und anderen Geometrien innerhalb der Skizze zu helfen. Hilfslinien können trotzdem als Drehachse für ein [PartDesign Drehteil](PartDesign_Revolution/de.md) verwendet werden.

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:480px;">



## Anwendung



### Werkzeuge umschalten 

1.  Sicherstellen, dass die Auswahl leer ist.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_ToggleConstruction.svg" width=16px> [Hilfsgeometrie umschalten](Sketcher_ToggleConstruction/de.md)** drücken.
    -   Den Menüeintrag **Skizze → Skizzengeometrien → <img src="images/Sketcher_ToggleConstruction.svg" width=16px> Hilfsgeometrie umschalten** auswählen.
    -   Ein Rechtsklick in die [3D-Ansicht](3D_view/de.md) und die Menüoption **<img src="images/Sketcher_ToggleConstruction.svg" width=16px> Hilfsgeometrie umschalten** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **G** dann **N**.
3.  Der Modus der Werkzeuge zur Geometrieerstellung wird umgeschaltet:
    -   Im normalen Modus sind ihre Menü- und Werkzeugleistensymbole weiß und sie erstellen normale Geometrie (Standardfarbe Weiß). Das Symbol dieses Werkzeugs ist dann: <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:16px;">.
    -   Im Hilfsgeometrie-Modus (Konstruktionsmodus) sind ihre Menü- und Werkzeugleistensymbole blau und sie erstellen Hilftgeometrie (Standardfarbe Blau). Das Symbol dieses Werkzeugs ist dann: <img alt="" src=images/Sketcher_ToggleConstruction_Constr.svg  style="width:16px;">.



### Geometrie umschalten 

1.  Ein oder mehrere Elemente in der Skizze auswählen.
2.  Das Werkzeug wie oben beschrieben aufrufen oder mit der folgenden zusätzlichen Möglichkeit:
    -   Ein Rechtsklick in den Abschnitt **Elemente** des [Sketcher-Dialogs](Sketcher_Dialog/de.md) und die Menüoption **<img src="images/Sketcher_ToggleConstruction.svg" width=16px> Hilfsgeometrie umschalten** im Kontextmenü auswählen.
3.  Die ausgewählten Elemente wechseln von normaler Geometrie zu Hilfsgeometrie oder umgekehrt. Ihre Darstellung passt sich entsprechend an.
4.  Der Modus der Werkzeuge zur Geometrieerstellung ändert sich nicht.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleConstruction/de

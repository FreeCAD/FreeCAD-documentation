---
- GuiCommand:/de
   Name:Sketcher CarbonCopy
   Name/de:Skizzierer Kopie
   MenuLocation:Skizze → Skizzengeometrien → Kopie
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   Version:0.17
---

# Sketcher CarbonCopy/de

## Beschreibung

Das **<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> [Skizzierer Kopie](Sketcher_CarbonCopy/de.md)** Werkzeug kopiert alle Geometrien und Beschränkungen aus einer anderen Skizze in die aktive Skizze.

Maßbeschränkungen, die vor der Kopierfunktion bestehen, bleiben über [ Ausdrücke](expressions/de.md) mit den Maßbeschränkungen der Originalskizze verknüpft.

## Anwendung

1.  Vergewissere dich, dass du dich im Bearbeitungsmodus einer vorhandenen **<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Skizze](Sketcher_NewSketch/de.md)** befindest. Diese Skizze ist das Ziel der Handlung.
2.  Drücke die **<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> [Kopie](Sketcher_CarbonCopy/de.md)** Schaltfläche.
3.  Klicke auf eine Kante aus einer anderen Skizze. (Diese Skizze ist die Quelle der Handlung).
4.  Sowohl Geometrieelemente als auch Beschränkungen werden in die aktive Skizze kopiert.
5.  Drücke **Esc** oder die rechte Maustaste, um den Vorgang zu beenden.

## Anmerkungen

-   Wenn Skizzen im <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> <img src=images/PartDesign_Body.svg style="width:PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) verwendet werden, sollte normalerweise die Skizze zur Kopie im gleichen **[16px"> [PartDesign Körper](PartDesign_Body/de.md)** wie die derzeit aktive Skizze sein. Wenn sich die zu kopierende Skizze nicht in der aktiven Skizze [Körper](PartDesign_Body/de.md) befindet, lässt der Mauszeiger keine Auswahl zu. Halte in diesem Fall **Ctrl** gedrückt, um die Auswahl von Skizzen aus anderen Körpern zu ermöglichen.
-   Normalerweise sollte sich die auszuwählende Skizze in einer Ebene befinden, die parallel zur derzeit aktiven Skizze liegt. Wenn die zu kopierende Skizze nicht parallel zur derzeit aktiven Skizze ist, halte **Strg**+**Alt** gedrückt, um die Auswahl nicht-paralleler Skizzen zu ermöglichen. Das Objekt wird dann an die Ebene der aktiven Skizze angepasst. Hinweisː ab diesem Schreiben muss das Dokument gespeichert und neu geladen werden, um es sichtbar zu machen. Dies funktioniert auch für Skizzen, die sich außerhalb der aktiven Skizze [Körper](PartDesign_Body/de.md) befinden.
-   Da kopierte Maßbeschränkungen Ausdrücke verwenden, werden sie in einer anderen Farbe gerendert. Die Farbe kann mit dem [Voreinstellungeneditor](Preferences_Editor/de.md) unter **Bearbeiten → Einstellungen → Skizzierer → Farben → Ausdrucksabhängige Beschränkungsfarbe** angepasst werden.
-   Wenn der Skizzierer Modus mit **<img src=images/Sketcher_ToggleConstruction.svg style="width:24px"> in den Konstruktionsmodus umgeschaltet wurde [Umschalten Konstruktion](Sketcher_ToggleConstruction/de.md)** werden alle kopierten Geometrien im Konstruktionsmodus erstellt.

## Begrenzungen

-   Die komplette Skizze wird kopiert, es ist nicht möglich, nur einen Teil davon auszuwählen. Nach dem Kopieren kannst du jedoch unerwünschte Elemente aus der kopierten Skizze löschen.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CarbonCopy/de

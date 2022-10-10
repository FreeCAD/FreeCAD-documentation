---
- GuiCommand   */de
   Name   *Sketcher CarbonCopy
   Name/de   *Sketcher Pause
   MenuLocation   *Sketch → Skizzengeometrien → Pause
   Workbenches   *[Sketcher](Sketcher_Workbench/de.md)
   Shortcut   ***G** **W**
   Version   *0.17
---

# Sketcher CarbonCopy/de

## Beschreibung

Das **[<img src=images/Sketcher_CarbonCopy.svg style="width   *16px"> [Skizzierer Kopie](Sketcher_CarbonCopy/de.md)** Werkzeug kopiert alle Geometrien und Beschränkungen aus einer anderen Skizze in die aktive Skizze.

Maßbeschränkungen, die vor der Kopierfunktion bestehen, bleiben über [ Ausdrücke](expressions/de.md) mit den Maßbeschränkungen der Originalskizze verknüpft.

## Anwendung

1.  Eine vorhandene **[<img src=images/Sketcher_NewSketch.svg style="width   *16px"> [Skizze](Sketcher_NewSketch/de.md)** sollte im Bearbeitungsmodus geöffnet sein. Diese Skizze ist das Ziel dieses Vorgangs.

2.  Die Schaltfläche **[<img src=images/Sketcher_CarbonCopy.svg style="width   *16px"> [Pause](Sketcher_CarbonCopy/de.md)** drücken.

3.  Auf eine Kante aus einer anderen Skizze klicken. (Diese Skizze ist die Quelle des Vorgangs).

4.  Sowohl Geometrieelemente als auch Randbedingungen werden in die aktive Skizze kopiert (\"durchgepaust\").

5.  
    **Esc**oder die rechte Maustaste drücken, um den Vorgang zu beenden.

## Anmerkungen


<div class="mw-translate-fuzzy">

-   Wenn Skizzen im <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) verwendet werden, sollte normalerweise die Skizze zur Kopie im gleichen **[<img src=images/PartDesign_Body.svg style="width   *16px"> [PartDesign Körper](PartDesign_Body/de.md)** wie die derzeit aktive Skizze sein. Wenn sich die zu kopierende Skizze nicht in der aktiven Skizze [Körper](PartDesign_Body/de.md) befindet, lässt der Mauszeiger keine Auswahl zu. Halte in diesem Fall **Ctrl** gedrückt, um die Auswahl von Skizzen aus anderen Körpern zu ermöglichen.
-   Normalerweise sollte sich die auszuwählende Skizze in einer Ebene befinden, die parallel zur derzeit aktiven Skizze liegt. Wenn die zu kopierende Skizze nicht parallel zur derzeit aktiven Skizze ist, halte **Strg**+**Alt** gedrückt, um die Auswahl nicht-paralleler Skizzen zu ermöglichen. Das Objekt wird dann an die Ebene der aktiven Skizze angepasst. Hinweisː ab diesem Schreiben muss das Dokument gespeichert und neu geladen werden, um es sichtbar zu machen. Dies funktioniert auch für Skizzen, die sich außerhalb der aktiven Skizze [Körper](PartDesign_Body/de.md) befinden.
-   Da kopierte Maßbeschränkungen Ausdrücke verwenden, werden sie in einer anderen Farbe gerendert. Die Farbe kann mit dem [Voreinstellungeneditor](Preferences_Editor/de.md) unter **Bearbeiten → Einstellungen → Skizzierer → Farben → Ausdrucksabhängige Beschränkungsfarbe** angepasst werden.
-   Wenn der Skizzierer Modus mit **[<img src=images/Sketcher_ToggleConstruction.svg style="width   *24px"> in den Konstruktionsmodus umgeschaltet wurde [Umschalten Konstruktion](Sketcher_ToggleConstruction/de.md)** werden alle kopierten Geometrien im Konstruktionsmodus erstellt.


</div>

## Begrenzungen

-   Die komplette Skizze wird kopiert, es ist nicht möglich, nur einen Teil davon auszuwählen. Nach dem Kopieren kannst du jedoch unerwünschte Elemente aus der kopierten Skizze löschen.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CarbonCopy/de

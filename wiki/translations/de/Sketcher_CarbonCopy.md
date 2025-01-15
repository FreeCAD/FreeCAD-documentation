---
 GuiCommand:
   Name: Sketcher CarbonCopy
   Name/de: Sketcher Pause
   MenuLocation: Skizze , Sketcher-Werkzeuge , Blaupause erstellen
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **W**
   Version: 0.17
---

# Sketcher CarbonCopy/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:24px;"> [Sketcher Pause](Sketcher_CarbonCopy/de.md) paust (kopiert) alle Geometrien und Randbedingungen aus einer anderen Skizze in die aktive Skizze durch.

Maßliche Randbedingungen, die vor der Pausfunktion bestehen, bleiben über [Ausdrücke](Expressions/de.md) mit den maßliche Randbedingungen der Originalskizze verknüpft.



## Anwendung

1.  Eine vorhandene [Skizze](Sketcher_NewSketch/de.md) sollte im Bearbeitungsmodus geöffnet sein. Diese Skizze ist das Ziel dieses Vorgangs.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Sketcher_CarbonCopy.svg" width=16px> [Blaupause erstellen](Sketcher_CarbonCopy.md)** drücken.
    -   Den Menüeintrag **Skizze → Sketcher-Werkzeuge → <img src="images/Sketcher_CarbonCopy.svg" width=16px> Blaupause erstellen** auswählen.
    -   Das Tastaturkürzel **G** dann **W**.
3.  Der Mauszeiger wandelt sich in ein Kreuz mit dem entsprechenden Werkzeugsymbol.
4.  Eine Kante aus einer anderen Skizze auswählen. Diese Skizze ist die Quelle dieses Vorgangs. Siehe [Hinweise](#Hinweise.md).
5.  Sowohl Geometrieelemente als auch Randbedingungen werden in die aktive Skizze kopiert (\"durchgepaust\").
6.  Dieses Werkzeug läuft immer im Fortsetzen-Modus: Wahlweise weitere Skizzen kopieren.
7.  Zum Beenden die rechte Maustaste oder **Esc** drücken oder ein anderes Werkzeug zum Erstellen von Geometrie oder Randbedingungen aufrufen.



## Anmerkungen

-   Im Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) kann die Skizze zum Durchpausen von außerhalb des [Körpers](PartDesign_Body/de.md) der gerade aktiven Skizze ausgewählt werden, aber nur wenn während der Auswahl die **Ctrl**- bzw. **Strg**-Taste gedrückt gehalten wird.
-   Die Skizze zum Durchpausen sollte parallel zur gerade aktiven Skizze liegen. Ist dies nicht der Fall müssen die **Ctrl**- und die **Alt**-Taste während der Auswahl gedrückt gehalten werden. Dies funktioniert auch mit Skizzen, die sich außerhalb des aktiven Körpers befinden.
-   Ist der [Konstruktionsmodus](Sketcher_ToggleConstruction/de.md) aktiv, wird die kopierte Geometrie als Hilfsgeometrie erstellt.
-   Die komplette Skizze wird kopiert; es ist nicht möglich nur einen Teilbereich auszuwählen. Aber nach dem Durchpausen können nicht erwünschte Elemente entfernt werden.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CarbonCopy/de

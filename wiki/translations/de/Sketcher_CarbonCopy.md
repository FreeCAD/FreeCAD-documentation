---
 GuiCommand:
   Name: Sketcher CarbonCopy
   Name/de: Sketcher Pause
   MenuLocation: Skizze , Skizzengeometrien , Pause
   Workbenches: Sketcher_Workbench/de
   Shortcut: **G** **W**
   Version: 0.17
---

# Sketcher CarbonCopy/de



## Beschreibung

Das Werkzeug **[<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> [Sketcher Pause](Sketcher_CarbonCopy/de.md)** paust (kopiert) alle Geometrien und Randbedingungen aus einer anderen Skizze in die aktive Skizze durch.

Maßliche Randbedingungen, die vor der Pausfunktion bestehen, bleiben über [Ausdrücke](expressions/de.md) mit den maßliche Randbedingungen der Originalskizze verknüpft.



## Anwendung

1.  Eine vorhandene **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Skizze](Sketcher_NewSketch/de.md)** sollte im Bearbeitungsmodus geöffnet sein. Diese Skizze ist das Ziel dieses Vorgangs.

2.  Die Schaltfläche **[<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> [Pause](Sketcher_CarbonCopy/de.md)** drücken.

3.  Auf eine Kante aus einer anderen Skizze klicken. (Diese Skizze ist die Quelle des Vorgangs).

4.  Sowohl Geometrieelemente als auch Randbedingungen werden in die aktive Skizze kopiert (\"durchgepaust\").

5.  
    **Esc**oder die rechte Maustaste drücken, um den Vorgang zu beenden.



## Anmerkungen

-   Wenn Skizzen im Arbeitsbereich <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/de.md) verwendet werden, sollte sich die durchzupausende Skizze normalerweise im selben **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper](PartDesign_Body.md)** befinden, wie die aktuell aktive Skizze. Ist die zu kopierende Skizze nicht im aktiven [Körper](PartDesign_Body.md), wird der Mauszeiger keine Auswahl zulassen. In diesem Falle hält man **Ctrl** gedrückt, um die Auswahl von Skizzen aus anderen Körpern zu erlauben.
-   Normalerweise soll die auszuwählende Skizze auf einer Ebene parallel zur Skizzenebene liegen. Ist die zu kopierende Skizze nicht parallel zur aktuell aktiven Skizze, hält man **Ctrl** + **Alt** gedrückt, um die Auswahl von nicht parallelen Skizzen zu erlauben. Das Objekt wird dann auf die Ebene der aktiven Skizze angepasst. Achtung: Zum Zeitpunkt des Schreibens muss das Dokument noch gespeichert und wieder geöffnet werden, damit die Anpassung sichtbar wird. Dies funktioniert auch mit Skizzen, die sich außerhalb des aktiven [Körpers](PartDesign_Body/de.md) befinden.
-   Da durchgepauste maßliche Randbedingungen Ausdrücke (Expressions) verwenden, werden sie in einer anderen Farbe dargestellt. Die Farbe kann mit dem [Voreinstellungseditor](Preferences_Editor/de.md) unter **Bearbeiten → Einstellungen → Skizze → Farben → Ausdrucksabhängige Beschränkung** angepasst werden.
-   Wenn der Sketcher-Modus mit ** [<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [UmschalterKonstruktion](Sketcher_ToggleConstruction/de.md)** in den Konstruktionsmodus umgeschaltet wurde, werden alle kopierten Geometrien im Konstruktionsmodus erstellt.



## Begrenzungen

-   Die komplette Skizze wird kopiert, es ist nicht möglich, nur einen Teil davon auszuwählen. Nach dem Kopieren können jedoch unerwünschte Elemente aus der kopierten Skizze gelöscht werden.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CarbonCopy/de

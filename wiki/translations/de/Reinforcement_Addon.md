# Reinforcement Addon/de
## Einleitung

Das Addon [Reinforcement](Reinforcement_Addon/de.md) (Armierung) ergänzt den Arbeitsbereich [Arch](Arch_Workbench/de.md) durch neue Schnittstellen und Voreinstellungen für das Erstellen gängiger Bewehrungsarten zur Verwendung mit [Arch Struktur](Arch_Structure/de.md)-Objekten.

Die Werkzeuge können mit dem [Addon-Manager](Std_AddonMgr/de.md) über das Menü **Werkzeuge → Addon-Manager → Reinforcement** installiert werden. FreeCAD muss neu gestartet werden, damit die neuen Werkzeuge unter der Schaltfläche **<img src="images/Arch_Rebar.svg" width=16px>  [Custom Rebar](Arch_Rebar/de.md)** erscheinen.

Diese Erweiterung wurde während des [Google Summer of Code](Google_Summer_of_Code.md) 2017 entwickelt, und wird in der Github-Datenablage [FreeCAD-Reinforcement](https://github.com/amrit3701/FreeCAD-Reinforcement) bereitgestellt, die von der Haupt-Datenablage von FreeCAD getrennt ist.



## Elemente

Der Arbeitsbereich Arch enthält nur ein Bewehrungswerkzeug:

-   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Bewehrung](Arch_Rebar/de.md): Erstellt eine auf einer [Skizze](Sketcher_Workbench/de.md) basierende, individuell angepasste Bewehrung in einem ausgewählten [Arch Struktur](Arch_Structure/de.md)-Objekt.

Das Addon Reinforcement enthält zusätzliche Armierungsarten:

-   <img alt="" src=images/Arch_Rebar_Straight.svg  style="width:32px;"> [Geradlinige Bewehrung](Arch_Rebar_Straight/de.md): erstellt einen geraden Bewehrungsstab.
-   <img alt="" src=images/Arch_Rebar_UShape.svg  style="width:32px;"> [U-förmige Bewehrung](Arch_Rebar_UShape/de.md): erstellt einen U-förmigen Bewehrungsstab.
-   <img alt="" src=images/Arch_Rebar_LShape.svg  style="width:32px;"> [L-förmige Bewehrung](Arch_Rebar_LShape/de.md): erstellt einen L-förmigen Bewehrungsstab.
-   <img alt="" src=images/Arch_Rebar_BentShape.svg  style="width:32px;"> [Abgesetzte Bewehrung](Arch_Rebar_BentShape/de.md): erstellt einen Bewehrungsstab mit Absatz.
-   <img alt="" src=images/Arch_Rebar_Stirrup.svg  style="width:32px;"> [Bewehrungsbügel](Arch_Rebar_Stirrup/de.md): erstellt einen Bewehrungsbügel.
-   <img alt="" src=images/Arch_Rebar_Helical.svg  style="width:32px;"> [Wendelbewehrung](Arch_Rebar_Helical/de.md): erstellt eine Wendelbewehrung.

Neue Werkzeuge mit grafischer Schnittstelle zur Eingabe von Werten

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Arch Armierung Rundsäulenbewehrung](Arch_Rebar_Circular_ColumnReinforcement/de.md)
-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Arch Armierung Säulenbewehrung](Arch_Rebar_ColumnReinforcement/de.md)
-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Arch Armierung Säulenbewehrung ZweiBügelSechsStäbe](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/de.md)
-   <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> [Arch Armierung Balkenbewehrung](Arch_Rebar_BeamReinforcement/de.md)



## Externe Arbeitsbereiche 

FreeCAD-Arbeitsbereiche können einfach in [Python](Python/de.md) programmiert werden, daher gibt es viele Leute außerhalb der FreeCAD-Hauptentwickler, die zusätzliche Arbeitsbereiche entwickeln.

Die Seite [externe Arbeitsbereiche](external_workbenches/de.md) enthält einige Informationen und Anleitungen zu einigen von ihnen, und das Projekt [FreeCAD-Addons](https://github.com/FreeCAD/FreeCAD-addons) hat sich zum Ziel gesetzt, diese zu sammeln und sie von FreeCAD aus leicht installierbar zu machen.

Neue Arbeitsbereiche sind in Entwicklung, bleib dran!



---
⏵ [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Category_Arch.md) > Reinforcement Addon/de

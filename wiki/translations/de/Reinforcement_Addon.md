# Reinforcement Addon/de
## Einleitung

Das [Armierung Erweiterung](Reinforcement_Addon/de.md) ergänzt die [Arch Arbeitsbereich](Arch_Workbench/de.md) durch neue Schnittstellen und Voreinstellungen für die Erstellung gängiger Bewehrungsarten zur Verwendung mit [Arch Strukturen](Arch_Structure/de.md).

Die Werkzeuge können mit dem [Erweiterungsmanager](Addon_Manager/de.md) über das Menü {{MenuCommand/de|Werkzeuge → Addon Manager → Bewehrung}} installiert werden. FreeCAD muss neu gestartet werden, damit die neuen Werkzeuge unter der **<img src="images/Arch_Rebar.svg" width=16px>  [Arch Bewehrung](Arch_Rebar/de.md)**Schaltfläche erscheinen.

Diese Erweiterung wurde während des [Google Summer of Code](Google_Summer_of_Code.md) 2017 entwickelt, und wird im Github Repositorium [FreeCAD Armierung](https://github.com/amrit3701/FreeCAD-Reinforcement) Github bereitgestellt, das vom Haupt Repositorium von FreeCAD getrennt ist.

## Elemente

Der Arch Arbeitsbereich bietet nur ein Bewehrungswerkzeug:

-   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> _ unter Verwendung einer [Skizze](Sketcher_Workbench/de.md).

Die Bewehrungserweiterung bietet zusätzliche Armierungsarten:

-   <img alt="" src=images/Arch_Rebar_Straight.svg  style="width:32px;"> [Gerade Bewehrung](Arch_Rebar_Straight/de.md): erzeugt einen geraden Bewehrungsstab.
-   <img alt="" src=images/Arch_Rebar_UShape.svg  style="width:32px;"> [UFörmige Bewehrung](Arch_Rebar_UShape/de.md): erzeugt einen U-förmigen Bewehrungsstab.
-   <img alt="" src=images/Arch_Rebar_LShape.svg  style="width:32px;"> [LFörmige Bewehrung](Arch_Rebar_LShape/de.md): erzeugt einen L-förmigen Bewehrungsstab.
-   <img alt="" src=images/Arch_Rebar_BentShape.svg  style="width:32px;"> [Gebogener Formstab](Arch_Rebar_BentShape/de.md): erzeugt einen gebogenen Bewehrungsstab.
-   <img alt="" src=images/Arch_Rebar_Stirrup.svg  style="width:32px;"> [Bügelbewehrung](Arch_Rebar_Stirrup/de.md): erzeugt einen schlaufenförmigen Bewehrungsstab.
-   <img alt="" src=images/Arch_Rebar_Helical.svg  style="width:32px;"> [Spiralförmige Bewehrung](Arch_Rebar_Helical/de.md): erzeugt einen spiralförmigen Bewehrungsstab.

Neue Werkzeuge mit grafischer Oberfläche zur Eingabe von Werten

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Arch Bewehrung Rundsäulenverstärkung](Arch_Rebar_Circular_ColumnReinforcement/de.md)
-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Arch BewehrungStützenverstärkung ](Arch_Rebar_ColumnReinforcement/de.md)
-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Arch Bewehrung Stützenbewehrung ZweiBinderSechsStützen](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/de.md)
-   <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> [Arch Bewehrung BalkenBewehrung](Arch_Rebar_BeamReinforcement/de.md)

## Externe Arbeitsbereiche 

FreeCAD Arbeitsbereiche sind einfach in [Python](Python/de.md) zu programmieren, daher gibt es viele Leute, die zusätzliche Arbeitsbereiche außerhalb der FreeCAD Hauptentwickler entwickeln.

Die Seite [externe Arbeitsbereiche](external_workbenches/de.md) enthält einige Informationen und Anleitungen zu einigen von ihnen, und das Projekt [FreeCAD Erweiterungen](https://github.com/FreeCAD/FreeCAD-addons) hat sich zum Ziel gesetzt, diese zu sammeln und sie von FreeCAD aus leicht installierbar zu machen.

Neue Arbeitsbereiche sind in Entwicklung, bleib dran!


 

_

---
[documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement Addon/de

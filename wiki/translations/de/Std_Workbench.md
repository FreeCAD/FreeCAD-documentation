---
 GuiCommand:
   Name: Std Workbench
   Name/de: Std Arbeitsbereich
   MenuLocation: Ansicht , Arbeitsbereich
   Workbenches: Alle
---

# Std Workbench/de



## Beschreibung

Der Befehl **Std Arbeitsbereich** aktiviert einen ausgewählten [Arbeitsbereich](Workbenches/de.md).

![](images/Std_Workbench_ComboBox_Icons_And_Text.png ) 
*Die voreingestellte Arbeitsbereichsauswahl als ComboBox*

![](images/Std_Workbench_TabBar_Icons_Only.png ) 
*Die optionale Arbeitsbereichsauswahl als Tab-Leiste (hier die Darstellung nur mit Symbolen) {{Version/de|1.0*}}



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Einen Arbeitsbereich in der Combo-Ansicht oder in der Tab-Leiste (<small>(v1.0)</small> ) der Symbolleiste Arbeitsbereich auswählen.
    -   Die Schaltfläche **<img src="images/List-add.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** in der Tab-Leiste drücken, um einen Arbeitsbereich, der in den [Voreinstellungen](Preferences_Editor/de#Vorhandene_Arbeitsbereiche.md) deaktiviert wurde, in dem Menü auszuwählen, das geöffnet wird.
    -   Einen Arbeitsbereich im Untermenü **Ansicht → Arbeitsbereich** auswählen.



## Hinweise

-   Zusätzliche [Externe Arbeitsbereiche](External_workbenches/de.md) können mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) heruntergeladen werden.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md).

-   Es gibt eine [Seite mit zugehörigen Einstellungen](Preferences_Editor/de#Vorhandene_Arbeitsbereiche.md): **Bearbeiten → Einstellungen... → Arbeitsbereiche → Vorhandene Arbeitsbereiche**. Der **Startarbeitsbereich**, die **Arbeitsbereichsauswahl** und weitere können angepasst werden. Mit der Schaltfläche **<img src="images/List-add.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** in der Tab-Leiste kann man über ihr Menü auf diese Seite zugreifen.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Um den Arbeitsbereich zu ändern, wird die Methode `activateWorkbench` des FreeCADGui-Moduls verwendet.


```python
import FreeCADGui

FreeCADGui.activateWorkbench("PartDesignWorkbench")
```





{{Std Base navi

}}  {{Interface navi}}



---
⏵ [documentation index](../README.md) > Std Workbench/de

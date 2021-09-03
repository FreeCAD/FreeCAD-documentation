---
- GuiCommand:/de
   Name:Std Workbench
   Name/de:Std Arbeitsbereich
   MenuLocation:Ansicht → Arbeitsbereich
   Workbenches:Alle
   SeeAlso:[Arbeitsbereiche](Workbenches/de.md)
---

## Beschreibung

Der **Std Arbeitsbereich** aktiviert einen ausgewählten [Arbetsbereich](Workbenches/de.md) einschließlich ihrer grafischen Benutzeroberfläche (GUI).

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:800px;"> 
*Die Arbeitsbereich Auswahlliste ist im Standard mit der Nummer 10 gekennzeichnet [Oberfläche](interface/de.md)*

## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Wähle einen Arbeitsbereich aus der **Arbeitsbereichs Auswahlliste** in der Arbeitsbereich Werkzeugleiste. Diese Option ist nicht verfügbar, wenn der aktuelle Arbeitsbereich ist `<none>` (kein Arbeitsbereich).
    -   Wähle einen Arbeitsbereich aus dem {{MenuCommand|Ansicht → Arbeitsbereich}} Untermenü.

## Hinweise

-   Zusätzliche [Externe Arbeitsbereiche](External_Workbenches/de.md) können mit dem <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Erweiterungsverwalter](Addon_Manager/de.md) heruntergeladen werden.

## Einstellungen

-   Der Startarbeitsbereich kann in den Einstellungen geändert werden: {{MenuCommand|Bearbeiten → Einstellungen... → Allgemein → Allgemein → Hochfahren}}. Siehe [Einstellungseditor](Preferences_Editor/de#General.md).

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um den Arbeitsbereich zu ändern, verwende die `aktiviereArbeitsbereich` Methode des FreeCADGui Moduls. Diese Methode ist nicht verfügbar, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.activateWorkbench("PartDesignWorkbench")
```





{{Std Base navi

}}  {{Interface navi}} 

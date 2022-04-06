---
- GuiCommand:/de
   Name:Std Workbench
   Name/de:Std Arbeitsbereich
   Empty:1
   MenuLocation:Ansicht → Arbeitsbereich
   Workbenches:Alle
   SeeAlso:[Arbeitsbereiche](Workbenches/de.md)
---

# Std Workbench/de

## Beschreibung

Der Befehl **Std Arbeitsbereich** aktiviert einen ausgewählten [Arbeitsbereich](Workbenches/de.md) einschließlich seiner grafischen Benutzeroberfläche (GUI).

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:800px;"> 
*Die Auswahlliste der Arbeitsbereiche auf der Standard-[Oberfläche](interface/de.md) ist mit der Nummer 10 gekennzeichnet.*

## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Auswahl eines Arbeitsbereiches aus der **Auswahlliste** in der Symbolleiste **Arbeitsbereich**. Diese Option ist nicht verfügbar, wenn der aktuelle Arbeitsbereich `<none>` (kein Arbeitsbereich) ist.
    -   Auswahl eines Arbeitsbereiches aus dem Untermenü **Ansicht → Arbeitsbereich**.

## Hinweise

-   Zusätzliche [Externe Arbeitsbereiche](External_workbenches/de.md) können mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) heruntergeladen werden.

## Einstellungen

-   Der Startarbeitsbereich kann in den Einstellungen geändert werden: **Bearbeiten → Einstellungen... → Allgemein → Allgemein → Hochfahren**. Siehe [Voreinstellungseditor](Preferences_Editor/de#Allgemeines.md).

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um den Arbeitsbereich zu ändern, verwende die Methode `activateWorkbench` des FreeCADGui-Moduls. Diese Methode ist nicht verfügbar, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.activateWorkbench("PartDesignWorkbench")
```





{{Std Base navi

}}  {{Interface navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Workbench/de

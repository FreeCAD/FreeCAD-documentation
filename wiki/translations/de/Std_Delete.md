---
 GuiCommand:
   Name: Std Delete
   Name/de: Std Löschen
   MenuLocation: Bearbeiten , Löschen
   Workbenches: Alle
   Shortcut: **Del**
---

# Std Delete/de



## Beschreibung

Der **Std Löschen** Befehl löscht die ausgewählten Objekte.



## Anwendung

1.  Wähle ein oder mehrere Objekte.
    -   Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Wähle die **Bearbeiten → <img src="images/Std_Delete.svg" width=16px> Löschen** Option aus dem Menü.
    -   Wähle die **<img src="images/Std_Delete.svg" width=16px> Löschen** Option

aus dem Kontextmenü der [Baumansicht](Tree_view/de.md) oder dem Kontextmenü der [3D Ansicht](3D_view/de.md).

#\* Verwende das Tastaturkürzel: **Del**.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Um ein Objekt zu löschen, verwende die Methode `removeObject` des Dokumentobjekts.


```python
import FreeCAD

FreeCAD.ActiveDocument.removeObject("myObjectName")
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std Delete/de

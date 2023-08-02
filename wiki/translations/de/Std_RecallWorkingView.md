---
- GuiCommand:
   Name: Std RecallWorkingView
   Name/de: Std ArbeitsansichtWiederherstellen
   MenuLocation: Ansicht -> Standardansichten -> Arbeitsansicht wiederherstellen
   Workbenches: Alle
   Shortcut: **End**
   Version: 0.21
   SeeAlso: Std_StoreWorkingView/de, Std_FreezeViews/de
---

# Std RecallWorkingView/de



## Beschreibung

Der Befehl **Std ArbeitsansichtWiederherstellen** stellt die gespeicherte Arbeitsansicht der aktiven [3D-Ansicht](3D_view.md) wieder her. Für weitere Informationen siehe [Std ArbeitsansichtSpeichern](Std_StoreWorkingView/de.md).



## Anwendung

1.  Sicherstellen, dass eine [3D-Ansicht](3D_view/de.md) aktiv ist, für die der Befehl [Std ArbeitsansichtSpeichern](Std_StoreWorkingView.md) wenigstens einmal verwendet wurde.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Den Menüeintrag **Ansicht → Standardansichten → Arbeitsansicht wiederherstellen** auswählen.
    -   Das Tastaturkürzel **End**.



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Wiederherstellen der gespeicherten Arbeitsansicht der aktiven 3D-Ansicht:


```python
import FreeCADGui

FreeCADGui.runCommand("Std_RecallWorkingView", 0)
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std RecallWorkingView/de

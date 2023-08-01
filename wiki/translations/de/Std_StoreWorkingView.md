---
- GuiCommand:/de
   Name:Std StoreWorkingView
   Name/de:Std ArbeitsansichtSpeichern
   MenuLocation:View → Standardansichten → Arbeitsansicht speichern
   Workbenches:Alle
   Shortcut:**Shift**+**End**
   Version:0.21
   SeeAlso:[Std ArbeitsansichtWiederherstellen](Std_RecallWorkingView/de.md), [Std AnsichtenEinfrieren](Std_FreezeViews/de.md)
---

# Std StoreWorkingView/de



## Beschreibung

Der Befehl **Std ArbeitsansichtSpeichern** speichert die Kameraeinstellungen der aktiven [3D-Ansicht](3D_view/de.md) als temporäre Arbeitsansicht. Diese Ansicht kann mit dem Befehl [Std ArbeitsansichtWiederherstellen](Std_RecallWorkingView/de.md) wiederhergestellt werden.

Jede 3D-Ansicht hat ihre eigene Arbeitsansicht. Eine neue Arbeitsansicht überschreibt die vorhandene Arbeitsansicht der aktiven 3D-Ansicht. Wird eine 3D-Ansicht geschlossen, geht ihre Arbeitsansicht verloren.



## Anwendung

1.  Sicherstellen, dass eine [3D-Ansicht](3D_view/de.md) aktiv ist.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Den Menüeintrag **Ansicht → Standardansichten → Arbeitsansicht speichern** auswählen.
    -   Das Tastaturkürzel **Shift**+**End**.



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Speichern der aktuellen Kameraeinstellungen der aktiven 3D-Ansicht als Arbeitsansicht:


```python
import FreeCADGui

FreeCADGui.runCommand("Std_StoreWorkingView", 0)
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std StoreWorkingView/de

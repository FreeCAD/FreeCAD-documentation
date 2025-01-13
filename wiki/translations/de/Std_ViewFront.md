---
 GuiCommand:
   Name: Std ViewFront
   Name/de: Std Vorderansicht
   MenuLocation: Ansicht , Standardansichten , Vorderseite
   Workbenches: Alle
   Shortcut: **1**
   SeeAlso: Std_ViewTop/de, Std_ViewRight/de
---

# Std ViewFront/de



## Beschreibung

Der Befehl **Std Vorderansicht** wendet die Kamerasicht der aktiven [3D-Ansicht](3D_view/de.md) in die Richtung der positiven Y-Achse.

![](images/FreeCAD_views_front.svg ) 
*Der Peil 1 zeigt in Richtung der Vorderansicht*



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Std_ViewFront.svg" width=16px> [Vorderansicht](Std_ViewFront/de.md)** drücken.
    -   Den Menüeintrag **Ansicht → Standardansichten → <img src="images/Std_ViewFront.svg" width=16px> Vorderansicht** auswählen.
    -   Die Menüoption **Standardansichten → <img src="images/Std_ViewFront.svg" width=16px> Vorderansicht** im Kontextmenü der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Das Tastaturkürzel **1**.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Die Methode `viewFront` des View-Objekts wird verwendet, um zur Vorderansicht zu wechseln. Methoden für die anderen Hauptausrichtungen der Ansicht stehen auch zur Verfügung: `viewTop`, `viewRight`, `viewRear`, `viewBottom` und `viewRight`.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.viewFront()
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std ViewFront/de

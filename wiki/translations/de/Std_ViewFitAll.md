---
 GuiCommand:
   Name: Std ViewFitAll
   Name/de: Std AnsichtAllesEinpassen
   MenuLocation: Ansicht , Standardansichten‏‎ , Einpassen
   Workbenches: Alle
   Shortcut: **V** **F**
   SeeAlso: Std_ViewFitSelection/de
---

# Std ViewFitAll/de



## Beschreibung

Der Befehl **Std AnsichtAllesEinpassen** zoomt und schwenkt die Kamera, bis alle sichtbaren Objekte in die aktive [3D-Ansicht](3D_view/de.md) passen.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Std_ViewFitAll.svg" width=16px> [Einpassen](Std_ViewFitAll/de.md)** drücken.
    -   Den Menüeintrag **Ansicht → Standardansichten → <img src="images/Std_ViewFitAll.svg" width=16px> Einpassen** auswählen.
    -   Die Menüoption **<img src="images/Std_ViewFitAll.svg" width=16px> Einpassen** im Kontextmenü der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Die Menüoption **<img src="images/Std_ViewFitAll.svg" width=16px> Einpassen** im Miniwürfelmenü des [Navigationswürfels](Navigation_Cube/de.md) auswählen.
    -   Das Tastaturkürzel **V** dann **F**.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Die Methode `fitAll` des View-Objekts wird verwendet, um den Zoomfaktor so zu ändern, dass alles in die Ansicht passt.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.fitAll()
```

Für die aktive Ansicht kann auch die Methode `SendMsgToActiveView` des FreeCADGui-Objekts verwendet werden.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView("ViewFit")
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std ViewFitAll/de

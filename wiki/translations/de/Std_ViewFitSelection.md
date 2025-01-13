---
 GuiCommand:
   Name: Std ViewFitSelection
   Name/de: Std AnsichtAuswahlEinpassen
   MenuLocation: Ansicht , Standardansichten , Auswahl einpassen
   Workbenches: Alle
   Shortcut: **V****S**
   SeeAlso: Std ViewFitAll/de
---

# Std ViewFitSelection/de



## Beschreibung

Der Befehl **Std AnsichtAuswahlEinpassen** zoomt und schwenkt die Kamera, so dass alle ausgewählten Objekte in die aktive [3D-Ansicht](3D_view/de.md) passen. Dieser Befehl ist nützlich, falls sich Objekte außerhalb (der Ränder) der aktuellen 3D-Ansicht befinden oder sich nicht problemlos per [3D-Navigation](Mouse_navigation/de.md) finden lassen.



## Anwendung

1.  Ein oder mehrere Objekte auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Std_ViewFitSelection.svg" width=16px> [Auswahl einpassen](Std_ViewFitSelection/de.md)** drücken.
    -   Den Menüeintrag **Ansicht → Standardansichten → <img src="images/Std_ViewFitSelection.png" width=16px> Auswahl einpassen** auswählen.
    -   Die Menüoption **<img src="images/Std_ViewFitSelection.svg" width=16px> Auswahl einpassen** im Kontextmenü der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Die Menüoption **<img src="images/Std_ViewFitSelection.svg" width=16px> Auswahl einpassen** im Miniwürfel-Menü des [Navigationswürfels](Navigation_Cube/de.md) auswählen.
    -   Das Tastaturkürzel **V**, dann **S**.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Die Methode `SendMsgToActiveView` des FreeCADGui-Objekts kann verwendet werden, um die aktive Ansicht so zu skalieren, dass die Auswahl hinein passt.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView("ViewSelection")
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std ViewFitSelection/de

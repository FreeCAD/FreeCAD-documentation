---
- GuiCommand:/de
   Name:Std ViewFitAll
   Name/de:Std AnsichtAllesEinpassen
   MenuLocation:Ansicht → Standardansichten‏‎ → Einpassen
   Workbenches:Alle
   Shortcut:**V** **F**
   SeeAlso:[Std AnsichtAuswahlEinpassen](Std_ViewFitSelection/de.md)
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


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die Ansicht auf \'Alles einpassen\' zu ändern, verwende die Methode `fitAll` des AktiveAnsicht-Objekts. Diese Methode ist nicht verfügbar, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.fitAll()
```

Alternativ kann die `SendMsgToActiveView`-Methode des FreeCADGui-Objekts benutzt werden. Diese Methode ist im FreeCAD-Konsolenmodus nicht verfügbar.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView('ViewFit')
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewFitAll/de

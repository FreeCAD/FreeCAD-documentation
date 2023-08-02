---
- GuiCommand:
   Name: Std ViewIsometric
   Name/de: Std ViewIsometric
   MenuLocation: Ansicht -> Standardansichten -> Axonometrisch -> Isometrisch
   Workbenches: Alle
   Shortcut: **0**
   SeeAlso: Std_ViewDimetric/de, Std_ViewTrimetric/de
---

# Std ViewIsometric/de



## Beschreibung

Der **Std AnsichtIsometrisch**-Befehl richtet die Kamera in der aktiven [3D-Ansicht](3D_view/de.md) neu aus, um eine [isometrisch](https://de.wikipedia.org/wiki/Axonometrie#Isometrische_Axonometrie)e Ansicht zu erreichen. Für eine wahrlich (truly) trimetrische Ansicht muss die 3D-Ansicht im [orthographischen Modus](Std_OrthographicCamera/de.md) sein, aber der Befehl funktioniert auch, wenn die Ansicht im [perspektivischen Modus](Std_PerspectiveCamera/de.md) ist.

![](images/Std_ViewIsometric_example.svg ) 
*Das [Achsenkreuz](Std_AxisCross/de.md) und ein Würfel in isometrischer Ansicht*



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Std_ViewIsometric.svg" width=16px> [Std Isometrische Ansicht auswählen (0)](Std_ViewIsometric/de.md)** drücken.
    -   Den Menüeintrag **Ansicht → Standardansichten → Axonometrisch → Isometrisch** auswählen.
    -   Die Menüoption **Standardansichten → Axonometrisch → Isometrisch** im Kontextmenü der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Die Menüoption **<img src="images/Std_ViewIsometric.svg" width=16px> Isometric** im Miniwürfelmenü des [Navigationswürfels](Navigation_Cube/de.md) auswählen.
    -   Das Tastaturkürzel: **0**.



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die Ansicht auf isometrisch zu ändern, verwende die Methode `viewIsometric` des AktiveAnsicht Objekts. Diese Methode ist nicht verfügbar, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewIsometric()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIsometric/de

---
- GuiCommand:/de
   Name:Std ViewIsometric
   Name/de:Std ViewIsometric
   MenuLocation:Ansicht → Standardansichten → Axonometrisch → Isometrisch
   Workbenches:Alle
   Shortcut:**0**
   SeeAlso:[Std AnsichtDimetrisch](Std_ViewDimetric/de.md), [Std AnsichtTrimetrisch](Std_ViewTrimetric/de.md)
---

# Std ViewIsometric/de

## Beschreibung

Der **Std AnsichtIsometrisch**-Befehl richtet die Kamera in der aktiven _ sein, aber der Befehl funktioniert auch, wenn die Ansicht im [perspektivischen Modus](Std_PerspectiveCamera/de.md) ist.

![](images/Std_ViewIsometric_example.svg ) 
*Das [Achsenkreuz](Std_AxisCross/de.md) und ein Würfel in isometrischer Ansicht*

## Anwendung

1.  Es gibt verschiedene Wege, den Befehl umzusetzen:
    -   Die **<img src="images/Std_ViewIsometric.svg" width=16px> [Std Isometrische Ansicht auswählen (0)](Std_ViewIsometric/de.md)**-Schaltfläche betätigen.
    -   Den Menüpunkt **Ansicht → Standardansichten → Axonometrisch → Isometrisch** aus dem Menü wählen.
    -   Den Menüpunkt **Standardansichten → Axonometrisch → Isometrisch** aus dem [3D-Ansicht](3D_view/de.md)-Kontextmenü wählen.
    -   Mit dem Tastenkürzel: **0**.

## Hinweise

-   Es ist auch möglich, über das Miniwürfel-Menü des [Navigationswürfels](Navigation_Cube/de.md) in den perspektivischen Ansichtsmodus zu wechseln.

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
[documentation index](../README.md) > Std ViewIsometric/de

---
- GuiCommand:/de
   Name:Std ViewFront
   Name/de:Std Vorderansicht
   MenuLocation:Ansicht → Standardansichten → Vorderseite
   Workbenches:Alle
   Shortcut:**1**
   SeeAlso:[Std Draufsicht](Std_ViewTop/de.md), [Std Ansicht von rechts](Std_ViewRight/de.md)
---

## Beschreibung

Der Befehl **Std Vorderansicht** wendet die Kamerasicht der aktiven [3D-Ansicht](3D_view/de.md) in die Richtung der positiven Y-Achse.

![](images/FreeCAD_views_front.svg ) *Der Peil 1 zeigt in Richtung der Vorderansicht*

## Anwendung

1.  Es gibt verschiedene Wegen, den Befehl umzusetzen:
    -   Die **<img src="images/Std_ViewFront.svg" width=16px> [Std Vorderansicht](Std_ViewFront/de.md)**-Schaltfläche betätigen.
    -   Den Menüpunkt **Ansicht → Standardansichten → <img src="images/Std_ViewFront.svg" width=16px> Vorderansicht** aus dem Menü wählen.
    -   Den Menüpunkt **Standardansichten → <img src="images/Std_ViewFront.svg" width=16px> Vorderansicht** aus dem [3D-Ansicht](3D_view/de.md)-Kontextmenü wählen.
    -   Mit dem Tastenkürzel: **1**.

## Skripten


**Siehe also:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Mit der `viewFront`-Methode des Objektes der aktiven Ansicht wechselt man in die Vorderansicht


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewFront()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}  

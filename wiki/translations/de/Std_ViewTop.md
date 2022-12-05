---
- GuiCommand:/de
   Name:Std ViewTop
   Name/de:Std Draufsicht
   MenuLocation:Ansicht → Standardansichten → Draufsicht
   Workbenches:Alle
   Shortcut:**2**
   SeeAlso:[Std Vorderansicht](Std_ViewFront/de.md), [Std Ansicht von rechts](Std_ViewRight.md)
---

# Std ViewTop/de

## Beschreibung

Der Befehl **Std Draufsicht** wendet die Kamerasicht der aktiven [3D-Ansicht](3D_view/de.md) in die Richtung der negativen Z-Achse.

![](images/FreeCAD_views_front.svg ) 
*der Pfeil 2 zeigt in Richtung der Draufsicht*

## Anwendung

1.  Es gibt verschiedene Wegen, den Befehl umzusetzen:
    -   Die **<img src="images/Std_ViewTop.svg" width=16px> [Std Draufsicht](Std_ViewTop/de.md)**-Schaltfläche betätigen.
    -   Den Menüpunkt **Ansicht → Standardansichten → <img src="images/Std_ViewTop.svg" width=16px> Draufsicht** aus dem Menü wählen.
    -   Den Menüpunkt **Standardansichten → <img src="images/Std_ViewTop.svg" width=16px> Draufsicht** aus dem [3D-Ansicht](3D_view/de.md)-Kontextmenü wählen.
    -   Mit dem Tastenkürzel: **2**.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Mit der `viewTop`-Methode des Objektes der aktiven Ansicht wechselt man in die Draufsicht. Diese Methode gibt es im FreeCAD-Konsolenmodus nicht.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewTop()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewTop/de

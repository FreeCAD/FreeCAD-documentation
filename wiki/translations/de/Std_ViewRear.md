---
- GuiCommand   */de
   Name   *Std ViewRear
   Name/de   *Std Rückansicht
   MenuLocation   *Ansicht → Standardansichten → Hinten
   Workbenches   *Alle
   Shortcut   ***4**
   SeeAlso   *[Std Bodenansicht](Std_ViewBottom/de.md), [Std Ansicht von links](Std_ViewLeft.md)
---

# Std ViewRear/de

## Beschreibung

Der Befehl **Std Rückansicht** wendet die Kamerasicht der aktiven [3D-Ansicht](3D_view/de.md) in die Richtung der negativen Y-Achse.

![](images/FreeCAD_views_rear.svg ) 
*Der Peil 4 zeigt in Richtung der Rückansicht*

## Anwendung

1.  Es gibt verschiedene Wegen, den Befehl umzusetzen   *
    -   Die **<img src="images/Std_ViewRear.svg" width=16px> [Std Rückansicht](Std_ViewRear/de.md)**-Schaltfläche betätigen.
    -   Den Menüpunkt **Ansicht → Standardansichten → <img src="images/Std_ViewRear.svg" width=16px> Rückansicht** aus dem Menü wählen.
    -   Den Menüpunkt **Standardansichten → <img src="images/Std_ViewRear.svg" width=16px> Rückansicht** aus dem [3D-Ansicht](3D_view/de.md)-Kontextmenü wählen.
    -   Mit dem Tastenkürzel   * **4**.

## Skripten


**Siehe auch   ***

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Mit der `viewRear`-Methode des Objektes der aktiven Ansicht wechselt man in die Rückansicht. Diese Methode gibt es im FreeCAD-Konsolenmodus nicht.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRear()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewRear/de

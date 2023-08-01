---
- GuiCommand:
   Name:Std ViewBottom
   Name/de:Std Bodenansicht
   MenuLocation:{{StdMenu|[Ansichtsmenü](Std_View_Menu/de.md)}} - Standardansichten - Bodenansicht
   Workbenches:Alle
   Shortcut:5
   SeeAlso:[Rückansicht](Std_ViewRear/de.md), [Ansicht von links](Std_ViewLeft/de.md)
---

# Std ViewBottom/de

## Beschreibung

Der Befehl **Std Bodenansicht** wendet die Kamerasicht der aktiven [3D Ansicht](3D_view/de.md) in die Richtung der positiven Z Achse.

![](images/FreeCAD_views_rear.svg ) 
*Pfeil 5 zeigt in Richtung der Bodenansicht*

## Anwendung

1.  Es gibt verschiedene Wege, den Befehl umzusetzen:
    -   Die **<img src="images/Std_ViewBottom.svg" width=16px> [Std Bodenansicht](Std_ViewFront/de.md)**-Schaltfläche betätigen.
    -   Den Menüpunkt **Ansicht → Standardansichten → <img src="images/Std_ViewBottom.svg" width=16px> Bodenansicht** aus dem Menü wählen.
    -   Den Menüpunkt **Standardansichten → <img src="images/Std_ViewBottom.svg" width=16px> Bodenansicht** aus dem [3D-Ansicht](3D_view/de.md)-Kontextmenü wählen.
    -   Mit dem Tastenkürzel: **5**.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Mit der `viewBottom`-Methode des Objektes der aktiven Ansicht wechselt man in die Bodenansicht. Diese Methode gibt es im FreeCAD-Konsolenmodus nicht.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewBottom()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewBottom/de

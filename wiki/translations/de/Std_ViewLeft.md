---
- GuiCommand:
   Name:Std ViewLeft
   Name/de:Std Ansicht von links
   MenuLocation:{{StdMenu|[Ansichtsmenü](Std_View_Menu/de.md)}} - Standardansichten - Links
   Workbenches:Alle
   Shortcut:**6**
   SeeAlso:[Rückansicht](Std_ViewRear/de.md), [Bodenansicht](Std_ViewBottom/de.md)
---

# Std ViewLeft/de

## Beschreibung

Der Befehl **Std Ansicht von links** wendet die Kamerasicht der aktiven [3D Ansicht](3D_view/de.md) in die Richtung der positiven X-Achse.

![](images/FreeCAD_views_rear.svg ) 
*Pfeil 6 zeigt in Richtung der Ansicht von links*

## Anwendung

1.  Es gibt verschiedene Wege, den Befehl umzusetzen:
    -   Die **<img src="images/Std_ViewLeft.svg" width=16px> [Std Ansicht von links](Std_ViewLeft/de.md)** Schaltfläche betätigen.
    -   Den Menüpunkt **Ansicht → Standardansichten → <img src="images/Std_ViewLeft.svg" width=16px> Ansicht von links** aus dem Menü wählen.
    -   Den Menüpunkt **Standardansichten → <img src="images/Std_ViewLeft.svg" width=16px> Ansicht von links** aus dem [3D-Ansicht](3D_view/de.md) Kontextmenü wählen.
    -   Mit dem Tastenkürzel: **6**.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Mit der `viewLeft` Methode des Objektes der aktiven Ansicht wechselt man in die Ansicht von links. Diese Methode gibt es im FreeCAD Konsolenmodus nicht.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewLeft()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewLeft/de

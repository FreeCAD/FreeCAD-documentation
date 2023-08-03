---
 GuiCommand:
   Name: Std ViewRight
   Name/de: Std Ansicht von rechts
   MenuLocation: Ansicht , Standardansichten , Rechts
   Workbenches: Alle
   Shortcut: **3**
   SeeAlso: Std_ViewFront/de, Std_ViewTop/de
---

# Std ViewRight/de

## Beschreibung

Der Befehl **Std Ansicht von rechts** wendet die Kamerasicht der aktiven [3D-Ansicht](3D_view/de.md) in die Richtung der negativen X-Achse.

![](images/FreeCAD_views_front.svg ) 
*Der Peil 3 zeigt in Richtung der Ansicht von rechts*

## Anwendung

1.  Es gibt verschiedene Wegen, den Befehl umzusetzen:
    -   Die **<img src="images/Std_ViewRight.svg" width=16px> [Std Ansicht von rechts](Std_ViewRight/de.md)**-Schaltfläche betätigen.
    -   Den Menüpunkt **Ansicht → Standardansichten → <img src="images/Std_ViewRight.svg" width=16px> Ansicht von rechts** aus dem Menü wählen.
    -   Den Menüpunkt **Standardansichten → <img src="images/Std_ViewRight.svg" width=16px> Ansicht von rechts** aus dem [3D-Ansicht](3D_view/de.md)-Kontextmenü wählen.
    -   Mit dem Tastenkürzel: **3**.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Mit der `viewRight`-Methode des Objektes der aktiven Ansicht wechselt man in die Ansicht von rechts. Diese Methode gibt es im FreeCAD-Konsolenmodus nicht.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRight()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewRight/de

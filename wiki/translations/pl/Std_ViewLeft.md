---
- GuiCommand:
   Name: Std ViewLeft
   Name/pl: Std: Widok od lewej
   MenuLocation: Widok -> Widoki standardowe -> Od lewej
   Workbenches: wszystkie
   Shortcut: **6**
   SeeAlso: Std_ViewRear/pl, Std_ViewBottom/pl
---

# Std ViewLeft/pl

## Opis

Polecenie **Widok od lewej** ustawia ujęcie widoku w aktywnym oknie [widoku 3D](3D_view/pl.md) w kierunku dodatnim osi X.

![](images/FreeCAD_views_rear.svg ) 
*Strzałka 6 wskazuje kierunek widoku z lewej.*

## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Std_ViewLeft.svg" width=16px> [Od lewej](Std_ViewLeft/pl.md)**.
    -   Wybierz z menu opcję **Widok → Widoki standardowe → <img src="images/Std_ViewLeft.svg" width=16px> Od lewej**.
    -   Z menu podręcznego okna [widoku 3D](3D_view/pl.md) wybierz opcję **Widoki standardowe → <img src="images/Std_ViewLeft.svg" width=16px> Od lewej**.
    -   Użyj skrótu klawiaturowego: **6**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok *Od lewej*, należy użyć metody `viewLeft` obiektu *ActiveView*. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewLeft()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewLeft/pl

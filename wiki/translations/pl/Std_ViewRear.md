---
- GuiCommand:/pl
   Name:Std ViewRear
   Name/pl:Std: Widok od tyłu
   MenuLocation:Widok → Widoki standardowe → Od tyłu
   Workbenches:wszystkie
   Shortcut:**4**
   SeeAlso:[Widok od dołu](Std_ViewBottom/pl.md), [Widok od lewej](Std_ViewLeft/pl.md)
---

# Std ViewRear/pl

## Opis

Polecenie **Widok od tyłu** ustawia ujęcie widoku w aktywnym oknie [widoku 3D](3D_view/pl.md) w kierunku ujemnym osi Y.

![](images/FreeCAD_views_rear.svg ) 
*Strzałka 4 wskazuje kierunek widoku z tyłu.*

## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Std_ViewRear.svg" width=16px> [Od tyłu](Std_ViewRear/pl.md)**.
    -   Wybierz z menu opcję **Widok → Widoki standardowe → <img src="images/Std_ViewRear.svg" width=16px> Od tyłu**.
    -   Z menu podręcznego okna [widoku 3D](3D_view/pl.md) wybierz opcję **Widoki standardowe → <img src="images/Std_ViewRear.svg" width=16px> Od tyłu**.
    -   Użyj skrótu klawiaturowego: **4**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok *Od tyłu*, należy użyć metody `viewRear` obiektu *ActiveView*. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRear()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewRear/pl

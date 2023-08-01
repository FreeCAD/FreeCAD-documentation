---
- GuiCommand:
   Name:Std ViewRight
   Name/pl:Std: Widok od prawej
   MenuLocation:Widok → Widoki standardowe → Od prawej
   Workbenches:wszystkie
   Shortcut:**3**
   SeeAlso:[Widok od przodu](Std_ViewFront/pl.md), [Widok od góry](Std_ViewTop/pl.md)
---

# Std ViewRight/pl

## Opis

Polecenie **Widok od prawej** ustawia ujęcie widoku w aktywnym oknie [widoku 3D](3D_view/pl.md) w kierunku ujemnym osi X.

![](images/FreeCAD_views_front.svg ) 
*Strzałka 3 wskazuje kierunek widoku z prawej.*

## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Std_ViewRight.svg" width=16px> [Od prawej](Std_ViewRight/pl.md)**.
    -   Wybierz z menu opcję **Widok → Widoki standardowe → <img src="images/Std_ViewRight.svg" width=16px> Od prawej**.
    -   Z menu podręcznego okna [widoku 3D](3D_view/pl.md) wybierz opcję **Widoki standardowe → <img src="images/Std_ViewRight.svg" width=16px> Od prawej**.
    -   Użyj skrótu klawiaturowego: **3**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok *Od prawej*, należy użyć metody `viewRight` obiektu *ActiveView*. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRight()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewRight/pl

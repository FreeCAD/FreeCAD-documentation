---
- GuiCommand:
   Name:Std ViewFront
   Name/pl:Std: Widok od przodu
   MenuLocation:Widok → Widoki standardowe → Od przodu
   Workbenches:wszystkie
   Shortcut:**1**
   SeeAlso:[Widok od góry](Std_ViewTop/pl.md), [Widok od prawej](Std_ViewRight/pl.md)
---

# Std ViewFront/pl

## Opis

Polecenie **Widok od przodu** ustawia ujęcie widoku w aktywnym oknie [widoku 3D](3D_view/pl.md) w kierunku dodatnim osi Y.

![](images/FreeCAD_views_front.svg ) 
*Strzałka 1 wskazuje kierunek widoku z przodu.*

## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Std_ViewFront.svg" width=16px> [Od przodu](Std_ViewFront/pl.md)**.
    -   Wybierz z menu opcję **Widok → Widoki standardowe → <img src="images/Std_ViewFront.svg" width=16px> Od przodu**.
    -   Z menu podręcznego okna [widoku 3D](3D_view/pl.md) wybierz opcję **Widoki standardowe → <img src="images/Std_ViewFront.svg" width=16px> Od przodu**.
    -   Użyj skrótu klawiaturowego: **1**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok *Od przodu*, należy użyć metody `viewFront` obiektu ActiveView. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewFront()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewFront/pl

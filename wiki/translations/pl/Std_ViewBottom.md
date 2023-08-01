---
- GuiCommand:/pl
   Name:Std ViewBottom
   Name/pl:Std: Widok od dołu
   MenuLocation:Widok → Widoki standardowe → Od dołu
   Workbenches:wszystkie
   Shortcut:**5**
   SeeAlso:[Widok od tyłu](Std_ViewRear/pl.md), [Widok od lewej](Std_ViewLeft/pl.md)
---

# Std ViewBottom/pl

## Opis

Polecenie **Widok od dołu** ustawia ujęcie widoku w aktywnym oknie [widoku 3D](3D_view/pl.md) w kierunku dodatnim osi Z.

![](images/FreeCAD_views_rear.svg ) 
*Strzałka 5 wskazuje kierunek widoku z dołu.*

## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Std_ViewBottom.svg" width=16px> [Od dołu](Std_ViewBottom/pl.md)**.
    -   Wybierz z menu opcję **Widok → Widoki standardowe → <img src="images/Std_ViewBottom.svg" width=16px> Od dołu**.
    -   Z menu podręcznego okna [widoku 3D](3D_view/pl.md) wybierz opcję **Widoki standardowe → <img src="images/Std_ViewBottom.svg" width=16px> Od dołu**.
    -   Użyj skrótu klawiaturowego: **5**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok *Od dołu*, należy użyć metody `viewBottom` obiektu *ActiveView*. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewBottom()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewBottom/pl

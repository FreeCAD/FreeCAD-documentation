---
- GuiCommand   */pl
   Name   *Std ViewTop
   Name/pl   *Std   * Widok od góry
   MenuLocation   *Widok → Widoki standardowe → Od góry
   Workbenches   *wszystkie
   Shortcut   ***2**
   SeeAlso   *[Widok od przodu](Std_ViewFront/pl.md), [Widok od prawej](Std_ViewRight/pl.md)
---

# Std ViewTop/pl

## Opis

Polecenie **Widok od góry** ustawia ujęcie widoku w aktywnym oknie [widoku 3D](3D_view/pl.md) w kierunku ujemnym osi Z.

![](images/FreeCAD_views_front.svg ) 
*Strzałka 2 wskazuje kierunek widoku z góry.*

## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia   *
    -   Naciśnij przycisk **<img src="images/Std_ViewTop.svg" width=16px> [Od góry](Std_ViewTop/pl.md)**.
    -   Wybierz z menu opcję **Widok → Widoki standardowe → <img src="images/Std_ViewTop.svg" width=16px> Od góry**.
    -   Z menu podręcznego okna [widoku 3D](3D_view/pl.md) wybierz opcję **Widoki standardowe → <img src="images/Std_ViewTop.svg" width=16px> Od góry**.
    -   Użyj skrótu klawiaturowego   * **2**.

## Tworzenie skryptów 


**Zobacz również   ***

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok *Od góry*, należy użyć metody `viewTop` obiektu *ActiveView*. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewTop()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewTop/pl

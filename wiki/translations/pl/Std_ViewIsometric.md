---
 GuiCommand:
   Name: Std ViewIsometric
   Name/pl: Std: Widok izometryczny
   MenuLocation: Widok , Widoki standardowe , Aksonometryczny , Izometryczny
   Workbenches: wszystkie
   Shortcut: **0**
   SeeAlso: Std_ViewDimetric/pl, Std_ViewTrimetric/pl
---

# Std ViewIsometric/pl



## Opis

Polecenie **Widok izometryczny** zmienia ustawienie ujęcia widoku w aktywnym oknie [widoku 3D](3D_view/pl.md), aby uzyskać widok [izometryczny](https://en.wikipedia.org/wiki/Isometric_projection). Aby uzyskać realnie izometryczny widok, okno widoku 3D powinno być w trybie [ortogonalnym](Std_OrthographicCamera/pl.md), ale polecenie działa również, jeśli widok jest ustawiony w trybie [perspektywy](Std_PerspectiveCamera/pl.md).

![](images/Std_ViewIsometric_example.svg ) 
*[Symbol osi](Std_AxisCross/pl.md) i sześcian w rzucie izometrycznym*



## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Std_ViewIsometric.svg" width=16px> [Izometryczny](Std_ViewIsometric/pl.md)**.
    -   Wybierz z menu opcję **Widok → Widoki standardowe → Aksonometria → <img src="images/Std_ViewIsometric.svg" width=16px> Izometryczny**.
    -   Wybierz opcję z menu podręcznego **Widoki standardowe → <img src="images/Std_ViewIsometric.svg" width=16px> Izometryczny** w oknie [widoku 3D](3D_view/pl.md).
    -   Wybierz opcję **<img src="images/Std_ViewIsometric.svg" width=16px> Izometryczny** z menu mini kostki [kostki nawigacyjnej](Navigation_Cube/pl.md).
    -   Użyj skrótu klawiaturowego: **0**.



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok *izometryczny*, należy użyć metody `viewIsometric` obiektu ActiveView. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewIsometric()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIsometric/pl

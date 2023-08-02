---
- GuiCommand:
   Name: Std ViewDimetric
   Name/pl: Std: Widok dimetryczny
   MenuLocation: Widok -> Widoki standardowe -> Aksonometryczny -> Dimetryczny
   Workbenches: wszystkie
   SeeAlso: Std_ViewIsometric/pl, Std_ViewTrimetric/pl
---

# Std ViewDimetric/pl

## Opis

Polecenie **Widok dimetryczny** zmienia ustawienie ujęcia widoku w aktywnym oknie [widoku 3D](3D_view/pl.md), aby uzyskać widok [dimetryczny](https://en.wikipedia.org/wiki/Axonometric_projection#Three_types). Aby uzyskać realnie dimetryczny widok, okno widoku 3D powinno być w trybie [ortogonalnym](Std_OrthographicCamera/pl.md), ale polecenie działa również, jeśli widok jest ustawiony w trybie [perspektywy](Std_PerspectiveCamera/pl.md).

![](images/Std_ViewDimetric_example.svg ) 
*[Symbol osi](Std_AxisCross/pl.md) i sześcian w rzucie dimetrycznym*

## Użycie

1.  Wybierz z menu głównego opcję **Widok → Widoki standardowe → Aksonometria → <img src="images/Std_ViewDimetric.svg" width=16px> Dimetryczny**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok *dimetryczny*, należy użyć metody `viewDimetric` obiektu ActiveView. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewDimetric()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewDimetric/pl

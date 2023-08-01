---
- GuiCommand:
   Name:Std ViewTrimetric
   Name/pl:Std: Widok Trimetryczny
   MenuLocation:Widok → Widoki standardowe → Aksonometryczny → Trimetryczny
   Workbenches:wszystkie
   SeeAlso:[Widok izometryczny](Std_ViewIsometric/pl.md), [Widok dimertyczny](Std_ViewDimetric/pl.md)
---

# Std ViewTrimetric/pl

## Opis

Polecenie **Widok trimetryczny** zmienia ustawienie ujęcia widoku w aktywnym oknie [widoku 3D](3D_view/pl.md), aby uzyskać widok [trimetryczny](https://en.wikipedia.org/wiki/Axonometric_projection#Three_types). Aby uzyskać realnie trimetryczny widok, okno widoku 3D powinno być w trybie [ortogonalnym](Std_OrthographicCamera/pl.md), ale polecenie działa również, jeśli widok jest ustawiony w trybie [perspektywy](Std_PerspectiveCamera/pl.md).

![](images/Std_ViewTrimetric_example.svg ) 
*[Symbol osi](Std_AxisCross/pl.md) i sześcian w rzucie trimetrycznym*

## Użycie

1.  Wybierz z menu głównego opcję **Widok → Widoki standardowe → Aksonometria → <img src="images/Std_ViewTrimetric.svg" width=16px> Trimetryczny**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok *trimetryczny*, należy użyć metody `viewTrimetric` obiektu ActiveView. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewTrimetric()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewTrimetric/pl

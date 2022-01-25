---
- GuiCommand:/pl
   Name:Std ViewFitSelection
   Name/pl:Std: Widok dopasowany do wyboru
   MenuLocation:Widok → Widoki standardowe → Dopasuj do wyboru
   Workbenches:wszystkie
   Shortcut:**V** **S**
   SeeAlso:[Dopasuj wszystko](Std_ViewFitAll/pl.md)
---

# Std ViewFitSelection/pl

## Opis

Polecenie **Dopasuj do wyboru** powiększa i przesuwa ujęcie widoku tak, że wszystkie wybrane obiekty mieszczą się w aktywnym oknie [widoku 3D](3D_view/pl.md).

## Użycie

1.  Wybierz jeden lub więcej obiektów.
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Std_ViewFitSelection.svg" width=16px> [Dopasuj do wyboru](Std_ViewFitSelection/pl.md)**.
    -   Wybierz z menu opcję **Widok → Widoki standardowe → <img src="images/Std_ViewFitSelection.svg" width=24px>Dopasuj do wyboru**.
    -   Wybierz z menu opcję **<img src="images/Std_ViewFitSelection.svg" width=24px> Dopasuj do wyboru** z menu kontekstowego w oknie [widoku 3D](3D_view/pl.md).
    -   Użyj skrótu klawiaturowego: **V**, a następnie **S**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics.md).

Aby zmienić widok na *dopasowany do wyboru* można użyć metody `SendMsgToActiveView` obiektu FreeCADGui. Metoda ta nie jest dostępna, jeśli FreeCAD jest w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView('ViewSelection')
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewFitSelection/pl

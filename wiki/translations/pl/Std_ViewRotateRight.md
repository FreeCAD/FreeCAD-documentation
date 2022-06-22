---
- GuiCommand   */pl
   Name   *Std ViewRotateRight
   Name/pl   *Std   * Odwróć widok w prawo
   MenuLocation   *Widok → Widoki standardowe → Odwróć w prawo
   Workbenches   *wszystkie
   Shortcut   ***Shift** + **Prawo**
   SeeAlso   *[Odwróć widok w lewo](Std_ViewRotateLeft/pl.md)
---

# Std ViewRotateRight/pl

## Opis

Polecenie **Odwróć widok w prawo** obraca widok w aktywnym oknie [widoku 3D](3D_view/pl.md) wokół osi normalnej *(prostopadłej do widoku)*, w 90-stopniowych przyrostach w prawo *(zgodnie z ruchem wskazówek zegara)*.

## Użycie

1.  Istnieje kilka sposobów wywołania tego polecenia   *
    -   Wybierz opcję **Widok → Widoki standardowe → <img src="images/Std_ViewRotateRight.svg" width=16px|16px> Odwróć w prawo** z menu.
    -   Wybierz opcję **Widoki standardowe → <img src="images/Std_ViewRotateRight.svg" width=16px> Odwróć w prawo** z menu podręcznego w oknie [widoku 3D](3D_view/pl.md).
    -   Użyj skrótu klawiaturowego   * **Shift** + **Prawo**.

## Tworzenie skryptów 


**Zobacz również   ***

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby obrócić widok w Prawo, użyj metody `viewRotateRigh` obiektu *ActiveView*. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRotateRight()
FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewRotateRight/pl

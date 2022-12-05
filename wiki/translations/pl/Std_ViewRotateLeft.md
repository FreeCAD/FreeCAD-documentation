---
- GuiCommand:/pl
   Name:Std ViewRotateLeft
   Name/pl:Std: Odwróć widok w lewo
   MenuLocation:Widok → Widoki standardowe → Odwróć w lewo
   Workbenches:wszystkie
   Shortcut:**Shift**+**Lewo**
   SeeAlso:[Odwróć widok w prawo](Std_ViewRotateRight/pl.md)
---

# Std ViewRotateLeft/pl

## Opis

Polecenie **Odwróć widok w lewo** obraca widok w aktywnym oknie [widoku 3D](3D_view/pl.md) wokół osi normalnej *(prostopadłej do widoku)*, w 90-stopniowych przyrostach w lewo *(przeciwnie do ruchu wskazówek zegara)*.

## Użycie

1.  Istnieje kilka sposobów wywołania tego polecenia:
    -   Wybierz opcję **Widok → Widoki standardowe → <img src="images/Std_ViewRotateLeft.svg" width=16px> Odwróć w lewo** z menu.
    -   Wybierz opcję **Widoki standardowe → <img src="images/Std_ViewRotateLeft.svg" width=16px> Odwróć w lewo** z menu podręcznego w oknie [widoku 3D](3D_view/pl.md).
    -   Użyj skrótu klawiaturowego: **Shift** + **Lewo**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby obrócić widok w lewo, użyj metody `viewRotateLeft` obiektu *ActiveView*. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRotateLeft()
FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewRotateLeft/pl

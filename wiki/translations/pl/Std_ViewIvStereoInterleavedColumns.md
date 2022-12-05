---
- GuiCommand:/pl
   Name:Std ViewIvStereoInterleavedColumns
   Name/pl:Std: Widok stereo z przeplotem kolumn
   MenuLocation:Widok → Widok trójwymiarowy → Widok z przeplotem kolumn
   Workbenches:wszystkie
   SeeAlso:[Widok stereo czerwony / cyjan](Std_ViewIvStereoRedGreen/pl.md),  [Widok poczwórny bufor stereo](Std_ViewIvStereoQuadBuff/pl.md), [Widok stereo z przeplotem wierszy](Std_ViewIvStereoInterleavedRows/pl.md), [Wyłącz widok trójwymiarowy](Std_ViewIvStereoOff/pl.md)
---

# Std ViewIvStereoInterleavedColumns/pl

## Opis

Polecenie **Widok stereo z przeplotem kolumn** zmienia aktywny [widok 3D](3D_view/pl.md) na tryb widoku stereo z przeplotem wierszy. Do korzystania z tego trybu stereo wymagana jest specjalna karta graficzna, specjalny monitor i [okulary z polaryzacją](https://en.wikipedia.org/wiki/Active_shutter_3D_system).

## Użycie

1.  Wybierz z menu opcję **Widok → Widok trójwymiarowy → <img src="images/Std_ViewIvStereoInterleavedColumns.svg" width=16px> Widok stereo z przeplotem kolumn**.

## Ustawienia

-   Odległość między oczami można zmienić w preferencjach: **Edycja → Preferencje ... → Wyświetlanie → Widok 3D → Odległość między oczami dla trybu stereo**. Zobacz również [Edytor usytawień](Preferences_Editor/pl#Widok_3D.md).

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok stereo z przeplotem kolumn, należy użyć metody `setStereoType` obiektu *ActiveView*. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('InterleavedColumns')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewIvStereoInterleavedColumns/pl

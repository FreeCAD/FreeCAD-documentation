---
- GuiCommand   */pl
   Name   *Std ViewIvStereoQuadBuff
   Name/pl   *Std   * Widok poczwórny bufor stereo
   MenuLocation   *Widok → Widok trójwymiarowy → Poczwórny bufor stereo
   Workbenches   *wszystkie
   SeeAlso   *[Widok stereo czerwony / cyjan](Std_ViewIvStereoRedGreen.md), [Widok stereo z przeplotem wierszy](Std_ViewIvStereoInterleavedRows/pl.md), [Widok stereo z przeplotem kolumn](Std_ViewIvStereoInterleavedColumns/pl.md), [Wyłącz widok trójwymiarowy](Std_ViewIvStereoOff/pl.md)
---

# Std ViewIvStereoQuadBuff/pl

## Opis

Polecenie **Poczwórny bufor stereo** zmienia aktywny [widok 3D](3D_view/pl.md) na tryb widoku stereo z poczwórnym buforem. Do korzystania z tego trybu stereo wymagana jest specjalna karta graficzna, specjalny monitor i [okulary z przysłoną](https   *//en.wikipedia.org/wiki/Active_shutter_3D_system).

## Użycie

1.  Wybierz z menu opcję **Widok → Widok trójwymiarowy → <img src="images/Std_ViewIvStereoQuadBuff.svg" width=16px> Poczwórny bufor stereo**.

## Ustawienia

-   Odległość między oczami można zmienić w preferencjach   * **Edycja → Preferencje ... → Wyświetlanie → Widok 3D → Odległość między oczami dla trybu stereo**. Zobacz również [Edytor usytawień](Preferences_Editor/pl#Widok_3D.md).

## Tworzenie skryptów 


**Zobacz również   ***

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok poczwórny bufor stereo, należy użyć metody `setStereoType` obiektu *ActiveView*. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('QuadBuffer')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewIvStereoQuadBuff/pl

---
 GuiCommand:
   Name: Std ViewIvStereoOff
   Name/pl: Std: Wyłącz widok trójwymiarowy
   MenuLocation: Widok , Widok trójwymiarowy , Widok z przeplotem kolumn
   Workbenches: wszystkie
   SeeAlso: Std_ViewIvStereoRedGreen/pl,  Std_ViewIvStereoQuadBuff/pl, Std_ViewIvStereoInterleavedRows/pl, Std_ViewIvStereoInterleavedColumns/pl
---

# Std ViewIvStereoOff/pl

## Opis

Polecenie **Wyłącz widok trójwymiarowy** wyłącza tryb stereo w aktywnym oknie [widoku 3D](3D_view/pl.md).

## Użycie

1.  Wybierz z menu opcję **Widok → Widok trójwymiarowy → <img src="images/Std_ViewIvStereoOff.svg" width=16px> Wyłącz widok trójwymiarowy**.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok standardowy, należy użyć metody `setStereoType` obiektu *ActiveView*. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('None')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIvStereoOff/pl

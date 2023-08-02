---
- GuiCommand:
   Name: Std ViewIvStereoRedGreen
   Name/pl: Std: Widok stereo czerwony / cyjan
   MenuLocation: Widok -> Widok trójwymiarowy -> Stereo czerwony / cyjan
   Workbenches: wszystkie
   SeeAlso: Std_ViewIvStereoQuadBuff/pl, Std_ViewIvStereoInterleavedRows/pl, Std_ViewIvStereoInterleavedColumns/pl, Std_ViewIvStereoOff/pl
---

# Std ViewIvStereoRedGreen/pl



## Opis

Polecenie **Widok stereo czerwony / cyjan** zmienia aktywny [widok 3D](3D_view/pl.md) na czerwono-cyjanowy, [anaglif](https://en.wikipedia.org/wiki/Anaglyph_3D), tryb widoku stereo. Do korzystania z tego trybu stereo wymagane są okulary z kolorowymi soczewkami.



## Użycie

1.  Wybierz z menu opcję **Widok → Widok trójwymiarowy → <img src="images/Std_ViewIvStereoRedGreen.svg" width=16px> Stereo czerwony / cyjan**.



## Ustawienia

-   Odległość między oczami można zmienić w preferencjach: **Edycja → Preferencje ... → Wyświetlanie → Widok 3D → Odległość między oczami dla trybu stereo**. Zobacz również [Edytor usytawień](Preferences_Editor/pl#Widok_3D.md).



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zmienić widok na widok stereo czerwony / cyjan, należy użyć metody `setStereoType` obiektu *ActiveView*. Metoda ta nie jest dostępna, jeśli FreeCAD działa w trybie konsoli.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('Anaglyph')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIvStereoRedGreen/pl

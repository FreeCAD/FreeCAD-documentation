---
 GuiCommand:
   Name: Arch CutLine
   Name/pl: Architektura: Linia Cięcia
   MenuLocation: Architektura , Linia Cięcia
   Workbenches: Arch_Workbench
   Version: 0.19
   SeeAlso: Arch_CutPlane/pl
---

# Arch CutLine/pl



## Opis

Narzędzie **Linia Cięcia** przecina obiekt architektury, taki jak [ściana](Arch_Wall/pl.md) lub [konstrukcja](Arch_Structure/pl.md), prostą krawędzią. W oparciu o tę krawędź i normalną [Płaszczyzna robocza szkicu](Draft_SelectPlane/pl.md) generowana jest powierzchnia cięcia.

<img alt="" src=images/Arch_CutLine_example_1.png  style="width:" height="300px;"> <img alt="" src=images/Arch_CutLine_example_2.png  style="width:" height="300px;">



*[Sciana](Arch_Wall/pl.md) przecięta linią. Po lewej: pole odejmowania, które pojawia się podczas korzystania z narzędzia. Po prawej: ściana wynikowa po zakończeniu cięcia.*



## Użycie

1.  W razie potrzeby wyrównaj płaszczyznę roboczą:
    -   Wybrana krawędź może nie być równoległa do normalnej płaszczyzny roboczej.
    -   Wygenerowana powierzchnia cięcia będzie prostopadła do płaszczyzny roboczej.
2.  Wybierz obiekt w [widoku drzewa](Tree_view/pl.md) lub [widoku 3D](3D_view/pl.md) do wycięcia.
3.  Wybierz krawędź prostą. Musi być ona wybrana w [widoku 3D](3D_view/pl.md).
4.  Naciśnij przycisk **<img src="images/Arch_CutLine.svg" width=16px> [Cięcie linią](Arch_CutLine/pl.md)**.
5.  Wybierz **Za** lub **Przed**, aby wskazać, po której stronie powierzchni cięcia materiał ma zostać usunięty.
6.  Naciśnij przycisk **OK**.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).



---
⏵ [documentation index](../README.md) > Arch CutLine/pl

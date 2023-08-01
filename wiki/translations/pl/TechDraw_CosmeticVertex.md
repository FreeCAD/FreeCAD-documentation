---
- GuiCommand:
   Name:TechDraw CosmeticVertex
   Name/pl:Rysunek Techniczny: Wstaw wierzchołek kosmetyczny
   MenuLocation:Rysunek Techniczny - Dodaj wierzchołki - Wstaw wierzchołek kosmetyczny
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version:0.19
   SeeAlso:[Dodaj wierzchołek punktu środkowego](TechDraw_Midpoints/pl.md), [Dodaj wierzchołki kwadrantu](TechDraw_Quadrants/pl.md)
---

# TechDraw CosmeticVertex/pl



## Opis

Narzędzie **Wstaw wierzchołek kosmetyczny** dodaje do widoku [wierzchołek](Glossary#V.md), który nie jest częścią geometrii źródłowej. Ten wierzchołek zachowuje się jak każdy inny wierzchołek i może być używany do wymiarowania.

<img alt="" src=images/TechDraw_CosmeticVertex_Sample.png  style="width:300px;"> 
*Wierzchołek kosmetyczny użyty do stworzenia wymiaru, który w innym przypadku byłby niemożliwy do uzyskania.*



## Użycie


<div class="mw-translate-fuzzy">

1.  Wybierz widok na rysunku.
2.  Naciśnij przycisk **<img src="images/TechDraw_CosmeticVertex.svg" width=16px> Wstaw wierzchołek kosmetyczny
**
3.  Otworzy się okno dialogowe zadania. Umożliwia ono ustawienie położenia wierzchołka kosmetycznego poprzez wybranie punktu lub wprowadzenie przesunięcia x,y od środka wybranego widoku.
4.  Aby wybrać pozycję, naciśnij przycisk **Wybór punktów**. Kliknij pozycję w widoku, a następnie naciśnij przycisk **OK**, aby utworzyć punkt. Aby zakończyć wybieranie punktu bez tworzenia wierzchołka kosmetycznego, naciśnij przycisk **Zakończ wskazywanie** w oknie dialogowym.


</div>

## Notes

-   You cannot change the position of an existing cosmetic vertex. At the moment there is no other way than to delete it and create a new one.
-   To delete a cosmetic vertex use <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [TechDraw CosmeticEraser](TechDraw_CosmeticEraser.md).



## Właściwości

Wierzchołki kosmetyczne nie mają własnych właściwości, ponieważ nie są obiektami dokumentu. Współdzielą ustawienia koloru i rozmiaru ze zwykłymi wierzchołkami geometrii.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Funkcja **Wstaw wierzchołek kosmetyczny** jest dostępna dla [makrodefinicji](Macros/pl.md) lub z konsoli [Python](Python/pl.md).


```python
dvp = App.ActiveDocument.View
org = App.Vector(0.0, 0.0, 0.0)
dvp.makeCosmeticVertex(org);

#lines too!
start = FreeCAD.Vector (1.0, 5.0, 0.0)
end = FreeCAD.Vector(1.0, -5.0, 0.0)
style = 2
weight = 0.75
pyGreen = (0.0, 0.0, 1.0, 0.0)
dvp.makeCosmeticLine(start,end,style, weight, pyGreen)
```





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw CosmeticVertex/pl

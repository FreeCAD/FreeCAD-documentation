---
 GuiCommand:
   Name: TechDraw CosmeticVertex
   Name/pl: Rysunek Techniczny: Wstaw wierzchołek kosmetyczny
   MenuLocation: Rysunek Techniczny , Dodaj wierzchołki , Wstaw wierzchołek kosmetyczny
   Workbenches: TechDraw_Workbench/pl
   Version: 0.19
   SeeAlso: TechDraw_Midpoints/pl, TechDraw_Quadrants/pl
---

# TechDraw CosmeticVertex/pl



## Opis

Narzędzie **Wstaw wierzchołek kosmetyczny** dodaje do widoku [wierzchołek](Glossary#V.md), który nie jest częścią geometrii źródłowej. Ten wierzchołek zachowuje się jak każdy inny wierzchołek i może być używany do wymiarowania.

<img alt="" src=images/TechDraw_CosmeticVertex_Sample.png  style="width:300px;"> 
*Wierzchołek kosmetyczny użyty do stworzenia wymiaru, który w innym przypadku byłby niemożliwy do uzyskania.*



## Użycie

1.  Wybierz widok na rysunku.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_CosmeticVertex.svg" width=16px> Wstaw wierzchołek kosmetyczny
**
    -   Wybierz opcję z menu **Rysunek Techniczny → Dodaj wierzchołki → <img src="images/TechDraw_CosmeticVertex.svg" width=16px> Wstaw wierzchołek kosmetyczny**.
3.  Otworzy się panel zadań.
4.  Opcjonalnie naciśnij przycisk **Wybór punktów** i wybierz punkt na stronie. Naciśnij przycisk **Zakończ wskazywanie**, aby anulować tę operację.
5.  Opcjonalnie zmień lub określ współrzędne X i Y punktu. Współrzędne odnoszą się do środka widoku.
6.  Naciśnij przycisk **OK**.



## Uwagi

-   Nie można zmienić położenia istniejącego wierzchołka kosmetycznego. W tej chwili nie ma innego sposobu niż usunięcie go i utworzenie nowego.
-   Aby usunąć wierzchołek kosmetyczny należy użyć narzędzia <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [Usuń geometrie pomocnicze](TechDraw_CosmeticEraser/pl.md).



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
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw CosmeticVertex/pl

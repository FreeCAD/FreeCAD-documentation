---
- GuiCommand:
   Name: TechDraw Midpoints
   Name/pl: Rysunek Techniczny: Dodaj wierzchołek punktu środkowego
   MenuLocation: Rysunek Techniczny - Dodaj wierzchołki - Dodaj wierzchołek punktu środkowego
   Workbenches: [Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version: 0.19
   SeeAlso: [Wstaw wierzchołek kosmetyczny](TechDraw_CosmeticVertex/pl.md), [Dodaj wierzchołki kwadrantu](TechDraw_Quadrants/pl.md)
---

# TechDraw Midpoints/pl


</div>



## Opis

Narzędzie **Dodaj wierzchołek punktu środkowego** dodaje [Wierzchołek pomocniczy](TechDraw_CosmeticVertex/pl.md) w punkcie środkowym jednej lub więcej wybranych krawędzi.

<img alt="" src=images/TechDraw_CosmeticMidpoint_Sample.png  style="width:250px;"> 
*Wierzchołki pomocnicze w punktach środkowych krawędzi.*



## Użycie


<div class="mw-translate-fuzzy">

1.  Wybierz jedną lub więcej krawędzi w widoku.
2.  Naciśnij przycisk **<img src="images/TechDraw_Midpoints.svg" width=16px> Dodaj wierzchołek punktu środkowego
**
3.  Wierzchołki pomocnicze zostaną dodane w punktach środkowych krawędzi.


</div>

## Notes

-   The created cosmetic vertices are not parametrically linked to the selected edges.
-   To delete a cosmetic vertex use <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [TechDraw CosmeticEraser](TechDraw_CosmeticEraser.md).



## Właściwości

Wierzchołki jako geometrie pomocnicze nie mają własnych właściwości, ponieważ nie są obiektami dokumentu. Współdzielą ustawienia koloru i rozmiaru ze zwykłymi wierzchołkami geometrii.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Kosmetyczne wierzchołki nie są obecnie dostępne dla [makrodefinicji](Macros/pl.md) lub z konsoli [Python](Python/pl.md). Poniższy fragment kodu usunie wszystkie wierzchołki kosmetyczne z widoku.


```python
v = App.ActiveDocument.View
v.clearCV()
App.ActiveDocument.recompute()
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Midpoints/pl

---
 GuiCommand:
   Name: TechDraw Quadrants
   Name/pl: Rysunek Techniczny: Dodaj wierzchołki kwadrantu
   MenuLocation: Rysunek Techniczny , Dodaj wierzchołki , Dodaj wierzchołki kwadrantu
   Workbenches: TechDraw_Workbench/pl
   Version: 0.19
   SeeAlso: TechDraw_CosmeticVertex/pl, TechDraw_Midpoints/pl
---

# TechDraw Quadrants/pl


</div>



## Opis


<div class="mw-translate-fuzzy">

Narzędzie **Dodaj wierzchołki kwadrantu** dodaje trzy [wierzchołki kosmetyczne](TechDraw_CosmeticVertex/pl.md) wzdłuż jednej lub więcej wybranych krawędzi. Wierzchołki są umieszczane na 25%, 50% i 75% długości. Dla okrągłej krawędzi daje to kosmetyczne wierzchołki pod kątem 90°, 180° i 270°, oprócz geometrycznego wierzchołka pod kątem 0°.


</div>

<img alt="" src=images/TechDraw_CosmeticQuadrant_Sample.png  style="width:250px;"> 
*Wierzchołki pomocnicze w punktach ćwiartki okręgu.*



## Użycie


<div class="mw-translate-fuzzy">

1.  Wybierz jedną lub więcej krawędzi w widoku. Można wybrać dowolną krawędź, nie tylko okręgi.
2.  Naciśnij przycisk **<img src="images/TechDraw_Quadrants.svg" width=16px> Dodaj wierzchołki kwadrantu**.
3.  Kosmetyczne wierzchołki zostaną dodane w ćwiartkach krawędzi.


</div>

## Notes

-   The created cosmetic vertices are not parametrically linked to the selected edges.
-   To delete a cosmetic vertex use <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:16px;"> [TechDraw CosmeticEraser](TechDraw_CosmeticEraser.md).



## Właściwości

Wierzchołki jako geometrie pomocnicze nie mają własnych właściwości, ponieważ nie są obiektami dokumentu. Współdzielą ustawienia koloru i rozmiaru ze zwykłymi wierzchołkami geometrii.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Funkcja **Kosmetyczne wierzchołki kwadrantu** nie są obecnie dostępne dla [makrodefinicji](Macros/pl.md) lub z konsoli [Python](Python/pl.md). Poniższy fragment kodu usunie wszystkie wierzchołki kosmetyczne z widoku.


```python
v = App.ActiveDocument.View
v.clearCV()
App.ActiveDocument.recompute()
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Quadrants/pl

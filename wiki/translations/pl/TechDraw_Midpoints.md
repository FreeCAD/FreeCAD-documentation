---
 GuiCommand:
   Name: TechDraw Midpoints
   Name/pl: Rysunek Techniczny: Dodaj wierzchołek punktu środkowego
   MenuLocation: Rysunek Techniczny , Dodaj wierzchołki , Dodaj wierzchołek punktu środkowego
   Workbenches: TechDraw_Workbench/pl
   Version: 0.19
   SeeAlso: TechDraw_CosmeticVertex/pl, TechDraw_Quadrants/pl
---

# TechDraw Midpoints/pl



## Opis

Narzędzie **Dodaj wierzchołek punktu środkowego** dodaje [Wierzchołek pomocniczy](TechDraw_CosmeticVertex/pl.md) w punkcie środkowym jednej lub więcej wybranych krawędzi.

<img alt="" src=images/TechDraw_CosmeticMidpoint_Sample.png  style="width:250px;"> 
*Wierzchołki pomocnicze w punktach środkowych krawędzi.*



## Użycie

1.  Wybierz jedną lub więcej krawędzi w widoku.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_Midpoints.svg" width=16px> '''Dodaj wierzchołek punktu środkowego'''
**
    -   Wybierz opcję z menu **Rysunek Techniczny → Dodaj wierzchołki → <img src="images/TechDraw_Midpoints.svg" width=16px> Dodaj wierzchołek punktu środkowego**.



## Uwagi

-   Utworzone wierzchołki kosmetyczne nie są parametrycznie powiązane z wybranymi krawędziami.
-   Aby usunąć wierzchołek kosmetyczny należy zaznaczyć ją i nacisnąć **Delete**. {{Version/pl|1.0}}



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

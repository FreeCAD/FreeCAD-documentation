---
- GuiCommand:
   Name:TechDraw HorizontalExtentDimension
   Name/pl:Rysunek Techniczny: Wstaw wymiar rozpiętości poziomej
   MenuLocation:Rysunek Techniczny → Wymiary → Wstaw wymiar rozpiętości poziomej
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version:0.19
   SeeAlso:[Wstaw wymiar długości](TechDraw_LengthDimension/pl.md), [Wstaw wymiar rozpiętości pionowej](TechDraw_VerticalExtentDimension/pl.md)
---

# TechDraw HorizontalExtentDimension/pl



## Opis

Narzędzie **Wstaw wymiar rozpiętości poziomej** dodaje wymiar liniowy do widoku. Wymiar rozciąga się od najbardziej wysuniętego na lewo punktu na wybranych obiektach do najbardziej wysuniętego na prawo punktu. W każdym punkcie zostanie umieszczony wierzchołek pomocniczy.

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;"> 
*Poziomy wymiar rozpiętości krzywej złożonej*



## Użycie

1.  Wybierz widok lub zbiór krawędzi w widoku.
2.  Naciśnij przycisk **<img src="images/TechDraw_HorizontalExtentDimension.svg" width=16px> '''Wstaw wymiar rozpiętości poziomej'''**.
3.  Do widoku zostanie dodany wymiar. Można go przeciągnąć do żądanej pozycji.



## Ograniczenia

Obiekty wymiarowe są podatne na \"[problem nazewnictwa topologicznego](Topological_naming_problem/pl.md)\". Zobacz stronę [Wstaw wymiar długości](TechDraw_LengthDimension/pl.md), aby uzyskać więcej informacji.



## Właściwości

Zapoznaj się z informacjami na stronie [Wstaw wymiar długości](TechDraw_LengthDimension/pl#Właściwości.md). Wyjątki opisano poniżej.



### Dane

-    **TypPomiaru**: wartością domyślną jest {{TRUE/pl}} - na podstawie geometrii 3D lub \"Rzutowanie\" - na podstawie rysunku. Zwykle nie jest manipulowany bezpośrednio przez użytkownika końcowego. Nie zaimplementowano jeszcze dla narzędzia Wstaw wymiar rozpiętości poziomej.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wstaw wymiar rozpiętości poziomej** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
selection = ['Edge1', 'Edge2']                      # or [] for all

TechDraw.makeExtentDim(view1, selection, 0)         # view1 is a DrawViewPart; 0 for horizontal
App.ActiveDocument.DimExtent.Y = -60                # offset dimension line from dimensioned edges in Y direction
App.ActiveDocument.DimExtent.X = 10                 # offset dimension text along dimension line in X direction
App.ActiveDocument.DimExtent.FormatSpec = '%.0f'    # Dimension format

TechDraw.makeExtentDim(view1, selection, 1)         # view1 is a DrawViewPart; 1 for vertical
App.ActiveDocument.DimExtent001.X = -130            # offset dimension line from dimensioned edges in X direction
App.ActiveDocument.DimExtent001.Y = 10              # offset dimension text along dimension line in Y direction
App.ActiveDocument.DimExtent001.FormatSpec = '%.0f'

# Note the dimension names are 'DimExtent', 'DimExtent001' etc in the order created.
```





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw HorizontalExtentDimension/pl

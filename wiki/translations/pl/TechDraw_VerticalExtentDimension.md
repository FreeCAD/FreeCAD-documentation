---
- GuiCommand:/pl
   Name:TechDraw VerticalExtentDimension
   Name/pl:Rysunek Techniczny: Wstaw wymiar rozpiętości pionowej
   MenuLocation:Rysunek Techniczny → Wymiary → Wstaw wymiar rozpiętości pionowej
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version:0.19
   SeeAlso:[Wstaw wymiar długości](TechDraw_LengthDimension/pl.md),  [Wstaw wymiar rozpiętości poziomej](TechDraw_HorizontalExtentDimension/pl.md)
---

# TechDraw VerticalExtentDimension/pl



## Opis

Narzędzie **Wstaw wymiar rozpiętości pionowej** dodaje wymiar liniowy do widoku. Wymiar rozciąga się od najbardziej wysuniętego na lewo punktu na wybranych obiektach do najbardziej wysuniętego na prawo punktu. W każdym punkcie zostanie umieszczony wierzchołek pomocniczy.

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;"> 
*Pionowy wymiar rozpiętości krzywej złożonej*



## Użycie

1.  Wybierz widok lub zbiór krawędzi w widoku.
2.  Naciśnij przycisk **<img src="images/TechDraw_VerticalExtentDimension.svg" width=16px> '''Wstaw wymiar rozpiętości pionowej'''**.
3.  Do widoku zostanie dodany wymiar. Można go przeciągnąć do żądanej pozycji.



## Ograniczenia

Obiekty wymiarowe są podatne na \"[problem nazewnictwa topologicznego](Topological_naming_problem/pl.md)\". Zobacz stronę [Wstaw wymiar długości](TechDraw_LengthDimension/pl.md), aby uzyskać więcej informacji.



## Właściwości

Zapoznaj się z informacjami na stronie [Wstaw wymiar długości](TechDraw_LengthDimension/pl#Właściwości.md). Wyjątki opisano poniżej.



### Dane

-    **TypPomiaru**: wartością domyślną jest {{TRUE/pl}} - na podstawie geometrii 3D lub \"Rzutowanie\" - na podstawie rysunku. Zwykle nie jest manipulowany bezpośrednio przez użytkownika końcowego. Nie zaimplementowano jeszcze dla narzędzia Wstaw wymiar rozpiętości pionowej.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wstaw wymiar rozpiętości pionowej** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
selection = [(view1, 'Edge1'), (view1, 'Edge2')]  #or [] for all
hExtentDim = TechDraw.Dimension.makeExtentDim(selection, VERTICAL)
rc = page.addView(hExtentDim)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw VerticalExtentDimension/pl

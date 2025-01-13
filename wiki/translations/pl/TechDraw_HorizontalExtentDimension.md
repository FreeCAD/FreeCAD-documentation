---
 GuiCommand:
   Name: TechDraw HorizontalExtentDimension
   Name/pl: Rysunek Techniczny: Wstaw wymiar rozpiętości poziomej
   MenuLocation: Rysunek Techniczny , Wymiary , Wstaw wymiar rozpiętości poziomej
   Workbenches: TechDraw_Workbench/pl
   Version: 0.19
   SeeAlso: TechDraw_LengthDimension/pl, TechDraw_VerticalExtentDimension/pl
---

# TechDraw HorizontalExtentDimension/pl



## Opis

Narzędzie **Wstaw wymiar rozpiętości poziomej** dodaje wymiar liniowy do widoku. Wymiar rozciąga się od najbardziej wysuniętego na lewo punktu na wybranych obiektach do najbardziej wysuniętego na prawo punktu.

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;"> 
*Poziome i pionowe wymiary rozpiętości krzywej złożonej*



## Użycie

1.  Wybierz widok lub zestaw krawędzi w widoku.
2.  Narzędzie można wywołać na kilka sposobów:
    -   
        {{Version/pl|1.0}}
        
        : Jeśli [preferencja](TechDraw_Preferences/pl#Wymiary.md) **Narzędzie wymiarowania** jest ustawiona na {{Value|Narzędzie pojedyncze}} (domyślnie): kliknij na strzałce skierowanej w dół po prawej stronie od przycisku **<img src="images/TechDraw_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** i wybierz opcję **<img src="images/TechDraw_HorizontalExtentDimension.svg" width=16px> Wstaw wymiar rozpiętości poziomej** z listy rozwijanej.

    -   Jeśli ta preferencja ma inną wartość (i {{VersionMinus/pl|0.21}}): wciśnij przycisk **<img src="images/TechDraw_HorizontalExtentDimension.svg" width=16px> [Wstaw wymiar rozpiętości poziomej](TechDraw_HorizontalExtentDimension/pl.md)**.

    -   Wybierz opcję z menu **Rysunek Techniczny → Wymiary → <img src="images/TechDraw_HorizontalExtentDimension.svg" width=16px> Wstaw wymiar rozpiętości poziomej**.
3.  Wymiar zostanie dodany do widoku.
4.  Wymiar można przeciągnąć do żądanej pozycji.
5.  W razie potrzeby dodaj tolerancje zgodnie z opisem na stronie [Wymiarowanie i tolerancja](TechDraw_Geometric_dimensioning_and_tolerancing#Tolerancja.md).



### Zmiana właściwości 

Aby zmienić właściwości obiektu wymiaru, kliknij dwukrotnie na niego w rysunku lub w [widoku drzewa](Tree_view/pl.md). Spowoduje to otwarcie okna [dialogowego wymiaru](TechDraw_LengthDimension/pl#Okno_dialogowe.md).



## Ograniczenia

Obiekty wymiarowe są podatne na \"[problem nazewnictwa topologicznego](Topological_naming_problem/pl.md)\". Zobacz stronę [Wstaw wymiar długości](TechDraw_LengthDimension/pl.md), aby uzyskać więcej informacji.



## Uwagi

Zapoznaj się również informacjami na stroni e[Wymiar długości](TechDraw_LengthDimension/pl#Uwagi.md).



## Właściwości

Zapoznaj się z informacjami na stronie [Wstaw wymiar długości](TechDraw_LengthDimension/pl#Właściwości.md). Wyjątki opisano poniżej.



### Dane


{{Properties_Title|Podstawowe}}

-    **TypPomiaru**: Nie wdrożono jeszcze dla wymiarów rozpiętości.



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
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw HorizontalExtentDimension/pl

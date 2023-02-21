---
- GuiCommand:/pl
   Name:TechDraw ProjectShape
   Name/pl:Rysunek Techniczny: Rzutowanie kształtów
   MenuLocation:Rysunek Techniczny → Rzutowanie kształtów ...
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Shortcut:
   Version:0.20
   SeeAlso:[Widok 2D kształtu](Draft_Shape2DView/pl.md)
---

# TechDraw ProjectShape/pl



## Opis

Narzędzie <img alt="" src=images/TechDraw_ProjectShape.svg  style="width:24px;"> **Rzut kształtu** tworzy rzuty kształtów. Rzuty tworzone są w oknie [widoku 3D](3D_view/pl.md), a nie na [stronie rysunku technicznego](TechDraw_PageDefault/pl.md).

![](images/ProjectShape1_it.png )



## Użycie

1.  Wybierz jeden lub więcej obiektów. Dla każdego obiektu zostanie utworzona osobny rzut.
2.  Istnieje kilka sposobów na wywołanie narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_ProjectShape.svg" width=16px> '''Rzutowanie kształtów ...'''**.
    -   Wybierz z menu opcję **Rysunek Techniczny → <img src="images/TechDraw_ProjectShape.svg" width=16px> Rzutowanie kształtów ...**.
3.  Otwiera się panel zadań **Rzutowanie kształtów**. Zobacz też sekcję [właściwości](#Właściwości.md).
4.  Ustawić żądane opcje.
5.  Wybrane opcje nie powinny skutkować pustym rzutem, ponieważ spowodują błąd. Na przykład dla obiektu posiadającego tylko ostre krawędzie, takiego jak [prostopadłościan](Part_Box/pl.md), należy zaznaczyć opcję **Widoczne ostre krawędzie** i/lub **Ukryte ostre krawędzie**.
6.  Naciśnij przycisk **OK**.



## Właściwości

Obiekt Rzutu wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Rzutowanie}}

-    **Źródło|Link**: Kształt, który ma być rzutowany.

-    **Kierunek|Vector**: Kierunek rzutowania. Jest to wektor normalny płaszczyzny projekcji.

-    **VCompound|Bool**: Jeśli opcja ma wartość {{TRUE/pl}}, to widoczne ostre krawędzie są pokazywane. Przykład: wszystkie krawędzie [prostopadłościanu](Part_Box/pl.md).

-    **Rg1 Line VCompound|Bool**: Jeśli opcja ma wartość {{TRUE/pl}}, widoczne gładkie krawędzie są pokazywane. Przykład: krawędzie między zaokrągleniem a sąsiednimi ścianami.

-    **Rg NLine VCompound|Bool**: Jeśli opcja ma wartość {{TRUE/pl}}, pokazane są widoczne krawędzie szyte. Przykład: szew ściany cylindrycznej 360°.

-    **Out Line VCompound|Bool**: Jeśli opcja ma wartość {{TRUE/pl}}, pokazywane są widoczne krawędzie konturowe *(które nie są ostre)*. Przykład: widok boczny [walca](Part_Cylinder.md) ma dwie takie krawędzie.

-    **Iso Line VCompound|Bool**: Jeśli opcja ma wartość {{TRUE/pl}}, widoczne izoparametry są wyświetlane. Obecnie nie działa.

-    **HCompound|Bool**: Jeśli opcja ma wartość {{TRUE/pl}}, pokazywane są ukryte ostre krawędzie.

-    **Rg1 Line HCompound|Bool**: Jeśli opcja ma wartość {{TRUE/pl}}, pokazane są ukryte gładkie krawędzie.

-    **Rg NLine HCompound|Bool**: Jeśli opcja ma wartość {{TRUE/pl}}, pokazane są ukryte krawędzie szyte.

-    **Out Line HCompound|Bool**: Jeśli opcja ma wartość {{TRUE/pl}}, pokazywane są ukryte krawędzie konturowe.

-    **Iso Line HCompound|Bool**: Jeśli opcja ma wartość {{TRUE/pl}}, pokazywane są ukryte izoparametry. Obecnie nie działa.



## Uwagi

Narzędzie to było wcześniej dostępne w środowisku pracy Kreślenie.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ProjectShape/pl

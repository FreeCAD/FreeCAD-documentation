---
 GuiCommand:
   Name: Points Convert
   Name/pl: Punkty: Konwertuj na punkty
   MenuLocation: Punkty , Konwertuj na punkty ...
   Workbenches: Points_Workbench/pl
---

# Points Convert/pl



## Opis

Polecenie **Konwertuj na punkty** tworzy chmury punktów z obiektów kształtu lub obiektów siatki.

Obiekt typu kształt oznacza tutaj dowolny obiekt z właściwością **Kształt**. Obiekty utworzone za pomocą środowisk pracy [Część](Part_Workbench/pl.md) i [Projekt Części](PartDesign_Workbench/pl.md) są obiektami kształtu. Ale podobnie jest z obiektami utworzonymi za pomocą środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md) i [Rysunek Roboczy](Draft_Workbench/pl.md).



## Użycie

1.  Wybierz jeden lub więcej obiektów.
2.  Istnieje kilka sposobów wywołania polecenia:
    -   Naciśnij przycisk **<img src="images/Points_Convert.svg" width=16px> '''Konwertuj na punkty'''**.
3.  Wybierz z menu opcję **Punkty → Konwertuj na punkty ...**.
4.  Otworzy się okno dialogowe **Odległość**.
5.  Wprowadź wartość **Największa odległość**. Wartość musi mieścić się w przedziale {{Value|0,05}} - {{Value|10.0}}.
6.  Naciśnij przycisk **OK**, aby zamknąć okno dialogowe i zakończyć polecenie.



## Właściwości

Obiekty chmury punktów są obiektami typu [Cecha geometrii](App_GeoFeature/pl.md) z następującymi dodatkowymi właściwościami. Wybierz opcję **Wyświetl wszystko** z menu kontekstowego [Edytora właściwości](Property_editor/pl.md), aby wyświetlić ukryte właściwości.



### Dane


{{TitleProperty|Podstawa}}

-    **Punkty|PointsKernel|Ukryte**: jądro związane z tym obiektem.

-    **Normalne|NormalList|Ukryte**: lista normalnych. Ta właściwość jest dostępna tylko dla chmur punktów utworzonych za pomocą polecenia [Konwertuj na punkty](Points_Convert/pl.md) z obiektów siatkowych lub obiektów kształtowych ze ścianami.


{{TitleProperty|Punkty strukturalne.}}

-    **Wysokość|Integer**: oznacza unikalną liczbę współrzędnej Y w chmurze punktów. Ta właściwość jest dostępna tylko dla chmur punktów utworzonych za pomocą polecenia [Uporządkowana chmura punktów](Points_Structure/pl.md).

-    **Szerokość|Integer**: oznacza unikalną liczbę współrzędnej X w chmurze punktów. Ta właściwość jest dostępna tylko dla chmur punktów utworzonych za pomocą polecenia [Uporządkowana chmura punktów](Points_Structure/pl.md).



### Widok


{{TitleProperty|Podstawa}}

-    **Rozmiar punktu|FloatConstraint**: rozmiar punktów w pikselach w oknie [widoku 3D](3D_view/pl.md).





{{Points Tools navi

}}



---
⏵ [documentation index](../README.md) > [Points](Points_Workbench.md) > Points Convert/pl

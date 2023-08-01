---
- GuiCommand:
   Name:Rysunek Roboczy: Widok 2D kształtu
   MenuLocation:Modyfikacja - Widok 2D kształtu
   Workbenches:[Rysunek Roboczy](Draft_Workbench/pl.md), [Architektura](Arch_Workbench/pl.md)
   SeeAlso:[Rysunek Techniczny: Rzut kształtu](TechDraw_ProjectShape/pl.md)
---

# Draft Shape2DView/pl



## Opis

Polecenie <img alt="" src=images/Draft_Shape2DView.svg  style="width:24px;"> **Widok 2D kształtu** tworzy rzuty 2D z wybranych obiektów, zwykle brył przestrzennych lub [Płaszczyzny przekroju](Arch_SectionPlane/pl.md) środowiska Architektura. Rzuty są umieszczane w oknie [widoku 3D](3D_view/pl.md).

Rzuty **Widok 2D kształtu** mogą być wyświetlane w środowisku [Rysunek Techniczny](TechDraw_Workbench/pl.md) używając polecenia [Wstaw widok rysunku](TechDraw_DraftView/pl.md). Alternatywnie środowisko [Rysunek Techniczny](TechDraw_Workbench/pl.md) oferuje swoje własne narzędzia do rzutowania. Tworzą one jednak rzuty, które są wyświetlane tylko na stronie rysunku a nie w oknie [widoku 3D](3D_view/pl.md).

![](images/Draft_Shape2DView_example.jpg ) 
*Rzutowanie brył na płaszczyznę XY*



## Użycie

1.  Opcjonalnie obróć [widok 3D](3D_view/pl.md). Kierunek ujęcia widoku w oknie [widoku 3D](3D_view/pl.md) określa wektor projekcji. Na przykład, [widok od góry](Std_ViewTop/pl.md) będzie rzutować na płaszczyznę XY. Wektor projekcji jest ignorowany dla rzutów utworzonych przez funkcję [Płaszczyzna przekroju](Arch_SectionPlane/pl.md) środowiska Architektura.
2.  Opcjonalnie wybierz jeden lub więcej obiektów.
3.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Draft_Shape2DView.svg" width=24px> [Widok 2D kształtu](Draft_Shape2DView/pl.md)**.
    -   Wybierz opcję z menu **Modyfikacja → <img src="images/Draft_Shape2DView.svg" width=24px> Widok 2D kształtu**.
4.  Jeśli nie wybrałeś jeszcze żadnego obiektu: wybierz obiekt w oknie [widoku 3D](3D_view/pl.md).
5.  Rzutowane obiekty są tworzone na płaszczyźnie XY.



## Jak tworzyć plany i przekroje o różnych szerokościach linii 

<img alt="" src=images/Draft_shape2dview_example_plan.png  style="width:700px;">

Rysunki z różnymi szerokościami linii dla linii widocznych i linii cięcia mogą być łatwo utworzone przez użycie dwóch obiektów *Widok 2D kształtu* z tego samego [Płaszczyzna przekroju](Arch_SectionPlane/pl.md). Jeden z obiektów *Widok 2D kształtu* ma ustawiony tryb rzutowania na **Bryła**, który renderuje linie widoczne, a drugi ustawiony na **Linia cięcia** lub **Powierzchnia cięcia**, który renderuje linie cięcia. Oba obiekty *Widok 2D kształtu* są następnie umieszczone w tym samym miejscu, jeden na drugim.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt *Widok 2D kształtu* wywodzi się z obiektu [Część: Part2DObject](Part_Part2DObject/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Rysunek Roboczy}}

-    **Aktualizacja automatyczna|Bool**: określa, czy rzut powinien być automatycznie obliczany ponownie, jeśli obiekt **Podstawa** ulegnie zmianie. Wybór wartości {{False/pl}} może być użyteczny, jeśli w dokumencie jest wiele obiektów *Widok 2D kształtu* lub jeśli są one złożone. Jeśli wybrano wartość {{False/pl}}, do aktualizacji rzutów należy użyć polecenia [Std: Odśwież](Std_Refresh/pl.md). {{Version/pl|0.20}}

-    **Podstawa|Link**: określa obiekt, który ma być wyświetlany.

-    **Numer ściany|IntegerList**: określa indeksy ścian, które mają być rzutowane. Działa tylko jeśli **Tryb rzutowania** ma wartość {{Value|Poszczególne ściany}}.

-    **Fuse Arch|Bool**: określa czy [obiekty Architektoniczne](Arch_Workbench/pl.md) tego samego typu i z tego samego materiału są łączone czy nie.

-    **Ukryte linie|Bool**: określa, czy ukryte linie są wyświetlane, czy nie.

-    **W miejscu|Bool**: działa tylko jeśli wybrany obiekt jest [płaszczyzną przekroju](Arch_SectionPlane/pl.md) środowiska Architektura, a **Tryb rzutowania** to {{Value|Cutlines}} lub {{Value|Cutfaces}}, określa czy rzut będzie współplanarny z płaszczyzną przekroju.

-    **Rzut|Vector**: określa kierunek rzutowania. Ignorowane, jeśli **Podstawa** jest [płaszczyzna przekroju](Arch_SectionPlane/pl.md) Architektura.

-    **Tryb projekcji|Enumeration**: określa tryb projekcji. Dostępne są następujące tryby:

    -   
        {{Value|Bryła}}
        
        : rzutuje cały wybrany obiekt.

    -   
        {{Value|Poszczególne ściany}}
        
        : wyświetla tylko ściany z listy **Numer ściany**.

    -   
        {{Value|Cutlines}}
        
        : działa tylko wtedy, gdy wybranym obiektem jest [płaszczyzna przekroju](Arch_SectionPlane/pl.md) środowiska Architektura, rzutuje tylko krawędzie przecięte przez płaszczyznę przekroju.

    -   
        {{Value|Cutfaces}}
        
        : działa tylko wtedy, gdy wybranym obiektem jest [płaszczyzna przekroju](Arch_SectionPlane/pl.md) środowiska Architektura, rzutuje powierzchnie przecięte płaszczyzną przekroju przez bryłę jako powierzchnie czołowe.

    -   
        {{Value|Ściany bryły}}
        
        : rzutuje cały wybrany obiekt poprzez cięcie powierzchni jedna po drugiej. Może być użyty, jeśli tryb {{Value|Bryła}} daje złe wyniki. {{Version/pl|0.20}}

-    **Długość segmentu|Float**: określa rozmiar w milimetrach odcinków liniowych, jeżeli parametr **Tesselacja** ma wartość {{TRUE/pl}}.

-    **Tesselacja|Bool**: określa czy teselacja powinna zostać wykonana. Teselacja oznacza, że krzywe są zastępowane przez sekwencje segmentów liniowych. Może to być pracochłonne obliczeniowo, jeśli wartość **Długość segmentu** jest zbyt krótka.

-    **Wyłącznie widoczne|Bool**: określa, czy rzut powinien być obliczany ponownie tylko wtedy, gdy jest widoczny.

-    **Punkty wykluczenia|Vector list**: Lista punktów wykluczenia. Krawędź przechodząca przez którykolwiek z tych punktów nie zostanie narysowana. {{Version/pl|0.20}}

-    **Nazwy wykluczeń|String list**: Lista nazw obiektów. Każdy oglądany lub wycinany obiekt podrzędny o nazwie zawartej w tej liście nie będzie rysowany. {{Version/pl|0.21}}



### Widok


{{TitleProperty|Rysunek Roboczy}}

-    **Wzór|Enumeration**: niewykorzystane.

-    **Rozmiar wzoru|Float**: niewykorzystane.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby utworzyć rzut 2D użyj metody `make_shape2dview` modułu Rysunek Roboczy ({{Version/pl|0.19}}). Ta metoda zastępuje przestarzałą metodę `makeShape2DView`.


```python
shape2dview = make_shape2dview(baseobj, projectionVector=None, facenumbers=[])
```

-    `baseobj`to obiekt, który ma być rzutowany.

-    `projectionVector`jest wektorem projekcji. Jeżeli nie jest podany, używana jest oś Z.

-    `facenumbers`jest listą numerów ścian (0 - bazowy). Jeśli podano, tylko te ściany są brane pod uwagę.

-    `shape2dview`jest zwracana wraz z utworzonym rzutem 2D.

W razie potrzeby zmień właściwość `Tryb projekcji` tworzonego obiektu. Może to być: `"Bryła"`, `"Poszczególne ściany"`, `"Cutlines"`, `"Cutfaces"` lub `"Ściany bryły"`.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

box = doc.addObject("Part::Box", "Box")
box.Length = 2300
box.Width = 500
box.Height = 1000

shape1 = Draft.make_shape2dview(box)

shape2 = Draft.make_shape2dview(box, App.Vector(1, -1, 1))

shape3 = Draft.make_shape2dview(box, App.Vector(-1, 1, 1), [0, 5])
shape3.ProjectionMode = "Individual Faces"

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Shape2DView/pl

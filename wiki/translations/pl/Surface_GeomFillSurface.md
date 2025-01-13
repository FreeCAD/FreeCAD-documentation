---
 GuiCommand:
   Name: Surface GeomFillSurface
   Name/pl: Powierzchnia 3D: Wypełnianie krzywych granicznych
   MenuLocation: Surface , Fill boundary curves
   Workbenches: Surface_Workbench/pl
   Version: 0.17
---

# Surface GeomFillSurface/pl



## Opis

Polecenie **[<img src=images/Surface_GeomFillSurface.svg style="width:16px"> '''Wypełnianie krzywych granicznych'''** tworzy parametryczną powierzchnię z dwóch, trzech lub czterech krawędzi granicznych, próbując utworzyć płynne przejście między nimi.

<img alt="" src=images/Surface_GeomFillSurface_4_edges.png  style="width:330px;"> <img alt="" src=images/Surface_GeomFillSurface_4_edges_example.png  style="width:330px;">

<img alt="" src=images/Surface_GeomFillSurface_3_edges.png  style="width:330px;"> <img alt="" src=images/Surface_GeomFillSurface_3_edges_example.png  style="width:330px;">

<img alt="" src=images/Surface_GeomFillSurface_2_edges.png  style="width:330px;"> <img alt="" src=images/Surface_GeomFillSurface_2_edges_example.png  style="width:330px;">



*Po lewej: krawędzie używane do generowania powierzchni za pomocą narzędzia '''Wypełnianie krzywych granicznych''', cztery połączone krawędzie, trzy połączone krawędzie i dwie odłączone krawędzie. Po prawej: powierzchnia wynikowa z użycia odpowiednio czterech, trzech i dwóch krawędzi.*



## Użycie

1.  Naciśnij przycisk **[<img src=images/Surface_GeomFillSurface.svg style="width:16px"> '''Wypełnianie krzywych granicznych'''**.
2.  Wybierz krawędzie w oknie [widoku 3D](3D_view/pl.md). Krawędzie muszą łączyć się ze sobą tak, aby tworzyły profil zamknięty.
3.  Naciśnij **OK**.


**Uwaga:**

Po utworzeniu nie jest możliwe zastosowanie dodatkowych wiązań do utworzonej powierzchni.



## Opcje


**Typ wypełnienia**

: {{RadioButton|TRUE|Rozciągnięcie}}, {{RadioButton|TRUE|Coons}}, lub {{RadioButton|TRUE|Zakrzywienie}}.



## Właściwości

Obiekt **Wypełnianie krzywych granicznych** *(klasa `Surface::GeomFillSurface`)* jest pochodną podstawowej klasy [Część: Cecha](Part_Feature/pl.md) *(klasa `Part::Feature`, wraz z klasą podrzędną `Part::Spline`)*, dlatego też współdzieli wszystkie właściwości tej ostatniej.

Oprócz właściwości opisanych na stronie [Cecha części](Part_Feature/pl.md), obiekt Rozszerz powierzchnię, posiada następujące właściwości w [edytorze właściwości](Property_editor/pl.md).



### Dane


{{TitleProperty|Podstawa}}

-    **Typ wypełnienia|Enumeration**: zastosowany algorytm wypełniania; Rozciągnięcie, styl z najbardziej płaskimi łatami. [{{Value|Coons}}](https://en.wikipedia.org/wiki/Coons_patch), zaokrąglony styl o mniejszej głębokości niż Zakrzywienie. Zakrzywiony, styl z najbardziej zaokrąglonymi łatami.

-    **Lista granic|LinkSubList**: lista krawędzi, które zostaną użyte do zbudowania powierzchni.

-    **Lista odwrócona|BoolList|(ukryte)**:



### Widok


{{TitleProperty|Podstawa}}

-    **Punkty kontrolne|Bool**: wartość domyślna to {{FALSE/pl}}, Jeśli ustawiono {{TRUE/pl}}, wyświetlona zostanie nakładka z punktami kontrolnymi krzywej.



## Skręcenie powierzchni 

Kształt powierzchni zależy od kierunku wybranych krawędzi; jeśli wybrano krawędzie, a wynikiem jest powierzchnia, która \"zakręca\" na siebie, jedna z krawędzi może wymagać listy wierzchołków w odwrotnej kolejności. Powierzchnia, która skręca się sama na sobie, prawdopodobnie będzie miała samoprzecięcia, a zatem będzie nieprawidłowym [kształtem](Part_TopoShape/pl.md). Można to zweryfikować za pomocą narzędzia **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Sprawdź geometrię](Part_CheckGeometry/pl.md)** środowiska pacy Część.

Na przykład, jeśli dwie krzywe mają punkty: 
```python
curve1 = [a, b, c, d]
curve2 = [e, f, g]
``` oraz wynikową powierzchnię po użyciu **[<img src=images/Surface_GeomFillSurface.svg style="width:16px"> [Wypełnianie krzywych granicznych](Surface_GeomFillSurface/pl.md)** lub **[<img src=images/Surface_Sections.svg style="width:16px"> [Przekrój powierzchni](Surface_Sections/pl.md)** jest powierzchnią skręconą, możesz utworzyć trzecią krzywą, która jest równa jednej z dwóch oryginalnych krzywych, ale z odwróconą listą punktów.

Albo 
```python
curve1 = [a, b, c, d]
curve3 = [g, f, e]
```

lub 
```python
curve3 = [d, c, b, a]
curve2 = [e, f, g]
``` powinno działać, aby wygenerować powierzchnię, która się nie skręca.

W praktyce oznacza to, że wszystkie krawędzie używane do generowania powierzchni powinny być tworzone najlepiej w tym samym kierunku zgodnym lub przeciwnym do ruchu wskazówek zegara. Przestrzeganie tej prostej zasady zwykle gwarantuje, że powierzchnia będzie podążać w najbardziej płynnym kierunku i nie będzie się skręcać.

Gdy właściwość **Oświetlenie** powierzchni ma wartość {{Value|Jedna strona}}, powierzchnia zostanie pomalowana na czarno, jeśli jej normalny kierunek wskazuje na [widok 3D](3D_view/pl.md) *(z dala od bieżącej widza)*, wskazując odwróconą powierzchnię w stosunku do innych kolorowych powierzchni.

<img alt="" src=images/Surface_twisting_example_smooth.png  style="width:330px;"> <img alt="" src=images/Surface_twisting_example_twisted.png  style="width:330px;"> 
*Po lewej: krawędzie graniczne są zorientowane w tym samym kierunku, a zatem wygenerowana powierzchnia jest gładka. Po prawej: krawędzie graniczne mają przeciwne kierunki, a zatem wygenerowana powierzchnia skręca się na sobie, powodując samoprzecinanie.*



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Narzędzie Wypełnianie krzywych granicznych powierzchni może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) poprzez dodanie obiektu {{Incode|Surface::GeomFillSurface}}.

-   Krawędzie, które mają być użyte do zdefiniowania powierzchni, muszą być przypisane jako [LinkSubList](FeaturePython_Custom_Properties/pl#App:_PropertyLinkSubList.md) do właściwości `BoundaryList` obiektu.
-   Typ algorytmu musi być przypisany jako ciąg znaków do właściwości `FillType`.
-   Wszystkie obiekty z krawędziami muszą zostać przeliczone, zanim będą mogły zostać użyte jako dane wejściowe dla właściwości obiektu GeomFillSurface.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

a = App.Vector(-140, -100, 0)
b = App.Vector(175, -108, 0)
c = App.Vector(200, 101, 0)
d = App.Vector(-135, 107, 70)

points1 = [a, App.Vector(-55, -91, 65), App.Vector(35, -85, -5), b]
obj1 = Draft.make_bspline(points1)

points2 = [b, App.Vector(217, -45, 55), App.Vector(217, 35, -15), c]
obj2 = Draft.make_bspline(points2)

points3 = [c, App.Vector(33, 121, 55), App.Vector(0, 91, 15), App.Vector(-80, 121, -40), d]
obj3 = Draft.make_bspline(points3)

points4 = [d, App.Vector(-140, 0, 45), a]
obj4 = Draft.make_bspline(points4)
doc.recompute()

surf = doc.addObject("Surface::GeomFillSurface", "Surface")
surf.BoundaryList = [(obj1, "Edge1"),
                     (obj2, "Edge1"),
                     (obj3, "Edge1"),
                     (obj4, "Edge1")]
doc.recompute()
```





{{Surface Tools navi

}}



---
⏵ [documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface GeomFillSurface/pl

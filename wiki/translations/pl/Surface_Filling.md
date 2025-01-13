---
 GuiCommand:
   Name: Surface Filling
   Name/pl: Powierzchnia 3D: Wypełnianie
   MenuLocation: Surface , Filling
   Workbenches: Surface_Workbench/pl
   Version: 0.17
---

# Surface Filling/pl



## Opis

Polecenie **[<img src=images/Surface_Filling.svg style="width:16px"> '''Wypełnianie'''** tworzy powierzchnię z serii połączonych krawędzi granicznych. Krzywizna powierzchni może być dodatkowo kontrolowana przez krawędzie i wierzchołki, które nie są krawędziami granicznymi, oraz powierzchnię podpierającą.

Geometria bazowa może należeć do krzywych utworzonych za pomocą środowiska [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownik](Sketcher_Workbench/pl.md), ale może również należeć do obiektów bryłowych, takich jak te utworzone za pomocą środowiska [Część](Part_Workbench/pl.md) lub [Projekt Części](PartDesign_Workbench/pl.md).

<img alt="" src=images/Surface_Filling_example.png  style="width:600px;"> 
*Dwie wypełnione powierzchnie ograniczone czterema krawędziami znajdującymi się na płaszczyźnie XY. Powierzchnia po prawej stronie jest dodatkowo kontrolowana przez krawędź niebędącą granicą.*



## Użycie

1.  Naciśnij przycisk **[<img src=images/Surface_Filling.svg style="width:16px"> '''Wypełnianie'''**.
2.  Otworzy się panel zadań **Granice**. Zobacz dostępne [Opcje](#Opcje.md).
3.  Wybierz dwie lub więcej krawędzi w oknie [widoku 3D](3D_view/pl.md):
    -   W tym momencie nie ma potrzeby naciskania przycisku **Dodaj krawędź** w sekcji **Granice**.
    -   Krawędzie muszą być wybrane w odpowiedniej kolejności.
    -   Krawędzie muszą być połączone, ale cała granica nie musi być zamknięta.
    -   Kompletna granica nie powinna się przecinać.
    -   W przypadku okrągłej granicy 360° można wybrać dwie półokrągłe krawędzie.
4.  Podgląd ostatecznego kształtu zostanie wyświetlony po wybraniu wystarczającej ilości prawidłowej geometrii.
5.  Opcjonalnie wybierz **Powierzchnia pomocnicza**. Zobacz [Przykład](#Przykład.md).
6.  Opcjonalnie wybierz jedno lub więcej **Wiązania krawędziowe**.
7.  Opcjonalnie wybierz jedno lub więcej **Wiązań wierzchołków**.
8.  Naciśnij przycisk **OK**.



## Opcje

-   W sekcji **Granice** można określić powierzchnię podparcia i krawędzie graniczne:
    -   Naciśnij przycisk **Powierzchnia podparcia** i wybierz ścianę w oknie [widoku 3D](3D_view/pl.md), aby dodać powierzchnię podparcia.
        -   Kliknij ikonę <img alt="" src=images/Edit-cleartext.svg  style="width:16px;">, aby usunąć powierzchnię podparcia.
    -   Naciśnij przycisk **Dodaj krawędź** raz, aby rozpocząć zaznaczanie krawędzi granicznych w oknie [widoku 3D](3D_view/pl.md).
    -   Istnieje kilka sposobów na usunięcie zaznaczenia krawędzi granicznych:
        -   Naciśnij przycisk **Usuń krawędź** raz, aby rozpocząć odznaczanie krawędzi w oknie [widoku 3D](3D_view/pl.md).
        -   Zaznacz krawędź na liście i naciśnij klawisz **Delete**.
        -   Kliknij prawym przyciskiem myszy krawędź na liście i wybierz **Usuń** z menu podręcznego.

-   W sekcji **Wiązania krawędzi** można określić krawędzie niebędące krawędziami granicznymi:
    -   Opcje wyboru są podobne do tych dla krawędzi granicznych.

-   W sekcji **Wiązania wierzchołków** można określić wierzchołki nie będące wierzchołkami granicznymi:
    -   Opcje wyboru są podobne do tych dla wierzchołków granicznych.

-   Naciśnij przycisk **Esc** lub przycisk **Anuluj** aby przerwać wykonywanie polecenia.



## Przykład

Polecenie **Powierzchnia podparcia** działa jako dodatkowe ograniczenie dla powierzchni. Poniższy prosty przykład pozwoli zrozumieć, jak to działa:

1.  W środowisku pracy <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Część](Part_Workbench/pl.md) utwórz <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> [walec](Part_Cylinder/pl.md) i ustaw jego **kąt** na {{Value|180°}}.
2.  Przełącz się ponownie na środowisko pracy <img alt="" src=images/Workbench_Surface.svg  style="width:16px;"> [Powierzchnia 3D](Surface_Workbench/pl.md) i naciśnij przycisk **[<img src=images/Surface_Filling.svg style="width:16px"> [Wypełnienie](Surface_Filling/pl.md)**.
3.  Wybierz dwie półokrągłe krawędzie i dwie proste krawędzie, które je łączą.
4.  Wynik jest zgodny z czterema krawędziami granicznymi, ale wewnętrzny kształt jest zupełnie inny od powierzchni cylindrycznej.
5.  Edytuj obiekt Powierzchnia i dla **Powierzchnia podparcia** wybierz powierzchnię cylindryczną.
6.  Zmodyfikowany kształt znacznie lepiej pasuje do powierzchni walcowej.



## Właściwości

Obiekt **Wypełnienie** *(klasa `Surface::Filling`)* jest pochodną podstawowej klasy [Część: Cecha](Part_Feature/pl.md) *(klasa `Part::Feature`, poprzez klasę podrzędną `Part::Spline`)*, dlatego też dzieli z nią wszystkie jej właściwości.

Oprócz właściwości opisanych na stronie [Cecha części](Part_Feature/pl.md), obiekt Rozszerz powierzchnię, posiada następujące właściwości w [edytorze właściwości](Property_editor/pl.md).



### Dane


{{TitleProperty|Wypełnienie}}

-    **Boundary Edges|LinkSubList**: Krawędzie graniczne, C0 jest wymagane dla krawędzi bez odpowiadającej im powierzchni.

-    **Boundary Faces|StringList**:

-    **Boundary Order|IntegerList**: Kolejność ograniczeń na powierzchniach granicznych; {{Value|0}}, {{Value|1}} i {{Value|2}} są możliwe.

-    **Unbound Edges|LinkSubList**: Nieograniczone krawędzie wiązania, C0 jest wymagane dla krawędzi bez odpowiedniej ściany.

-    **Unbound Faces|StringList**:

-    **Unbound Order|IntegerList**: Kolejność ograniczeń na niezwiązanych powierzchniach; {{Value|0}}, {{Value|1}} i {{Value|2}} są możliwe.

-    **Free Faces|LinkSubList**: Wolne ograniczenie na powierzchni.

-    **Free Order|IntegerList**: Kolejność wiązań na wolnych powierzchniach.

-    **Points|LinkSubList**: Punkty wiązania na powierzchni.

-    **Initial Face|LinkSub**: początkowa powierzchnia do użycia.

-    **Degree|Integer**: Stopień początkowy, domyślnie {{Value|3}}.

-    **Points On Curve|Integer**: Liczba punktów na krawędzi dla wiązania.

-    **Iterations|Integer**: Liczba iteracji, domyślnie {{Value|2}}.

-    **Anisotropy|Bool**: Wartość domyślna to {{FALSE/pl}}.

-    **Tolerance2d|Float**: Tolerancja 2D, domyślnie {{Value|0.0}}.

-    **Tolerance3d|Float**: Tolerancja 3D, domyślnie {{Value|0.0}}.

-    **Tol Angular|Float**: Tolerancja G1, domyślnie {{Value|0.01}}.

-    **Tol Curvature|Float**: Tolerancja G2, domyślnie {{Value|0.10}}.

-    **Maximum Degree|Integer**: Maksymalny stopień krzywej, wartością domyślną jest {{Value|8}}.

-    **Maximum Segments|Integer**: Maksymalna liczba segmentów, domyślnie {{Value|9}}.



### Widok


{{TitleProperty|Podstawa}}

-    **Punkty kontrolne|Bool**: wartość domyślna to {{FALSE/pl}}, Jeśli ustawiono {{TRUE/pl}}, wyświetlona zostanie nakładka z punktami kontrolnymi krzywej.



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wypełnienie** powierzchni może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) poprzez dodanie obiektu {{Incode|Surface::Filling}}.

-   Krawędzie, które mają być użyte do zdefiniowania powierzchni, muszą być przypisane jako [LinkSubList](FeaturePython_Custom_Properties/pl#App:_PropertyLinkSubList.md) do właściwości `BoundaryEdges` obiektu.
-   Pomocnicze krawędzie i wierzchołki muszą być przypisane jako [LinkSubLists](FeaturePython_Custom_Properties/pl#App:_PropertyLinkSubList.md) do właściwości `UnboundEdges` i `Points` obiektu.
-   Wszystkie obiekty z krawędziami muszą zostać obliczone, zanim będą mogły zostać użyte jako dane wejściowe dla właściwości obiektu Filling.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

a = App.Vector(-20, -20, 0)
b = App.Vector(-18, 25, 0)
c = App.Vector(60, 26, 0)
d = App.Vector(33, -20, 0)

points1 = [a, App.Vector(-20, -8, 0), App.Vector(-17, 7, 0), b]
obj1 = Draft.make_bspline(points1)

points2 = [b, App.Vector(0, 25, 0), c]
obj2 = Draft.make_bspline(points2)

points3 = [c, App.Vector(37, 4, 0), d]
obj3 = Draft.make_bspline(points3)

points4 = [d, App.Vector(-2, -18, 0), a]
obj4 = Draft.make_bspline(points4)
doc.recompute()

surf = doc.addObject("Surface::Filling", "Surface")
surf.BoundaryEdges = [(obj1, "Edge1"),
                      (obj2, "Edge1"),
                      (obj3, "Edge1"),
                      (obj4, "Edge1")]
doc.recompute()

# 
points_spl = [App.Vector(-10, 0, 2),
              App.Vector(4, 0, 7),
              App.Vector(18, 0, -5),
              App.Vector(25, 0, 0),
              App.Vector(30, 0, 0)]
aux_edge = Draft.make_bspline(points_spl)
doc.recompute()

surf.UnboundEdges = [(aux_edge, "Edge1")]
doc.recompute()

# 
aux_v1 = Draft.make_line(App.Vector(-13, -12, 5),
                         App.Vector(-13, -12, -5))
aux_v2 = Draft.make_line(App.Vector(-3, 18, 5),
                         App.Vector(-3, 18, -5))
doc.recompute()

surf.Points = [(aux_v1, "Vertex2"),
               (aux_v2, "Vertex1")]
doc.recompute()
```





{{Surface Tools navi

}}



---
⏵ [documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface Filling/pl

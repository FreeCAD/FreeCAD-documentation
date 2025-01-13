---
 GuiCommand:
   Name: Surface Sections
   Name/pl: Powierzchnia 3D: Przekrój powierzchni
   MenuLocation: Surface , Sections
   Workbenches: Surface_Workbench/pl
   Version: 0.19
---

# Surface Sections/pl



## Opis

Polecenie **[<img src=images/Surface_Sections.svg style="width:16px"> '''Przekrój powierzchni'''** służy do tworzenia powierzchni z krawędzi, które reprezentują poprzeczne przekroje powierzchni.

<img alt="" src=images/Surface_Sections_edges_example.png  style="width:" height="250px;"> <img alt="" src=images/Surface_Sections_example.png  style="width:" height="250px;">



*Po lewej: krawędzie kontrolne ''(przekroje poprzeczne)''. Po prawej: powierzchnia utworzona z tych krawędzi.*



## Użycie

1.  Upewnij się, że masz co najmniej dwie krawędzie lub krzywe w przestrzeni. Na przykład można je utworzyć za pomocą narzędzi środowiska pracy <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md) lub <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Szkicownik](Sketcher_Workbench/pl.md).
2.  Naciśnij przycisk **[<img src=images/Surface_Sections.svg style="width:16px"> '''Przekrój powierzchni'''**.
3.  Naciśnij **Dodaj krawędź**.
4.  Użyj kursora, aby wybrać żądane krawędzie w oknie [widoku 3D](3D_view/pl.md); podgląd ostatecznego kształtu zostanie wyświetlony po wybraniu dwóch prawidłowych krawędzi.
5.  Naciśnij **OK**, aby zakończyć operację.



## Opcje

-    **Dodaj krawędź**: naciśnij raz, aby rozpocząć wybieranie krawędzi w oknie [widoku 3D](3D_view/pl.md). Pojedyncze linie, takie jak **[<img src=images/Draft_BSpline.svg style="width:16px"> [Rysunek Roboczy: Krzywa złożona](Draft_BSpline/pl.md)** i **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [Szkicownik: Krzywa złożona](Sketcher_CreateBSpline/pl.md)**, a także dowolne krawędzie z obiektów bryłowych, jak te z **[<img src=images/PartDesign_Body.svg style="width:16px"> [Zawartości](PartDesign_Body/pl.md)** środowiska Projekt Części i **[<img src=images/Part_Primitives.svg style="width:16px"> [geometrie pierwotne](Part_Primitives/pl.md)** środowiska Część.

-    **Usuń krawędź**: naciśnij raz, aby rozpocząć wybieranie krawędzi w oknie [Widok 3D](3D_view/pl.md); muszą to być krawędzie, które zostały wcześniej wybrane za pomocą **Dodaj krawędź**.

-    **Prawy przycisk myszy**: otwórz menu podręczne i wybierz **Usuń** lub naciśnij **Del** na klawiaturze, aby usunąć aktualnie wybraną krawędź z listy.

-    **Przeciągnij**: przeciągnięcie aktualnie zaznaczonego elementu na liście w celu zmiany kolejności, w jakiej będzie on przetwarzany; lista jest przetwarzana od góry do dołu.

-   Naciśnij **Anuluj** lub **Esc**, aby przerwać bieżącą operację.



## Właściwości

Obiekt **Przekrój powierzchni** *(klasa `Surface::Sections`)* jest pochodną podstawowej klasy [Część: Cecha](Part_Feature/pl.md) *(klasa `Part::Feature`, poprzez klasę podrzędną `Part::Spline`)*, dlatego też dzieli z nią wszystkie jej właściwości.

Oprócz właściwości opisanych na stronie [Cecha części](Part_Feature/pl.md), obiekt Przekrój powierzchni, posiada następujące właściwości w [edytorze właściwości](Property_editor/pl.md).



### Dane


{{TitleProperty|Przekroje}}

-    **NSections|LinkSubList**: lista krawędzi, które zostaną użyte do zbudowania powierzchni.



### Widok


{{TitleProperty|Podstawa}}

-    **Punkty kontrolne|Bool**: wartość domyślna to {{FALSE/pl}}, Jeśli ustawiono {{TRUE/pl}}, wyświetlona zostanie nakładka z punktami kontrolnymi krzywej.



## Skręcenie powierzchni 

Kształt powierzchni zależy od kierunku wybranych krawędzi. Jeśli krawędzie zostaną wybrane, a wynikiem będzie powierzchnia, która \"zakręca\" na siebie, jedna z krawędzi może wymagać listy wierzchołków w odwrotnej kolejności. Zobacz informacje na stronie **[<img src=images/Surface_GeomFillSurface.svg style="width:16px"> [Wypełnianie krzywych granicznych](Surface_GeomFillSurface/pl#Skręcenie_powierzchni.md)** w celu uzyskania pełniejszego wyjaśnienia.

<img alt="" src=images/Surface_twisting_example_smooth.png  style="width:330px;"> <img alt="" src=images/Surface_twisting_example_twisted.png  style="width:330px;">



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Narzędzie Przekrój powierzchni może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) poprzez dodanie obiektu `Surface::Sections`.

-   Krawędzie, które mają być użyte do zdefiniowania krzywej, muszą być przypisane jako [Struktura danych LinkSub](FeaturePython_Custom_Properties/pl#App:_PropertyLinkSub.md) do właściwości `NSections` obiektu.
-   Wszystkie obiekty z krawędziami muszą zostać obliczone, zanim będą mogły zostać użyte jako dane wejściowe dla właściwości obiektu Sections.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

pl1 = App.Placement()
obj1 = Draft.make_circle(50, placement=pl1, face=False, startangle=0, endangle=180)

pl2 = App.Placement(App.Vector(0, 0, 25), App.Rotation())
obj2 = Draft.make_circle(30, placement=pl2, face=False, startangle=0, endangle=180)

points3 = [App.Vector(18, -10, 50),
           App.Vector(12, 10, 50),
           App.Vector(-12, 10, 50),
           App.Vector(-18, -10, 50)]
obj3 = Draft.make_bspline(points3)

points4 = [App.Vector(15, -20, 100),
           App.Vector(0, 6, 100),
           App.Vector(-15, -20, 100)]
obj4 = Draft.make_bspline(points4)
doc.recompute()

surf = doc.addObject("Surface::Sections", "Surface")
surf.NSections = [(obj1, "Edge1"),
                  (obj2, "Edge1"),
                  (obj3, "Edge1"),
                  (obj4, "Edge1")]
doc.recompute()
```





{{Surface Tools navi

}}



---
⏵ [documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface Sections/pl

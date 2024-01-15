---
 GuiCommand:
   Name: Surface BlendCurve
   Name/pl: Powierzchnia 3D: Krzywa łącząca
   MenuLocation: Powierzchnia , Krzywa łącząca
   Workbenches: Surface_Workbench/pl
   Version: 0.21
---

# Surface BlendCurve/pl



## Opis

Narzędzie **Krzywa łącząca** tworzy krzywą Bezier\'a między dwiema krawędziami, z zachowaniem pożądanej ciągłości.

Geometria bazowa może należeć do krzywych utworzonych za pomocą środowiska [Rysunek Roboczy](Draft_Workbench/pl.md) lub [Szkicownik](Sketcher_Workbench/pl.md), ale może również należeć do obiektów bryłowych, takich jak te utworzone za pomocą środowiska [Część](Part_Workbench/pl.md).

<img alt="" src=images/Surface_BlendCurve_G3_example.png  style="width:400px;"> <img alt="" src=images/Surface_BlendCurve_Comb.png  style="width:400px;"> 
*Krzywa łączenia powierzchni łącząca dwie krawędzie z ciągłością G3. Pomarańczowy wielokąt reprezentuje punkty kontrolne. Grzebień krzywizny (z zewnętrznego środowiska pracy [Krzywe](Curves_Workbench/pl.md)) jest gładki w punktach styku.*



## Użycie

1.  Wybierz dwie krawędzie w oknie [widoku 3D](3D_view/pl.md).
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Surface_BlendCurve.svg" width=16px> '''Krzywa łącząca'''**.
    -   Wybierz z menu opcję **Surface → <img src="images/Surface_BlendCurve.svg" width=16px> Krzywa łącząca**.
3.  Dostosuj kształt krzywej we właściwościach obiektu **Dane**.



## Właściwości

Krzywa łącząca jest pochodną podstawowej klasy [Część: Cecha](Part_Feature/pl.md) *(`Part::Feature`, poprzez klasę podrzędną `Part::Spline`)*, dlatego też dzieli z nią wszystkie jej właściwości.

Oprócz właściwości opisanych na stronie [Część: Cecha](Part_Feature/pl.md), krzywa mieszania powierzchni ma następujące właściwości w [edytorze właściwości](Property_editor/pl.md).



### Dane


{{TitleProperty|Krzywa łącząca}}

-    **Start Edge|LinkSub**: Pierwsza krawędź wejściowa.

-    **Start Continuity|Integer**: Geometryczna wartość ciągłości

-    **Start Parameter|Float**: Znormalizowany parametr wzdłuż krawędzi; od {{Value|0.0}} (początek krawędzi) do {{Value|1.0}} *(koniec krawędzi)*.

-    **Start Size|Float**: Rozmiar stycznej.

-    **End Edge|LinkSub**: Druga krawędź wejściowa.

-    **End Continuity|Integer**: Geometryczna wartość ciągłości

-    **End Parameter|Float**: Znormalizowany parametr wzdłuż krawędzi; od {{Value|0.0}} (początek krawędzi) do {{Value|1.0}} \'\'\'\'(koniec krawędzi).

-    **End Size|Float**: Rozmiar stycznej.



### Widok


{{TitleProperty|Baza}}

-    **Control Points|Bool**: wartość domyślna to {{FALSE/pl}}, Jeśli ustawiono {{TRUE/pl}}, wyświetlona zostanie nakładka z punktami kontrolnymi krzywej.



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Narzędzie Blend Curve może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) poprzez dodanie obiektu `Surface::FeatureBlendCurve`.

-   Krawędzie, które mają być użyte do zdefiniowania krzywej, muszą być przypisane jako [Struktura danych LinkSub](LinkSub/pl.md) do właściwości `StartEdge` i `EndEdge` obiektu.
-   Wszystkie obiekty z krawędziami muszą zostać obliczone, zanim będą mogły zostać użyte jako dane wejściowe dla właściwości obiektu Blend Curve.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

points1 = [App.Vector(-20, -20, 0), App.Vector(-20, -8, 0), App.Vector(-17, 7, 0), App.Vector(-18, 25, 0)]
obj1 = Draft.make_bspline(points1)

points2 = [App.Vector(60, 26, 0), App.Vector(37, 4, 0), App.Vector(33, -20, 0)]
obj2 = Draft.make_bspline(points2)

doc.recompute()

bcurve = doc.addObject("Surface::FeatureBlendCurve","BlendCurve")
bcurve.StartEdge = (obj1, 'Edge1')
bcurve.EndEdge = (obj2, 'Edge1')
bcurve.EndParameter = 1.00
bcurve.StartSize = -5.00
bcurve.EndSize = -5.00

doc.recompute()
```





{{Surface Tools navi

}}



---
⏵ [documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface BlendCurve/pl

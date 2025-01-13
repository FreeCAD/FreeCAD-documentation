---
 GuiCommand:
   Name: Draft Draft2Sketch
   Name/pl: Rysunek Roboczy: Rysunek roboczy do szkicu
   MenuLocation: Modyfikacja , Rysunek roboczy do szkicu
   Workbenches: Draft_Workbench/pl, BIM_Workbench/pl
---

# Draft Draft2Sketch/pl



## Opis

Narzędzie <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:24px;"> **Rysunek roboczy do szkicu** konwertuje obiekty środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md) na obiekty środowiska [Szkicownik](Sketcher_NewSketch/pl.md) i odwrotnie.

![](images/Draft_Draft2Sketch_example.png ) 
*Konwertowanie obiektów środowiska Rysunek Roboczy na szkice Szkicownika.*



## Użycie

1.  Opcjonalnie wybierz jeden lub więcej obiektów Rysunku Roboczego lub [szkic](Sketcher_NewSketch/pl.md) środowiska Szkicownik.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_Draft2Sketch.svg" width=16px> '''Rysunek roboczy do szkicu'''**.
    -   [Środowisko pracy Rysunek Roboczy](Draft_Workbench/pl.md): Wybierz z menu opcję **Modyfikacja → <img src="images/Draft_Draft2Sketch.svg" width=16px> Rysunek roboczy do szkicu**.
    -   [Środowisko pracy BIM](BIM_Workbench/pl.md): Wybierz opcję **Modyfikacja → <img src="images/Draft_Draft2Sketch.svg" width=16px> Rysunek roboczy do szkicu** z menu.
3.  Jeśli nie wybrałeś jeszcze żadnego obiektu: wybierz obiekt w oknie [widoku 3D](3D_view/pl.md).
4.  Zostanie utworzony nowy obiekt.



## Uwagi

-   Obiekty nie pochodzące ze środowiska pracy Rysunek Roboczy, które są całkowicie płaskie, również mogą być konwertowane.
-   Polecenie może obsługiwać tylko obiekty zbudowane z linii prostych, łuków kołowych, łuków eliptycznych, krzywych złożónych i krzywych Béziera.
-   [Krzywe Bezier\'a](Draft_BezCurve/pl.md) będą aproksymowane przez [Krzywe złożone przez punkty kontrolne](Sketcher_CreateBSpline/pl.md) środowiska Szkicownik.
-   Zewnętrzne środowisko pracy [KicadStepUp](KicadStepUp_Workbench/pl.md) zawiera polecenie do konwersji [krzywych złożonych](Draft_BSpline/pl.md) środowiska Rysunek Roboczy na serię [łuków](Sketcher_CreateArc/pl.md) Szkicownika. Więcej informacji można znaleźć w temacie na forum [BSplines to Shape2DView and Sketcher](https://forum.freecadweb.org/viewtopic.php?f=9&t=25082).
-   [Ten inny temat na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=58781#p505207) zawiera makrodefinicję do takiej konwersji.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby przekonwertować obiekty na szkic, użyj metody `make_sketch` ({{Version/pl|0.19}}) modułu Rysunek Roboczy. Metoda ta zastępuje przestarzałą metodę `makeSketch`.


```python
sketch = make_sketch(objects_list, autoconstraints=False, addTo=None, delete=False, name="Sketch", radiusPrecision=-1, tol=1e-3)
```

-    `lista_obiektów`zawiera obiekty do konwersji. Jest to pojedynczy obiekt lub lista obiektów. Obsługiwane są obiekty `Draft`, `Part::Feature` i `Part.Shape`.

-   Jeśli `więzyautomatyczne` ma wartość {{True/pl}}, wiązania zbieżności są dodawane do węzłów należących do tego samego obiektu źródłowego.

-    `dodajDo`jest istniejącym obiektem szkicu, do którego dodawana jest geometria. Jeśli nie zostanie podany, tworzony jest nowy szkic.

-   Jeśli `usuń` ma wartość {{True/pl}}, obiekty źródłowe są usuwane.

-    `nazwa`jest nazwą nowego szkicu.

-    `precyzjaPromienia`wskazuje, jak powinny być obsługiwane wiązania promienia:

    -   Użyj `-1`, aby wyłączyć wiązania promienia.
    -   Użyj `0`, aby dodać indywidualne wiązania promienia.
    -   Użyj liczby dodatniej, aby zaokrąglić promienie zgodnie z tą precyzją i dodać wiązania równości między krzywymi o równych promieniach.

-    `tol`jest tolerancją używaną do sprawdzania, czy kształty są płaskie i współpłaszczyznowe. Użyj `-1` dla ścisłej analizy.

-    `szkic`jest zwracany wraz z obiektem szkicu.

Aby przekonwertować szkic na obiekty środowiska Rysunek Roboczy, użyj metody `draftify` modułu Rysunek Roboczy.


```python
draftify(objectslist, makeblock=False, delete=True)
```

-    `listaobiektów`zawiera obiekty do konwersji. Jest to pojedynczy obiekt lub lista obiektów.

-   Jeśli `makeblock` ma wartość {{True/pl}}, konwertowane obiekty są grupowane w `Part::Part2DObject`.

-   Jeśli `usuń` ma wartość {{True/pl}}, obiekty źródłowe są usuwane.

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(2000, 1000)
circle = Draft.make_circle(500)
doc.recompute()

sketch_from_draft = Draft.make_sketch([rectangle, circle], autoconstraints=True, delete=False, radiusPrecision=0)
doc.recompute()

draft_from_sketch = Draft.draftify(sketch_from_draft, delete=False)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Draft2Sketch/pl

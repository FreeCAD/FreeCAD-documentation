# Sketcher scripting/pl
{{TOCright}}



## Tworzenie obiektu Szkicu przy użyciu środowiska Python 

Tworzymy obiekt Szkic w następujący sposób:


```python
import FreeCAD as App
import Part
import Sketcher

doc = App.newDocument()  

sketch = doc.addObject("Sketcher::SketchObject", "Sketch")
sketch.addGeometry(Part.LineSegment(App.Vector(1.2, 1.8, 0),
                                    App.Vector(5.2, 5.3, 0)), False)
sketch.addGeometry(Part.LineSegment(App.Vector(6.5, 1.5, 0),
                                    App.Vector(10.2, 5.0, 0)), False)
sketch.addGeometry(Part.LineSegment(App.Vector(12.2, 1.0, 0),
                                    App.Vector(15.4, 5.0, 0)), False)

doc.recompute()
```

Dodaje również trzy linie w nowo utworzonym Szkicu.



## Tworzenie wiązań przy użyciu środowiska Python 

Wiązania geometryczne <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> oraz <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:24px;"> można tworzyć z poziomu makropoleceń oraz z poziomu konsoli Python za pomocą następującego polecenia:


```pythonsketch.addConstraint(Sketcher.Constraint(ConstraintType, EdgeOrPartOfEdge…)) 
```

Wiązania wymiarowe <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:24px;"> <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:24px;"> oraz specjalne <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> [wiązanie prawo Snell\'a](Sketcher_ConstrainSnellsLaw/pl.md) można tworzyć z poziomu makropoleceń oraz konsoli Python za pomocą poniższego polecenia:


```pythonsketch.addConstraint(Sketcher.Constraint(DimensionalConstraintType, EdgeOrPartOfEdge…, App.Units.Quantity("float_value unit"))) 
```

na przykład


```pythonsketch.addConstraint(Sketcher.Constraint(DimensionalConstraintType, EdgeOrPartOfEdge…, App.Units.Quantity("123.0 mm"))) 
```

Pierwszy argument `ConstraintType` jest opisany poniżej w akapicie [Rodzaje wiązań](#Rodzaje_wiązań.md).

Wiązanie może przyjąć do sześciu argumentów, które są krawędziami lub wskazują, która część krawędzi jest używana przez wiązanie. Szczegóły dotyczące tego, jakie kombinacje krawędzi i ich części mogą być przekazane jako argumenty, znajdują się w dokumentacji poszczególnych wiązań. Głównym problemem w przypadku tej funkcji jest poprawne określenie numeru linii i numeru wierzchołka linii, które chcemy przetworzyć. Poniższe akapity opisują jak [identyfikować numerację linii](#Rozpoznawanie_numeracji_linii.md) oraz jak [identyfikować numerację części podrzędnych linii](#Rozpoznawanie_numeracji_części_składowych_linii.md).



## Rodzaje wiązań 

W przypadku wiązań geometrycznych pierwszym argumentem jest jeden z poniższych. Aby uzyskać informacje na temat możliwych kombinacji argumentów dozwolonych dla każdego wiązania, zobacz odpowiednią stronę funkcji.

++++
| Kod                        | Ikonka                                                                                     | Funkcja                                                            |
+============================+============================================================================================+====================================================================+
|             | <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;">       | [Zbieżność](Sketcher_ConstrainCoincident/pl.md)            |
| `"Coincident"`    |                                                                                            |                                                                    |
|                         |                                                                                            |                                                                    |
++++
|             | <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> | [Punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md) |
| `"PointOnObject"` |                                                                                            |                                                                    |
|                         |                                                                                            |                                                                    |
++++
|             | <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:24px;">           | [Pionowo](Sketcher_ConstrainVertical/pl.md)                |
| `"Vertical"`      |                                                                                            |                                                                    |
|                         |                                                                                            |                                                                    |
++++
|             | <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:24px;">       | [Poziomo](Sketcher_ConstrainHorizontal/pl.md)              |
| `"Horizontal"`    |                                                                                            |                                                                    |
|                         |                                                                                            |                                                                    |
++++
|             | <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;">           | [Równolegle](Sketcher_ConstrainParallel/pl.md)             |
| `"Parallel"`      |                                                                                            |                                                                    |
|                         |                                                                                            |                                                                    |
++++
|             | <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:24px;"> | [Prostopadle](Sketcher_ConstrainPerpendicular/pl.md)       |
| `"Perpendicular"` |                                                                                            |                                                                    |
|                         |                                                                                            |                                                                    |
++++
|             | <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;">             | [Stycznie](Sketcher_ConstrainTangent.md)                   |
| `"Tangent"`       |                                                                                            |                                                                    |
|                         |                                                                                            |                                                                    |
++++
|             | <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;">                 | [Zrównane](Sketcher_ConstrainEqual/pl.md)                  |
| `"Equal"`         |                                                                                            |                                                                    |
|                         |                                                                                            |                                                                    |
++++
|             | <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;">         | [Symetrycznie](Sketcher_ConstrainSymmetric/pl.md)          |
| `"Symmetric"`     |                                                                                            |                                                                    |
|                         |                                                                                            |                                                                    |
++++
|             | <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:24px;">                 | [Zablokowanie](Sketcher_ConstrainBlock/pl.md)              |
| `"Block"`         |                                                                                            |                                                                    |
|                         |                                                                                            |                                                                    |
++++

W przypadku wiązań wymiarowych pierwszym argumentem jest jeden z poniższych. Zobacz odpowiednią stronę funkcji dla możliwych kombinacji argumentów dozwolonych dla każdego wiązania

++++
| Kod                        | Ikonka                                                                             | Funkcja                                                         |
+============================+====================================================================================+=================================================================+
|             | <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;"> | [Długość w poziomie](Sketcher_ConstrainDistanceX/pl.md) |
| `"DistanceX"`     |                                                                                    |                                                                 |
|                         |                                                                                    |                                                                 |
++++
|             | <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;"> | [Długość w pionie](Sketcher_ConstrainDistanceY/pl.md)   |
| `"DistanceY"`     |                                                                                    |                                                                 |
|                         |                                                                                    |                                                                 |
++++
|             | <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:24px;">   | [Odległości](Sketcher_ConstrainDistance/pl.md)          |
| `"Distance"`      |                                                                                    |                                                                 |
|                         |                                                                                    |                                                                 |
++++
|             | <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:24px;">       | [Promień](Sketcher_ConstrainRadius/pl.md)               |
| `"Radius"`        |                                                                                    |                                                                 |
|                         |                                                                                    |                                                                 |
++++
|             | <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:24px;">   | [Średnica](Sketcher_ConstrainDiameter/pl.md)            |
| `"Diameter"`      |                                                                                    |                                                                 |
|                         |                                                                                    |                                                                 |
++++
|             | <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:24px;">         | [Kąt](Sketcher_ConstrainAngle/pl.md)                    |
| `"Angle"`         |                                                                                    |                                                                 |
|                         |                                                                                    |                                                                 |
++++
|             | <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:24px;">         | [Kąt](Sketcher_ConstrainAngle/pl.md)                    |
| `"AngleViaPoint"` |                                                                                    |                                                                 |
|                         |                                                                                    |                                                                 |
++++

Wiązanie <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> [prawo Snell\'a](Sketcher_ConstrainSnellsLaw/pl.md) w kontekście skryptów zachowuje się jak wiązanie wymiarowe. Ponownie, zobacz odpowiednią stronę funkcji dla możliwych kombinacji argumentów dozwolonych dla każdego wiązania.

++++
| Kod                    | Ikonka                                                                             | Funkcja                                                     |
+========================+====================================================================================+=============================================================+
|         | <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> | [prawo Snell\'a](Sketcher_ConstrainSnellsLaw/pl.md) |
| `"SnellsLaw"` |                                                                                    |                                                             |
|                     |                                                                                    |                                                             |
++++

Wiązanie <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:24px;"> [Lock](Sketcher_ConstrainLock.md) to polecenie GUI, które tworzy więz <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:24px;">. [Odległości poziomej](Sketcher_ConstrainDistanceX.md) i <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:24px;">, czyli nie jest wiązaniem samym w sobie.



## Rozpoznawanie numeracji linii 

Narysowałem trzy linie, jak pokazano na poniższym rysunku.

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure1.jpg  style="width:600px;">

Przesuwając kursor myszy nad linią jej numer można zobaczyć w lewym dolnym rogu okna programu FreeCAD, patrz następny rysunek.

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure2.jpg  style="width:600px;">

Niestety numeracja wyświetlana w oknach programu FreeCAD zaczyna się od 1, podczas gdy numeracja linii użytej w skrypcie zaczyna się od 0: oznacza to, że musisz odjąć jeden za każdym razem, gdy chcesz odwołać się do linii.

Liczby dodatnie oznaczają krawędzie szkicu (linie proste, okręgi, stożki, krzywe itd.). Następujące wartości mogą być używane do oznaczania elementów, które nie są krawędziami szkicu:

-    `-1`oznacza poziomą oś x

-    `-2`oznacza pionową oś y

-    `-n`oznacza numer elementu geometrii zewnętrznej `n-3` (np. element geometrii zewnętrznej o indeksie 0 na spłaszczonej liście `n-3`) *(np. element geometrii zewnętrznej o indeksie 0 na spłaszczonej liście `sketch.ExternalGeometry` byłby oznaczony przez -3, kolejny element na spłaszczonej liście byłby oznaczony -4 i tak dalej)*.



## Rozpoznawanie numeracji części składowych linii 

Podczas określania, na którą część linii ma wpływ wiązanie, można użyć następujących wartości:

-    `0`, aby wskazać, że wiązanie wpływa na całą krawędź.

-    `1`, aby wskazać, że wiązanie wpływa na punkt początkowy krawędzi *(pełny okrąg nie ma punktu początkowego)*.

-    `2`, aby wskazać, że wiązanie wpływa na punkt końcowy krawędzi.

-    `3`, aby wskazać, że wiązanie wpływa na punkt środkowy krawędzi. Dla <img alt="" src=images/Sketcher_CompCreateCircle.png  style="width:" height="24px;">[Okręgu](Sketcher_CompCreateCircle/pl.md) i <img alt="" src=images/Sketcher_CompCreateConic.png  style="width:" height="24px;">[Stożka](Sketcher_CompCreateConic/pl.md) *(elipsy)*, jest to środek okręgu lub środek *(przecięcie osi głównej i pomocniczej)* elipsy. Dla prostych <img alt="" src=images/Sketcher_CreateLine.svg  style="width:24px;"> [Linii](Sketcher_CreateLine/pl.md), `3` nie może być użyty do wskazania punktu środkowego.

-    `n`do wskazania, że wiązanie wpływa na n-ty biegun <img alt="" src=images/Sketcher_CompCreateBSpline.png  style="width:" height="24px;"> [krzywej złożonej](Sketcher_CompCreateBSpline/pl.md).

Wierzchołki oznaczone numerami 1 i 2 są ponumerowane zgodnie z kolejnością ich utworzenia. Aby sprawdzić kolejność ich utworzenia *(jeśli masz wiele linii, nie pamiętasz, który wierzchołek utworzyłeś jako pierwszy)*, wystarczy przesunąć kursor myszki nad dwa wierzchołki jednej linii, patrz poniższy rysunek.

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure3.jpg  style="width:600px;">

4 i 5, oznacza to, że do wierzchołka o niższym numerze *(4 w tym przykładzie)* odwołamy się za pomocą numeru 1 *(pierwszego w poleceniu skryptu)*, a do wierzchołka o wyższym numerze *(5 w tym przykładzie)* odwołamy się za pomocą numeru 2 w poleceniu skryptu.



## Przykład

Weźmy przykład z poprzednich trzech linijek. Kolejna cyfra wskazuje numerację każdej linii i ich wierzchołków zgodnie z konwencją dotyczącą skryptów.

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure3Bis.jpg  style="width:600px;">



*<b>niebieski tekst:</b> numeracja linii, <b>czarny tekst:</b> numeracja wierzchołków*

Polecenie `sketch.addConstraint(Sketcher.Constraint("Coincident", 1, 2, 2, 1))` daje następujący wynik:

<img alt="" src=images/PartDesignConstraintPointOnPointScriptingFigure4.jpg  style="width:600px;">

Pełny kod do narysowania trzech linii i dodania wiązania zbieżności dla dwóch punktów z dwóch linii wygląda następująco:


```python
import FreeCAD as App
import Part
import Sketcher

doc = App.newDocument()  

sketch = doc.addObject("Sketcher::SketchObject", "Sketch")
sketch.addGeometry(Part.LineSegment(App.Vector(1.2, 1.8, 0),
                                    App.Vector(5.2, 5.3, 0)), False)
sketch.addGeometry(Part.LineSegment(App.Vector(6.5, 1.5, 0),
                                    App.Vector(10.2, 5.0, 0)), False)
sketch.addGeometry(Part.LineSegment(App.Vector(12.2, 1.0, 0),
                                    App.Vector(15.4, 5.0, 0)), False)
sketch.addConstraint(Sketcher.Constraint("Coincident", 1, 2, 2, 1))

doc.recompute()
```


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher scripting/pl

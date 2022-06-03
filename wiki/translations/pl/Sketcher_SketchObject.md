# Sketcher SketchObject/pl
{{TOCright}}

## Wprowadzenie

<img alt="" src=images/Sketcher_Sketch.svg  style="width   *32px;">

Obiekt [SketchObject](Sketcher_SketchObject/pl.md), lub formalnie `Sketcher   *   *SketchObject`, jest podstawowym elementem do tworzenia obiektów 2D za pomocą środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md).

Obiekt `Sketcher   *   *SketchObject` wywodzi się z obiektu [Part2DObject](Part_Part2DObject/pl.md), co oznacza, że jest to obiekt [Cecha](Part_Feature/pl.md) wyspecjalizowany dla geometrii 2D. Podobnie jak obiekt Part2DObject, obiekt SketchObject może być dołączany do płaszczyzn i powierzchni. Ponadto obiekt SketchObject może obsługiwać wiązania geometryczne.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width   *800px;">



*Uproszczony diagram zależności pomiędzy podstawowymi obiektami w programie FreeCAD.*

## Użycie

1.  Przejdź do środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md).
2.  Naciśnij przycisk **[<img src=images/Sketcher_NewSketch.svg style="width   *16px"> [Utwórz szkic](Sketcher_NewSketch/pl.md)**.
3.  Wybierz **orientację szkicu** jako   * Płaszczyzna XY, Płaszczyzna XZ lub Płaszczyzna YZ. Opcjonalnie wybierz także opcję **Odwróć kierunek** i podaj wartość **Odsunięcia**.
4.  Naciśnij przycisk **OK**.

Chociaż obiekt SketchObject może być używany samodzielnie do rysowania na płaszczyźnie, jest on najczęściej używany w połączeniu ze środowiskiem [Projekt Części](PartDesign_Workbench/pl.md) do tworzenia brył wyciąganych.

1.  Przejdź do środowiska [Projekt Części](PartDesign_Workbench.md).

2.  Naciśnij przycisk **[<img src=images/PartDesign_Body.svg style="width   *16px"> [Zawartość](PartDesign_Body.md)**.

3.  Naciśnij przycisk **[<img src=images/PartDesign_NewSketch.svg style="width   *16px"> [Utwórz szkic](PartDesign_NewSketch/pl.md)**.

4.  
    **Wybierz cechę**   * Płaszczyzna\_XY *(płaszczyzna bazowa)*, Płaszczyzna\_XZ *(płaszczyzna bazowa)* lub Płaszczyzna\_YZ *(płaszczyzna bazowa)*.

5.  Naciśnij przycisk **OK**.

## Właściwości

Zobacz stronę [Właściwości](Property/pl.md) dla wszystkich typów właściwości, które mogą mieć obiekty tworzone skryptami.

Obiekt [SketchObject](Sketcher_SketchObject/pl.md) *(klasa `Sketcher   *   *SketchObject`)* wywodzi się z obiektu [Part2DObject](Part_Part2DObject/pl.md) *(klasa `Part   *   *Part2DObject`)* i dziedziczy wszystkie jego właściwości.

Obiekt SketchObject ma także następujące dodatkowe właściwości w obszarze [edytora właściwości](Property_editor/pl.md). Ukryte właściwości można pokazać za pomocą polecenia **Wyświetl wszystko** w menu kontekstowym okna [edycji właściwości](Property_editor/pl.md).

### Dane


{{TitleProperty|Szkic}}

-    **Geometria|GeometryList|ukryty**   * lista geometrii części istniejących wewnątrz szkicu.

-    **Wiązania|**   * nazwane wiązania, jeśli istnieją. W przeciwnym razie jest to pusta lista `[]`.

-    **Geometria zewnętrzna|LinkSubList**   * lista geometrii części spoza tego szkicu, które są używane jako odniesienie.

-    **W pełni związany|Bool|ukryty**   * *(tylko do odczytu)* jeśli parametr przyjmuje wartość {{TRUE/pl}} szkic jest w pełni związany.

### Widok


{{TitleProperty|Wiązania automatyczne}}

-    **Wiązania automatyczne|Bool**   * jeśli parametr ma wartość {{TRUE/pl}} to podczas rysowania geometrii automatycznie dodawane są wiązania.

-    **Unikaj wiązań nadmiarowych|Bool**   * jeśli parametr ma wartość {{TRUE/pl}} unika się zbędnych automatycznych wiązań.


{{TitleProperty|Siatka}}

-    **Automatyczny rozmiar siatki|Bool|ukryty**   * jeśli parametr ma wartość {{TRUE/pl}} rozmiar siatki jest zmieniany na podstawie ramki otaczającej geometrii szkicu.

-    **Rozmiar siatki|Length**   * wielkość odstępu między liniami siatki lokalnej w oknie [widoku 3D](3D_view/pl.md). Wartość domyślna to {{value|10 mm}}.

-    **Przyciąganie do siatki|Bool**   * jeśli parametr ma wartość {{TRUE/pl}} siatkę można wykorzystać do przyciągania punktów.

-    **Styl siatki|Enumeration**   * styl linii siatki {{value|Przerywana}} *(domyślnie)* lub {{value|Cienka}}.

-    **Pokaż siatkę|Bool**   * jeśli parametr ma wartość {{TRUE/pl}} w oknie [widoku 3D](3D_view/pl.md) zostanie wyświetlona siatka lokalna obiektu. Siatka ta jest niezależna od [siatki projektu](Draft_ToggleGrid/pl.md).

-    **Pokaż tylko w trybie edycji|Bool**   * jeśli parametr ma wartość {{TRUE/pl}} siatka jest wyświetlana tylko podczas edycji szkicu.

-    **Ciasna siatka|Bool**   * jeśli parametr ma wartość `True` lokalna siatka zostanie umieszczona wokół punktu położenia odniesienia kształtu, w przeciwnym razie będzie bardziej rozciągnięta.

-    **maksymalna liczba linii|Integer**   * maksymalna liczba wierszy w siatce.


{{TitleProperty|Widoczność automatyczna}}

-    **Środowisko edycji|String**   * nazwa środowiska roboczego, które ma zostać uaktywnione podczas edycji szkicu. Wartością domyślną jest {{value|SketcherWorkbench}}.

-    **Wymuś Ortho|Bool**   * jeśli parametr ma wartość {{TRUE/pl}} po otwarciu szkicu ujęcie widoku zostanie ustawione w trybie [ortogonicznym](Std_OrthographicCamera/pl.md).

-    **Ukryj zależne|Bool**   * jeśli parametr ma wartość {{TRUE/pl}} wszystkie obiekty zależne od szkicu są ukrywane po otwarciu szkicu.

-    **Restore Camera|Bool**   * jeśli parametr ma wartość {{TRUE/pl}} pozycja ujęcia widoku jest zapisywana przed otwarciem szkicu i przywracana po jego zamknięciu.

-    **Widok Przekroju|Bool**   * jeśli parametr ma wartość {{TRUE/pl}} podczas edycji szkicu widoczne są tylko obiekty *(ich części)* znajdujące się za płaszczyzną szkicu.

-    **Wyświetl odnośniki|Bool**   * jeśli parametr ma wartość {{TRUE/pl}} wszystkie obiekty używane w łączach do geometrii zewnętrznej są wyświetlane po otwarciu szkicu.

-    **Wyświetl podparcie|Bool**   * jeśli parametr ma wartość {{TRUE/pl}} po otwarciu szkicu są wyświetlane wszystkie obiekty, do których jest dołączony ten szkic.

-    **Tempo Vis|PythonObject|ukryty**   * klasa niestandardowa powiązana z tym obiektem, która obsługuje ukrywanie i pokazywanie innych obiektów podczas otwierania i zamykania szkicu.

## Tworzenie skryptów 


**Zobacz również   ***

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty skryptowe](Scripted_objects/pl.md).

Ogólne informacje na temat dodawania obiektów do dokumentu można znaleźć na stronie [Część   * właściwość](Part_Feature/pl.md).

Obiekt *SketchObject* jest tworzony za pomocą metody dokumentu `addObject()`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher   *   *SketchObject", "Sketch")
obj.Label = "Custom label"
```

Dlatego też, dla klasy podrzędnej [Python](Python/pl.md), powinieneś stworzyć obiekt `Sketcher   *   *SketchObjectPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Sketcher   *   *SketchObjectPython", "CustomSketch")
obj.Label = "Custom label"
```


{{Sketcher_Tools_navi

}} {{Document_objects_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SketchObject/pl

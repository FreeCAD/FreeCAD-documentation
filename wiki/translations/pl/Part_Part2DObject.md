# Part Part2DObject/pl
## Wprowadzenie

<img alt="" src=images/Tree_Part2D.svg  style="width:32px;">

Obiekt [Part2DObject](Part_Part2DObject/pl.md) środowiska Część, lub formalnie `Part::Part2DObject`, jest prostym elementem [kształtu topologicznego](Part_TopoShape/pl.md), który może być wyświetlany w oknie [widoku 3D](3D_view/pl.md).

Obiekt `Part::Part2DObject` wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md), ale jest wyspecjalizowany do geometrii 2D, ponieważ jego kształt będzie leżał na płaszczyźnie. Płaszczyzna ta jest zdefiniowana przez właściwość **Umiejscowienie** ( pozycja, normalna i obrót). Płaszczyzna może być jednak również zdefiniowana przez pomocnicze elementy geometryczne, takie jak płaszczyzna utworzona przez trzy dowolne wierzchołki lub ściana bryły.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Uproszczony diagram zależności pomiędzy podstawowymi obiektami w programie FreeCAD.*



## Użycie

Obiekt [Part Part2DObject](Part_Part2DObject/pl.md) jest obiektem wewnętrznym, więc nie można go utworzyć z poziomu interfejsu graficznego, tylko z poziomu [konsoli Python](Python_console/pl.md) jak opisano w sekcji [tworzenie skryptów](Part_Feature/pl#Tworzenie_skrypt.C3.B3w.md).

Obiekt `Part::Part2DObject` jest zdefiniowany w środowisku pracy [Część](Part_Workbench/pl.md), ale może być używany jako klasa bazowa dla [obiektów tworzonych skryptami](Scripted_objects/pl.md) we wszystkich [środowiskach pracy](Workbenches/pl.md), które tworzą dwuwymiarowe kształty geometryczne. Na przykład, jest to obiekt bazowy dla szkiców *([obiektów szkicu](Sketcher_SketchObject/pl.md))* i dla większości obiektów tworzonych za pomocą środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md).

Środowisko pracy może dodać więcej właściwości do tego podstawowego elementu, aby stworzyć obiekt o złożonym wyglądzie.



## Właściwości

Zobacz stronę [Właściwości](Property/pl.md) dla wszystkich typów właściwości, które mogą mieć obiekty tworzone skryptami.

Obiekt [Part Part2DObject](Part_Part2DObject.md) *(klasa `Part::Part2DObject`)* wywodzi się z [Część: Cecha](Part_Feature.md) *(klasa `Part::Feature`)* i dziedziczy wszystkie jej właściwości.

Obiekt Part2DObject ma także następujące dodatkowe właściwości w obszarze [edytora właściwości](Property_editor/pl.md). Ukryte właściwości można pokazać za pomocą polecenia **Wyświetl wszystko** w menu kontekstowym okna [edycji właściwości](Property_editor/pl.md).



### Dane


{{TitleProperty|Dołączenie}}

-    <div id="Property_Typ_mocowania">
    </div>**Typ mocowania|String|ukryty**: nazwa klasy obiektu attach engine sterującego dołączeniem. Domyślnie jest to `Attacher::AttachEnginePlane`.

-    <div id="Property_Podparcie">
    </div>
    **Podparcie|LinkSubList**: jest to płaszczyzna lub powierzchnia obsługująca geometrię 2D. Domyślnie jest to pusta lista `[]`.

-    <div id="Property_Tryb_dołączenia">
    </div>
    **Tryb odłączenia|Enumeration**: {{value|Dezaktywowany}} domyślnie. Ta właściwość określa płaszczyznę, która będzie używana przez obiekt jako odniesienie dla geometrii 2D. Kliknięcie na elipsę **...** *(trzy kropki)*, po prawej stronie pola edycyjnego, uruchamia polecenie [Część: Edycja mocowania](Part_EditAttachment.md), które umożliwia wybór płaszczyzny pomocniczej poprzez wybranie różnych elementów w oknie [widoku 3D](3D_view/pl.md). Dostępne są różne tryby: {{value|Deactivated}}, {{value|Przemieść położenie odniesienia}}, {{value|Objekt XY}}, {{value|Objekt XZ}}, {{value|Objekt YZ}}, {{value|Płaszczyzna ściany}}, {{value|Stycznie do powierzchni}}, {{value|Normalna do krawędzi}}, {{value|Frenet NB}}, {{value|Frenet TN}}, {{value|Frenet TB}}, {{value|Współśrodkowo}}, {{value|Płaszczyzna przez 3 punkty}}, {{value|Normalna do 3 punktów}}, {{value|Składanie}}, {{value|Bezwładność 2-3}}, {{value|Wyrównane O-N-X}}, {{value|Wyrównane O-N-Y}}, {{value|Wyrównane O-X-Y}}, {{value|Wyrównane O-X-N}}, {{value|Wyrównane O-X-N}}, {{value|Wyrównane O-Y-N}}, {{value|Wyrównane O-Y-X}}.

-    <div id="Property_Dołączenie_odwrotne">
    </div>
    **Dołączenie odwrotne|Bool**: wartość domyślna to {{FALSE/pl}}.Jeśli parametr ma wartość {{TRUE/pl}}, kierunek Z zostanie odwrócony. Na przykład [szkic](Sketch/pl.md) zostanie odwrócony do góry nogami. Ukryje, jeśli parametr **Tryb dołączenia** ma wartość {{value|Dezaktywowany}}.

-    <div id="Property_Ścieżka_dołączenia">
    </div>
    **Ścieżka dołączenia|Float|ukryty**: ustawia punkt krzywej, na który ma być mapowany [szkic](Sketch/pl.md). Przebiega od {{value|0}} do {{value|1}}, co odpowiada wartościom {{value|początek}} i {{value|koniec}}. Domyślnie przyjmuje wartość {{value|0}}.

-    <div id="Property_Odsunięcie_mocowania">
    </div>
    **Odsunięcie mocowania|umocowanie**: pozycja obiektu w oknie [widoku 3D](3D_view/pl.md), w odniesieniu do umiejscowienia obiektu dołączonego. Położenie jest określone przez punkt `Bazowy` *(wektor)* i punkt `Obrotu` *(oś i kąt)*. Zobacz [Umiejscowienie](Placement/pl.md). Ukryje, jeśli **Tryb dołączenia** ma wartość {{value|Dezaktywowany}}.



## Tworzenie skryptów 


**Zobacz również:**

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty skryptowe](Scripted_objects/pl.md).

Ogólne informacje na temat dodawania obiektów do dokumentu można znaleźć na stronie [Część: właściwość](Part_Feature/pl.md).

Obiekt Part2DObject jest tworzony za pomocą metody `addObject()`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObject", "Name")
obj.Label = "Custom label"
```

Dlatego też, dla klasy podrzędnej [Python](Python/pl.md), powinieneś stworzyć obiekt `Part::Part2DObject`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Part2DObjectPython", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Part2DObject/pl

# App GeoFeature/pl
## Wprowadzenie

<img alt="" src=images/Feature.svg  style="width:32px;">

Obiekt **App: Cechy geometrii**, lub formalnie `App::GeoFeature`, jest klasą bazową większości obiektów wyświetlających elementy geometryczne w oknie [widoku 3D](3D_view/pl.md), ponieważ zawiera właściwość **Umiejscowienie**.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Uproszczony diagram zależności pomiędzy podstawowymi obiektami w programie FreeCAD.*



## Użycie

App: Cechy geometrii jest obiektem wewnętrznym, więc nie można go utworzyć z poziomu interfejsu graficznego. Zasadniczo nie jest on przeznaczony do bezpośredniego użycia, a raczej może być podklasowany, aby uzyskać obiekt typu bare-bones, który ma tylko podstawową właściwość **Umiejscowienie** do zdefiniowania jego pozycji w oknie [Widoku 3D](3D_view/pl.md).

Niektóre z najważniejszych obiektów pochodnych są następujące:

-   Klasa [Część: Cecha](Part_Feature/pl.md), rodzic większości obiektów o kształtach [topologicznych](Part_TopoShape/pl.md) 2D i 3D.
-   Klasa [Siatka: Cecha](Mesh_Feature/pl.md), rodzic większości obiektów wykonanych z [Siatka](Mesh_MeshObject/pl.md), a nie brył.
-   Klasa [MES: FemMeshObject](FEM_Mesh/pl.md), rodzic siatek elementów skończonych utworzonych za pomocą [środowiska pracy MES](FEM_Workbench/pl.md).
-   Klasa [CAM: Cecha](Path_Feature/pl.md), rodzic ścieżek utworzonych za pomocą [środowiska pracy Część](Path_Workbench/pl.md) do użytku w obróbce CNC.
-   Klasa [App: Część](App_Part/pl.md), która definiuje [Std: Część](Std_Part/pl.md), które mogą być używane jako kontenery korpusów do wykonywania złożeń.

Podczas tworzenia tego obiektu w środowisku [Python](Python/pl.md), zamiast klasy podrzędnej `App::GeoFeature`, należy utworzyć klasę podrzędną `App::GeometryPython`, ponieważ ta ostatnia zawiera domyślnego dostawcę widoku oraz atrybuty `Proxy` dla samego obiektu i jego dostawcy widoku. Zobacz także sekcję [tworzenie skryptów](App_GeoFeature/pl#Tworzenie_skryptów.md).



## Właściwości App GeoFeature 

Zobacz stronę [Właściwości](Property/pl.md) dla wszystkich typów właściwości, które mogą mieć obiekty tworzone skryptami.

App: Cechy geometrii *(klasa`App::GeoFeature`)* jest pochodną podstawowego obiektu [App DocumentObject](App_DocumentObject/pl.md) *(klasa `App::DocumentObject`)* i dziedziczy wszystkie jego właściwości. Dodatkowo posiada właściwość **Umiejscowienie**, która kontroluje jego pozycję w oknie [Widoku 3D](3D_view/pl.md).



## Właściwości App GeometryPython 

Zobacz stronę [Właściwości](Property/pl.md) dla wszystkich typów właściwości, które mogą mieć obiekty tworzone skryptami.

Obiekt **App: Cechy geometrii Python** *(klasa `App::GeometryPython`)* jest pochodną podstawowego obiektu [App: Cechy geometrii](App_GeoFeature/pl.md) *(klasa `App::GeoFeature`)* i dziedziczy wszystkie jego właściwości. Posiada również kilka dodatkowych właściwości.

Są to właściwości dostępne w [edytorze właściwości](Property_editor/pl.md). Ukryte właściwości można wyświetlić za pomocą polecenia **Wyświetl wszystko** w menu kontekstowym [edytora właściwości](Property_editor/pl.md).



### Dane


{{TitleProperty|Podstawa}}

-    **Proxy|PythonObject|Ukryte**: niestandardowa klasa powiązana z tym obiektem.

-    **Umiejscowienie|Placement**: pozycja obiektu w [widoku 3D](3D_view/pl.md). Umiejscowienie jest definiowane przez punkt `Bazowy` *(wektor)* i `Obrót` *(oś i kąt)*. Zobacz informacje na stronie [Umiejscowienie](Placement/pl.md).

    -   
        **Kąt**
        
        : kąt obrotu wokół **Osi**. Domyślnie jest to {{value|0°}} *(zero stopni)*.

    -   
        **Oś**
        
        : wektor jednostkowy definiujący oś obrotu dla umiejscowienia. Każdy element jest wartością zmiennoprzecinkową pomiędzy {{value|0}} i {{value|1}}. Jeśli jakakolwiek wartość znajduje się powyżej {{value|1}}, wektor jest normalizowany tak, aby jego wielkość wynosiła {{value|1}}. Domyślnie jest to dodatnia oś Z, {{value|(0, 0, 1)}}.

    -   
        **Pozycja**
        
        : wektor ze współrzędnymi 3D punktu bazowego. Domyślnie jest to punkt odniesienia połażenia {{value|(0, 0, 0)}}.

-    **Etykieta|String**: edytowalna przez użytkownika nazwa tego obiektu, jest to dowolny ciąg UTF8.

-    **Etykieta2|String|Ukryte**: dłuższy, edytowalny przez użytkownika opis tego obiektu, jest to dowolny ciąg UTF8, który może zawierać nowe linie. Domyślnie jest to pusty ciąg {{value|""}}.

-    **SilnikWyrażeń|Ukryte**: lista wyrażeń. Domyślnie jest pusta {{value|[]}}.

-    **Widoczność|Bool|Ukryte**: określa czy obiekt ma być wyświetlany czy nie.



### Widok


{{TitleProperty|Baza}}

-    **Proxy|PythonObject|Ukryte**: niestandardowa klasa [dostawcy widoku](Viewprovider/pl.md) powiązana z tym obiektem.


{{TitleProperty|Opcje wyświetlania}}

.

-    **Ramka otaczająca|Bool**: jeśli ma wartość {{TRUE/pl}}, obiekt wyświetli obwiednię w oknie [widoku 3D](3D_view/pl.md).

-    **Tryb wyświetlania|Enumeration**: zobacz informacje w [App: Właściwości Python](App_FeaturePython/pl.md).

-    **Pokaż w drzewie|Bool**: zobacz informacje w [App: Właściwości Python](App_FeaturePython/pl.md).

-    **Widoczność|Bool**: zobacz informacje w [App: Właściwości Python](App_FeaturePython/pl.md).


{{TitleProperty|Styl obiektu}}

-    **Kolor kształtu|Color**: krotka trzech zmiennoprzecinkowych wartości RGB  jasnoszary .

-    **Materiał kształtu|Material|ukryte**: powiązany z tym obiektem [Materiał](App_Material/pl.md). Domyślnie włąściwość jest pusta.

-    **Przeźroczystość|Percent**: wartość całkowita od {{value|0}} do {{value|100}}, która określa poziom przeźroczystości ścian w [widoku 3D](3D_view.md). Wartość {{value|100}} oznacza całkowicie niewidoczne ściany, ściany są niewidoczne, ale nadal można je wybrać, o ile właściwość **Wybieralny** ma wartość {{TRUE/pl}}.


{{TitleProperty|Wybór}}

-    **Na górze po wybraniu|Enumeration**: zobacz informacje na stronie [App: Właściwości Python](App_FeaturePython/pl.md).

-    **Wybieralny|Bool**: jeśli ma wartość {{TRUE/pl}}, obiekt może zostać wybrany za pomocą kursora w oknie [widoku 3D](3D_view/pl.md). W przeciwnym razie obiekt nie może zostać wybrany, dopóki ta właściwość nie zostanie ustawiona na {{TRUE/pl}}.

-    **Styl wyboru|Enumeration**: zobacz informacje na ten temat zawarte na stronie [App: Właściwości Python](App_FeaturePython/pl.md).



## Tworzenie skryptów 


**Zobacz również:**

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty skryptowe](Scripted_objects/pl.md).

Ogólne informacje na temat dodawania obiektów do dokumentu można znaleźć na stronie [Część: właściwość](Part_Feature/pl.md).

Obiekt Cechy geometrii jest tworzony za pomocą metody `addObject()` dokumentu. Jeśli chcesz utworzyć obiekt o kształcie 2D lub 3D [kształt topologiczny](Part_TopoShape/pl.md), lepszym rozwiązaniem może być utworzenie jednej z klas podrzędnych wyspecjalizowanych do obsługi kształtów, na przykład [Część: Cecha](Part_Feature/pl.md) lub [Część: Część na obiekt 2D](Part_Part2DObject/pl.md).


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::GeoFeature", "Name")
obj.Label = "Custom label"
```

Dlatego też, dla klasy podrzędnej [Python](Python/pl.md), powinieneś stworzyć obiekt `App::GeometryPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::GeometryPython", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
⏵ [documentation index](../README.md) > App GeoFeature/pl

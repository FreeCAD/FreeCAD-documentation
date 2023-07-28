# Mesh Feature/pl
{{TOCright}}



## Wprowadzenie

<img alt="" src=images/Mesh_Tree.svg  style="width:32px;">

Obiekt [Cecha siatki](Mesh_Feature/pl.md), lub formalnie `Mesh::Feature`, jest prostym elementem z powiązanym [obiektem siatki](Mesh_MeshObject/pl.md), który może być wyświetlany w oknie [widoku 3D](3D_view/pl.md).

Cecha siatki jest podobna koncepcyjnie do cechy [Część: Cecha](Part_Feature/pl.md). Pierwsza jest obiektem bazowym dla elementów z informacją o \"siatce\", podczas gdy druga jest obiektem bazowym dla elementów z informacją o \"kształcie geometrycznym\".

Proszę zauważyć, że środowisko pracy [MES](FEM_Workbench/pl.md) również używa siatek, ale używa innego obiektu, zwanego [MES: Siatka](FEM_Mesh/pl.md) *(klasa `Fem::FemMeshObject`)*. Obiekt ten nie jest pochodną cechy Siatka i ma inne właściwości.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Uproszczony diagram zależności pomiędzy podstawowymi obiektami w programie FreeCAD.*



## Użycie

Prawie wszystkie obiekty siatkowe tworzone poleceniami dostępnymi w środowisku pracy [Siatka](Mesh_Workbench/pl.md) są [cechami siatki](Mesh_Feature/pl.md). Wyjątek stanowią parametryczne obiekty siatkowe tworzone poleceniem [Utwórz bryłę pierwotną](Mesh_BuildRegularSolid/pl.md). Obiekt [cecha siatki](Mesh_Feature/pl.md) można również utworzyć z poziomu [konsoli Python](Python_console/pl.md), jak opisano w sekcji [tworzenie skryptów](#Tworzenie_skrypt.C3.B3w.md).

Klasa `Mesh::Feature` jest zdefiniowana w środowisku pracy [Siatka](Mesh_Workbench/pl.md), ale może być użyta jako klasa bazowa dla [obiektów tworzonych skryptami](Scripted_objects/pl.md) we wszystkich [środowiskach pracy](Workbenches/pl.md), które wytwarzają płaskie i przestrzenne siatki.

Obiekt `Mesh::Feature` posiada proste właściwości, takie jak [umiejscowienie](Placement/pl.md), oraz właściwości wizualne określające wygląd jego krawędzi i ścian.



## Właściwości

Zapoznaj się z treścią na stronie [Właściwości](Property/pl.md) aby poznać wszystkie typy właściwości, które mogą mieć obiekty tworzone skryptami.

Klasa [Siatka: Cecha](Mesh_Feature/pl.md) (`Mesh::Feature`) wywodzi się z podstawowej [Cechy geometrii](App_GeoFeature/pl.md) (`App::GeoFeature`) i dziedziczy wszystkie jej właściwości. Posiada również kilka dodatkowych właściwości. Przede wszystkim właściwość **Siatka**, która przechowuje jej [obiekt siatki](Mesh_MeshObject/pl.md). Jest to geometria, która jest wyświetlana w oknie [widoku 3D](3D_view/pl.md).

Są to właściwości dostępne w [edytorze właściwości](Property_editor/pl.md). Ukryte właściwości można wyświetlić za pomocą polecenia **Wyświetl wszystko** w menu kontekstowym [edytora właściwości](Property_editor/pl.md).



### Dane


{{TitleProperty|Podstawa}}

-    **Pośrednik|PythonObject|Hidden**: niestandardowa klasa związana z tym obiektem. Istnieje to tylko dla wersji [Python](Python.md). Zobacz akapit [Tworzenie skryptów](#Tworzenie_skryptów/pl.md).

-    **Siatka|MeshKernel**: klasa [Siatka: MeshObject](Mesh_MeshObject/pl.md) związana z tym obiektem. Wymienia ona liczbę {{Value|Punktów}}, {{Value|Krawędzi}} i {{Value|Ścian}} siatki.

-    **Umiejscowienie|Placement**: pozycja obiektu w oknie [widoku 3D](3D_view/pl.md). Umiejscowienie jest określone przez `Base` punkt *(wektor)*, oraz `Obrót` *(oś i kąt)*. Zobacz stronę [Umiejscowienie](Placement/pl.md)

    -   
        **Kąt**
        
        : kąt obrotu wokół **Oś**. Domyślnie jest to wartość {{value|0°}} *(zero stopni)*.

    -   
        **Oś**
        
        : wektor jednostkowy określający oś obrotu dla umiejscowienia. Każdy element jest wartością zmiennoprzecinkową pomiędzy {{value|0}} a {{value|1}}. Jeśli jakakolwiek wartość jest większa od {{value|1}}, wektor jest normalizowany tak, aby jego wielkość wynosiła {{value|1}}. Domyślnie jest to dodatnia oś Z, {{value|(0, 0, 1)}}.

    -   
        **Pozycja**
        
        : wektor zawierający współrzędne 3D punktu bazowego. Domyślnie jest to początek układu odniesienia {{value|(0, 0, 0)}}.

-    **Etykieta|String**: edytowalna przez użytkownika nazwa tego obiektu, jest to dowolny ciąg znaków UTF8.

-    **Etykieta2|String|Hidden**: dłuższy, edytowalny przez użytkownika opis tego obiektu, jest to dowolny ciąg UTF8, który może zawierać znaki nowej linii. Domyślnie jest to pusty ciąg {{value|""}}.

-    **Silnik wyrażeń|Hidden**: lista wyrażeń. Domyślnie jest pusta {{value|[]}}.

-    **Widoczność|Bool|Hidden**: decyduje czy wyświetlać obiekt, czy nie.



### Widok


{{TitleProperty|Podstawa}}

-    **Proxy|PythonObject|Ukryte**: klasa własna [dostawca widoku](Viewprovider/pl.md) związana z tym obiektem. Istnieje wyłącznie dla wersji środowiska [Python](Python/pl.md). Zobacz sekcję [tworzenie skryptów](#Tworzenie_skrypt.C3.B3w.md).


{{TitleProperty|Opcje wyświetlania}}

-    **Ramka Otaczająca|Bool**: jeśli ma wartość {{TRUE/pl}}, obiekt będzie pokazywał Ramkę otaczającą w oknie [widoku 3D](3D_view/pl.md).

-    **Tryb wyświetlania|Enumeration**: {{value|Cieniowany}} *(bez krawędzi)*, {{value|Szkielet}} *(bez ścian)*, {{value|Cieniowany z krawędziami}} *(zwykła wizualizacja)*, {{value|Punkty}} *(tylko wierzchołki)*.

-    **Pokazuj na drzewie|Bool**: jeśli ma wartość {{TRUE/pl}}, obiekt pojawia się w oknie [Widoku Drzewa](Tree_view/pl.md). W przeciwnym razie jest niewidoczny.

-    **Widoczność|Bool**: jeśli ma wartość {{TRUE/pl}}, obiekt pojawia się w oknie [widoku 3D](3D_view/pl.md). W przeciwnym razie jest niewidoczny. Domyślnie właściwość ta może być włączana i wyłączana przez naciśnięcie klawisza **Spacja**.


{{TitleProperty|Styl obiektu}}

-    **Kolorowanie|Bool|Hidden**: wartość domyślna to {{FALSE/pl}}.

-    **Kąt zagięcia|FloatConstraint**:

-    **Oświetlenie|Enumeration**: {{value|Jednostronnie}} *(wartość domyślna)*, {{value|Dwustronnie}}. Oświetlenie pochodzi z dwóch stron lub z jednej strony w oknie [widoku 3D](3D_view/pl.md).

-    **Kolor linii|Color**: krotka trzech zmiennoprzecinkowych wartości RGB completely black .

-    **Przejrzystość linii|Percent**: wartość całkowita od {{value|0}} do {{value|100}} *(wartość procentowa)* określająca poziom przezroczystości krawędzi w oknie [widoku 3D](3D_view/pl.md). Wartość {{value|100}} oznacza całkowicie niewidoczne krawędzie. Krawędzie są niewidoczne, ale nadal można je wybrać, o ile parametr **Do wyboru** ma wartość {{TRUE/pl}}.

-    **Szerokość linii|FloatConstraint**: wartość typu zmiennoprzecinkowego określająca szerokość krawędzi w pikselach wyświetlane w oknie [widoku 3D](3D_view/pl.md). Wartość domyślna to {{value|1.0}}.

-    **Otwarte krawędzie|Bool**: wartość domyślna to {{FALSE/pl}}.

-    **Rozmiar punktu|FloatConstraint**: podobnie jak **Szerokość linii**, określa rozmiar wierzchołków.

-    **Kolor kształtu|Color**: podobnie jak light gray.

-    **Materiał kształtu|Material|Hidden**: obiekt [Materiał](App_Material/pl.md) związany z tym obiektem. Domyślnie jest on pusty.

-    **Przezroczystość|Percent**: wartość całkowita od {{value|0}} do {{value|100}} *(wartość procentowa)* określająca poziom przezroczystości ścian w oknie [widoku 3D](3D_view/pl.md). Wartość {{value|100}} oznacza całkowicie niewidoczne ściany. Ściany są niewidoczne, ale nadal można je wybrać, o ile parametr **Do wyboru** ma wartość {{TRUE/pl}}.


{{TitleProperty|Wybieranie}}

-    **Na górze po wybraniu|Enumeration**: {{value|Wyłączony}} *(domyślnie)*, {{value|Włączony}}, {{value|Objekt}}, {{value|Element}}.

-    **Do wyboru|Bool**: jeśli ma wartość {{TRUE/pl}}, obiekt można wybrać kursorem w oknie [widoku 3D](3D_view/pl.md). W przeciwnym razie obiekt nie może być wybrany, dopóki opcja ta nie zostanie ustawiona na wartość {{TRUE/pl}}.

-    **Styl wyboru|Enumeration**: {{value|Kształt}} *(domyślnie)*, {{value|Ramka Otaczająca}}. Jeśli parametr ma wartość {{value|Kształt}}, cały kształt *(wierzchołki, krawędzie i ściany)* zostanie podświetlony w oknie [widoku 3D](3D_view/pl.md). Jeśli {{value|Ramka Otaczająca}}, podświetlone zostanie tylko pole ograniczające.



## Tworzenie skryptów 


**Zobacz również:**

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty tworzone skryptami](Scripted_objects/pl.md).

Ogólne informacje na temat dodawania obiektów do dokumentu można znaleźć na stronie [Część: właściwość](Part_Feature/pl.md).

Cecha siatki jest tworzona za pomocą metody dokumentu `addObject()`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Mesh::Feature", "Name")
obj.Label = "Custom label"
```

Dlatego też, dla klasy podrzędnej [Python](Python/pl.md), powinieneś stworzyć obiekt `Mesh::FeaturePython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Mesh::FeaturePython", "Name")
obj.Label = "Custom label"
```


{{Mesh_Tools_navi

}} {{Document_objects_navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Mesh](Mesh_Workbench.md) > Mesh Feature/pl

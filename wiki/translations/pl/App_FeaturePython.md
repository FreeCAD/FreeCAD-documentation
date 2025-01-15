# App FeaturePython/pl
## Wprowadzenie

Obiekt <img alt="" src=images/Feature.svg  style="width:32px;"> [App: Właściwości Python](App_FeaturePython/pl.md), lub formalnie `App::FeaturePython`, jest prostą instancją [App: Obiekt dokumentu](App_DocumentObject/pl.md) w środowisku [Python](Python/pl.md).

Jest to prosty obiekt, który domyślnie nie ma wielu właściwości, na przykład nie ma [umiejscowienia](Placement/pl.md) lub [kształtu topologicznego](Part_TopoShape/pl.md). W zależności od przypisanych mu właściwości, może być używany do zarządzania różnymi typami danych.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Uproszczony diagram zależności pomiędzy podstawowymi obiektami w programie FreeCAD.*



## Użycie

App: Właściwości Python jest obiektem wewnętrznym, więc nie można go utworzyć z poziomu interfejsu graficznego. Jest on przeznaczony do tworzenia klas podrzędnych, które będą obsługiwać różne typy danych.

Na przykład obiekty [Adnotacja wieloliniowa](Draft_Text/pl.md), [Wymiar](Draft_Dimension/pl.md) i [Pośrednia płaszczyzna robocza](Draft_WorkingPlaneProxy/pl.md) w środowisku pracy [Rysunek Roboczy](Draft_Workbench/pl.md) są obiektami `App::FeaturePython` z niestandardową ikoną i dodatkowymi właściwościami. Przechowują one dane, ale nie rzeczywisty obiekt [kształtu topologicznego](Part_TopoShape/pl.md).

Jeśli pożądany obiekt ma mieć umiejscowienie, kształt, dołączenie lub inne złożone właściwości, lepiej jest utworzyć jedną z bardziej złożonych klas, na przykład [App: Cechy geometrii](App_GeoFeature/pl.md), [Część: Cecha](Part_Feature/pl.md) lub [Część: Część na obiekt 2D](Part_Part2DObject/pl.md).



## Właściwości

Zobacz stronę [Właściwości](Property/pl.md) dla wszystkich typów właściwości, które mogą mieć obiekty tworzone skryptami.

Klasa [App: Właściwości Python](App_FeaturePython/pl.md) (`App::FeaturePython`) jest pochodną podstawowej klasy [App: Obiekt dokumentu](App_DocumentObject/pl.md) *(`App::DocumentObject`)* i dziedziczy wszystkie jej właściwości. Posiada również kilka dodatkowych właściwości.

Są to właściwości dostępne w [edytorze właściwości](Property_editor/pl.md). Ukryte właściwości można wyświetlić za pomocą polecenia **Wyświetl wszystko** w menu kontekstowym [edytora właściwości](Property_editor/pl.md).



### Dane


{{TitleProperty|Podstawa}}

-    **Proxy|PythonObject|ukryte**: niestandardowa klasa powiązana z tym obiektem.

-    **Label|String**: edytowalna przez użytkownika nazwa tego obiektu, jest to dowolny ciąg UTF8.

-    **Label2|String|ukryte**: dłuższy, edytowalny przez użytkownika opis tego obiektu, jest to dowolny ciąg UTF8, który może zawierać nowe linie. Domyślnie jest to pusty ciąg {{value|""}}.

-    **ExpressionEngine|ukryte**: lista wyrażeń. Domyślnie jest pusta {{value|[]}}.

-    **Visibility|Bool|ukryte**: czy obiekt ma być wyświetlany czy nie.



### Widok


{{TitleProperty|Podstawa}}

-    **Proxy|PythonObject|ukryte**: niestandardowa klasa [Dostawca widoku](Viewprovider/pl.md) powiązana z tym obiektem.


{{TitleProperty|Opcje wyświetlania}}

-    **Display Mode|Enumeration**: domyślnie jest puste.

-    **Show In Tree|Bool**: wartość domyślna to {{TRUE/pl}}, w którym to przypadku obiekt pojawi się w oknie [widoku drzewa](Tree_view/pl.md). W przeciwnym razie obiekt zostanie ukryty w oknie drzewa. Gdy obiekt w drzewie jest niewidoczny, można go ponownie zobaczyć, otwierając menu kontekstowe nad nazwą dokumentu *(prawym przyciskiem myszki)* i wybierając {{CheckBox|TRUE|Pokaż elementy ukryte w widoku drzewa}}. Następnie można wybrać ukryty element i przełączyć właściwość **Pokaż w drzewie** z powrotem na wartość {{TRUE/pl}}.

-    **Visibility|Bool**: wartość domyślna to {{TRUE/pl}}, w którym to przypadku obiekt będzie widoczny w oknie [3D view](3D_view/pl.md), jeśli posiada [kształt](Part_TopoShape/pl.md), w przeciwnym razie będzie niewidoczny. Domyślnie właściwość ta może być włączana i wyłączana poprzez zaznaczenie obiektu i naciśnięcie przycisku **Spacja**.


{{TitleProperty|Wybieranie}}

-    **On Top When Selected|Enumeration**: kontroluje sposób, w jaki zaznaczenie pojawia się w oknie [widoku 3D](3D_view/pl.md), jeśli obiekt ma [kształt](Part_TopoShape/pl.md), a istnieje wiele obiektów częściowo zakrytych przez inne. Domyślnie {{value|Wyłączone}}, co oznacza, że nie pojawi się żadne specjalne podświetlenie. {{value|Włączone}} oznacza, że obiekt pojawi się na wierzchu każdego innego obiektu po wybraniu. {{value|Object}} oznacza, że obiekt pojawi się na wierzchu tylko wtedy, gdy cały obiekt zostanie wybrany w oknie [Widoku drzewa](Tree_view/pl.md). {{value|Element}} oznacza, że obiekt pojawi się na wierzchu tylko wtedy, gdy element podrzędny *(wierzchołek, krawędź, ściana)* zostanie wybrany w oknie [widoku 3D](3D_view.md).

-    **Selection Style|Enumeration**: kontroluje sposób podświetlenia obiektu, jeśli ma on [kształt](Part_TopoShape/pl.md). Jeśli jest to {{value|kształt}}, cały kształt *(wierzchołki, krawędzie i ściany)* zostanie podświetlony w oknie [widoku 3D](3D_view/pl.md); jeśli jest to {{value|Ramka otaczająca}}, pojawi się obwiednia otaczająca obiekt i zostanie podświetlona.



## Tworzenie skryptów 


**Zobacz również:**

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty skryptowe](Scripted_objects/pl.md).

Ogólne informacje na temat dodawania obiektów do dokumentu można znaleźć na stronie [Część: właściwość](Part_Feature/pl.md).

Obiekt App: Właściwości Python jest tworzony za pomocą metody dokumentu `addObject()`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::FeaturePython", "Name")
obj.Label = "Custom label"
```



---
⏵ [documentation index](../README.md) > App FeaturePython/pl

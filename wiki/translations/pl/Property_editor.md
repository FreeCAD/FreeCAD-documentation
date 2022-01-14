# Property editor/pl
{{TOCright}}

## Wprowadzenie

[Edytor właściwości](property_editor.md) pojawia się, gdy aktywna jest zakładka **Model** [widoku łączonego](combo_view.md). Umożliwia zarządzanie publicznie eksponowanymi właściwościami obiektów w dokumencie.

Ogólnie rzecz biorąc, edytor właściwości jest przeznaczony do obsługi tylko jednego obiektu w tym samym czasie. Wartości wyświetlane w edytorze właściwości należą do wybranego obiektu aktywnego dokumentu. Mimo to, niektóre właściwości, takie jak kolory, mogą być ustawione dla wielu zaznaczonych obiektów. Jeśli nie ma zaznaczonych elementów, edytor właściwości będzie pusty.

Nie wszystkie właściwości mogą być zawsze modyfikowane. W zależności od określonego statusu właściwości, niektóre z nich będą niewidoczne *(nie wymienione)* lub będą tylko do odczytu *(nie edytowalne)*. {{TOCright}}

![](images/FreeCAD_Property_editor_empty.png )



*Pusty edytor właściwości, gdy żaden obiekt nie jest zaznaczony.*

## Typy właściwości 

Właściwość jest informacją taką jak numer lub ciąg znaków dołączony do dokumentu FreeCAD lub obiektu w dokumencie.

Własny [obiekt skryptowy](scripted_objects.md) może używać dowolnych typów właściwości zdefiniowanych w systemie bazowym. Zobacz pełną listę [Właściwości](Property.md).

Niektóre z najczęściej używanych typów właściwości to właśnie: 
```python
App::PropertyBool
App::PropertyFloat
App::PropertyAngle
App::PropertyDistance
App::PropertyInteger
App::PropertyString
App::PropertyMatrix
App::PropertyVector
App::PropertyPlacement
```

Różne obiekty mogą mieć różne typy właściwości. Jednak wiele obiektów ma te same typy, ponieważ pochodzą one z tej samej klasy wewnętrznej. Na przykład, większość obiektów opisujących kształty geometryczne *(linie, okręgi, prostokąty, bryły, importowane części itp.)* ma właściwość **Położenie**, która określa ich położenie w widoku [3D](3D_view.md).

## Właściwości widoku i danych 

Istnieją dwie klasy właściwości obiektu dostępne poprzez zakładki w edytorze właściwości:

-    **View**właściwości związane z **wizualnym** wyglądem obiektu. Właściwości **View** są związane z **ViewProvider** (atrybut obiektu `ViewObject`) i są dostępne tylko wtedy, gdy załadowany jest graficzny interfejs użytkownika *(GUI)*. Nie są one dostępne przy korzystaniu z FreeCAD w trybie konsolowym lub jako biblioteka zasobów własnych.

-    **Data**właściwości związane z parametrami \"fizycznymi\" obiektu. Właściwości **Data** definiują podstawowe właściwości obiektu. Istnieją przez cały czas, nawet gdy FreeCAD jest używany w trybie konsolowym lub jako biblioteka. Oznacza to, że jeśli załadujesz dokument w trybie konsolowym, możesz edytować promień okręgu lub długość linii, nawet jeśli nie widzisz wyniku na ekranie.

Z tego powodu właściwości **Data** są uważane za bardziej **realne**, ponieważ naprawdę definiują geometrię kształtu. Z drugiej strony, właściwości **View** są mniej ważne, ponieważ wpływają jedynie na wygląd powierzchni geometrii. Na przykład okrąg o promieniu 10mm różni się od okręgu o promieniu 5mm. Kolor okręgu *(właściwość widoku)* nie ma wpływu na jego kształt, ale promień ma *(właściwość danych)*. W wielu przypadkach w niniejszej dokumentacji słowo **właściwość** jest rozumiane jako odnoszące się do **Właściwości danych**, a nie do **Właściwości widoku**.

### Własności podstawowe 


**Zobacz również: [Object name](Object_name.md)**

Najprostszy [obiekt skryptowy](scripted_objects.md) nie pokaże żadnej właściwości **Data** w edytorze właściwości, z wyjątkiem atrybutu `Label`. `Label` jest edytowalnym łańcuchem użytkownika, który identyfikuje obiekt w [widoku drzewa](tree_view.md). Z drugiej strony, atrybut `Name` obiektu jest przypisany w momencie jego utworzenia i nie może być zmieniony. Atrybut ten jest tylko do odczytu i również nie jest wyświetlany w edytorze właściwości.

Podstawowy obiekt parametryczny jest tworzony w następujący sposób.


```python
obj = App.ActiveDocument.addObject("App::FeaturePython", "App__FeaturePython")
obj.Label = "Plain_object"
print(obj.Name)
print(obj.Label)
```

<img alt="" src=images/FreeCAD_Property_editor_View_basic.png  style="width:" height="264px;"> <img alt="" src=images/FreeCAD_Property_editor_Data_basic.png  style="width:" height="264px;">



*Zakładki Widok i Dane edytora właściwości, dla podstawowego obiektu skryptowego '''App::FeaturePython'''.*

Większość obiektów geometrycznych, które mogą być tworzone i wyświetlane w [widoku 3D](3D_view.md) pochodzi z `Part::Feature`. Zobacz [Właściwości części](Part_Feature.md), aby dowiedzieć się, jakie podstawowe właściwości mają te obiekty.

Dla geometrii 2D większość obiektów pochodzi z [`Part::Part2DObject`](Part_Part2DObject.md) *(wywodzi się z [`Part::Feature`](Part_Feature.md))*, która jest podstawą Środowiska pracy [Sketches](Sketch.md), i większości [Elementy Draft](Draft_Workbench.md). Zobacz [Część2DObject](Part_Part2DObject.md), aby zapoznać się z najbardziej podstawowymi właściwościami tych obiektów.

## Działania


{{Version/pl|0.19}}

Kliknięcie prawym przyciskiem myszy w pustym miejscu widoku lub z wybraną właściwością powoduje wyświetlenie tylko jednego polecenia:

-    **Show all**: jeśli jest aktywny, oprócz standardowych właściwości, które już się pojawiają, pokazuje wszystkie ukryte właściwości danych i widoku w odpowiednich zakładkach.

    -   Dane: \"Proxy\", \"Label2\", \"Expression Engine\", oraz \"Visibility\".
    -   Widok: \"Proxy\".

Gdy opcja **Show all** jest aktywna, a wybrana jest jedna właściwość, dostępnych jest więcej akcji za pomocą drugiego kliknięcia prawym przyciskiem myszy:

-    **Show all**: dezaktywuje polecenie **Show all**, ukrywając dodatkowe właściwości Dane i Widok.

-    **Add Property**: dodaje dynamiczną właściwość do obiektu; działa to zarówno z obiektami zdefiniowanymi w C++ jak i Python [objekty skryptowane](scripted_objects.md).

-    **Expression**: przywołuje edytor formuły, który umożliwia użycie [wyrażenia](Expressions.md) w wartości właściwości.

-    **Hidden**: jeżeli opcja jest aktywna, ustawia właściwość jako ukrytą, co oznacza, że będzie wyświetlana w edytorze właściwości tylko wtedy, gdy aktywna jest opcja **Show all**.

-    **Output**: jeżeli opcja jest aktywna, ustawia właściwość jako wyjście.

-    **NoRecompute**: jeżeli opcja jest aktywna, ustawia właściwość jako nieprzeliczaną, gdy dokument jest ponownie obliczany. Jest to przydatne, gdy właściwość powinna być utrzymywana bez wpływu innych aktualizacji.

-    **ReadOnly**: jeśli opcja ta jest aktywna, ustawia daną cechę jako tylko do odczytu. Nie będzie można jej edytować w edytorze właściwości, dopóki przełącznik ten nie zostanie wyłączony. Pozycja menu **Wyrażenia...** nie jest już dostępna. **Uwaga:** Zmiana atrybutu może być nadal możliwa poprzez okno dialogowe, które aktualizuje daną cechę.

-    **Transient**: jeżeli opcja jest aktywna, ustawia właściwość jako przejściową. Wartość właściwości przejściowej nie jest zapisywana do pliku. Podczas otwierania pliku jest ona inicjowana wartością domyślną.

-    **Touched**: jeżeli opcja jest aktywna, to obiekt zostanie oznaczony do ponownego przeliczenia.

-    **EvalOnRestore**: jeżeli opcja jest aktywna, to obiekt jest przeliczany po przywróceniu dokumentu.

## Przykładowe właściwości obiektu z PartDesign 

W tej sekcji pokazujemy kilka wspólnych właściwości, które są widoczne dla [PartDesign Body](PartDesign_Body.md), oraz jedną cechę [PartDesign Feature](PartDesign_Feature.md). Specyficzne właściwości obiektu można znaleźć na stronie poświęconej dokumentacji tego obiektu.

### Widok

Większość z tych właściwości jest dziedziczona z obiektu podstawowego [Part Feature](Part_Feature.md).

<img alt="" src=images/FreeCAD_Property_editor_View.png  style="width:490px;"> {{TitleProperty|Base}}

-    **Angular Deflection**: jest to sposób na określenie, jak dokładnie wygenerować siatkę do renderowania na ekranie lub przy eksporcie. Domyślną wartość stanowi 28,5 stopnia lub 0,5 radiana. Im mniejsza wartość, tym gładszy będzie wygląd w [widok 3D](3D_view.md), oraz tym gęstsza siatka będzie eksportowana.

-    **Bounding Box**: określa, czy wyświetlana jest ramka pokazująca ogólny obszar obiektu.

-    **Deviation**: ustawia precyzję reprezentacji wielokątnej modelu w oknie [widoku 3D](3D_view.md) *(teselacja)*. Niższe wartości wskazują na lepszą jakość. Wartość jest wyrażona w procentach wielkości obiektu.

-    **Styl wyświetlania**: tryb wyświetlania całej bryły, {{Value|Linie konturu}} *(domyślnie)*, {{Value|Zacieniony}}, {{Value|Szkielet}}, {{Value|Punkty}}.

-    **Tryb wyświetlania - korpusu**: tryb wyświetlania krawędzi bryły, {{Value|Through}} *(domyślnie)*, {{Value|Tip}}.

-    **Draw Style**: {{Value|Solid}}, {{Value|Dashed}}, {{Value|Dotted}}, {{Value|Dashdot}}; definiuje styl krawędzi w oknie [widoku 3D](3D_view.md).

-    **Lighting**: {{Value|One side}}, {{Value|Two side}} *(domyślnie)*.

-    **Line Color**: składowe koloru RGB dla krawędzi, domyślnie jest to {{value|(25, 25, 25)}}.

-    **Line Width**: grubość krawędzi, domyślnie wynosi {{value|2}} piksele.

-    **On Top When Selected**: {{value|Disabled}}, {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Point Color**: składowe koloru RGB dla wierzchołków, domyślnie ustawia się na {{value|(25, 25, 25)}}.

-    **Point Size**: rozmiar wierzchołków, domyślnie ustawia się na {{value|2}} piksele.

-    **Selectable**: określa czy obiekt można zaznaczyć czy nie.

-    **Selection Style**: {{value|Shape}}, {{value|BoundBox}}.

-    **Shape Color**: składowe koloru RGB dla kształtu, domyślnie ustawia się na {{value|(204, 204, 204)}}.

-    **Show In Tree**: jeżeli posiada wartość `True`, obiekt pojawia się w widoku drzewa. W przeciwnym razie jest definiowany jako niewidzialny.

-    **Transparency**: stopień przejrzystości, zakres od {{value|0}} *(domyślnie)* do {{value|100}}.

-    **Visibility**: określa czy dany obiekt jest widoczny w oknie [widoku 3D](3D_view.md). Przełacznikiem jest klawisz **Spacja** z klawiatury komputera.




### Dane

W tym przypadku obserwujemy właściwości [PartDesign Wyciągnij przez obrót](PartDesign_Revolution.md).

<img alt="" src=images/FreeCAD_Property_editor_Data.png  style="width:490px;"> {{TitleProperty|Base}}

-    {{propertyData|Label}}: Zdefiniowana przez użytkownika nazwa nadana obiektowi, którą można dowolnie zmieniać.


{{TitleProperty|Part Design}}

-    **Refine**: Udoskonalenie procesu scalania z innymi przedmiotami.


{{TitleProperty|Revolution}}

-    **Base**: Punkt w przestrzeni, który określa, gdzie odbywa się wyciągnięcie przez obrót. Nie można go modyfikować bezpośrednio, tylko podczas edycji elementu.

-    **Axis**: Oś, wokół której będzie przeprowadzane wyciągnięcie przez obrót. Nie można go modyfikować bezpośrednio, tylko podczas edycji elementu.

-    {{propertyData|Angle}}: Kąt określający, o ile element bazowy jest obracany. Domyślnie jest to wartość {{value|360 stopni}}, jednakże możliwe jest wprowadzanie wartości dla dowolnego kąta.


{{TitleProperty|Sketch Based}}

-    **Midplane**: Jeśli obiektem bazowym jest [Szkic](Sketch.md), funkcja zwróci wartość `True`, i wykonany zostanie obrót przy użyciu szkicu służącego jako płaszczyzna symetrii. Jest to zauważalne, jeśli wartość **kąta** będzie inna niż {{value|360 stopni}}.

-    **Reversed**: wartość domyślna to `True`. Decyduje o kierunku obrotu podczas wykonywania wyciągnięcia.




## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics.md).

Zobacz dział [obiekty skryptowe](scripted_objects.md), aby uzyskać pełne informacje na temat dodawania właściwości do obiektów zdefiniowanych przez [Python](Python.md).

Do większości właściwości widocznych w edytorze właściwości można uzyskać dostęp z [Konsola Pythona](Python_console.md). Właściwości te są tylko atrybutami klasy definiującej wybrany obiekt. Na przykład, jeżeli edytor właściwości pokazuje właściwość **Group**, oznacza to, że obiekt posiada atrybut `Group`. 
```python
print(obj.Group)
```

Te atrybuty *(właściwości)* są dodawane metodą `addProperty` obiektu bazowego. Niezbędne jest podanie przynajmniej typu [property](property.md), oraz jego nazwy. 
```python
obj.addProperty("App::PropertyFloat", "Custom")
print(obj.Custom)
```

Właściwości są zgodne z konwencją `CapitalCamelCase` lub `PascalCase`, co oznacza, że każde słowo zaczyna się od dużej litery i nie ma żadnych podkreśleń. Gdy edytor właściwości wyświetla takie nazwy, pozostawia miejsce pomiędzy każdą wielką literą, ułatwiając jej odczytanie.


```python
obj.addProperty("App::PropertyDistance", "CustomCamelProperty")
obj.CustomCamelProperty = 1000
print(obj.CustomCamelProperty)
```

![](images/FreeCAD_Property_editor_Custom.png ) 
*Edytor właściwości obiektu pokazujący właściwości danych [PartDesign Body](PartDesign_Body.md), z dwiema dodatkowymi właściwościami, ''Custom'' oraz ''Custom Camel Property''.*

W podobny sposób dodawane są właściwości **widoku**, nie do obiektu bazowego, ale do jego reprezentacji `ViewObject`. Wynika z tego, że właściwości takie jak **Angular Deflection**, **Bounding Box**, **Display Mode Mode Body**, **Line Color** i inne mogą być badane i zmieniane z konsoli [Python](Python_console.md).


```python
print(obj.ViewObject.AngularDeflection)
print(obj.ViewObject.BoundingBox)
print(obj.ViewObject.DisplayMode)
print(obj.ViewObject.DisplayModeBody)
print(obj.ViewObject.LineColor)
```

Wszystkie publiczne właściwości obiektu i jego widoku dostawcy są zawarte w odpowiednim atrybucie `PropertiesList`. 
```python
print(obj.PropertiesList)
print(obj.ViewObject.PropertiesList)
```





{{Interface navi

}} {{Std Base navi}}

---
[documentation index](../README.md) > Property editor/pl

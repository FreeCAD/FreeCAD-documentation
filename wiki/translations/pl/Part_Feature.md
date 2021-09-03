

## Wprowadzenie


{{TOCright}}

<img alt="" src=images/Part_3D_object.svg  style="width:32px;">

Obiekt [Cecha Części](Part_Feature/pl.md), lub formalnie `Part::Feature`, jest prostym elementem z powiązanym z nim [kształtem topologicznym](Part_TopoShape/pl.md), który może być wyświetlany w oknie [widoku 3D](3D_view/pl.md).

Cecha części jest klasą nadrzędną dla większości obiektów 2D *(Rysunek roboczy, Szkicownik)* i 3D *(Część, Projekt części)*, z wyjątkiem siatek, które są zwykle oparte na [cechach siatek](Mesh_Feature/pl.md), lub [obiektach FemMesh](FEM_Mesh/pl.md) dla obiektów MES.

Każdy obiekt stworzony za pomocą środowiska [Część](Part_Workbench/pl.md) jest w istocie [cechą części](Part_Feature/pl.md).

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Uproszczony diagram zależności pomiędzy podstawowymi obiektami w programie. Klasa `Part::Feature* jest źródłem większości obiektów 2D ''(Rysunek roboczy, Szkicownik)'' i 3D ''(Część, Projekt części)'', które posiadają [kształt topologiczny](Part_TopoShape/pl.md).`

## Użycie

Obiekt [cecha części](Part_Feature/pl.md) jest obiektem wewnętrznym, więc nie można go utworzyć z poziomu interfejsu graficznego, tylko z poziomu [konsoli Python](Python_console/pl.md) jak opisano w sekcji [tworzenie skryptów](Part_Feature/pl#Tworzenie_skrypt.C3.B3w.md).

Klasa `Part::Feature` jest zdefiniowana w środowisku [Część](Part_Workbench/pl.md) ale może być użyta jako klasa bazowa dla [obiektów tworzonych skryptami](Scripted_objects/pl.md) we wszystkich [środowiskach pracy](Workbenches/pl.md) które produkują kształty geometryczne 2D i 3D. Zasadniczo wszystkie obiekty produkowane w środowisku pracy [Część](Part_Workbench/pl.md) są instancjami `Part::Feature`. Obiekty bryłowe importowane z plików STEP lub BREP będą importowane przy użyciu środowiska [Część](Part_Workbench/pl.md), więc będą również importowane jako elementy `Part::Feature`, aczkolwiek bez historii parametrycznej.


`Part::Feature`

jest również klasą nadrzędną [zawartości Projektu części](PartDesign_Body/pl.md), [cechy Projektu części](PartDesign_Feature/pl.md), oraz [Part2DObject](Part_Part2DObject/pl.md), która jest wyspecjalizowana dla kształtów 2D *(planarnych)*.

Element `Part::Feature` posiada proste właściwości jak [umiejscowienie](Placement/pl.md), oraz właściwości wizualne określające wygląd jego wierzchołków, krawędzi i ścian. Środowisko pracy może dodać więcej właściwości do tego podstawowego elementu, aby stworzyć obiekt o złożonym wyglądzie.

## Własności

[Cecha części](Part_Feature/pl.md) *(klasa `Part::Feature`)* wywodzi się z podstawowej [App: GeoFeature](App_GeoFeature/pl.md) *(klasa `App::GeoFeature`)*, dlatego dzieli wszystkie właściwości tej ostatniej.

Oprócz właściwości opisanych w [App: GeoFeature](App_GeoFeature/pl.md), Cecha części posiada właściwość **Kształt**, która przechowuje [kształt topologiczny części](Part_TopoShape/pl.md) tego obiektu. Jest to geometria, która jest wyświetlana w oknie [widoku 3D](3D_view/pl.md).

Inne właściwości, które posiada ten obiekt, to te związane z wyglądem jego [kształtu topologicznego](Part_TopoShape/pl.md), w tym {{PropertyView/pl|Odchylenie kątowe}}, **Odchylenie**, **Styl rysowania**, **Oświetlenie**, **Kolor linii**, **Szerokość linii**, **Kolor wierzchołka**, **Rozmiar wierzchołka**, a także właściwości ukryte **Kolor rozproszony**, **Tablica kolorów linii**, **Materiał linii**, **Tablica kolorów wierzchołków** i **Materiał punktu**.

Zobacz stronę [Właściwości](Property/pl.md) dla wszystkich typów właściwości, które mogą mieć obiekty tworzone skryptami.

Są to właściwości dostępne w [edytorze właściwości\|](Property_editor/pl.md). Ukryte właściwości można pokazać za pomocą polecenia {{MenuCommand|Wyświetl wszystko}} w menu kontekstowym okna [edycji właściwości](Property_editor/pl.md).

### Dane


{{TitleProperty|Podstawowe}}

-    **Umieszczenie|Placement**: pozycja obiektu w oknie [widoku 3D](3D_view/pl.md). Umieszczenie jest określone przez punkt `Base` *(wektor)* i `Rotation` *(oś i kąt)*. Zobacz stronę [Umiejscowienie](Placement/pl.md).

    -   
        **Kąt**
        
        : kąt obrotu wokół osi **Oś**. Domyślnie jest to {{value|0°}} *(zero stopni)*.

    -   
        **Oś**
        
        : wektor jednostkowy określający oś obrotu dla położenia. Każda składowa jest wartością zmiennoprzecinkową pomiędzy {{value|0}} a {{value|1}}. Jeśli jakakolwiek wartość jest powyżej {{value|1}}, wektor jest normalizowany tak, aby jego wielkość wynosiła {{value|1}}. Domyślnie jest to dodatnia oś Z, {{value|(0, 0, 1)}}.

    -   
        **Pozycja**
        
        : wektor zawierający współrzędne 3D punktu bazowego. Domyślnie jest to początek {{value|(0, 0, 0)}}.

-    **Etykieta|String**: nazwa obiektu edytowalna przez użytkownika, jest to dowolny ciąg znaków w kodowaniu UTF8.

#### Ukryte Dane właściwości {#ukryte_dane_właściwości}

-    **Pośrednik|PythonObject|hidden**: klasa własna związana z tym obiektem. Istnieje wyłącznie dla wersji środowiska [Python](Python/pl.md). Zobacz sekcję [tworzenie skryptów](Part_Feature/pl#Tworzenie_skrypt.C3.B3w.md).

-    **Kształt|PartShape|hidden**: klasa [kształt topologiczny części](Part_TopoShape/pl.md) związana z tym obiektem.

-    **Etykieta2|String|hidden**: dłuższy, edytowalny przez użytkownika opis tego obiektu, jest to dowolny łańcuch UTF8, który może zawierać znaki nowej linii. Domyślnie jest to pusty łańcuch {{value|""}}.

-    **Mechanizm wyrażeń|ExpressionEngine|hidden**: lista wyrażeń. Domyślnie jest ona pusta {{value|[]}}.

-    **Widoczność|Bool|hidden**: decyduje o tym, czy obiekt ma być wyświetlany, czy nie.

### Widok

Większość obiektów we FreeCAD ma coś, co nazywa się „[dostawca widoku](Viewprovider/pl.md)", jest to klasa definiująca wygląd obiektu w oknie [widoku 3D](3D_view/pl.md) oraz w [drzewie widoku](Tree_view/pl.md). Domyślny dostawca widoku obiektów elementu części definiuje właściwości prezentowane poniżej. Obiekty skryptowe, które pochodzą z elementu cecha części, również będą miały dostęp do tych właściwości.


{{TitleProperty|Podstawowe}}

-    **Pośrdnik|PythonObject|hidden**: klasa własna [dostawca widoku](Viewprovider/pl.md) związana z tym obiektem. Istnieje wyłącznie dla wersji środowiska [Python](Python/pl.md). Zobacz sekcję [tworzenie skryptów](Part_Feature/pl#Tworzenie_skrypt.C3.B3w.md).


{{TitleProperty|Opcje wyświetlania}}

-    **Ramka otaczająca|Bool**: jeśli wartość to `True`, obiekt wyświetli ramkę ograniczającą w [widoku 3D](3D_view/pl.md).

-    **Tryb wyświetlania|Enumeration**: {{value|Linie główne}} *(regularna wizualizacja)*, {{value|Zacieniony}} *(bez krawędzi)*, {{value|Model krawędziowy}} *(bez ścian)*, {{value|Punkty}} *(tylko wierzchołki)*.

-    **Pokaż na drzewie|Bool**: wartość domyślna to `True`, w którym to przypadku obiekt pojawi się w widoku [widoku drzewa](Tree_view/pl.md). W przeciwnym razie obiekt zostanie ukryty w widoku drzewa. Gdy obiekt w drzewie jest niewidoczny, można go ponownie wyświetlić, otwierając menu kontekstowe nad nazwą dokumentu *(prawy przycisk myszy)* i wybrać {{CheckBox|TRUE|Pokaż ukryte elementy}}. Następnie można wybrać ukryty element i wartość **Pokaż na drzewie** przełączyć z powrotem na `True`.

-    **Widoczność|Bool**: jeśli ma wartość `True`, obiekt pojawia się w [widoku 3D](3D_view/pl.md). W przeciwnym razie jest niewidoczny. Standardowo właściwość ta może być przełączana przez naciśnięcie klawisza **Spacja** na klawiaturze.


{{TitleProperty|Wygląd obiektu}}

-    **Odchylenie kątowe|Angle**: jest to towarzysz **Odchylenia**. Jest to kolejny sposób na określenie, jak precyzyjnie wygenerować siatkę do renderowania na ekranie lub podczas eksportu. Domyślną wartością jest {{value|28.5 stopni}}, lub {{value|0.5 radiana}}. Jest to wartość maksymalna, im mniejsza wartość tym gładszy będzie wygląd w [widoku 3D](3D_view/pl.md), i tym drobniejsza będzie siatka, która zostanie wyeksportowana.

-    **Odchylenie|FloatConstraint**: jest to towarzysz **Odchylenia kątowego**. Jest to kolejny sposób na określenie, jak drobna ma być generowana siatka do renderowania na ekranie lub podczas eksportu. Domyślną wartością jest {{value|0.5%}}. Jest to wartość maksymalna, im mniejsza wartość tym gładszy będzie wygląd w [widoku 3D](3D_view/pl.md) i tym drobniejsza będzie siatka, która zostanie wyeksportowana.

-    **Kolor rozproszenia|ColorList|hidden**: jest to lista krotek RGB definiujących kolory, podobna do {{PropertyView/pl|Kolor kształtu}}. Domyślnie jest to lista zawierająca jeden ciąg {{value| [(0,8, 0,8, 0,8)]}}.

Odchylenie jest wartością w procentach, która jest związana z wymiarami w milimetrach ramki otaczającej obiekt. Odchylenie w milimetrach można obliczyć w następujący sposób: 
```python
deviation_in_mm = (w + h + d)/3 * deviation/100
``` gdzie {{value|w}}, {{value|h}}, {{value|d}} są wymiarami ramki otaczającej.

-    **Styl rysowania|Enumeration**: {{value|Bryła}} *(domyślnie)*, {{value|Kreskowana}}, {{value|Kropkowana}}, {{value|Kropka-kreska}}, określa styl krawędzi w [widoku 3D](3D_view/pl.md).

-    **Oświetlenie|Enumeration**: {{value|Dwie strony}} *(domyślnie)*, {{value|Jedna strona}}; oświetlenie pochodzi z dwóch lub jednej strony w [widoku 3D](3D_view/pl.md).

-    **Kolor linii|Color**: krotka trzech zmiennoprzecinkowych wartości RGB  niemal czarny .

-    **Tablica kolorów linii|ColorList|hidden**: jest to lista krotek RGB określających kolory, podobna do **Kolor linii**. Domyślnie jest to lista {{value|[(0.09, 0.09, 0.09)]}}.

-    **Materiał linii|Material|hidden**: [App: Materiał](App_Material/pl.md) związany z krawędziami w tym obiekcie. Domyślnie jest on pusty.

-    **Szerokość linii|FloatConstraint**: wartość typu float określająca szerokość krawędzi w pikselach w [widoku 3D](3D_view/pl.md). Domyślnie przyjmuje wartość {{value|2.0}}.

-    **Kolor wierzchołka|Color**: podobnie jak **Kolor linii**, definiuje kolor wierzchołków.

-    **Tablica kolorów wierzchołków|ColorList|hidden**: jest to lista krotek RGB określających kolory, podobna do **Kolor wierzchołka**. Domyślnie jest to lista {{value|[(0.09, 0.09, 0.09)]}}.

-    **Materiał wierzchołka|Material|hidden**: [Materiał](App_Material/pl.md) powiązany z wierzchołkami w tym obiekcie. Domyślnie wartość jest pusta.

-    **Rozmiar wierzchołka|FloatConstraint**: podobnie jak **Szerokość linii**, definiuje rozmiar wierzchołków.

-    **Kolor kształtu|Color**: podobnie jak jasny szary.

-    **Materiał kształtu|Material|hidden**: [Materiał](App_Material/pl.md) związany z tym obiektem. Domyślnie wartość jest pusta.

-    **Przejrzystość|Percent**: liczba całkowita z zakresu {{value|0}} do {{value|100}}. *(wartość procentowa)* określająca poziom przezroczystości ścian w [widoku 3D](3D_view/pl.md). Wartość {{value|100}} oznacza całkowicie niewidoczne ściany Ściany są niewidoczne, ale nadal można je wybierać tak długo, jak wartość **Do wyboru** wynosi `True`.


{{TitleProperty|Wybieranie}}

-    **Na wierzchu po zaznaczeniu|Enumeration**: kontroluje sposób, w jaki zaznaczenie pojawia się w oknie [widoku 3D](3D_view/pl.md), jeśli obiekt ma [kształt](Part_TopoShape/pl.md) i jest wiele obiektów częściowo zakrytych przez inne. Domyślna wartość to {{value|Disabled}}, co oznacza, że nie pojawi się żadne specjalne podświetlenie. Wartość {{value|Enabled}} oznacza, że obiekt pojawi się na wierzchu każdego innego obiektu, gdy zostanie wybrany, {{value|Object}} oznacza, że obiekt pojawi się na wierzchu tylko jeśli cały obiekt jest zaznaczony w [widoku drzewa](Tree_view.md). Wartość {{value|Element}} oznacza, że obiekt pojawi się na wierzchu tylko jeśli element podrzędny *(wierzchołek, krawędź, ściana)* jest zaznaczony w [widoku 3D](3D_view/pl.md).

-    **Do wyboru|Bool**: jeśli parametr ma wartość `True`, obiekt może być wybrany kursorem myszki w [widoku 3D](3D_view/pl.md). W przeciwnym razie, obiekt nie może być wybrany dopóki ta opcja nie zostanie ustawiona na `True`.

-    **Styl wyboru|Enumeration**: kontroluje sposób podświetlania obiektu. Jeśli wybrano {{value|Kształt}}, cały kształt *(wierzchołki, krawędzie i ściany)* będzie podświetlony w [widoku 3D](3D_view/pl.md); jeśli jest to {{value|Ramka otaczająca}}, pole ograniczające pojawi się wokół obiektu i zostanie podświetlone.

### Wartość odchylenia {#wartość_odchylenia}

<img alt="" src=images/View_property_Deviation.svg  style="width:500px;"> *Parametry ugięcia algorytmu `BRepMesh_IncrementalMesh*; d < ugięcie liniowe, α < ugięcie kątowe.`

Zobacz wątek na forum, [Odchylenie i odchylenie kątowe](https://forum.freecadweb.org/viewtopic.php?f=3&t=45512).

## Tworzenie skryptów {#tworzenie_skryptów}


**Zobacz również:**

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty skryptowe](Scripted_objects/pl.md).

Cecha części jest tworzona za pomocą metody dokumentu `addObject()`. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::Feature", "Name")
obj.Label = "Custom label"
```

Ta podstawowa `Part::Feature` nie posiada obiektu Proxy, więc nie może być w pełni wykorzystana do tworzenia klas podrzędnych.

Dlatego też, dla klasy podrzędnej [Python](Python/pl.md), powinieneś stworzyć obiekt `Part::FeaturePython`. 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Part::FeaturePython", "Name")
obj.Label = "Custom label"
```

### Nazwa


**Zobacz również:**

[Nazwa obiektu](Object_name/pl.md), aby uzyskać więcej informacji na temat właściwości Nazwy.

Funkcja `addObject` posiada dwa podstawowe argumenty typu string.

-   Pierwszy argument wskazuje typ obiektu, w tym przypadku `"Part::FeaturePython"`.
-   Drugi argument jest łańcuchem określającym atrybut `Name`. Jeśli nie zostanie podany, domyślnie przyjmuje taką samą nazwę jak klasa, czyli `"Part__FeaturePython"`. Nazwa `Name` może zawierać tylko proste znaki alfanumeryczne oraz podkreślnik, `[_0-9a-zA-Z]`. Jeśli podane zostaną inne symbole, zostaną one zamienione na znaki podkreślenia, na przykład `"A+B:C*"` jest zamieniane na `"A_B_C_"`.

### Etykieta

W razie potrzeby atrybut `Etykieta` może zostać zmieniony na bardziej wymowny tekst.

-    `Etykieta`może przyjąć dowolny ciąg znaków UTF8, włączając w to akcenty i spacje. Ponieważ [widok drzewa](Tree_view/pl.md) wyświetla `Etykietę`, dobrą praktyką jest zmiana atrybutu `Etykiety` na bardziej opisowy ciąg znaków.

-   Domyślnie `Etykieta` jest unikalna, tak jak `Nazwa`. Jednak to zachowanie może być zmienione w [Edytorze Preferencji](Preferences_Editor/pl.md), {{MenuCommand|Edycja → Preferencje → Ogólne → Dokument → Zezwalaj na duplikowanie etykiet obiektów w jednym dokumencie}}. Oznacza to, że ogólnie `Etykieta` może być powtarzana w tym samym dokumencie, podczas testowania dla konkretnego elementu użytkownik powinien polegać na `Nazwie`, a nie na `Etykiecie`.


 {{Document objects navi}} 

# TopoShape API/pl
{{VeryImportantMessage
|''(listopad 2018 r.)'' Informacje te mogą być niekompletne i nieaktualne. Najnowsze API - patrz [https://www.freecadweb.org/api dokumentacja API generowana automatycznie].}}

Kształt Topologiczny jest obiektem macierzystym modułu Część. Wszystkie typy kształtów *(polilinia, ściana, bryła, itd\...)* modułu Część są Kształtami Topologicznymi i posiadają następujące atrybuty i metody. Przykład: 
```python
import Part
sh = Part.makeBox(10,10,10)
print sh.Faces
for f in sh.Faces:
   print f.Edges
```


{{APIProperty|Area|Całkowite pole powierzchni ścian figury.}}


{{APIProperty|BoundBox|Ramka otaczająca obiekt}}


{{APIProperty|CenterOfMass|Środek masy aktualnego układu. Jeżeli pole grawitacyjne jest jednorodne, jest to środek ciężkości. Współrzędne zwracane dla środka masy są wyrażone w bezwzględnym kartezjańskim układzie współrzędnych.}}


{{APIProperty|CompSolids|Wylicza kolejne figury w tym kształcie.}}


{{APIProperty|Compounds|Wylicza kolejne złożenia w tym kształcie.}}


{{APIProperty|Edges|Wylicza kolejne krawędzie w tym kształcie.}}


{{APIProperty|Faces|Wylicza kolejne ściany w tym kształcie.}}


{{APIProperty|Length|Całkowita długość krawędzi kształtu.}}


{{APIProperty|Matrix|Bieżąca transformacja obiektu jako macierz}}


{{APIProperty|Orientation|orientacja kształtu.}}


{{APIProperty|Placement|Bieżąca transformacja obiektu jako umiejscowienie}}


{{APIProperty|ShapeType|Typ kształtu.}}


{{APIProperty|Shells|Wyświetla listę następnych kształtów w tym kształcie.}}


{{APIProperty|Solids|Lista następnych kształtów w tym kształcie.}}


{{APIProperty|Vertexes|Lista wierzchołków w tym kształcie.}}


{{APIProperty|Volume|Całkowita objętość brył tego kształtu.}}


{{APIProperty|Wires|Lista polilinii w tym kształcie.}}


{{APIFunction|approximate| |Dokonuje aproksymacji krzywej złożonej z tej polilinii|obiekt BSplineCurve}}


{{APIFunction|check| |Sprawdza kształt i zgłasza błędy w strukturze kształtu. Jest to bardziej szczegółowe sprawdzenie jak w isValid().| }}


{{APIFunction|common|TopoShape|Przecięcie tego i danego kształtu topologicznego.|kształt topologiczny}}


{{APIFunction|complement| |Oblicza dopełnienie orientacji tego kształtu, tzn. odwraca wewnętrzny/zewnętrzny status granic tego kształtu..|kształt topologiczny}}


{{APIFunction|copy| |Creates a copy of this shape|kształt topologiczny}}


{{APIFunction|cut|TopoShape|Różnica pomiędzy obecnym a danym kształtem topologicznym.|kształt topologiczny}}


{{APIFunction|distToShape| TopoShape |Oblicza minimalną odległość pomiędzy obecnym i podanym kształtem topologicznym..|float<minimalny dystans>,list<najbliższe punkty>,list<najbliższe kształty podrzędne i parametry> }}


{{APIFunction|exportBrep| string |Eksportuje zawartość obecnego kształtu do pliku BREP. BREP jest natywnym formatem CasCade.| }}


{{APIFunction|exportIges| string |Eksportuje zawartość kształtu do pliku w formacie IGES.| }}


{{APIFunction|exportStep| string |Eksportuje zawartość kształtu do pliku w formacie STEP.| }}


{{APIFunction|exportStl| string |Eksportuje zawartość kształtu do pliku w formacie STL siatka.| }}


{{APIFunction|extrude|Vector|Wyciąga kształt wzdłuż kierunku.|kształt topologiczny}}


{{APIFunction|fuse|TopoShape|Połączenie obecnego i danego kształtu topologicznego.|kształt topologiczny}}


{{APIFunction|getAllDerivedFrom| |Zwraca wszystkie pochodne tego typu obiektu|lista}}


{{APIFunction|hashCode| |Wartość ta jest obliczana na podstawie wartości bazowego odniesienia kształtu i lokalizacji. Orientacja nie jest brana pod uwagę..|string}}


{{APIFunction|isClosed| |Sprawdza czy kształt ma formę zamkniętą.|boolean}}


{{APIFunction|isDerivedFrom|string|Zwraca wartość {{true/pl}}, jeśli podany typ jest ojcem.|boolean}}


{{APIFunction|isEqual|TopoShape|Zwraca wartość {{true/pl}}, jeśli oba kształty korzystają z tego samego kształtu topologicznego, mają to samo położenie i mają tę samą orientację.|boolean}}


{{APIFunction|isInside|Vector,float,Boolean|Sprawdza, czy punkt znajduje się wewnątrz bryły o określonej tolerancji. Jeśli trzeci parametr jest {{true/pl}}, punkt na powierzchni jest uważany za wewnętrzny.|boolean}}


{{APIFunction|isNull| |Sprawdza, czy kształt jest istniejący.|boolean}}


{{APIFunction|isPartner|TopoShape|Zwraca wartość {{true/pl}}, jeśli oba kształty mają ten sam kształt topologiczny, ale mogą mieć inne położenie i orientację.|boolean}}


{{APIFunction|isSame|TopoShape|Sprawdza czy oba kształty mają tę samą geometrię, zwraca wartość true jeśli oba kształty mają ten sam kształt topologiczny, mają to samo położenie, ale mogą mieć różną orientację.|boolean}}


{{APIFunction|isValid| |Sprawdza, czy kształt jest poprawny, tzn. czy istnieje, czy nie jest pusty lub uszkodzony.|boolean}}


{{APIFunction|makeFillet|float,TopoShape|Zwraca nowy obiekt oparty na kształcie topologicznym, ale z zaokrągleniem o promieniu "float" zastosowanym do każdej krawędzi.|kształt topologiczny}}


{{APIFunction|makeHomogenousWires|wire|Sprawia, że obecna i dany polilinia są jednorodne i mają taką samą liczbę krawędzi|polilinia}}


{{APIFunction|makeOffset|float|Przesuwa kształt o zadaną wartość.|kształt topologiczny}}


{{APIFunction|makePipe|wire|Wykonuje rurę przez przeciąganie po polilinii.|kształt topologiczny}}


{{APIFunction|makePipeShell|wire|Tworzy przeciągnięcie zdefiniowane przez profile wzdłuż polilinii.|kształt topologiczny}}


{{APIFunction|makeShapeFromMesh|mesh|Tworzy kształt złożony z danych siatki. Uwaga: Powinno być używane tylko dla raczej małych oczek.|kształt topologiczny}}


{{APIFunction|makeThickness|list,float,float|Bryłę wydrążoną buduje się z bryły wejściowej i zbioru ścian tej bryły, które mają zostać usunięte. Pozostałe ściany bryły stają się ścianami wydrążonej bryły, a ich grubość jest określana w czasie konstrukcji. Przekazywane argumenty to lista ścian, które mają zostać pominięte, grubość ścian oraz wartość tolerancji.|kształt topologiczny}}


{{APIFunction|nullify| |Niszczy referencję do kształtu przechowywaną w tym kształcie. W wyniku tego kształt ten staje się pusty.|}}


{{APIFunction|project|TopoShape|Rzutuj kształt na ten kształt.|kształt topologiczny}}


{{APIFunction|read|string|Wczytuje plik typu IGES, STEP lub BREP.|kształt topologiczny}}


{{APIFunction|reverse| |Odwraca orientację tego kształtu.| }}


{{APIFunction|revolve|Vector, Vector, float|Obraca kształt wokół osi o zadany stopień. ex: Part.revolve(Vector(0,0,0),Vector(0,0,1),360) obraca kształt wokół osi Z o 360 stopni.|kształt topologiczny}}


{{APIFunction|rotate|Vector<position>, Vector<direction>, float<angle>|Obraca ten kształt o wartość kąta w stopniach wokół osi określonej przez położenie i kierunek. np: Shp.rotate(Vector(0,0,0),Vector(0,0,1),180) obróć kształt wokół osi Z o 180 stopni.| }}


{{APIFunction|scale|float<factor>, [Vector<centre>]|Równomiernie skaluje ten kształt o współczynnik. Opcjonalnie określ środek transformacji skalującej.| }}


{{APIFunction|section|TopoShape|Przekrój tego z danym kształtem topologicznym.|kształt topologiczny}}


{{APIFunction|sewShape| |Zszywa kształt, jeśli występuje szczelina.| }}


{{APIFunction|tessellate|float|Tesseluje kształt i zwraca listę wierzchołków i indeksów ścian. Podana wartość "float" jest tolerancją.|lista}}


{{APIFunction|toNurbs| |Konwersja kompletnej geometrii kształtu na geometrię NURBS. Na przykład, wszystkie krzywe podpierające krawędzie kształtu bazowego są konwertowane na krzywe złożone, a wszystkie powierzchnie podpierające jego ściany są konwertowane na powierzchnie krzywych złożonych.|krzywa NURBS}}


{{APIFunction|transformGeometry|matrix|Stosuje transformację geometryczną na kopii kształtu. Zastosowana transformacja jest zdefiniowana jako macierz 4x4. Podstawowa geometria poniższych kształtów może zmienić się w krzywą, która obsługuje krawędź kształtu, lub powierzchnię, która obsługuje powierzchnię kształtu. Na przykład, okrąg może zostać przekształcony w elipsę podczas stosowania transformacji powinowactwa. Może się również zdarzyć, że okrąg zostanie wtedy przedstawiony jako krzywa złożona. Przekształcenie jest stosowane do wszystkich krzywych, które obsługują krawędzie kształtu oraz do wszystkich powierzchni, które obsługują ściany kształtu. Uwaga: Jeżeli chcesz przekształcić kształt bez zmiany jego geometrii, użyj metod translate lub rotate.|kształt topologiczny}}


{{APIFunction|transformShape|matrix|Stosuje transformację na kształcie bez zmiany geometrii bazowej.| }}


{{APIFunction|translate|Vector|Stosuje przesunięcie do aktualnego położenia tego kształtu.| }}


{{APIFunction|writeInventor| |Zapisuje siatkę w formacie OpenInventor do łańcucha znaków.|string}}

Niektóre atrybuty i metody mają zastosowanie tylko do określonych Kształtów Topologicznych. Te elementy mają zastosowanie do krawędzi *(TopoShapeEdge)*.


{{APIProperty|FirstParameter|Wartość parametru na jednym końcu Krawędzi. Niekoniecznie na Vertex[0]. [http://en.wikipedia.org/wiki/Parametric_equations Patrz równania parametryczne]}}


{{APIProperty|LastParameter|Wartość parametru na drugin końcu Krawędzi. Niekoniecznie na  Vertex[1].}}


{{APIFunction|getParameterByLength|Float|Mapuje przedział [0,Długość] na przedział [FirstParameter,LastParameter]|Float }}


{{APIFunction|valueAt|Float|Zwraca wektor 3D odpowiadający parametrowi value.|Vector}}


{{APIFunction|parameterAt|Vertex,[Face]|Zwraca wartość parametru odpowiadającą wierzchołkowi ''(3D point)''.|Float}}


{{APIFunction|tangentAt|Float|Zwraca wektor kierunku stycznej do krawędzi przy wartości parametru ''(jeśli istnieje)''.|Vector}}


{{APIFunction|normalAt|Float|Zwraca wektor kierunku normalnej do krawędzi na wartość parametru ''(jeśli istnieje jednoznacznie)''.|Vector}}


{{APIFunction|curvatureAt|Float|Zwraca krzywiznę krawędzi przy parametrze value.|Float}}


{{APIFunction|centerOfCurvatureAt|Float|Zwraca środek (punkt 3D) okręgu oscylującego przy parametrze value.|Vector}}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > TopoShape API/pl

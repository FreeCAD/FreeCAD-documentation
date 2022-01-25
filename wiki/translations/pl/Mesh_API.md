# Mesh API/pl
{{VeryImportantMessage
|''(listopad 2018 r.)'' Informacje te mogą być niekompletne i nieaktualne. Najnowsze API - patrz [https://www.freecadweb.org/api dokumentacja API generowana automatycznie].}}

Obiektami Siatek można manipulować poprzez dodawanie nowych elementów, usuwanie elementów, importowanie z pliku STL, przekształcanie siatki i wiele więcej. Dla pełnego przeglądu tego, co można zrobić zobacz także dokumentację środowiska pracy [Siatka](Mesh_Workbench/pl.md). Obiekt siatki nie może być dodany bezpośrednio do istniejącego dokumentu. Dlatego dokument musi tworzyć obiekt z klasą właściwości, która obsługuje siatki. Przykład:


```python
m = Mesh.Mesh()
... # Operowanie siatką
d = FreeCAD.activeDocument() # Uzyskaj dostęp do aktywnego dokumentu
f = d.addObject("Mesh::Feature", "Mesh") # Utwórz cechę siatki
f.Mesh = m # Przypisanie obiektu siatki do właściwości wewnętrznej
d.recompute()
```


{{APIFunction|addFacet|Facet|Dodaje wielokąt do siatki| }}


{{APIFunction|addFacets|list|Dodaje listę wielokątów do siatki| }}


{{APIFunction|addMesh|Mesh|Łączy tą siatkę z inną siatką.| }}


{{APIFunction|clear| |Oczyszcza siatkę| }}


{{APIFunction|coarsen| |Zmniejsza gęstość siatki| }}


{{APIFunction|collapseEdge|Edge|Usuwa krawędź i oba wielokąt, które dzielą tę krawędź| }}


{{APIFunction|collapseFacet|Facet|Usuwa wielokąt z siatki| }}


{{APIFunction|collapseFacets|list|Usuwa listę wielokątów z siatki| }}


{{APIFunction|copy| |Tworzy kopię siatki|obiekt siatki}}


{{APIFunction|countComponents| |Uzyskaj liczbę obszarów niezależnych topologicznie|integer}}


{{APIFunction|countNonUniformOrientedFacets| |Uzyskaj liczbę nieprawidłowo zorientowanych elementów.|integer}}


{{APIFunction|countSegments| |Podaj liczbę segmentów, która może być również równa 0|integer}}


{{APIFunction|crossSections| |Uzyskaj przekroje siatki poprzez różne płaszczyzny| }}


{{APIFunction|difference|Mesh|Różnica pomiędzy bieżącym a podanym obiektem siatki.| }}


{{APIFunction|fillupHoles| |Otwory do wypełniania| }}


{{APIFunction|fixDeformations| |Napraw zdeformowane wielokąty| }}


{{APIFunction|fixDegenerations| |Usuń zniekształcone wielokąty| }}


{{APIFunction|fixIndices| |Napraw wszystkie nieprawidłowe indeksy| }}


{{APIFunction|fixSelfIntersections| |Napraw samoprzecięcia| }}


{{APIFunction|flipNormals| |Odwróć wektory normalne| }}


{{APIFunction|foraminate| |Uzyskaj listę indeksów wielokątów i punktów przecięcia| }}


{{APIFunction|getPlanes| |Pobierz wszystkie płaszczyzny siatki jako segmenty. W najgorszym przypadku każdy trójkąt może być traktowany jako pojedyncza płaszczyzna, jeśli żaden z jego sąsiadów nie jest współpłaszczyznowy.| }}


{{APIFunction|getSegment|Uzyskaj listę indeksów wielokątów opisujących dany segment| }}


{{APIFunction|getSeparateComponents| |Zwraca listę zawierającą różne komponenty (wydzielone obszary) siatki jako oddzielne siatki.|lista}}


{{APIFunction|harmonizeNormals| |Dostosuj niewłaściwie zorientowane wielokąty| }}


{{APIFunction|hasNonManifolds| |Sprawdź, czy siatka ma elementy typu non-manifolds|boolean}}


{{APIFunction|hasNonUniformOrientedFacets| |Sprawdza czy siatka ma wielokąty o niespójnej orientacji| }}


{{APIFunction|hasSelfIntersections| |Sprawdź, czy siatka przecina samą siebie| }}


{{APIFunction|inner| |Pobierz część wewnątrz przecięcia| }}


{{APIFunction|insertVertex|Vertex|Wstawia wierzchołek do wielokąta| }}


{{APIFunction|intersect|Mesh|Przecięcie tego i podanego obiektu siatki| }}


{{APIFunction|isSolid| |Sprawdź, czy siatka jest bryłą| }}


{{APIFunction|meshFromSegment| |Tworzenie siatki z segmentu| }}


{{APIFunction|nearestFacetOnRay|tuple, tuple|Uzyskaj indeks i punkt przecięcia najbliższej półprostej. Pierwszym parametrem jest krotka trzech zmiennych określająca punkt bazowy półprostej, drugim parametrem jest krotka trzech zmiennych określająca kierunek. Wynikiem jest słownik z indeksem i punktem przecięcia lub pusty słownik, jeśli nie ma przecięcia|dictionary}}


{{APIFunction|offset|float|Przesuń punkt wzdłuż ich normalnych| }}


{{APIFunction|offsetSpecial|float|Przesuń punkt wzdłuż ich normalnych| }}


{{APIFunction|optimizeEdges| |Zoptymalizuj krawędzie, aby uzyskać ładniejsze wielokąty| }}


{{APIFunction|optimizeTopology| |Zoptymalizuj krawędzie, aby uzyskać ładniejsze wielokąty| }}


{{APIFunction|outer| |Pobierz część poza przecięciem| }}


{{APIFunction|printInfo| |Uzyskaj szczegółowe informacje na temat siatki| }}


{{APIFunction|read| |Wczytaj obiekt siatki z pliku.| }}


{{APIFunction|refine| |Dopracuj siatkę| }}


{{APIFunction|removeComponents|integer|Usuń elementy o liczbie wielokątów mniejszej lub równej podanej liczbie| }}


{{APIFunction|removeDuplicatedFacets| |Usuń zduplikowane wielokąty| }}


{{APIFunction|removeDuplicatedPoints| |Usuń zduplikowane punkty| }}


{{APIFunction|removeFacets|list|Usuń listę indeksów wielokątów z siatki| }}


{{APIFunction|removeFoldsOnSurface| |Usunąć fałdy na powierzchniach| }}


{{APIFunction|removeNonManifolds| |Usuń elementy typu non-manifolds| }}


{{APIFunction|rotate| |Zastosuj obrót do siatki| }}


{{APIFunction|setPoint|int, Vector|Ustawia punkt o indeksie| }}


{{APIFunction|smooth| |Wygładzić siatkę| }}


{{APIFunction|snapVertex| |Wstaw nowy wielokąt na granicy| }}


{{APIFunction|splitEdge| |Podział krawędzi| }}


{{APIFunction|splitEdges| |Podział wszystkich krawędzi| }}


{{APIFunction|splitFacet| |Podział wielokątów| }}


{{APIFunction|swapEdge| |Zamień wspólną krawędź z sąsiadem| }}


{{APIFunction|transform| |Zastosuj transformację do siatki| }}


{{APIFunction|transformToEigen| |Przekształć siatkę w jej bazę własną| }}


{{APIFunction|translate|Vector|Zastosuj przesunięcie do siatki| }}


{{APIFunction|unite|Mesh|Połączenie pomiędzy obecnym a podanym obiektem siatki| }}


{{APIFunction|write|string|Zapisz obiekt siatki do pliku| }}


{{APIFunction|writeInventor| |Zapisz siatkę w formacie OpenInventor do łańcucha znaków|a string}}


{{APIProperty|Area|Obszar obiektu siatki}}


{{APIProperty|CountEdges|Liczba wierzchołków obiektu siatki}}


{{APIProperty|CountFacets|Liczba wielokątów obiektu siatki}}


{{APIProperty|CountPoints|Liczba punktów obiektu siatki}}


{{APIProperty|Facets|Zbiór wielokątów. Za pomocą tego atrybutu można uzyskać dostęp do wielokątów siatki: for f in mesh.Facets: print f. Facet.Points jest listą krotek współrzędnych dla wierzchołków. Facet.PointIndices jest listą indeksów dla wierzchołków wielokątów. UWAGA! Przechowuj Wielokąty w zmiennej lokalnej, ponieważ jest ona generowana w locie, za każdym razem gdy jest dostępna}}


{{APIProperty|Points|Kolekcja punktów siatki; Dzięki temu atrybutowi można uzyskać dostęp do punktów siatki: for p in mesh.Points: print p.x, p.y, p.z,p.Index.UWAGA! przechowuj Punkty w zmiennej lokalnej, ponieważ jest ona generowana w locie, przy każdym dostępie}}


{{APIProperty|Topology|Punkty i indeksy wierzchołków jako krotki. Topology[0] jest listą wszystkich wierzchołków. Każdy z nich jest krotką 3 współrzędnych. Topology[1] jest listą wszystkich wielokątów. Każdy z nich jest listą indeksów wierzchołków w Topology[0] UWAGA! przechowuj Topology w zmiennej lokalnej, ponieważ jest ona generowana w locie, za każdym razem, gdy jest dostępna.}}


{{APIProperty|Volume|objętość obiektu siatki}}


{{APIProperty|BoundBox|Ramka ograniczająca obiektu}}


{{APIProperty|Matrix|Aktualna transformacja obiektu jako macierz}}


{{APIProperty|Placement|Aktualne przekształcenie obiektu jako umieszczenie}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Mesh](Mesh_Workbench.md) > Mesh API/pl

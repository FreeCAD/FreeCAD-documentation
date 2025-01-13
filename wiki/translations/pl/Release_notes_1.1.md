# Release notes 1.1/pl
**FreeCAD 1.1 jest w trakcie rozwoju, nie ma jeszcze oczekiwanej daty wydania.**


{{Message|
Czy brakuje jakichś funkcji? Wspomnij o nich w wątku na forum [https://forum.freecad.org/viewtopic.php?f&#61;10&t&#61;92080 Informacje o wydaniu v1.1].

Więcej informacji na temat sposobów przyczyniania się do rozwoju programu FreeCAD można znaleźć na stronie [Pomóż w rozwoju FreeCAD](Help_FreeCAD/pl.md).}}


{{Message|Wszystkie obrazy na tej stronie muszą używać przyrostka **_relnotes_1.1**.}}




**FreeCAD 1.1** zostanie wydany w roku *\...*, pobranie będzie możliwe ze strony [Pobieranie programu](Download/pl.md). Ta strona jest podsumowaniem najciekawszych zmian i funkcji.

Starsze uwagi na temat wydania FreeCAD można znaleźć na stronie [Lista funkcji](Feature_list/pl#Informacje_o_wydaniu.md).

Miejsce na przyciągający wzrok obrazek wybrany przez adminów z [galerii pokazowej użytkowników](https://forum.freecad.org/viewforum.php?f=24).



## Ogólne



## Interfejs użytkownika 



### Dalsze ulepszenia interfejsu użytkownika 

-   Dodano domyślny skrót dla [Preferencji](Std_DlgPreferences/pl.md). [Pull request #15536](https://github.com/FreeCAD/FreeCAD/pull/15536)
-   Usprawniono stronę preferencji obszaru powiadomień. [Pull request #15207](https://github.com/FreeCAD/FreeCAD/pull/15207)
-   Do narzędzia [Pomiary](Std_Measure/pl.md) dodano opcje automatycznego zapisu i wskazywania dodającego. [Pull request #17717](https://github.com/FreeCAD/FreeCAD/pull/17717)



## Rdzeń i API 



### Rdzeń programu 

+++
| <img alt="" src=images/Core_datums_relnotes_1.1.png  style="width:384px;"> | Narzędzia do globalnych geometrii konstrukcyjnych zostały dodane umożliwiając tworzenie układów współrzędnych, płaszczyzn, osi i punktów pomocniczych, które można również dołączać i wykorzystywać w Złożeniu. [Pull request #18332](https://github.com/FreeCAD/FreeCAD/pull/18332) |
+++

   
  <img alt="" src=images/Core_Transform_relnotes_1.1.gif  style="width:384px;">Kliknij na obrazku jeśli animacja nie uruchamia się automatycznie.   Narzędzie [Przemieszczenie](Std_TransformManip/pl.md) zostało przebudowane i pozwala teraz na precyzyjne sterowanie oprócz przeciągania w widoku 3D. Można wyrównywać interaktywny manipulator z dowolnym elementem w dokumencie i przemieszczać obiekt w lokalnym układzie współrzędnych (U, V, W) manipulatora lub w globalnym układzie współrzędnych. Manipulator można wyrównać z początkiem układu współrzędnych obiektu jak dotychczas, ale też ze środkiem masy obiekty. Dostępna jest nowa opcja do przesuwania obiekty (w położeniu manipulatora) do lokalizacji docelowej w dokumencie i odwracanie orientacji. [Pull request #17564](https://github.com/FreeCAD/FreeCAD/pull/17564)
   



### API



#### Usunięte API Pythona 



#### Zmienione API Phytona 



#### Nowe API Pythona 



## Środowisko pracy Start 



## Menadżer dodatków 



## Środowisko pracy Złożenie 

-   Dodane zostało narzędzie [Wstaw nową część](Assembly_InsertNewPart/pl.md) umożliwiające łatwe dodawanie nowych części do złożenia. [Pull request #17922](https://github.com/FreeCAD/FreeCAD/pull/17922)
-   Dodane zostało narzędzie [Utwórz symulację](Assembly_CreateSimulation/pl.md) umożliwiające dodawanie ruchów do połączeń i tworzenie animacji. [Pull request #16414](https://github.com/FreeCAD/FreeCAD/pull/16414)



### Pozostałe ulepszenia środowiska Złożenie 

-   Nowe globalne geometrie konstrukcyjne można wykorzystywać do dołączania połączeń aby składać części. [Pull request #18332](https://github.com/FreeCAD/FreeCAD/pull/18332)



## Środowisko pracy BIM 



### Pozostałe ulepszenia środowiska BIM 

-   Panel [Widoków BIM](BIM_Views/pl.md) został przebudowany i ma teraz również sekcję dla wszystkich widoków 2D. [Pull request #15836](https://github.com/FreeCAD/FreeCAD/pull/15836)
-   Wsparcie NativeIFC dla obiektów 2D objects zostało dodane do środowiska pracy BIM, pozwalając na osadzanie obiektów 2D (linii, tekstów, wymiarów) wewnątrz plików IFC, jak również otwieranie takich plików z innych programów BIM. [Pull request #16629](https://github.com/FreeCAD/FreeCAD/pull/16629)



## Środowisko pracy CAM 



### Pozostałe ulepszenia środowiska CAM 

-   Dodane zostały operacje gwintowania G84/G74. [Pull request #8069](https://github.com/FreeCAD/FreeCAD/pull/8069)
-   Do operacji profilowania dodane zostało wsparcie dla wielu przejść. [Pull request #17326](https://github.com/FreeCAD/FreeCAD/pull/17326)



## Środowisko pracy Rysunek Roboczy 



### Kolejne ulepszenia dla środowiska Rysunek Roboczy 

-   Dodano wsparcie dla względnych ścieżek czcionek do [Kształtu z tekstu](Draft_ShapeString/pl.md). [Pull request #17819](https://github.com/FreeCAD/FreeCAD/pull/17819)
-   Polecenie [Rysunek Roboczy: Zaokrąglenie](Draft_Fillet/pl.md) działa teraz na wskazanych krawędziach zamiast na pierwszej krawędzi wskazanych obiektów. [Pull request #17945](https://github.com/FreeCAD/FreeCAD/pull/17945) oraz [Pull request #18150](https://github.com/FreeCAD/FreeCAD/pull/18150)
-   Menu polecenia [Grupowanie automatyczne](Draft_AutoGroup/pl.md) dla warstw jest teraz sortowane alfabetycznie. [Pull request #18172](https://github.com/FreeCAD/FreeCAD/pull/18172)
-   Obsługa Łączy w [obiektach środowiska Rysunek Roboczy w środowisku Rysunek Techniczny](TechDraw_DraftView/pl.md) została naprawiona. [Pull request #18175](https://github.com/FreeCAD/FreeCAD/pull/18175)
-   Położenie pola *Mnożnik skali* w interfejsie zostało ulepszone ([Ustaw styl](Draft_SetStyle/pl.md), [Edytor stylu opisu](Draft_AnnotationStyleEditor/pl.md) i [Rysunek Roboczy: Ustawienia](Draft_Preferences/pl.md)). [Pull request #18299](https://github.com/FreeCAD/FreeCAD/pull/18299)



## Środowisko pracy MES 



### Pozostałe ulepszenia środowiska MES 

-   Szczegółowość logów Gmsh można teraz ustawić w [Preferencjach](FEM_Preferences/pl#Gmsh.md). [Pull request #17699](https://github.com/FreeCAD/FreeCAD/pull/17699)
-   Właściwość **Second Order Linear** i wsparcie dla [lokalnego zagęszczenia siatki](FEM_MeshRegion/pl.md), wcześniej dostępne tylko dla Gmsh, są teraz również dostępne dla nowej implementacji [Netgen](FEM_MeshNetgenFromShape/pl.md). [Pull request #17170](https://github.com/FreeCAD/FreeCAD/pull/17170)
-   Dodany został [przekrój](FEM_ElementGeometry1D/pl.md) skrzynkowy i eliptyczny dla belek. [Pull request #15843](https://github.com/FreeCAD/FreeCAD/pull/15843)
-   Narzędzie [Usuń wyniki](FEM_ResultsPurge/pl.md) usuwa teraz wszystkie obiekty wyników, nie tylko te natywne dla solvera CalculiX. [Pull request #18328](https://github.com/FreeCAD/FreeCAD/pull/18328)
-   [Wiązanie tie](FEM_ConstraintTie/pl.md) można teraz stosować na powierzchnie powłok. [Pull request #18325](https://github.com/FreeCAD/FreeCAD/pull/18325)
-   Dla solvera Elmer można teraz ustawić format wyników (binarny lub ASCII) i zapisywanie identyfikatorów geometrii, również w [Preferencjach](FEM_Preferences/pl#Elmer.md). [Pull request #17972](https://github.com/FreeCAD/FreeCAD/pull/17972)
-   Do [Filtra konturów](FEM_PostFilterContours/pl.md) dodana została opcja wygładzania. [Pull request #18088](https://github.com/FreeCAD/FreeCAD/pull/18088)
-   Dodany został parametr *BucklingAccuracy* dla [solvera CalculiX](FEM_SolverCalculixCxxtools/pl.md) - może być konieczny do uchwycenia pierwszej wartości własnej w liniowych analizach wyboczenia. [Pull request #18790](https://github.com/FreeCAD/FreeCAD/pull/18790)
-   Teraz wszystkie obiekty MES, dla których wygaszanie ma sens mogą zostać wygaszone. Wcześniej tylko warunki brzegowe i obciążenia były wygaszalne. [Pull request #18636](https://github.com/FreeCAD/FreeCAD/pull/18636)



## Środowisko pracy Materiał 



### Pozostałe ulepszenia środowiska Materiał 



## Środowisko pracy Siatka 



### Pozostałe ulepszenia środowiska Siatka 



## Środowisko pracy OpenSCAD 



### Pozostałe ulepszenia środowiska OpenSCAD 



## Środowisko pracy Część 



### Pozostałe ulepszenia środowiska Część 

-   Narzędzie [Sprawdź geometrię](Part_CheckGeometry/pl.md) teraz również zawiera wyniki dla prawidłowych kształtów, pokazuje pominięte obiekty i generuje raporty w [widoku raportu](Report_view/pl.md).



## Środowisko pracy Projekt Części 



### Pozostałe ulepszenia środowiska Projekt Części 

-   Początek Zawartości środowiska Projekt Części korzysta teraz z nowych globalnych geometrii konstrukcyjnych. Wygląd został zmieniony a płaszczyzny powiększają się przy tworzeniu nowego szkicu. Ponieważ orientacja była błędna w starszych wersjach programu FreeCAD, pliki w nich utworzone muszą być przekonwertowane przy otwieraniu. Może to zepsuć pliki z odniesieniami do geometrii konstrukcyjnych i pliki przekonwertowane lub utworzone na nowo w {{VersionPlus/pl|1.1}} będą zepsute w {{VersionMinus/pl|1.0}}. [Pull request #18126](https://github.com/FreeCAD/FreeCAD/pull/18126)
-   Polecenie [Włącz / wyłącz przeliczanie](Std_ToggleFreeze/pl.md) jest teraz dostępne ze środowiska pracy Projekt Części. [Pull request #18373](https://github.com/FreeCAD/FreeCAD/pull/18373)
-   Narzędzie [Otwórz](PartDesign_Hole/pl.md) może teraz tworzyć różne [gwinty Whitwortha](https://en.wikipedia.org/wiki/British_Standard_Whitworth), zgodnie z normami BSW, BSF, BSP i NPT. [Pull request #15744](https://github.com/FreeCAD/FreeCAD/pull/15744)
-   Wydajność gwintów modelowanych narzędziem [Otwór](PartDesign_Hole/pl.md) została zwiększona. [Pull request #15744](https://github.com/FreeCAD/FreeCAD/pull/15744)
-   Kąt początkowy dla zwężających się gwintów w narzędziu [Otwór](PartDesign_Hole/pl.md) jest teraz automatycznie ustawiany na wartość z norm ISO 7-1 i ASME B1.20.1. [Pull request #15744](https://github.com/FreeCAD/FreeCAD/pull/15744)



## Środowisko pracy Punkty 



### Pozostałe ulepszenia środowiska Punkty 



## Środowisko pracy Szkicownik 

   
  <img alt="" src=images/Sketcher_defining_external_relnotes_1.1.gif  style="width:384px;">Kliknij na obrazku jeśli animacja się nie uruchamia.   Dodane zostało narzędzie [Rzutowanie](Sketcher_Projection/pl.md) umożliwiające tworzenie definiującej [geometrii zewnętrznej](Sketcher_External/pl.md) i przełączanie między trybem definiującym i konstrukcyjnym dla geometrii zewnętrznej. [Pull request #17736](https://github.com/FreeCAD/FreeCAD/pull/17736)
   

+++
| <img alt="" src=images/Sketcher_intersection_relnotes_1.1.png  style="width:384px;"> | Dodane zostało narzędzie [Przecięcie](Sketcher_Intersection/pl.md) umożliwiające tworzenie [geometrii zewnętrznej](Sketcher_External/pl.md) w oparciu o wskazaną geometrię odniesienia i przecięcie z płaszczyzną szkicu. [Pull request #17736](https://github.com/FreeCAD/FreeCAD/pull/17736) |
+++

   
  <img alt="" src=images/Sketcher_external_faces_relnotes_1.1.gif  style="width:384px;">Click on the image if the animation does not start.   [Geometria zewnętrzna](Sketcher_External/pl.md) (zarówno rzutowania jak i przecięcia) może być teraz tworzona poprzez wskazanie ściany. [Pull request #17736](https://github.com/FreeCAD/FreeCAD/pull/17736)
   



### Pozostałe ulepszenia środowiska Szkicownik 

-   Możliwe jest teraz bezpośrednie używanie geometrii zewnętrznej (zarówno konstrukcyjnej, jak i definiującej) jako wejścia dla narzędzi takich jak odsunięcie czy szyk. [Pull request #17615](https://github.com/FreeCAD/FreeCAD/pull/17615)
-   Geometria zewnętrzna (rzutowania lub przecięcia) jest teraz domyślnie definiująca (nie trzeba jej obrysowywać jak w wersji 1.0 i starszych). Można ją przełączyć na konstrukcyjną jak każdą inną geometrię. [Pull request #17736](https://github.com/FreeCAD/FreeCAD/pull/17736)
-   Osie w Szkicowniku są teraz wyświetlane z nieskończoną długością. [Pull request #17312](https://github.com/FreeCAD/FreeCAD/pull/17312)
-   Szkice są teraz segregowane alfabetycznie w oknie dialogowym narzędzia [Mapuj szkic na powierzchnię](Sketcher_MapSketch/pl.md). [Pull request #16518](https://github.com/FreeCAD/FreeCAD/pull/16518)
-   Dodane zostały grupowe przeciąganie, co umożliwia jednoczesne przeciąganie wszystkich zaznaczonych obiektów geometrycznych. [Pull request #18273](https://github.com/FreeCAD/FreeCAD/pull/18273)
-   Dodane zostało nowe ustawienie, które, jeśli zaznaczone, sprawia, że tworzenie geometrii zewnętrznej jest niezależne od aktualnego trybu konstrukcyjnego - jest ona wtedy zawsze tworzona jako geometria odniesienia. [Pull request #18697](https://github.com/FreeCAD/FreeCAD/pull/18697)



## Środowisko pracy Arkusz Kalkulacyjny 



### Pozostałe ulepszenia środowiska Arkusz Kalkulacyjny 

-   Dodane zostały domyślne skróty dla poleceń [Pogrub](Spreadsheet_StyleBold/pl.md), [Pochyl](Spreadsheet_StyleItalic.md) i [Podkreśl](Spreadsheet_StyleUnderline.md). [Pull request #15556](https://github.com/FreeCAD/FreeCAD/pull/15556)
-   Dwukrotne kliknięcie na separatorze w nagłówku dopasowuje teraz rozmiar kolumny do jej zawartości. [Pull request #16296](https://github.com/FreeCAD/FreeCAD/pull/16296)
-   Do Arkusza Kalkulacyjnego dodane zostało przybliżanie. [Pull request #16130](https://github.com/FreeCAD/FreeCAD/pull/16130)



## Środowisko pracy Powierzchnia 3D 



### Pozostałe ulepszenia środowiska Powierzchnia 3D 



## Środowisko pracy Rysunek Techniczny 



### Pozostałe ulepszenia środowiska Rysunek Techniczny 

-   Narzędzie [Wstaw adnotację obszaru](TechDraw_AreaDimension/pl.md) teraz poprawnie uwzględnia otwory w ścianach. [Pull request #17740](https://github.com/FreeCAD/FreeCAD/pull/17740)
-   Dodana została walidacja kształtu - można ją włączyć w [Preferencjach](TechDraw_Preferences/pl#Zaawansowane.md). [Pull request #18282](https://github.com/FreeCAD/FreeCAD/pull/18282)



## Kompilacja



## Znane ograniczenia 



## Dodatkowe zasoby



---
⏵ [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.1/pl

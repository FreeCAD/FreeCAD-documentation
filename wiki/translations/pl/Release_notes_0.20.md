# Release notes 0.20/pl
**Ta strona zawiera nowe funkcje, które są dodawane do wersji deweloperskiej FreeCAD, aktualnie oznaczonej numerem '''0.20'''. Gdy nastąpi zamrożenie funkcjonalności wersji 0.20, usuń ten komunikat i nie dodawaj więcej funkcji do tej strony. Oczekuje się, że FreeCAD 0.20 zostanie wydany po roku 2021.**


**Wszystkie obrazy na tej stronie muszą używać przyrostka {{FileName|_relnotes_0.20** !!!}}


{{Message|
Czy brakuje jakichś funkcji? Wspomnij o nich w wątku na forum [https://forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;56135 Informacje o wydaniu v0.20].

Zobacz artykuł [Pomóż w rozwoju FreeCAD](Help_FreeCAD.md), aby dowiedzieć się więcej na temat sposobów wspierania FreeCAD.
}}


{{TOCright}}

**FreeCAD 0.19** zostanie wydany w roku *2020*, pobranie będzie mozliwe ze strony [Download](Download.md). Jest to podsumowanie najciekawszych zmian. Pełna lista zmian znajduje się w [MantisBT bugtracker FC 0.20 changelog](https://www.freecadweb.org/tracker/changelog_page.php?version_id=78).

Starsze uwagi na temat wydania FreeCAD można znaleźć na stronie [Lista funkcji](Feature_list/pl#Informacje_o_wydaniu.md).

## Najważniejsze informacje 

## Informacje ogólne 

### Python 3 oraz Qt5 

### Znane problemy 

### W rozwoju 

Aby przeprowadzić [kompilację w systemie Windows](Compile_on_Windows/pl.md), dostępne są różne Libpacki *(wstępnie spakowane biblioteki)*:

-   Libpack dla Windows z Qt xx, OCC yy, i Python zz

Najniższa obsługiwana wersja Pythona to 3.6.9 według <https://forum.freecadweb.org/viewtopic.php?f=10&t=62701>.

Obsługiwane systemy operacyjne:

-   Linux Ubuntu Bionic Beaver (18.04) i Focal Fossa (20.04)
-   MacOS wersja minimalna 10.12 Sierra
-   Windows 7, 8 i 10

Inne wiadomości dotyczące rozwoju:

### Dokumentacja

### Znane problemy 

## Interfejs użytkownika 

+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/Navi_Cube_relnotes_0.20.gif ) | Kostka nawigacyjna została przerobiona, aby umożliwić korzystanie z tych nowych funkcji:                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                | -   Istnieją teraz krawędzie umożliwiające oglądanie ujęcia pod kątem 45°.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                | -   Nowa opcja [Obróć do najbliższego](Preferences_Editor/pl#Nawigacja.md) pozwala na oglądanie sceny w najbliższym sensownym stanie. Gdy jest ona wyłączona, kliknięcie na ścianę sześcianu spowoduje, że będzie ona zawsze w tej samej pozycji, niezależnie od tego, w jakiej pozycji kostki się znajdowałeś, gdy klikałeś na tę ścianę. Zobacz animację po lewej stronie, aby zrozumieć, co to oznacza. Spróbuj wykonać taką samą sekwencję kliknięć jak w animacji bez opcji *Obróć do najbliższego*, aby poznać różnicę. |
|                                                                | -   Klikając na kropkę umieszczoną na górze po prawej stronie kostki, można szybko zobaczyć widok z tyłu aktualnego ujęcia.                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                | -   Rozmiar sześcianu można dostosować za pomocą opcji [Rozmiar kostki](Preferences_Editor/pl#Nawigacja.md).                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                | [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=52118), [pull request \#4502](https://github.com/FreeCAD/FreeCAD/pull/4502).                                                                                                                                                                                                                                                                                                                                                                                     |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

  -------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](images/Improved_tooltips_relnotes_0.20.gif )   Tooltipy wyświetlają teraz nazwę polecenia w tytule, ułatwiając nowym użytkownikom szukanie pomocy. Na końcu podpowiedzi, pomiędzy nawiasami, użytkownik może również przeczytać *(Std\_WhatsThis)*, które dokładnie odpowiadają nazwie strony wiki. [dyskusja na Forum](https://forum.freecadweb.org/viewtopic.php?f=34&t=58747), [pull request \#4502](https://github.com/FreeCAD/FreeCAD/pull/4978).
  -------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/Std_UserEditMode_relnotes_0.20.gif  style="width:384px;">   Nowe polecenie [Std UserEditMode](Std_UserEditMode/pl.md) pozwala użytkownikowi wybrać tryb edycji, który będzie używany, gdy obiekt zostanie dwukrotnie kliknięty w [Widoku drzewa](Tree_view/pl.md). Kliknij na obrazek po lewej stronie, aby zobaczyć animację wyboru. Jeśli wybrany tryb edycji nie ma zastosowania, zostanie użyty domyślny tryb edycji obiektu. [Pull request \#5110](https://github.com/FreeCAD/FreeCAD/pull/5110).
  ------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/Dependencies-selection_relnotes_0.20.png ) | Dodano opcję **Dodaj do zaznaczenia obiekty zależne** do menu kontekstowego [widoku drzewa](Tree_view/pl.md).   |
|                                                                                          | [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=13566), [pull request \#4133](https://github.com/FreeCAD/FreeCAD/pull/4133). |
|                                                                                          |                                                                                                                                                   |
|                                                                                          | Na obrazku obiekt *Hole001* został wybrany przez użytkownika, a następnie                                                                         |
|                                                                                          | jego zależności zostały dodane do zaznaczenia poprzez użycie opcji menu kontekstowego.                                                            |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

### Dalsze ulepszenia interfejsu użytkownika 

-   Dodane zostały dwa nowe style nawigacji myszką. Jeden oparty na **[OpenSCAD](Mouse_navigation/pl#OpenSCAD.md)**\', drugi na **[TinkerCAD](Mouse_navigation/pl#TinkerCAD.md)**. [Forum dyskusyjne OpenSCAD](https://forum.freecadweb.org/viewtopic.php?f=8&t=60975), [Forum dyskusyjne TinkerCAD](https://forum.freecadweb.org/viewtopic.php?p=544639#p544376), [commit 1](https://github.com/FreeCAD/FreeCAD/commit/a1c9ab658c), [commit 2](https://github.com/FreeCAD/FreeCAD/commit/ef100d55e9d50), [commit 3](https://github.com/FreeCAD/FreeCAD/commit/549e5b5650).
-   Możliwe jest teraz przesuwanie widoku [Grafu zależności](Std_DependencyGraph/pl.md) za pomocą myszy. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=34791), [pull request \#4638](https://github.com/FreeCAD/FreeCAD/pull/4638).
-   Naprawiono błąd, który powodował, że korzystanie z urządzeń wyposażonych w pióro (np. z tabletu Wacom) było powolne do tego stopnia, że było całkowicie nieużyteczne. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=45046), [pull request \#4687](https://github.com/FreeCAD/FreeCAD/pull/4687).
-   Układ współrzędnych w oknie [widoku 3D](3D_view/pl.md) może zostać zmieniony w preferencjach w sekcji [Wyświetlanie → Widok 3D](Preferences_Editor/pl#Widok_3D.md). [Pull request \#5182](https://github.com/FreeCAD/FreeCAD/pull/5182)
-   Nowe ustawienie w [Preferencje → Ogólne](Preferences_Editor/pl#Og.C3.B3lne.md) pozwala na zastąpienie separatora dziesiętnego klawiatury numerycznej odpowiednim lokalnym separatorem, jeśli są one różne. [Pull request \#3256](https://github.com/FreeCAD/FreeCAD/pull/3256) [Pull request \#5150](https://github.com/FreeCAD/FreeCAD/pull/5150) [Pull request 5203](https://github.com/FreeCAD/FreeCAD/pull/5203).

## Aplikacja::Łączenie i montaż 

## System podstawowy, App, baza i przestrzenie nazw GUI 

+-------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <img alt="" src=images/Object_selection_relnotes_0.20.png  style="width:384px;"> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                           | **Edycja → Kopiuj**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                           | lub **Edycja → Powiel zaznaczony obiekt** dla obiektu z zależnościami, pojawia się nowy przycisk **Użyj wyboru początkowego** w oknie wyboru obiektu. Kliknięcie tego przycisku powoduje skopiowanie/duplikację tylko tych obiektów, które zostały wybrane przed otwarciem okna dialogowego, ignorując zależności i wszelkie działania, które mogły zostać podjęte w czasie, gdy okno było otwarte, takie jak zaznaczanie lub odznaczanie pól wyboru. Efekt jest taki sam, jak gdybyś usunął zaznaczenie wszystkich pól wyboru obok obiektów, których pierwotnie nie zaznaczyłeś i nacisnął przycisk **OK**. Uwaga: Należy zachować szczególną ostrożność podczas kopiowania/duplikowania Stron Rysunku Technicznego. Zaleca się również kopiowanie/duplikowanie wszystkich elementów podrzędnych strony *(Szablony, Widoki, Wymiary, itp.)*. W przeciwnym razie zmiany na jednej ze stron będą miały również wpływ na drugą stronę, np. usunięcie jednego z widoków na jednej stronie spowoduje usunięcie go z drugiej strony. Usunięcie jednej ze stron spowoduje również usunięcie całej zawartości z drugiej strony, jeśli nie zostaną wykonane kopie zawartości. |
+-------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-   Dodano nowy typ dodatku o nazwie [Zestaw preferencji](Preference_Packs/pl.md), pozwalający na dystrybucję i zastosowanie podzbioru pliku preferencji użytkownika *(user.cfg)*. [Dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=17&t=62477), [Pull request \#4787](https://github.com/FreeCAD/FreeCAD/pull/4787).

## Menadżer dodatków 

## Środowisko pracy Architektura 

## Środowisko pracy Rysunek Roboczy 

-   Do panelu zadań wielu poleceń kreślenia dodano pole wyboru **Globalnie**. Zaznaczenie go umożliwia wprowadzenie współrzędnych w globalnym układzie współrzędnych, nawet jeśli [płaszczyzna robocza](Draft_SelectPlane/pl.md) nie jest wyrównana do globalnej płaszczyzny XY.

-   Wprowadzono polecenie <img alt="" src=images/Draft_Hatch.svg  style="width:24px;"> [Kreskowanie](Draft_Hatch/pl.md). Tworzy ono kreskowanie na powierzchniach wybranego obiektu przy użyciu wzorców z plików typu PAT programu AutoCAD.

-   Wprowadzono polecenie <img alt="" src=images/Draft_AddNamedGroup.svg  style="width:24px;"> _ zostało rozszerzone o tę samą funkcjonalność.

-   Zakończono prace nad poleceniem <img alt="" src=images/Draft_SetStyle.svg  style="width:24px;"> [Ustaw styl](Draft_SetStyle/pl.md), trwające jeszcze w wersji 0.19 programu FreeCAD.

-   Dodano opcję edycji podwójnym kliknięciem dla <img alt="" src=images/Draft_Text.svg  style="width:24px;">. [Adnotacji wieloliniowej](Draft_Text/pl.md). Otwiera ona ten sam panel zadań edycji, który jest używany podczas tworzenia tekstu.

Dla calowych <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> [wymiarów](Draft_Dimension/pl.md) architektonicznych {{Value|arch}} została wprowadzona opcja **Nadpisanie jednostki**.

-   Obiekty <img alt="" src=images/Draft_Shape2DView.svg  style="width:24px;"> [Widok 2D kształtu](Draft_Shape2DView/pl.md) mają teraz właściwość **Automatyczna aktualizacja**. Ustawienie jej na wartość {{False/pl}} może być użyteczne, jeśli w dokumencie jest wiele obiektów Shape2DView lub jeśli są one złożone.

-   Jest teraz możliwe odwrócenie _. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=23&t=58643&start=20), [pull request \#4811](https://github.com/FreeCAD/FreeCAD/pull/4811).

### Kolejne ulepszenia dla środowiska Rysunek Roboczy 

-   Naprawiono [Przyciągnij do siatki](Draft_Snap_Grid/pl.md), gdy kursor znajduje się nad ścianą. [Dyskusja na forum](https://forum.freecad.org/viewtopic.php?f=23&t=62274). [Git commit](https://github.com/FreeCAD/FreeCAD/commit/1761eb8ce).

-   Nowe [Adnotacje wieloliniowe](Draft_Text/pl.md) są teraz wyrównane z [płaszczyzną roboczą](Draft_SelectPlane/pl.md), [pull request \#5092](https://github.com/FreeCAD/FreeCAD/pull/5092).

-   Dodano wsparcie dla dwóch konwerterów DWG: _ i [FreeCAD i Import DWG](FreeCAD_and_DWG_Import/pl.md), aby uzyskać więcej informacji.

## Środowisko pracy MES 

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/FEM_Gmsh-MeshSizeFromCurvature_relnotes_0.20.png  style="width:384px;">Efekt funkcji *Rozmiar siatki na podstawie krzywizny*, po lewej: ustawiona na 12, po prawej: wyłączona                 Pojawiła się nowa właściwość generatora siatki [Gmsh](FEM_MeshGmshFromShape/pl.md). Można określić liczbę elementów siatki na $2\pi$ razy promień krzywizny. Domyślnie jest to 12 i aby uzyskać drobniejszą siatkę na małych rogach lub otworach, wartość ta może być zwiększona dla lepszych rezultatów. Ta funkcja wymaga wersji Gmsh 4.8 lub nowszej. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=56401), [pull request \#4596](https://github.com/FreeCAD/FreeCAD/pull/4596)
  <img alt="" src=images/FEM_Gmsh-RecombinationAlgorithm_relnotes_0.20.png  style="width:384px;">Efekt działania algorytmu rekombinacji; po lewej: przy użyciu *Simple*, po prawej: przy użyciu *Simple full-quad*.   FreeCAD pozwala teraz wybrać algorytm, jak również metodę rekombinacji siatki 3D dla generatora siatek [Gmsh](FEM_MeshGmshFromShape/pl.md). Więcej szczegółów na temat rekombinacji elementów siatki można znaleźć na tej stronie [Rekombinacja elementów](FEM_MeshGmshFromShape/pl#Rekombinacja_element.C3.B3w.md). [Pull request \#4706](https://github.com/FreeCAD/FreeCAD/pull/4706)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Dalsze ulepszenia MES 

-   Dodano nowy solver: **Solve → <img src=images/FEM_SolverMystran.svg style="width:16px">. [Solver Mystran](FEM_SolverMystran/pl.md)**. Wiele commitów.
-   Dodano nowe wiązanie: **Model → Geometrical Constraints → <img src=images/FEM_ConstraintSpring.svg style="width:16px"> [Constraint Spring](FEM_ConstraintSpring/pl.md)**. [PR \#4982](https://github.com/FreeCAD/FreeCAD/pull/4982).
-   Kolejność elementów w generatorze siatek [Gmsh](FEM_MeshGmshFromShape/pl.md) może być zmieniona poprzez okno dialogowe siatki [PR \#4660](https://github.com/FreeCAD/FreeCAD/pull/4660).
-   Karty materiałowe mogą teraz zawierać wartości przewodności elektrycznej [PR \#4647](https://github.com/FreeCAD/FreeCAD/pull/4647).
-   Dodano karty materiałowe dla Azotu i Argonu [PR \#4649](https://github.com/FreeCAD/FreeCAD/pull/4649)
-   Dodano wsparcie dla [Gmsh](FEM_MeshGmshFromShape/pl.md) algorytmów siatkowych \"HXT\" *(3D)* i \"Packing Parallelograms\" *(2D)* [PR \#4654](https://github.com/FreeCAD/FreeCAD/pull/4654).
-   Umożliwiono ustawienie dla [Gmsh](FEM_MeshGmshFromShape#Properties/pl.md) właściwości **Optymalizacja wysokiego poziomu** określonego algorytmu [PR \#4705](https://github.com/FreeCAD/FreeCAD/pull/4705).
-   Nieliniowe materiały stałe z prostym utwardzaniem mogą mieć teraz dowolną liczbę granic plastyczności. [PR \#5024](https://github.com/FreeCAD/FreeCAD/pull/5024)

## Import

## Postępowanie z materiałami 

## Środowisko pracy Siatka 

### Ulepszona obsługa elementów NASTRAN GRID 

Narzędzie do importu siatki obsługuje teraz element \"GRID\*\" o wysokiej precyzji. Element \"GRID\" o standardowej precyzji został również ulepszony i obsługuje teraz zarówno dane numeryczne z ograniczeniem spacji, jak i dane o stałej szerokości pola, zgodnie z dokumentacją formatu NASTRAN95.

### Planowane ulepszenia 

Naprawiono fałszywe negatywy podczas testów autoprzecinania, gdy ściany są współpłaszczyznowe: [pull request \#5002](https://github.com/FreeCAD/FreeCAD/pull/5002).

## Środowisko pracy OpenSCAD 

Ulepszono współdziałanie z OpenSCAD, dodając obsługę kilku operacji, których brakowało we wcześniejszych wersjach (wyciągnięcia liniowe z obrotem, wyciągnięcia obrotowe). Kilka operacji zostało zmodyfikowanych, aby zapewnić ulepszone odpowiedniki obiektów FreeCAD, szczególnie w przypadku skręconych wyciągnięć. Zmodyfikowano generowanie powierzchni z danych dyskretnych, aby uzyskać wyniki bardziej podobne do OpenSCAD, niż powierzchnie wielowypustowe.

**Dodaj element OpenSCAD** - posiada teraz dodatkowe opcje

Wczytaj - wczytaj plik w formacie scad
Zapisz - zapisz plik w formacie scad
Odśwież - aktualizacja widoku FreeCAD
Wyczyść - wyczyść tekst

Jest tam również pole tekstowe do zgłaszania błędów w OpenSCAD.

## Środowisko pracy Część 

### Planowane ulepszenia środowiska Część 

-   Okno dialogowe do edycji [walców](Part_Cylinder/pl.md) pozwala teraz na określenie kąta względem wektora normalnego wybranej płaszczyzny mocowania. W ten sposób można tworzyć przechylone walce. [Pull request \#4708](https://github.com/FreeCAD/FreeCAD/pull/4708)

## Środowisko pracy Projekt Części 

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/PD_Pocket-direction_relnotes_0.20.gif  style="width:384px;"> Wykonywanie kieszeni wzdłuż różnych kierunków. Kliknij na obrazek, aby wyświetlić animację.                                            Teraz można określić kierunek wycięcia kieszeni. [Pull request \#5164](https://github.com/FreeCAD/FreeCAD/pull/5164)
  <img alt="" src=images/PD_Pad-Length-along-reference_relnotes_0.20.gif  style="width:384px;">Wyciągnięcie wzdłuż krawędzi modelu.Kliknij na obrazek, aby wyświetlić animację.                                    Istnieje nowa opcja wyciągania wzdłuż kierunku krawędzi w modelu 3D. [pull request \#4685](https://github.com/FreeCAD/FreeCAD/pull/4685)
  <img alt="" src=images/PD_Pad-Length-alog-direction_relnotes_0.20.gif  style="width:384px;">Efekt działania nowej opcji *Długość wzdłuż wektora normalnego szkicu*.Kliknij na obrazek, aby wyświetlić animację.   Pojawiła się nowa opcja dopasowywania określonej długości wzdłuż kierunku. Długość jest mierzona wzdłuż wektora normalnego szkicu lub wzdłuż kierunku niestandardowego. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=17&t=50466), [pull request \#3893](https://github.com/FreeCAD/FreeCAD/pull/3893)
  <img alt="" src=images/PartDesign_Cylinder_direction.png  style="width:384px;">                                                                                                                                                                                Okno dialogowe do edycji [walca](PartDesign_AdditiveCylinder/pl.md) *(addytywny i subtraktywny)* pozwala teraz na określenie kąta względem wektora normalnego wybranej płaszczyzny mocowania. W ten sposób można tworzyć skośne walce. [pull request \#4708](https://github.com/FreeCAD/FreeCAD/pull/4708)
  <img alt="" src=images/PartDesign_Chamfer_Face_Selection_relnotes_0.20.png  style="width:384px;">                                                                                                                                            Jeśli w narzędziu [Fazka](PartDesign_Chamfer/pl.md) określono odległość i kąt oraz wybrano powierzchnie, odległość zostanie zastosowana wzdłuż wybranych powierzchni. Analogicznie, jeśli podano dwie odległości, to wzdłuż wybranej powierzchni zostanie zastosowana wielkość 1. Zachowanie to można zamienić na inną powierzchnię za pomocą przycisku Przerzuć kierunek. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=19&t=62084), [pull request \#5039](https://github.com/FreeCAD/FreeCAD/pull/5039)
  <img alt="" src=images/PartDesign_Loft_Vertex_relnotes_0.20.png  style="width:384px;">                                                                                                                                                                  Możliwe jest teraz tworzenie [Wyciągnięcie przez profile](PartDesign_AdditiveLoft/pl.md), [Subtraktywne wyciągnięcie przez profile](PartDesign_SubtractiveLoft/pl.md), [Wyciągnięcie po ścieżce](PartDesign_AdditivePipe/pl.md) lub [Subtraktywne wyciągnięcie po ścieżce](PartDesign_SubtractivePipe/pl.md) w kierunku lub z [wierzchołka](Glossary/pl#V.md) szkicu lub bryły. Pozwala to na przykład na tworzenie piramid. [Pull request \#5170](https://github.com/FreeCAD/FreeCAD/pull/5170) 
*(dla profili)*, [Pull request \#5193](https://github.com/FreeCAD/FreeCAD/pull/5193) *(dla ścieżki)*
  <img alt="" src=images/PartDesign_Helix_Growth_relnotes_0.20.png  style="width:384px;">                                                                                                                                                                Funkcja [Helisa](PartDesign_AdditiveHelix/pl.md) posiada nowy tryb **Wysokość - Obroty - Przyrost** do tworzenia płaskich spiral. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=19&t=56378) [Pull request \#4590](https://github.com/FreeCAD/FreeCAD/pull/4590)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Planowane ulepszenia środowiska Projekt Części 

-   Funkcja [Helisa](PartDesign_AdditiveHelix/pl.md) można teraz również użyć normalnej szkicu jako osi [pull request \#5199](https://github.com/FreeCAD/FreeCAD/pull/5199),
-   Funkcja [Koło łańcuchowe](PartDesign_Sprocket/pl.md) może teraz tworzyć również koła łańcuchowe zgodne z normami ISO [wątek na forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=44525#p478369) [pull request \#4478](https://github.com/FreeCAD/FreeCAD/pull/4478),
-   Funkcje [Wyciągnięcie po profilach](PartDesign_AdditiveLoft.md) oraz [Wyciągnięcie po ścieżce](PartDesign_AdditivePipe.md) pozwalają teraz na użycie powierzchni bryły dla przekroju.. [Pull request \#5155](https://github.com/FreeCAD/FreeCAD/pull/5155),
-   Możliwe jest teraz wybranie kilku powierzchni przed wywołaniem okna dialogowego [wyciągnięcia](PartDesign_Pad/pl.md) lub [kieszeni](PartDesign_Pocket/pl.md). W tym przypadku pierwsza wybrana powierzchnia zostanie użyta do określenia domyślnego kierunku wyciągnięcia /kieszeni. [commit d34a5616](https://github.com/FreeCAD/FreeCAD/commit/d34a5616a2b38c96ad05f9a0763ba7504dfb814d).

## Środowisko pracy Path 

## Środowisko pracy Render 

## Środowisko pracy Szkicownik 

  --------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/SketcherSplitExample2_relnotes_0.20.png )                                                  Nowa funkcja do !_ istniejących linii lub łuków. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=9&t=55412) [pull request \#4420](https://github.com/FreeCAD/FreeCAD/pull/4420)
  <img alt="" src=images/SketcherCreateRoundedRectangleExample_relnotes_0.20.png )                  Nowe narzędzie !_ do tworzenia prostokątów z zaokrąglonymi rogami. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=17&t=59210) [Main pull request \#4835](https://github.com/FreeCAD/FreeCAD/pull/4835)
  <img alt="" src=images/SketcherCreateCenteredRectangleExample_relnotes_0.20.png  style="width:384px;">   Nowe narzędzie <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:24px;">. [Centered rectangle](Sketcher_CreateRectangle_Center/pl.md) do definiowania prostokątów poprzez punkt środkowy. [Main commit](https://github.com/FreeCAD/FreeCAD/commit/8b4acf11c2caf53cc1cb8dccd8bb6de8516f4492)
  <img alt="" src=images/Radiam_anim_relnotes_0.20.gif  style="width:384px;">                                                         Nowa funkcja <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:24px;"> [Radiam](Sketcher_ConstrainRadiam/pl.md) do automatycznego przypisywania wagi do bieguna B-splajnu, średnicy do pełnego okręgu lub promienia do łuku. Obsługa wielokrotnego wyboru jako narzędzia średnicy / promienia. [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=57584&start=20#p509485) [Main pull request \#4855](https://github.com/FreeCAD/FreeCAD/pull/4855)
  <img alt="" src=images/SketcherRemoveAxesAlignmentResult_relnotes_0.20.png )                          Nowe narzędzie !_ do usuwania wyrównania osi przy jednoczesnej próbie zachowania relacji wiązań zaznaczenia. [Main commit](https://github.com/FreeCAD/FreeCAD/commit/3c593a33cedc3e6a42928d9087f8a160852cc685)
  Funkcja ![](images/SketcherSnapSlot_relnotes_0.20.gif )                                                [Utwórz wpust](Sketcher_CreateSlot/pl.md) może być związana poziomo lub pionowo poprzez ręczne przytrzymanie go za pomocą klawisza **Ctrl** lub poprzez użycie opcji **Wiązania automatyczne** Szkicownika. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/5200)
  --------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Planowane ulepszenia środowiska Szkicownik 

-   Zaktualizowana obsługa przycinania [Pull Request](https://github.com/FreeCAD/FreeCAD/pull/4330) [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=10&t=54441) \<\-- Potrzebuje prezentacji ekranów
-   Zachowanie funkcji <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:24px;"> [rowek](Sketcher_CreateSlot/pl.md) uległo zmianie. Rowki mogą być teraz tworzone poprzez zdefiniowanie środka obu półokręgów. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4843) [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=17&t=59243&p=508658#p508658)
-   Automatyzacja widoczności pozwala na otwarcie Szkicownika w [trybie przekroju](Sketcher_ViewSection/pl.md) po wejściu do trybu edycji. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4742) [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=57056)
-   Automatyzacja widoczności pozwala na wymuszenie pracy ujęcia widoku w [trybie ortogonalnym](Std_OrthographicCamera/pl.md) przy wejściu w tryb edycji. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4778) [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=44747)
-   Opcja wyświetlania nazwy wiązania wymiarowego i użycia dla niej niestandardowego formatu. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4966) [Dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?t=61153)
-   Podczas szkicowania [3-punktowego łuku](Sketcher_Create3PointArc/pl.md) z włączoną opcją automatycznego wiązania, [wiązanie stycznej](Sketcher_ConstrainTangent/pl.md) jest proponowane dla wszystkich 3 punktów podczas najechania na linię/krzywą. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4945) [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=60596&p=520217#p520209).
-   Wiązania promienia/średnicy są wyświetlane przy użyciu obrotu kątowego, aby ułatwić wizualizację. Kąt i opcjonalna losowość są ustawiane przez użytkownika za pomocą parametrów udokumentowanych w [Fine-tuning](Fine-tuning/pl.md) [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4934) [Dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=60370).
-   Możliwe jest teraz ustalenie kąta kierunku podczas używania narzędzia [Szyk prostokątny](Sketcher_RectangularArray/pl.md) [commit](https://github.com/FreeCAD/FreeCAD/commit/c9eaa2393d33) [Dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?p=535691#p535691)
-   Możliwe jest teraz ustalenie kąta kierunku podczas używania narzędzi [Klonuj](Sketcher_Clone/pl.md), [Kopiuj](Sketcher_Copy/pl.md) i [Przesuń](Sketcher_Move/pl.md) [commit](https://github.com/FreeCAD/FreeCAD/commit/6e4a09f569cf) [Dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=62799)

### Poprawki błędów Szkicownika 

-   Naprawiono opcję „Odniesienie" niedziałającą dla promienia/średnicy w czasie tworzenia [Pull request \#4744 dla promienia](https://github.com/FreeCAD/FreeCAD/pull/4744) [4832 Pull request \#4832 dla średnicy](https://github.com/FreeCAD/FreeCAD/pull/) [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=57584),
-   [Kalka techniczna](Sketcher_CarbonCopy/pl.md) poprawiono wykrywanie równoległości / wyrównania, dodając tolerancję na błędy obliczeń zmiennoprzecinkowych [Pull request](https://github.com/FreeCAD/FreeCAD/pull/5197) [dyskusja na forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=63956)

## Środowisko pracy Arkusz Kalkulacyjny 

  -------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/Spreadsheet-Preferences-Spreadsheet_relnotes_0.20.png )   The workbench now has !_. Są one wykorzystywane przez polecenia <img alt="" src=images/Spreadsheet_Import.svg  style="width:16px;"> _. [Pull request \#5073](https://github.com/FreeCAD/FreeCAD/pull/5073)
  -------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   W menu kontekstowym wiersza / kolumny można teraz wybrać, w jakich pozycjach będą wstawiane nowe wiersze / kolumny. [pull request \#4704](https://github.com/FreeCAD/FreeCAD/pull/4704).

### Planowane ulepszenia arkusza kalkulacyjnego 

-   Import XLSX *(używany przez [Std Import](Std_Import/pl.md))*: Dodano wsparcie dla funkcji floor i ceil. [Pull request \#5015](https://github.com/FreeCAD/FreeCAD/pull/5015).

## Środowisko pracy Start 

## Środowisko pracy Surface 

## Środowisko pracy Rysunek Techniczny 

+-------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <img alt="" src=images/TechDraw_ExtensionExample_relnotes_0.20.png  style="width:400px;"> | Kilka nowych narzędzi, tak zwanych [rozszerzeń](TechDraw_Workbench/pl#Pakiet_rozszerze.C5.84.md), jest już dostępnych. Oferują one nowe, funkcje geometrii pomocniczych do ulepszania rysunków:                  |
|                                                                                                             |                                                                                                                                                                                                                          |
|                                                                                                             | -   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:24px;"> [Oś otworu](TechDraw_ExtensionCircleCenterLines/pl.md)                                                |
|                                                                                                             | -   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:24px;"> [Geometria pomocnicza dla otworu gwintowanego, widok z boku](TechDraw_ExtensionThreadHoleSide/pl.md)        |
|                                                                                                             | -   <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width:24px;"> [Geometria pomocnicza dla gwintu śruby, widok z boku](TechDraw_ExtensionThreadBoltSide/pl.md)               |
|                                                                                                             | -   <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width:24px;"> [Geometria pomocnicza dla otworu gwintowanego, widok od dołu](TechDraw_ExtensionThreadHoleBottom/pl.md) |
|                                                                                                             | -   <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width:24px;"> [Geometria pomocnicza dla śruby, widok od dołu](TechDraw_ExtensionThreadBoltBottom/pl.md)               |
+-------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Kolejne ulepszenia dla środowiska Rysunek Techniczny 

## Środowisko pracy Web 

## Zewnętrzne Środowiska pracy 


**Uwaga:**

Są to nowe stanowiska pracy utworzone w tym cyklu rozwojowym lub starsze stanowiska pracy, które otrzymały aktualizacje. Zobacz [zewnętrzne stanowiska pracy](External_workbenches.md), aby uzyskać pełną listę dodatkowych Środowisk pracy, które mogą być zainstalowane w programie FreeCAD. Jeśli chcesz aby Twoje Środowisko pracy zostało dodane, dołącz do forum i zaprezentuj swój kod.

### Narzędzia do druku 3D 

### Środowisko pracy A2plus 

### Środowisko pracy Złożenie 3 

## Środowisko pracy Złożenie 4 

### Tekstury architektoniczne 

### BOLTSFC

### Środowisko pracy CurvedShapes 

### Środowisko pracy Dodo *(wcześniej Flamingo)* 

### Środowisko pracy Elementy Złączne 

### FCGear

Środowisko pracy [FCGear](FCGear_Workbench/pl.md) otrzymało kilka ulepszeń

-   Dla kół zębatych ewolwentowych, średnica zewnętrzna *(aka wierzchołek)* i średnica nasady są wyświetlane jako właściwości *([szczegóły](https://github.com/looooo/freecad.gears/pull/69))*.
-   Obiekty kół zębatych maja teraz [Edycję mocowania](Part_EditAttachment/pl.md) *([szczegóły](https://github.com/looooo/freecad.gears/pull/72))*.
-   Obiekty kół zębatych mogą być teraz używane jako cechy addytywne w Zawartości środowiska Projekt Części *([szczegóły](https://github.com/looooo/freecad.gears/pull/74))*.
-   Tworzenie obiektów przekładni pojawia się teraz w stosie cofania *([szczegóły](https://github.com/looooo/freecad.gears/pull/83))*.

### Środowisko pracy MeshRemodel 

### Środowisko pracy MOOC 

### NodeEditor *(PyFlow)* 

### Trails PyTrails, Turns oraz pivy\_trackers i Geomatics 

_ _ _

---
[documentation index](../README.md) > [News](Category_News.md) > Release notes 0.20/pl

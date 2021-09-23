# Feature list/pl
 

Jest to obszerną, ale nie kompletna lista funkcji, realizowanych przez program FreeCAD. Jeśli chcesz zobaczyć przyszłe wydarzenia, zobacz [\|Mapa rozwoju](Development_roadmap.md), aby szybko zorientować się, co będzie dalej. Ponadto, miłym miejscem jest galeria [Zrzutów ekranu](Screenshots.md).


{{TOCright}}

## Informacje o wydaniu 

-   [Wydanie 0.11](Release_notes_0.11.md) - Marzec 2011
-   [Wydanie 0.12](Release_notes_0.12.md) - Grudzień 2011
-   [Wydanie 0.13](Release_notes_0.13.md) - January 2013
-   [Wydanie 0.14](Release_notes_0.14/pl.md) - Marzec 2014
-   [Wydanie 0.15](Release_notes_0.15/pl.md) - Marzec 2015
-   [Wydanie 0.16](Release_notes_0.16.md) - Kwiecień 2016
-   [Wydanie 0.17](Release_notes_0.17/pl.md) - Kwiecień 2018
-   [Wydanie 0.18](Release_notes_0.18/pl.md) - Marzec 2019
-   [Wydanie 0.19](Release_notes_0.19/pl.md) - Marzec 2021
-   [Wydanie 0.20](Release_notes_0.20.md) -

## Główne cechy 

-   ![](images/Feature1.jpg ) Kompletne **jądro geometrii** bazujące na [Open CASCADE Technology](http://en.wikipedia.org/wiki/Open_CASCADE) umożliwiający kompleksowe operacje 3D na złożonych typach kształtów, z natywnym wsparciem dla koncepcji takich jak [Boundary Representation](https://en.wikipedia.org/wiki/Boundary_representation) *(BREP)*, [Non-uniform rational basis spline](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline) *(NURBS)* krzywe i powierzchnie, szeroki zakres kształtów geometrycznych, operacje boolean [fillets](https://en.wikipedia.org/wiki/Fillet_(mechanics)), oraz wbudowana obsługa formatów [STEP](https://en.wikipedia.org/wiki/ISO_10303) i [IGES](https://en.wikipedia.org/wiki/IGES).
-   ![](images/Feature3.jpg ) Pełny **model parametryczny**. Wszystkie obiekty FreeCAD są naturalnie parametryczne, co oznacza, że ich kształt może być oparty na [właściwości](Property/pl.md) lub nawet zależny od innych obiektów. Wszystkie zmiany są przeliczane na żądanie i rejestrowane przez stos cofnij/przywróć. Nowe typy obiektów mogą być dodawane w prosty sposób, a nawet mogą być [w pełni oprogramowane w środowisku Python](Scripted_objects/pl.md).
-   ![](images/Feature4.jpg ) Architektura modułowa\", która umożliwia dodanie funkcjonalności rozszerzeń wtyczek *(modułów)* do podstawowej aplikacji. Rozszerzenie może być tak złożone, jak cała nowa aplikacja zaprogramowana w C++ lub tak proste, jak [skrypt Python](Power_users_hub/pl.md) lub samodzielnie nagrana [makrodefinicja](Macros/pl.md). Masz pełny dostęp do prawie każdej części FreeCAD z wbudowanego interpretera **Python**, makr lub zewnętrznych skryptów, bez względu na to, czy jest to [tworzenie i transformacja geometrii](Topological_data_scripting/pl.md), dwu- lub trójwymiarowa reprezentacja tej geometrii([scenegraph](scenegraph.md)) a nawet [interfejs FreeCAD](PySide/pl.md) 
-   ![](images/Feature5.jpg ) Import i eksport do **standardowych formatów**, takich jak [STEP](http://en.wikipedia.org/wiki/ISO_10303), [IGES](http://en.wikipedia.org/wiki/IGES), [OBJ](http://en.wikipedia.org/wiki/Obj), [STL](http://en.wikipedia.org/wiki/STL_%28file_format%29), [DXF](http://en.wikipedia.org/wiki/Dxf), [SVG](http://en.wikipedia.org/wiki/Svg), [DAE](http://en.wikipedia.org/wiki/COLLADA), [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) lub [OFF](http://people.sc.fsu.edu/~jburkardt/data/off/off.html), [NASTRAN](http://en.wikipedia.org/wiki/NASTRAN), [VRML](http://en.wikipedia.org/wiki/VRML) w dodatku do macierzystego formatu plików FreeCAD {{FileName|[FCStd](File_Format_FCStd.md)}}. Poziom kompatybilności pomiędzy FreeCAD i danym formatem pliku może się różnić, ponieważ zależy to od modułu, który ten format wdraża.
-   ![](images/Feature7.jpg ) [Szkicownik](Sketcher_Workbench/pl.md) ze zintegrowanym mechanizmem wiązań, umożliwiającym szkicowanie kształtów 2D o związanej geometrii. Zbudowane za pomocą programu Sketcher związane kształty 2D mogą być następnie wykorzystane jako podstawa do budowania innych obiektów w całym FreeCAD.
-   ![](images/Feature9.jpg ) Środowisko pracy [Symulacja Robota](Robot_Workbench/pl.md), które pozwala na badanie ruchów robotów w środowisku graficznym.
-   ![](images/Feature8.jpg ) Środowisko pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md) z opcjami widoków szczegółowych, przekrojów, wymiarowania i innych, pozwalającymi na generowanie widoków 2D istniejących modeli 3D. Moduł następnie tworzy gotowe do eksportu pliki SVG lub PDF. Jest też starszy moduł [Kreślenie](Drawing_Workbench/pl.md) z nielicznymi poleceniami Gui, lecz posiada potężną funkcjonalność Pythona.
-   ![](images/Feature-raytracing.jpg ) Środowisko pracy [Rendering](Raytracing_Workbench/pl.md) który może eksportować obiekty 3D do renderowania z zewnętrznymi śilnikami. Obecnie obsługuje tylko moduły [povray](http://en.wikipedia.org/wiki/POV-Ray) i [LuxRender](http://en.wikipedia.org/wiki/LuxRender), ale w przyszłości ma zostać rozszerzony o kolejne programy renderujące.
-   ![](images/Feature-arch.jpg ) Środowisko pracy [Architektura](Arch_Workbench/pl.md) umożliwia modelowanie [Building Information Modeling](http://en.wikipedia.org/wiki/Building_Information_Modeling) przepływ pracy *(BIM)*, z kompatybilnością [Industry Foundation Classes](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) *(IFC)*.
-   ![](images/Feature-CAM.jpg ) Środowisko pracy [Path](Path_Workbench/pl.md) dedykowane do obróbki mechanicznej dla [Computer Aided Manufacturing](https://en.wikipedia.org/wiki/Computer-aided_manufacturing) *(CAM)*. Korzystając z modułu Ścieżka, można tworzyć, wyświetlać i modyfikować [G-code](http://en.wikipedia.org/wiki/G-code) używany do sterowania maszyną docelową.
-   ![](images/Feature_spreadsheet.png ) Środowisko pracy [Arkusz Kalkulacyjny](Spreadsheet_Workbench/pl.md) oraz [parser wyrażeń](Expressions/pl.md), które można wykorzystać do obsługi modeli danych opartych na formułach i organizowania danych modelu w centralnej lokalizacji.

## Cechy ogólne 

-   **Wieloplatformowość**. FreeCAD działa i zachowuje się dokładnie tak samo na platformach takich jak Linux, MacOS, Windows i innych.

-   **aplikacja z pełnym interfejsem graficznym**. FreeCAD posiada kompletny graficzny interfejs użytkownika oparty na strukturze [Qt](https://www.qt.io/), z przeglądarką 3D opartą na [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor); umożliwiający szybkie renderowanie scen 3D i bardzo przystępną wizualizację graficzną ujęć.

-   **FreeCAD działa także jako aplikacja uruchamiana z linii poleceń**, W trybie wiersza poleceń, FreeCAD działa bez interfejsu GUI, ale z wszystkimi narzędziami geometrii. W tym trybie zajmuje stosunkowo mało miejsca w pamięci i może być używany, na przykład, jako serwer do produkcji treści dla innych aplikacji.

-   **FreeCAD może być zaimportowany jako [moduł Python](Embedding_FreeCAD/pl.md)**, do innych aplikacji potrafiących wykonywać skrypty Python. Podobnie jak w trybie konsolowym, część interfejsu jest niedostępna, ale wszystkie narzędzia geometrii są dostępne.

-   **Koncepcja Środowisk pracy**: W interfejsie FreeCAD narzędzia są pogrupowane według [Środowisk pracy](workbenches.md). Pozwala to wyświetlać tylko narzędzia używane do wykonania określonego zadania, utrzymując przestrzeń pracy bez zbędnych elementów i zapewniając odpowiednią reakcję, oraz umożliwiając szybkie ładowanie aplikacji.

-   *plugin / moduł frameworka do późniejszego ładowania funkcji / typów danych*. FreeCAD jest podzielony na główną aplikację z modułami, które są ładowane tylko wtedy, gdy są potrzebne. Prawie wszystkie narzędzia i typy geometrii są przechowywane w modułach. Moduły zachowują się jak wtyczki; oprócz selektywnego uruchamiania, można je dodawać lub usuwać z istniejącej instalacji FreeCAD.

-   **parametryczne obiekty dokumentów towarzyszących**. Wszystkie obiekty w dokumencie FreeCAD mogą być zdefiniowane przez parametry. Parametry te mogą być modyfikowane i ponownie obliczane w dowolnym momencie. Ponieważ relacje między obiektami są zachowane, modyfikacja jednego obiektu będzie automatycznie rozprzestrzeniać się do dowolnych obiektów zależnych.

-   **Tworzenie parametrycznych prymitywów**. Obiekty pierwotne, takie jak pole, kula, cylinder itp. mogą być tworzone poprzez określenie ich wiązań geometrycznych.

-   **operacje graficznej modyfikacji**. FreeCAD może wykonywać przekształcenia, obracanie, skalowanie, lustrzane odbicie, przesunięcie *(czy to banalne, czy jak opisano w [Jung/Shin/Choi](https://www.researchgate.net/publication/240754626_Self-intersection_Removal_in_Triangular_Mesh_Offsetting))* lub konwersję kształtu, w dowolnej płaszczyźnie przestrzeni 3D.

-   **[Konstrukcyjna geometria bryłowa](Constructive_solid_geometry.md) (operacje logiczne)**. FreeCAD może wykonywać operacje konstrukcyjne z geometrią bryłową *(połączenie, różnica, przecięcie)*.

-   **Graficzne tworzenie geometrii płaskiej**. Linie, zamknięte przestrzenie, prostokąty, krzywe złożone, łuki okrągłe lub eliptyczne mogą być tworzone graficznie w dowolnej płaszczyźnie przestrzeni 3D.

-   Modelowanie wytłoczeń prostych lub wytłoczeń obrotowych **wyciągnięć**, **przekrojów** i **zaokrągleń**.

-   **komponenty kształtu**, takie jak *wierzchołki*\', **krawędzie**, **kształty zamknięte** i **płaszczyzny**.

-   **Testowanie i naprawa**. FreeCAD posiada narzędzia do testowania siatek *(test bryłowy, test bez użycia podwójnych rozgałęzień, test samoczynnego przecięcia)* oraz do naprawy siatek *(wypełnienie otworów, jednolita orientacja)*.

-   **Adnotacje**. FreeCAD może wstawiać dodatkowe dopisy do tekstu lub wymiarów.

-   **Framework Cofnij/Ponów**. Wszystkie operacje przeprowadzone w programie FreeCAD można cofnąć/ponownie wykonać, z dostępem użytkownika do stosu cofnięcia. Można cofnąć wiele kroków jednocześnie.

-   **Zorientowany na transakcje**. Stos undo/redo przechowuje operacje wykonywane na dokumentach, a nie pojedyncze działania, pozwalając każdemu narzędziu dokładnie określić, co należy cofnąć lub przerobić.

-   **Wbudowany framework [pisania skryptów](Scripting/pl.md)**. FreeCAD posiada wbudowany interpreter [Python](http://www.python.org/), z API, które obejmuje prawie każdą część aplikacji, interfejs, geometrię i reprezentację tej geometrii w przeglądarce 3D. Interpreter może uruchamiać złożone skrypty, jak również pojedyncze polecenia. Całe moduły mogą być kompletnie zaprogramowane w Pythonie.

-   **Wbudowana konsola Pythona**. Interpretator Pythona zawiera konsolę z podświetlaniem składni, funkcję automatycznego uzupełniania i przeglądarkę klas. Polecenia Pythona mogą być wydawane bezpośrednio w FreeCAD i natychmiast zwracać wyniki, pozwalając autorom skryptów na testowanie funkcjonalności w locie, badanie zawartości modułów FreeCAD i łatwe zapoznanie się z wewnętrznymi elementami FreeCAD.

-   **Odzwierciedlenie działań użytkownika**. Wszystko co użytkownik robi w interfejsie FreeCAD uruchamia kod Pythona, który może być prezentoway w konsoli i zapisywany w makrach.

-   **Pełny zapis i edycja [makr](Macros/pl.md)**. Polecenia Pythona wydane podczas manipulowania interfejsem przez użytkownika mogą być nagrywane, ewentualnie edytowane i zapisywane w celu późniejszego odtworzenia.

-   **złożony *(oparty na ZIP)* format zapisu dokumentów**. Dokumenty FreeCAD są zapisywane z rozszerzeniem {{FileName|.[FCStd](File_Format_FCStd.md)}}. Dokument może zawierać wiele różnych typów informacji, takich jak geometria, skrypty lub miniaturowe ikony. Plik {{FileName|.FCStd}} jest sam w sobie kontenerem zip; zapisany plik FreeCAD jest już skompresowany.

-   **w pełni konfigurowalny/skryptowalny graficzny interfejs użytkownika**. Interfejs FreeCAD oparty na [Qt](https://www.qt.io/) jest w pełni dostępny poprzez interpreter Pythona. Poza prostymi funkcjami, które FreeCAD sam dostarcza do Środowisk pracy, dostępny jest cały szkielet Qt. Użytkownik może wykonywać dowolne operacje na interfejsie graficznym, takie jak tworzenie, dodawanie, dokowanie, modyfikowanie lub usuwanie widżetów i pasków narzędzi.

-   **thumbnailer**. *(obecnie tylko systemy Linux)* Ikony dokumentów FreeCAD pokazują zawartość pliku w większości aplikacji do zarządzania plikami, takich jak Nautilus Gnome.

-   **modułowy instalator MSI**. Instalator FreeCAD umożliwia elastyczną instalację w systemach Windows. Utrzymywane są również pakiety dla systemów Ubuntu.

## W rozwoju 

-   ![](images/Feature-assembly.jpg ) Środowisko pracy [Złożenie](Assembly_project/pl.md) które umożliwia pracę z wieloma projektami, wieloma kształtami, wieloma dokumentami, wieloma plikami, wieloma powiązaniami\... Moduł ten jest obecnie w stanie planowania.

## Dodatkowe Środowiska pracy 

Power użytkownicy stworzyli różne niestandardowe [zewnętrzne środowiska pracy](External_workbenches/pl.md).







[Category:User Documentation](Category:User_Documentation.md)

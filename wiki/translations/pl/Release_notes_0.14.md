# Release notes 0.14/pl
FreeCAD **0.14** został wydany 1 lipca 2014 roku. Stanowi podsumowanie najciekawszych rozwiązań. Pełna lista zmian znajduje się w [dzienniku zmian Mantis](http://www.freecadweb.org/tracker/changelog_page.php). Starsze wersje można znaleźć na stronie: [0.13](Release_notes_0.13.md) - [0.12](Release_notes_0.12.md) - [0.11](Release_notes_0.11.md)

<img alt="" src=images/Freecad_jeep.png  style="width:1024px;">


<center>

Model Jeepa wykonany przez Psicofila


</center>

## Informacje ogólne 

### Migracja serwisu 

Przenieśliśmy w końcu wszystkie nasze usługi sieciowe z [SourceForge](http://www.sourceforge.net) na naszą [własną domenę](http://www.freecadweb.org). Nowa strona domowa FreeCAD może być znaleziona na <http://www.freecadweb.org>, Wiki jest teraz na <http://www.freecadweb.org/wiki>, tracker błędów i nowych funkcji na <http://www.freecadweb.org/tracker>, oraz forum na <http://forum.freecadweb.org>. Jeśli masz konto w jednej z usług gdy byliśmy na SourceForge, możesz zatrzymać istniejące konto użytkownika podążając według [tych wskazówek](http://forum.freecadweb.org/viewtopic.php?f=8&t=4942).

Jedyną częścią FreeCAD pozostającą na SourceForge jest główne repozytorium gita, znajdujące się pod tym samym adresem: <http://sourceforge.net/p/free-cad/code/ci/master/tree/> ale będące automatycznym mirrorem kodu ustawionym na githubie, na <http://github.com/FreeCAD/FreeCAD_sf_master>

Jeśli nie spotkałeś jeszcze niesamowitej społeczności FreeCAD, odpłać nam wizytą na forum i bądź zachwycony jej zdolnościami, energią i przydatnością.

### Przejście na pyside, FreeCAD jest teraz całkowicie LGPL 

Z uwagi na wiele komplikacji spowodowanych podwójnym licencjonowaniem programu FreeCAD *(LGPL & GPL)*, i niektórych jego komponentów *(głównie jądra OpenCasCade)* będących niekompatybilnymi z kodem GPL, zdecydowaliśmy przejść ze wszelkich pozostałości kodu GPL we FreeCAD na LGPL. W wyniku tej operacji, [PyQt](http://en.wikipedia.org/wiki/PyQt) nie jest już wykorzystywane i zostało zastąpione przez [PySide](http://en.wikipedia.org/wiki/PySide). Nie ma to większych konsekwencji dla piszących skrypty, PyQt może być ciągle używane wewnątrz programu FreeCAD.

Po ukończeniu przejścia na LGPL, również OpenCasCade [zmieniło licencję na LGPL](http://www.opencascade.org/getocc/license/) - to rozwiązało nasze wszystkie problemy z licencjami. Teraz mamy znacznie bardziej przejrzysty i zunifikowany model licencjonowania, co powinno spełnić wymagania najbardziej restrykcyjnych dystrybucji Linuksa.

### Wtyczki i projekty poboczne: Biblioteka części, BOLTS, importer Eagle 

W ostatnim roku pojawiło się kilka interesujących pobocznych projektów wokół FreeCAD. [Biblioteka części](http://github.com/yorikvanhavre/FreeCAD-library) została utworzona przez społeczność i powoli rośnie, składając się z części wielokrotnego użytku do dodaniu do twoich modeli FreeCAD. Może ona zostać uruchomiona i używana wewnątrz FreeCAD przy użyciu makra.

Innym podobnym, ale bardziej ambitnym projektem jest [BOLTS](http://bolts-library.org/), które również jest biblioteką części, ale zbudowanych z parametrycznych skryptów umożliwiających budowę szerokiego spektrum parametrycznych części. BOLTS, pomimo, że niezależne od aplikacji, może również zostać uruchomione we FreeCAD przez wykonanie makra. Poniższy obraz pokazuje BOLTS działające wewnątrz FreeCAD.

<img alt="" src=images/Freecad-bearing.png  style="width:1024px;">

Kolejnym interesującym zewnętrznym projektem jest [importer EAGLE](http://sourceforge.net/projects/eaglepcb2freecad/), który pozwala importować do FreeCAD projekty płytek PCB wykonanych w kilku różnych aplikacjach.

### Eksport WebGL 

Z poziomu FreeCAD-a, możesz teraz wyeksportować swoją scenę jako plik html z [WebGL.](http://en.wikipedia.org/wiki/WebGL) Ten plik zawiera osadzoną przeglądarkę [three.js](http://threejs.org/), która pozwala obejrzeć scenę z poziomu Internetu, bez konieczności instalacji jakiejkolwiek wtyczki, o ile używasz przeglądarki obsługującej WebGL.

### System jednostek 

W końcu, system [jednostek](units/pl.md) został zaimplementowany na poziomie FreeCAD, przez co jest dostępny we wszystkich modułach. Możesz teraz wybrać w preferencjach schemat jednostek. Obecnie dostępne schematy zawierają milimetry, metry i jednostki imperialne, więcej schematów powinno być dostępne niebawem. Gdy tylko schemat jest ustanowiony, większość właściwości i narzędzi FreeCAD będzie preferować ich użycie. Jednak system jest elastyczny i większości miejsc, możesz mieszać jednostki jak tyko chcesz, np. dając wymiary w calach w dokumencie ustawionym na milimetry.

### Arkusze Stylów 

FreeCAD 0.14 staje się nawet jeszcze bardziej konfigurowalny dzięki dodaniu [Arkuszy Stylów](http://forum.freecadweb.org/viewtopic.php?f=8&t=4700&start=30) używanych do kontrolowania obrazu tła okna głównego. Użytkownik nie jest już zmuszony do używania szarego, kamiennego tła. Niemal każdy obraz, zdjęcie czy własny deseń może zostać wykorzystany do wypełnienia przestrzeni tła w głównym oknie FreeCAD.

<img alt="" src=images/Style_Sheets.png  style="width:1024px;">

### Nadpisywanie stylów wyświetlania 

Domyślny pasek narzędzi Widoku został rozszerzony o kilka nowych przycisków dla łatwego przełączania całego widoku 3D między trybami siatki, cieniowanym i cieniowanym z konturami.

### Okno 3D i wygładzanie krawędzi 

W programie FreeCAD dodano nowe opcje do systemu wygładzania krawędzi 3D. Możesz je znaleźć w ustawieniach. Jeśli masz dobry układ graficzny, to możesz teraz się cieszyć FreeCAD z bardzo wysokiej jakości wygładzaniem krawędzi.

## Part

### Połączenie przekrojów (Loft) i wyciągnięcie po ścieżce (Sweep) 

Narzędzia [Part Loft](Part_Loft.md) i [Part Sweep](Part_Sweep.md) zostały ulepszone i mogą teraz używać jako profili obiektów ze środowiska pracy Draft.

### Odsunięcie (Offset) 

Nowe narzędzie [Part Offset](Part_Offset/pl.md) tworzy kopię wybranego kształtu w określonej odległości od niego.

### Grubość (Thickness) 

Nowe narzędzie [Part Thickness](Part_Thickness/pl.md) jest teraz dostępne. To narzędzie działa na bryłę i zamienia ją w obiekt wydrążony, nadając każdej z ścian określoną grubość.

### Utwórz Kombinację (Make Compound) 

[Part Workbench](Part_Workbench/pl.md) zawiera teraz narzędzie [Make Compound](Part_Compound/pl.md), które pozwala szybko tworzyć obiekt kombinację z zestawu zaznaczonych kształtów.

### Prymitywy Part 

Nowe prymitywy Part zostały dodane do narzędzia [Part CreatePrimitives](Part_CreatePrimitives/pl.md): graniastosłupy, wielokąty foremne i spirale są teraz łatwe do utworzenie przez ustawienie kilku parametrów. Dalej, niektóre narzędzia z [Środowiska pracy Draft](Draft_Workbench/pl.md) mogą skorzystać z tej funkcji i również tworzyć te prymitywy, zamiast zwykłych obiektów Draft, jeśli odpowiednia opcja jest ustawiona w preferencjach Draft.

![](images/Part_Create_Primitives1.jpeg )

### Narzędzia pomiarowe 

Nowy zestaw narzędzi pomiarowych został dodany do środowiska pracy [Część](Part_Workbench/pl.md). Możesz nim wybrać dwa elementy *(wierzchołki, krawędzie lub ściany)* i wyświetlić bezwzględną odległość między nimi oraz odległość wzdłuż osi X i Y.

## PartDesign & Szkicownik (Sketcher) 

### Weryfikacja szkicu 

Środowisko pracy [Szkicownik](Sketcher_Workbench/pl.md) posiada teraz nowe narzędzie [Sprawdź poprawność szkicu](Sketcher_ValidateSketch/pl.md), które pomoże Ci zweryfikować poprawność szkicu, poprzez znalezienie brakujących lub zbędnych wiązań. Może również automatycznie dodawać brakujące wiązania, aby szkic był w pełni związany.

### Generator kół zębatych 

Narzędzie [generatora ewolwentowych kół zębatych](PartDesign_InvoluteGear/pl.md) zostało dodane do środowiska pracy [Projekt Części](PartDesign_Workbench/pl.md) by szybko tworzyć takie koła z zadanych parametrów.

## Rysunek (Drawing) 

### Automatyczne rzutowanie 

Środowisko pracy **Drawing** jest dalej usprawniany nowymi, ekscytującymi funkcjami. Projekcje Ortograficzne pozwalają teraz wyświetlać wszystkie widoki jak i zapewniać znacznie lepszą kontrolę nad poszczególnymi widokami. Kolejna kluczowa funkcja, Szablony Rysunku mogą zawierać teraz informacje definiujące położenie Granic i Bloku Tytułowego, które będą automatycznie ograniczać granice Projekcji jak i zapobiegać nachodzeniu na obszar zajęty przez Blok Tytułowy.

<img alt="" src=images/DrawingWB.png  style="width:1024px;">

### Symbole

Nowe narzędzie [Symbol Rysunkowy](Drawing_Symbol/pl.md) jest dostępne w [Środowisku pracy Drawing](Drawing_Workbench/pl.md) pozwalając na szybkie umieszczanie obiektów SVG w arkuszu Rysunku. Te obiekty są przechowywane w pliku FreeCAD, więc nie musisz dodawać oryginalnego pliku SVG, gdy dystrybuujesz swoje pliki.

## Raytracing

### Nowe narzędzia renderingu 

<img alt="" src=images/Raytracing_example.jpg  style="width:1024px;">

Zatroszczono się również o środowisko pracy [Raytracingu](Raytracing_Workbench/pl.md) i jego pasek narzędzi został przebudowany. \"Stare\" przyciski które ręcznie tworzyły częściowe pliki povray zostały usunięte *(są one ciągle dostępne w menu)* i teraz możesz tworzyć rendering w ten sam sposób jak używasz środowiska pracy [Kreślenie](Drawing_Workbench/pl.md): Tworzysz nowy projekt, nadajesz mu szablon i w końcu wypełniasz go widokami twoich obiektów. Gdy wszystko jest gotowe, po prostu wciśnij przycisk renderingu lub wyeksportuj do pliku gotowego na rendering na zewnątrz FreeCAD.

System [szablonów Raytracingu](Raytracing_Workbench/pl#Templates.md) również został rozszerzony i szablony są teraz łatwiejsze w obsłudze i tworzeniu.

Pliki .pov utworzone przez FreeCAD zawierają teraz informację o proporcjach obrazu. Użytkownicy nie muszą dalej zachowywać proporcji 4:3 w swoich ustawieniach Raytracingu lub manualne edytować plik wyjściowy w celu uzyskania prawidłowego renderu. Teraz może być wprowadzona dowolna szerokość i wysokość, bez strachu, że wyrenderowane obiekty będą spłaszczone lub wyciągnięte.

### Obsługa Luxrender 

Razem z istniejącą obsługą [POV-Ray](http://en.wikipedia.org/wiki/POV-Ray), środowisko pracy [Raytracing](Raytracing_Workbench/pl.md) obsługuje tera również [LuxRender](http://en.wikipedia.org/wiki/LuxRender). Podczas gdy POV-Ray [klasycznym raytracerem](http://pl.wikipedia.org/wiki/%C5%9Aledzenie_promieni), który emituje promienie z kamery w celu znalezienia koloru każdego piksela obrazu, Luxrender jest [bezstronnym rendererem](http://en.wikipedia.org/wiki/Unbiased_rendering), który potrzebuje znacznie więcej czasu na rendering scen, ale tworzy znacznie bardziej realistycznie oświetlenie.

## Arkusz kalkulacyjny (Spreadsheet) 

Zostało dodane nowe Środowisko pracy [Arkusza Kalkulacyjnego](Spreadsheet_Workbench/pl.md). Pozwala ono tworzyć obiekty [arkusza kalkulacyjnego](Spreadsheet_Create/pl.md) zawierające dwuwymiarowe dane. Wyposażony jest on również w edytor pozwalający zmieniać zawartość arkusza *(tekst, liczby i niektóre podstawowe formuły są obsługiwane)*, specjalny obiekt [kontrolera komórek](Spreadsheet_Controller/pl.md), który może skanować dokument dla określonych typów obiektów, wydobywając z nich określone właściwości i wypełniać wybrany zakres komórek ich wartościami.

<img alt="" src=images/Arch_tutorial_53.jpg  style="width:1024px;">

## Rysunek (Draft) 

### Import/eksport DWG 

FreeCAD może teraz importować i eksportować do [formatu DWG](https://pl.wikipedia.org/wiki/DWG), dzięki darmowemu, wieloplatformowemu [Teigha Converter](https://www.opendesign.com/guestfiles/oda_file_converter). Gdy tylko Teigha Converter jest zainstalowany, a ścieżka do niego jest ustawiona w preferencjach FreeCAD Draft, FreeCAD jest gotów do używania go do importu i eksportu plików dwg, przez konwersję ich do dxf i użycie importera/eksportera Draft. Dlatego też import i eksport plików dwg ma te same ograniczenia co [format dxf](Draft_DXF.md).

### Draft to Drawing działa z grupami 

Narzędzie [Draft to Drawing](Draft_Workbench/pl.md), używane do umiejscawiania obiektów Rysunku Roboczego na [arkuszu rysunku *(Drawing)*](Drawing_Workbench/pl.md), może być teraz stosowany na grupach, pozwalając na tworzenie mniejszej liczby obiektów Widoku w arkuszu rysunku. Inteligentnie łącząc twoje obiekty Draft w kilka grup, możesz uzyskać szybki sposób na kontrolę wyglądu wielu obiektów na twojej stronie.

### Wymiarowanie zostało przepisane 

Narzędzie[Rysunek Roboczy: Wymiar](Draft_Dimension/pl.md) zostało całkowicie przepisane i obiekty wymiarów zachowują się teraz znacznie lepiej, oraz zyskały kilka nowych właściwości, pozwalających na ich lepsze dostrojenie, jak ładniejsze i skalowalne strzałki, większa kontrola nad pozycją tekstu i kierunkiem wymiaru i, przede wszystkim, lepsze wsparcie środowiska pracy [Kreślenie](Drawing_Workbench/pl.md). Teraz możesz umiejscawiać wymiary w dowolnym miejscu przestrzeni 3D i oczekiwać prawidłowych rezultatów, gdy umieszczasz je na arkuszu rysunku *(Drawing)* przy użyciu narzędzia [Rysunku Roboczego](Draft_Workbench/pl.md).

<img alt="" src=images/Draft_dimensions_recode.jpg  style="width:1024px;">

### Kreskowanie

Środowisko pracy [Rysunek Roboczy](Draft_Workbench/pl.md) zawiera teraz też nową zabawkę: kreskowanie. Na określonych obiektach Draft *(tych, które formują zamknięty kształt, jak zamknięte polilinie, prostokąty, wielokąty foremne czy okręgi)*, można teraz stosować kreskowanie. Obecnie dostępne jest tylko kilka domyślnych wzorów kreskowania, ale ponieważ te wzory są bardzo łatwe do utworzenia *(to po prostu pliki svg)*, inne mogą zostać utworzone właśnie przez użytkownika i domyślna kolekcja może rozrosnąć się szybko. Obiekty Draft z wzorami są wiernie obsługiwane przez [warsztat Kreślenie](Drawing_Workbench/pl.md).

<img alt="" src=images/Draft_hatches.jpg  style="width:1024px;">

### Elipsy

Została dodana obsługa [elips](Draft_Ellipse/pl.md), warsztat Draft pozwala teraz ci rysować pełne elipsy lub ich wycinki.

### Faza

Jak przy zaokrągleniach, które pojawiły się w [wydaniu 0.13](Release_notes_0.13.md), prostokąty Draft, przewody i wielokąty zyskały teraz nową właściwość, która fazuje ich kąt. Faza jest stosowana przed zaokrągleniem i obie właściwości mogą być używane razem, pozwalając ci przekształcać prosty przewód w skomplikowany obiekt o złożony z wielu sekcji.

### Upgrade i downgrade zostały przepisane 

Narzędzia [Draft Upgrade](Draft_Upgrade.md) i [Draft Downgrade](Draft_Downgrade.md), wcześniej zaklęte kawałki magii, co od których nigdy nie miałeś pewności jaki dadzą wynik. Zostały przekodowane, a teraz wysyłają dużo bardziej przyjazne komunikaty, informujące Cię, co zostało zrobione i dlaczego. Są one teraz również dostępne dla skryptów Pythona, nie tylko jako całość, ale także ich wewnętrzne operacje. Więc można dokładnie nakazać wykonanie określonego typu aktualizacji.

### Facebinder

Nowe narzędzie [Draft Facebinder](Draft_Facebinder/pl.md) zostało dodane. Wykonuje ono bardzo prostą, ale potencjalnie bardzo przydatną operację: zbiera dowolną liczbę zaznaczonych ścian z różnych obiektów i tworzy nowy obiekt z tych ścian. Nowy obiekt zachowuje powiązanie do oryginalnych obiektów , więc jakakolwiek w nich zmiana jest odwzorowana na obiekcje facebinder. To powinno udowodnić swą przydatność szczególnie w obiektach [architektonicznych](Arch_Workbench/pl.md), gdzie możesz teraz konstruować nowe obiekty z ścian kilku obiektów.

### Shape strings 

Nowe narzędzie [Draft ShapeString](Draft_ShapeString/pl.md) tworzy obiekty planarne z tekstu i fontu truetype. Te obiekty, w przeciwieństwie do typowych adnotacji jak [Tekst Draft](Draft_Text/pl.md), są prawdziwymi obiektami 3D, mogą być wyciągane i przez to używane do tworzenia grawerowania lub innych obiektów 3D z wyciśniętym tekstem.

### Krzywe Beziera 

Wraz z istniejącymi krzywymi [łuk okręgu](Draft_Arc/pl.md) i [B-spline](Draft_BSpline/pl.md), nowy typ krzywej został włączony do środowiska Rysunek Roboczy: [krzywe Beziera](Draft_BezCurve/pl.md). Mogą być on tworzone przez klikanie punktów, w ten sam sposób jak inne obiekty Draft, ale możesz też później [edytować](Draft_Edit/pl.md) je i modyfikować ich uchwyty, osiągając bardzo precyzyjną kontrolę nad kształtem krzywej.

## Środowisko pracy Arch 

### Wstępne ustawienia struktury + profile 

Narzędzie [Arch Structure](Arch_Structure.md) zyskało kilka ulepszeń: teraz posiada predefiniowane ustawienia. Pozwalają one na szybkie zbudowanie belki lub kolumny w oparciu o standardowy profil, taki jak INP lub HEB, oraz łatwiejszy system pozycjonowania, ze specjalnym trybem [snapping](Draft_Snap.md). Teraz można również nadać elementom konstrukcyjnym ścieżkę wytłaczania, dzięki czemu możliwe są bardzo zaawansowane konfiguracje. Niektóre elementy oferowane przez [BOLTS](#Plugins_and_side_projects:_Parts_library.2C_BOLTS.2C_Eagle_importer.md) mogą być również tworzone bezpośrednio jako elementy konstrukcyjne Środowiska pracy Arch.

### Wstępne ustawienia okien 

Narzędzie [Arch Window](Arch_Window.md) zyskało również nowy system konfiguracji nastaw. Mimo, że nadal bazuje na szkicach, co zapewnia maksymalną elastyczność (praktycznie każdy typ okna może być łatwo tworzony), nowe okna mogą być teraz wykonane z szeregu nastaw. Wystarczy wybrać ustawienie wstępne, wypełnić kilka parametrów i umieścić okno w ścianie wyjściowej lub elemencie konstrukcyjnym. Pod nim zostanie utworzony odpowiedni szkic, który można edytować w dowolnym momencie.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:1024px;">

### Przestrzenie

Nowy obiekt [Space](Arch_Space.md) jest już dostępny, co pozwala na budowanie, zaznaczanie i obliczanie powierzchni i powierzchni podłogi. Obiekty te zawsze obejmują stałą objętość, dzięki czemu zawsze możesz znać ich objętość i powierzchnię podłogi. Mogą one być zbudowane z bryły lub z zestawu powierzchni granicznych.

### Ściany wielowarstwowe 

[Sciany](Arch_Wall.md) mogą być teraz wielowarstwowe, z bardzo prostą sztuczką: kilka ścian może być opartych na tej samej linii bazowej, określając przesunięcie odległości od linii bazowej. Takie rozwiązanie, połączone na przykład z [Arch Frames](Arch_Frame.md), pozwala na tworzenie skomplikowanych, obramowanych ścian lub ścian z warstwą izolacji. Co więcej, ściany te są świadome swoich \"braci\" *(inne ściany oparte na tej samej linii podstawowej)*, a każde okno umieszczone na jednej z tych ścian stworzy również otwór dla swoich braci.

<img alt="" src=images/Screenshot_arch_multiwall.jpg  style="width:1024px;">

### Schody

Dodano również nowe narzędzie [szchody](Arch_Stairs.md), które pozwala budować złożone schody z kilku parametrów. Obecnie dostępne są tylko proste schody, ale lista będzie się powiększać z czasem. Schody te mają wiele parametrów konfiguracyjnych, takich jak powierzchnia stopni, czy rodzaj ich konstrukcji.

### Pręty zbrojeniowe 

Pręty zbrojeniowe *(zwane również zbrojeniami)* zostały wprowadzone za pomocą narzędzia [Arch Rebar](Arch_Rebar.md). Są one również oparte na szkicach, co zapewnia dużą elastyczność. Są one tworzone zasadniczo poprzez rysowanie schematów prętów na odpowiednich powierzchniach czołowych [elementów konstrukcyjnych](Arch_Structure.md), a następnie przekształcanie tych schematów w rzeczywiste pręty zbrojeniowe.

<img alt="" src=images/Screenshot_arch_rebar.jpg  style="width:1024px;">

### Ramy

Systemy ramowe stosowane są wszędzie w architekturze: poręcze, systemy konstrukcyjne, ściany szkieletowe itp. Nowe narzędzie [Arch Frame](Arch_Frame.md) umożliwia łatwe tworzenie wszelkiego rodzaju konstrukcji szkieletowych, poprzez połączenie obiektu profilowego, którym może być dowolny płaski, wytłaczany kształt, taki jak prostokąt lub okrąg, oraz obiektu układowego, który definiuje linie wytłaczania, na których umieszczane są elementy obiektu szkieletu. Układy są zazwyczaj rysowane za pomocą Środowiska pracy [Sketcher](Sketcher_Workbench.md). Takie obiekty ram mogą być następnie zamienione w ściany lub konstrukcje, jeśli zajdzie taka potrzeba.

### Sondaż

Kolejne proste, ale użyteczne narzędzie jest teraz dostępne w trybie [Arch Survey](Arch_Survey.md). W tym trybie, klikasz na wierzchołki, krawędzie, ścianye lub całe obiekty i otrzymujesz ich wysokość, długość, powierzchnię lub objętość. Informacje te są wyświetlane na modelu, ale także kopiowane do schowka i zbierane jako tekst, więc łatwo jest wkleić je w innych aplikacjach, co daje dość szybki przepływ pracy podczas budowania rachunków ilościowych.

### Poradniki

Nowy 35-stronicowy [poradnik](Arch_tutorial.md) opisuje Środowisko pracy Arch we wszystkich jego szczegółach, uwzględniając kompletne wykonanie ćwiczenia.

### Import/eksport IFC 

Wiele pracy wykonano zarówno na FreeCAD jak i [IfcOpenShell](http://www.ifcopenshell.org), który jest oprogramowaniem odpowiedzialnym za obsługę plików IFC w środowisku Architektura. Używając [development version](http://github.com/aothms/IfcOpenShell) IfcOpenShell, oprócz spektakularnego wzrostu szybkości importu plików IFC średniej wielkości *(około 50MB)*, FreeCAD jest również w stanie eksportować modele do formatu IFC. Obsługa eksportu jest nadal w początkowej fazie rozwoju, ale już teraz udaje się wyeksportować pliki, które można odczytać bez błędów przez większość głównych aplikacji obsługujących IFC.

## Pełna lista 

Pełna lista poprawek błędów i nowych funkcji znajduje się na stronie <http://freecadweb.org/tracker/changelog_page.php>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 0.14/pl

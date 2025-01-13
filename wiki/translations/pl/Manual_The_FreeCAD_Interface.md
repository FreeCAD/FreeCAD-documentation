# Manual:The FreeCAD Interface/pl
{{Manual:TOC}}

FreeCAD jest oparty na [Qt](https://pl.wikipedia.org/wiki/Qt) i charakteryzuje się prostym i przejrzystym interfejsem. Bardziej doświadczeni użytkownicy CAD będą w stanie dostrzec podobieństwa z innymi programami, podczas gdy nowi użytkownicy znajdą nawigację intuicyjną i łatwą do odkrywania różnych opcji, jakie oferuje FreeCAD. Oto domyślny wygląd programu FreeCAD:

![](images/FreeCAD_022_Start.png )

Strona Startowa pełni rolę ekranu powitalnego, zaprojektowanego w celu ułatwienia szybkiego i łatwego dostępu do głównych obszarów FreeCAD, które użytkownik może chcieć eksplorować. Dzięki niej użytkownicy mogą bez trudu tworzyć nowe części, otwierać niedawno używane pliki i rozpocząć rysowanie 2D. Dodatkowo zawiera skróty do pomocnych zasobów, takich jak samouczki i fora użytkowników, które są niezwykle cenne zarówno dla początkujących, jak i bardziej doświadczonych użytkowników szukających wskazówek lub porad. Użytkownicy mogą łatwo dostosować wygląd Strony Startowej zgodnie z własnymi preferencjami.

W miarę jak stajesz się bardziej biegły w korzystaniu z programu FreeCAD, możesz dostosować ustawienia w preferencjach. Dzięki temu FreeCAD może otworzyć się bezpośrednio w jednym z środowisk pracy z gotowym nowym dokumentem. Alternatywnie, możesz po prostu zamknąć kartę Strony Startowej i ręcznie utworzyć nowy dokument.

![](images/FreeCAD_022_PartDesign.png )



### Środowiska pracy 

FreeCAD wykorzystuje system zwany \"środowiskami pracy\", podobny do koncepcji używanych w zaawansowanym oprogramowaniu projektowym, takim jak Revit czy CATIA. Idea środowiska pracy jest analogiczna do wyspecjalizowanych stacji w laboratorium naukowym, gdzie różne stanowiska są wyposażone w odpowiednie narzędzia do różnych rodzajów eksperymentów. W laboratorium może być jedno stanowisko dedykowane chemii, drugie biologii, a trzecie fizyce, z odpowiednimi narzędziami potrzebnymi w tych dziedzinach.

W kontekście FreeCAD każde środowisko pracy jest dostosowane do określonego typu zadania, organizując wszystkie niezbędne narzędzia do danej aktywności w jednym interfejsie. Przełączając się między środowiskami pracy, zestaw narzędzi i kontrolki widoczne w interfejsie użytkownika zmieniają się, aby odpowiadać potrzebom wybranego zadania, chociaż faktyczna zawartość projektu lub \"scena\", nad którą pracujesz, nie ulega zmianie. Umożliwia to płynne przejścia w przepływie pracy, na przykład rozpoczynając projektowanie od podstawowych kształtów 2D w środowisku pracy Rysunek Roboczy, a następnie rozwijając te projekty za pomocą zaawansowanych narzędzi modelowania w środowisku pracy Część.

Określenia \"środowisko pracy\" i \"moduł\" są czasami używane zamiennie, ale mają różne znaczenia w FreeCAD. Moduł to każde rozszerzenie, które dodaje funkcjonalność do FreeCAD, podczas gdy środowisko pracy to specyficzny rodzaj modułu, który wyposażony jest w własne komponenty interfejsu użytkownika, takie jak paski narzędzi i menu, zaprojektowane w celu ułatwienia realizacji określonych typów zadań. W związku z tym każde środowisko pracy jest modułem, ale nie każdy moduł kwalifikuje się jako środowisko pracy.

Najważniejszym elementem sterującym interfejsu FreeCAD jest selektor środowiska pracy, który służy do przełączania się z jednego środowiska pracy na drugie:

![](images/FreeCAD_WB.png )

-   <img alt="" src=images/Workbench_Assembly.svg  style="width:32px;"> The [Złożenie](Assembly_Workbench/pl.md) do tworzenia i rozwiązywania mechanicznych złożeń. {{Version/pl|1.0}}

-   <img alt="" src=images/Workbench_BIM.svg  style="width:32px;"> The [BIM](BIM_Workbench/pl.md) do pracy z elementami architektonicznymi i tworzenia modeli [BIM](https://en.wikipedia.org/wiki/Building_information_modeling). Łączy środowisko pracy Architektura i wcześniej zewnętrzne środowisko pracy BIM dostępne w {{VersionMinus/pl|0.21}}.

-   <img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> [CAM](CAM_Workbench/pl.md) służy do tworzenia instrukcji G-Code. To środowisko pracy zostało nazwane \"Path\" w {{VersionMinus/pl|0.21}}.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [Rysunek Roboczy](Draft_Workbench/pl.md) zawiera narzędzia 2D oraz podstawowe operacje CAD 2D i 3D.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> [MES](FEM_Workbench/pl.md) zapewnia narzędzia do analiz metodą elementów skończonych *(MES)*.

-   <img alt="" src=images/_Workbench_Inspection.svg  style="width:32px;"> [Inspekcja](Inspection_Workbench/pl.md) ma na celu udostępnienie narzędzi do badania kształtów. Nadal jest we wczesnej fazie rozwoju.

-   <img alt="" src=images/Workbench_Material.svg  style="width:32px;"> [Materiał](Material_Workbench.md) obsługuje system materiałów we FreeCAD. {{Version/pl|1.0}}

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> [Siatka](Mesh_Workbench/pl.md) do pracy z siatkami o trójkątnych oczkach.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> [OpenSCAD](OpenSCAD_Workbench/pl.md) dla interoperacyjności z OpenSCAD i naprawiania historii modeli typu [konstrukcyjnej geometrii bryły](Constructive_solid_geometry/pl.md) *(CSG)*.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [Część](Part_Workbench/pl.md) do pracy z pierwotnymi obiektami geometrycznymi i operacjami logicznymi.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [Projekt Części](PartDesign_Workbench/pl.md) do budowy kształtów części ze szkiców.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> [Punkty](Points_Workbench/pl.md) do pracy z chmurami punktów.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> [Inżynieria Wsteczna](Reverse_Engineering_Workbench/pl.md) ma na celu dostarczenie specyficznych narzędzi do konwersji kształtów/brył/siatek na parametryczne elementy kompatybilne z FreeCAD.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> [Robot](Robot_Workbench/pl.md) do badania ruchów robotów. Obecnie nie jest utrzymywany.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Szkicownik](Sketcher_Workbench/pl.md) do pracy na szkicach z zachowaniem wiązań geometrii.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> [Arkusz Kalkulacyjny](Spreadsheet_Workbench/pl.md) do tworzenia i manipulowania danymi w arkuszu kalkulacyjnym.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> [Powierzchnia](Surface_Workbench/pl.md) dostarcza narzędzi do tworzenia i modyfikowania powierzchni. Jest on podobny do opcji Ściana z krawędzi narzędzia [Konstruktor kształtu](Part_Builder/pl.md).

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md) do tworzenia rysunków technicznych dla modeli przestrzennych. Jest to następca środowiska [Kreślenie](Drawing_Workbench/pl.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> [Test Framework](Testing/pl.md) służy do debugowania programu FreeCAD.

Środowiska pracy często wprowadzają w błąd nowych użytkowników, ponieważ nie zawsze oczywiste jest to, w którym środowisku pracy szukać konkretnego narzędzia. Jednak po krótkim czasie stają się one intuicyjne, a użytkownicy szybko zdają sobie sprawę, że środowiska pracy to wygodny sposób na organizację licznych narzędzi, które oferuje FreeCAD. Dodatkowo, środowiska pracy są w pełni konfigurowalne.



### Interfejs użytkownika 

Przyjrzyjmy się bliżej różnym częściom interfejsu:

![](images/FreeCAD_022_Interface.png )

Główne okno aplikacji można podzielić mniej więcej na 11 sekcji:

1.  [Główny obszar widoku](main_view_area/pl.md), który może zawierać różne okna z zakładkami.
2.  [Widok 3D](3D_view/pl.md), zazwyczaj osadzony w [głównym obszarze widoku](main_view_area/pl.md). Widok 3D jest centralnym elementem interfejsu, wyświetlającym i umożliwiającym manipulację obiektami, nad którymi pracujesz. Możliwe jest posiadanie wielu widoków tego samego dokumentu (lub obiektów) lub otwieranie kilku dokumentów jednocześnie. Dodatkowo, każdy widok można oddzielić od głównego okna.
3.  Zakładka Model i [Panel zadań](task_panel/pl.md).
    1.  Zakładka Model pokazuje zawartość i strukturę twojego dokumentu.
    2.  Zakładka Zadania to miejsce, w którym FreeCAD poprosi cię o wartości specyficzne dla używanego warsztatu i narzędzia (na przykład wymiary obiektu).
4.  [Edytor właściwości](property_editor/pl.md), który pojawia się, gdy zakładka Model jest aktywna w interfejsie. Umożliwia zarządzanie publicznymi właściwościami obiektów w dokumencie. Składa się z sekcji Dane i Widok, pokazujących odpowiednio właściwości wizualizacji i parametryczne obiektów.
5.  [Widok zaznaczenia](selection_view/pl.md), który wskazuje wybrane obiekty lub podelementy obiektów (wierzchołki, krawędzie, powierzchnie).
6.  [Widok raportu](report_view/pl.md), w którym wyświetlane są komunikaty, ostrzeżenia i błędy.
7.  [Konsola Pythona](python_console/pl.md). Konsola Pythona, w której wyświetlane są wszystkie wykonane polecenia i gdzie można wprowadzać kod Pythona.
8.  [Pasek statusu](status_bar/pl.md), w którym pojawiają się niektóre komunikaty i podpowiedzi.
9.  Obszar paska narzędzi, w którym są dokowane paski narzędzi.
10. [Wybór środowiska pracy](Std_Workbench/pl.md), w którym wybierasz aktywne [środowisko pracy](workbenches/pl.md).
11. [Menu standardowe](Standard_Menu/pl.md), które zawiera podstawowe operacje programu.

Większość z powyższych paneli można ukryć lub wyświetlić za pomocą opcji **Widok → Panele** w menu.



### Dostosowanie interfejsu graficznego 

Interfejs FreeCAD jest zaprojektowany z myślą o szerokiej personalizacji. Wszystkie paski narzędzi i panele można przenosić, układać w stosy, a nawet dokować w różnych konfiguracjach zgodnie z preferencjami użytkownika. Dodatkowo można je zamknąć, a następnie ponownie otworzyć w razie potrzeby. Poza tymi możliwościami, użytkownicy mają wiele innych opcji, w tym możliwość tworzenia własnych pasków narzędzi z narzędziami wybranymi z dowolnego dostępnego środowiska pracy oraz przypisywania lub modyfikowania skrótów klawiaturowych w celu usprawnienia pracy. Ta elastyczność zapewnia, że użytkownicy mogą dostosować środowisko do swoich specyficznych potrzeb i preferencji.

Te zaawansowane opcje dostosowywania są dostępne w menu **Przybory → Dostosuj ...**:

![](images/FreeCAD_022_Customization.png )

**Więcej informacji:**

-   [Jak zacząć](Getting_started/pl.md)
-   [Dostosowywanie interfejsu użytkownika do własnych potrzeb](Interface_Customization/pl.md)
-   [Środowiska pracy](Workbenches/pl.md)
-   [More about Python](https://www.python.org)



---
⏵ [documentation index](../README.md) > Manual:The FreeCAD Interface/pl

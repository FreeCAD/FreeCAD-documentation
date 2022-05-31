# User hub/pl
{{TOCright}} <img alt="" src=images/User_hub.png  style="width   *64px;">



Jesteś właśnie na głównej stronie pomocy przeznaczonej dla wszystkich nowych użytkowników FreeCAD.

Tak jak sam program FreeCAD, tak i ta dokumentacja jest w ciągłym rozwoju. Niektóre informacje mogą być już nieaktualne, lub pominięte. Jeśli nie możesz znaleźć potrzebnych informacji, nie wahaj się zapytać na forum [FreeCAD forum](https   *//forum.freecadweb.org).

Jeśli chciałbyś wesprzeć projekt FreeCAD, proszę wykjonaj [dotację](donate.md) oraz zobacz stronę   * [Wesprzyj program FreeCAD](Help_FreeCAD/pl.md) dla innych sposobów wnoszenia wkładu. Jeśli chciałbyś przyczynić się do tworzenia tej Wiki, poproś o uprawnienia edycji [na forum](https   *//forum.freecadweb.org/viewtopic.php?f=21&t=6830), i przeczytaj [WikiPages](WikiPages.md). Tam znajdziesz ogólne zasady których powinieneś się trzymać podczas edycji Wikipedii.

A jeśli interesuje cię historia programu FreeCAD, odwiedź stronę [Historia](History.md).

## Korzystanie z programu FreeCAD 

### Wprowadzenie

-   [Przegląd aplikacji](About_FreeCAD/pl.md)   * Ogólny przegląd programu FreeCAD.
-   [Instalacja](Installing/pl.md)   * Instrukcja instalacji FreeCAD dla [Linux](Install_on_Linux/pl.md), [Mac](Install_on_Mac/pl.md) i [Windows](Install_on_Windows/pl.md).
-   [Instalacja dokumentacji użytkownika](Installing_Helpfile/pl.md)   * jak zainstalować dokumentację offline, bazującą na Wiki.
-   [Instalacja dodatkowych komponentów](Installing_additional_components/pl.md)   * jak zainstalować dodatkowe komponenty zewnętrzne, które mogą współpracować z programem FreeCAD.
-   [Jak zacząć](Getting_started/pl.md)   * Szybkie wprowadzenie do dostępnych funkcji programu.
-   [FAQ](Frequently_asked_questions/pl.md)   * Odpowiedzi na najczęściej zadawane pytania.
-   [Poradniki](Tutorials/pl.md) obejmujące różne części FreeCAD.

#### Migracja z innego oprogramowania? 

-   [Rozwiązania](Workarounds.md)
-   [Migracja do FreeCAD z Fusion360](Migrating_to_FreeCAD_from_Fusion360/pl.md)
-   [Migracja do FreeCAD z OnShape](Migrating_to_FreeCAD_from_OnShape/pl.md)
-   [Migracja do FreeCAD z SolidWorks](Migrating_to_FreeCAD_from_SolidWorks/pl.md)
-   [Migracja do FreeCAD z Revit](Migrating_to_FreeCAD_from_Revit/pl.md)
-   [FreeCAD BIM poradnik migracji](https   *//yorik.uncreated.net/blog/2020-010-freecad-bim-guide)
-   [Tabela kompatybilności aplikacji BIM](BIM_application_compatibility_table/pl.md)

### Informacje podstawowe 

-   [Interface](Interface/pl.md)   * interfejs FreeCAD jest zbudowany z różnych elementów graficznych dostępnych na ekranie, w tym [widok 3D](3D_view/pl.md), [widok drzewa](Tree_view/pl.md), [edytor właściwości](Property_editor/pl.md), [panel zadań](Task_panel/pl.md), oraz [konsola Pythona](Python_console/pl.md).
-   [Nawigacja przy użyciu myszki](Mouse_navigation/pl.md)   * różne warianty obsługi za pomocą myszki lub gładzika do obsługi widoku 3D.
-   [Wybór](Selection_methods/pl.md)   * różne style wybierania obiektów w programie.
-   [Nazwa obiektu](Object_name/pl.md)   * obiekty FreeCAD mają atrybut `Nazwa` tylko do odczytu, który je jednoznacznie identyfikuje, oraz atrybut `Etykieta`, który można być edytowany przez użytkownika.
-   [Edytor ustawień](Preferences_Editor/pl.md) i [Presonalizacja](Interface_Customization/pl.md)   *   * mechanizm, który pozwala dostosować wiele parametrów systemu bazowego i poszczególnych środowisk roboczych.
-   [Właściwości obiektów](Property_editor/pl.md)   * Jak działają właściwości obiektów w programie FreeCAD.
-   [Struktura dokumentu](Document_structure/pl.md)   * W jaki sposób twój dokument jest zorganizowany, z jakich części się składa.
-   [Formaty plików](Import_Export/pl.md)   * różne typy plików, które mogą być odczytywane i zapisywane przez FreeCAD.
-   [Środowiska pracy](Workbenches/pl.md)   * W jaki sposób zorganizowany jest interfejs aplikacji.
-   [Makra](Macros/pl.md)   * jak łatwo zautomatyzować powtarzające się czynności

### Środowiska pracy 

[Środowisko pracy](Workbenches/pl.md) reprezentowane jest przez zestaw powiązanych narzędzi, które są wykorzystywane do realizacji konkretnych zadań. Są to podstawowe środowiska pracy dołączone do każdej instalacji FreeCAD   *

-   <img alt="" src=images/Freecad.svg  style="width   *32px;"> [Narzędzia standardowe](Std_Base/pl.md). Te polecenia i narzędzia są obecne we wszystkich środowiskach pracy.

-   <img alt="" src=images/Workbench_Arch.svg  style="width   *32px;"> [Architektura](Arch_Workbench/pl.md) do pracy z elementami architektonicznymi.

-   <img alt="" src=images/Workbench_Draft.svg  style="width   *32px;"> [Rysunek Roboczy](Draft_Workbench/pl.md) zawiera narzędzia 2D oraz podstawowe operacje CAD 2D i 3D.

-   <img alt="" src=images/Workbench_FEM.svg  style="width   *32px;"> [MES](FEM_Workbench/pl.md) zapewnia przepływ pracy w zakresie analizy elementów skończonych *(Finite Element Analysis FEA)*.

-   <img alt="" src=images/Workbench_Image.svg  style="width   *32px;"> [Obraz](Image_Workbench/pl.md) do pracy z obrazami bitmapowymi.

<img alt="" src=images/_Workbench_Inspection.svg  style="width   *32px;"> [Inspekcja](Inspection_Workbench/pl.md) ma na celu udostępnienie narzędzi do badania kształtów. Nadal jest w fazie rozwoju.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width   *32px;"> [Siatka](Mesh_Workbench/pl.md) do pracy z siatkami o trójkątnych oczkach.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width   *32px;"> [OpenSCAD](OpenSCAD_Workbench/pl.md) dla interoperacyjności z OpenSCAD i naprawiania historii modeli typu [konstrukcyjnej geometrii bryły](Constructive_solid_geometry/pl.md) *(CSG)*.

-   <img alt="" src=images/Workbench_Part.svg  style="width   *32px;"> [Część](Part_Workbench/pl.md) do pracy z częściami CAD.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width   *32px;"> [Projekt Części](PartDesign_Workbench/pl.md) do budowy kształtów części ze szkiców.

-   <img alt="" src=images/Workbench_Path.svg  style="width   *32px;"> [Path](Path_Workbench/pl.md) jest używany do tworzenia operacji G-Code. Jest on nadal w fazie rozwoju.

-   <img alt="" src=images/Workbench_Points.svg  style="width   *32px;"> [Punkty](Points_Workbench/pl.md) do pracy z chmurami punktów.

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width   *32px;"> [Raytracing](Raytracing_Workbench/pl.md) do pracy z ray-tracingiem (renderingiem).

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width   *32px;"> [Inżynieria Wsteczna](Reverse_Engineering_Workbench/pl.md) ma na celu dostarczenie specyficznych narzędzi do konwersji kształtów/brył/siatek na parametryczne elementy kompatybilne z FreeCAD. Jest nadal w fazie rozwoju.

-   <img alt="" src=images/Workbench_Robot.svg  style="width   *32px;"> [Robot](Robot_Workbench/pl.md) do badania ruchów robotów.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width   *32px;"> [Szkicownik](Sketcher_Workbench/pl.md) do pracy na szkicach z zachowaniem wiązań geometrii.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width   *32px;"> [Arkusz Kalkulacyjny](Spreadsheet_Workbench/pl.md) do tworzenia i manipulowania danymi w arkuszu kalkulacyjnym.

-   <img alt="" src=images/Workbench_Start.svg  style="width   *32px;"> [Start](Start_Workbench/pl.md) pozwala na szybkie przejście do jednego z najczęściej stosowanych stołów warsztatowych.

-   <img alt="" src=images/Workbench_Surface.svg  style="width   *32px;"> [Powierzchnia](Surface_Workbench/pl.md) dostarcza narzędzi do tworzenia i modyfikowania powierzchni. Jest on podobny do narzędzia [konstruktora kształtu części](Part_Builder/pl.md) środowiska Część, z krawędzi.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width   *32px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md) do tworzenia rysunków technicznych dla modeli przestrzennych. Jest to następca środowiska [Kreślenie](Drawing_Workbench/pl.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width   *32px;"> [Test Framework](Testing/pl.md) służy do debugowania programu FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width   *32px;">[Web](Web_Workbench/pl.md) udostępnia okno przeglądarki w oknie [widoku 3D](3D_view/pl.md) dla programiu FreeCAD.

### Makra

[Makrodefinicje](Macros.md) to niewielkie fragmenty kodu [Python](Python.md), które wykonują proste lub złożone zadania, dotychczasowo niedostępne w bazowym systemie FreeCAD.

Doświadczeni użytkownicy napisali różne [makra](macros.md), aby wzbogacić FreeCAD o więcej funkcjonalności.

Od wersji FreeCAD 0.17, wiele makr można zainstalować za pomocą [Menadżer dodatków](Std_AddonMgr/pl.md). Lista makrodefinicji znajduje się na stronie [przepisy na makrodefinicje](Macros_recipes/pl.md). Ręczna instalacja - patrz [Jak zainstalować makra](How_to_install_macros/pl.md).

### Dodatkowe Środowiska pracy 

Gdy wiele makrodefinicji lub funkcji jest opracowywanych przy użyciu wspólnych pasków narzędzi i menu, mogą one stać się nowym Środowiskiem pracy.

[Zewnętrzne Środowiska pracy](External_workbenches.md) to zbiór funkcji, które nie są częścią podstawowego systemu FreeCAD, zwykle stworzone są przez doświadczonych użytkowników i ukierunkowane na realizacje konkretnej potrzeby.

Od wersji FreeCAD **0.17**, wiele stołów roboczych może być zainstalowanych przy użyciu [Menadżera dodatków](Std_AddonMgr/pl.md). Ręczna instalacja - patrz [Jak zainstalować dodatkowe Środowiska pracy](How_to_install_additional_workbenches/pl.md).

## Odwołania

[Lista komend](List_of_Commands/pl.md)   * Pełna lista dostępnych poleceń FreeCAD.

## System pomocy Online 

Jest to oficjalna pomoc Online FreeCAD. Proszę zwrócić uwagę, że cały system pomocy Online jest obecnie opracowywany na nowo. Zostanie on użyty do wygenerowania pliku w formacie .CHM, który będzie dystrybuowany wraz z pakietami binarnymi FreeCAD. W chwili obecnej pomoc online streszcza niektóre z najbardziej kompletnych sekcji tej wiki.

-   [ System pomocy online - Spis treści](Online_Help_Toc/pl.md)

## Informacje dodatkowe 

-   [Centrum Power użytkownika](Power_users_hub/pl.md) to miejsce dla zaawansowanych użytkowników programu FreeCAD.
-   [Portal społecznościowy FreeCAD](FreeCAD_Community_Portal/pl.md) wyświetla listę projektów wykonanych przez członków społeczności zgromadzonej wokół FreeCAD.
-   Nie rozumiesz jakiegoś terminu lub zwrotu w FreeCAD? Sprawdź go w [Słowniczku](Glossary/pl.md).




[Category   *Hubs](Category_Hubs.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Hubs](Category_Hubs.md) > User hub/pl

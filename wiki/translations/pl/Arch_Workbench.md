# <img alt="Ikonka FreeCAD dla środowiska pracy Architektura" src=images/Workbench_Arch.svg  style="width:64px;"> Arch Workbench/pl






## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Architektura](Arch_Workbench/pl.md) zapewnia [modelowanie informacji o budynku](http://en.wikipedia.org/wiki/Building_Information_Modeling) *(BIM)* nowoczesny przepływ pracy programu FreeCAD, z obsługą funkcjonalności takich jak w pełni parametryczne struktury architektoniczne obejmujące: ściany, elementy konstrukcyjne, dachy, okna, schody, rury i meble. Obsługuje on dane [branżowe klasy fundamentów](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) plików *([IFC](Arch_IFC.md))* oraz produkcję rzutów poziomych 2D w połączeniu z Środowiskiem pracy <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md).

Środowisko pracy Architektura importuje wszystkie narzędzia środowiska <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md), ponieważ używa obiektów 2D do budowy swoich przestrzennych obiektów architektonicznych. Niemniej jednak Arch może używać kształtów brył utworzonych w innych środowiskach pracy, takich jak <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md) i <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md).

Funkcjonalność BIM FreeCAD jest obecnie stopniowo poszerzana w obrębie środowiska pracy Architektura, które posiada podstawowe narzędzia architektoniczne, oraz <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [środowisko pracy BIM](BIM_Workbench/pl.md), które można zainstalować za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md). Środowisko BIM dodaje nową warstwę interfejsu nad narzędziami Arch, w celu uczynienia przepływu BIM bardziej intuicyjnym i przyjaznym dla użytkownika. Zobacz [Przewodnik migracji FreeCAD BIM](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide).

Twórcy Draft, Arch i BIM współpracują również z większą [Społecznością OSArch](https://osarch.org), mając na uwadze ostateczny cel, jakim jest poprawa projektowania budynków przy użyciu całkowicie wolnego oprogramowania.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">



## Przybory

Są to narzędzia służące do tworzenia obiektów architektonicznych.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Ściana](Arch_Wall/pl.md): Tworzy ścianę od podstaw lub używając wybranego obiektu jako podstawy.

-   <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Konstrukcja](Arch_Structure/pl.md): Tworzy element konstrukcyjny od podstaw lub używając wybranego obiektu jako podstawy.

-   <img alt="" src=images/Arch_CompRebarStraight.png  style="width:48px;"> [Narzędzia zbrojenia](Arch_CompRebarStraight/pl.md): Narzędzia te są dostępne tylko wtedy, gdy zainstalowano środowisko pracy [Zbrojenie](Reinforcement_Workbench/pl.md).

  -<img alt="" src=images/Arch_Rebar_Straight.svg  style="width:32px;"> [Pręty zbrojeniowe proste](Arch_Rebar_Straight/pl.md): Tworzy prosty pręt zbrojeniowy w wybranym elemencie konstrukcyjnym.

-   <img alt="" src=images/Arch_Rebar_UShape.svg  style="width:32px;"> [Pręty zbrojeniowe typu U](Arch_Rebar_UShape/pl.md): Tworzy pręt zbrojeniowy w kształcie litery U w wybranym elemencie konstrukcyjnym.

  - <img alt="" src=images/Arch_Rebar_LShape.svg  style="width:32px;"> [Pręty zbrojeniowe typu L](Arch_Rebar_LShape/pl.md): Tworzy pręt zbrojeniowy w kształcie litery L w wybranym elemencie konstrukcyjnym.

  - <img alt="" src=images/Arch_Rebar_Stirrup.svg  style="width:32px;"> [Strzemiona zbrojeniowe](Arch_Rebar_Stirrup/pl.md): Tworzy pręt zbrojeniowy strzemion w wybranym elemencie konstrukcyjnym.

  - <img alt="" src=images/Arch_Rebar_BentShape.svg  style="width:32px;"> [Pręty zbrojeniowe wygięte](Arch_Rebar_BentShape/pl.md): Tworzy pręt zbrojeniowy typu wygiętego w wybranym elemencie konstrukcyjnym.

  - <img alt="" src=images/Arch_Rebar_Helical.svg  style="width:32px;"> [Pręty zbrojeniowe spiralne](Arch_Rebar_Helical/pl.md): Tworzy spiralny pręt zbrojeniowy w wybranym elemencie konstrukcyjnym.

  - <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Pręty zbrojeniowe, zbrojenie słupów](Arch_Rebar_ColumnReinforcement/pl.md): Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym słupa prostokątnego.

  - <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> [Pręty zbrojeniowe, zbrojenie belek](Arch_Rebar_BeamReinforcement/pl.md): Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym belki.

  - <img alt="" src=images/Arch_Rebar_Slab_Reinforcement.svg  style="width:32px;"> [Pręty zbrojeniowe, zbrojenie płyt stropowych](Arch_Rebar_Slab_Reinforcement/pl.md): Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym płyty.

  - <img alt="" src=images/Arch_Rebar_Footing_Reinforcement.svg  style="width:32px;"> [Zbrojenie stóp fundamentowych](Arch_Rebar_Footing_Reinforcement/pl.md): Tworzy pręty zbrojeniowe wewnątrz obiektu konstrukcyjnego ławy fundamentowej.

  - <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Pręt zbrojeniowy](Arch_Rebar/pl.md): Tworzy niestandardowy pręt zbrojeniowy w wybranym elemencie konstrukcyjnym za pomocą szkicu.

-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Ściana kurtynowa](Arch_CurtainWall/pl.md): Tworzy ścianę kurtynową od podstaw lub używając wybranego obiektu jako bazy.

-   <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;"> [Część budowli - piętro](Arch_BuildingPart/pl.md): Tworzy część budynku zawierającą wybrane obiekty.

-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Projekt](Arch_Project/pl.md): Tworzy projekt zawierający wybrane obiekty.

-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Teren](Arch_Site/pl.md): Tworzy teren z uwzględnieniem wybranych obiektów.

-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Budynek](Arch_Building/pl.md): Tworzy budynek wraz z wybranymi obiektami.

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Piętro](Arch_Floor/pl.md): Tworzy piętro obejmujące wybrane obiekty.

-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Odniesienie](Arch_Reference/pl.md): Łączy obiekty z innego pliku FreeCAD do bieżącego dokumentu.

-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Okno](Arch_Window/pl.md): Tworzy okno od podstaw lub używając wybranego obiektu jako bazy.

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Dach](Arch_Roof/pl.md): Tworzy spadzisty dach z wybranych linii łamanych.

-   <img alt="" src=images/Arch_CompAxis.png  style="width:48px;"> [Komponent osie](Arch_CompAxis/pl.md)

  - <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Osie](Arch_Axis/pl.md): Dodaje zestaw osi jednokierunkowych.

  - <img alt="" src=images/Arch_AxisSystem.svg  style="width:32px;"> [Układ osi](Arch_AxisSystem/pl.md): Dodaje układ osi składający się z kilku osi.

  - <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Siatka](Arch_Grid/pl.md): Dodaje obiekt przypominający siatkę.

-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Płaszczyzna przekroju](Arch_SectionPlane/pl.md): Dodaje obiekt płaszczyzny przekroju.

-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Kubatura](Arch_Space/pl.md): Tworzy obiekt kubatury.

-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Schody](Arch_Stairs/pl.md): Tworzy obiekt schodów.

-   <img alt="" src=images/Arch_CompPanel.png  style="width:48px;"> [Komponent panel](Arch_CompPanel/pl.md)

  - <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Panel](Arch_Panel/pl.md): Tworzy obiekt panelu z wybranego obiektu 2D.

  - <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Panelizacja do cięcia](Arch_Panel_Cut/pl.md): Tworzy widok wycięcia 2D z panelu.

  - <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Arkusz panela](Arch_Panel_Sheet/pl.md): Tworzy arkusz cięcia 2D zawierający wycięcia paneli lub innych obiektów 2D.

  - <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Zagnieżdżanie](Arch_Nest/pl.md): Umożliwia zagnieżdżenie kilku płaskich obiektów wewnątrz kształtu kontenera.

-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Wyposażenie](Arch_Equipment/pl.md): Tworzy obiekt wyposażenia lub mebli.

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Ramy](Arch_Frame/pl.md): Tworzy obiekt ramy na podstawie wybranego układu.

-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Ogrodzenie](Arch_Fence/pl.md): Tworzy obiekt ogrodzenia z wybranego słupka i ścieżki.

-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Kratownica](Arch_Truss/pl.md): Tworzy kratownicę na podstawie wybranej linii lub od podstaw.

-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profil](Arch_Profile/pl.md): Tworzy parametryczny profil 2D.

-   <img alt="" src=images/Arch_CompSetMaterial.png  style="width:48px;"> [Komponent ustaw materiał](Arch_CompSetMaterial/pl.md)

  - <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Materiał](Arch_SetMaterial/pl.md): Tworzy materiał i przypisuje go do wybranych obiektów, jeśli takie istnieją.

  - <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Materiał złożony](Arch_MultiMaterial/pl.md): Tworzy materiał złożony z wielu elementów i przypisuje go do wybranych obiektów, jeśli takie istnieją.

-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Obmiar](Arch_Schedule/pl.md): Tworzenie różnych typów obmiaru.

-   <img alt="" src=images/Arch_CompPipe.png  style="width:48px;"> [Komponent narzędzia rur](Arch_CompPipe/pl.md)

  - <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Rura](Arch_Pipe/pl.md): Tworzy rurę.

  - <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Kształtka](Arch_PipeConnector/pl.md): Tworzy połączenie kolankiem lub połączenie typu trójnik między dwoma lub trzema wybranymi rurami.



### Narzędzia do modyfikacji 

Są to narzędzia służące do modyfikowania obiektów architektonicznych.

-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Płaszczyzna cięcia](Arch_CutPlane/pl.md): Przycina obiekt według płaszczyzny.

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Linia cięcia](Arch_CutLine/pl.md): Przycina obiekt zgodnie z linią.

-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Dodaj komponent](Arch_Add/pl.md): Dodaje obiekty do komponentu.

-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Usuń komponent](Arch_Remove/pl.md): Odejmuje lub usuwa obiekty z komponentu.

-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Spis wymiarów](Arch_Survey/pl.md): Włącza lub wyłącza tryb pomiaru.



### Przydatne narzędzia 

Są to dodatkowe narzędzia, które pomogą Ci w konkretnych zadaniach.

-   <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Komponent](Arch_Component/pl.md): Tworzy nieparametryczny komponent architektury.

-   <img alt="" src=images/Arch_CloneComponent.svg  style="width:32px;"> [Klonuj komponent](Arch_CloneComponent/pl.md): Tworzy komponenty architektury, które są klonami wybranych obiektów architektury *(nie mylić z funkcją środowiska Rysunek Roboczy [Klonuj](Draft_Clone/pl.md))*.

-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Podziel siatkę](Arch_SplitMesh/pl.md): Dzieli wybraną siatkę na osobne elementy.

-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Siatka na kształt](Arch_MeshToShape/pl.md): Przekształca siatkę w kształt, ujednolicając współpłaszczyznowe powierzchnie.

-   <img alt="" src=images/Arch_SelectNonSolidMeshes.svg  style="width:32px;"> [Zaznacz siatki niebryłowe](Arch_SelectNonSolidMeshes/pl.md): Wybiera wszystkie siatki typu non-manifold z bieżącego zaznaczenia lub z dokumentu.

-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Usuń kształt](Arch_RemoveShape/pl.md): Zmienia obiekt architektury oparty na kształcie sześciennym w całkowicie parametryczny.

-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Zamknij otwory](Arch_CloseHoles/pl.md): Zamyka otwory w wybranym obiekcie opartym na kształcie.

-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Połącz ściany](Arch_MergeWalls/pl.md): Scala dwie lub więcej ścian.

-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Sprawdź](Arch_Check/pl.md): Sprawdza, czy wybrane obiekty są bryłami i nie zawierają defektów.

-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Przełącz flagę Brep IFC](Arch_ToggleIfcBrepFlag/pl.md): Wymusza wyeksportowanie wybranego obiektu jako obiektu [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).

-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [Trzy widoki](Arch_3Views/pl.md): Tworzy widoki z góry, z przodu i z boku dla [siatki](Mesh_Workbench/pl.md).

-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> [Arkusz kalkulacyjny IFC](Arch_IfcSpreadsheet/pl.md): Tworzy arkusz kalkulacyjny do przechowywania właściwości [IFC](Arch_IFC/pl.md) obiektu.

-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Przełącz widoczność elementów podrzędnych](Arch_ToggleSubs/pl.md): Pokazuje lub ukrywa elementy podrzędne obiektu architektury.



### Ustawienia

-   <img alt="" src=images/Preferences-arch.svg  style="width:32px;"> [Preferences](Arch_Preferences.md): preferencje dotyczące domyślnego wyglądu ścian, konstrukcji, zbrojenia, okien, schodów, paneli, rur, siatek i osi.



### Formaty plików 

-   [IFC](Arch_IFC.md) : Industry foundation Classes.
-   [DAE](Arch_DAE.md) : format Collada dla siatek.
-   [OBJ](Arch_OBJ.md) : format OBJ dla siatek *(tylko eksport)*.
-   [JSON](Arch_JSON.md) : format zapisu obiektu w JavaScript *(tylko eksport)*.
-   [3DS](Arch_3DS.md) : format 3DS *(tylko import)*.
-   [SHP](Arch_SHP.md): GIS Shapefiles *(tylko import)*.



## API

Moduł Arch może być używany w skryptach [Python](Python.md) i [makrodefiniacjach](Macros/pl.md) za pomocą funkcji [Arch Python API](Arch_API/pl.md).



## Poradniki

-   [Migracja do FreeCAD z Revit](Migrating_to_FreeCAD_from_Revit/pl.md)
-   [Architecture workflow](http://yorik.uncreated.net/guestblog.php?tag=freecad): Przykład, w jaki sposób FreeCAD może zacząć zajmować pierwsze miejsce pod względem przepływu pracy w architekturze.
-   [Poradnik do Środowiska pracy Arch](Arch_tutorial.md) *(v0.14)*.
-   [Szybki przegląd na blogu Yorika](http://yorik.uncreated.net/guestblog.php?2012=180) *(v0.13)*.
-   [Wideo prezentacja Środowiska pracy Arch](https://www.youtube.com/watch?v=lTDOeHapv_E) *(2016)*.
-   [Poradnik Arch panel](Arch_panel_tutorial.md) *(v0.15)*
-   [Rozdział z podręcznika FreeCAD dotyczący modelowania BIM](Manual_BIM_modeling.md)
-   [Import z formatu STL lub OBJ](Import_from_STL_or_OBJ.md)
-   [Eksport do formatu STL lub OBJ](Export_to_STL_or_OBJ.md)



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Arch Workbench/pl

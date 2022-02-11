# <img alt="Arch workbench icon" src=images/Workbench_Arch.svg  style="width:64px;"> Arch Workbench/pl


{{TOCright}}

## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Architektura](Arch_Workbench/pl.md) zapewnia [modelowanie informacji o budynku](http://en.wikipedia.org/wiki/Building_Information_Modeling) *(BIM)* nowoczesny przepływ pracy programu FreeCAD, z obsługą funkcjonalności takich jak w pełni parametryczne struktury architektoniczne obejmujące: ściany, elementy konstrukcyjne, dachy, okna, schody, rury i meble. Obsługuje on dane [branżowe klasy fundamentów](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) plików *([IFC](Arch_IFC.md))* oraz produkcję rzutów poziomych 2D w połączeniu z Środowiskiem pracy <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md).

Środowisko pracy Architektura importuje wszystkie narzędzia środowiska <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md), ponieważ używa obiektów 2D do budowy swoich przestrzennych obiektów architektonicznych. Niemniej jednak Arch może używać kształtów brył utworzonych w innych środowiskach pracy, takich jak <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md) i <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md).

Funkcjonalność BIM FreeCAD jest obecnie stopniowo poszerzana w obrębie Środowiska pracy Arch, który posiada podstawowe narzędzia architektoniczne, oraz <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [Środowisko pracy BIM](BIM_Workbench/pl.md), które można zainstalować za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md). Środowisko BIM dodaje nową warstwę interfejsu nad narzędziami Arch, w celu uczynienia przepływu BIM bardziej intuicyjnym i przyjaznym dla użytkownika. Zobacz [Przewodnik migracji FreeCAD BIM](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide).

Twórcy Draft, Arch i BIM współpracują również z większą [Społecznością OSArch](https://osarch.org), mając na uwadze ostateczny cel, jakim jest poprawa projektowania budynków przy użyciu całkowicie wolnego oprogramowania.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">

## Przybory

Są to narzędzia służące do tworzenia obiektów architektonicznych.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Ściana](Arch_Wall/pl.md): tworzy ścianę od podstaw lub wykorzystuje wybrany obiekt jako podstawę.
-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Ściana kurtynowa](Arch_CurtainWall/pl.md): tworzy od podstaw ścianę osłonową lub wykorzystuje wybrany obiekt jako podstawę. {{Version/pl|0.19}}
-   <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Element konstrukcyjny](Arch_Structure/pl.md): tworzy element konstrukcyjny od podstaw lub wykorzystując wybrany obiekt jako podstawę.

-   <img alt="" src=images/Arch_CompRebarStraight.png  style="width:48px;"> [Komponent pręty zbrojeniowe](Arch_CompRebarStraight/pl.md): dodatek do konstruowania zbrojeń powiększa zasobność środowiska pracy Architektura.
    -   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> [Pręty zbrojeniowe proste](Arch_Rebar_Straight/pl.md): w wybranym elemencie konstrukcji tworzy prosty pręt zbrojeniowy.
    -   <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> [Pręty zbrojeniowe typu U](Arch_Rebar_UShape/pl.md): w wybranym elemencie konstrukcji tworzy pręt zbrojeniowy w kształcie litery U.
    -   <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> [Pręty zbrojeniowe typu L](Arch_Rebar_LShape/pl.md): w wybranym elemencie konstrukcji tworzy pręt zbrojeniowy o kształcie litery L.
    -   <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> [Pręty zbrojeniowe wygięte](Arch_Rebar_BentShape/pl.md): w wybranym elemencie konstrukji tworzy pręt zbrojeniowy o kształcie ugiętym *(Bent Shape)*.
    -   <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> [Strzemiona](Arch_Rebar_Stirrup/pl.md): w wybranym elemencie konstrukcji tworzy pręt zbrojeniowy strzemion.
    -   <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> [Pręty zbrojeniowe spiralne](Arch_Rebar_Helical/pl.md): w wybranym elemencie konstrukcji tworzy spiralny pręt zbrojeniowy.
    -   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.png  style="width:32px;"> [Zbrojenie słupów](Arch_Rebar_ColumnReinforcement/pl.md): tworzy pręty zbrojeniowe wewnątrz obiektu konstrukcji słupa.
    -   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.png  style="width:32px;"> [Zbrojenie słupa dwa ściągi sześć prętów zbrojeniowych](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/pl.md): tworzy pręty zbrojeniowe wewnątrz obiektu konstrukcji słupa.
    -   <img alt="" src=images/Arch_Rebar_BeamReinforcement.png  style="width:32px;"> [Zbrojenie belek](Arch_Rebar_BeamReinforcement/pl.md): tworzy pręty zbrojeniowe wewnątrz obiektu konstrukcji dźwigara.
    -   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Pręt zbrojeniowy](Arch_Rebar/pl.md): na podstawie szkicu tworzy niestandardowy pręt zbrojeniowy w wybranym elemencie konstrukcji.

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Piętro](Arch_Floor/pl.md): tworzy podłogę z wybranymi obiektami.
-   <img alt="" src=images/Arch_BuildingPart.png  style="width:32px;"> [Część budynku](Arch_BuildingPart/pl.md): tworzy fragment budynku zawierający wybrane obiekty.
-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Budowla](Arch_Building/pl.md): tworzy budynek zawierający wybrane obiekty.
-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Teren](Arch_Site/pl.md): tworzy witrynę zawierającą wybrane obiekty.
-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Projekt](Arch_Project/pl.md): tworzy projekt zawierający wybrane obiekty.
-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Odniesienie](Arch_Reference/pl.md): łączy obiekty z innego pliku FreeCAD do bieżącego dokumentu.
-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Okno](Arch_Window/pl.md): tworzy okno z wykorzystaniem wybranego obiektu jako podstawy.
-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Płaszczyzna przekroju](Arch_SectionPlane/pl.md): dodaje obiekt płaszczyzny przekroju do dokumentu.

-   <img alt="" src=images/Arch_CompAxis.png  style="width:48px;"> [Narzędzia osi](Arch_CompAxis/pl.md): narzędzie Axis pozwala na umieszczenie szeregu osi w aktualnym dokumencie.
    -   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Osie](Arch_Axis/pl.md): dodaje 1-kierunkowy układ osi do dokumentu.
    -   <img alt="" src=images/Arch_AxisSystem.svg  style="width:32px;"> [Układ osi](Arch_AxisSystem/pl.md): dodaje do dokumentu układ osi składający się z kilku osi.
    -   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Siatka](Arch_Grid/pl.md): dodaje do dokumentu obiekt podobny do siatki.

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Dach](Arch_Roof/pl.md): tworzy dach skośny z wybranej płaszczyzny.
-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Kubatura](Arch_Space/pl.md): tworzy obiekt przestrzenny w dokumencie.
-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Schody](Arch_Stairs/pl.md): tworzy obiekt schodów w dokumencie.

-   <img alt="" src=images/Arch_CompPanel.png  style="width:48px;"> [Narzędzia panelu](Arch_CompPanel/pl.md): pozwala na budowanie wszelkiego rodzaju elementów przypominających panele.
    -   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Panel](Arch_Panel/pl.md): tworzy obiekt panelu z wybranego obiektu 2D.
    -   <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Panelizacja do cięcia](Arch_Panel_Cut/pl.md): tworzy widok cięcia 2D z panelu. {{Version/pl|0.17}}
    -   <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Arkusz panela](Arch_Panel_Sheet/pl.md): tworzy arkusz cięcia 2D wraz z cięciami paneli lub innych obiektów 2D. {{Version/pl|0.17}}
    -   <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Zagnieżdżanie](Arch_Nest/pl.md): umożliwia zagnieżdżenie kilku płaskich przedmiotów w kształcie kontenera. {{Version/pl|0.17}}

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Ramka](Arch_Frame/pl.md): tworzy obiekt ramki z wybranego układu.
-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Ogrodzenie](Arch_Fence/pl.md): tworzy obiekt ogrodzenia z wybranego słupka i ścieżki. {{Version/pl|0.19}}
-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Kratownica](Arch_Truss/pl.md): Tworzy kratownicę z wybranej linii począwszy od podstaw. {{Version/pl|0.19}}
-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Wyposażenie](Arch_Equipment/pl.md): tworzy wyposażenie lub obiekt umeblowania.
-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profil](Arch_Profile/pl.md): Tworzy parametryczny profil 2D. {{Version/pl|0.19}}

-   <img alt="" src=images/Arch_CompPipe.png  style="width:48px;"> [Narzędzia do rur](Arch_CompPipe/pl.md) <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Rura](Arch_Pipe/pl.md): Tworzy rurę. {{Version/pl|0.17}}
    -   <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Kształtka](Arch_PipeConnector/pl.md): tworzy połączenie typu kolanko lub trójnik pomiędzy 2 lub 3 wybranymi rurami. {{Version/pl|0.17}}

-   <img alt="" src=images/Arch_CompSetMaterial.png  style="width:48px;"> [Komponent ustaw materiał](Arch_CompSetMaterial/pl.md): narzędzia Materiałowe pozwalają na definiowanie materiałów w aktywnym dokumencie.
    -   <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Materiał](Arch_SetMaterial/pl.md): pozwala stworzyć materiał i przypisać go do wybranych obiektów, jeśli takie istnieją.
    -   <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Materiał złożony](Arch_MultiMaterial/pl.md): tworzy wielość materiałów i przypisuje je do wybranych obiektów, jeśli istnieją. {{Version/pl|0.17}}
-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Obmiar](Arch_Schedule/pl.md): tworzy różne rodzaje zestawień obmiarów.

### Narzędzia do modyfikacji 

Są to narzędzia służące do modyfikowania obiektów architektonicznych.

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Cięcie wzdłuż linii](Arch_CutLine/pl.md): Przetnij obiekt według linii. {{Version/pl|0.19}}
-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Cięcie płaszczyzną](Arch_CutPlane/pl.md): przetnij obiekt zgodnie z płaszczyzną.
-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Dodaj komponent](Arch_Add/pl.md): dodaje pozycje do elementu składowego.
-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Usuń komponent](Arch_Remove/pl.md): odejmuje lub usuwa pozycje z elementu składowego.
-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Spis wymiarów](Arch_Survey/pl.md): uruchamia lub zakańcza tryb pomiarowy.

### Przydatne narzędzia 

Są to dodatkowe narzędzia, które pomogą Ci w konkretnych zadaniach.

-   <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Komponent](Arch_Component/pl.md): tworzy nieparametryczny komponent architektoniczny.
-   <img alt="" src=images/Arch_Component_Clone.svg  style="width:32px;"> [Klonuj komponent](Arch_CloneComponent/pl.md): pozwala stworzyć komponenty architektury, które są klonami wybranych obiektów architektury *(nie należy mylić z funkcją [Draft: klonuj](Draft_Clone/pl.md))*.
-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Podziel siatkę](Arch_SplitMesh/pl.md): dzieli wybrane siatki na odrębne części składowe.
-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Siatka na kształt](Arch_MeshToShape/pl.md): przekształca siatkę na kształt, jednocząc powierzchnie współpłaszczyznowe.
-   <img alt="" src=images/Arch_SelectNonManifold.svg  style="width:32px;"> [Wybierz siatki typu non-solid](Arch_SelectNonSolidMeshes/pl.md): wybiera wszystkie niestałe siatki z bieżącego wyboru lub z dokumentu.
-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Usuń kształt](Arch_RemoveShape/pl.md): zmienia obiekt architektury oparty na kształcie sześcianu na w pełni parametryczny.
-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Zamknij otwory](Arch_CloseHoles/pl.md): zamyka otwory w wybranym obiekcie opartym na kształcie.
-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Połącz ściany](Arch_MergeWalls/pl.md): łączy dwie lub więcej ścian.
-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Sprawdź](Arch_Check/pl.md): sprawdza, czy zaznaczone obiekty są bryłami i nie zawierają defektów.
-   <img alt="" src=images/IFC.svg  style="width:32px;"> [Przeglądarka Ifc](Arch_IfcExplorer/pl.md): umożliwia przeglądanie zawartości plików typu [IFC](Arch_IFC/pl.md).
-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Przełącz flagę IFC Brep](Arch_ToggleIfcBrepFlag/pl.md): Wymusza wyeksportowanie wybranego obiektu jako [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).
-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [Trzy widoki](Arch_3Views/pl.md): tworzy widok od góry, od przodu i z boku dla [siatki](Mesh_Workbench/pl.md).
-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> [Arkusz kalkulacyjny IFC](Arch_IfcSpreadsheet/pl.md): tworzy arkusz kalkulacyjny do przechowywania własności obiektu [IFC](Arch_IFC/pl.md).
-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Przełącz widoczność odjęcia](Arch_ToggleSubs/pl.md): pokazuje lub ukrywa elementy składowe obiektu architektury.

### Ustawienia

-   <img alt="" src=images/Preferences-arch.svg  style="width:32px;"> [Preferences](Arch_Preferences.md): preferencje dotyczące domyślnego wyglądu ścian, konstrukcji, zbrojenia, okien, schodów, paneli, rur, siatek i osi.

### Formaty plików 

-   [IFC](Arch_IFC.md) : Industry foundation Classes.
-   [DAE](Arch_DAE.md) : format Collada dla siatek.
-   [OBJ](Arch_OBJ.md) : format Obj dla siatek *(tylko eksport)*.
-   [JSON](Arch_JSON.md) : format zapisu obiektu w JavaScript *(tylko eksport)*.
-   [3DS](Arch_3DS.md) : format 3DS *(tylko import)*.
-   [SHP](Arch_SHP.md): GIS Shapefiles *(tylko import)*.

## API

Moduł Arch może być używany w skryptach [Python](Python.md) i [makrodefiniacjach](Macros/pl.md) za pomocą funkcji [Arch Python API](Arch_API/pl.md).

## Poradniki

-   [Architecture workflow](http://yorik.uncreated.net/guestblog.php?tag=freecad): Przykład, w jaki sposób FreeCAD może zacząć zajmować pierwsze miejsce pod względem przepływu pracy w architekturze.
-   [Poradnik do Środowiska pracy Arch](Arch_tutorial.md) *(v0.14)*.
-   [Szybki przegląd na blogu Yorika](http://yorik.uncreated.net/guestblog.php?2012=180) *(v0.13)*.
-   [Wideo prezentacja Środowiska pracy Arch](https://www.youtube.com/watch?v=lTDOeHapv_E) *(2016)*.
-   [Poradnik Arch panel](Arch_panel_tutorial.md) *(v0.15)*
-   [Rozdział z podręcznika FreeCAD dotyczący modelowania BIM](Manual_BIM_modeling.md)
-   [Import z formatu STL lub OBJ](Import_from_STL_or_OBJ.md)
-   [Eksport do formatu STL lub OBJ](Export_to_STL_or_OBJ.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Arch](Category_Arch.md) > Arch Workbench/pl

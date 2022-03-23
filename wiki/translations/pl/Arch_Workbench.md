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

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Ściana](Arch_Wall/pl.md): Tworzy ścianę od podstaw lub używając wybranego obiektu jako podstawy.

-   <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Konstrukcja](Arch_Structure/pl.md): Tworzy element konstrukcyjny od podstaw lub używając wybranego obiektu jako podstawy.

-   <img alt="" src=images/Arch_CompRebarStraight.png  style="width:48px;"> [Narzędzia zbrojenia](Arch_CompRebarStraight/pl.md): Narzędzia te są dostępne tylko wtedy, gdy zainstalowano środowisko pracy [Zbrojenie](Reinforcement_Workbench/pl.md).

:\*<img alt="" src=images/Arch_Rebar_Straight.svg  style="width:32px;"> [Pręty zbrojeniowe proste](Arch_Rebar_Straight/pl.md): Tworzy prosty pręt zbrojeniowy w wybranym elemencie konstrukcyjnym.

-   <img alt="" src=images/Arch_Rebar_UShape.svg  style="width:32px;"> [Pręty zbrojeniowe typu U](Arch_Rebar_UShape/pl.md): Tworzy pręt zbrojeniowy w kształcie litery U w wybranym elemencie konstrukcyjnym.

:\* <img alt="" src=images/Arch_Rebar_LShape.svg  style="width:32px;"> [Pręty zbrojeniowe typu L](Arch_Rebar_LShape/pl.md): Tworzy pręt zbrojeniowy w kształcie litery L w wybranym elemencie konstrukcyjnym.

:\* <img alt="" src=images/Arch_Rebar_Stirrup.svg  style="width:32px;"> [Strzemiona zbrojeniowe](Arch_Rebar_Stirrup/pl.md): Tworzy pręt zbrojeniowy strzemion w wybranym elemencie konstrukcyjnym.

:\* <img alt="" src=images/Arch_Rebar_BentShape.svg  style="width:32px;"> [Pręty zbrojeniowe wygięte](Arch_Rebar_BentShape/pl.md): Tworzy pręt zbrojeniowy typu wygiętego w wybranym elemencie konstrukcyjnym.

:\* <img alt="" src=images/Arch_Rebar_Helical.svg  style="width:32px;"> [Pręty zbrojeniowe spiralne](Arch_Rebar_Helical/pl.md): Tworzy spiralny pręt zbrojeniowy w wybranym elemencie konstrukcyjnym.

:\* <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Pręty zbrojeniowe, zbrojenie słupów](Arch_Rebar_ColumnReinforcement/pl.md): Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym słupa prostokątnego.

:\* <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> [Pręty zbrojeniowe, zbrojenie belek](Arch_Rebar_BeamReinforcement/pl.md): Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym belki.

:\* <img alt="" src=images/Arch_Rebar_Slab_Reinforcement.svg  style="width:32px;"> [Pręty zbrojeniowe, zbrojenie płyt stropowych](Arch_Rebar_Slab_Reinforcement/pl.md): Tworzy pręty zbrojeniowe w wybranym elemencie konstrukcyjnym płyty.

:\* <img alt="" src=images/Arch_Rebar_Footing_Reinforcement.svg  style="width:32px;"> [Zbrojenie stóp fundamentowych](Arch_Rebar_Footing_Reinforcement/pl.md): Tworzy pręty zbrojeniowe wewnątrz obiektu konstrukcyjnego ławy fundamentowej.

:\* <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Pręt zbrojeniowy](Arch_Rebar/pl.md): Tworzy niestandardowy pręt zbrojeniowy w wybranym elemencie konstrukcyjnym za pomocą szkicu.

-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Ściana kurtynowa](Arch_CurtainWall/pl.md): Tworzy ścianę kurtynową od podstaw lub używając wybranego obiektu jako bazy. {{Version/pl|0.19}}

-   <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;"> [Część budowli - piętro](Arch_BuildingPart/pl.md): Tworzy część budynku zawierającą wybrane obiekty.

-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Projekt](Arch_Project/pl.md): Tworzy projekt zawierający wybrane obiekty.

-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Site](Arch_Site.md): Creates a site including selected objects.

-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Building](Arch_Building.md): Creates a building including selected objects.

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Level](Arch_Floor.md): Creates a floor including selected objects.

-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [External reference](Arch_Reference.md): Links objects from another FreeCAD file into the current document.

-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Window](Arch_Window.md): Creates a window from scratch or using a selected object as a base.

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Roof](Arch_Roof.md): Creates a sloped roof from a selected wire.

-   <img alt="" src=images/Arch_CompAxis.png  style="width:48px;"> [Axis tools](Arch_CompAxis.md)

:\* <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Axis](Arch_Axis.md): Adds a 1-direction array of axes.

:\* <img alt="" src=images/Arch_AxisSystem.svg  style="width:32px;"> [Axis System](Arch_AxisSystem.md): Adds an axis system composed of several axes.

:\* <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Grid](Arch_Grid.md): Adds a grid-like object.

-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Section Plane](Arch_SectionPlane.md): Adds a section plane object.

-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Space](Arch_Space.md): Creates a space object.

-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Stairs](Arch_Stairs.md): Creates a stairs object.

-   <img alt="" src=images/Arch_CompPanel.png  style="width:48px;"> [Panel tools](Arch_CompPanel.md)

:\* <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Panel](Arch_Panel.md): Creates a panel object from a selected 2D object.

:\* <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Panel Cut](Arch_Panel_Cut.md): Creates a 2D cut view from a panel.

:\* <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Panel Sheet](Arch_Panel_Sheet.md): Creates a 2D cut sheet including panel cuts or other 2D objects.

:\* <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Nest](Arch_Nest.md): Allows to nest several flat objects inside a container shape.

-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Equipment](Arch_Equipment.md): Creates an equipment or furniture object.

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Frame](Arch_Frame.md): Creates a frame object from a selected layout.

-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Fence](Arch_Fence.md): Creates a fence object from a selected post and path. <small>(v0.19)</small> 

-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Truss](Arch_Truss.md): Creates a truss from a selected line or from scratch. <small>(v0.19)</small> 

-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profile](Arch_Profile.md): Creates a parametric 2D profile. <small>(v0.19)</small> 

-   <img alt="" src=images/Arch_CompSetMaterial.png  style="width:48px;"> [Material tools](Arch_CompSetMaterial.md)

:\* <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Material](Arch_SetMaterial.md): Creates a material and attributes it to selected objects, if any.

:\* <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Multi-Material](Arch_MultiMaterial.md): Creates a multi-material and attributes it to selected objects, if any.

-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Schedule](Arch_Schedule.md): Creates different types of schedules.

-   <img alt="" src=images/Arch_CompPipe.png  style="width:48px;"> [Pipe tools](Arch_CompPipe.md)

:\* <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Pipe](Arch_Pipe.md): Creates a pipe.

:\* <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Connector](Arch_PipeConnector.md): Creates a corner or T-connection between 2 or 3 selected pipes.

### Narzędzia do modyfikacji 

Są to narzędzia służące do modyfikowania obiektów architektonicznych.

-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Cut with plane](Arch_CutPlane.md): Cuts an object according to a plane.

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Cut with line](Arch_CutLine.md): Cuts an object according to a line. <small>(v0.19)</small> 

-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Add component](Arch_Add.md): Adds objects to a component.

-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Remove component](Arch_Remove.md): Subtracts or removes objects from a component.

-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Survey](Arch_Survey.md): Enters or leaves surveying mode.

### Przydatne narzędzia 

Są to dodatkowe narzędzia, które pomogą Ci w konkretnych zadaniach.

-   <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Component](Arch_Component.md): Creates a non-parametric Arch component.

-   <img alt="" src=images/Arch_CloneComponent.svg  style="width:32px;"> [Clone component](Arch_CloneComponent.md): Produces Arch Components that are clones of selected Arch objects (not to be confused with [Draft Clone](Draft_Clone.md)).

-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Split Mesh](Arch_SplitMesh.md): Splits a selected mesh into separate components.

-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Mesh to Shape](Arch_MeshToShape.md): Converts a mesh into a shape, unifying coplanar faces.

-   <img alt="" src=images/Arch_SelectNonSolidMeshes.svg  style="width:32px;"> [Select non-manifold meshes](Arch_SelectNonSolidMeshes.md): Selects all non-manifold meshes from the current selection or from the document.

-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Remove Shape from Arch](Arch_RemoveShape.md): Turns cubic shape-based Arch object fully parametric.

-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Close holes](Arch_CloseHoles.md): Closes holes in a selected shape-based object.

-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Merge Walls](Arch_MergeWalls.md): Merge two or more walls.

-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Check](Arch_Check.md): Check if the selected objects are solids and don\'t contain defects.

-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Toggle IFC Brep flag](Arch_ToggleIfcBrepFlag.md): Forces a selected object to be exported as an [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).

-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [3 Views from mesh](Arch_3Views.md): Creates top, front and side views from a [mesh](Mesh_Workbench.md).

-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> [Create IFC spreadsheet\...](Arch_IfcSpreadsheet.md): Creates a spreadsheet to store [IFC](Arch_IFC.md) properties of an object.

-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Toggle subcomponents](Arch_ToggleSubs.md): Shows or hides the subcomponents of an Arch object.

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





{{Arch_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Arch Workbench/pl

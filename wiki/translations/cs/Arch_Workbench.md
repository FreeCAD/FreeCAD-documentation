


{{docnav/cs|[Workbenches/cs](Workbenches/cs.md)|[Draft Workbench/cs](Draft_Workbench/cs.md)|IconL=|IconR=Workbench_Draft.svg}}

<img alt="Arch workbench icon" src=images/Workbench_Arch.svg  style="width:128px;">


{{TOCright}}

Pracovní plocha Architektura poskytuje moderní [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) pracovní prostředí ve FreeCADu s možnostmi jako je podpora [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes), plně parametrizované stavební entity jako jsou zdi, strukturální prvky nebo okna a bohatá 2D dokumentace. Pracovní plocha Architektura také zahrnuje všechny nástroje [Pracovní plocha kreslení](Draft_Workbench/cs.md).

The <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch Workbench](Arch_Workbench.md) provides a modern [building information modelling](http://en.wikipedia.org/wiki/Building_Information_Modeling) (BIM) workflow to FreeCAD, with support for features like fully parametric architectural entities such as walls, beams, roofs, windows, stairs, pipes, and furniture. It supports industry foundation classes ([IFC](Arch_IFC.md)) files, and production of 2D floor plans in combination with the <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Workbench](TechDraw_Workbench.md).

The Arch Workbench imports all tools from the <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft Workbench](Draft_Workbench.md), as it uses its 2D objects to build 3D parametric architectural objects. Nevertheless, Arch can also use solid shapes created with other workbenches like <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench.md) and <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench.md).

The BIM functionality of FreeCAD is now progressively split into this Arch Workbench, which holds basic architectural tools, and the <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM Workbench](BIM_Workbench.md), which is available from the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md). This BIM Workbench adds a new interface layer on top of the Arch tools, with the aim of making the BIM workflow more intuitive and user-friendly. See [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide).

The developers of Draft, Arch, and BIM also collaborate with the greater [OSArch community](https://osarch.org), with the ultimate goal of improving building design by using entirely free software.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">

## Nástroje

Tyto nástroje slouží pro vytváření architektonických objektů.

-   <img alt="" src=images/Arch_Wall.png  style="width:32px;"> [Zeď](Arch_Wall/cs.md): Vytváří zeď buď od počátku nebo použitím vybraného objektu jako základu
-   <img alt="" src=images/Arch_Structure.png  style="width:32px;"> [Strukturální prvek](Arch_Structure/cs.md): Vytváří strukturální prvek buď od počátku nebo použitím vybraného objektu jako základu

-   <img alt="" src=images/Arch_Rebar.png  style="width:32px;"> [Překlad](Arch_Rebar/cs.md): Vytváří železobetonový překlad ve vybraném strukturálním prvku

-   <img alt="" src=images/Arch_Floor.png  style="width:32px;"> [Podlaží](Arch_Floor/cs.md): Vytváří podlaží zahrnutím vybraných objektů
-   <img alt="" src=images/Arch_Building.png  style="width:32px;"> [Budova](Arch_Building/cs.md): Vytváří budovu zahrnutím vybraných objektů
-   <img alt="" src=images/Arch_Site.png  style="width:32px;"> [Staveniště](Arch_Site/cs.md): Vytváří staveniště zahrnutím vybraných objektů
-   <img alt="" src=images/Arch_Window.png  style="width:32px;"> [Okno](Arch_Window/cs.md): Vytváří okno použitím vybraného objektu jako základu
-   <img alt="" src=images/Arch_SectionPlane.png  style="width:32px;"> [Řez](Arch_SectionPlane/cs.md): Přidává do dokumentu řez objektem

-   Axis tools
    -   <img alt="" src=images/Arch_Axis.png  style="width:32px;"> [Osový systém](Arch_Axis/cs.md): Přidává do dokumentu osový systém
    -   <img alt="" src=images/Arch_AxisSystem.png  style="width:32px;"> [Axes system](Arch_AxisSystem.md): Adds an axes system composed of several axes to the document
    -   <img alt="" src=images/Arch_Grid.png  style="width:32px;"> [Grid](Arch_Grid.md): Adds a grid-like object to the document

-   <img alt="" src=images/Arch_Roof.png  style="width:32px;"> [Střecha](Arch_Roof/cs.md): Vytváří šikmou střechu z vybrané plochy
-   <img alt="" src=images/Arch_Space.png  style="width:32px;"> [Prostor](Arch_Space/cs.md): Vytváří v dokumentu objekt prostoru
-   <img alt="" src=images/Arch_Stairs.png  style="width:32px;"> [Schodiště](Arch_Stairs/cs.md): Vytváří v dokumentu objekt schodiště

-   <img alt="" src=images/Arch_CompPanel.png  style="width:48px;"> [Panel tools](Arch_CompPanel.md): Allows you to build all kinds of panel-like elements.
    -   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Panel](Arch_Panel.md): Creates a panel object from a selected 2D object
    -   <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Panel Cut](Arch_Panel_Cut.md): Creates a 2D cut view from a panel <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Panel Sheet](Arch_Panel_Sheet.md): Creates a 2D cut sheet including panel cuts or other 2D objects <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Nest](Arch_Nest.md): Allow to nest several flat objects inside a container shape <small>(v0.17)</small> 

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Frame](Arch_Frame.md): Creates a frame object from a selected layout
-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Fence](Arch_Fence.md): Creates a fence object from a selected post and path. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Truss](Arch_Truss.md): Creates a truss from a selected line of from scratch. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Equipment](Arch_Equipment.md): Creates an equipment or furniture object
-   <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profile](Arch_Profile.md): Creates a parametric 2D profile. <small>(v0.19)</small> 

-   <img alt="" src=images/Arch_CompPipe.png  style="width:48px;"> [Pipe tools](Arch_CompPipe.md) <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Pipe](Arch_Pipe.md): Creates a pipe <small>(v0.17)</small> 
    -   <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Pipe Connector](Arch_PipeConnector.md): Creates a corner or tee connection between 2 or 3 selected pipes <small>(v0.17)</small> 

-   <img alt="" src=images/Arch_CompSetMaterial.png  style="width:48px;"> [Material tools](Arch_CompSetMaterial.md): The Material tools allows to add materials to the active document.
    -   <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Material](Arch_SetMaterial.md): Creates a material and attributes it to selected objects, if any
    -   <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Multi-Material](Arch_MultiMaterial.md): Creates a multi-material and attributes it to selected objects, if any <small>(v0.17)</small> 
-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Schedule](Arch_Schedule.md): Creates different types of schedules

### Modification tools {#modification_tools}

These are tools for modifying architectural objects.

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Cut with a line](Arch_CutLine.md): Cut an object according to a line. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Cut with plane](Arch_CutPlane.md): Cut an object according to a plane.
-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Add component](Arch_Add.md): Adds objects to a component
-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Remove component](Arch_Remove.md): Subtracts or removes objects from a component
-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Survey](Arch_Survey.md): Enters or leaves surveying mode

### Utilities

These are additional tools to help you in specific tasks.

-   <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Component](Arch_Component.md): Creates a non-parametric Arch component
-   <img alt="" src=images/Arch_CloneComponent.svg  style="width:32px;"> [Clone component](Arch_CloneComponent.md): Produces Arch Components that are clones of selected Arch objects (not to be confused with [Draft Clone](Draft_Clone.md))
-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Split Mesh](Arch_SplitMesh.md): Splits a selected mesh into separate components
-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Mesh To Shape](Arch_MeshToShape.md): Converts a mesh into a shape, unifying coplanar faces
-   <img alt="" src=images/Arch_SelectNonManifold.svg  style="width:32px;"> [Select non-solid meshes](Arch_SelectNonSolidMeshes.md): Selects all non-solid meshes from the current selection or from the document
-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Remove Shape](Arch_RemoveShape.md): Turns cubic shape-based arch object fully parametric
-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Close Holes](Arch_CloseHoles.md): Closes holes in a selected shape-based object
-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Merge Walls](Arch_MergeWalls.md): Merge two or more walls
-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Check](Arch_Check.md): Check if the selected objects are solids and don\'t contain defects
-   <img alt="" src=images/IFC.svg  style="width:32px;"> [Ifc Explorer](Arch_IfcExplorer.md): Browse the contents of an [IFC](Arch_IFC.md) file
-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Toggle IFC Brep flag](Arch_ToggleIfcBrepFlag.md): Forces a selected object to be exported as an [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).
-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [3 Views from mesh](Arch_3Views.md): Creates top, frontal and side views from a [mesh](Mesh_Workbench.md).
-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> [Create IFC spreadsheet\...](Arch_IfcSpreadsheet.md): Creates a spreadsheet to store [IFC](Arch_IFC.md) properties of an object
-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Toggle Subcomponents](Arch_ToggleSubs.md): Shows or hides the subcomponents of an Arch object.

### Preferences

-   <img alt="" src=images/Preferences-arch.svg  style="width:32px;"> [Preferences](Arch_Preferences.md): preferences for the default appearance of walls, structures, rebars, windows, stairs, panels, pipes, grids and axes.

### Souborové formáty {#souborové_formáty}

-   [IFC](Arch_IFC/cs.md) : Industry foundation Classes (pouze import)
-   [DAE](Arch_DAE/cs.md) : Síťový formát Collada
-   [OBJ](Arch_OBJ/cs.md) : Síťový formát Obj (pouze export)

## API

Modul Architektura může být použit v pythonovských skriptech a [makrech](macros/cs.md) použitím funkcí [Arch Python API](http://www.freecadweb.org/api/Arch.html).

## Výukový program {#výukový_program}

-   [Výukový program architektura](Arch_tutorial/cs.md)
-   [Architektonický výukový program v Yorikově blogu](http://yorik.uncreated.net/guestblog.php?2012=180)


{{docnav/cs|[Workbenches/cs](Workbenches/cs.md)|[Draft Workbench/cs](Draft_Workbench/cs.md)|IconL=|IconR=Workbench_Draft.svg}}


 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)

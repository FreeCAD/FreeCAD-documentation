# Arch Workbench/zh




{{docnav/zh|[Workbenches/zh](Workbenches/zh.md)|[Draft Workbench/zh](Draft_Workbench/zh.md)|IconL=|IconR=Workbench_Draft.svg}}

<img alt="Arch workbench icon" src=images/Workbench_Arch.svg  style="width:128px;">


{{TOCright}}

## 简介

建筑工作台在Freecad中提供了一个现代[建筑信息建模技术](http://en.wikipedia.org/wiki/Building_Information_Modeling) (BIM) 工作流，它支持特征参数建筑实体，如墙壁，结构元件，屋顶，窗户，楼梯，管道和家具等功能。它支持[建筑业国际工业标准](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) (IFC) 数据, 同时可以结合[技术制图工作台生成平面图](TechDraw_Workbench.md)。

The <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch Workbench](Arch_Workbench.md) provides a modern [building information modelling](http://en.wikipedia.org/wiki/Building_Information_Modeling) (BIM) workflow to FreeCAD, with support for features like fully parametric architectural entities such as walls, beams, roofs, windows, stairs, pipes, and furniture. It supports industry foundation classes ([IFC](Arch_IFC.md)) files, and production of 2D floor plans in combination with the <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Workbench](TechDraw_Workbench.md).

建筑工作台导入来自[草图工作台的所有工具](Draft_Workbench.md)，因为它使用2D对象来构建其建筑对象。然而，建筑工作台还可以使用其他如[零件工作台和](Part_Workbench.md)[零件设计工作台的其他工作台上创建的实体对象](partdesign_workbench.md)。

FreeCAD的[BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling)功能在逐步融入具有所有基础BIM工具和[BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling)插件的建筑工作台。你可以通过工具→插件管理器, 在建筑工具之上添加一个新的界面层，其目的是使得Freecad中的BIM工作流更加直观和用户友好。

The developers of Draft, Arch, and BIM also collaborate with the greater [OSArch community](https://osarch.org), with the ultimate goal of improving building design by using entirely free software.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">

## Tools

These are tools for creating architectural objects.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Wall](Arch_Wall.md): creates a wall from scratch or using a selected object as a base.
-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Curtain Wall](Arch_CurtainWall.md): creates a curtain wall from scratch or using a selected object as a base. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Structural element](Arch_Structure.md): creates a structural element from scratch or using a selected object as a base.

-   <img alt="" src=images/Arch_CompRebarStraight.png  style="width:48px;"> [Rebar tools](Arch_CompRebarStraight.md): the Reinforcement Addon augments the Arch Workbench Structures.
    -   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> [Straight Rebar](Arch_Rebar_Straight.md): creates a Straight reinforcement bar in a selected structural element.
    -   <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> [UShape Rebar](Arch_Rebar_UShape.md): creates a UShape reinforcement bar in a selected structural element.
    -   <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> [LShape Rebar](Arch_Rebar_LShape.md): creates a LShape reinforcement bar in a selected structural element.
    -   <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> [Bent Shape Rebar](Arch_Rebar_BentShape.md): creates a Bent Shape reinforcement bar in a selected structural element.
    -   <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> [Stirrup Rebar](Arch_Rebar_Stirrup.md): creates a Stirrup reinforcement bar in a selected structural element.
    -   <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> [Helical Rebar](Arch_Rebar_Helical.md): creates a Helical reinforcement bar in a selected structural element.
    -   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.png  style="width:32px;"> [ColumnReinforcement](Arch_Rebar_ColumnReinforcement.md): creates a reinforcing bars inside a Column Arch Structure object.
    -   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.png  style="width:32px;"> [ColumnReinforcement TwoTiesSixRebars](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars.md): creates a reinforcing bars inside a Column Arch Structure object.
    -   <img alt="" src=images/Arch_Rebar_BeamReinforcement.png  style="width:32px;"> [BeamReinforcement](Arch_Rebar_BeamReinforcement.md): creates reinforcing bars inside a Beam Arch Structure object.
    -   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Rebar](Arch_Rebar.md): creates a custom reinforcement bar in a selected structural element using a sketch.

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Floor](Arch_Floor.md): Creates a floor including selected objects
-   <img alt="" src=images/Arch_BuildingPart.png  style="width:32px;"> [Building Part](Arch_BuildingPart.md): Creates a building part including selected objects
-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Building](Arch_Building.md): Creates a building including selected objects
-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Site](Arch_Site.md): Creates a site including selected objects
-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Project](Arch_Project.md): Creates a project including selected objects
-   <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Reference](Arch_Reference.md): Links objects from another FreeCAD file into this document
-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Window](Arch_Window.md): Creates a window using a selected object as a base
-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Section Plane](Arch_SectionPlane.md): Adds a section plane object to the document

-   <img alt="" src=images/Arch_CompAxis.png  style="width:48px;"> [Axis tools](Arch_CompAxis.md): The Axis tool allows you to places a series of axes in the current document.
    -   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Axis](Arch_Axis.md): Adds a 1-direction array of axes to the document
    -   <img alt="" src=images/Arch_Axis_System.svg  style="width:32px;"> [Axes system](Arch_AxisSystem.md): Adds an axes system composed of several axes to the document
    -   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Grid](Arch_Grid.md): Adds a grid-like object to the document

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Roof](Arch_Roof.md): Creates a sloped roof from a selected face
-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Space](Arch_Space.md): Creates a space object in the document
-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Stairs](Arch_Stairs.md): Creates a stairs object in the document

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

### Modification tools 

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

### File formats 

-   [IFC](Arch_IFC.md): industry foundation classes
-   [DAE](Arch_DAE.md): Collada mesh format
-   [OBJ](Arch_OBJ.md): Obj mesh format (export only)
-   [JSON](Arch_JSON.md): JavaScript Object Notation format (export only)
-   [3DS](Arch_3DS.md): 3DS format (import only)
-   [SHP](Arch_SHP.md): GIS Shapefiles (import only)

## API

The Arch module can be used in [Python](Python.md) scripts and [macros](macros.md) using the [Arch Python API](http://www.freecadweb.org/api/Arch.html) functions.

## Tutorials

-   [Architecture workflow](http://yorik.uncreated.net/guestblog.php?tag=freecad): An example of how FreeCAD can begin to have its preliminary place in an architecture workflow.
-   [Arch tutorial](Arch_tutorial.md) (v0.14)
-   [Quick arch overview on Yorik\'s blog](http://yorik.uncreated.net/guestblog.php?2012=180) (v0.13)
-   [Video presentation of the Arch workbench](https://www.youtube.com/watch?v=lTDOeHapv_E) (2016)
-   [Arch panel tutorial](Arch_panel_tutorial.md) (v0.15)
-   [BIM modeling chapter from the FreeCAD manual](Manual:BIM_modeling.md)
-   [Import from STL or OBJ](Import_from_STL_or_OBJ.md)
-   [Export to STL or OBJ](Export_to_STL_or_OBJ.md)


{{docnav/zh|[Workbenches/zh](Workbenches/zh.md)|[Draft Workbench/zh](Draft_Workbench/zh.md)|IconL=|IconR=Workbench_Draft.svg}}


 

[Category:Workbenches](Category:Workbenches.md)

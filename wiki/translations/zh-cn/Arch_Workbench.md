# Arch Workbench/zh-cn






<img alt="Arch workbench icon" src=images/Workbench_Arch.svg  style="width:128px;">


{{TOCright}}

## 简介

建筑工作台为FreeCAD提供了一种现代化的[建筑信息模型（building information modelling）](http://en.wikipedia.org/wiki/Building_Information_Modeling) (BIM)工作流程，它支持的特性有完全参数化的建筑实体，如墙、结构构件、屋顶、窗口、台阶、管道与家具。建筑工作台还支持[建筑业国际工业标准（industry foundation classes）](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) (IFC) 数据，以及联合[TechDraw工作台制作](TechDraw_Workbench.md)2D平面布置图。

由于建筑工作台要利用2D对象来构建其建筑对象，因此，它导入了[底图工作台（Draft Workbench）中的所有工具](Draft_Workbench.md)。除此以外，建筑工作台亦可使用如[零件工具台（Part）与](Part_Workbench.md)[零件设计工作台（PartDesign）所创建的对象](PartDesign_Workbench.md)。

FreeCAD中的BIM功能正逐步拆分至此建筑工作台中，它持有基本的建筑体工具与[BIM Workbench](BIM_Workbench.md)，后者可以利用[Addon Manager进行安装](Std_AddonMgr.md)。本工作台在建筑工具（Arch tools）之上添加了一个新的接口层，目标是令FreeCAD中的BIM工作流程更为直观且更易于使用。

The developers of Draft, Arch, and BIM also collaborate with the greater [OSArch community](https://osarch.org), with the ultimate goal of improving building design by using entirely free software.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">

## 工具

以下这些工具用于创建建筑对象。

-   <img alt="" src=images/Arch_Wall.png  style="width:32px;"> [墙体（Wall）](Arch_Wall.md): 从零开始或以选中的对象为基础来创建一堵墙
-   <img alt="" src=images/Arch_Structure.png  style="width:32px;"> [结构构件（Structural element）](Arch_Structure.md): 从头开始或以选中的对象为基础来创建一个结构构件

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

### 修改工具

以下这些工具用于修改建筑对象。

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Cut with a line](Arch_CutLine.md): Cut an object according to a line. <small>(v0.19)</small> 
-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Cut with plane](Arch_CutPlane.md): Cut an object according to a plane.
-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Add component](Arch_Add.md): Adds objects to a component
-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Remove component](Arch_Remove.md): Subtracts or removes objects from a component
-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Survey](Arch_Survey.md): Enters or leaves surveying mode

### 实用工具

以下这些工具可助您实现一些特定任务。

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

### 首选项

-   <img alt="" src=images/Preferences-arch.svg  style="width:32px;"> [建筑工作台首选项（Preferences）](Arch_Preferences.md): 针对墙体、构件、钢筋、窗口、台阶、面板、管道、网格与坐标轴默认外观的设置首选项。

### 文件格式

-   [IFC](Arch_IFC.md) : 建筑业国际工业标准（Industry foundation Classes）
-   [DAE](Arch_DAE.md) : Collada网格格式
-   [OBJ](Arch_OBJ.md) : Obj网格格式 (仅限于导出)
-   [JSON](Arch_JSON.md) : JavaScript对象表示法格式 (仅限于导出)
-   [3DS](Arch_3DS.md) : 3DS格式 (仅限于导入)

## API

在[Python脚本与](Python.md)[宏（macros）中调用](macros.md)[Arch Python API](http://www.freecadweb.org/api/Arch.html)函数即可使用本建筑模块。

## 教程

-   [Architecture workflow](http://yorik.uncreated.net/guestblog.php?tag=freecad): An example of how FreeCAD can begin to have its preliminary place in an architecture workflow.
-   [Arch tutorial](Arch_tutorial.md) (v0.14)
-   [Quick arch overview on Yorik\'s blog](http://yorik.uncreated.net/guestblog.php?2012=180) (v0.13)
-   [Video presentation of the Arch workbench](https://www.youtube.com/watch?v=lTDOeHapv_E) (2016)
-   [Arch panel tutorial](Arch_panel_tutorial.md) (v0.15)
-   [BIM modeling chapter from the FreeCAD manual](Manual:BIM_modeling.md)
-   [Import from STL or OBJ](Import_from_STL_or_OBJ.md)
-   [Export to STL or OBJ](Export_to_STL_or_OBJ.md)


{{docnav/zh-cn|[Workbenches/zh-cn](Workbenches/zh-cn.md)|[Draft Workbench/zh-cn](Draft_Workbench/zh-cn.md)|IconL=|IconR=Workbench_Draft.svg}}


 

[Category:Workbenches](Category:Workbenches.md)

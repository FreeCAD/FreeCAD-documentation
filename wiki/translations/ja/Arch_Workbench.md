# Arch Workbench/ja
{{docnav/ja|[Workbenches/ja](Workbenches/ja.md)|[Draft Module/ja](Draft_Workbench/ja.md)|IconL=|IconR=Workbench_Draft.svg}}

<img alt="Arch workbench icon" src=images/Workbench_Arch.svg  style="width:128px;">


{{TOCright}}

建築ワークベンチによって近代的なBIMワークフローをFreeCADで使用することができます。IFCサポート、壁や構造要素や窓といった完全にパラメトリックな建築物の構成要素、優れた2Dドキュメント制作といった機能がサポートされています。また建築ワークベンチでは製図ワークベンチの全てのツールが使用できます。

The <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch Workbench](Arch_Workbench.md) provides a modern [building information modelling](http://en.wikipedia.org/wiki/Building_Information_Modeling) (BIM) workflow to FreeCAD, with support for features like fully parametric architectural entities such as walls, beams, roofs, windows, stairs, pipes, and furniture. It supports industry foundation classes ([IFC](Arch_IFC.md)) files, and production of 2D floor plans in combination with the <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Workbench](TechDraw_Workbench.md).

The Arch Workbench imports all tools from the <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft Workbench](Draft_Workbench.md), as it uses its 2D objects to build 3D parametric architectural objects. Nevertheless, Arch can also use solid shapes created with other workbenches like <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench.md) and <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench.md).

建築ワークベンチによって近代的な[BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling)ワークフローをFreeCADで使用することができます。[IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes)サポート、壁や構造要素や窓といった完全にパラメトリックな建築物の構成要素、優れた2Dドキュメント制作といった機能がサポートされています。また建築ワークベンチでは[製図ワークベンチの全てのツールが使用できます](Draft_Workbench/jp.md)。

The developers of Draft, Arch, and BIM also collaborate with the greater [OSArch community](https://osarch.org), with the ultimate goal of improving building design by using entirely free software.

<img alt="" src=images/Screenshot_arch_window.jpg  style="width:600px;">

### 構築用ツール

建築用オブジェクトを作成するためのツールです。

-   <img alt="" src=images/Arch_Wall.png  style="width:32px;"> [壁](Arch_Wall/jp.md): 選択されているオブジェクトを基礎として壁を作成します
-   <img alt="" src=images/Arch_Structure.png  style="width:32px;"> [構造要素](Arch_Structure/jp.md): 選択されているオブジェクトを基礎として構造要素を作成します

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

-   <img alt="" src=images/Arch_Floor.png  style="width:32px;"> [床](Arch_Floor/jp.md): 選択されているオブジェクトを含む床を作成します
-   <img alt="" src=images/Arch_Building.png  style="width:32px;"> [Building](Arch_Building/jp.md): 選択されているオブジェクトを含む建造物を作成します
-   <img alt="" src=images/Arch_Site.png  style="width:32px;"> [サイト](Arch_Site/jp.md): 選択されているサイトを含む建造物を作成します
-   <img alt="" src=images/Arch_Window.png  style="width:32px;"> [窓](Arch_Window/jp.md): 選択されているオブジェクトを基礎として使って窓を作成します
-   <img alt="" src=images/Arch_SectionPlane.png  style="width:32px;"> [断面](Arch_SectionPlane/jp.md): ドキュメントに断面を追加します


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Arch_Axis.png  style="width:32px;"> [座標系](Arch_Axis/jp.md): ドキュメントに座標系を追加します


</div>

-   <img alt="" src=images/Arch_Roof.png  style="width:32px;"> [屋根](Arch_Roof/jp.md): 選択されている面から傾斜屋根を作成します

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

### 修正用ツール

These are tools for modifying architectural objects.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Arch_Add.png  style="width:32px;"> [追加](Arch_Add/jp.md): 構成要素にオブジェクトを追加します
-   <img alt="" src=images/Arch_Remove.png  style="width:32px;"> [削除](Arch_Remove/jp.md): 構成要素からオブジェクトを減算したり削除したりします


</div>

### ユーティリティ

特定の作業を補助するための付加的なツールです。

-   <img alt="" src=images/Arch_SplitMesh.png  style="width:32px;"> [メッシュの分割](Arch_SplitMesh/jp.md): 選択されているメッシュを別々の構成要素に分割します
-   <img alt="" src=images/Arch_MeshToShape.png  style="width:32px;"> [メッシュからシェイプへ](Arch_MeshToShape/jp.md): 同一面を統合しつつメッシュをシェイプに変換します
-   <img alt="" src=images/Arch_RemoveShape.png  style="width:32px;"> [シェイプの削除](Arch_RemoveShape/jp.md): 三次元シェイプベースの建築オブジェクトを完全にパラメトリックなものに変えます
-   <img alt="" src=images/Arch_SelectNonSolidMeshes.png  style="width:32px;"> [非ソリッドなメッシュを選択](Arch_SelectNonSolidMeshes/jp.md): 現在の選択オブジェクトまたはドキュメントから全ての非ソリッドなメッシュを選択します
-   <img alt="" src=images/Arch_CloseHoles.png  style="width:32px;"> [穴埋め](Arch_CloseHoles/jp.md): 選択されているシェイプベースオブジェクトの穴を埋めます
-   <img alt="" src=images/Arch_Check.png  style="width:32px;"> [検証](Arch_Check/jp.md): 選択されているオブジェクトが欠陥を含んでいないソリッドであるかどうかをチェックします

### Preferences

-   <img alt="" src=images/Preferences-arch.svg  style="width:32px;"> [Preferences](Arch_Preferences.md): preferences for the default appearance of walls, structures, rebars, windows, stairs, panels, pipes, grids and axes.

### ファイル形式

-   [IFC](Arch_IFC/jp.md) : Industry Foundation Classes形式（インポートのみ）
-   [DAE](Arch_DAE/jp.md) : Colladaメッシュ形式
-   [OBJ](Arch_OBJ/jp.md) : Objメッシュ形式（エクスポートのみ）

## API

The Arch module can be used in [Python](Python.md) scripts and [macros](Macros.md) using the [Arch Python API](Arch_API.md) functions.

## Tutorials

-   [Architecture workflow](http://yorik.uncreated.net/guestblog.php?tag=freecad): An example of how FreeCAD can begin to have its preliminary place in an architecture workflow.
-   [Arch tutorial](Arch_tutorial.md) (v0.14)
-   [Quick arch overview on Yorik\'s blog](http://yorik.uncreated.net/guestblog.php?2012=180) (v0.13)
-   [Video presentation of the Arch workbench](https://www.youtube.com/watch?v=lTDOeHapv_E) (2016)
-   [Arch panel tutorial](Arch_panel_tutorial.md) (v0.15)
-   [BIM modeling chapter from the FreeCAD manual](Manual_BIM_modeling.md)
-   [Import from STL or OBJ](Import_from_STL_or_OBJ.md)
-   [Export to STL or OBJ](Export_to_STL_or_OBJ.md)


{{docnav/ja|[Workbenches/ja](Workbenches/ja.md)|[Draft Module/ja](Draft_Workbench/ja.md)|IconL=|IconR=Workbench_Draft.svg}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Arch](Category_Arch.md) > Arch Workbench/ja

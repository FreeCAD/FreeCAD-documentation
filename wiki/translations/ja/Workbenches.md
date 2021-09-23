# Workbenches/ja



<div class="mw-translate-fuzzy">

[Revitや](wikipedia:Revit.md)[Catiaといった多くの現代的なデザインのためのアプリケーションと同様](wikipedia:CATIA.md)、FreeCADは[ワークベンチというコンセプトを基盤にしています](wikipedia:Workbench.md)。ワークベンチとは言うなれば特定の作業のために特別に編成されたツールのセットです。伝統的な家具工房では木材を扱う者のための作業台や金属部品を扱う者のための作業台があり、恐らくは全ての部品を一つに組み立てる者のための作業台もあったことでしょう。


</div>

FreeCAD, like many modern design applications such as [Revit](wikipedia:Revit.md) or [CATIA](wikipedia:CATIA.md), is based on the concept of [Workbench](wikipedia:Workbench.md). A workbench can be considered as a set of tools specially grouped for a certain task. In a traditional furniture workshop, you would have a work table for the person who works with wood, another one for the one who works with metal pieces, and maybe a third one for the guy who mounts all the pieces together.

FreeCADでは同じ考え方を採用しています。関係する作業に従ってツールはワークベンチにグループ化されているのです。

あるワークベンチから別のワークベンチに切り替えると、そのインタフェースで利用できるツールが変わります。

ワークベンチを切り替えるとインターフェイスが変わってそのツールが利用可能になります。ツールバー、コマンドバー、さらにはインターフェイスの他の部分も新しいワークベンチに切り替わりますが、シーンの内容は変わりません。例えば製図ワークベンチで2D形状を描画し、さらにパートワークベンチを使ってそこから作業を続けるといったことが可能です。


<div class="mw-translate-fuzzy">

ワークベンチは「モジュール」と呼ばれることがあります。ただし、ワークベンチとモジュールは別のエンティティです。モジュールはFreeCADを拡張したものですが、ワークベンチはツールバーやメニューをまとめた特別なGUI設定です。通常、すべてのモジュールには独自のワークベンチが含まれているため、名前を交差使用しています。


</div>

## ビルトインワークベンチ


<div class="mw-translate-fuzzy">

今のところ以下のワークベンチが利用可能になっています：


</div>

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Base](Std_Base.md). This is not really a workbench, but rather a category of \'standard\' commands and tools that can be used in all workbenches.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> The [Arch Workbench](Arch_Workbench.md) for working with architectural elements.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> The [FEM Workbench](FEM_Workbench.md) provides Finite Element Analysis (FEA) workflow.

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> The [Image Workbench](Image_Workbench.md) for working with bitmap images.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> The [Inspection Workbench](Inspection_Workbench.md) is made to give you specific tools for examination of shapes. It is still under development.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> The [Mesh Workbench](Mesh_Workbench.md) for working with triangulated meshes.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> The [OpenSCAD Workbench](OpenSCAD_Workbench.md) for interoperability with OpenSCAD and repairing [constructive solid geometry](constructive_solid_geometry.md) (CSG) model history.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> The [Part Workbench](Part_Workbench.md) for working with CAD parts.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> The [Part Design Workbench](PartDesign_Workbench.md) for building Part shapes from sketches.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> The [Path Workbench](Path_Workbench.md) is used to produce G-Code instructions. It is still under development.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> The [Points Workbench](Points_Workbench.md) for working with point clouds.

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> The [Raytracing Workbench](Raytracing_Workbench.md) for working with ray-tracing (rendering).

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> The [Reverse Engineering Workbench](Reverse_Engineering_Workbench.md) is intended to provide specific tools to convert shapes/solids/meshes into parametric FreeCAD-compatible features. It is still under development.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> The [Robot Workbench](Robot_Workbench.md) for studying robot movements.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> The [Sketcher Workbench](Sketcher_Workbench.md) for working with geometry-constrained sketches.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> The [Spreadsheet Workbench](Spreadsheet_Workbench.md) for creating and manipulating spreadsheet data.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> The [Start Center Workbench](Start_Workbench.md) allows you to quickly jump to one of the most common workbenches.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar as the Part Shape builder Face from edges.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models. It is the successor of the [Drawing Workbench](Drawing_Workbench.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> The [Web Workbench](Web_Workbench.md) provides you with a browser window instead of the [3D view](3D_view.md) within FreeCAD.

### Deprecated

The following workbenches are still included in the base installation for compatibility purposes, but they should no longer be used.

-   <img alt="" src=images/Workbench_Complete.svg  style="width:32px;"> The [Complete Workbench](Complete_Workbench.md) holds all commands and features from all workbenches that met certain quality criteria. {{Obsolete|0.17}}

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> The [Drawing Workbench](Drawing_Workbench.md) was used for producing technical drawings but has now been deprecated. It is still needed to read old FreeCAD files that contain objects created with this workbench. The [TechDraw Workbench](TechDraw_Workbench.md) is its more advanced replacement. {{Obsolete|0.17}}

## External workbenches 


<div class="mw-translate-fuzzy">

FreeCADワークベンチは[Pythonでプログラムするのが簡単です](Python.md)。したがって、FreeCADの主な開発者の外に追加のワークベンチを開発する人がいます。


</div>

The [external workbenches](external_workbenches.md) page lists all that are known to this community. Most are easily installable from within FreeCAD, using the [Addon Manager](Addon_Manager.md), found under menu **Tools → <img src="images/AddonManager.svg" width=24px> Addon manager**.


<div class="mw-translate-fuzzy">

複数の新しいワークベンチが開発中です。お楽しみに！


</div>


<div class="mw-translate-fuzzy">


{{docnav/jp|Property/jp|Mesh Module/jp}}


</div>




[Category:Workbenches](Category:Workbenches.md)

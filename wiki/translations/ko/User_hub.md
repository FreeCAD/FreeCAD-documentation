# User hub/ko
{{TOCright}} <img alt="" src=images/User_hub.png  style="width:64px;">



이건 FreeCAD에 처음 온 사람을 위한 주요 도움 영역입니다.


<div class="mw-translate-fuzzy">

FreeCAD 자체처럼, 이 페이지는 계속 개발중이며, 빠지거나 틀린 정보가 있을 수 있습니다.


</div>


<div class="mw-translate-fuzzy">

FreeCAD에 기여하고 싶다면, [Help FreeCAD](Help_FreeCAD.md) 페이지를 보세요. 이 위키를 편집하고 싶다면,[포럼](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830)에서 편집권한을 갖는 위키 계정을 요청하고, 따라야 하는 일반 규칙을 위해 [위키 페이지를](WikiPages.md) 읽으세요.


</div>

몇 년 전에 FreeCAD가 어떻게 시작되었는지 알고 싶으면 [ History](History.md) 페이지를 방문하세요.

## FreeCAD 사용하기 

### 소개


<div class="mw-translate-fuzzy">

-   [Application Overview](About_FreeCAD.md): A general overview of FreeCAD
-   [Installing](Installing.md): How to install FreeCAD on [Windows](Install_on_Windows.md), [Linux](Install_on_Linux.md) and [Mac](Install_on_Mac.md)
-   [Installing help files](Installing_Helpfile.md): how to install the offline documentation which is based on this wiki.
-   [Getting started](Getting_started.md): A quick overview of the available tools
-   [FAQ](FAQ.md): Frequently asked questions
-   [Tutorials](Tutorials.md) covering different parts of FreeCAD


</div>

#### Migrating from other software? 

-   [Workarounds](Workarounds.md)
-   [Migrating to FreeCAD from Fusion360](Migrating_to_FreeCAD_from_Fusion360.md)
-   [Migrating to FreeCAD from OnShape](Migrating_to_FreeCAD_from_OnShape.md)
-   [Migrating to FreeCAD from SolidWorks](Migrating_to_FreeCAD_from_SolidWorks.md)
-   [Migrating to FreeCAD from Revit](Migrating_to_FreeCAD_from_Revit.md)
-   [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide)
-   [BIM applications compatibility table](BIM_application_compatibility_table.md)


<div class="mw-translate-fuzzy">

### 기본 응용프로그램 


</div>

-   [Interface](Interface.md): the FreeCAD interface is composed of various graphical elements on the screen, including the [3D view](3D_view.md), the [tree view](Tree_view.md), the [property editor](Property_editor.md), the [task panel](Task_panel.md), and the [Python console](Python_console.md).
-   [Mouse navigation](Mouse_navigation.md): the different types of using the mouse or trackpad to navigate in the 3D view.
-   [Selection methods](Selection_methods.md): the different methods of selecting objects in the software.
-   [Objects naming](Object_name.md): FreeCAD objects have a read-only `Name` that uniquely identifies them, and a `Label` which is user editable.
-   [Preferences Editor](Preferences_Editor.md): the system that allows you to control many properties of the base system and of the individual workbenches.
-   [File formats](Import_Export.md): the different file formats that FreeCAD can read and write.

### Workbenches

[Workbenches](Workbenches.md) are collections of tools used for specific tasks. These are the base workbenches bundled with every FreeCAD installation:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Standard tools](Std_Base.md). These commands and tools are present in all workbenches.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> The [Arch Workbench](Arch_Workbench.md) for working with architectural elements.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> The [FEM Workbench](FEM_Workbench.md) provides Finite Element Analysis (FEA) workflow.

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> The [Image Workbench](Image_Workbench.md) for working with bitmap images.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> The [Inspection Workbench](Inspection_Workbench.md) is made to give you specific tools for examination of shapes. It is still under development.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> The [Mesh Workbench](Mesh_Workbench.md) for working with triangulated meshes.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> The [OpenSCAD Workbench](OpenSCAD_Workbench.md) for interoperability with OpenSCAD and repairing [constructive solid geometry](Constructive_solid_geometry.md) (CSG) model history.

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

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar to the [Part Builder](Part_Builder.md) Face from edges option.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models. It is the successor of the [Drawing Workbench](Drawing_Workbench.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> The [Web Workbench](Web_Workbench.md) provides you with a browser window instead of the [3D view](3D_view.md) within FreeCAD.

### Macros

[Macros](Macros.md) are relatively small snippets of [Python](Python.md) code that perform a simple or a complex task that is not available in the base FreeCAD system.

Power users have written various [macros](macros.md) to enhance FreeCAD with more capabilities.

Since FreeCAD 0.17, many macros can be installed using the [Addon Manager](Std_AddonMgr.md). For a list of the macros refer to the [Macros recipes](Macros_recipes.md) page. For manual installation see [How to install macros](How_to_install_macros.md).

### External workbenches 

When many macros or functions are developed together, and are organized in toolbars and menus, they can become a new workbench.

[External workbenches](External_workbenches.md) are collections of functions that are not part of the base FreeCAD system, usually developed by experienced users, and targeting a particular need.

Since FreeCAD 0.17, many workbenches can be installed using the [Addon Manager](Std_AddonMgr.md). For manual installation see [How to install additional workbenches](How_to_install_additional_workbenches.md).

## 참조


<div class="mw-translate-fuzzy">

-   [Commands Reference](List_of_Commands.md): FreeCAD 명령어의 완전한 목록.


</div>

## 온라인 도움 

This is the official FreeCAD online help. Please note that the whole online help system is currently being reworked. It will be used to generate a .CHM file, that will be distributed with the binary packages of FreeCAD. At the moment the online help summarizes some of the most complete sections of this wiki.

-   [Online help system - Table of Contents](Online_Help_Toc.md)

## 좀 더 


<div class="mw-translate-fuzzy">

-   The [Power users hub](Power_users_hub.md) is the place to go if you would like to see more advanced use of FreeCAD
-   The [FreeCAD Community Portal](FreeCAD_Community_Portal.md) lists projects made by community members around FreeCAD.
-   FreeCAD 용어를 이해 못하시면? [어휘](Glossary.md) 페이지를 보세요.


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Hubs](Category_Hubs.md) > User hub/ko

# Manual:The FreeCAD Interface/zh-cn
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

FreeCAD 使用 [Qt 框架](https://en.wikipedia.org/wiki/Qt_(software))来绘制和管理其界面。这个框架被广泛应用于各种应用程序，因此 FreeCAD 的界面非常经典，没有特别难以理解的地方。大多数按钮都是标准的，可以在你期望的位置找到，例如 **文件 → 打开，编辑 → 粘贴** 等。下面是你第一次打开安装后的 FreeCAD 时的界面，显示了启动中心的外观：


</div>


<div class="mw-translate-fuzzy">

![](images/FreeCAD-v0-18-FirstStart.png )


</div>


<div class="mw-translate-fuzzy">

启动中心是一个方便的 \"欢迎界面\"，为新进入的客人提供有用的信息，比如你最近打开过的文件、FreeCAD 世界的最新内容，或者常用工作台的快速信息。它还会通知你是否有新的稳定版本的 FreeCAD 可用。


</div>


<div class="mw-translate-fuzzy">

一段时间后，当你更熟悉 FreeCAD 时，你可能会在偏好设置中进行了更改，这样当 FreeCAD 启动时，你会直接进入一个工作台并打开一个新文档。或者，你可以简单地关闭开始页面标签并创建一个新文档：


</div>


<div class="mw-translate-fuzzy">

![](images/FreeCAD-v0-18-NewProject.png )


</div>



### 工作台


<div class="mw-translate-fuzzy">

工作台是一组按照专业领域划分的工具（工具栏按钮、菜单和其他界面控件）。可以将其想象为一个工作室，其中有不同的人一起工作：一个人处理金属，另一个人处理木材。每个人在自己的工作室里有一张专门用于自己工作的桌子和特定的工具。然而，他们都可以在同一对象上工作。在 FreeCAD 中也是如此。


</div>

In the context of FreeCAD, each Workbench is tailored to a particular type of task, organizing all the necessary tools for that activity in one interface. When switching between Workbenches, the set of tools and controls visible in the user interface adjusts to reflect the needs of the selected task, though the actual project contents or \"scene\" you are working on does not change. This allows for seamless transitions in workflow, such as beginning a design with basic 2D shapes in the Draft Workbench and then elaborating on these designs with advanced modeling tools in the Part Workbench.

The terms \"Workbench\" and \"Module\" are sometimes used interchangeably, but they have distinct meanings within FreeCAD. A Module is any extension that adds functionality to FreeCAD, while a Workbench is a specific kind of Module equipped with its own user interface components such as toolbars and menus, designed to facilitate specific types of tasks. Thus, every Workbench is a Module, but not every Module qualifies as a Workbench.

FreeCAD 界面中最重要的控件是工作台选择器，您可以使用它来在不同的工作台之间进行切换：


<div class="mw-translate-fuzzy">

![](images/FreeCAD-v0-18-WorkbenchMenu.png )


</div>

-   <img alt="" src=images/Workbench_Assembly.svg  style="width:32px;"> The [Assembly Workbench](Assembly_Workbench.md) for building and solving mechanical assemblies. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_BIM.svg  style="width:32px;"> The [BIM Workbench](BIM_Workbench.md) for working with architectural elements and creating [BIM](https://en.wikipedia.org/wiki/Building_information_modeling) models. It combines the Arch Workbench and the formerly external BIM Workbench available in {{VersionMinus|0.21}}.

-   <img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> The [CAM Workbench](CAM_Workbench.md) is used to produce G-Code instructions. This workbench was called \"Path Workbench\" in {{VersionMinus|0.21}}.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> The [FEM Workbench](FEM_Workbench.md) provides Finite Element Analysis (FEA) workflow.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> The [Inspection Workbench](Inspection_Workbench.md) is made to give you specific tools for the examination of shapes. Still in the early stages of development.

-   <img alt="" src=images/Workbench_Material.svg  style="width:32px;"> The [Material Workbench](Material_Workbench.md) handles the FreeCAD material system. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> The [Mesh Workbench](Mesh_Workbench.md) for working with triangulated meshes.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> The [OpenSCAD Workbench](OpenSCAD_Workbench.md) for interoperability with OpenSCAD and repairing [constructive solid geometry](Constructive_solid_geometry.md) (CSG) model history.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> The [Part Workbench](Part_Workbench.md) for working with geometric primitives and boolean operations.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> The [Part Design Workbench](PartDesign_Workbench.md) for building Part shapes from sketches.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> The [Points Workbench](Points_Workbench.md) for working with point clouds.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> The [Reverse Engineering Workbench](Reverse_Engineering_Workbench.md) is intended to provide specific tools to convert shapes/solids/meshes into parametric FreeCAD-compatible features.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> The [Robot Workbench](Robot_Workbench.md) for studying robot movements. Currently unmaintained.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> The [Sketcher Workbench](Sketcher_Workbench.md) for working with geometry-constrained sketches.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> The [Spreadsheet Workbench](Spreadsheet_Workbench.md) for creating and manipulating spreadsheet data.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar to the [Part Builder](Part_Builder.md) Face from edges option.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models. It is the successor of the [Drawing Workbench](Drawing_Workbench.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.


<div class="mw-translate-fuzzy">

对于新用户来说，工作台经常会引起困惑，因为很难确定在哪个工作台中能找到特定的工具。但是一旦熟悉了，就会感觉自然而然，因为这是一种方便的方式来组织 FreeCAD 提供的众多工具。工作台也是完全可定制的（见下文）。同一个工具可能会出现在多个工作台中。无论工具出现在哪个工作台中，其按钮图标始终相同。


</div>



### 界面

让我们更仔细地看一下界面的各个部分：


<div class="mw-translate-fuzzy">

![](images/FreeCAD-v0-18-Cube.png )


</div>

The main window of the application can be roughly divided into 11 sections:

1.  The [Main view area](Main_view_area.md), which can contain different tabbed windows.
2.  The [3D view](3D_view.md), normally embedded in the [main view area](Main_view_area.md). The 3D view is the central element of the interface, displaying and allowing manipulation of the objects you are working on. It is possible to have multiple views of the same document (or objects) or to have several documents open simultaneously. Additionally, each view can be detached from the main window separately.
3.  The Model and and the [Tasks](Task_panel.md) tab.
    1.  The Model tab shows you the contents and structure of your document.
    2.  The Tasks tab is where FreeCAD will prompt you for values specific to the workbench and tool you are currently using (for example dimensions of an object).
4.  The [Property editor](Property_editor.md) which appears when the Model tab is active in the interface. It allows managing the publicly exposed properties of the objects in the document. It consists of the Data and View sections, showing the visualization properties and the parametric properties of the objects respectively.
5.  The [Selection view](Selection_view.md) which indicates the objects or sub-elements of objects (vertices, edges, faces) that are selected.
6.  The [Report view](Report_view.md) where messages, warnings and errors are shown.
7.  The [Python console](Python_console.md).The Python console, where all the commands executed are printed, and where you can enter Python code.
8.  The [Status bar](Status_bar.md) where some messages and tooltips appear.
9.  The toolbar area, where the toolbars are docked.
10. The [workbench selector](Std_Workbench.md), where you select the active [workbench](Workbenches.md).
11. The [standard menu](Standard_Menu.md), which holds basic operations of the program.

Most of the above panels can be hidden or revealed using the **View → Panels menu**



### 自定义界面


<div class="mw-translate-fuzzy">

FreeCAD 提供了深度可自定义的界面。所有面板和工具栏可以移动到不同的位置或堆叠在一起。它们也可以通过"视图"菜单或右键单击界面的空白区域在需要时关闭和重新打开。除此之外，还有许多其他选项可供使用，例如创建包含来自任何工作台的工具的自定义工具栏，或者分配和更改键盘快捷键。


</div>

这些高级自定义选项可以在**工具 → 自定义菜单**中找到：


<div class="mw-translate-fuzzy">

![](images/FreeCAD-v0-18-CustomizeInterface.png )


</div>

**延伸阅读**

-   [FreeCAD 入门](Getting_started/zh-cn.md)
-   [自定义界面](Interface_Customization/zh-cn.md)
-   [工作台](Workbenches/zh-cn.md)
-   [关于 Python 的更多信息](https://www.python.org)



---
⏵ [documentation index](../README.md) > Manual:The FreeCAD Interface/zh-cn

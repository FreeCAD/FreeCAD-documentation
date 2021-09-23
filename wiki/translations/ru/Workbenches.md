# Workbenches/ru





FreeCAD, подобно многим современным приложениям для проектирования, таким как \[//ru.wikipedia.org/wiki/Revit Revit\] или \[//ru.wikipedia.org/wiki/CATIA CATIA\], базируется на концепции \[//ru.wikipedia.org/wiki/Верстак верстаков\]. Верстаки можно рассматривать как набор инструментов, специально сгруппированных под определенные задачи. В традиционных мебельных мастерских, вы имели бы рабочий стол для человека работающего с деревом, другой для работающего с металлическими частями, и, возможно, третий для того, который монтирует все это вместе.

Тоже самое относится и к FreeCAD. Инструменты сгруппированы в верстаки в соответствии с задачами, к которым они относятся.

Когда вы переключаетесь с одного верстака на другой, доступные в интерфейсе инструменты меняются. Панели инструментов, командные панели и, возможно, другие части интерфейса, переключаются на новый инструментарий, но содержание вашей сцены не меняется. Вы могли бы, например, начать рисовать 2D форму в Чертежном инструментарии, а дальше работать над ней в инструментарии Деталей.

Следует отметить, что иногда верстаки называют *модулями*. Однако, стоит отметить, что верстаки и модули это разные понятия. Модуль - это любое расширение FreeCAD, в то время как Верстак - это специальный тип модуля со своей собственной конфигурацией графического интерфейса (панели инструментов и меню).

## Встроенные верстаки 

В комплекте с FreeCAD идут следующие верстаки:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Std Base](Std_Base.md). This is not really a workbench, but rather a category of \'standard\' commands and tools that can be used in all workbenches.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> [Архитектурный верстак](Arch_Workbench/ru.md) для работы с элементами архитектуры.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> The [Draft Workbench](Draft_Workbench.md) contains 2D tools and basic 2D and 3D CAD operations.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> [Верстак МКЭ](FEM_Workbench/ru.md) обеспечивает рабочий процесс Метода Конечных Элементов (МКЭ).

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

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> [Верстак Электронных таблиц](Spreadsheet_Workbench/ru.md) для создания и редактирования табличных данных.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> The [Start Center Workbench](Start_Workbench.md) allows you to quickly jump to one of the most common workbenches.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar as the Part Shape builder Face from edges.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models. It is the successor of the [Drawing Workbench](Drawing_Workbench.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> The [Web Workbench](Web_Workbench.md) provides you with a browser window instead of the [3D view](3D_view.md) within FreeCAD.

### Не рекомендуемые 

The following workbenches are still included in the base installation for compatibility purposes, but they should no longer be used.

-   <img alt="" src=images/Workbench_Complete.svg  style="width:32px;"> The [Complete Workbench](Complete_Workbench.md) holds all commands and features from all workbenches that met certain quality criteria. {{Obsolete|0.17}}

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> The [Drawing Workbench](Drawing_Workbench.md) was used for producing technical drawings but has now been deprecated. It is still needed to read old FreeCAD files that contain objects created with this workbench. The [TechDraw Workbench](TechDraw_Workbench.md) is its more advanced replacement. {{Obsolete|0.17}}

## Внешние верстаки 

Верстаки FreeCAD легко программируются в [Python](Python/ru.md), поэтому многие разрабатывают дополнительные верстаки вне кодовой базы FreeCAD.

Страница [внешние верстаки](External_workbenches/ru.md) перечисляет все известные сообществу. Большинство из них легко устанавливается из FreeCAD, используя [Addon Manager](Addon_Manager/ru.md) через меню **Инструменты → <img src="images/AddonManager.svg" width=24px> Addon manager**.

Новые верстаки всегда в разработке, следите за обновлениями!







[Category:Workbenches](Category:Workbenches.md)

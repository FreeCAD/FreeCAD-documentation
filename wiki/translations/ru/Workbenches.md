# Workbenches/ru
<div class="mw-translate-fuzzy">

FreeCAD, подобно многим современным приложениям для проектирования, таким как \[//ru.wikipedia.org/wiki/Revit Revit\] или \[//ru.wikipedia.org/wiki/CATIA CATIA\], базируется на концепции \[//ru.wikipedia.org/wiki/Верстак верстаков\]. Верстаки можно рассматривать как набор инструментов, специально сгруппированных под определенные задачи. В традиционных мебельных мастерских, вы имели бы рабочий стол для человека работающего с деревом, другой для работающего с металлическими частями, и, возможно, третий для того, который монтирует все это вместе.


</div>

Тоже самое относится и к FreeCAD. Инструменты сгруппированы в верстаки в соответствии с задачами, к которым они относятся.

Когда вы переключаетесь с одного верстака на другой, доступные в интерфейсе инструменты меняются. Панели инструментов, командные панели и, возможно, другие части интерфейса, переключаются на новый инструментарий, но содержание вашей сцены не меняется. Вы могли бы, например, начать рисовать 2D форму в Чертежном инструментарии, а дальше работать над ней в инструментарии Деталей.

Следует отметить, что иногда верстаки называют *модулями*. Однако, стоит отметить, что верстаки и модули это разные понятия. Модуль - это любое расширение FreeCAD, в то время как Верстак - это специальный тип модуля со своей собственной конфигурацией графического интерфейса (панели инструментов и меню).



## Встроенные верстаки 

### Current

Следующие верстаки идут в комплекте с каждой установкой FreeCAD:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Стандартные инструменты](Std_Base/ru.md). На самом деле это не верстак, а скорее категория \'стандартных\' команд и инструментов, которые можно использовать на всех верстаках.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> [Верстак Arch](Arch_Workbench/ru.md) для работы с элементами архитектуры.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [Верстак Draft](Draft_Workbench/ru.md) содержит 2D-инструменты и основные операции 2D и 3D CAD.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> [Верстак FEM](FEM_Workbench/ru.md) обеспечивает рабочий процесс анализа Методом Конечных Элементов (МКЭ).


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> [Верстак Inspection](Inspection_Workbench/ru.md) сделан для того, чтобы дать вам специфические инструменты для осмотра форм. Он всё ещё находится в стадии разработки.


</div>

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> [Верстак Mesh](Mesh_Workbench/ru.md) для работы с триангулярными (разбитыми на треугольники) сетками.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> [Верстак OpenSCAD](OpenSCAD_Workbench/ru.md) обеспечивает совместимость с OpenSCAD и восстановление истории модели [конструктивной твердотельной геометрии](constructive_solid_geometry/ru.md) (CSG).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [ Верстак Part](Part_Workbench/ru.md) для работы с деталями САПР.


</div>

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [ Верстак Part Design](PartDesign_Workbench/ru.md) для построения фигур деталей из эскизов.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> [Верстак Path](Path_Workbench/ru.md) используется для создания инструкций G-Code. Он всё ещё находится в стадии разработки.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> [Верстак Points](Points_Workbench/ru.md) для работы с облаками точек.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> [Верстак Reverse Engineering](Reverse_Engineering_Workbench/ru.md) предназначен для предоставления специальных инструментов для преобразования форм/тел/сеток в параметрические элементы, совместимые с FreeCAD. Он все ещё находится в стадии разработки.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> [Верстак Robot](Robot_Workbench/ru.md) для изучения движений робота.


</div>

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Верстак Sketcher](Sketcher_Workbench/ru.md) для работы с геометрически ограниченными эскизами.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> [Верстак Spreadsheet](Spreadsheet_Workbench/ru.md) для создания и обработки данных электронной таблицы.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> [Верстак Start Center](Start_Workbench/ru.md) позволяет быстро перейти к одному из наиболее распространённых верстаков.


</div>

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> [Верстак Surface](Surface_Workbench/ru.md) предоставляет инструменты для создания и изменения поверхностей. Он похож на опцию Грань из отрезков [Построителя Форм](Part_Builder/ru.md).

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> [Верстак TechDraw](TechDraw_Workbench/ru.md) для создания технических чертежей из 3D-моделей. Это преемник [Верстака Drawing](Drawing_Workbench/ru.md).

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> [Верстак Test Framework](Testing/ru.md) предназначен для отладки FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> [Верстак Web](Web_Workbench/ru.md) предоставляет окно браузера вместо [3D вида](3D_view/ru.md) FreeCAD.

### Obsolete

The following workbenches are no longer included after version 0.20:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> [Верстак Drawing](Drawing_Workbench/ru.md) использовался для изготовления технических чертежей, но в настоящее время устарел. По-прежнему необходимо читать старые файлы FreeCAD, содержащие объекты, созданные с помощью этого верстака. [Верстак TechDraw](TechDraw_Workbench/ru.md) является его более продвинутой заменой. {{Obsolete|0.17}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> [Верстак Image](Image_Workbench/ru.md) для работы с растровыми изображениями.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> [Верстак Raytracing](Raytracing_Workbench/ru.md) для работы с трассировкой лучей (рендеринг).


</div>



## Внешние верстаки 

Верстаки FreeCAD легко программируются в [Python](Python/ru.md), поэтому многие разрабатывают дополнительные верстаки вне кодовой базы FreeCAD.


<div class="mw-translate-fuzzy">

Страница [внешние верстаки](External_workbenches/ru.md) перечисляет все известные сообществу. Большинство из них легко устанавливается из FreeCAD, используя [Addon Manager](Std_AddonMgr/ru.md) через меню **Инструменты → <img src="images/Std_AddonMgr.svg" width=24px> Addon manager**.


</div>



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Workbenches/ru

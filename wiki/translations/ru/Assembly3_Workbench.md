# <img alt="Assembly3 workbench icon" src=images/Assembly3_workbench_icon.svg  style="width   *64px;"> Assembly3 Workbench/ru


{{TOCright}}

## Введение

<img alt="" src=images/Assembly3_workbench_icon.svg  style="width   *24px;"> [Assembly3](Assembly3_Workbench/ru.md) это [внешний верстак](External_workbenches/ru.md), используемый для выполнения сборок различных тел, содержащихся в едином файле или нескольких документах. Верстак Assembly3 основан на нескольких изменениях основных функций, сделанных для версии FreeCAD 0.19 (например, [App Link](App_Link/ru.md)), поэтому его нельзя использовать с более ранними версиями.

Основные особенности Assembly3 Workbench   *

-   **динамический/интерактивный решатель**. Это означает, что вы можете перемещать детали с помощью мыши, в то время как решающая программа ограничивает движение. Это позволяет, например, подключить колесо к оси и вращать колесо интерактивно с помощью мыши.
-   **ссылки**. Это означает, что вы можете использовать одну единственную деталь, например винт несколько раз в сборке (в разных местах) без дублирования геометрии.
-   **внешняя ссылка**. Возможно иметь документ FreeCAD, который содержит только сборку без деталей. Все части могут быть в отдельных файлах. Файлы могут быть даже в библиотеке или где-нибудь еще в файловой системе. Единственное требование - файл должен быть загружен при создании ссылки. После создания ссылки файл должен быть открыт для обновления ссылок, связанных с файлом. Assembly3 решает эту проблему, открывая файлы в фоновом режиме по мере необходимости.
-   **иерархические сборки**. Как и в реальной жизни, механический узел может состоять из узлов. Они могут снова состоять из подузлов и так далее.
-   **заморозка сборки**. Поскольку ЦП может обрабатывать только определённое количество одновременных ограничений в реальном времени, замораживание сборки позволяет использовать ограничения даже для больших сборок. При замораживании готовых сборок или ограничений, которые не должны оставаться динамическими (например, сварные, болтовые или склеенные детали), они исключаются из расчётов обновления и считаются решателем Assembly3 фиксированной геометрией.

       *   Обратите внимание, что другие подходы предлагают другое решение этой проблемы, например <img alt="" src=images/Assembly4_workbench_icon.svg  style="width   *24px;"> [Assembly4 Workbench](Assembly4_Workbench/ru.md).

[наверх](#top.md)

### Панели инструментов 

По состоянию на 2020 год верстак Assembly3 имеет следующие панели инструментов.

#### Основная панель инструментов 

   *   <img alt="" src=images/Assembly_New_Assembly.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_New_Group.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_New_Element.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_Import.svg‎‎  style="width   *28px;"><img alt="" src=images/AngleDown.svg‎‎  style="width   *14px;"><img alt="" src=images/Assembly3_workbench_icon.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_QuickSolve.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_Move.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_QuickMove.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_LockMover.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_TogglePartVisibility.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_Trace.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_AutoRecompute.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_SmartRecompute.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_AutoFixElement.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_AutoElementVis.svg‎‎  style="width   *28px;"><img alt="" src=images/AngleDown.svg‎‎  style="width   *14px;"><img alt="" src=images/Assembly_Add_Workplane.svg‎‎  style="width   *28px;"><img alt="" src=images/AngleDown.svg‎‎  style="width   *14px;"><img alt="" src=images/Assembly_TreeItemUp.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_TreeItemDown.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintMultiply.svg‎‎  style="width   *28px;">


<div class="mw-collapsible mw-collapsed">


   *   **Основная панель инструментов** содержит инструменты, покрывающие наиболее часто используемые функции верстака. Всплывающие подсказки покажут ярлыки клавиатуры.


<div class="mw-collapsible-content toccolours">

   ** <img alt="" src=images/Assembly_New_Assembly.svg‎‎  style="width   *32px;"> [Create assembly](Assembly3_CreateAssembly/ru.md)   * Добавить папку сборки

   ** <img alt="" src=images/Assembly_New_Group.svg‎‎  style="width   *32px;"> [Group objects](Assembly3_GroupObjects/ru.md)   * Группировать объекты

   ** <img alt="" src=images/Assembly_New_Element.svg‎‎  style="width   *32px;"> [Create element](Assembly3_CreateElement/ru.md)   * Создать элемент.

   ** Импорт из STEP. Имеет две установки

   **\* <img alt="" src=images/Assembly_Import.svg‎‎  style="width   *32px;"> [Import from STEP](Assembly3_ImportFromSTEP/ru.md)   * Импорт STEP-файлов

   **\* <img alt="" src=images/Assembly_ImportMulti.svg‎‎  style="width   *32px;"> [Import as multi-document](Assembly3_ImportMultiDocument/ru.md)   * Импорт сборок из STEP в отдельные документы

   ** <img alt="" src=images/Assembly3_workbench_icon.svg‎‎  style="width   *32px;"> [Resolve constraints](Assembly3_ResolveConstraints/ru.md)   * Разрешить ограничения

   ** <img alt="" src=images/Assembly_QuickSolve.svg‎‎  style="width   *32px;"> [Quick solve](Assembly3_QuickSolve/ru.md)   * Быстрое разрешение ограничений

   ** <img alt="" src=images/Assembly_Move.svg‎‎  style="width   *32px;"> [Move part](Assembly3_MovePart/ru.md)   * Перемещение деталей в 3D, это специфично для Assembly3

   ** <img alt="" src=images/Assembly_AxialMove.svg‎‎  style="width   *32px;"> [Axial move](Assembly3_AxialMove/ru.md)   * Axial move parts in 3D, это классический инструмент, доступный в любом месте FreeCAD.

   ** <img alt="" src=images/Assembly_QuickMove.svg‎‎  style="width   *32px;"> [Быстрое перемещение](Assembly3_QuickMove/ru.md)   * При этом выделенная в дереве часть будет прикреплена к курсору мыши. Она изменит положение детали при щелчке мышью.

   **   * Часто добавляемые части накладываются друг на друга в начале координат. Используйте эту функцию, чтобы захватить деталь, которую вы не видите.

   ** <img alt="" src=images/Assembly_LockMover.svg‎‎  style="width   *32px;"> [Lock mover](Assembly3_LockMover/ru.md)   * Блокировка перемещения зафиксированных частей. Переключаемая кнопка. Когда эта кнопка не нажата, можно перемещать части, которые имеют ограничение \"Locked\".

   ** <img alt="" src=images/Assembly_TogglePartVisibility.svg‎‎  style="width   *32px;"> [Переключатель видимости](Assembly3_TogglePartVisibility/ru.md)   * Переключает видимость выделенной части.

   **   * Обратите внимание, что это отличается использование пробела. Использование пробела для выделенных элементов из подразделов в 3D-виде часто ведет себя не так, как ожидалось. Используйте эту функцию в этих случаях (или сочетание A-Space).

   ** <img alt="" src=images/Assembly_Trace.svg‎‎  style="width   *32px;"> [Trace part move](Assembly3_TracePartMove/ru.md)   * Отслеживание перемещения детали (TBD)

   ** <img alt="" src=images/Assembly_AutoRecompute.svg‎‎  style="width   *32px;"> [Auto recompute](Assembly3_AutoRecompute/ru.md)   * Автопересчет. Обычно включено.

   **   * Может быть не включено при ремонте ограничений или исправлении деталей, когда решатель выдает сообщение *\"не сходятся\"* (например, поворачивая деталь на 180 градусов).

   ** <img alt="" src=images/Assembly_SmartRecompute.svg‎‎  style="width   *32px;"> [Smart recompute](Assembly3_SmartRecompute/ru.md)   * Умный пересчёт. Обычно включено.

   ** <img alt="" src=images/Assembly_AutoFixElement.svg‎‎  style="width   *32px;"> [Auto fix element](Assembly3_AutoFixElement/ru.md)   * Автоматическое исправление элементов. Экспериментальная возможность в 0.19_pre

   ** Стиль элемента. Имеет две настройки

   **\* <img alt="" src=images/Assembly_AutoElementVis.svg‎‎  style="width   *32px;"> [Auto element visibility](Assembly3_AutoElementVisibility/ru.md)   * Автоматическая видимость элемента.

   **\* <img alt="" src=images/Assembly_ShowElementCS.svg‎‎  style="width   *32px;"> [Show element coordinate system](Assembly3_ShowElementCS/ru.md)   * Показать систему координат элемента.

   ** Рабочая плоскость и начала координат. Добавляет рабочую плоскость, размещение или начало координат. Должна быть выбрана деталь. Имеет пять установок

   **\* <img alt="" src=images/Assembly_Add_Workplane.svg‎‎  style="width   *32px;"> [Add workplane](Assembly3_AddWorkplane/ru.md)   * добавить рабочую область

   **\* <img alt="" src=images/Assembly_Add_WorkplaneXZ.svg‎‎  style="width   *32px;"> [Add XZ workplane](Assembly3_AddXZWorkplane/ru.md)   * добавить XZ область

   **\* <img alt="" src=images/Assembly_Add_WorkplaneZY.svg‎‎  style="width   *32px;"> [Add ZY workplane](Assembly3_AddZYWorkplane/ru.md)   * Добавить YZ область

   **\* <img alt="" src=images/Assembly_Add_Placement.svg‎‎  style="width   *32px;"> [Add placement](Assembly3_AddPlacement/ru.md)   * добавить Размещение

   **\* <img alt="" src=images/Assembly_Add_Origin.svg‎‎  style="width   *32px;"> [Add Origin](Assembly3_AddOrigin/ru.md)   * добавить Начало координат

   ** <img alt="" src=images/Assembly_TreeItemUp.svg‎‎  style="width   *32px;"> [Move item up](Assembly3_MoveItemUp/ru.md)   * MПереместить выбранный элемент дерева вверх

   ** <img alt="" src=images/Assembly_TreeItemDown.svg‎‎  style="width   *32px;"> [Move item down](Assembly3_MoveItemDown/ru.md)   * Переместите выбранный элемент дерева вниз

   **   * Позволяет сортировать Детали, Элементы или Ограничения в древе. Сворачивает элемент (сверху вниз и наоборот). Работает лишь при единичном выборе.

   ** <img alt="" src=images/Assembly_ConstraintMultiply.svg‎‎  style="width   *32px;"> [Multiply constraint](Assembly3_MultiplyConstraint/ru.md)   * Множественное Ограничение. Это может быть выбрано, если присутствует несколько частей и подходящих Элементов.

   **   * Используется, например, для назначения нескольких креплений одного типа в несколько отверстий с одним ограничением.


</div>


</div>

#### Панель основных ограничений 

   *   <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintAlignment.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width   *28px;"><img alt="" src=images/AngleDown.svg‎‎  style="width   *14px;"><img alt="" src=images/Assembly_ConstraintAxial.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintSameOrientation.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintMultiParallel.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintAngle.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPerpendicular.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointCoincident.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointInPlane.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointOnCircle.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointsDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointPlaneDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointLineDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintSymmetric.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintMore.svg‎‎  style="width   *28px;">


<div class="mw-collapsible mw-collapsed">


   *   Некоторые инструменты на деле представляют собой меню для дополнительных инструментов.


<div class="mw-collapsible-content toccolours">

   ** <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width   *32px;"> [Locked](Assembly3_ConstraintLock/ru.md)   * Добавьте ограничение \"Locked\", чтобы зафиксировать одну или несколько частей.

   **   * Вам нужно выбрать элемент геометрии детали.

   **   * Если вы фиксируете вершину или ребро, деталь по-прежнему может свободно вращаться вокруг вершины или ребра.

   **   * Фиксация грани полностью заблокирует деталь.

   ** <img alt="" src=images/Assembly_ConstraintAlignment.svg‎‎  style="width   *32px;"> [Plane Alignment](Assembly3_ConstraintAlignment/ru.md)   * Добавьте ограничение \"Plane alignment\", чтобы выровнять плоские грани двух или более деталей.

   **   * Грани становятся копланарными или параллельными с возможной дистанцией.

   ** <img alt="" src=images/Assembly_ConstraintCoincidence.svg‎‎  style="width   *32px;"> [Plane Coincidence](Assembly3_ConstraintCoincidence/ru.md)   * Добавьте ограничение \"Plane coincidence\", чтобы совместить плоские грани двух или более деталей.

   **   * Грани совпадут в своих центрах с возможной дистанцией.

   ** Attachment имеет две настройки

   **\* <img alt="" src=images/Assembly_ConstraintAttachment.svg‎‎  style="width   *32px;"> [Attachment](Assembly3_ConstraintAttachment/ru.md)   * Добавьте ограничение \"Attachment\", чтобы прикрепить две детали с выбранными элементами геометрии.

   **\*   * Это ограничение полностью фиксирует детали относительно друг друга.

   **\* <img alt="" src=images/Assembly_ConstraintAttachmentOffset.svg‎‎  style="width   *32px;"> [AttachmentOffset](Assembly3_ConstraintAttachmentOffset/ru.md)   * То же, что и ограничение \"Attachment\", но с сохранением текущего относительного размещения задействованных частей путем установки смещения элемента.

   **\*   * Это ограничение полностью фиксирует детали относительно друг друга.

   ** <img alt="" src=images/Assembly_ConstraintAxial.svg‎‎  style="width   *32px;"> [Axial Alignment](Assembly3_ConstraintAxial/ru.md)   * Добавьте ограничение \"Axial alignment\" для выравнивания ребер/граней двух или более деталей.

   **   * ограничение принимает

   **   *   * линейные ребра, которые становятся коллинеарными,

   **   *   * плоские грани, которые выровнены по оси нормали к поверхности,

   **   *   * и цилиндрическая грань, которые выровнены по осевому направлению.

   **   * Можно смешивать различные типы геометрических элементов.

   ** <img alt="" src=images/Assembly_ConstraintSameOrientation.svg‎‎  style="width   *32px;"> [Same orientation](Assembly3_ConstraintSameOrientation/ru.md)   * Добавьте ограничение \"Same orientation\", чтобы выровнять грани двух или более деталей.

   **   * Плоскости выровнены, чтобы иметь одинаковую ориентацию (т.е. вращение)

   ** <img alt="" src=images/Assembly_ConstraintMultiParallel.svg‎‎  style="width   *32px;"> [Multi parallel](Assembly3_ConstraintMultiParallel/ru.md)   * Добавьте зависимость \"Multi parallel\", чтобы сделать плоские грани или линейные ребра двух или более деталей параллельными.

   ** <img alt="" src=images/Assembly_ConstraintAngle.svg‎‎  style="width   *32px;"> [Angle](Assembly3_ConstraintAngle/ru.md)   * Добавьте ограничение \"Angle\", чтобы задать угол между плоскими гранями или линейными ребрами двух деталей.

   ** <img alt="" src=images/Assembly_ConstraintPerpendicular.svg‎‎  style="width   *32px;"> [Perpendicular](Assembly3_ConstraintPerpendicular/ru.md)   * Добавьте ограничение \"Perpendicular\", чтобы сделать плоские грани или линейные ребра двух деталей перпендикулярными.

   ** <img alt="" src=images/Assembly_ConstraintPointCoincident.svg‎‎  style="width   *32px;"> [Points coincident](Assembly3_ConstraintPointsCoincident/ru.md)   * Добавьте ограничение \"Point coincident\", чтобы совместить две точки в 2D или 3D.

   ** <img alt="" src=images/Assembly_ConstraintPointInPlane.svg‎‎  style="width   *32px;"> [Point on plane](Assembly3_ConstraintPointInPlane/ru.md)   * Добавьте \"Point on plane\", чтобы ограничить одну или несколько точек плоскостью.

   ** <img alt="" src=images/Assembly_ConstraintPointOnLine.svg‎‎  style="width   *32px;"> [Point on line](Assembly3_ConstraintPointOnLine/ru.md)   * Добавьте \"Point on line\", чтобы ограничить точку линией в 2D или 3D.

   ** <img alt="" src=images/Assembly_ConstraintPointOnCircle.svg‎‎  style="width   *32px;"> [Point on circle](Assembly3_ConstraintPointOnCircle/ru.md)   * Добавьте \"Point on circle\", чтобы ограничить одну или несколько точек цилиндрической поверхностью, заданной окружностью.

   **   * Обратите внимание, что вы должны выбрать точку (любой элемент геометрии может определить точку), а затем выбрать окружность (или цилиндрическую поверхность),

   **   * после чего вы можете добавить дополнительные точки к вашему выбору, если надо.

   ** <img alt="" src=images/Assembly_ConstraintPointsDistance.svg‎‎  style="width   *32px;"> [Points distance](Assembly3_ConstraintPointsDistance/ru.md)   * Добавьте \"Points distance\", чтобы ограничить расстояние между двумя или более точками.

   ** <img alt="" src=images/Assembly_ConstraintPointPlaneDistance.svg‎‎  style="width   *32px;"> [Point plane distance](Assembly3_ConstraintPointPlaneDistance/ru.md)   * Добавьте \"Point plane distance\", чтобы ограничить расстояние между одной или несколькими точками и плоскостью.

   ** <img alt="" src=images/Assembly_ConstraintPointLineDistance.svg‎‎  style="width   *32px;"> [Point line distance](Assembly3_ConstraintPointLineDistance/ru.md)   * Добавьте \"Point line distance\" чтобы ограничить расстояние между точкой и линейным ребром в 2D или 3D.

   ** <img alt="" src=images/Assembly_ConstraintSymmetric.svg‎‎  style="width   *32px;"> [Symmetric](Assembly3_ConstraintSymmetric/ru.md)   * Добавьте зависимость \"Symmetric\", чтобы сделать элементы геометрии двух деталей симметричными относительно плоскости.

   **   * Поддерживаемые элементы   * линейная кромка и плоская грань.

   ** <img alt="" src=images/Assembly_ConstraintMore.svg‎‎  style="width   *32px;"> [More](Assembly3_ConstraintMore/ru.md)   * Включение дополнительных панелей инструментов ограничений

   **   * На деле не ограничение, а тумблер для отображения/скрытия **Additional Constraints Toolbars**.


</div>


</div>

#### Additional Constraints Toolbars 

   *   <img alt="" src=images/Assembly_ConstraintPointDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintEqualAngle.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointsSymmetric.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintSymmetricLine.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointsHorizontal.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointsVertical.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintLineHorizontal.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintLineVertical.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintArcLineTangent.svg‎‎  style="width   *28px;"> (Assembly3 Constraints2)





   *   <img alt="" src=images/Assembly_ConstraintSketchPlane.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintLineLength.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintEqualLength.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintLengthRatio.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintLengthDifference.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintLengthEqualPointLineDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintMidPoint.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintDiameter.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintEqualRadius.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintPointsProjectDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintEqualPointLineDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_ConstraintColinear.svg‎‎  style="width   *28px;"> (Assembly3 Sketch Constraints)


<div class="mw-collapsible mw-collapsed">


   *   You can enable these by selecting the **<img src="images/Assembly_ConstraintMore.svg‎‎" width=16px> [More](Assembly3_ConstraintMore.md)** button on the Main Constraints toolbar.


<div class="mw-collapsible-content toccolours">

   ** <img alt="" src=images/Assembly_ConstraintPointDistance.svg‎‎  style="width   *32px;"> [Point distance](Assembly3_ConstraintPointDistance.md)   * Add a \"Point distance\" to constrain the distance of two points in 2D or 3D.

   ** <img alt="" src=images/Assembly_ConstraintEqualAngle.svg‎‎  style="width   *32px;"> [Equal angle](Assembly3_ConstraintEqualAngle.md)   * Add an \"Equal angle\" to equate the angles between two lines or normals.

   ** <img alt="" src=images/Assembly_ConstraintPointsSymmetric.svg‎‎  style="width   *32px;"> [Points symmetric](Assembly3_ConstraintPointsSymmetric.md)   * Add a \"Points symmetric\" constraint to make two points symmetric about a plane.

   ** <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width   *32px;"> () [Symmetric horizontal](Assembly3_ConstraintSymmetricHorizontal.md)   * Symmetric horizontal

   ** <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width   *32px;"> () [Symmetric vertical](Assembly3_ConstraintSymmetricVertical.md)   * Symmetric vertical

   ** <img alt="" src=images/Assembly_ConstraintSymmetricLine.svg‎‎  style="width   *32px;"> [Symmetric line](Assembly3_ConstraintSymmetricLine.md)   * Add a \"Symmetric line\" constraint to make two points symmetric about a line.

   ** <img alt="" src=images/Assembly_ConstraintPointsHorizontal.svg‎‎  style="width   *32px;"> [Points horizontal](Assembly3_ConstraintPointsHorizontal.md)   * Add a \"Points horizontal\" constraint to make two points horizontal with each other when projected onto a plane.

   ** <img alt="" src=images/Assembly_ConstraintPointsVertical.svg‎‎  style="width   *32px;"> [Points vertical](Assembly3_ConstraintPointsVertical.md)   * Add a \"Points vertical\" constraint to make two points vertical with each other when projected onto a plane.

   ** <img alt="" src=images/Assembly_ConstraintLineHorizontal.svg‎‎  style="width   *32px;"> [Line horizontal](Assembly3_ConstraintLineHorizontal.md)   *Add a \"Line horizontal\" constraint to make a line segment horizontal when projected onto a plane.

   ** <img alt="" src=images/Assembly_ConstraintLineVertical.svg‎‎  style="width   *32px;"> [Line vertical](Assembly3_ConstraintLineVertical.md)   * Add a \"Line vertical\" constraint to make a line segment vertical when projected onto a plane.

   ** <img alt="" src=images/Assembly_ConstraintArcLineTangent.svg‎‎  style="width   *32px;"> [Arc line tangent](Assembly3_ConstraintArcLineTangent.md)   * Add an \"Arc line tangent\" constraint to make a line tangent to an arc at the start or end point of the arc.

   ** <img alt="" src=images/Assembly_ConstraintSketchPlane.svg‎‎  style="width   *32px;"> [Sketch plane](Assembly3_ConstraintSketchPlane.md)   * Add a \"Sketch plane\" to define the work plane of any draft element inside or following this constraint.

   **   * Add an empty \"Sketch plane\" to undefine the previous work plane.

   ** <img alt="" src=images/Assembly_ConstraintLineLength.svg‎‎  style="width   *32px;"> [Line length](Assembly3_ConstraintLineLength.md)   * Add a \"Line length\" constrain the length of a non-subdivided Draft.Wire.

   ** <img alt="" src=images/Assembly_ConstraintEqualLength.svg‎‎  style="width   *32px;"> [Equal length](Assembly3_ConstraintEqualLength.md)   * Add an \"Equal length\" constraint to make two lines of the same length.

   ** <img alt="" src=images/Assembly_ConstraintLengthRatio.svg‎‎  style="width   *32px;"> [Length ratio](Assembly3_ConstraintLengthRatio.md)   * Add a \"Length ratio\" to constrain the length ratio of two lines.

   ** <img alt="" src=images/Assembly_ConstraintLengthDifference.svg‎‎  style="width   *32px;"> [Length difference](Assembly3_ConstraintLengthDifference.md)   * Add a \"Length difference\" to constrain the length difference of two lines.

   ** <img alt="" src=images/Assembly_ConstraintLengthEqualPointLineDistance.svg‎‎  style="width   *32px;"> [Length Equal Point Line Distance](Assembly3_ConstraintLengthEqualPointLineDistance.md)   * Add a \"Length Equal Point Line Distance\" to constrain the distance

   **   * between a point and a line to be the same as the length of a another line.

   ** <img alt="" src=images/Assembly_ConstraintGeneral.svg‎‎  style="width   *32px;"> ( <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg‎‎  style="width   *32px;"> )[Equal Line Arc Length](Assembly3_ConstraintEqualLineArcLength.md)   * Add an \"Equal Line Arc Length\" constraint to make a line of the same length as an arc.

   ** <img alt="" src=images/Assembly_ConstraintMidPoint.svg‎‎  style="width   *32px;"> [Mid point](Assembly3_ConstraintMidPoint.md)   * Add a \"Mid point\" to constrain a point to the middle point of a line.

   ** <img alt="" src=images/Assembly_ConstraintDiameter.svg‎‎  style="width   *32px;"> [Diameter](Assembly3_ConstraintDiameter.md)   * Add a \"Diameter\" to constrain the diameter of a circle/arc.

   ** <img alt="" src=images/Assembly_ConstraintEqualRadius.svg‎‎  style="width   *32px;"> [Equal radius](Assembly3_ConstraintEqualRadius.md)   * Add an \"Equal radius\" constraint to make two circles/arcs of the same radius.

   ** <img alt="" src=images/Assembly_ConstraintPointsProjectDistance.svg‎‎  style="width   *32px;"> [Points project distance](Assembly3_ConstraintPointsProjectDistance.md)   * Add a \"Points project distance\" to constrain the distance of two points projected on a line.

   ** <img alt="" src=images/Assembly_ConstraintEqualPointLineDistance.svg‎‎  style="width   *32px;"> [Equal point line distance](Assembly3_ConstraintEqualPointLineDistance.md)   * Add an \"Equal point line distance\" to constrain the distance

   **   * between a point and a line to be the same as the distance between another point and line.

   ** <img alt="" src=images/Assembly_ConstraintColinear.svg‎‎  style="width   *32px;"> [Colinear](Assembly3_ConstraintColinear.md)   * Add a \"Colinear\" constraint to make two lines collinear.


</div>


</div>


   *   Панель **Ограничений** (**Constraints tool bars**) будет основной панелью, используемой при сборке деталей.
   *   По умолчанию она неактивна, но активируются после выбора хотя бы одной грани, линии или точки детали.
   *   Обычно вы выбираете элементы, которые должны быть объединены, а затем выбираете тип ограничения.
   *   Различные цветные рамки отмечают различные характеристики ограничений   *

       *   2D/3D при добавлении более 2 Элементов.
   *   Подробное описание можно найти в вики Gibhub.

#### Панель навигации 

   *   <img alt="" src=images/Assembly_GotoRelation.svg‎‎  style="width   *28px;"> <img alt="" src=images/LinkSelect.svg‎‎  style="width   *28px;"> <img alt="" src=images/LinkSelectFinal.svg‎‎  style="width   *28px;">


<div class="mw-collapsible mw-collapsed">


   *   Эти функции полезны при работе со сборкой с иерархией связанных внешних файлов.


<div class="mw-collapsible-content toccolours">

   ** <img alt="" src=images/Assembly_GotoRelation.svg‎‎  style="width   *32px;"> [Go to relation](Assembly3_GoToRelation/ru.md)   * Открывает группу отношений (по умолчанию скрыта) и выбирает объект отношения.

   ** <img alt="" src=images/Std_LinkSelectLinked.svg  style="width   *32px;"> [Select linked object](Std_LinkSelectLinked/ru.md)   * Выбирает связанный объект и переключается на его документ. <small>(v0.19)</small> 

   ** <img alt="" src=images/Std_LinkSelectLinkedFinal.svg  style="width   *32px;"> [Select linked final](Std_LinkSelectLinkedFinal/ru.md)   * Выбирает объект с самыми глубокими ссылками и переключается на его документ. <small>(v0.19)</small> 


</div>


</div>

#### Панель Measurement 

   *   <img alt="" src=images/Assembly_MeasurePointDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_MeasurePointLineDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_MeasurePointPlaneDistance.svg‎‎  style="width   *28px;"> <img alt="" src=images/Assembly_MeasureAngle.svg‎‎  style="width   *28px;">


<div class="mw-collapsible mw-collapsed">


   *   **Панель Measurement** добавляет функции для измерения расстояний между двумя объектами.


<div class="mw-collapsible-content toccolours">

   ** <img alt="" src=images/Assembly_MeasurePointDistance.svg‎‎  style="width   *32px;"> [Measure points](Assembly3_MeasurePoints/ru.md)   * Добавьте \"Measure points\" для измерения расстояния между двумя точками в 2D или 3D.

   ** <img alt="" src=images/Assembly_MeasurePointLineDistance.svg‎‎  style="width   *32px;"> [Measure point to line](Assembly3_MeasurePointLine/ru.md)   * Добавьте \"Measure point to line\" для измерения расстояния между точкой и линейным ребром в 2D или 3D.

   ** <img alt="" src=images/Assembly_MeasurePointPlaneDistance.svg‎‎  style="width   *32px;"> [Measure point to plane](Assembly3_MeasurePointPlane/ru.md)   * Добавьте \"Measure point to plane\" для измерения угла между точкой и плоскостью.

   ** <img alt="" src=images/Assembly_MeasureAngle.svg‎‎  style="width   *32px;"> [Measure angle](Assembly3_MeasureAngle/ru.md)   * Добавьте \"Measure angle\" для измерения угла между плоскими гранями или линейными рёбрами двух разных деталей.

   *   Функции измерения радиуса или диаметра нет. .
   *   Инструменты измерения выдерживают замену деталей, например расстояние между краями куба при изменении размера куба.
   *   Поскольку вычисления ограничений выполняются в реальном времени и обновляются при любых изменениях. За кулисами функция очень похожа на [ограничения](#Ограничения/ru.md). Расстояние или угол между [элементами](#Элементы.md) рассчитывается таким же образом, как и для [ограничений](#Ограничения.md). Отображение в дереве работает аналогично.


</div>


</div>

Как обычно, вы можете изменять панели инструментов и добавлять или удалять отдельные инструменты. Обязательно проверьте меню Assembly3 на наличие функций, которые могут отсутствовать на панели инструментов.

[наверх](#top.md)

### Ограничения

Проектировщик использует ограничения для достижения желаемого результата для соотношения двух частей. Выбор правильных ограничений, которые лучше всего подходят для решения каждой проблемы - Искусство. Каждая удалённая степень свободы теоретически должна устраняться только один раз между двумя объектами, но на практике со многими инструментами САПР выбранные ограничения создают комбинации избыточных ограничений, порой компенсируемые сложными алгоритмами, а порой нет. Assembly3 действительно использует алгоритмы для выявления и компенсации избыточных ограничений, но очевидно, что они еще не очень развиты. Таким образом, на практике для ограничений Assembly3 можно избежать проблем, зная, сколько степеней свободы (DOF) было использовано, а какие ещё предстоит заблокировать. Никакая часть не должна иметь связи с ограничениями превышающими 6 степеней свободы.

   *   Примечание   * Если решатель встречает комбинацию, которую невозможно разрешить, он выдаст ошибку. Решателю сложно выяснить, что вызвало проблему, поэтому, как правило, из данной ошибки не будет ясно, «где» проблема. В крупных сборках это может привести к сложному поиску проблем. К сожалению, нет простого способа избежать этого. Однако это подталкивает полностью осознавать как работает система (например, см. [Elements](#Elements.md) ниже), использовать чёткие имена для всех задействованных компонентов и добавлять новые ограничения лишь когда решатель может разрешить текущую сборку. Очень полезной для отслеживания проблемы является функция «ContexMenu/Deactivate» у каждого ограничения.

Ограничения Assembly3 определяют ограничения в положении или ориентации между двумя [элементами](#Элементы.md). Некоторые ограничения работают даже с более чем двумя [Элементами](#Элементы.md). [Элемент](#Элементы.md) может быть гранью, линией, кромкой или точкой детали. Обычно ограничения определяются путем выбора желаемого [элемента](#Элементы.md), а затем выбора ограничения на [панели инструментов](#Панели_инструментов.md) Constraints.

-   Фиксирует 6 степеней свободы, оставляют 0   *
    -   **Lock**   * ограничение блокирует все степени свободы грани. Его следует использовать для одной базовой детали в каждой сборке. Вы также можете включить функцию *MoveLock* (на панели инструментов), чтобы деталь не могла быть перемещена случайно. Обычно не имеет значения, какую грань/линию/точку вы используете для фиксации детали. Также обратите внимание, что блокировка действительна только для прямой сборки, то есть в случае подсборки родительской сборке все равно потребуется заблокированная деталь сама по себе.
    -   **Attachment**   * Делает системы координат обоих элементов одинаковыми для всех осей. Это самая простая функция с точки зрения вычислений, и ее следует использовать везде, где это возможно. Обратите внимание, что вы можете использовать свойства элемента для компенсации смещений и углов, если два [Элемента](#Элементы.md) не идеально выровнены.
-   Фиксирует 5 степеней свободы, оставляет 1   *
    -   **Plane Coincident**   * фиксирует Tx, Ty, Tz, Rx, Ry. Только Rz свободен. Остаётся вращение вокруг нормали, проходящей через «центр плоскости».
-   Фиксируют 4 степеней свободы, оставляют 2   *
    -   **Axial Alignment**   * фиксирует Tx, Ty, Rx, Ry. Только Tz, Rz свободен. Остается вращение вокруг оси формы и перенос вдоль этой же оси. Два ограничения *PointOnLine* (при различных точках) дают тот же результат. Ограничение \''Colinear\'' - тоже.
    -   **PointOnLine**   * Исключает сдвиг и вращение вдоль нормали к опорной линии. Допускаются только перемещение и вращение по оси линии.
-   Фиксируют 3 степени свободы, оставляют 3   *
    -   **Same Orientation**   * фиксирует Rx, Rz, Rz. Все Т остаются свободными.
    -   **Points Coincident**   * фиксирует Tx, Ty, Tz. Все R остаются свободными.
    -   **PointOnPoint** исключает 3 сдвига.
    -   **Plane Alignment**   * фиксирует Tz, Rx, Ry (движение в плоскости). Это исключает смещение по нормали к базовой плоскости и два вращения вокруг осей этой плоскости.
-   Фиксируют 2 степени свободы, оставляют 4   *
    -   **Multi Parallel**   * фиксирует Rx, Ry, все T и R остаются. Это исключает два вращения вокруг осей базовой плоскости.
-   Фиксируют 1 степень свободы, оставляют 5   *
    -   **Points in Plane**   * фиксирует Tz. Это исключает смещение по нормали к базовой плоскости.
    -   **Points Distance**   * фиксирует расстояние между исходными точками элемента.

           *   Это дает вам больше свободы, чем *Points in Plane*.

Другое

-   **Points on Circle**   * фиксирует Tz и частично Tx, Ty. Замораживает перемещение точки (или нескольких точек) в области круга или диска. Вы должны выбрать круг вторым. Это оставляет все вращения свободными и даёт ограниченный сдвиг в базовой плоскости круга.

*   * Примечание   * В следующем списке Tx, Ty, Tz и Rx, Ry, Rz используются для описания перемещений и поворотов относительно опорных систем координат задействованных Элементов. Это не всегда точно или полностью определено, например когда задействована линия, не определяется, проходит ли она по X, Y или под любым углом между ними. Система используется для простоты и легкости сравнения взамен правильного, но более сложного определения. Таким образом, Z обычно является нормальным направлением всех задействованных граней. Пожалуйста, не стесняйтесь изменять это, используя лучший подход с улучшенной читаемостью.*

[наверх](#top.md)

### Элементы

Элементы это особый термин, используемый в верстаке Assembly 3. Понимание Элементов важно для понимания того, как следует использовать Assembly 3.

Полезно думать об элементе как об общем слове, обозначающем «выбираемый элемент» детали, то есть грань, ребро, круг, угол или другую точку. Элементы, которые вы выбираете для их ограничения, являются этими Элементами. В дереве папка Assembly имеет три подпапки. Рядом с \'Parts\' и \'Constraints\' есть папка \'Elements\', которая пуста, пока не добавлены ограничения. При добавлении ограничения само ограничение получает два (или более) листа, это выбранные «Элементы». Также они добавляются в папку «Элементы», которая представляет собой просто список всех элементов, используемых в сборке. Рекомендуется изменить их имена (с помощью клавиши F2), особенно в больших сборках.

Давайте рассмотрим пример

   *   Создайте новый файл и добавьте куб и цилиндр с помощью верстака Part. Установите цилиндр над кубом. Сначала зафиксируйте базовую деталь, в нашем случае куб. Выберите нижнюю сторону куба и установите ограничения \"Locked\" (первая иконка в Constraints [toolbar](#Toolbars.md)). Выберите верхнюю сторону цилиндра и верхнюю сторону куба. Затем выберите ограничение \"Совпадение плоскостей\" (\"Plane Coincident\"). Теперь цилиндр переместится в куб и в дереве в разделе \'Constraints\' (\"Ограничения\") будет добавлен новый елемент с двумя дочерними узлами. Дополнительно те же самые два дочерних узла будут добавлены в разделе \'Elements\' (\"Элементы\"). Если Ваш цилиндр внутри куба а не сверху, исправим это сначала   * выберите дочерний узел в разделе \'Constraints\' (\"Ограничения\"), который является гранью цилиндра, щелкните правой кнопкой мыши и в контекстном меню и выберите \'Flip Part\' (\"Перевернуть Деталь\"). Теперь цилиндр будет установлен на куб.

Главное, что нужно понять, - это то, что ограничение действует на ссылки на элементы в списке в папке дерева \'Elements\'. Это позволяет сохранять структуру ограничений без изменений при замене деталей. Это очень сложно увидеть без примера.

Вернемся к примеру выше

   *   Примечание   * убедитесь, что вы добавили в куб ограничение \"Locked\", иначе это может сбивать с толку.
   *   В окне САПР выберите другую грань куба. Теперь мы работаем только в древовидной структуре. Перейдите мышкой по дереву, в котором должен быть выбран куб. Перетащите кубик в папку \'Elements\'. Перетащите его на имя \'Elements\', а не где-нибудь еще в папке - причину мы увидим позже. Вы должны увидеть, что в список \'Elements\' добавлен еще один элемент. Теперь выберите в папке \'Constraints\' дочерний узел грани куба в ограничении \"Plane Coincident\" и удалите его. Ограничение покажет восклицательный знак, так как отсутствует один элемент. Обратите внимание, что, удалив элемент в ограничении, мы *не* удалили его в списке. Это потому, что в ограничении была только ссылка на элемент в списке. Теперь возьмите только что добавленный элемент в списке \'Elements\' и перетащите его на ограничение \"Plane Coincident\". Теперь цилиндр переместится на другую выбранную грань. Нам может понадобиться снова выбрать в контекстном меню \'flip part\', если цилиндр снова окажется внутри куба.

Пример показал, что, не удаляя ограничение, мы можем менять элементы, которые используются для ограничения. Таким же образом мы можем переместить цилиндр в совершенно другую часть. Поигравшись с этим примером еще немного, вы заметите некоторые дополнительные вещи, как

-   Если вы переименуете элемент в списке, имя будет изменено во всех ограничениях.
-   вы можете использовать один элемент в списке в нескольких ограничениях.
-   Вы можете использовать окно свойств элемента, чтобы добавить **смещения**. В примере это может перемещать цилиндр по грани куба.
-   вы можете использовать кнопку \"Show Element Coordinate System\" на главной панели инструментов, чтобы увидеть, что делают в контекстном меню \'Flip Part\' и \'Flip Element\'. Обязательно посмотрите, что происходит в окне свойств.
-   вы можете добавить ограничение в совершенно другом порядке   * сначала добавьте несколько элементов в «Список элементов» (полезно наименование, например, «Верхняя грань куба» или «Лицевая грань куба»), затем добавьте ограничение, ничего не выбирая - это будет пустым ограничением. Затем перетащите элементы из списка «Элементы». Результат такой же, как и в первом примере. После выполнения этого упражнения должно быть ясно, как работают ограничения с элементами.
-   вы можете изменить существующее ограничение между существующими элементами, просто выбрав другой элемент в свойстве PropertyWindow/ConstraintType.

[наверх](#top.md)

## Совместимость

На Assembly3 повлиял [Assembly2](Assembly2_Workbench/ru.md), но они не совместимы. Если у Вас есть старые модели, созданные в Assembly2, оставайтесь с FreeCAD 0.16 и используйте Assembly2 с ним.

Новые модели, разработанные с Assembly3, должны открываться и редактироваться с ним.

Несмотря на наличие похожих инструментов, Assembly3 не совместим ни с [A2plus](A2plus_Workbench.md), ни с [Assembly4](Assembly4_Workbench.md). Модели, созданные в этих верстаках, должны открываться только своими верстаками.

[наверх](#top.md)

## Установка

[Верстак Assembly3](Assembly3_Workbench/ru.md) (по состоянию на март 2022) доступен через [Addon Manager](Std_AddonMgr/ru.md). Все внешние зависимости Assembly3 должны разрешаться автоматически через Addon Manager.

#### Альтернативная установка 

Есть два альтернативных пути для установки Assembly3   *

-   Отдельная ветка FreeCAD, сделанная realthunder; смотри [выпуски FreeCAD_assembly3](https   *//github.com/realthunder/FreeCAD_assembly3/releases). Эта ветка базируется на конкретной точке главной ветки FreeCAD, но имеет дополнительные возможности, пока не присутствующие в главной ветке. Поскольку эта ветвь базируется на конкретном слепке с процесса разработки, в неё не попали позднейшие возможности, внедрённые позднее в главную ветку.
-   [AppImage](AppImage.md) версии в разработке. Это базируется на текущей главной ветке, и включает зависимости, требуемые для работы с Assembly3, такие как вычислитель из SolveSpace.

Поскольку AppImage работает только для Linux, выбором для пользователей Windows (кто хочет установить Assembly3 альтернативным путём) будет лишь первый вариант тестирования Assembly3 (ветка realthunderа).

[наверх](#top.md)

## HowTo

### Начать

Есть много способов создать сборку с помощью Assembly3. Вот самый простой из возможных вариантов.

   *   <img alt="" src=images/Assembly3_Example-GettingStarted.jpg  style="width   *600px;">
   *   *Окончательный результат примера «Начало работы». На изображении выбран верстак Assembly3, поэтому видно несколько его панелей инструментов. Обратите внимание, что вертикальная «TabBar» слева от древовидного представления - это верстак AddOn, который не содержится в стандартном FreeCAD (но может быть установлен с помощью Addon-Manager).*

-   Press **<img src="images/Std_New.svg" width=16px> [New](Std_New/ru.md)** для создания нового файла FreeCAD
-   Выберите верстак <img alt="" src=images/Assembly3_workbench_icon.svg  style="width   *16px;"> [Assembly3](Assembly3_Workbench/ru.md).
-   Выберите **<img src="images/Assembly_New_Assembly.svg‎‎" width=16px> [Create assembly](Assembly3_CreateAssembly/ru.md)
**
-   Перейдите на верстак <img alt="" src=images/Workbench_Part.svg  style="width   *16px;"> [Part](Part_Workbench/ru.md) добавьте <img alt="" src=images/Part_Cylinder.svg  style="width   *16px;"> [Cylinder](Part_Cylinder/ru.md) и <img alt="" src=images/Part_Box.svg  style="width   *16px;"> [Cube](Part_Box/ru.md)
-   <img alt="" src=images/Std_Save.svg  style="width   *16px;"> [Сохраните](Std_Save/ru.md) файл с любым именем, которое вам нравится. <img alt="" src=images/Std_CloseActiveWindow.svg  style="width   *16px;"> [Закройте](Std_CloseActiveWindow/ru.md) and <img alt="" src=images/Std_Open.svg  style="width   *16px;"> [откройте](Std_Open/ru.md) файл снова.

\*   * Древовидное представление должно выглядеть так 
```python
 Assembly
   Constraints
   Elements
   Parts
 Cylinder
 Cube
```

<img alt="" src=images/Assembly3_Example-Tree-01.png  style="width   *300px;"> <img alt="" src=images/Assembly3_Example-Tree-02.png  style="width   *280px;">

-   Теперь перетащите мышью **Cylinder** и **Cube** на папку **Parts**. Они переместятся внутрь.

       *   Это самый быстрый способ, подходящий для простых случаев вроде этого. Лучше использовать объект link   *
       *   Выбрать **Cube** и **Cylinder** и затем **<img src="images/Std_LinkMake.svg" width=16px> [Make link](Std_LinkMake/ru.md)** или через **Context menu** (-\> LinkActions -\> MakeLink) или через панель **Structure**.
       *   Это добавляет два объекта ссылок. Затем перетащите объекты ссылок в папку *Parts*.
-   Щелкните по обеим верхним поверхностям цилиндра и куба (удерживая Ctrl, или Cmd на Mac)
-   Выберите верстак <img alt="" src=images/Assembly3_workbench_icon.svg  style="width   *16px;"> [Assembly3](Assembly3_Workbench/ru.md).
-   Выберите **<img src="images/Assembly_ConstraintCoincidence.svg‎‎" width=16px> [Plane Coincidence](Assembly3_ConstraintCoincidence.md)** из [Main constraints toolbar](#Main_Constraints_Toolbar/ru.md).

Теперь части должны быть соединены друг с другом, и ваше дерево должно выглядеть примерно так (0.20.pre и Link Branch)   *

<img alt="" src=images/Assembly3_Example-Tree-03.png  style="width   *300px;"> <img alt="" src=images/Assembly3_Example-Tree-04.png  style="width   *280px;">

-   Щелкните правой кнопкой мыши **\_Element** (любой из двух) и выберите \"Flip Part\".

\*   * Теперь **цилиндр** должен быть наверху **коробки**. Если перевёрнуто всё, вернитесь и выберите \"Flip Part\" на другом элементе.

   *   Мы пропустили один важный шаг, который должен выполняться в больших сборках   * блокировка базовой детали.
   *   Это означает, что нужно определить одну деталь, которую нельзя будет перемещать по ограничениям. В вашем случае для этого мы используем куб   *
    -   Выберите нижнюю грань куба. Только нижняя грань, а не весь куб.
    -   выберите ограничение **<img src="images/Assembly_ConstraintLock.svg‎‎" width=16px> [Locked](Assembly3_ConstraintLock.md)** на [панели инструментов ограничения](#Main_Constraints_Toolbar.md)

Готово.

Готовое дерево сборки должно выглядеть примерно как (0.20.pre и Link Branch)   *

<img alt="" src=images/Assembly3_Example-Tree-05.png  style="width   *300px;"> <img alt="" src=images/Assembly3_Example-Tree-06.png  style="width   *280px;">   *

Если хотите, можете переместить ограничение **Locked** вверх по дереву. Для этого используйте кнопку **<img src="images/Assembly_TreeItemUp.svg‎‎" width=16px> [Move item up](Assembly3_MoveItemUp/ru.md)** на главной [панели инструментов](#Main_Toolbar.md).

**Заметьте**   * все новые внешние файлы должны быть **сохранены**, **закрыты** и повторно открыты как минимум один раз, чтобы Assembly3 могла их найти.

   *   Без этого FreeCAD не сможет передать дескриптор файла верстаку Assembly3 и он не сможет найти новую деталь.
   *   Когда все части находятся в том же файле, вы тоже должны **сохранить**, **закрыть** и снова открыть файл.

[наверх](#top.md)

### Добавление смещения 

Assembly3 не предлагает смещение с константами, как это делают [верстак A2plus](A2plus_Workbench/ru.md) или другие инструменты САПР. Вместо этого он предлагает более общую и гибкую систему для добавления сдвигов, а также углов.

-   Добавьте смещение в свойствах одного [Elements](#Элементы.md) из [Constraint](#Ограничения.md).

       *   вы можете выбрать любой из двух.

Пример   *

-   Добавьте 2 куба в сборку и выберите их боковые грани.
-   выберите \"PlaneCoincident\". Кубики будут прикреплены друг к другу.
-   выберите один элемент и «Контекстное меню → Flip Part». Кубики будут прикреплены бок о бок.
-   выберите одно свойство элемента Offset/Position/Zz и установите значение 5 мм. Кубики будут находиться на расстоянии 5 мм друг от друга.

   ** Проверьте с другими осями или полями углов/осей. Также убедитесь, что вы получаете тот же результат при использовании другого элемента. Для других Ограничений применяется аналогичный подход.

[наверх](#top.md)

### Устранение сбоя решателя 

Это часто случается, когда детали чрезмерно ограничены, т.е. заблокировано более 6 степеней свободы.

Самый простой способ найти проблему - щелкнуть соответствующие ограничения в дереве и выбрать в контекстном меню *Disable* и произвести повторный расчёт. Полезно узнать последние добавленные ограничения перед отказом решателя и просто отменить их.

Примечание   * поскольку Assembly3 пытается за кулисами скомпенсировать чрезмерно ограниченные части, иногда проблема просто запускается новым ограничением, но основная причина в другом. Прежде чем удалить все и начать заново, помните, что вы можете повторно использовать элементы. Если вы назвали их, вы можете определить необходимые элементы и заново построить ограничения, вообще не используя трехмерный вид. Смотрите раздел [Элементы](#Элементы.md) выше.

[наверх](#top.md)

### Замена детали или переименование имени файла 

Когда деталь удаляется или изменяется имя файла, сборка ломается, ее нельзя решить, и решатель выдаст сообщение \"Inconsistent constraints\" («Несогласованные ограничения»). Решатель помечает недопустимые элементы и ограничения в дереве знаком вопроса.

Один из способов решить эту проблему - просто удалить все недопустимые ограничения и элементы, импортировать новую часть и все повторить. Но есть способ лучше   *

-   Переименуйте файл
-   \# Используя файловый менеджер скопируйте файл, который хотите переименовать. Затем дайте копии новое имя.
-   \# Откройте копию в FreeCAD. Сборка и старый файл тоже должны быть открыты
-   \# Выберите старый объект в дереве и нажмите на поле для изменения свойства \"Linked object\" («Связанный объект») (оно должно содержать старое имя файла)
-   \# Откроется диалоговое окно со списком всех открытых деталей. Он показывает имена файлов и объекты каждой детали. Выберите старую деталь и объект. Найдите переименованную деталь в дереве и выберите тот же объект в новой детали. Затем подтвердите выбор.
-   \# Удалить старую деталь в дереве. Также можно удалить и файл.
-   \# Ограничения и элементы старой детали стали недействительными. Откройте ограничения или список элементов в дереве. Затем последовательно
-   \# \* выберите грани каждого элемента на новой детали. Элемент в дереве будет выделен.
-   \# \* Возьмите этот элемент и перетащите его на старый элемент (либо в списке элементов, либо в одном из ограничений, где он использовался). Этот элемент должен стать действительным.
-   \# \* Повторите процедуру для остальных элементов. Часто одного элемента достаточно, чтобы Assembly3 могла автоматически идентифицировать остальные элементы детали.
-   \# \* Если элемент был случайно назначен не той поверхности, просто повторите с правильной гранью.
-   \# При желании измените имя объекта в FreeCAD

-   Замена детали другой деталью

       *   *на достаточно похожую деталь, чтобы исходные ограничения, конечно, все еще имели смысл*
-   \# Удалите старую деталь в дереве. Также можно удалить файл.
-   \# Ограничения и элементы старой детали стали недействительными. Откройте ограничение или список элементов в дереве.
-   \# \* Выберите грань элемента новой детали. Элемент в дереве будет выделен.
-   \# \* Возьмите этот элемент и перетащите его на старый элемент (либо в списке элементов, либо в одном из ограничений, где он использовался). Этот элемент должен стать действительным.
-   \# \* Повторите процедуру для остальных элементов.
-   \# \* Если элемент был случайно назначен не той поверхности, просто повторите с правильной гранью.
-   \# При желании измените имя объекта в FreeCAD

\'\'Примечания
\* Эти способы не такие сложные, как могут показаться. Через 2--3 применения они станут гармоничнее и станут легче в применении.

-   Это не только быстрее, чем удаление и повторное выполнение ограничений, но и безопаснее, потому что элемент может быть использован в родительской сборке. Удаление оригинала уничтожит эту ссылку, повторная установка сохранит ее.
-   Также эта процедура становится действительно быстрой и простой, если ограничения и элементы имеют названия. Не нужно гадать, куда следует перетащить грани, потому что названия говорят сами за себя (см. [Советы и хитрости](#Советы_и_хитрости.md)).

\'\'

[top](#top.md)

### Советы и хитрости 

-   Использование иерархических сборок помогает избежать проблем с решателем и позволяет сохранить плавность моделирования. Вы можете заморозить подсистему одним щелчком мыши и сэкономите ресурсы процессора (используйте контекстное меню в дереве). При загрузке сборки Assembly3 не нужно открывать внешние файлы для замороженных подсистем, что сохраняет компактность дерева.
-   Очень полезно выработать привычку именовать элементы и ограничения. Используйте клавишу **F2**, чтобы это делать быстро в дереве. Инструменты сортировки дерева в основной панели инструментов будут очень полезными. Сборка с полностью именованными ограничениями и элементами очень проста в понимании для других людей или для самого себя, по сравнению с предыдущими файлами.

       *   Примерами имен ограничений для стола могут быть \"Align_FrontLegs\", \"Align_FrameBottom-LegTops\", а именами элементов - \"Leg1_Top\" или \"TableTop_Front\", \"TableTop_Left\".
-   Пожалуйста, обратите внимание, что после того, как внешние файлы открыты сборкой, их нелегко закрыть снова, не закрыв сборку. Так как сборка сохраняет открытыми эти файлы в обратном порядке, вкладка может исчезнуть, но файл останется видимым в дереве. При наличии нескольких слоев подсистем закрытие отдельных файлов становится близким к невозможности. Такое поведение может измениться, но до тех пор возможным подходом может быть регулярное использование команд *Файл/Сохранить все* и *Файл/Закрыть все* для очистки дерева перед работой с другой подсистемой.

       *   \'\'Пример   * рассмотрим, что у вас есть большой станок с ЧПУ с основной сборкой и подразделом для каждого модуля. После того, как у вас открыта основная сборка, она может открыть буквально сотни файлов вплоть до одного шарикоподшипника. Перед работой над подразделом корпуса электроники станка хорошо сохранить и закрыть все файлы, чтобы получить пустое дерево. Затем откройте только подраздел корпуса электроники. При этом откроются все нужные файлы, и только они.
-   Использование внешних файлов облегчает повторное использование частей или версионирование частей с такими системами, как git или Subversion. Рабочий процесс во FreeCAD с Assembly чувствуется точно так же, как и с файлами, в которых все части находятся в одном файле. Для частого обмена файлами с другими сторонами более удобным может оказаться использование отдельных файлов.
-   Детали с множественными связями. Если вы добавите ссылку в сборку, то она будет иметь значение свойства под названием \"Element Count\", по умолчанию 0. Если вы установите это значение в 3, то получите 3 экземпляра этой части. Они будут добавлены в подпапку и могут быть использованы как полностью разделяемые части. Используйте эту возможность, чтобы сохранить данные в файле на низком уровне, т.к. часть сохраняется только один раз. Каждый экземпляр содержит только различия.
-   Вставьте несколько деталей, например, Винты, одним кликом. Проверьте [Assembly3 Wiki](https   *//github.com/realthunder/FreeCAD_assembly3/wiki/Constraints-and-Solvers) на сайте Github. Это не только потрясающая функция (даже немножко волшебная), но и действительно очень полезная.

-   Использование [верстак TabBar](https   *//github.com/triplus/TabBar) ускоряет работу со сборкой. Это добавляет панель инструментов с одной кнопкой для каждого рабочего места. Вы можете отсортировать панель инструментов и разместить ее где угодно. Многие люди помещают его вертикально слева, рядом с деревом. Если у вас есть Assembly3, Part, PartDesign и другие часто используемые рабочие места, расположенные ближе к верху, переключение между ними становится чрезвычайно простым.

[наверх](#top.md)

## Ссылки

-   [Объект App Link](App_Link/ru.md), который обеспечивает работу Assembly3.
-   [FreeCAD_assembly3](https   *//github.com/realthunder/FreeCAD_assembly3) репозиторий и документация.
-   [Обзор Assembly3](https   *//forum.freecadweb.org/viewtopic.php?f=20&t=25712), большая ветка обсуждения.
-   [Пробный учебник для Assembly 3 WB](http   *//help-freecad-jpg87.fr/02_ass_ind.php) от jpg87.
-   [Текущий статус Assembly](https   *//forum.freecadweb.org/viewtopic.php?f=20&t=34583)
-   [Внешние верстаки](External_workbenches/ru.md)




[Category   *Addons](Category_Addons.md) [Category   *External Workbenches](Category_External_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Assembly3 Workbench/ru

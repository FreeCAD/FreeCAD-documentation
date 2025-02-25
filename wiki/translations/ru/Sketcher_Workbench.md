# <img alt="Логотип верстака Sketcher" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/ru






## Введение


<div class="mw-translate-fuzzy">

Верстак <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [ Sketcher](Sketcher_Workbench/ru.md) применяется в FreeCAD, для создания двухмерных эскизов, предназначенных для дальнейшего использования в верстаках: <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/ru.md), <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch](Arch_Workbench/ru.md) и других. Плоский двухмерный эскиз является основой для построения большинства CAD моделей, поскольку 2D-эскиз можно «выдавливать» для создания объемных фигур; 2D-эскизы могут быть использованы для создания других элементов, таких как вырезы, выступы или \"надстройки\" поверх ранее построенных объемных фигур. Вместе с логическими операциями, перечисленными в <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [верстаке Part](Part_Workbench/ru.md), Sketcher формирует основу [конструктивной геометрии](constructive_solid_geometry/ru.md) (CSG) построения твердых тел. Более того, вместе с операциями <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [верстака PartDesign](PartDesign_Workbench/ru.md), Sketcher так же формирует основы методов [функционального редактирования](feature_editing/ru.md) при создании твердых тел.


</div>

Together with boolean operations defined in the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md), the Sketcher Workbench, or \"The Sketcher\" for short, forms the basis of the [constructive solid geometry](Constructive_solid_geometry.md) (CSG) method of building solids. Together with <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign Workbench](PartDesign_Workbench.md) operations, it also forms the basis of the [feature editing](Feature_editing.md) methodology of creating solids. But many other workbenches use sketches as well.


<div class="mw-translate-fuzzy">

Функции \"ограничения\" верстака Sketcher, позволяют задавать фигурам точные геометрические размеры определяя длины, углы и отношения (горизонтальность, вертикальность, перпендикулярность и т. д.). Решатель \"ограничений\" в интерактивном режиме обсчитывает ограничения степеней свободы геометрии эскиза.


</div>


<div class="mw-translate-fuzzy">

Sketcher не предназначен для создания 2D чертежей. Когда эскизы используются для создания твердотельного элемента, они автоматически скрываются. Ограничения видны только в режиме редактирования эскиза.


</div>

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*Так выглядит полностью ограниченный эскиз*

## Constraints


<div class="mw-translate-fuzzy">

Ограничения противоположны традиционным явно заданным размерам, они позволяют постепенно ограничивать степени свободы объекта (по англ. Degrees Of Freedom сокращенно \"DOF\"). Например, отрезок не имеющий никаких ограничений имеет 4 степени свободы, его можно: перемещать по горизонтали, перемещать по вертикали, вращать и масштабировать.


</div>

Применение горизонтального или вертикального ограничения или углового ограничения (относительно другой линии или одной из осей) уберет возможность вращать отрезок, оставляя таким образом 3 степени свободы. Привязка одной из точек отрезка к центру системы координат уберет еще 2 степени свободы. Применение ограничения размера уберет последнюю степень свободы. Такой отрезок будет считаться **полностью ограниченым**.


<div class="mw-translate-fuzzy">

Между собой могут быть ограничены и несколько объектов. Две линии могут быть объединены ограничением в точке их пересечения. Между ними может быть установлен угол или же они могут быть перпендикулярны. Линия может касаться дуги или круга и т.п. Сложный эскиз с несколькими объектами может иметь несколько различных решений, и его **полное ограничение** означает, что только одно из этих возможных решений было достигнуто на основе примененных ограничений.


</div>


<div class="mw-translate-fuzzy">

Существует два вида ограничений: геометрические и размерные. Они подробно описаны в разделе [Инструменты](#Инструменты.md) ниже.


</div>

### Edit constraints 

When a [driving dimensional constraint](Sketcher_ToggleDrivingConstraint.md) is created, and if the **Ask for value after creating a dimensional constraint** [preference](Sketcher_Preferences#Display.md) is selected (default), a dialog opens to edit its value.

![](images/Sketcher_Edit_Constraint.png )

You can enter a numerical value or an [expression](Expressions.md), and it is possible to name the constraint to facilitate its use in other expressions. You can also check the **Reference** checkbox to switch the constrain to [reference mode](Sketcher_ToggleDrivingConstraint.md).

To edit the value of an existing dimensional constraint do one of the following:

-   Double-click the constraint value in the [3D view](3D_view.md).
-   Double-click the constraint in the [Sketcher Dialog](Sketcher_Dialog.md).
-   Right-click the constraint in the Sketcher Dialog and select the **Change value** option from the context menu.

### Reposition constraints 

Dimensional constraints can be repositioned in the 3D view by dragging. Hold down the left mouse button over the constraint value and move the mouse. The symbols of geometric constraints are positioned automatically and cannot be moved.

## Profile sketches 

To create a sketch that can be used as a profile for generating solids certain rules must be followed:

-   The sketch must contain only closed contours. Gaps between endpoints, however small, are not allowed.
-   Contours can be nested, to create voids, but should not self-intersect or intersect other contours.
-   Contours cannot share edges with other contours. Duplicate edges must be avoided.
-   T-connections, that is more than two edges sharing a common point, or a point touching an edge, are not allowed.

These rules do not apply to construction geometry (default color blue), which is not shown outside edit mode, or if the sketch is used for a different purpose. Depending on the workbench and the tool that will use the profile sketch, additional restrictions may apply.

## Drawing aids 

The Sketcher Workbench has several drawing aids and other features that can help when creating geometry and applying constraints.

### Continue modes 

There are two continue modes: **Geometry creation \"Continue Mode\"** and **Constraint creation \"Continue Mode\"**. If these are checked (default) in the [preferences](Sketcher_Preferences#Display.md), related tools will restart after finishing. To exit a continuous tool press **Esc** or the right mouse button. This must be repeated if a continuous geometry tool has already received input. You can also exit a continuous tool by starting another geometry or constraint creation tool. Note that pressing **Esc** if no tool is active will exit sketch edit mode. Uncheck the **Esc can leave sketch edit mode** [preference](Sketcher_Preferences#General.md) if you often inadvertently press **Esc** too many times.

### Auto constraints 

In sketches that have **Auto constraints** checked (default) several constraints are applied automatically. The icon of a proposed automatic constraint is shown next to the cursor when it is placed correctly. Left-Clicking will then apply that constraint. This is a per-sketch setting that can be changed in the [Sketcher Dialog](Sketcher_Dialog#Constraints.md) or by changing the **Autoconstraints** [property](Property_editor.md) of the sketch.

The following constraints are applied automatically:

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [Coincident](Sketcher_ConstrainCoincident.md)

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [Point on object](Sketcher_ConstrainPointOnObject.md)

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:16px;"> [Horizontal](Sketcher_ConstrainHorizontal.md)

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:16px;"> [Vertical](Sketcher_ConstrainVertical.md)

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:16px;"> [Tangent](Sketcher_ConstrainTangent.md)

-    <small>(v1.0)</small> : <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [Symmetric](Sketcher_ConstrainSymmetric.md) (line midpoint)

### Snapping


<small>(v0.21)</small> 

It is possible to [snap](Sketcher_Snap.md) to grid lines and grid intersection, to edges of geometry and midpoints of lines and arcs, and to certain angles. Please note that snapping does not produce constraints in and of itself. For example, only if [Auto constraints](#Auto_constraints.md) is switched on will snapping to an edge produce a [Point on object constraint](Sketcher_ConstrainPointOnObject.md). But just picking a point on the edge would then have the same result.

### On-View-Parameters 


<small>(v1.0)</small> 

Depending on the selected option in the [preferences](Sketcher_Preferences#General.md) only the dimensional On-View-Parameters or both the dimensional and the positional On-View-Parameters can be enabled. Positional parameters allow the input of exact coordinates, for example the center of a circle, or the start point of a line. Dimensional parameters allow the input of exact dimensions, for example the radius of a circle, or the length and angle of a line. On-View-Parameters are not available for all tools.

![](images/Sketcher_On_view_parameters_positional.png ) 
*Determining the center point of a circle with the positional parameters enabled*

![](images/Sketcher_On_view_parameters_dimensional.png ) 
*Determining the radius of a circle with the dimensional parameters enabled*

If values are entered and confirmed by pressing **Enter** or **Tab**, related constraints are added automatically. If two parameters are displayed at the same time, for example the X and Y coordinate of a point, it is possible to enter one value and pick a point to define the other. Depending on the object additional constraints may be required to fully constrain it. Constraints resulting from On-View-Parameters take precedence over those that may result from [Auto constraints](Sketcher_Dialog#Constraints.md).

<img alt="" src=images/Sketcher_ArcExample3.png  style="width:300px;"> 
*Arc created by entering all On-View-Parameters with resulting automatically created constraints*

### Coordinate display 

If the **Show coordinates beside cursor while editing** [preference](Sketcher_Preferences#Display.md) is checked (default), the parameters of the current geometry tool (coordinates, radius, or length and angle) are displayed next to the cursor. This is deactivated while On-View-Parameters are shown.

## Selection methods 

While a sketch is in edit mode the following selection methods can be used:

### 3D view element selection 

As elsewhere in FreeCAD, an element can be selected in the [3D view](3D_view.md) with a single left mouse click. But there is no need to hold down the **Ctrl** key when selecting multiple elements. Holding down that key is possible though and has the advantage that you can miss-click without losing the selection. Edges, points and constraints can be selected in this manner.

### 3D view box selection 

Box selection in the 3D view works without using [Std BoxSelection](Std_BoxSelection.md) or [Std BoxElementSelection](Std_BoxElementSelection.md):

1.  Make sure that no tool is active.
2.  Do one of the following:
    -   Click in an empty area and drag a rectangle from left to right to select elements that lie completely inside the rectangle.
    -   Click in an empty area and drag a rectangle from right to left to also select elements that touch or cross the rectangle.

You can box-select edges and points, constraints cannot be box-selected.

### 3D view connected geometry selection 


<small>(v1.0)</small> 

Double-clicking an edge in the 3D view will select all edges directly and indirectly connected with that edge via endpoints. There is no need for the edges to be connected with [Coincident constraints](Sketcher_ConstrainCoincident.md), endpoints need only have the same coordinates.

### Sketcher Dialog selection 

Edges and points can also be selected from the Elements section of the [Sketcher Dialog](Sketcher_Dialog.md), and constraints from the Constraints section of that dialog.

## Copy, cut and paste 


<small>(v1.0)</small> 

The standard keyboard shortcuts, **Ctrl**+**C**, **Ctrl**+**X** and **Ctrl**+**V**, can be used to copy, cut and paste selected Sketcher geometry including related constraints. But these tools are also available from the **Sketch → Sketcher tools** menu. They can be used within the same sketch but also between different sketches or separate instances of FreeCAD. Since the data is copied to the clipboard in the form of Python code, it can be used in other ways too (e.g. shared on the forum).



## Инструменты


<div class="mw-translate-fuzzy">

Все инструменты верстака Sketcher находятся в меню Sketch, которое появляется при загрузке верстака Sketcher.


</div>

Some tools are also available from the [3D view](3D_view.md) context menu while a sketch is in edit mode, or from the context menus of the [Sketcher Dialog](Sketcher_Dialog.md).


<small>(v0.21)</small> 

: If a sketch is in edit mode the Structure toolbar is hidden as none of its tools can then be used.



### Основные

#### Sketcher toolbar 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> [Создать эскиз](Sketcher_NewSketch/ru.md): Создать новый эскиз на выбранной грани или плоскости. Если во время использования этого инструмента грань не выбрана, пользователю, во всплывающем окне, предлагается выбрать плоскость.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_EditSketch.svg‎‎  style="width:32px;"> [Редактировать эскиз](Sketcher_EditSketch/ru.md): Редактировать выбранный эскиз. Это откроет [Диалоговое окно Sketcherа](Sketcher_Dialog/ru.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MapSketch.svg‎‎  style="width:32px;"> [Разместить эскиз на грани](Sketcher_MapSketch/ru.md): Сопоставляет эскиз с ранее выбранной гранью твёрдого тела.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [Переориентировать эскиз](Sketcher_ReorientSketch/ru.md): Позволяет прикрепить эскиз к одной из основных плоскостей.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Проверить эскиз](Sketcher_ValidateSketch/ru.md): Проверить отклонения различных точек и настроить их.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width:32px;"> [Объединить эскизы](Sketcher_MergeSketches/ru.md): Объединить два или более эскиза.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width:32px;"> [Отразить эскиз](Sketcher_MirrorSketch/ru.md): Зеркально отразить эскиз вдоль оси x, оси y или относительно нормали.


</div>

#### Sketcher Edit Mode toolbar 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_LeaveSketch.svg‎‎  style="width:32px;"> [Покинуть эскиз](Sketcher_LeaveSketch/ru.md): Выйти из режима редактирования эскиза.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ViewSketch.svg‎‎  style="width:32px;"> [Обзор эскиза](Sketcher_ViewSketch/ru.md): Установить вид модели перпендикулярно плоскости эскиза.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [Обзор сечения](Sketcher_ViewSection/ru.md): Создаёт плоскость сечения, которая временно скрывает любой объект перед плоскостью эскиза.


</div>

#### Sketcher edit tools toolbar 

-   <img alt="" src=images/Sketcher_Grid.svg  style="width:32px;"> [Toggle grid](Sketcher_Grid.md): Toggles the grid in the sketch currently being edited. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_Snap.svg  style="width:32px;"> [Toggle snap](Sketcher_Snap.md): Toggles snapping in all sketches. Settings can be changed in the related menu. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_RenderingOrder.svg  style="width:32px;"> [Configure rendering order](Sketcher_RenderingOrder.md): The rendering order of all sketches can be changed in the related menu. <small>(v0.21)</small> 

#### Other


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Остановить операцию](Sketcher_StopOperation/ru.md): В режиме редактирования остановить текущую операцию, будь то рисование, установка ограничений и т. д.


</div>



### Геометрические построения 

Содежит инструменты для создания объектов.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePoint.svg‎‎  style="width:32px;"> [Точка](Sketcher_CreatePoint/ru.md): Добавить точку.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Линия по точкам](Sketcher_CreatePolyline/ru.md): Построить линию (ломанную) по точкам. Нажатие клавиши **M** при построении позволяет переключаться между различными режимами построения.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:32px;"> [Отрезок](Sketcher_CreateLine/ru.md): Построить отрезок по двум точкам. При применении некоторых ограничений отрезки воспринимаются, как бесконечные линии.


</div>

-   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create arc:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateArc.svg  style="width:32px;"> [Дуга](Sketcher_CreateArc/ru.md): Построить сегмент дуги задав центр, радиус, начальный угол и конечный угол.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [Дуга по 3 точкам](Sketcher_Create3PointArc/ru.md): Построить сегмент дуги по двум конечным точкам и точке на окружности.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Эллиптическая дуга](Sketcher_CreateArcOfEllipse/ru.md): Построить эллиптическую дугу по центральной точке, главной точке радиуса, начальной и конечной точкам.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Гипербола](Sketcher_CreateArcOfHyperbola/ru.md): Построить гиперболу.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Парабола](Sketcher_CreateArcOfParabola/ru.md): Построить параболу.


</div>

-   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create circle/ellipse:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:32px;"> [Окружность](Sketcher_CreateCircle/ru.md): Построить окружность по центру и радиусу.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [Окружность по трём точкам](Sketcher_Create3PointCircle/ru.md): Построить окружность по трём произвольным точкам.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Эллипс от центра](Sketcher_CreateEllipseByCenter/ru.md): Построить эллипс по центральной точке, точке большого радиуса и точке малого радиуса.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Эллипс по 3 точкам](Sketcher_CreateEllipseBy3Points/ru.md): Построить эллипс по внешнему диаметру (2 точки) и точке малого радиуса.


</div>

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create rectangle:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Прямоугольник](Sketcher_CreateRectangle/ru.md): Рисует прямоугольник по 2-ум противоположным точкам.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Прямоугольник по центру](Sketcher_CreateRectangle_Center/ru.md): Рисует прямоугольник по точке центра и вершине. {{Version/ru|0.20}}


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Скруглённый прямоугольник](Sketcher_CreateOblong/ru.md): Построить скруглённый прямоугольник по двум точкам. {{Version/ru|0.20}}


</div>

-   <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create regular polygon:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Треугольник](Sketcher_CreateTriangle/ru.md): Построить правильный треугольник, вписанный в окружность вспомогательной геометрии.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Квадрат](Sketcher_CreateSquare/ru.md): Построить равносторонний квадрат, вписанный в окружность вспомогательной геометрии.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width:32px;"> [Пятиугольник](Sketcher_CreatePentagon/ru.md): Построить равносторонний пятиугольник, вписанный в окружность вспомогательной геометрии.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Шестиугольник](Sketcher_CreateHexagon/ru.md): Построить равносторонний шестиугольник, вписанный в окружность вспомогательной геометрии.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width:32px;"> [Семиугольник](Sketcher_CreateHeptagon/ru.md): Построить равносторонний семиугольник, вписанный в окружность вспомогательной геометрии.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> [Восьмиугольник](Sketcher_CreateOctagon/ru.md): Построить равносторонний восьмиугольник, вписанный в окружность вспомогательной геометрии.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Правильный многоугольник](Sketcher_CreateRegularPolygon/ru.md) : Построить правильный многоугольник с определенным количеством сторон, по двум точкам: центральной и крайней.


</div>

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create slot:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Паз](Sketcher_CreateSlot/ru.md): Построить овал, по двум точкам.


</div>

  - <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:32px;"> [Arc slot](Sketcher_CreateArcSlot.md): Creates an arc slot. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create B-spline:


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [B-сплайн](Sketcher_CreateBSpline/ru.md): Построить B-сплайн кривую по контрольным точкам.


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [Периодический B-сплайн](Sketcher_CreatePeriodicBSpline/ru.md): Построить периодическую (замкнутую) кривую B-сплайн по контрольным точкам.


</div>

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [B-spline by knots](Sketcher_CreateBSplineByInterpolation.md): Creates a B-spline curve by knot points. Idem.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [Periodic B-spline by knots](Sketcher_CreatePeriodicBSplineByInterpolation.md): Creates a periodic (closed) B-spline curve by knot points. Idem.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Переключить вспомогательную геометрию](Sketcher_ToggleConstruction/ru.md): Переключить геометрию эскиза из/в режим вспомогательной геометрии. Вспомогательная геометрия показана синим цветом и не видна вне режима редактирования Sketcher.


</div>



### Ограничения эскиза 


<div class="mw-translate-fuzzy">

Ограничения используются для задания длин, задания правил взаимодействия между элементами эскиза, для блокировки эскиза по вертикальным и горизонтальным осям. Некоторые ограничения требуют использования [Вспомогательных ограничений](Sketcher_helper_constraint/ru.md).


</div>

-   <img alt="" src=images/Sketcher_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Dimensional constraints:

  - <img alt="" src=images/Sketcher_Dimension.svg  style="width:32px;"> [Dimension](Sketcher_Dimension.md): Is the context-sensitive constraint tool of the Sketcher Workbench. Based on the current selection, it offers appropriate dimensional constraints, but also geometric constraints. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Горизонтальное расстояние](Sketcher_ConstrainDistanceX/ru.md): Фиксирует горизонтальное расстояние между двумя точками или конечными точками линии. Если выбран только один элемент, то расстояние устанавливается относительно начала координат.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;"> [Вертикальное расстояние](Sketcher_ConstrainDistanceY/ru.md): Фиксирует вертикальное расстояние между двумя точками или конечными точками линии. Если выбран только один элемент, то расстояние устанавливается относительно начала координат.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [Расстояние](Sketcher_ConstrainDistance/ru.md): Задает размер выбранной линии, ограничивая ее длину, или задает расстояние между двумя точками, ограничивая по расстоянию между ними.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Радиус/диаметр](Sketcher_ConstrainRadiam/ru.md): Автоматический указывает радиус/диаметр выбранной дуги или окружности (вес для полюса B-сплайна, диаметр для полного круга, радиус для дуги) {{Version/ru|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Радиус](Sketcher_ConstrainRadius/ru.md): Задает радиус выбранной дуги или круга, ограничивая его.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Диаметр](Sketcher_ConstrainDiameter/ru.md): Задает диаметр выбранной дуги или окружности заданием ограничения радиуса.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Угол](Sketcher_ConstrainAngle/ru.md): Указать угол между двумя выбранными отрезками.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Зафиксировать](Sketcher_ConstrainLock/ru.md): Ограничивает выбранный элемент, устанавливая вертикальные и горизонтальные расстояния относительно начала координат, тем самым фиксируя местоположение этого элемента. Позже эти ограничения расстояния могут быть отредактированы.


</div>

-   <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:32px;"> [Coincident (unified)](Sketcher_ConstrainCoincidentUnified.md): Creates a coincident constraint between points, fixes points on edges or axes, or creates a concentric constraint. It combines the [Coincident](Sketcher_ConstrainCoincident.md) and [Point on object](Sketcher_ConstrainPointOnObject.md) tools. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [Ограничение наложения точек](Sketcher_ConstrainCoincident/ru.md): Прикрепляет точку к одной или нескольким другим точкам (совпадает с ними). Он действует как концентрическое ограничение, если выбраны две или более окружностей, дуг, эллипсов или дуг эллипсов.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [Привязать точку к объекту](Sketcher_ConstrainPointOnObject/ru.md): Прикрепляет точку к отрезку, дуге или оси координат.


</div>

-   <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;">Horizontal/vertical constraints:

  - <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:32px;"> [Horizontal/vertical](Sketcher_ConstrainHorVer.md): Constrains lines or pairs of points to be horizontal or vertical, whichever is closest to the current alignment. It combines the [Horizontal](Sketcher_ConstrainHorizontal.md) and [Vertical](Sketcher_ConstrainVertical.md) tools. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [Горизонталь](Sketcher_ConstrainHorizontal/ru.md): Преобразует выбранные отрезки или линии в строго горизонтальные. При применении этого ограничения можно выбрать более одного объекта.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;"> [Вертикаль](Sketcher_ConstrainVertical/ru.md): Преобразует выбранные отрезки или линии в строго вертикальные. При применении этого ограничения можно выбрать более одного объекта.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;"> [Параллельность](Sketcher_ConstrainParallel/ru.md): Ограничивает две или более линии, параллельные друг другу.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [Перпендикулярность](Sketcher_ConstrainPerpendicular/ru.md): Ограничивает две линии, перпендикулярные друг другу, или ограничить линию, перпендикулярную конечной точке дуги.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [Ограничение касательности](Sketcher_ConstrainTangent/ru.md): Создаёт касательную и ограничение между двумя выбранными объектами, или коллинеарное ограничение между двумя линиями. Линия не обязательно должна лежать непосредственно на дуге или окружности, чтобы быть ограниченной касательной к этой дуге или окружности.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [Равенство](Sketcher_ConstrainEqual/ru.md): Создает ограничение равенства двух выбранных объектов. При использовании на кругах или дугах их радиусы будут равны.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [Симметричность](Sketcher_ConstrainSymmetric/ru.md): Создает симметрию и ограничение между двумя точками относительно линии или между двумя точками относительно третьей выбранной точки.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Блокировать](Sketcher_ConstrainBlock/ru.md): Блокирует перемещение ребра, то есть предотвращает изменение текущего положения его вершин. Это может быть очень полезно для фиксации позиций В-сплайнов. Смотрите ветку форума [Block Constraint forum topic](https://forum.freecadweb.org/viewtopic.php?f=9&t=26572).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> [Ограничение преломления (Закон Снеллиуса)](Sketcher_ConstrainSnellsLaw/ru.md): Ограничивает две линии по закону преломления света. Моделирует свет, проходящий через границу раздела сред.


</div>

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Toggle constraints:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [Переключить ограничения в построительные/основные](Sketcher_ToggleDrivingConstraint/ru.md): Переключает панель инструментов или выбранные ограничения в/из вспомогательного режима.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Вкл/выкл ограничение](Sketcher_ToggleActiveConstraint/ru.md): Включить или отключить уже установленное ограничение. {{Version/ru|0.19}}


</div>



### Инструменты эскизов 

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Create fillet/chamfer:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Скругление](Sketcher_CreateFillet/ru.md): Создаёт скругление между двумя непараллельными линиями.


</div>

  - <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:32px;"> [Chamfer](Sketcher_CreateChamfer.md): creates a chamfer between two non-parallel edges. This is the same tool as [Fillet](Sketcher_CreateFillet.md) but with a different initial mode. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Edit edge:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:32px;"> [Обрезать](Sketcher_Trimming/ru.md): Обрезать линию, окружность или дугу относительно выбранной точки.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Разделить ребро](Sketcher_Split/ru.md): Разделяет ребро на два, сохраняя большинство ограничений. {{Version/ru|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Продлить](Sketcher_Extend/ru.md): Продлить линию или дугу до линии границы, дуги, эллипса, эллиптической дуги или точки в пространстве.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [Внешняя геометрия](Sketcher_External/ru.md): Создать ребро, связанное с внешней геометрией.


</div>

-   <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> External geometry:

  - <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"> [Create external projection geometry](Sketcher_Projection.md): Creates the projection edges of external geometry. <small>(v1.1)</small> 

  - <img alt="" src=images/Sketcher_Intersection.svg  style="width:32px;"> [Create external intersection geometry](Sketcher_Intersection.md): Creates the intersection edges of external geometry with the sketch plane. <small>(v1.1)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [Структурная копия](Sketcher_CarbonCopy/ru.md): Копировать геометрию из другого эскиза.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width:32px;"> [Выбрать начало координат](Sketcher_SelectOrigin/ru.md): Выбирает начало координат эскиза.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width:32px;"> [Выбрать горизонтальную ось](Sketcher_SelectHorizontalAxis/ru.md): Выбирает горизонтальную ось (ось абсцисс) эскиза.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width:32px;"> [Выбрать вертикальную ось](Sketcher_SelectVerticalAxis/ru.md): Выбирает вертикальную ось (ось ординат) эскиза.


</div>

-   <img alt="" src=images/Sketcher_Translate.svg  style="width:32px;"> [Array transform](Sketcher_Translate.md): Moves or optionally creates copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Rotate.svg  style="width:32px;"> [Polar transform](Sketcher_Rotate.md): Rotates or optionally creates rotated copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Scale.svg  style="width:32px;"> [Scale transform](Sketcher_Scale.md): Scales or optionally creates scaled copies of selected elements. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Offset.svg  style="width:32px;"> [Offset geometry](Sketcher_Offset.md): Creates equidistant edges around selected edges. <small>(v1.0)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [Симметрия](Sketcher_Symmetry/ru.md): Копирует элемент эскиза симметрично выбранной линии.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Удалить выравнивание осей](Sketcher_RemoveAxesAlignment/ru.md): Удаляет выравнивание осей, пытаясь по возможности сохранить связь ограничения перпендикулярности и эквивалентности ребер. {{Version/ru|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Удалить всю геометрию](Sketcher_DeleteAllGeometry/ru.md): Удаляет всю геометрию из эскиза.


</div>

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Удалить все ограничения](Sketcher_DeleteAllConstraints/ru.md): Удаляет все ограничения из эскиза.

-   <img alt="" src=images/Edit-copy.svg  style="width:32px;"> Copy in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

-   <img alt="" src=images/Edit-cut.svg  style="width:32px;"> Cut in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).

-   <img alt="" src=images/Edit-paste.svg  style="width:32px;"> Paste in Sketcher: See [Copy, cut and paste](#Copy,_cut_and_paste.md).



### Инструменты эскизов для B-сплайн-ов 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width:32px;"> [Преобразовать геометрию в B-сплайн](Sketcher_BSplineApproximate/ru.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Увеличить степень B-сплайна](Sketcher_BSplineIncreaseDegree/ru.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Уменьшить степень B-сплайна](Sketcher_BSplineDecreaseDegree/ru.md), {{Version/ru|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Увеличить количество узлов сопряжения B-сплайна](Sketcher_BSplineIncreaseKnotMultiplicity/ru.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Уменьшить количество узлов сопряжения B-сплайна](Sketcher_BSplineDecreaseKnotMultiplicity/ru.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Вставить узел](Sketcher_BSplineInsertKnot/ru.md), {{Version/ru|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Объединить кривые](Sketcher_JoinCurves/ru.md), {{Version/ru|0.21}}


</div>

### Sketcher visual 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Выбрать элементы со степенями свободы](Sketcher_SelectElementsWithDoFs/ru.md): Выбирает геометрию подсвеченную зеленым цветом, имеющую не степени свободы, иначе говоря не полностью ограниченную.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width:32px;"> [Выбрать связанные ограничения](Sketcher_SelectConstraints/ru.md): Выберает элементы эскиза, связанные с ограничениями.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width:32px;"> [Выбрать связанную геометрию](Sketcher_SelectElementsAssociatedWithConstraints/ru.md): Выбрать элементы эскиза, связанные с ограничениями.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:32px;"> [Выбрать избыточные ограничения](Sketcher_SelectRedundantConstraints/ru.md): Выбирает избыточные ограничения эскиза.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:32px;"> [Выбрать конфликтующие ограничения](Sketcher_SelectConflictingConstraints/ru.md): Выбирает конфликтующие ограничения эскиза.


</div>

-   <img alt="" src=images/Sketcher_ArcOverlay.svg  style="width:32px;"> [Show/hide circular helper for arcs](Sketcher_ArcOverlay.md): Shows or hides the circular helpers (underlying virtual circles) for arcs in all sketches. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Show/hide B-spline information layer:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Показать/Скрыть степень B-сплайна](Sketcher_BSplineDegree/ru.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Показать/Скрыть полигон управления B-сплайном](Sketcher_BSplinePolygon/ru.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Показать/Скрыть кривую B-сплайна](Sketcher_BSplineComb/ru.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Показать/Скрыть узлы сопряжения B-сплайнов](Sketcher_BSplineKnotMultiplicity/ru.md)


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Показть/скрыть контрольную точку веса B-сплайна](Sketcher_BSplinePoleWeight/ru.md), {{Version/ru|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [Показать/скрыть внутреннюю геометрию](Sketcher_RestoreInternalAlignmentGeometry/ru.md): Восстанавливает отсутствующую/удаленную внутреннюю геометрию выбранного эллипса, дуги эллипса/гиперболы/параболы или B-сплайна.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Переключение Виртуального Пространства](Sketcher_SwitchVirtualSpace/ru.md): Позволяет скрыть все ограничения эскиза и снова сделать их видимыми.


</div>

### Obsolete tools 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Клонировать](Sketcher_Clone/ru.md): Клонирует элемент эскиза.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width:32px;"> [Замкнуть фигуру](Sketcher_CloseShape/ru.md): Создает замкнутую фигуру, применяя ограничение совпадения к конечным точкам. Данный инструмент устарел, и не будет поддерживаться в будущих релизах (<small>(v1.0)</small> ).


</div>


<div class="mw-translate-fuzzy">

  - <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Скругление с сохранением ограничений](Sketcher_CreatePointFillet.md): Создает скругление между двумя непараллельными линиями, сохраняя их (виртуальное) пересечение.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width:32px;"> [Соединить ребра](Sketcher_ConnectLines/ru.md): Соединяет элементы эскиза применяя ограничение совпадения к конечным точкам. Данный инструмент устарел, и не будет поддерживаться в будущих релизах (<small>(v1.0)</small> ).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Копия](Sketcher_Copy/ru.md): Копирует элемент эскиза.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Перемещение](Sketcher_Move/ru.md): Перемещает выбранную геометрию, используя в качестве ссылки последнюю выбранную точку.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [Прямоугольный массив](Sketcher_RectangularArray/ru.md): Создает массив из выбранных элементов эскиза.


</div>



### Настройки


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Preferences-general.svg  style="width:32px;"> [Настройки](Sketcher_Preferences/ru.md): Настройки для верстака Sketcher.


</div>




<div class="mw-translate-fuzzy">

## Оптимальные решения 


</div>


<div class="mw-translate-fuzzy">

Каждый пользователь САПР со временем вырабатывает свой собственный способ работы, но есть несколько полезных общих принципов, которым нужно следовать.


</div>


<div class="mw-translate-fuzzy">

-   Набором простых эскизов управлять легче, чем одним сложным. Например, первый эскиз может быть создан для применения 3D операции (такой как выдавливание или вращение), а второй может содержать отверстия или вырезы. Некоторые детали могут быть опущены, чтобы позднее быть реализованными 3D-операциями. Вы можете избегать скруглений в эскизе, если их слишком много, и добавить их позднее 3D-операцией.
-   Всегда создавайте замкнутый контур, иначе из эскиза не получится создать твердое тело, а только набор открытых граней. Если вы не хотите, чтобы некоторые элементы были включены в создание твердого тела, включите их в состав вспомогательных элементов конструкции с помощью инструмента Вспомогательный режим.
-   Используйте функцию Авто Ограничения, чтобы уменьшить количество ограничений, которые вам нужно будет добавить вручную.
-   Как правило, сначала используются геометрические ограничения, затем размерные ограничения, последним и заблокировав эскиз. Но помните: правила созданы для того, чтобы их нарушать. Если вам трудно манипулировать эскизом, может быть полезно сначала ограничить несколько объектов, прежде чем закончить свой контур.
-   Если возможно, отцентрируйте свой эскиз в начале координат (0,0) с ограничением блокировки. Если ваш эскиз не симметричен, расположите одну из его точек в начале координат или выберите красивые круглые числа для расстояний блокировки. В версии 0.12 внешние ограничения (ограничение эскиза существующей 3D-геометрией, такой как ребра или другие эскизы) не реализованы. Это означает, что для размещения геометрии следующих эскизов на вашем первом эскизе вам необходимо вручную установить расстояния относительно вашего первого эскиза. Ограничение блокировки (25,75) из начала координат легче запомнить, чем (23.47,73.02).
-   Если у вас есть выбор между ограничением Расстояния и ограничением Горизонтального или Вертикального расстояния, предпочтите двое последних. Ограничения горизонтального и вертикального расстояния менее затратны в плане вычисления.
-   В общем, лучше всего использовать следующие ограничения: Горизонталь и Вертикаль; Горизонтальное и Вертикальное расстояние; Совпадение Точка к Точке. Если возможно, ограничьте использование следующих: Расстояние; Касательная; Точка на Объекте; Симметричность.
-   Если вы сомневаетесь в достоверности эскиза после его завершения (некоторые элементы все равно подсвечиваются зелёными цветом), закройте диалоговое окно Sketcher, переключитесь на верстак <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/ru.md) и запустите инструмент **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Проверка геометрии](Part_CheckGeometry/ru.md)**.


</div>



## Уроки


<div class="mw-translate-fuzzy">

-   [Справочник по Sketcher](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) от chrisb. Это большой 70-ти страничный PDF документ который служит подробным руководством по Sketcher. В нем объясняются основы использования Sketcher и подробно рассказывается о создании геометрических фигур и каждом из ограничений.
-   [Базовые уроки по Sketcher](Basic_Sketcher_Tutorial/ru.md) для начинающих
-   [Мини Урок по Sketcher - Ограничения на практике](Sketcher_Micro_Tutorial_-_Constraint_Practices/ru.md)
-   [Требования к эскизам верстака Sketcher](Sketcher_requirement_for_a_sketch/ru.md) Минимальные требования для эскиза и полного определения эскиза.


</div>



## Программирование

Страница [программирование в Sketcher](Sketcher_scripting/ru.md) содержит в себе примеры создания различных ограничений через скрипты Python.

## Examples

For some ideas of what can be achieved with Sketcher tools, have a look at: [Sketcher examples](Sketcher_Examples.md).

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:80px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:90px;">



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Sketcher](Category_Sketcher.md) > Sketcher Workbench/ru


{{Page in progress}}

 

<img alt="Иконка верстака Draft на которой изображен Кульман" src=images/Workbench_Draft.svg  style="width:128px;">


{{TOCright}}

## Введение

<img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [Верстак Draft Workbench](Draft_Module/ru.md) позволяет начертить простые двумерные объекты и предлагает некоторые инструменты для их последующей модификации. Он так же предоставляет инструменты для указания рабочей плоскости, сетки и привязки для точного управления расположением геометрии.

Создаваемые плоские объекты могут использоваться для общего черчения как в программах Inkscape или Autocad. Эти плоские фигуры могут так же использоваться как базовые компоненты трёхмерных объектов, создаваемых другими верстаками, например, <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [Part](Part_Workbench/ru.md) и <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> [Arch](Arch_Workbench/ru.md). Так же возможно преобразование объектов Draft в объекты <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Sketch](Sketcher_Workbench/ru.md), это значит, что фигуры могут так же использоваться в <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [верстаке PartDesign](PartDesign_Workbench/ru.md) для создания твёрдых тел.

FreeCAD --- это, прежде всего, приложение для 3D-моделирования, и поэтому его инструменты для двумерного рисования не столь совершенны, как в других чертёжных программах. Если вашей основной целью является создание сложных 2D-чертежей и файлов в формате [DXF](DXF/ru.md), и вам не нужно 3D-моделирование, возможно вы захотите использовать специальное программное обеспечения для технического черчения, такое как [LibreCAD](https://ru.wikipedia.org/wiki/LibreCAD), [QCad](https://ru.wikipedia.org/wiki/QCad), TurboCad и другие.

<img alt="Draft Workbench Example" src=images/Draft_Workbench_Example.png  style="width:400px;">

## Черчение объектов {#черчение_объектов}

Эти инструменты предназначенные для создания объектов.

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Линия](Draft_Line/ru.md): чертит отрезок через две точки.
-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Полилиния](Draft_Wire/ru.md): чертит ломанную, состоящую из отрезков (полилинию).
-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Fillet](Draft_Fillet/ru.md): чертит fillet (скруглённый угол) или chamfer (сглаженный линией угол) между двумя простыми [линиями](Draft_Line/ru.md). <small>(v0.19)</small> .
-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Дуга](Draft_Arc/ru.md): чертит дугу по центру, радиусу, начальному и конечному углу.
-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Arc 3Points](Draft_Arc_3Points/ru.md): чертит круглый дуговой сегмент по трём точкам, находящимся на окружности. <small>(v0.19)</small> .
-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Окружность](Draft_Circle/ru.md): чертит окружность по центру и радиусу.
-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Эллипс](Draft_Ellipse/ru.md): чертит эллипс по двум угловым точкам.
-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Прямоугольник](Draft_Rectangle/ru.md): чертит прямоугольник по двум противоположным точкам.
-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Многоугольник](Draft_Polygon/ru.md): чертит правильный многоугольник по центру, радиусу и числу сторон.
-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B-сплайн](Draft_BSpline/ru.md): чертит B-сплайн по последовательности точек.
-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Cubic Bezier Curve](Draft_CubicBezCurve/ru.md): чертит кривую Безье третьего порядка протягиванием двух точке. <small>(v0.19)</small> .
-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Кривая Безье](Draft_BezCurve/ru.md): чертит кривую Безье по последовательности точек.
-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Точка](Draft_Point/ru.md): вставляет точку.
-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Граневяз](Draft_Facebinder/ru.md): создаёт новый объект из выбранных граней существующих объектов.
-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Текст в кривую](Draft_ShapeString/ru.md): создаёт сложную форму, представляющую текстовую строку в заданном месте.

## Аннотации

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Текст](Draft_Text/ru.md): чертит многострочную текстовую аннотацию.
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimension](Draft_Dimension/ru.md): чертить размерную аннотацию.
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Label](Draft_Label/ru.md): помещает метку со стрелкой, указывающую на выбранный элемент. <small>(v0.17)</small> 
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Annotation style editor](Draft_AnnotationStyleEditor/ru.md): Открывает редактор для изменения стиля аннотации этих объектов. <small>(v0.19)</small> 

## Изменение объектов {#изменение_объектов}

Эти инструменты изменяют существующие объекты. Они работают на выбранных объектах, но если ни одного объекта не выбрано, вам будет предложено его выбрать.

многие операционные инструменты (перемещение, поворот, массивы и т.д.) так же работают над твердотельными объектами ([Part](Part_Workbench/ru.md), [PartDesign](PartDesign_Workbench/ru.md), [Arch](Arch_Workbench/ru.md) и т.д.).

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Перемещение](Draft_Move/ru.md): перемещает объект(ы) из одной локации в другую.
-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Повернуть](Draft_Rotate/ru.md): поворачивает объект(ы) от начального и до конечного угла.
-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Масштаб](Draft_Scale/ru.md): изменяет размер выбранного(ых) объекта(ов) вокруг базовой точки.
-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Отразить](Draft_Mirror/ru.md): создаёт зеркальное отражение выбранных объектов.
-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Смещение](Draft_Offset/ru.md): перемещает сегменты объекта на заданное расстояние.
-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Trim/Extend (Trimex)](Draft_Trimex/ru.md): обрезает или удлиняет объект.
-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Pастягивать](Draft_Stretch/ru.md): растягивает выбранные объекты {{Version/ru|0.17}}

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Клонировать](Draft_Clone/ru.md): клонирует выбранные объекты.
-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> Инструменты работы с массивами.
    -   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [OrthoArray](Draft_OrthoArray/ru.md): создаёт ортогональный объект из выбранного объекта. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Polar Array](Draft_PolarArray/ru.md): создаёт массив в полярном узоре, то есть охватывающий угол. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Circular Array](Draft_CircularArray/ru.md): создает массив по круговой схеме, то есть от центра и двигаясь радиально наружу. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Массив по направляющей](Draft_PathArray/ru.md): создаёт массив объектов, помещая копии вдоль пути.
    -   <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> [Path LinkArray](Draft_PathLinkArray/ru.md): создаёт массив элементов [App::Link](Std_LinkMake/ru.md), помещая копии вдоль трассы. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point Array](Draft_PointArray/ru.md): создаёт массив объектов, где копии помещёны в заданных точках. <small>(v0.18)</small> 

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Правка](Draft_Edit/ru.md): редактировать выбранный объект.
-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Subelement highlight](Draft_SubelementHighlight/ru.md): входит в режим, позволяющий редактировать внутренние элементы объектов. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Join](Draft_Join/ru.md): объединяет линии в единую полилинию. <small>(v0.18)</small> 
-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Split](Draft_Split/ru.md): разделяет полилинию по точке на две. <small>(v0.18)</small> 
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Обновить](Draft_Upgrade/ru.md): обновляет объекты в объект более высокого уровня.
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Перестроить](Draft_Downgrade/ru.md): перестраивает объекты в объекты более низкого уровня.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [направляющая в BSpline](Draft_WireToBSpline/ru.md): Преобразовать полилинию в B-Сплайн и наоборот
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Преобразовать в эскиз](Draft_Draft2Sketch/ru.md): Преобразует объект Draft в эскиз верстака [Sketcher](Sketcher_Workbench/ru.md) и обратно
-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Slope](Draft_Slope/ru.md): изменяет угол возвышения выбранной в данный момент [линии](Draft_Line.md) или [полилинии](Draft_Wire/ru.md). <small>(v0.17)</small> 
-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [Flip Dimension](Draft_FlipDimension/ru.md): переворачивает ориентацию текста в [размере](Draft_Dimension/ru.md).

-   <img alt="" src=images/Draft_Shape2DView.png  style="width:32px;"> [2D вид фигуры](Draft_Shape2DView/ru.md): создаёт двумерный объект, представляющий собой плоскую проекцию другого трёхмерного объекта.

## Draft Tray {#draft_tray}

Панель инструментов Draft появляется когда стартует верстак, и позволяет выбрать рабочую плоскость, вместе с некоторыми визуальными параметрами вроде цвета линии, цвета фигур, размера текста, ширина линии, и автоматической группы.

![](images/Draft_tray_default.png )

Its tools are also available in the {{MenuCommand|Draft → Utilities}} menu:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Выбор плоскости](Draft_SelectPlane/ru.md): устанавливает вашу рабочую плоскость для следующих операций из стандартного вида либо выбранной плоскости.
-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Переключить режим конструирования](Draft_ToggleConstructionMode/ru.md): включает и выключает режим конструирования в Draft.
-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [AutoGroup](Draft_AutoGroup/ru.md): автоматически помещает новый объект в данную [группу](Std_Group/ru.md) или [визуальную группу](Draft_VisGroup/ru.md). <small>(v0.17)</small> 
-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Применить текущий стиль](Draft_Apply/ru.md): устанавливает для выделенных объектов указанный цвет и длину линий.

-   <img alt="" src=images/Draft_SetStyle.svg  style="width:32px;"> [Set style](Draft_SetStyle.md): sets the default style for new objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off.

-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [AutoGroup](Draft_AutoGroup.md): changes the active [Draft Layer](Draft_Layer.md) or, optionally, the active [Std Group](Std_Group.md) or group-like [Arch](Arch_Workbench.md) object.

## Draft annotation scale widget {#draft_annotation_scale_widget}

With the [Draft annotation scale widget](Draft_annotation_scale_widget.md) the Draft annotation scale can be specified. <small>(v0.19)</small> 

![](images/Draft_annotation_scale_widget_button.png )

## Draft snap widget {#draft_snap_widget}

The [Draft snap widget](Draft_snap_widget.md) can be used as an alternative for the [Draft Snap toolbar](#Draft_snap_toolbar.md). <small>(v0.19)</small> 

![](images/Draft_snap_widget_button.png )

## Панель инструментов привязки Draft {#панель_инструментов_привязки_draft}

Панель инструментов [Draft Snap](Draft_Snap/ru.md) позволяет выбрать текущий режим привязки. Его кнопка остаётся ненажатой при активности режима.

-   <img alt="" src=images/Draft_ToggleSnap.svg  style="width:32px;"> [Toggle snap](Draft_ToggleSnap/ru.md): включает/выключает [привязку](Draft_Snap/ru.md).
-   <img alt="" src=images/Snap_Endpoint.svg  style="width:32px;"> [Endpoint](Draft_Endpoint/ru.md): привязка к конечным точкам линий, дуг и сегментов сплайна.
-   <img alt="" src=images/Snap_Midpoint.svg  style="width:32px;"> [Midpoint](Draft_Midpoint/ru.md): привязка к средней точке линий и дуговых сегментов.
-   <img alt="" src=images/Snap_Center.svg  style="width:32px;"> [Center](Draft_Center/ru.md): привязка к центральным точкам дуг и окружностей.
-   <img alt="" src=images/Snap_Angle.svg  style="width:32px;"> [Angle](Draft_Angle/ru.md): привязка к особым точкам окружностей и дуг под углом 45 ° и 90 °.
-   <img alt="" src=images/Snap_Intersection.svg  style="width:32px;"> [Intersection](Draft_Intersection/ru.md): привязка к пересечению двух отрезков линии или дуги. Наведите указатель мыши на два нужных объекта, чтобы активировать их привязки пересечения.
-   <img alt="" src=images/Snap_Perpendicular.svg  style="width:32px;"> [Perpendicular](Draft_Perpendicular/ru.md): на отрезках линии и дуги привязка перпендикулярно самой последней точке.
-   <img alt="" src=images/Snap_Extension.svg  style="width:32px;"> [Extension](Draft_Extension/ru.md): привязка к воображаемой линии, которая выходит за пределы конечных точек отрезков. Наведите указатель мыши на нужный объект, чтобы активировать его расширение привязки.
-   <img alt="" src=images/Snap_Parallel.svg  style="width:32px;"> [Parallel](Draft_Parallel/ru.md): привязка к воображаемой линии, параллельной отрезку. Наведите указатель мыши на нужный объект, чтобы активировать его параллельную привязку.
-   <img alt="" src=images/Snap_Special.svg  style="width:32px;"> [Special](Draft_Special/ru.md): привязка к специальным точкам, определенным объектом. <small>(v0.17)</small> 
-   <img alt="" src=images/Snap_Near.svg  style="width:32px;"> [Near](Draft_Near/ru.md): привязка к ближайшей точке или краю на ближайшем объекте.
-   <img alt="" src=images/Snap_Ortho.svg  style="width:32px;"> [Ortho](Draft_Ortho/ru.md): привязка к воображаемым линиям, которые пересекают последнюю точку и простираются на 0°, 45° и 90°.
-   <img alt="" src=images/Snap_Grid.svg  style="width:32px;"> [Grid](Draft_Grid/ru.md): привязка к пересечению линий сетки, если сетка видна.
-   <img alt="" src=images/Snap_WorkingPlane.svg  style="width:32px;"> [Working plane](Draft_WorkingPlane/ru.md): всегда помещает точку привязки к текущей [рабочей плоскости](Draft_SelectPlane/ru.md), даже если захвачена точка вне её.
-   <img alt="" src=images/Snap_Dimensions.svg  style="width:32px;"> [Dimensions](Draft_Dimensions/ru.md): показывает временные размеры X и Y при привязке.
-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Toggle grid](Draft_ToggleGrid/ru.md): включает/выключает видимость сетки.

## Сервисные инструменты {#сервисные_инструменты}

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Layer](Draft_Layer/ru.md): создаёт слой в текущем документе, в который можно добавить объект, чтобы контролировать его видимость и цвет. Заменяет [VisGroup](Draft_VisGroup/ru.md). <small>(v0.19)</small> 
-   <img alt="" src=images/Draft_VisGroup.svg  style="width:32px;"> [VisGroup](Draft_VisGroup/ru.md): создаёт в текущем документе VisGroup. {{Obsolete|0.19}}
-   <img alt="" src=images/Draft_SetWorkingPlaneProxy.svg  style="width:32px;"> [Set Working Plane Proxy](Draft_SetWorkingPlaneProxy/ru.md): создаёт промежуточный объект для хранения текущей позиции [рабочей плоскости](Draft_SelectPlane/ru.md). <small>(v0.17)</small> 
-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Переключить режим отображения](Draft_ToggleDisplayMode/ru.md): переключить режим отображения выбранных объектов между \"Flat Lines\" и \"Wireframe\".
-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Добавить в группу](Draft_AddToGroup/ru.md): быстро добавить выбранные объекты в существующую [группы](Std_Group/ru.md) или [визуальной группы](Draft_VisGroup/ru.md).
-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Выбрать группу](Draft_SelectGroup/ru.md): выбрать содержимое выбранной [группы](Std_Group/ru.md) или [визуальной группы](Draft_VisGroup/ru.md).
-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Add to Construction group](Draft_AddConstruction/ru.md): добавляет выделенные объекты в конструкционную группу. <small>(v0.17)</small> 
-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Heal](Draft_Heal/ru.md): исправляет проблемный объект Draft, найденный в очень старом файле.

## Меню Вспомогательные {#меню_вспомогательные}

Дополнительные инструменты доступны из меню {{MenuCommand|Draft → Вспомогательные}}, или через контекстное меню по правому клику мыши, зависящее от выбранного объекта.

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Переключить режим продолжения](Draft_ToggleContinueMode/ru.md): включает и выключает режим продолжения
-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> [Show snap bar](Draft_ShowSnapBar/ru.md): показывает или скрывает инструментальную панель [привязки](Draft_Snap/ru.md).

## Дополнительные возможности {#дополнительные_возможности}

-   [Работа с координатами вручную](Draft_Coordinates/ru.md): позволяет вводить координаты вручную, вместо указания их на экране.
-   [Геометрические ограничения](Draft_Constrain/ru.md): ограничивает указатель в горизонтальном или вертикальном перемещении относительно предыдущей точки.
-   [Привязка](Draft_Snap/ru.md): позволяет разместить новые точки на специальных частях существующих объектов или на сетке.
-   [Copy Mode](Draft_Copying/ru.md): Все инструменты редактирования могут либо модифицировать выделенный объект или создать его модифицированную копию. Нажатие и удержание **Alt** во время модификации объекта, то есть перемещения или вращения, создаёт копию при отпускании клавиши.
-   [Construction Mode](Draft_ToggleConstructionMode/ru.md): позволяет создавать отдельную от остальной геометрию, просто включая или выключая этот режим.
-   [Рабочая плоскость](Draft_SelectPlane/ru.md): позволяет задать плоскость в трёхмерном пространстве, где будут проводиться операции с плоскими фигурами

## Tree view context menu {#tree_view_context_menu}

The following additional options are available in the [Tree view](Tree_view.md) context menu:

### Selection options {#selection_options}

If there is a selection the context menu contains one additional sub-menu:

-    {{MenuCommand|Utilities}}: a subset of the tools available in the main Draft Utilities menu.

### Wire options {#wire_options}

For a [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) and [Draft BezCurve](Draft_BezCurve.md) this additional option is available:

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Flatten this wire: flattens the wire based on its internal geometry. This option currently does not work properly.

### Layer container options {#layer_container_options}

For a [Draft LayerContainer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> Merge layer duplicates: this option currently does not work.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Add new layer](Draft_Layer.md): adds a new layer to the current document.

### Layer options {#layer_options}

For a [Draft Layer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Activate this layer](Draft_AutoGroup.md): makes the selected layer the active layer.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select layer contents](Draft_SelectGroup.md): selects the objects inside the selected layer.

### Working plane proxy options {#working_plane_proxy_options}

For a [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) these additional options are available:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write camera position](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the camera settings stored in the working plane proxy.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write objects state](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the visibility state of objects stored in the working plane proxy.

## 3D view context menu {#d_view_context_menu}

The following additional options are available in the [3D view](3D_view.md) context menu:

### No-selection options {#no_selection_options}

If there is no selection the context menu contains one additional sub-menu:

-    {{MenuCommand|Utilities}}: a subset of the tools available in the main Draft Utilities menu.

### Selection options {#selection_options_1}

If there is a selection the context menu contains two additional sub-menus:

-    {{MenuCommand|Draft}}: tools for [drawing objects](#Drawing_objects.md) and [modifying objects](#Modifying_objects.md).

-    {{MenuCommand|Utilities}}: a subset of the tools available in the main Draft Utilities menu.

### Устаревшее

Эти инструменты удалены из интерфейса в v0.19, поскольку в них больше нет нужды.

-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Закончить линию](Draft_FinishLine/ru.md): завершает черчение текущей [полилинии](Draft_Wire/ru.md) или [сплайна](Draft_BSpline/ru.md) без их замыкания.
-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Замкнуть линию](Draft_CloseLine/ru.md): заканчивает черчение текущей [полилинии](Draft_Wire/ru.md) или [сплайна](Draft_BSpline/ru.md), и замыкает их.
-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Отменить последний сегмент](Draft_UndoLine/ru.md): отменяет последний сегмент [полилинии](Draft_Wire.md).

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Drawing](Draft_Drawing.md): writes selected objects to a [Drawing Workbench](Drawing_Workbench.md) page. {{Obsolete|0.17}}

These [3D view](3D_view.md) context menu options are still available when the [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) or [Draft BezCurve](Draft_BezCurve.md) command is active but will be removed in the near future:

-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Undo last segment](Draft_Wire#Options.md): use the {{button|<img src="images/Draft_UndoLine.svg" width=16px> Undo}} button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Finish line](Draft_Wire#Options.md): use the **<img src="images/Draft_FinishLine.svg" width=16px> Finish** button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Close line](Draft_Wire#Options.md): use the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button in the task panel of the command instead. {{Obsolete|0.20}}

## Настройки

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Preferences](Draft_Preferences/ru.md): общие настройки для рабочей плоскости и инструментов черчения.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Import-Export Preferences](Import_Export_Preference/ru.md): настройки, доступные для импорта и экспорта в различные форматы файлов.

## Форматы файлов {#форматы_файлов}

Эти функции предназначены для открытия, импорта или экспорта других форматов файлов. Открытие подразумевает открытие нового документа с содержимым файла, в то время как импортирование добавляет содержимое файла в текущий документ. Экспорт сохраняет выделенные объекты в файл. Если ничего не выбрано, будут экспортированы все объекты. Учитывайте, что задача модуля Draft - работа с плоскими объектами, так что процедуры импорта фокусируются на двумерных объектах, хотя форматы DXF и OCA так же поддерживают определения объектов в трёхмерном пространстве (объекты не обязательно плоские), они не импортируют объекты вроде сеток, трйхмерных поверхностей и так далее, а только линии, окружности, тексты или плоские фигуры. Ныне поддерживаемые форматы файлов: Верстак Draft позволяет FreeCAD импортировать и экспортировать следующие форматы файлов:

-   [Autodesk .DXF](Draft_DXF/ru.md): импорт и экспорт файлов [DXF (Drawing Exchange Format)](http://en.wikipedia.org/wiki/AutoCAD_DXF), созданных в двумерных приложениях САПР. Смотри так же [FreeCAD and DXF Import](FreeCAD_and_DXF_Import.md).
-   [Autodesk .DWG](Draft_DXF/ru.md): импорт и экспорт файлов DWG через экспортёр DXF при установленной утилите [ODA Converter](Extra_python_modules/ru.md). Смотри так же [FreeCAD and DWG Import](FreeCAD_and_DWG_Import/ru.md).
-   [SVG (геометрия)](Draft_SVG/ru.md): импорт и экспорт файлов [SVG (Scalable Vector Graphics)](http://ru.wikipedia.org/wiki/Scalable_Vector_Graphics), созданных в приложениях векторной графики
-   [формат Open Cad .OCA](Draft_OCA/ru.md): импорт и экспорт файлов OCA/GCAD, потенциально нового [формата файлов открытых САПР](http://groups.google.com/group/open_cad_format)
-   [формат Airfoil Data .DAT](Draft_DAT/ru.md): импорт файлов DAT, описывающих [профили Airfoil](http://www.ae.illinois.edu/m-selig/ads/coord_database.html).

### Установка импортёров {#установка_импортёров}

-   [FreeCAD and DWG Import](FreeCAD_and_DWG_Import/ru.md): импорт и экспорт файлов DWG
-   [FreeCAD and DXF Import](FreeCAD_and_DXF_Import/ru.md): импорт и экспорт файлов DXF

## Модульные тесты {#модульные_тесты}


**Смотри так же:**

[Test Workbench](Test_Workbench/ru.md).

Для запуска модульных тестов рабочей среды выполните следующие действия с терминала операционной системы. 
```python
freecad -t TestDraft
```

## Написание сценариев {#написание_сценариев}

Инструменты модуля Draft могут использоваться в [макросах](macros/ru.md) и в консоли [Python](Python/ru.md), используя [программный интерфейс Draft](Draft_API/ru.md).

Рабочая среда включает модуль для создания образцов всех объектов в новом документе. <small>(v0.19)</small> 

Используйте это, чтобы проверить, что все объекты произведены правильно. 
```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

Проверка кода этого модуля полезна, чтобы понять, как использовать интерфейс программирования. 
```python
$INSTALLDIR/Mod/Draft/drafttests/draft_test_objects.py
```

Где `$INSTALLDIR` это верхний уровень каталога, где установлена программа, например, в Linux это может быть `/usr/share/freecad`.

<img alt="" src=images/Draft_test_objects.png  style="width:500px;"> 
*Тестовые объекты [верстака Draft](Draft_Workbench/ru.md).*

## Учебники

-   [Руководство по Draft](Draft_tutorial/ru.md)
-   [Устаревшее руководство по Draft](Draft_tutorial_Outdated/ru.md)
-   [Руководство по инструменту Draft преобразования текста в кривые](Draft_ShapeString_tutorial/ru.md)





 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)

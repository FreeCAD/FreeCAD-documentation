
{{Page in progress}}

 

<img alt="Draft workbench icon" src=images/Workbench_Draft.svg  style="width:128px;">


{{TOCright}}

## Introduction

## 简介

您可以利用底图工作台来绘制简单的2D对象，再利用其提供的其他工具来修改这些对象。此工作台提供了工具来定义工作平面、网格。另外，还有一个snapping系统可助您精确地控制几何体的位置。

用户创建的2D对象能以类似于Inkscape或Autocad中的方式用于通用绘图。这些2D图形也可用作[零件工作台与](Part_Workbench.md)[建筑工作台等其他工作台所创](Arch_Workbench.md)3D对象的基本组件。另外，也可以将底图对象转换至[构图工作台](Sketcher_Workbench.md)，这意味着能够在[零件设计工作台中利用这些图形来创建实体](PartDesign_Workbench.md)。

FreeCAD是一款以3D建模为主的应用软件，这使它的2D工具并非如其他绘图程序那样高级。如果您的主要目的是复杂的2D绘图与处理[DXF文件](DXF.md)，并不是3D建模，那么不妨考虑一款关于技术制图的专用软件，例如[LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), TurboCad以及其他类似程序。

<img alt="Draft Workbench Example" src=images/Draft_Workbench_Example.png  style="width:400px;">

## 绘制对象

下面来介绍一些用于创建对象的工具。

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [线段（Line）](Draft_Line.md): 绘制两点间的线段。
-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [连线（Wire）](Draft_Wire.md): 绘制一条由多条线段构成的折线(polyline)。
-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [圆形（Circle）](Draft_Circle.md): 根据中心点与半径来绘制一个圆形。
-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [弧（Arc）](Draft_Arc.md): 根据中心点、半径、起始角度与结束角度来绘制一条弧。
-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [3点绘弧（Arc 3Points）](Draft_Arc_3Points.md): 根据圆周上的3点来绘制一条弧线段。 <small>(v0.19)</small> 
-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [椭圆形（Ellipse）](Draft_Ellipse.md): 根据两个角点来绘制一个椭圆形。
-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [多边形（Polygon）](Draft_Polygon.md): 根据中心点、半径与边数来绘制一个规则的多边形。
-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [矩形（Rectangle）](Draft_Rectangle.md): 根据两个角点来绘制一个多边形。
-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [文本（Text）](Draft_Text.md): 绘制一个多行文本注解。
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [维度注解（Dimension）](Draft_Dimension.md): 绘制一个维度注解。
-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B样条（BSpline）](Draft_BSpline.md): 根据一系列点来绘制一个B样条。
-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [点（Point）](Draft_Point.md): 插入一个点对象。
-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [ShapeString](Draft_ShapeString.md): 在给定位置插入一个由复合图形构成的字符串。
-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Facebinder](Draft_Facebinder.md): 根据已存在对象上所选定的面来创建一个新对象。
-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [贝塞尔曲线（Bezier Curve）](Draft_BezCurve.md): 根据一系列点来绘制一条贝塞尔曲线。
-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [三次贝塞尔曲线（Cubic Bezier Curve）](Draft_CubicBezCurve.md): 通过拖动两个点来绘制一条三次贝塞尔曲线。<small>(v0.19)</small> 
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [标签（Label）](Draft_Label.md): 设置一个箭头指向选定元素的标签。 <small>(v0.17)</small> 

## Annotation objects {#annotation_objects}

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Text](Draft_Text.md): draws a multi-line text annotation.
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimension](Draft_Dimension.md): draws a dimension annotation.
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Label](Draft_Label.md): places a label with an arrow pointing to a selected element.
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Annotation style editor](Draft_AnnotationStyleEditor.md): opens an editor to change the annotation style of these objects. <small>(v0.19)</small> 

## 修改对象

以下这些工具用来修改已存在的对象。这写工具处理的是用户选定的对象，如果没有选择待处理对象，系统会提醒你选择一个。

许多工具(移动, 旋转, 阵列等)也可用于处理实体对象([零件](Part_Workbench.md), [零件设计](PartDesign_Workbench.md), [建筑等](Arch_Workbench.md))。

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [移动（Move）](Draft_Move.md): 将对象移动到另一个地方。
-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [旋转（Rotate）](Draft_Rotate.md): 将对象从起始角度旋转到结束角度。
-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [偏移（Offset）](Draft_Offset.md): 将对象中的线段按特定距离进行偏移。
-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Trim/Extend (Trimex)](Draft_Trimex.md): trims or extends an object.
-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Join](Draft_Join.md): joins lines together into a single wire. <small>(v0.18)</small> 
-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Split](Draft_Split.md): splits a wire into two at a point. <small>(v0.18)</small> 
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Upgrade](Draft_Upgrade.md): upgrades objects into a higher-level object.
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Downgrade](Draft_Downgrade.md): downgrades objects into lower-level objects.
-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Scale](Draft_Scale.md): scales selected objects around a base point.
-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Edit](Draft_Edit.md): edits a selected object.
-   <img alt="" src=images/Draft_Edit_Improved.svg  style="width:32px;"> [Edit Improved](Draft_Edit_Improved.md): enters an edit mode that allows editing different objects. <small>(v0.19)</small> 
-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [Wire to BSpline](Draft_WireToBSpline.md): converts a wire to a B-Spline and vice-versa.
-   <img alt="" src=images/Draft_AddPoint.svg  style="width:32px;"> [Add point](Draft_AddPoint.md): adds a point to a wire or B-Spline.
-   <img alt="" src=images/Draft_DelPoint.svg  style="width:32px;"> [Delete point](Draft_DelPoint.md): deletes a point from a wire or B-Spline.
-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Shape 2D View](Draft_Shape2DView.md): creates a 2D object which is a flattened 2D view of a 3D object.
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Draft to Sketch](Draft_Draft2Sketch.md): converts a Draft object to a [Sketcher Workbench](Sketcher_Workbench.md) Sketch and vice-versa.
-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Array](Draft_Array.md): creates a polar or rectangular array from selected objects.
-   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path Array](Draft_PathArray.md): creates an array of objects by placing the copies along a path.
-   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point Array](Draft_PointArray.md): creates an array of objects by placing the copies at certain points. <small>(v0.18)</small> 
-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [克隆（Clone）](Draft_Clone.md): 对选定的对象进行克隆操作。
-   <img alt="" src=images/Draft_PutOnSheet.svg  style="width:32px;"> [绘制（Drawing）](Draft_Drawing.md): 将选定的对象写入[工程制图工作台页面](工程制图工作台.md)。
-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [镜像（Mirror）](Draft_Mirror.md): 对选定的对象进行镜像操作。
-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [拉伸（Stretch）](Draft_Stretch.md): 拉伸选定的对象。<small>(v0.17)</small> 

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clone](Draft_Clone.md): clones the selected objects.
-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> Array tools.
    -   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Ortho Array](Draft_OrthoArray.md): creates an orthogonal array from the selected object. It can also create [App Link](App_Link.md) copies. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Polar Array](Draft_PolarArray.md): creates an array in a polar pattern, that is, sweeping an angle. It can also create [App Link](App_Link.md) copies. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Circular Array](Draft_CircularArray.md): creates an array in a circular pattern, that is, starting from a center and moving outwards radially. It can also create [App Link](App_Link.md) copies. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path Array](Draft_PathArray.md): creates an array of objects by placing the copies along a path.
    -   <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> [Path LinkArray](Draft_PathLinkArray.md): like <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Path Array](Draft_PathArray.md), but creates [App Links](App_Link.md) instead of regular copies. <small>(v0.19)</small> 
    -   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point Array](Draft_PointArray.md): creates an array of objects by placing the copies at certain points.
    -   <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> [Point LinkArray](Draft_PointLinkArray.md): like <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Point Array](Draft_PointArray.md), but creates [App Links](App_Link.md) instead of regular copies. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Edit](Draft_Edit.md): edits a selected object.
-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Subelement highlight](Draft_SubelementHighlight.md): enters an edit mode that allows editing different objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Join](Draft_Join.md): joins lines together into a single wire.
-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Split](Draft_Split.md): splits a wire into two at a point.
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Upgrade](Draft_Upgrade.md): upgrades objects into a higher-level object.
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Downgrade](Draft_Downgrade.md): downgrades objects into lower-level objects.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [Wire to BSpline](Draft_WireToBSpline.md): converts a wire to a B-Spline and vice-versa.
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Draft to Sketch](Draft_Draft2Sketch.md): converts a Draft object to a [Sketcher Workbench](Sketcher_Workbench.md) Sketch and vice-versa.
-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Slope](Draft_Slope.md): changes the elevation slope of the currently selected [Draft Line](Draft_Line.md) or [Draft Wire](Draft_Wire.md).
-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [Flip Dimension](Draft_FlipDimension.md): flips the orientation of the text of a [Draft Dimension](Draft_Dimension.md).

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Shape 2D View](Draft_Shape2DView.md): creates a 2D object which is a flattened 2D view of a 3D object.

## Draft Tray {#draft_tray}

The [Draft Tray](Draft_Tray.md) allows selecting the working plane, defining style settings, toggling construction mode, and specifying the active layer or group.

![](images/Draft_tray_default.png )

Its tools are also available in the {{MenuCommand|Draft → Utilities}} menu:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Select Plane](Draft_SelectPlane.md): selects the current Draft working plane.

-   <img alt="" src=images/Draft_SetStyle.svg  style="width:32px;"> [Set style](Draft_SetStyle.md): sets the default style for new objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off.

-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [AutoGroup](Draft_AutoGroup.md): changes the active [Draft Layer](Draft_Layer.md) or, optionally, the active [Std Group](Std_Group.md) or group-like [Arch](Arch_Workbench.md) object.

## Draft annotation scale widget {#draft_annotation_scale_widget}

With the [Draft annotation scale widget](Draft_annotation_scale_widget.md) the Draft annotation scale can be specified. <small>(v0.19)</small> 

![](images/Draft_annotation_scale_widget_button.png )

## Draft snap widget {#draft_snap_widget}

The [Draft snap widget](Draft_snap_widget.md) can be used as an alternative for the [Draft Snap toolbar](#Draft_snap_toolbar.md). <small>(v0.19)</small> 

![](images/Draft_snap_widget_button.png )

## Draft Snap toolbar {#draft_snap_toolbar}

The Draft Snap toolbar allows selecting the active snap options. The buttons belonging to active options stay depressed. For general information about snapping see: [Draft Snap](Draft_Snap.md).

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Toggle snap](Draft_Snap_Lock.md): toggles [object snapping](Draft_Snap.md) globally on or off.
-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Endpoint](Draft_Snap_Endpoint.md): snaps to the endpoints of line, arc and spline segments.
-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Midpoint](Draft_Snap_Midpoint.md): snaps to the middle point of line and arc segments.
-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Center](Draft_Snap_Center.md): snaps to the center point of circles, arcs and faces, [WP proxies](Draft_WorkingPlaneProxy.md) and [Building parts](Arch_BuildingPart.md)
-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Angle](Draft_Snap_Angle.md): snaps to the special cardinal points of circles and arcs, at 45° and 90°.
-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Intersection](Draft_Snap_Intersection.md): snaps to the intersection of two line or arc segments. Hover the mouse over the two desired objects to activate their intersection snaps.
-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Perpendicular](Draft_Snap_Perpendicular.md): on line and arc segments, snaps perpendicularly to the latest point.
-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Extension](Draft_Snap_Extension.md): snaps on an imaginary line that extends beyond the endpoints of line segments. Hover the mouse over the desired object to activate its extension snap.
-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Parallel](Draft_Snap_Parallel.md): snaps on an imaginary line parallel to a line segment. Hover the mouse over the desired object to activate its parallel snap.
-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Special](Draft_Snap_Special.md): snaps on special points defined by the object.
-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Near](Draft_Snap_Near.md): snaps to the closest point or edge on the nearest object.
-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Ortho](Draft_Snap_Ortho.md): snaps on imaginary lines that cross the last point, and extend at 0°, 45° and 90°.
-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Grid](Draft_Snap_Grid.md): snaps to the intersections of the grid lines, if the grid is visible.
-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Working plane](Draft_Snap_WorkingPlane.md): always places the snapped point on the current [working plane](Draft_SelectPlane.md), even if you snap to a point outside that working plane.
-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Dimensions](Draft_Snap_Dimensions.md): shows temporary X and Y dimensions while snapping.
-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Toggle grid](Draft_ToggleGrid.md): toggles the visibility of the grid on or off.

## 实用工具

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Layer](Draft_Layer.md): creates a Layer in the current document, to which objects can be added to control object visibility and color. It replaces Draft VisGroup. <small>(v0.19)</small> 
-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Working Plane Proxy](Draft_WorkingPlaneProxy.md): create a proxy object to store the current [Working Plane](Draft_SelectPlane.md) position.
-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Toggle display mode](Draft_ToggleDisplayMode.md): switches the display mode of selected objects between \"Flat Lines\" and \"Wireframe\".
-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Add to group](Draft_AddToGroup.md): quickly adds selected objects to an existing [Std Group](Std_Group.md).
-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select group contents](Draft_SelectGroup.md): selects the contents of a selected [Std Group](Std_Group.md) or [Draft Layer](Draft_Layer.md).
-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Add to Construction group](Draft_AddConstruction.md): add selected objects to the Construction group.
-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Heal](Draft_Heal.md): heals problematic Draft objects found in very old files.

## Additional tools {#additional_tools}

其他工具可从{{MenuCommand|Draft → Utilities}}菜单处找到。或者右击当前的环境菜单（context menu），具体可用工具取决于当前所选对象。

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Toggle continue mode](Draft_ToggleContinueMode.md): toggles the Draft continue mode on or off.
-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Apply current style](Draft_ApplyStyle.md): applies the current style to selected objects and groups.
-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> [Show snap bar](Draft_ShowSnapBar.md): shows the [Draft Snap toolbar](#Draft_Snap_toolbar.md).

## 其他功能

-   [底图坐标（Coordinates）](Draft_Coordinates.md): 利用输入坐标的方式取代点击3D视图来定义一个新的点。
-   [底图约束（Constraining）](Draft_Constrain.md): 限制鼠标指针在相对于前一个点的水平方向或垂直方向上移动。
-   [底图捕捉（Snapping）](Draft_Snap.md): 将新添加的点定位于已存在对象上的特定位置或网格上。

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

## Obsolete tools {#obsolete_tools}

These commands are obsolete but still available:

-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Array](Draft_Array.md): creates a polar or rectangular array from selected objects. {{Obsolete|0.19}}

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Drawing](Draft_Drawing.md): writes selected objects to a [Drawing Workbench](Drawing_Workbench.md) page. {{Obsolete|0.17}}

These [3D view](3D_view.md) context menu options are still available when the [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) or [Draft BezCurve](Draft_BezCurve.md) command is active but will be removed in the near future:

-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Undo last segment](Draft_Wire#Options.md): use the {{button|<img src="images/Draft_UndoLine.svg" width=16px> Undo}} button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Finish line](Draft_Wire#Options.md): use the **<img src="images/Draft_FinishLine.svg" width=16px> Finish** button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Close line](Draft_Wire#Options.md): use the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button in the task panel of the command instead. {{Obsolete|0.20}}

## 首选项

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [底图首选项](Draft_Preferences.md): 针对工作平面与绘制工具的一般设置。
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [导入-导出首选项](Import_Export_Preference.md): 导入或导出不同格式文件的相关选项。

## 文件格式

底图模块为FreeCAD提供了下列格式文件的导出、导出服务：

-   [Autodesk .DXF](Draft_DXF.md): 导入或导出由2D CAD应用程序创建的[图形交换文件](http://en.wikipedia.org/wiki/AutoCAD_DXF)。参见[FreeCAD and DXF Import](FreeCAD_and_DXF_Import.md)。
-   [Autodesk .DWG](Draft_DXF.md): 在[ODA转换器安装完成后](Extra_python_modules#ODA_Converter_(previously_Teigha_Converter).md)，通过DXF导入工具导入或导出DWG文件。参见[FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md)。
-   [SVG](Draft_SVG.md): 导入或导出由矢量绘图应用程序创建的[可伸缩矢量图形](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics)文件。
-   [Open Cad format .OCA](Draft_OCA.md): 导入或导出OCA/GCAD文件，这是一种潜在的新式[开放CAD文件格式](http://groups.google.com/group/open_cad_format)。
-   [Airfoil Data Format .DAT](Draft_DAT.md): 导入DAT文件，此格式详情可参见[Airfoil profiles](http://www.ae.illinois.edu/m-selig/ads/coord_database.html)。

### Install importers {#install_importers}

-   [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md): Imports and exports DWG files
-   [FreeCAD and DXF Import](FreeCAD_and_DXF_Import.md): Imports and exports DXF files

## Unit tests {#unit_tests}


**See also:**

[Test Workbench](Test_Workbench.md).

To run the unit tests of the workbench execute the following from the operating system terminal. 
```python
freecad -t TestDraft
```

## 脚本

借助[Draft API即可在](Draft_API.md)[宏与](macros.md)[Python控制台中使用各种底图工具](Python.md)。

The workbench includes a module to create samples of all objects in a new document. <small>(v0.19)</small> 

Use this to test that all objects are produced correctly. 
```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

Inspecting the code of this module is useful to understand how to use the programming interface. 
```python
$INSTALLDIR/Mod/Draft/drafttests/draft_test_objects.py
```

Where `$INSTALLDIR` is the toplevel directory where the software was installed; for example, in Linux it may be `/usr/share/freecad`.

<img alt="" src=images/Draft_test_objects.png  style="width:500px;"> 
*Test objects for the [Draft Workbench](Draft_Workbench.md).*

## 有关教程

-   [底图教程](Draft_tutorial.md)
-   [底图教程（过期）](Draft_tutorial_Outdated.md)
-   [底图ShapeString教程](Draft_ShapeString_tutorial.md)





 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)

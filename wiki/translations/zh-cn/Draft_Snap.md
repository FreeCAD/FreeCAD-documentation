# Draft Snap/zh-cn
{{TOCright}}

## 描述


<div class="mw-translate-fuzzy">

在[底图工作台工具中](Draft_Workbench/zh-cn.md)，您可以通过指针单击3D视图来拾取图形中的点、距离、半径与角度。


</div>


<div class="mw-translate-fuzzy">

捕捉功能可用于[底图工作台与](Draft_Workbench.md)[建筑工作台（Arch Workbench）中的大多工具](Arch_Workbench.md)，利用捕捉工具栏中的**<img src="images/Snap_Lock.svg" width=16px> [Draft ToggleSnap](Draft_ToggleSnap.md)**按钮即可对此功能进行全局开启或关闭。而通过**View → Toolbars → Draft Snap**菜单便可以激活捕捉工具栏。通过点选捕捉工具栏中的各按钮，即可开启或关闭对应的捕捉方法。


</div>

![](images/Draft_Snap_Endpoint_example.png )


<div class="mw-translate-fuzzy">


*利用捕捉功能，令所绘线段垂直于另一线段*


</div>

## Snap tools 

These tools are available in the Draft Snap toolbar and in the [Draft snap widget](Draft_snap_widget.md).

Note that circular edges do not have to be full circles.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Snap Lock](Draft_Snap_Lock.md): enables or disables snapping globally.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Snap Endpoint](Draft_Snap_Endpoint.md): snaps to the endpoints of edges.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Snap Midpoint](Draft_Snap_Midpoint.md): snaps to the midpoint of straight and circular edges.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> _ and [Arch BuildingParts](Arch_BuildingPart.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Snap Angle](Draft_Snap_Angle.md): snaps to the special cardinal points on circular edges, at multiples of 30° and 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Snap Intersection](Draft_Snap_Intersection.md): snaps to the intersection of two edges.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Snap Perpendicular](Draft_Snap_Perpendicular.md): snaps to the perpendicular point on edges.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Snap Extension](Draft_Snap_Extension.md): snaps to an imaginary line that extends beyond the endpoints of straight edges.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Snap Parallel](Draft_Snap_Parallel.md): snaps to an imaginary line parallel to straight edges.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Snap Special](Draft_Snap_Special.md): snaps to special points defined by the object.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Snap Near](Draft_Snap_Near.md): snaps to the nearest point on faces or edges.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Snap Ortho](Draft_Snap_Ortho.md): snaps to imaginary lines that cross the previous point at 0°, 45°, 90° and 135°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Snap Grid](Draft_Snap_Grid.md): snaps to the intersections of grid lines.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> _.

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Snap Dimensions](Draft_Snap_Dimensions.md): shows temporary X and Y dimensions.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Toggle Grid](Draft_ToggleGrid.md): switches the grid on or off.

## Advanced snapping 

-   Additional snap points can be obtained by combining two snap options. For example combining [Draft Snap Ortho](Draft_Snap_Ortho.md) and [Draft Snap Extension](Draft_Snap_Extension.md) will give you a snap point at the intersection of their imaginary lines.
-   Snapping can be combined with [constraining](Draft_Constrain.md).
-   Press **Q** to insert a \"hold point\" at the current location of the cursor. You can snap to the orthogonal axes of hold points, and to the intersections of these axes. If the [Draft Snap Midpoint](Draft_Snap_Midpoint.md) option is active, you can also snap to the midpoint between two hold points.
-   Press **** one or more times to snap to an object that is obscured by other geometry. This is called \"snap cycling\". Note that you must move the cursor by a small amount in the [3D view](3D_view.md) after pressing the key.

![](images/Draft_Snap_example_cycling_1.png ) *Snap cycling 1: The red rectangle was created first therefore it has snap priority. Without snap cycling you cannot snap to the green rectangle where it is overlapped by the red rectangle.*

![](images/Draft_Snap_example_cycling_2.png ) *Snap cycling 2: After using the snap cycle key once the green rectangle receives snap priority. Snapping to the midpoint of the overlapped green edge is now possible.*

## Notes


<div class="mw-translate-fuzzy">

同时采用多种捕捉方法，可能会便于您将对象绘制在预期位置上。但如果您的鼠标指针频繁被导向在一个错误的点上，那也许就是采用多种捕捉方法所带来的副作用，此时，请尝试仅采用一种捕捉方法。


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

Note that after changing some preferences you must restart FreeCAD.

-   When a _ command.
-   To only snap when the **Snap mod** key is held down:
    -   Deselect: **Edit → Preferences... → Draft → Grid and snapping → Snapping → Always snap (disable snap mod)**.
    -   The default **Snap mod** key, **Ctrl**, can be changed: **Edit → Preferences... → Draft → Grid and snapping → Snapping → Snap mod**.
-   To only show the Draft Snap toolbar when a command is active:
    -   Select: **Edit → Preferences... → Draft → Grid and snapping → Snapping → Show Draft Snap toolbar**.
    -   Select: **Edit → Preferences... → Draft → Grid and snapping → Snapping → Hide Draft Snap toolbar after use**.
-   The snap symbols can be changed: **Edit → Preferences... → Draft → Visual settings → Visual settings → Snap symbol style**.
-   The color of the snap symbols and the dimensions of [Draft Snap Dimensions](Draft_Snap_Dimensions.md) can be changed: **Edit → Preferences... → Draft → Visual settings → Visual settings → Color**.
-   The mentioned single character keyboard shortcuts can be changed: **Edit → Preferences... → Draft → User interface settings → In-Command Shortcuts**.

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap/zh-cn

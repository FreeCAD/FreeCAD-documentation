# Draft Snap/zh-cn
## 描述


<div class="mw-translate-fuzzy">

在[底图工作台](Draft_Workbench/zh-cn.md)工具中，您可以通过指针单击3D视图来拾取图形中的点、距离、半径与角度。


</div>


<div class="mw-translate-fuzzy">

捕捉功能可用于[底图工作台](Draft_Workbench.md)与[建筑工作台（Arch Workbench）](Arch_Workbench.md)中的大多工具，利用捕捉工具栏中的**<img src="images/Draft_Snap_Lock.svg" width=16px> [Draft ToggleSnap](Draft_Snap_Lock.md)**按钮即可对此功能进行全局开启或关闭。而通过**View → Toolbars → Draft Snap**菜单便可以激活捕捉工具栏。通过点选捕捉工具栏中的各按钮，即可开启或关闭对应的捕捉方法。


</div>

![](images/Draft_Snap_Endpoint_example.png )


<div class="mw-translate-fuzzy">



*利用捕捉功能，令所绘线段垂直于另一线段*


</div>

## Snap tools 

These tools are available in the Draft snap toolbar and in the [Draft snap widget](Draft_snap_widget.md).

Note that circular edges do not have to be full circles.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Snap lock](Draft_Snap_Lock.md): enables or disables snapping globally.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Snap endpoint](Draft_Snap_Endpoint.md): snaps to the endpoints of edges.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Snap midpoint](Draft_Snap_Midpoint.md): snaps to the midpoint of edges.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Snap center](Draft_Snap_Center.md): snaps to the center point of faces and circular edges, and to the **Placement** point of [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md) and [Arch BuildingParts](Arch_BuildingPart.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Snap angle](Draft_Snap_Angle.md): snaps to the special cardinal points on circular edges, at multiples of 30° and 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Snap intersection](Draft_Snap_Intersection.md): snaps to the intersection of two edges.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Snap perpendicular](Draft_Snap_Perpendicular.md): snaps to the perpendicular points on faces (<small>(v0.21)</small> ) and edges.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Snap extension](Draft_Snap_Extension.md): snaps to an imaginary line that extends beyond the endpoints of straight edges.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Snap parallel](Draft_Snap_Parallel.md): snaps to an imaginary line parallel to straight edges.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Snap special](Draft_Snap_Special.md): snaps to special points defined by the object.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Snap near](Draft_Snap_Near.md): snaps to the nearest point on faces and edges.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Snap ortho](Draft_Snap_Ortho.md): snaps to imaginary lines that cross the previous point at multiples of 45°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Snap grid](Draft_Snap_Grid.md): snaps to the intersections of grid lines.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Snap working plane](Draft_Snap_WorkingPlane.md): projects snap points onto the current [working plane](Draft_SelectPlane.md).

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Snap dimensions](Draft_Snap_Dimensions.md): shows temporary X and Y dimensions.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Toggle grid](Draft_ToggleGrid.md): changes the visibility of the grid.

## Advanced snapping 

-   Additional snap points can be obtained by combining two snap options. For example combining [Draft Snap Ortho](Draft_Snap_Ortho.md) and [Draft Snap Extension](Draft_Snap_Extension.md) will give you a snap point at the intersection of their imaginary lines.
-   Snapping can be combined with [constraining](Draft_Constrain.md).
-   Press **Q** to insert a \"hold point\" at the current location of the cursor. You can snap to the orthogonal axes of hold points, and to the intersections of these axes. If the [Draft Snap Midpoint](Draft_Snap_Midpoint.md) option is active, you can also snap to the midpoint between two hold points.
-   Press **** one or more times to snap to an object that is obscured by other geometry. This is called \"snap cycling\". Note that you must move the cursor by a small amount in the [3D view](3D_view.md) after pressing the key.

![](images/Draft_Snap_example_cycling_1.png ) 
*Snap cycling 1: The red rectangle was created first therefore it has snap priority. Without snap cycling you cannot snap to the green rectangle where it is overlapped by the red rectangle.*

![](images/Draft_Snap_example_cycling_2.png ) 
*Snap cycling 2: After using the snap cycle key once the green rectangle receives snap priority. Snapping to the midpoint of the overlapped green edge is now possible.*

## Notes


<div class="mw-translate-fuzzy">

同时采用多种捕捉方法，可能会便于您将对象绘制在预期位置上。但如果您的鼠标指针频繁被导向在一个错误的点上，那也许就是采用多种捕捉方法所带来的副作用，此时，请尝试仅采用一种捕捉方法。


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   When a [Draft](Draft_Workbench.md) or [BIM](BIM_Workbench.md) command requiring point input is active, the maximum distance at which [Draft Snap Grid](Draft_Snap_Grid.md) detects the intersections of grid lines can be changed on-the-fly by pressing **P** (increase key) or **M** (decrease key). This setting is stored: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Draft → snapRange**. It can also be changed in the task panel of the [Draft SelectPlane](Draft_SelectPlane.md) command.
-   To only snap when the **Snap modifier** key is held down:
    -   Deselect: **Edit → Preferences... → Draft → Grid and snapping → Always snap**.
    -   The default **Snap modifier** key, **Ctrl**, can be changed: **Edit → Preferences... → Draft → Grid and snapping → Snap modifier**.
-   To only show the Draft snap toolbar when a command is active select: **Edit → Preferences... → Draft → Interface → Only show the Draft snap toolbar during commands**. <small>(v1.0)</small> 
-   The snap symbols can be changed: **Edit → Preferences... → Draft → Grid and snapping → Snap symbol style**.
-   The color of the snap symbols and the dimensions of [Draft Snap Dimensions](Draft_Snap_Dimensions.md) can be changed: **Edit → Preferences... → Draft → Grid and snapping → Snap symbol color**.
-   The size of the snap symbols depends on: **Edit → Preferences... → Display → 3D View → Marker size**. <small>(v1.0)</small> 
-   The mentioned single character keyboard shortcuts can be changed: **Edit → Preferences... → Draft → Interface → In-command shortcuts**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap/zh-cn

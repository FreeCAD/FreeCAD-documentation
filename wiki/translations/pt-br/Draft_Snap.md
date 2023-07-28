# Draft Snap/pt-br
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}



## Descrição

In the <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft Workbench](Draft_Workbench.md) and the <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch Workbench](Arch_Workbench.md) you can create geometry by picking points in the [3D view](3D_view.md) or by entering coordinates in the [task panel](Task_panel.md) of commands. Another way of selecting points is by snapping. Snapping allows to select exact geometric points on, or defined by, existing objects or the grid. You can for example snap to the endpoint of a line, to the center of a circle, or to the intersection of two edges.

Snapping is available with most [Draft](Draft_Workbench.md) and [Arch](Arch_Workbench.md) commands.

![](images/Draft_Snap_Endpoint_example.png ) 
*Snapping to the endpoint of an edge*

## Snap tools 

These tools are available in the Draft snap toolbar and in the [Draft snap widget](Draft_snap_widget.md).

Note that circular edges do not have to be full circles.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Snap Lock](Draft_Snap_Lock.md): enables or disables snapping globally.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Snap Endpoint](Draft_Snap_Endpoint.md): snaps to the endpoints of edges.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Snap Midpoint](Draft_Snap_Midpoint.md): snaps to the midpoint of edges.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Snap Center](Draft_Snap_Center.md): snaps to the center point of faces and circular edges, and to the **Placement** point of [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md) and [Arch BuildingParts](Arch_BuildingPart.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Snap Angle](Draft_Snap_Angle.md): snaps to the special cardinal points on circular edges, at multiples of 30° and 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Snap Intersection](Draft_Snap_Intersection.md): snaps to the intersection of two edges.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Snap Perpendicular](Draft_Snap_Perpendicular.md): snaps to the perpendicular points on faces (<small>(v0.21)</small> ) and edges.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Snap Extension](Draft_Snap_Extension.md): snaps to an imaginary line that extends beyond the endpoints of straight edges.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Snap Parallel](Draft_Snap_Parallel.md): snaps to an imaginary line parallel to straight edges.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Snap Special](Draft_Snap_Special.md): snaps to special points defined by the object.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Snap Near](Draft_Snap_Near.md): snaps to the nearest point on faces and edges.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Snap Ortho](Draft_Snap_Ortho.md): snaps to imaginary lines that cross the previous point at multiples of 45°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Snap Grid](Draft_Snap_Grid.md): snaps to the intersections of grid lines.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Snap WorkingPlane](Draft_Snap_WorkingPlane.md): projects snap points onto the current [working plane](Draft_SelectPlane.md).

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Snap Dimensions](Draft_Snap_Dimensions.md): shows temporary X and Y dimensions.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Toggle Grid](Draft_ToggleGrid.md): switches the grid on or off.

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

-   Multiple snap options can be active at the same time, but it is advisable to only activate the snap options you really need. Activating too many can slow things down.
-   It is not a good idea to have [Draft Snap Near](Draft_Snap_Near.md) permanently active as it takes precedence over many other snap options.



## Preferências

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

Note that after changing some preferences you must restart FreeCAD.

-   When a [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) command requiring point input is active, the maximum distance at which [Draft Snap Grid](Draft_Snap_Grid.md) detects the intersections of grid lines can be changed on-the-fly by pressing **[** (increase key) or **]** (decrease key). This setting is stored: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Draft → snapRange**. It can also be changed in the task panel of the [Draft SelectPlane](Draft_SelectPlane.md) command.
-   To only snap when the **Snap mod** key is held down:
    -   Deselect: **Edit → Preferences... → Draft → Grid and snapping → Snapping → Always snap (disable snap mod)**.
    -   The default **Snap mod** key, **Ctrl**, can be changed: **Edit → Preferences... → Draft → Grid and snapping → Snapping → Snap mod**.
-   To only show the Draft snap toolbar when a command is active:
    -   Select: **Edit → Preferences... → Draft → Grid and snapping → Snapping → Show Draft snap toolbar**.
    -   Select: **Edit → Preferences... → Draft → Grid and snapping → Snapping → Hide Draft snap toolbar after use**.
-   The snap symbols can be changed: **Edit → Preferences... → Draft → Visual settings → Visual settings → Snap symbol style**.
-   The color of the snap symbols and the dimensions of [Draft Snap Dimensions](Draft_Snap_Dimensions.md) can be changed: **Edit → Preferences... → Draft → Visual settings → Visual settings → Color**.
-   The mentioned single character keyboard shortcuts can be changed: **Edit → Preferences... → Draft → User interface settings → In-Command Shortcuts**.


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap/pt-br

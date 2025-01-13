---
 GuiCommand:
   Name: Draft SelectPlane
   Name/ru: Draft SelectPlane
   MenuLocation: Draft , Utilities , Select Plane
   Workbenches: Draft_Workbench/ru, Arch_Workbench/ru
   Shortcut: **W** **P**
   SeeAlso: Draft_SetWorkingPlaneProxy/ru, Draft_ToggleGrid/ru
---

# Draft SelectPlane/ru


</div>



## Описание

The <img alt="" src=images/Draft_SelectPlane.svg  style="width:24px;"> **Draft SelectPlane** command defines the current Draft working plane. This is the plane in the [3D view](3D_view.md) where new [Draft](Draft_Workbench.md) objects are created. A working plane can be based on one of several [presets](#Usage_with_presets.md) or on a selection. The selection can be created before ([pre-selection](#Usage_with_pre-selection.md)) or after ([post-selection](#Usage_with_post-selection.md)) starting the command.


<small>(v1.0)</small> 

: For each 3D view a separate working plane is stored.

The ![](images/Draft_tray_button_plane.png ) button in the [Draft Tray](Draft_Tray.md) changes depending on the current working plane. <small>(v1.0)</small> : If the working plane is not set to **Auto** an asterisk (*****) is appended to the button label if the origin of the working plane does not match the global origin.

<img alt="" src=images/WorkingPlane_example.png  style="width:400px;"> 
*Shapes created on different working planes*

## Usage with pre-selection 

1.  Do one of the following:
    -   Select a single object. The following objects are supported:
        -   [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md): the **View Data** (the camera position) and the **Visibility Map** (the saved visibility of objects) of the working plane proxy are also restored.
        -   [Arch Axes](Arch_Axis.md) (<small>(v1.0)</small> )
        -   [Arch AxisSystems](Arch_AxisSystem.md) (<small>(v1.0)</small> )
        -   [Arch BuildingParts](Arch_BuildingPart.md)
        -   [Arch SectionPlanes](Arch_SectionPlane.md)
        -   [Std Parts](Std_Part.md): to avoid selecting subelements it is advisable to select these in the [Tree view](Tree_view.md).
        -   Non-solid objects that consist of a single flat face or a single curved edge, or (<small>(v1.0)</small> ) that have three or more vertices.
        -   Solid objects or objects without a shape that have a **Placement** property. (<small>(v1.0)</small> )
    -   Select one or more subelements. You can select:
        -   A flat face.
        -   A curved edge.
        -   Three vertices.
        -   An edge and a vertex, or two edges. The combined vertices must define a plane. (<small>(v1.0)</small> )
2.  There are several ways to invoke the command:
    -   Press the ![](images/Draft_tray_button_plane.png ) button in the [Draft Tray](Draft_Tray.md).
    -   [Draft](Draft_Workbench.md): Select the **Utilities → <img src="images/Draft_SelectPlane.svg" width=16px> Select plane** option from the menu, or from the [Tree view](Tree_view.md) or [3D view](3D_view.md) context menu.
    -   Draft: Use the keyboard shortcut: **W** then **P**.
3.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.

## Usage with post-selection 

1.  Invoke the command as explained above.
2.  The **Working plane setup** task panel opens. See [Options](#Options.md) for more information.
3.  Do one of the following:
    -   Select a single object. See the [previous paragraph](#Usage_with_pre-selection.md).
    -   Select one or more subelements. See the [previous paragraph](#Usage_with_pre-selection.md).
4.  Click anywhere in the [3D view](3D_view.md) to confirm the selection and finish the command.
5.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.

## Usage with presets 

1.  Invoke the command as explained above.
2.  The **Working plane setup** task panel opens. See [Options](#Options.md) for more information.
3.  Press any of the buttons to finish the command.
4.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.



## Опции

-   Press the **<img src="images/View-top.svg" width=16px> Top (XY)** button to align the working plane with the XY plane of the global coordinate system.
-   Press the **<img src="images/View-front.svg" width=16px> Front (XZ)** button to align the working plane with the XZ plane of the global coordinate system.
-   Press the **<img src="images/View-right.svg" width=16px> Side (YZ)** button to align the working plane with the YZ plane of the global coordinate system.
-   Press the **<img src="images/View-isometric.svg" width=16px> Align to view** button to align the working plane with the current [3D view](3D_view.md). If the **Center plane on view** checkbox is not checked the working plane origin will match the origin of the global coordinate system, else it will match the center of the current [3D view](3D_view.md).
-   Press the **<img src="images/View-axonometric.svg" width=16px> Automatic** button to set the working plane to **Auto**. A working plane set to **Auto** will automatically align with the current [3D view](3D_view.md) whenever a Draft or [BIM](BIM_Workbench.md) command requiring point input is started. This is equivalent to pressing the **<img src="images/View-isometric.svg" width=16px> Align to view** button before using the command. Additionally the working plane will align to planar faces that have been selected before starting the command, or when points on planar faces are picked during the command.
-   The **Offset** defines the perpendicular distance between the calculated plane and the actual working plane.
-   Check the **Center plane on view** checkbox to put the origin of the working plane in the center of to the current [3D view](3D_view.md). This option can be useful in combination with the **<img src="images/View-isometric.svg" width=16px> Align to view** button.
-   Select a vertex in the [3D view](3D_view.md) and press the **<img src="images/Draft_Move.svg" width=16px> Move working plane** button to move the working plane so that its origin matches the position of the selected vertex.
-   The **Grid color** button allows to quickly change the color of the grid. <small>(v1.0)</small> 
-   The **Grid spacing** defines the distance between grid lines.
-   The **Major lines every** value determines where major grid lines are drawn. Major grid lines are slightly thicker than minor grid lines. For example if the grid spacing is {{Value|0.5 m}} and there is a main line every {{Value|10 squares}}, such a line will occur every {{Value|5 m}}.
-   The **Grid size** value determines the number of squares in the X and Y direction of the grid.
-   The **Snapping radius** is the maximum distance at which [Draft Snap Grid](Draft_Snap_Grid.md) detects the intersections of grid lines.
-   Press the **<img src="images/view-fullscreen.svg" width=16px> Center view** button to align the [3D view](3D_view.md) with the current working plane.
-   Press the **<img src="images/sel-back.svg" width=16px> Previous** button to reset the working plane to its previous position.
-   Press the **Next <img src="images/sel-forward.svg" width=16px>** button to reset the working plane to its next position. <small>(v1.0)</small> 
-   Press **Esc** or the **Close** button to abort the command.

## Notes

-   It can be useful to align the [3D view](3D_view.md) with the selected Draft working plane. For example after switching the working plane to Front you may want to switch to the [Front view](Std_ViewFront.md) as well.
-   The grid can be toggled with the [Draft ToggleGrid](Draft_ToggleGrid.md) command.
-   By double-clicking [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md) in the [Tree view](Tree_view.md) you can quickly switch between working planes.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   The grid settings in the task panel as well as several other grid settings are available as preferences: **Edit → Preferences... → Draft → Grid and snapping**.
-   The Snapping radius can also be changed on-the-fly (see [Draft Snap](Draft_Snap#Preferences.md)) or by changing: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Draft → snapRange**.

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<small>(v1.0)</small> 

The WorkingPlane module offers two classes to create working plane objects: the `PlaneBase` class and the `PlaneGui` class. The second class inherits from the first. Objects of the `PlaneGui` class interact with the GUI (the [Draft Tray](Draft_Tray.md) button), the [3D view](3D_view.md) and the [grid](Draft_Snap_Grid.md). `PlaneBase` objects do not.

Use the `get_working_plane()` method of the WorkingPlane module to get an instance of the `PlaneGui` class linked to the current 3D view. The method either returns the existing working plane linked to the view or creates a new working plane if required.


```python
import FreeCAD as App
import WorkingPlane

wp = WorkingPlane.get_working_plane()

origin = App.Vector(0, 0, 0)
normal = App.Vector(1, 1, 1).normalize()
offset = 17
wp.align_to_point_and_axis(origin, normal, offset)

point = App.Vector(10, 15, 2)
projection = wp.project_point(point)
print(projection)
```

The `PlaneBase` class can be used to create working planes independent of the GUI:


```python
import WorkingPlane

wp = WorkingPlane.PlaneBase()
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SelectPlane/ru

---
- GuiCommand:
   Name:Draft SelectPlane
   MenuLocation:Utilities → Select Plane
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut:**W** **P**
   SeeAlso:[Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md)
---

# Draft SelectPlane

## Description

The <img alt="" src=images/Draft_SelectPlane.svg  style="width:24px;"> **Draft SelectPlane** command selects the current Draft working plane. This is the plane in the [3D view](3D_view.md) where new [Draft](Draft_Workbench.md) objects are created. A new working plane can be based on one of several [presets](#Usage_with_presets.md) or on a selection. The selection can be created before ([pre-selection](#Usage_with_pre-selection.md)) or after ([post-selection](#Usage_with_post-selection.md)) starting the command.

 <img alt="" src=images/WorkingPlane_example.png  style="width:400px;">  
*Shapes created on different working planes*

## Usage with pre-selection 

1.  Do one of the following:
    -   Select a single object. The following objects are supported:
        -   [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md): the **View Data** (the camera position) and the **Visibility Map** (the saved visibility of objects) of the working plane proxy are also restored.
        -   [Arch BuildingParts](Arch_BuildingPart.md).
        -   [Arch SectionPlanes](Arch_SectionPlane.md).
        -   _.
        -   [Part Feature](Part_Feature.md) objects that have a single face. [Part Planes](Part_Plane.md) for example.
        -   Objects that are not [Part Feature](Part_Feature.md) objects and have a **Placement** property.
    -   Select one or more subelements. You can select:
        -   A flat face.
        -   Three vertices.
        -   A circular edge.
        -   Two straight edges that are co-planar but not co-linear.
        -   A straight edge and a vertex that does not lie on the (extended) edge.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft SelectPlane](Draft_SelectPlane.md)** button in the [Draft Tray](Draft_Tray.md). Depending on the current working plane this button can look different.
    -   Select the **Utilities → <img src="images/Draft_SelectPlane.svg" width=16px> Select Plane** option from the menu.
    -   Use the keyboard shortcut: **W** then **P**.
3.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.

## Usage with post-selection 

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft SelectPlane](Draft_SelectPlane.md)** button in the [Draft Tray](Draft_Tray.md). Depending on the current working plane this button can look different.
    -   Select the **Utilities → <img src="images/Draft_SelectPlane.svg" width=16px> Select Plane** option from the menu.
    -   Use the keyboard shortcut: **W** then **P**.
2.  The **Working plane setup** task panel opens. See [Options](#Options.md) for more information.
3.  Do one of the following:
    -   Select a single object. See the [previous paragraph](#Usage_with_pre-selection.md) for the supported objects.
    -   Select one or more subelements. You can select:
        -   A flat face.
        -   Three vertices.
4.  Click anywhere in the [3D view](3D_view.md) to confirm the selection and finish the command.
5.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.

## Usage with presets 

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft SelectPlane](Draft_SelectPlane.md)** button in the [Draft Tray](Draft_Tray.md). Depending on the current working plane this button can look different.
    -   Select the **Utilities → <img src="images/Draft_SelectPlane.svg" width=16px> Select Plane** option from the menu.
    -   Use the keyboard shortcut: **W** then **P**.
2.  The **Working plane setup** task panel opens. See [Options](#Options.md) for more information.
3.  Press any of the buttons to finish the command.
4.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.

## Options

-   Press the **<img src="images/View-top.svg" width=16px> Top (XY)** button to align the working plane with the XY plane of the global coordinate system.
-   Press the **<img src="images/View-front.svg" width=16px> Front (XZ)** button to align the working plane with the XZ plane of the global coordinate system.
-   Press the **<img src="images/View-right.svg" width=16px> Side (YZ)** button to align the working plane with the YZ plane of the global coordinate system.
-   Press the **<img src="images/View-isometric.svg" width=16px> Align to view** button to align the working plane with the current [3D view](3D_view.md). If the **Center plane on view** checkbox is unchecked the working plane origin will match the origin of the global coordinate system, else it will match the center of the current [3D view](3D_view.md).
-   Press the **<img src="images/View-axonometric.svg" width=16px> Automatic** button to automatically align the working plane with the current [3D view](3D_view.md) whenever a Draft or [Arch](Arch_Workbench.md) command requiring point input is started. This is equivalent to pressing the **<img src="images/View-isometric.svg" width=16px> Align to view** button before using the command.
-   The **Offset** defines the perpendicular distance between the calculated plane and the actual working plane.
-   Check the **Center plane on view** checkbox to put the origin of the working plane in the center of to the current [3D view](3D_view.md). This option really only makes sense if the **<img src="images/View-isometric.svg" width=16px> Align to view** button is used.
-   Select a vertex in the [3D view](3D_view.md) and press the **<img src="images/Draft_Move.svg" width=16px> Move working plane** button to move the working plane so that its origin matches the position of the selected vertex.
-   The **Grid spacing** defines the distance between grid lines.
-   The **Main line every** value determines where main grid lines are drawn. Main grid lines are slightly thicker than normal grid lines. For example if the grid spacing is {{Value|0.5 m}} and there is a main line every {{Value|10 lines}}, such a line will occur every {{Value|5 m}}.
-   The **Grid extension** value determines the number of grid lines in the X and Y direction of the grid.
-   The **Snapping radius** is the maximum distance at which [Draft Snap Grid](Draft_Snap_Grid.md) detects the intersections of grid lines.
-   Press the **<img src="images/view-fullscreen.svg" width=16px> Center view** button to use the origin of the current working plane as the center of the [3D view](3D_view.md).
-   Press the **<img src="images/edit-undo.svg" width=16px> Previous** button to reset the working plane to its previous position.
-   Press **Esc** or the {{button|Close}} button to abort the command.

## Notes

-   It can be useful to align the [3D view](3D_view.md) with the selected Draft working plane. For example after switching the working plane to Front you may want to switch to the [Front view](Std_ViewFront.md) as well.
-   The grid can be toggled with the [Draft ToggleGrid](Draft_ToggleGrid.md) command.
-   By double-clicking [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md) in the [Tree view](Tree_view.md) you can quickly switch between working planes.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   The grid settings in the task panel as well as several other grid settings are available as preferences: **Edit → Preferences... → Draft → Grid and snapping → Grid**.
-   To use the grid the **Edit → Preferences... → Draft → Grid and snapping → Grid → Use grid** option must be selected. After changing this preference you must restart FreeCAD.
-   The Snapping radius can also be changed on-the-fly (see [Draft Snap](Draft_Snap#Preferences.md)) or by changing: **Tools → Edit parameters... → BaseApp → Preferences → Mod → Draft → snapRange**.

## Scripting

See also: _.

If the [Draft Workbench](Draft_Workbench.md) is active the FreeCAD application object has a `DraftWorkingPlane` property which stores the current Draft working plane. You can access this property and apply transformations to it:

 
```python
# This code only works if the Draft Workbench is active!

import FreeCAD as App
import FreeCADGui as Gui

workplane = App.DraftWorkingPlane

v1 = App.Vector(0, 0, 0)
v2 = App.Vector(1, 1, 1).normalize()

workplane.alignToPointAndAxis(v1, v2, 17)
Gui.Snapper.toggleGrid()
Gui.Snapper.toggleGrid()
```

It is also possible to create planes independently of the Draft working plane. This can be useful for calculations and projections:

 
```python
import WorkingPlane

my_plane = WorkingPlane.plane()

v1 = App.Vector(0, 0, 0)
v2 = App.Vector(1, 1, 1).normalize()
my_plane.alignToPointAndAxis(v1, v2, 17)

projection = my_plane.projectPoint(App.Vector(10, 15, 2))
print(projection)
```

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SelectPlane

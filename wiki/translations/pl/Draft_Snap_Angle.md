---
- GuiCommand:
   Name:Draft Snap Angle
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   SeeAlso:[Draft Snap](Draft_Snap.md), [Draft Snap Lock](Draft_Snap_Lock.md)
---

# Draft Snap Angle/pl

## Description

The <img alt="" src=images/Draft_Snap_Angle.svg  style="width:24px;"> **Draft Snap Angle** option snaps to the special cardinal points on circular edges, at multiples of 30° and 45°. The edges can belong to [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) objects but also to objects created with other [workbenches](Workbenches.md).

In FreeCAD version 0.19 and earlier this snap option only works properly for circular edges on a plane parallel to the XY plane of the global coordinate system.

![](images/Draft_Snap_Angle_example.png ) 
*Snapping the second point of a line to the -30° point on a circular edge. The small magenta circles indicate all available special cardinal points.*

## Usage

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
2.  If **Draft Snap Angle** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_Angle.svg" width=16px>** button in the Draft Snap toolbar.
    -   Press the **<img src="images/Draft_Snap_Lock.svg" width=16px><img src="images/Toolbar_flyout_arrow.svg" width=8px>** button in the [Draft snap widget](Draft_snap_widget.md) and in the menu select the **<img src="images/Draft_Snap_Angle.svg" width=16px> Snap Angle** option.
3.  Choose a [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) command to create your geometry.
4.  Note that you can also change snap options while a command is active.
5.  Move the cursor over a circular edge.
6.  The edge is highlighted.
7.  If a cardinal point is found the point is marked and the <img alt="" src=images/Draft_Snap_Angle.svg  style="width:16px;"> icon is displayed near the cursor.
8.  Optionally move the cursor closer to another cardinal point to select that point instead.
9.  Click to confirm the point.

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Angle/pl

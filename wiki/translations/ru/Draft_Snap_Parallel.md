---
- GuiCommand:/ru
   Name:Draft Parallel
   Name/ru:Draft Parallel
   MenuLocation:Черчение → [Привязка](Draft_Snap/ru.md) → Параллельно
   Workbenches:[Draft](Draft_Workbench/ru.md), [Arch](Arch_Workbench/ru.md)
   Shortcut:
   SeeAlso:
---

# Draft Snap Parallel/ru


</div>

## Description

The <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:24px;"> **Draft Snap Parallel** option snaps to an imaginary line parallel to straight edges. The edges can belong to [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) objects but also to objects created with other [workbenches](Workbenches.md).

Up to two edges can be referenced by this snap option and [Draft Snap Extension](Draft_Snap_Extension.md), making it possible to snap to virtual intersections. Both snap options can also be combined with other snap options.

This snap option currently does not work if the cursor is next to the referenced edge. You must move the cursor to an area beyond the endpoints of the edge.

![](images/Draft_Snap_Parallel_example.png ) 
*Snapping the second point of a line to an invisible line that is parallel to an edge*

## Usage

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
2.  If **Draft Snap Parallel** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_Parallel.svg" width=16px>** button in the Draft Snap toolbar.
    -   Press the **<img src="images/Draft_Snap_Lock.svg" width=16px><img src="images/Toolbar_flyout_arrow.svg" width=8px>** button in the [Draft snap widget](Draft_snap_widget.md) and in the menu select the **<img src="images/Draft_Snap_Parallel.svg" width=16px> Snap Parallel** option.
3.  Choose a [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) command to create your geometry.
4.  Note that you can also change snap options while a command is active.
5.  Pick a first point. This snap option requires a previous point. The parallel snap line will pass through this point.
6.  Move the cursor over a straight edge.
7.  The edge is highlighted.
8.  If you now move the cursor around the previous point you will notice a \"magnetic\" effect when the cursor is on the parallel snap line.
9.  The point is marked and the <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:16px;"> icon is displayed near the cursor.
10. Click to confirm the point.

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).

---
[documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Parallel/ru

---
 GuiCommand:
   Name: Draft Snap Midpoint
   MenuLocation: Snapping , Snap midpoint
   Workbenches: Draft_Workbench, BIM_Workbench
   SeeAlso: Draft_Snap, Draft_Snap_Lock
---

# Draft Snap Midpoint/en

## Description

The <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> **Draft Snap Midpoint** option snaps to the midpoint of edges. The edges can belong to [Draft](Draft_Workbench.md) or [BIM](BIM_Workbench.md) objects but also to objects created with other [workbenches](Workbenches.md).

![](images/Draft_Snap_Midpoint_example.png ) 
*Snapping the second point of a line to the midpoint of an edge*

## Usage

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
2.  If **Draft Snap Midpoint** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_Midpoint.svg" width=16px> [Snap midpoint](Draft_Snap_Midpoint.md)** button in the Draft snap toolbar.
    -   [Draft](Draft_Workbench.md): Hold down the **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button in the [Draft snap widget](Draft_snap_widget.md) and in the menu that opens select the **<img src="images/Draft_Snap_Midpoint.svg" width=16px> Snap midpoint** option.
    -   [BIM](BIM_Workbench.md): Select the **Snapping → <img src="images/Draft_Snap_Midpoint.svg" width=16px> Snap midpoint** option from the menu, or from the [3D view](3D_view.md) context menu.
3.  Choose a Draft or BIM command to create your geometry.
4.  Note that you can also change snap options while a command is active.
5.  Move the cursor over an edge.
6.  The edge is highlighted.
7.  If a midpoint is found the point is marked and the <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:16px;"> icon is displayed near the cursor.
8.  Click to confirm the point.

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Midpoint/en

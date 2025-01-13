---
 GuiCommand:
   Name: Draft Snap Grid
   MenuLocation: Snapping , Snap grid
   Workbenches: Draft_Workbench, BIM_Workbench
   SeeAlso: Draft_Snap, Draft_Snap_Lock, Draft_ToggleGrid, Draft_SelectPlane
---

# Draft Snap Grid/en

## Description

The <img alt="" src=images/Draft_Snap_Grid.svg  style="width:24px;"> **Draft Snap Grid** option snaps to the intersections of grid lines.

![](images/Draft_Snap_Grid_example.png ) 
*Snapping the second point of a line to the grid*

## Usage

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Optionally change the [working plane and/or the grid](Draft_SelectPlane.md).
2.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
3.  If **Draft Snap Grid** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_Grid.svg" width=16px> [Snap grid](Draft_Snap_Grid.md)** button in the Draft snap toolbar.
    -   [Draft](Draft_Workbench.md): Hold down the **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button in the [Draft snap widget](Draft_snap_widget.md) and in the menu that opens select the **<img src="images/Draft_Snap_Grid.svg" width=16px> Snap grid** option.
    -   [BIM](BIM_Workbench.md): Select the **Snapping → <img src="images/Draft_Snap_Grid.svg" width=16px> Snap grid** option from the menu, or from the [3D view](3D_view.md) context menu.
4.  Choose a Draft or BIM command to create your geometry.
5.  Note that you can also change snap options while a command is active.
6.  If required use [Draft ToggleGrid](Draft_ToggleGrid.md) to display the grid. The grid must be visible for this snap option to work.
7.  Move the cursor near the intersection of two grid lines.
8.  If an intersection is found the point is marked and the <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> icon is displayed near the cursor.
9.  Click to confirm the point.

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).

-   Several grid preferences are available: **Edit → Preferences... → Draft → Grid and snapping**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Grid/en

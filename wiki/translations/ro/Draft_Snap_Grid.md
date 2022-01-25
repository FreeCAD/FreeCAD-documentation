---
- GuiCommand:/ro
   Name/ro:Draft Grid
   Icon:Snap_Grid.svg
   MenuLocation:Draft → [Snapping](Draft_Snap.md) → Grid
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   SeeAlso:[[Draft ToggleGrid/ro]], [[Draft Snap/ro]]
---

# Draft Snap Grid/ro


</div>

## Description

The <img alt="" src=images/Draft_Snap_Grid.svg  style="width:24px;"> **Draft Snap Grid** option snaps to the intersections of grid lines. The grid can only be used if the **Use grid** preference is selected. See [Preferences](#Preferences.md).

![](images/Draft_Snap_Grid_example.png ) 
*Snapping the second point of a line to the grid*

## Usage


{{Draft Tools navi/ro}}

1.  Optionally change the [working plane and/or the grid](Draft_SelectPlane.md).
2.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
3.  If **Draft Snap Grid** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_Grid.svg" width=16px>** button in the Draft Snap toolbar.
    -   Press the **<img src="images/Draft_Snap_Lock.svg" width=16px><img src="images/Toolbar_flyout_arrow.svg" width=8px>** button in the [Draft snap widget](Draft_snap_widget.md) and in the menu select the **<img src="images/Draft_Snap_Grid.svg" width=16px> Snap Grid** option.
4.  Choose a [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) command to create your geometry.
5.  Note that you can also change snap options while a command is active.
6.  In FreeCAD version 0.19 and 0.20 the grid is now displayed if it was not yet visible. In previous versions you may have to [toggle the grid](Draft_ToggleGrid.md) to make it visible.
7.  Move the cursor near the intersection of two grid lines.
8.  If an intersection is found the point is marked and the <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> icon is displayed near the cursor.
9.  Click to confirm the point.


{{Userdocnavi/ro}}

See [Draft Snap](Draft_Snap#Preferences.md).

-   To use the grid select: **Edit → Preferences... → Draft → Grid and snapping → Grid → Use grid**. After changing this preference you must restart FreeCAD.
-   Several other grid preferences are also available: **Edit → Preferences... → Draft → Grid and snapping → Grid**.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Grid/ro

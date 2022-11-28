---
- GuiCommand   *
   Name   *Draft Snap Grid
   Workbenches   *[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   SeeAlso   *[Draft Snap](Draft_Snap.md), [Draft Snap Lock](Draft_Snap_Lock.md), [Draft ToggleGrid](Draft_ToggleGrid.md), [Draft SelectPlane](Draft_SelectPlane.md)
---

# Draft Snap Grid/pt-br

## Descrição

The <img alt="" src=images/Draft_Snap_Grid.svg  style="width   *24px;"> **Draft Snap Grid** option snaps to the intersections of grid lines. The grid can only be used if the **Use grid** preference is selected. See [Preferences](#Preferences.md).

![](images/Draft_Snap_Grid_example.png ) 
*Snapping the second point of a line to the grid*

## Utilização

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Optionally change the [working plane and/or the grid](Draft_SelectPlane.md).
2.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width   *16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
3.  If **Draft Snap Grid** is not active do one of the following   *
    -   Press the **<img src="images/Draft_Snap_Grid.svg" width=16px>** button in the Draft snap toolbar.
    -   Hold down the **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button in the [Draft snap widget](Draft_snap_widget.md) and in the menu that opens select the **<img src="images/Draft_Snap_Grid.svg" width=16px> Snap Grid** option.
4.  Choose a [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) command to create your geometry.
5.  Note that you can also change snap options while a command is active.
6.  The grid is now displayed if it was not yet visible.
7.  Move the cursor near the intersection of two grid lines.
8.  If an intersection is found the point is marked and the <img alt="" src=images/Draft_Snap_Grid.svg  style="width   *16px;"> icon is displayed near the cursor.
9.  Click to confirm the point.

## Preferências

See [Draft Snap](Draft_Snap#Preferences.md).

-   To use the grid select   * **Edit → Preferences... → Draft → Grid and snapping → Grid → Use grid**. After changing this preference you must restart FreeCAD.
-   Several other grid preferences are also available   * **Edit → Preferences... → Draft → Grid and snapping → Grid**.


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Grid/pt-br

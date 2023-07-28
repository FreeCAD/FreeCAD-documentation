---
- GuiCommand:/ru
   Name:Draft Snap Perpendicular
   Name/ru:Draft Perpendicular
   MenuLocation:Черчение → [Привязка](Draft_Snap/ru.md) → Нормаль
   Workbenches:[Draft](Draft_Workbench/ru.md), [Arch](Arch_Workbench/ru.md)
   Shortcut:
   SeeAlso:
---

# Draft Snap Perpendicular/ru


</div>

## Description


<div class="mw-translate-fuzzy">

### Описание


</div>

This snap option will also find points on extended faces and edges.

![](images/Draft_Snap_Perpendicular_example.png ) 
*Snapping the second point of a line to the perpendicular point on an extended edge*

## Usage

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
2.  If **Draft Snap Perpendicular** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_Perpendicular.svg" width=16px>** button in the Draft snap toolbar.
    -   Hold down the **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button in the [Draft snap widget](Draft_snap_widget.md) and in the menu that opens select the **<img src="images/Draft_Snap_Perpendicular.svg" width=16px> Snap Perpendicular** option.
3.  Choose a [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) command to create your geometry.
4.  Note that you can also change snap options while a command is active.
5.  Pick a first point. This snap option requires a previous point. The perpendicular point will be determined in relation to this point.
6.  Move the cursor over a face or edge.
7.  The face or edge is highlighted.
8.  If a perpendicular point is found the point is marked and the <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:16px;"> icon is displayed near the cursor.
9.  If there are multiple perpendicular points: optionally move the cursor closer to another perpendicular point. <small>(v0.21)</small> 
10. Click to confirm the point.

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Perpendicular/ru

---
- GuiCommand:
   Name:Draft Snap Special
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Version:0.17
   SeeAlso:[Draft Snap](Draft_Snap.md), [Draft Snap Lock](Draft_Snap_Lock.md)
---

# Draft Snap Special/en

## Description

The <img alt="" src=images/Draft_Snap_Special.svg  style="width:24px;"> **Draft Snap Special** option snaps to [special points](#Supported_special_points.md) defined by the object. The supported objects are [Arch Walls](Arch_Wall.md), [Arch Structures](Arch_Structure.md) and [Arch Equipment](Arch_Equipment.md).

![](images/Draft_Snap_Special_example.png ) 
*Snapping the second point of a line to a special point of an  Arch Wall, which is a vertex of its Base object*

## Usage

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
2.  If **Draft Snap Special** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_Special.svg" width=16px>** button in the Draft Snap toolbar.
    -   Press the **<img src="images/Draft_Snap_Lock.svg" width=16px><img src="images/Toolbar_flyout_arrow.svg" width=8px>** button in the [Draft snap widget](Draft_snap_widget.md) and in the menu select the **<img src="images/Draft_Snap_Special.svg" width=16px> Snap Special** option.
3.  Choose a [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) command to create your geometry.
4.  Note that you can also change snap options while a command is active.
5.  Move the cursor over a supported object.
6.  The object is highlighted.
7.  If a special point is found the point is marked and the <img alt="" src=images/Draft_Snap_Special.svg  style="width:16px;"> icon is displayed near the cursor.
8.  If the object has multiple special points: optionally move the cursor closer to another special point.
9.  Click to confirm the point.

## Supported special points 

-   The vertices of the **Base** object of <img alt="" src=images/Arch_Wall.svg  style="width:16px;"> [Arch Walls](Arch_Wall.md).
-   The **Placement** point of <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [Arch Structures](Arch_Structure.md).
-   The **Snap Points** of <img alt="" src=images/Arch_Equipment.svg  style="width:16px;"> [Arch Equipment](Arch_Equipment.md).

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Special/en

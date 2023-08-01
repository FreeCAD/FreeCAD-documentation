---
- GuiCommand:
   Name:Draft Snap Dimensions
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   SeeAlso:[Draft Snap](Draft_Snap.md), [Draft Snap Lock](Draft_Snap_Lock.md), [Draft SelectPlane](Draft_SelectPlane.md)
---

# Draft Snap Dimensions

## Description

The <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:24px;"> **Draft Snap Dimensions** option shows temporary X and Y dimensions. They display the X and Y distance between the cursor and the previous point in the [working plane](Draft_SelectPlane.md) coordinate system. The dimensions are created on the [working plane](Draft_SelectPlane.md).

 <img alt="" src=images/Draft_Snap_Dimensions_example.png  style="width:400px;">  
*Temporary dimensions show the position of the cursor*

## Usage

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Optionally change the [working plane](Draft_SelectPlane.md).
2.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
3.  If **Draft Snap Dimensions** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_Dimensions.svg" width=16px>** button in the Draft snap toolbar.
    -   Press the **<img src="images/Draft_Snap_Dimensions.svg" width=16px>** button in the [Draft snap widget](Draft_snap_widget.md).
4.  Choose a [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) command to create your geometry.
5.  Note that you can also change snap options while a command is active.
6.  Pick a first point. This snap option requires a previous point.
7.  As you move the cursor around temporary dimensions are displayed.

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Dimensions

# Draft Snap Dimensions/ru
---
 GuiCommand:
   Name: Draft Snap Dimensions
   Name/ru: Draft Snap Dimensions
   MenuLocation: Черчение, Draft Snap/ru , Размеры
   Workbenches: Draft_Workbench/ru, Arch_Workbench/ru
   Shortcut: 
   SeeAlso: ---


</div>

## Description

The <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:24px;"> **Draft Snap Dimensions** option shows temporary X and Y dimensions. They display the X and Y distance between the cursor and the previous point in the [working plane](Draft_SelectPlane.md) coordinate system. The dimensions are created on the [working plane](Draft_SelectPlane.md).

<img alt="" src=images/Draft_Snap_Dimensions_example.png  style="width:400px;"> 
*Temporary dimensions show the position of the cursor*

## Usage

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Optionally change the [working plane](Draft_SelectPlane.md).
2.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
3.  If **Draft Snap Dimensions** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_Dimensions.svg" width=16px> [Snap dimensions](Draft_Snap_Dimensions.md)** button in the Draft snap toolbar.
    -   [Draft](Draft_Workbench.md): Press the **<img src="images/Draft_Snap_Dimensions.svg" width=16px> [Snap dimensions](Draft_Snap_Dimensions.md)** button in the [Draft snap widget](Draft_snap_widget.md).
    -   [BIM](BIM_Workbench.md): Select the **Snapping → <img src="images/Draft_Snap_Dimensions.svg" width=16px> Snap dimensions** option from the menu, or from the [3D view](3D_view.md) context menu.
4.  Choose a Draft or BIM command to create your geometry.
5.  Note that you can also change snap options while a command is active.
6.  Pick a first point. This snap option requires a previous point.
7.  As you move the cursor around temporary dimensions are displayed.

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Dimensions/ru

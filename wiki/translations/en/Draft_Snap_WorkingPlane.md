---
 GuiCommand:
   Name: Draft Snap WorkingPlane
   MenuLocation: Snapping , Snap working plane
   Workbenches: Draft_Workbench, BIM_Workbench
   SeeAlso: Draft_Snap, Draft_Snap_Lock, Draft_SelectPlane
---

# Draft Snap WorkingPlane/en

## Description

The <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:24px;"> **Draft Snap WorkingPlane** option projects snap points onto the current [working plane](Draft_SelectPlane.md). It can only be used in combination with another snap option.

![](images/Draft_Snap_WorkingPlane_example.png ) 
*Snapping the second point of a line to the projected endpoint of an edge*

## Usage

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Optionally change the [working plane](Draft_SelectPlane.md).
2.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
3.  If **Draft Snap WorkingPlane** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_WorkingPlane.svg" width=16px> [Snap working plane](Draft_Snap_WorkingPlane.md)** button in the Draft snap toolbar.
    -   [Draft](Draft_Workbench.md): Press the **<img src="images/Draft_Snap_WorkingPlane.svg" width=16px> [Snap working plane](Draft_Snap_WorkingPlane.md)** button in the [Draft snap widget](Draft_snap_widget.md).
    -   [BIM](BIM_Workbench.md): Select the **Snapping → <img src="images/Draft_Snap_WorkingPlane.svg" width=16px> Snap working plane** option from the menu, or from the [3D view](3D_view.md) context menu.
4.  Make sure at least one other snap option is active.
5.  Choose a Draft or BIM command to create your geometry.
6.  Note that you can also change snap options while a command is active.
7.  Move the cursor over the object you want to snap to.
8.  The object is highlighted.
9.  If a snap point is found it is projected onto the [working plane](Draft_SelectPlane.md) where it is marked.
10. Click to confirm the point.

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap WorkingPlane/en

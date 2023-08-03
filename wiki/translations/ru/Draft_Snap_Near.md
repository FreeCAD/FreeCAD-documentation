---
 GuiCommand:
   Name: Draft Snap Near
   Name/ru: Draft Snap Near
   MenuLocation: Черчение , Draft Snap/ru , Ближайшие
   Workbenches: Draft_Workbench/ru, Arch_Workbench/ru
   Shortcut: 
   SeeAlso: 
---

# Draft Snap Near/ru


</div>

## Description

The <img alt="" src=images/Draft_Snap_Near.svg  style="width:24px;"> **Draft Snap Near** option snaps to the nearest point on faces and edges. The faces and edges can belong to [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) objects but also to objects created with other [workbenches](Workbenches.md).

![](images/Draft_Snap_Near_example.png ) 
*Snapping the second point of a line to the nearest point on an edge*

## Usage

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
2.  If **Draft Snap Near** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_Near.svg" width=16px>** button in the Draft snap toolbar.
    -   Hold down the **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button in the [Draft snap widget](Draft_snap_widget.md) and in the menu that opens select the **<img src="images/Draft_Snap_Near.svg" width=16px> Snap Near** option.
3.  Choose a [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) command to create your geometry.
4.  Note that you can also change snap options while a command is active.
5.  Move the cursor over a face or edge.
6.  The face or edge is highlighted.
7.  If a nearest point is found the point is marked.
8.  Optionally move the cursor along the face or edge to select a different nearest point.
9.  Click to confirm the point.

## Notes

-   It is not a good idea to have [Draft Snap Near](Draft_Snap_Near.md) permanently active as it takes precedence over many other snap options.
-   In {{VersionMinus|0.20}} when snapping to curves, [Draft Snap Near](Draft_Snap_Near.md) snaps to their segmented representation in the [3D view](3D_view.md) which results in an inaccuracy. To get an exact on-curve point draw a [Draft Line](Draft_Line.md) across the curve and then cut the line with [Draft Trimex](Draft_Trimex.md) using the curve as a cutting tool.

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Near/ru

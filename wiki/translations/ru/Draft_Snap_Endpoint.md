# Draft Snap Endpoint/ru
---
 GuiCommand:
   Name: Draft Endpoint
   Name/ru: Draft Endpoint
   MenuLocation: Черчение , Draft Snap/ru , Конечные точки
   Workbenches: Draft_Workbench/ru, Arch_Workbench/ru
   Shortcut: 
   SeeAlso: ---


</div>

## Description

The <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:24px;"> **Draft Snap Endpoint** option snaps to the endpoints of edges. The edges can belong to [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) objects but also to objects created with other [workbenches](Workbenches.md).

![](images/Draft_Snap_Endpoint_example.png ) 
*Snapping the second point of a line to the endpoint of an edge*

## Usage

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
2.  If **Draft Snap Endpoint** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_Endpoint.svg" width=16px>** button in the Draft snap toolbar.
    -   Hold down the **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button in the [Draft snap widget](Draft_snap_widget.md) and in the menu that opens select the **<img src="images/Draft_Snap_Endpoint.svg" width=16px> Snap Endpoint** option.
3.  Choose a [Draft](Draft_Workbench.md) or [Arch](Arch_Workbench.md) command to create your geometry.
4.  Note that you can also change snap options while a command is active.
5.  Move the cursor over an edge.
6.  The edge is highlighted.
7.  If an endpoint is found the point is marked and the <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:16px;"> icon is displayed near the cursor.
8.  Optionally move the cursor closer to the other endpoint to select that point instead.
9.  Click to confirm the point.

## Preferences

See [Draft Snap](Draft_Snap#Preferences.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Endpoint/ru

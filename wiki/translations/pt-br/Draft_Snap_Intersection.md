---
 GuiCommand:
   Name: Draft Snap Intersection
   MenuLocation: Snapping , Snap intersection
   Workbenches: Draft_Workbench, BIM_Workbench
   SeeAlso: Draft_Snap, Draft_Snap_Lock
---

# Draft Snap Intersection/pt-br



## Descrição

The <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:24px;"> **Draft Snap Intersection** option snaps to the intersection of two edges. The edges can belong to [Draft](Draft_Workbench.md) or [BIM](BIM_Workbench.md) objects but also to objects created with other [workbenches](Workbenches.md).

This snap option will also find apparent intersections of (extended) straight edges if <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:16px;"> [Draft Snap WorkingPlane](Draft_Snap_WorkingPlane.md) is active as well.

![](images/Draft_Snap_Intersection_example.png ) 
*Snapping the second point of a line to the intersection of two edges*



## Utilização

For general information about snapping see [Draft Snap](Draft_Snap.md).

1.  Make sure snapping is enabled. See <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Snap Lock](Draft_Snap_Lock.md).
2.  If **Draft Snap Intersection** is not active do one of the following:
    -   Press the **<img src="images/Draft_Snap_Intersection.svg" width=16px> [Snap intersection](Draft_Snap_Intersection.md)** button in the Draft snap toolbar.
    -   [Draft](Draft_Workbench.md): Hold down the **<img src="images/Draft_Snap_Lock.svg" width=x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button in the [Draft snap widget](Draft_snap_widget.md) and in the menu that opens select the **<img src="images/Draft_Snap_Intersection.svg" width=16px> Snap intersection** option.
    -   [BIM](BIM_Workbench.md): Select the **Snapping → <img src="images/Draft_Snap_Intersection.svg" width=16px> Snap intersection** option from the menu, or from the [3D view](3D_view.md) context menu.
3.  Choose a Draft or BIM command to create your geometry.
4.  Note that you can also change snap options while a command is active.
5.  Move the cursor over one of the edges that intersect.
6.  The edge is highlighted.
7.  Move the cursor over the other edge.
8.  The edge is highlighted.
9.  If an intersection is found the point is marked and the <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:16px;"> icon is displayed near the cursor.
10. If the edges have multiple intersections: optionally move the cursor closer to another intersection.
11. Click to confirm the point.



## Preferências

See [Draft Snap](Draft_Snap#Preferences.md).


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Intersection/pt-br

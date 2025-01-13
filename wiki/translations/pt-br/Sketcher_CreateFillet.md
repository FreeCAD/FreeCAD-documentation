# Sketcher CreateFillet/pt-br
---
 GuiCommand:-br   Name: Sketcher CreateFillet   Name/pt-br: Sketcher CreateFillet   Workbenches: Sketcher Workbench/pt-br   Sketcher|Shortcut: F   MenuLocation: Sketch , Sketcher geometries , Create fillet---


</div>

## Description

The <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:24px;"> [Sketcher CreateFillet](Sketcher_CreateFillet.md) tool creates a fillet between two non-parallel edges. <small>(v1.0)</small> : The tool can also create a chamfer.


<small>(v1.0)</small> 

: If two straight edges connected by a [Coincident constraint](Sketcher_ConstrainCoincident.md) are filleted or chamfered, the corner point can optionally be preserved. The tool then adds a [Point object](Sketcher_CreatePoint.md) that has a [Point on object constraint](Sketcher_ConstrainPointOnObject.md) with both edges. Constraints connected to the corner point are transferred to the new point object.

![](images/SketcherCreateFilletExample.png‎ )

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_CreateFillet.svg" width=16px> [Create fillet](Sketcher_CreateFillet.md)** button.
    -   Select the **Sketcher → Sketcher tools → <img src="images/Sketcher_CreateFillet.svg" width=16px> Create fillet** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_CreateFillet.svg" width=16px> Create fillet** option from the context menu.
    -   Use the keyboard shortcut: **G** then **F**, then **F**.
2.  If there is a previous selection it is cleared. The tool does not accept a pre-selection.
3.  The cursor changes to a cross with the current tool mode icon.
4.  The **Fillet/Chamfer parameters** section (<small>(v1.0)</small> ) is added at the top of the [Sketcher Dialog](Sketcher_Dialog.md).
5.  Optionally press the **U** key or uncheck the **Preserve corner** checkbox to disable that option. <small>(v1.0)</small> 
6.  Optionally press the **M** key or select from the dropdown list in the parameters section to change the tool mode:
    -   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:16px;"> 
**Fillet**
    -   <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:16px;"> 
**Chamfer**
7.  Do one of the following:
    -   Pick a point with a [Coincident constraint](Sketcher_ConstrainCoincident.md) connecting two non-parallel straight edges.
    -   Pick two non-parallel edges. Either edge can be a straight [line](Sketcher_CreateLine.md), an [arc](Sketcher_CreateArc.md), an [arc of ellipse](Sketcher_CreateArcOfEllipse.md), an [arc of hyperbola](Sketcher_CreateArcOfHyperbola.md) or an [arc of parabola](Sketcher_CreateArcOfParabola.md). [B-splines](Sketcher_Workbench#Sketcher_CompCreateBSpline.md) are currently not supported.
8.  The fillet or chamfer is created, including a point object in case of a preserved corner. For a chamfer a construction geometry arc is also created.
9.  This tool always runs in continue mode: optionally keep selecting points and/or edges.
10. To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

## Notes

-   The construction geometry arc of a chamfer is not visible outside the sketch. It cannot be deleted without breaking the geometry of the chamfer.
-   Some ([conic](Sketcher_Workbench#Sketcher_CompCreateConic.md)) curves may need to be [trimmed](Sketcher_Trimming.md) before they can be filleted.
-   The fillet radius depends on the selection method. If a [Coincident constraint](Sketcher_ConstrainCoincident.md) connecting two straight edges is selected, the fillet radius is derived from the length of the shortest edge. If two edges are selected the radius is the distance from the first clicked point to the (extended) intersection of the edges.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateFillet/pt-br

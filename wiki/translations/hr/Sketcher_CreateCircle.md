---
 GuiCommand:
   Name: Sketcher CreateCircle
   MenuLocation: Sketch , Sketcher geometries , Create circle by center
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **C**
   SeeAlso: Sketcher_CreateArc
---

# Sketcher CreateCircle/hr

## Description

The <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:24px;"> [Sketcher CreateCircle](Sketcher_CreateCircle.md) tool creates a circle by its center and a point along the circle. <small>(v1.0)</small> : Or optionally by three points along the circle.

![](images/Sketcher_CircleExample1.png‎ )

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences#General.md). <small>(v1.0)</small> 
Dim-OVP = Dimensional On-View-Parameters. <small>(v1.0)</small> 

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_CreateCircle.svg" width=16px> [Center and rim point](Sketcher_CreateCircle.md)** button.
    -   Select the **Sketcher → Sketcher geometries → <img src="images/Sketcher_CreateCircle.svg" width=16px> Create circle by center** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_CreateCircle.svg" width=16px> Create circle by center** option from the context menu.
    -   Use the keyboard shortcut: **G** then **C**.
2.  The cursor changes to a cross with the current tool mode icon.
3.  The **Circle parameters** section (<small>(v1.0)</small> ) is added at the top of the [Sketcher Dialog](Sketcher_Dialog.md).
4.  Optionally press the **M** key or select from the dropdown list in the parameters section to change the tool mode:
    -   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:16px;"> **Center**:
        1.  Pick the center of the circle. Or with Pos-OVP: enter its X and/or Y coordinate.
        2.  Pick a point to define the radius of the circle. Or with Dim-OVP: enter this radius.
    -   <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:16px;"> **3 rim points**: <small>(v1.0)</small> 
        1.  Pick three points to define the circle. Or with Pos-OVP: enter their X and/or Y coordinates. No constraints are created for these points.
5.  The circle is created and applicable Pos-OVP and Dim-OVP based constraints are added.
6.  If the tool runs in [continue mode](Sketcher_Workbench#Continue_modes.md):
    1.  Optionally keep creating circles.
    2.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateCircle/hr

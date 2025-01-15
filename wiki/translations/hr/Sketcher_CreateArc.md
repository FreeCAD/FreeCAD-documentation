---
 GuiCommand:
   Name: Sketcher CreateArc
   MenuLocation: Sketch , Sketcher geometries , Create arc by center
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **A**
   SeeAlso: Sketcher_CreateCircle
---

# Sketcher CreateArc/hr

## Description

The <img alt="" src=images/Sketcher_CreateArc.svg  style="width:24px;"> [Sketcher CreateArc](Sketcher_CreateArc.md) tool creates an arc by its center and its endpoints. <small>(v1.0)</small> : Or optionally by its endpoints and a point along the arc.

<img alt="" src=images/Sketcher_ArcExample3.png  style="width:400px;"> 
*Arc created in Center mode with automatically applied constraints defined by entering all On-View-Parameters*

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences#General.md). <small>(v1.0)</small> 
Dim-OVP = Dimensional On-View-Parameters. <small>(v1.0)</small> 

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_CreateArc.svg" width=16px> [Center and endpoints](Sketcher_CreateArc.md)** button.
    -   Select the **Sketcher → Sketcher geometries → <img src="images/Sketcher_CreateArc.svg" width=16px> Create arc by center** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_CreateArc.svg" width=16px> Create arc by center** option from the context menu.
    -   Use the keyboard shortcut: **G** then **A**.
2.  The cursor changes to a cross with the current tool mode icon.
3.  The **Arc parameters** section (<small>(v1.0)</small> ) is added at the top of the [Sketcher Dialog](Sketcher_Dialog.md).
4.  Optionally press the **M** key or select from the dropdown list in the parameters section to change the tool mode:
    -   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:16px;"> **Center**:
        1.  Pick the center of the arc. Or with Pos-OVP: enter its X and/or Y coordinate.
        2.  Pick the start point of the arc, this also defines the radius. Or with Dim-OVP: enter the radius and/or start angle of the arc. The angle is relative to the X axis of the sketch. No constraint is created for this angle.
        3.  Pick the endpoint of the arc. Or with Dim-OVP: enter the aperture angle of the arc.
    -   <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:16px;"> **3 rim points**: <small>(v1.0)</small> 
        1.  Pick the start and end points of the arc. Or with Pos-OVP: enter their X and/or Y coordinates.
        2.  Pick another point to define the radius. Or with Pos-OVP: enter its X and/or Y coordinate. No constraints are created for this point.
5.  The arc is created and applicable Pos-OVP and Dim-OVP based constraints are added.
6.  If the tool runs in [continue mode](Sketcher_Workbench#Continue_modes.md):
    1.  Optionally keep creating arcs.
    2.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArc/hr

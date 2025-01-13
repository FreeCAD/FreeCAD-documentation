---
 GuiCommand:
   Name: Sketcher CreateArcSlot
   MenuLocation: Sketch , Sketcher geometries , Create arc slot
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **S** **2**
   Version: 1.0
   SeeAlso: Sketcher_CreateSlot
---

# Sketcher CreateArcSlot

## Description

The <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:24px;"> [Sketcher CreateArcSlot](Sketcher_CreateArcSlot.md) tool creates an arc slot, a closed polyline consisting of two parallel concentric arcs closed by two semicircles or two radial straight lines.

 <img alt="" src=images/Sketcher_CreateArcSlot_Example.png  style="width:300px;">  
*Arc slot with arc ends (left) and flat ends (right)*

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences#General.md).
Dim-OVP = Dimensional On-View-Parameters.

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_CreateArcSlot.svg" width=16px> [Create arc slot](Sketcher_CreateArcSlot.md)** button.
    -   Select the **Sketcher → Sketcher geometries → <img src="images/Sketcher_CreateArcSlot.svg" width=16px> Create arc slot** option from the menu.
    -   The keyboard shortcut: **G** then **S**, then **2**.
2.  The cursor changes to a cross with the tool icon.
3.  The **Arc Slot parameters** section is added at the top of the [Sketcher Dialog](Sketcher_Dialog.md).
4.  Optionally press the **M** key or select from the dropdown list in the parameters section to change the tool mode:
    -   <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:16px;"> **Arc ends**:
        1.  Pick the center of the arc slot. Or with Pos-OVP: enter its X and/or Y coordinate.
        2.  Pick the center of the first semicircle, this also defines the radius of the (virtual) centerline of the slot. Or with Dim-OVP: enter the radius and/or start angle of the slot. The angle is relative to the X axis of the sketch. No constraint is created for this angle.
        3.  Pick the center of the second semicircle. Or with Dim-OVP: enter the aperture angle of the centerline arc.
        4.  Pick a point to define the radius of the semicircles. Or with Dim-OVP: enter this radius.
    -   <img alt="" src=images/Sketcher_CreateRectangleSlot.svg  style="width:16px;"> **Flat ends**:
        1.  Pick the center of the arc slot. Or with Pos-OVP: enter its X and/or Y coordinate.
        2.  Pick the start point of the first arc, this also defines its radius. Or with Dim-OVP: enter the radius and/or start angle of the first arc. The angle is relative to the X axis of the sketch. No constraint is created for this angle.
        3.  Pick the end point of the first arc. Or with Dim-OVP: enter the aperture angle of the arc.
        4.  Pick a point to define the width of the slot. Or with Dim-OVP: enter this width.
5.  The slot is created and applicable Pos-OVP and Dim-OVP based constraints are added.
6.  If the tool runs in [continue mode](Sketcher_Workbench#Continue_modes.md):
    1.  Optionally keep creating slots.
    2.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

## Notes

-   The points picked to define either the radius of the semicircles or the offset of inner and outer arcs don\'t have to touch the geometry, the distance from the cursor to the slot center actually controls the value.
-   In **Arc ends** mode the first radius applies to a virtual center arc, while it applies to one of the outline arcs in **Flat ends** mode.
-   If the entered width value in **Flat ends** mode is positive the constrained arc becomes the inner arc, for a negative value it will be the outer arc.




 {{Sketcher_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcSlot

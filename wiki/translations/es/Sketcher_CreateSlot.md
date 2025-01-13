# Sketcher CreateSlot/es
---
 GuiCommand:   Name: Sketcher CreateSlot   Name/es: Sketcher CreateSlot   Workbenches: Sketcher Workbench/es   Sketcher|MenuLocation: Sketch , Sketcher geometries , Create slot   Shortcut:    SeeAlso: ---


</div>



## Descripción

The <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:24px;"> [Sketcher CreateSlot](Sketcher_CreateSlot.md) tool creates a slot, a closed polyline consisting of two semicircles connected by two parallel straight lines.

![](images/SketcherCreateSlotExample.png‎ )

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences#General.md). <small>(v1.0)</small> 
Dim-OVP = Dimensional On-View-Parameters. <small>(v1.0)</small> 

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_CreateSlot.svg" width=16px> [Create slot](Sketcher_CreateSlot.md)** button.
    -   Select the **Sketcher → Sketcher geometries → <img src="images/Sketcher_CreateSlot.svg" width=16px> Create Slot** option from the menu.
    -   The keyboard shortcut: **G** then **S**.
2.  The cursor changes to a cross with the tool icon.
3.  Pick the center of the first semicircle. Or with Pos-OVP: enter its X and/or Y coordinate.
4.  Pick the center of the second semicircle. Or with Dim-OVP: enter the distance between the centers and/or angle of the slot. The angle is relative to the X axis of the sketch.
5.  Pick a point to define the radius of the slot. Or with Dim-OVP: enter this radius.
6.  The slot is created and applicable Pos-OVP and Dim-OVP based constraints are added.
7.  If the tool runs in [continue mode](Sketcher_Workbench#Continue_modes.md):
    1.  Optionally keep creating slots.
    2.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

## Notes

-    {{VersionMinus|0.21}}(<small>(v0.20)</small> ): Holding **Ctrl** when picking the second center will constrain the slot to be drawn horizontally or vertically.

-    <small>(v1.0)</small> : [Angular snap](Sketcher_Snap.md) can be used to control the angle of the slot.

-    <small>(v0.20)</small> : A slot can also be constrained horizontally or vertically if the [Auto constraints](Sketcher_Workbench#Auto_constraints.md) option is enabled.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateSlot/es

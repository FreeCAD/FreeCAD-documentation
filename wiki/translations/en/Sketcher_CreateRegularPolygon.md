---
 GuiCommand:
   Name: Sketcher CreateRegularPolygon
   MenuLocation: Sketch , Sketcher geometries , Create regular polygon
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **P** **R**
---

# Sketcher CreateRegularPolygon/en

## Description

The <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:24px;"> [Sketcher CreateRegularPolygon](Sketcher_CreateRegularPolygon.md) tool creates a regular polygon.

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences#General.md). <small>(v1.0)</small> 
Dim-OVP = Dimensional On-View-Parameters. <small>(v1.0)</small> 

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_CreateRegularPolygon.svg" width=16px> [Regular polygon](Sketcher_CreateRegularPolygon.md)** button.
    -   Select the **Sketcher → Sketcher geometries → <img src="images/Sketcher_CreateRegularPolygon.svg" width=16px> Create regular polygon** option from the menu.
    -   Use the keyboard shortcut: **G** then **P**, then **R**.
2.  Enter the **Number of Sides** in the dialog that opens.
3.  The cursor changes to a cross with the tool icon.
4.  The **Polygon parameters** section (<small>(v1.0)</small> ) is added at the top of the [Sketcher Dialog](Sketcher_Dialog.md).
5.  Optionally change the number of **Sides** (this can also be done after picking the center):
    -   Enter a number greater than two.
    -   Press the **U** key to increase the number.
    -   Press the **J** key to decrease the number.
6.  Pick the center of the polygon. Or with Pos-OVP: enter its X and/or Y coordinate.
7.  Pick the first point of the polygon, this also defines the radius of the circumscribed circle. Or with Dim-OVP: enter the radius of the circle and/or the angle of the first point. The angle is relative to the X axis of the sketch. No constraint is created for this angle.
8.  The polygon is created, including a circumscribed construction geometry circle, and applicable Pos-OVP and Dim-OVP based constraints are added.
9.  If the tool runs in [continue mode](Sketcher_Workbench#Continue_modes.md):
    1.  Optionally keep creating polygons.
    2.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

## Notes

-   The construction geometry circle is not visible outside the sketch. It cannot be deleted without breaking the geometry of the polygon.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateRegularPolygon/en

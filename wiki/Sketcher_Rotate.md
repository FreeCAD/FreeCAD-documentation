---
 GuiCommand:
   Name: Sketcher Rotate
   MenuLocation: Sketch , Sketcher tools , Polar transform
   Workbenches: Sketcher_Workbench
   Shortcut: **Z** **P**
   Version: 1.0
   SeeAlso: 
---

# Sketcher Rotate

## Description

The <img alt="" src=images/Sketcher_Rotate.svg  style="width:24px;"> [Sketcher Rotate](Sketcher_Rotate.md) tool rotates or optionally creates rotated copies of selected elements. Copies are evenly distributed along the rotation angle.

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences#General.md).
Dim-OVP = Dimensional On-View-Parameters.

1.  Select one or more edges and/or [Point objects](Sketcher_CreatePoint.md). Constraints, except [Horizontal](Sketcher_ConstrainHorizontal.md) and [Vertical](Sketcher_ConstrainVertical.md) constraints, restricted to the selected elements are also processed. If the original elements are rotated, any other constraints associated with them will be deleted.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_Rotate.svg" width=16px> [Polar transform](Sketcher_Rotate.md)** button.
    -   Select the **Sketcher → Sketcher tools → <img src="images/Sketcher_Rotate.svg" width=16px> Polar transform** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_Rotate.svg" width=16px> Polar transform** option from the context menu.
    -   The keyboard shortcut: **Z** then **P**.
3.  The cursor changes to a cross with the tool icon.
4.  The **Rotate parameters** section is added at the top of the [Sketcher Dialog](Sketcher_Dialog.md).
5.  Optionally change the number of **Copies** (if the number is zero the original elements are rotated):
    -   Enter a number.
    -   Press the **U** key to increase the number.
    -   Press the **J** key to decrease the number.
6.  Optionally check the **Apply equal constraints** checkbox to exclude dimensional constraints from the operation, and instead apply <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:16px;"> [Equal constraints](Sketcher_ConstrainEqual.md) between the original objects and their copies.
7.  Pick the rotation center. Or with Pos-OVP: enter its X and/or Y coordinate.
8.  Pick a point to define the start angle. Or with Dim-OVP: enter it.
9.  Pick a point to define rotation angle. Or with Dim-OVP: enter it.
10. The original elements are rotated or rotated copies are created. No Pos-OVP or Dim-OVP based constraints are added.

## Notes

-   It can be advisable to use [Sketcher RemoveAxesAlignment](Sketcher_RemoveAxesAlignment.md) before using this tool.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Rotate

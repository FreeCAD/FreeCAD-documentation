---
 GuiCommand:
   Name: Sketcher Offset
   MenuLocation: Sketch , Sketcher tools , Offset geometry
   Workbenches: Sketcher_Workbench
   Shortcut: **Z** **T**
   Version: 1.0
   SeeAlso: 
---

# Sketcher Offset

## Description

The <img alt="" src=images/Sketcher_Offset.svg  style="width:24px;"> [Sketcher Offset](Sketcher_Offset.md) tool creates equidistant edges around selected edges.

 <img alt="" src=images/Sketcher_OffsetExample.png‎  style="width:400px;">  
*Equidistant edges around a closed (O) and an open (U) construction polyline*

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

Dim-OVP = Dimensional [On-View-Parameters](Sketcher_Preferences#General.md).

1.  Select one or more lines, circles and/or circular arcs.
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_Offset.svg" width=16px> [Offset geometry](Sketcher_Offset.md)** button.
    -   Select the **Sketcher → Sketcher tools → <img src="images/Sketcher_Offset.svg" width=16px> Offset geometry** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_Offset.svg" width=16px> Offset geometry** option from the context menu.
    -   Use the keyboard shortcut: **Z** then **T**.
3.  The cursor changes to a cross with the tool icon.
4.  The **Offset parameters** section is added at the top of the [Sketcher Dialog](Sketcher_Dialog.md).
5.  Optionally press the **U** key or check the **Delete original geometries** checkbox to only keep the new outline.
6.  Optionally press the **J** key or check the **Add offset constraint** checkbox to add a dimensional constraint between the offset outline and the original geometry.
7.  Optionally press the **M** key or select from the dropdown list in the parameters section to change the tool mode:
    -   <img alt="" src=images/Sketcher_OffsetArc.svg  style="width:16px;"> 
**Arc**
    -   <img alt="" src=images/Sketcher_OffsetIntersection.svg  style="width:16px;"> 
**Intersection**
8.  Pick a point to define the offset distance. Or with Dim-OVP: enter this distance.
9.  The geometry is created and if **Add offset constraint** has been selected a dimensional constraint is added.

## Limitations

This tool has certain limitations, mainly due to [OCC](OpenCASCADE.md) issues:

-   The following types of geometry are currently unsupported: ellipses, B-splines, hyperbolas and parabolas.
-   Offsetting a single line can yield unexpected results.
-   Open profiles are offset on both sides, creating a closed contour.
-   External geometry can\'t be offset directly.




 {{Sketcher_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Offset

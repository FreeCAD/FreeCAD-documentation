---
 GuiCommand:
   Name: Sketcher CreateArcOfHyperbola
   MenuLocation: Sketch , Sketcher geometries , Create arc of hyperbola
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **H**
   Version: 0.17
   SeeAlso: Sketcher_CreateArcOfParabola
---

# Sketcher CreateArcOfHyperbola/zh-cn

## Description

The <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:24px;"> [Sketcher CreateArcOfHyperbola](Sketcher_CreateArcOfHyperbola.md) tool creates an arc of hyperbola.

![](images/Sketcher_CreateArcOfHyperbola_Example.png ) 
*Arc of hyperbola (white) with internal geometry (dark yellow)*

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_CreateArcOfHyperbola.svg" width=16px> [Arc of hyperbola by center, vertex, endpoints](Sketcher_CreateArcOfHyperbola.md)** button.
    -   Select the **Sketcher → Sketcher geometries → <img src="images/Sketcher_CreateArcOfHyperbola.svg" width=16px> Create arc of hyperbola** option from the menu.
    -   Use the keyboard shortcut: **G** then **H**.
2.  The cursor changes to a cross with the tool icon.
3.  Pick the center of the major radius of the arc (labelled 1 in the image above).
4.  Pick the vertex of the arc (labelled 2 in the image above), this also defines its major radius.
5.  Pick the start point of the arc (labelled 3 or 4 in the image above), this also defines its curvature.
6.  Pick the endpoint of the arc (labelled 3 or 4 in the image above).
7.  The arc of hyperbola is created, including a set of internal geometry.
8.  If the tool runs in [continue mode](Sketcher_Workbench#Continue_modes.md):
    1.  Optionally keep creating arcs.
    2.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

## Notes

-   Elements of the internal geometry can be deleted. They can be recreated at any time with [Sketcher RestoreInternalAlignmentGeometry](Sketcher_RestoreInternalAlignmentGeometry.md).





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcOfHyperbola/zh-cn

---
 GuiCommand:
   Name: Sketcher CreateArcOfParabola
   MenuLocation: Sketch , Sketcher geometries , Create arc of parabola
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **J**
   Version: 0.17
   SeeAlso: Sketcher_CreateArcOfHyperbola
---

# Sketcher CreateArcOfParabola/zh-cn

## Description

The <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:24px;"> [Sketcher CreateArcOfParabola](Sketcher_CreateArcOfParabola.md) tool creates an arc of parabola.

![](images/Sketcher_CreateArcOfParabola_Example.png ) 
*Arc of parabola (white) with internal geometry (dark yellow)*

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_CreateArcOfParabola.svg" width=16px> [Arc of parabola by focus, vertex, endpoints](Sketcher_CreateArcOfParabola.md)** button.
    -   Select the **Sketcher → Sketcher geometries → <img src="images/Sketcher_CreateArcOfParabola.svg" width=16px> Create arc of parabola** option from the menu.
    -   Use the keyboard shortcut: **G** then **J**.
2.  The cursor changes to a cross with the tool icon.
3.  Pick the focus of the arc (labelled 1 in the image above).
4.  Pick the vertex of the arc (labelled 2 in the image above).
5.  Pick the start point of the arc (labelled 3 or 4 in the image above).
6.  Pick the endpoint of the arc (labelled 3 or 4 in the image above).
7.  The arc of parabola is created, including a set of internal geometry.
8.  If the tool runs in [continue mode](Sketcher_Workbench#Continue_modes.md):
    1.  Optionally keep creating arcs.
    2.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

## Notes

-   Elements of the internal geometry can be deleted. They can be recreated at any time with [Sketcher RestoreInternalAlignmentGeometry](Sketcher_RestoreInternalAlignmentGeometry.md).


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcOfParabola/zh-cn

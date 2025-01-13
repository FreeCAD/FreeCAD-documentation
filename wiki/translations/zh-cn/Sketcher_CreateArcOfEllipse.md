---
 GuiCommand:
   Name: Sketcher CreateArcOfEllipse
   MenuLocation: Sketch , Sketcher geometries , Create arc of ellipse
   Workbenches: Sketcher_Workbench
   Shortcut: **G** **E** **A**
   Version: 0.15
   SeeAlso: Sketcher_CreateEllipseByCenter
---

# Sketcher CreateArcOfEllipse/zh-cn



## 描述

The <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:24px;"> [Sketcher CreateArcOfEllipse](Sketcher_CreateArcOfEllipse.md) tool creates an arc of ellipse.

![](images/Sketcher_CreateArcOfEllipse_Example.png ) 
*Arc of ellipse (white) with internal geometry (dark yellow)*



## 用法

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

1.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_CreateArcOfEllipse.svg" width=16px> [Arc of ellipse by center, radius, endpoints](Sketcher_CreateArcOfEllipse.md)** button.
    -   Select the **Sketcher → Sketcher geometries → <img src="images/Sketcher_CreateArcOfEllipse.svg" width=16px> Create arc of ellipse** option from the menu.
    -   Use the keyboard shortcut: **G** then **E**, then **A**.
2.  The cursor changes to a cross with the tool icon.
3.  Pick the center of the arc.
4.  Pick an endpoint of one of the axes of the arc, this also defines one of its radii.
5.  Pick the start point of the arc, this also defines the other radius of the arc.
6.  Pick the endpoint of the arc.
7.  The arc of ellipse is created, including a set of internal geometry (major axis, minor axis and two foci).
8.  If the tool runs in [continue mode](Sketcher_Workbench#Continue_modes.md):
    1.  Optionally keep creating arcs.
    2.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

## Notes

-   Elements of the internal geometry can be deleted. They can be recreated at any time with [Sketcher RestoreInternalAlignmentGeometry](Sketcher_RestoreInternalAlignmentGeometry.md).
-   Once created, the major and minor axes of an arc of ellipse are strict and cannot be swapped by resizing. This is a consequence of the solver parametrization and the same strict behavior of [OpenCASCADE](OpenCASCADE.md). An arc of ellipse must be rotated to swap its axes.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArcOfEllipse/zh-cn

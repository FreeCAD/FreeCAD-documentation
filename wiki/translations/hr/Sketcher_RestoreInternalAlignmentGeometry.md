---
 GuiCommand:
   Name: Sketcher RestoreInternalAlignmentGeometry
   MenuLocation: Sketch , Sketcher visual , Show/hide internal geometry
   Workbenches: Sketcher_Workbench
   Shortcut: **Z** **I**
   SeeAlso: 
---

# Sketcher RestoreInternalAlignmentGeometry/hr

## Description

The <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:24px;"> [Sketcher RestoreInternalAlignmentGeometry](Sketcher_RestoreInternalAlignmentGeometry.md) tool deletes the internal geometry of elements, or recreates missing internal geometry. The tool does not delete internal geometry that has associated constraints.

## Usage

1.  Select one or more sketch elements that support internal geometry ([ellipse](Sketcher_CreateEllipseByCenter.md), [arc of ellipse](Sketcher_CreateArcOfEllipse.md), [arc of hyperbola](Sketcher_CreateArcOfHyperbola.md), [arc of parabola](Sketcher_CreateArcOfParabola.md) or [B-spline](Sketcher_CreateBSpline.md)).
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_RestoreInternalAlignmentGeometry.svg" width=16px> [Show/hide internal geometry](Sketcher_RestoreInternalAlignmentGeometry.md)** button.
    -   Select the **Sketch → Sketcher visual → <img src="images/Sketcher_RestoreInternalAlignmentGeometry.svg" width=16px> Show/hide internal geometry** option from the menu.
    -   Use the keyboard shortcut: **Z** then **I**.
3.  Internal geometry is deleted for selected elements with a complete set of internal geometry, else missing internal geometry is recreated.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RestoreInternalAlignmentGeometry/hr

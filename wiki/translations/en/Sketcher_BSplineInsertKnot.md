---
 GuiCommand:
   Name: Sketcher BSplineInsertKnot
   MenuLocation: Sketch , Sketcher B-spline tools , Insert knot
   Workbenches: Sketcher_Workbench
   Version: 0.20
   SeeAlso: Sketcher_BSplineIncreaseKnotMultiplicity, Sketcher_BSplineDecreaseKnotMultiplicity
---

# Sketcher BSplineInsertKnot/en

## Description

The <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:24px;"> [Sketcher BSplineInsertKnot](Sketcher_BSplineInsertKnot.md) tool inserts a knot into a [B-spline](B-Splines.md). If a knot already exists at the specified parameter its multiplicity is increased by one.

## Usage

1.  Select a B-spline.
2.  There are several ways to invoke the tool:
    -   Press the **[<img src=images/Sketcher_BSplineInsertKnot.svg style="width:16px"> [Insert knot](Sketcher_BSplineInsertKnot.md)** button.

    -   Select the **Sketch → Sketcher B-spline tools → <img src="images/Sketcher_BSplineInsertKnot.svg" width=16px> Insert knot** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_BSplineInsertKnot.svg" width=16px> Insert knot** option from the context menu.
3.  Move the cursor to the desired location.
4.  The current position is marked with a small circle and its parameter value is indicated.
5.  Click to insert a knot, or click an existing knot to increase its multiplicity.
6.  This tool always runs in continue mode: optionally keep inserting knots and/or increasing multiplicity values.
7.  To finish, right-click or press **Esc**, or start geometry or constraint creation tool.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineInsertKnot/en

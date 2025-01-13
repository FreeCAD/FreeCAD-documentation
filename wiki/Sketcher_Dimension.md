---
 GuiCommand:
   Name:  Sketcher Dimension
   MenuLocation: Sketch , Sketcher constraints , Dimension
   Workbenches: Sketcher_Workbench
   Shortcut: **D**
   Version: 1.0
---

# Sketcher Dimension

## Description

The <img alt="" src=images/Sketcher_Dimension.svg  style="width:24px;"> [Sketcher Dimension](Sketcher_Dimension.md) tool is the context-sensitive constraint tool of the Sketcher Workbench. Based on the current selection, it offers appropriate dimensional constraints, but also geometric constraints.

## Usage

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

1.  Optionally select one or more elements (edges or points). [B-spline](Sketcher_Workbench#Sketcher_CompCreateBSpline.md) edges are currently not supported.
2.  There are several ways to invoke the tool:
    -   If the **Dimensioning constraints** [preference](Sketcher_Preferences#General.md) is set to {{Value|Both}} or {{Value|Single tool}} (default): press the **<img src="images/Sketcher_Dimension.svg" width=16px> [Dimension](Sketcher_Dimension.md)** button.
    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **Dimension → <img src="images/Sketcher_Dimension.svg" width=16px> Dimension** option from the context menu.
    -   If there is a selection: Right-click in the 3D view and select the **<img src="images/Sketcher_Dimension.svg" width=16px> Dimension** option from the context menu.
    -   Use the keyboard shortcut: **D**.
3.  The cursor changes to a cross with the tool icon.
4.  If you have not yet selected an element: select one.
5.  Depending on the selected element(s) a constraint is proposed.
6.  Optionally select an additional element.
7.  Optionally deselect an element by clicking it again.
8.  The proposed constraint is updated after every selection change.
9.  Optionally press the **M** key one or more times to cycle through other available constraints, if any.
10. If a geometric constraint is proposed, selected elements may change giving a preview of the result.
11. Do one of the following:
    -   Click in an empty area in the [3D view](3D_view.md) to confirm:
        1.  If a dimensional constraint is created the clicked point determines its location. For a linear dimension the clicked point also determines its type: <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:16px;"> [Horizontal distance](Sketcher_ConstrainDistanceX.md), <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:16px;"> [Vertical distance](Sketcher_ConstrainDistanceY.md) or <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:16px;"> [Distance](Sketcher_ConstrainDistance.md).
        2.  If a [driving dimensional constraint](Sketcher_ToggleDrivingConstraint.md) is created, depending on the [preferences](Sketcher_Preferences#Display.md), a dialog opens to [edit its value](Sketcher_Workbench#Edit_constraints.md).
        3.  A constraint is added.
        4.  This tool always runs in continue mode: optionally keep creating constraints.
    -   To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.




 {{Sketcher_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Dimension

---
 GuiCommand:
   Name:  Sketcher ConstrainHorVer
   MenuLocation: Sketch , Sketcher constraints , Constrain horizontal/vertical
   Workbenches: Sketcher_Workbench
   Shortcut: **A**
   Version: 1.0
   SeeAlso: Sketcher_ConstrainHorizontal, Sketcher_ConstrainVertical
---

# Sketcher ConstrainHorVer/pt-br


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Description


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:24px;"> [Sketcher ConstrainHorVer](Sketcher_ConstrainHorVer.md) tool constrains lines or pairs of points to be horizontal (parallel to the horizontal axis of the sketch) or vertical, whichever is closest to the current alignment.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

This tool combines the [Sketcher ConstrainHorizontal](Sketcher_ConstrainHorizontal.md) and [Sketcher ConstrainVertical](Sketcher_ConstrainVertical.md) tools.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Usage


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   If the **Auto tool for Horizontal/Vertical** [preference](Sketcher_Preferences#General.md) is selected (default): press the **<img src="images/Sketcher_ConstrainHorVer.svg" width=16px> [Constrain horizontal/vertical](Sketcher_ConstrainHorVer.md)** button.
    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainHorVer.svg" width=16px> Constrain horizontal/vertical** option from the menu.
    -   Right-click in the [3D view](3D_view.md) and select the **Constrain → <img src="images/Sketcher_ConstrainHorVer.svg" width=16px> Constrain horizontal/vertical** option from the context menu.
    -   Use the keyboard shortcut: **A**.
3.  The cursor changes to a cross with the tool icon.
4.  Do one of the following:
    -   Select two points.
    -   Select a single line.
5.  A constraint is added.
6.  Optionally keep creating constraints.
7.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.


</div>



### Modo de execução única 


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Do one of the following:
    -   Select two or more points (the selection order can be relevant see [Notes](#Notes.md)).
    -   Select one or more lines. Points can be included in the selection, but will be ignored.
2.  Invoke the tool as explained above, or with the following additional option:
    -   Right-click in the [3D view](3D_view.md) and select the **<img src="images/Sketcher_ConstrainHorVer.svg" width=16px> Constrain horizontal/vertical** option from the context menu.
3.  Depending on the selection one or more constraints are added.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Notes


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   More than 2 points are processed in the selection order, one pair at a time. The 1st point is paired with the 2nd. When they are constrained the 2nd point may move. The new location of the 2nd point determines which constraint is applied when the 2nd and 3rd point are constrained, etc.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorVer/pt-br

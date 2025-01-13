---
 GuiCommand:
   Name: Constraint InternalAngle
   Workbenches: Sketcher Workbench
   Shortcut: A
   MenuLocation: Sketch , Sketcher constraints , Constrain angle
   SeeAlso: Sketcher ConstrainDistance, Sketcher ConstrainPerpendicular
---

# Sketcher ConstrainAngle/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Constrângerea de unghi este o [datum constraint](Sketcher_Workbench#Sketcher_Constraints.md) având ca scop fixarea unghiurilor unei schițe. Este capabilă să definească pantele liniilor individuale, unghiurile dintre linii, unghiurile de intersecții ale curbelor și deschiderile unghiulare ale arcurilor circulare.


</div>




<div class="mw-translate-fuzzy">

## Cum se folosește 

Sunt patru căi diferite pentru ca această constrângere să fie aplicată:

1.  Liniilor individuale
2.  între linii
3.  asupra interesecțiilor curbelor
4.  Arcurilor de cercuri


</div>

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

### [Continue mode](Sketcher_Workbench#Continue_modes.md) 

1.  Make sure there is no selection.
2.  There are several ways to invoke the tool:
    -   
        <small>(v1.0)</small> 
        
        : If the **Dimensioning constraints** [preference](Sketcher_Preferences#General.md) is set to {{Value|Single tool}} (default): press the down arrow to the right of the **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** button and select the **<img src="images/Sketcher_ConstrainAngle.svg" width=16px> Constrain angle** option from the dropdown.

    -   If this preference has a different value (and in {{VersionMinus|0.21}}): press the **<img src="images/Sketcher_ConstrainAngle.svg" width=16px> [Constrain angle](Sketcher_ConstrainAngle.md)** button.

    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainAngle.svg" width=16px> Constrain angle** option from the menu.

    -   
        <small>(v1.0)</small> 
        
        : Right-click in the [3D view](3D_view.md) and select the **Dimension → <img src="images/Sketcher_ConstrainAngle.svg" width=16px> Constrain angle** option from the context menu.

    -   Use the keyboard shortcut: **K** then **A**.
3.  The cursor changes to a cross with the tool icon.
4.  Do one of the following:
    -   Select two lines.
    -   Select a point and two edges (in that order).
    -   Select an edge, a point and an edge (idem).
5.  If a [driving dimensional constraint](Sketcher_ToggleDrivingConstraint.md) is created, depending on the [preferences](Sketcher_Preferences#Display.md), a dialog opens to [edit its value](Sketcher_Workbench#Edit_constraints.md). A negative value will reverse the angle direction.
6.  An Angle constraint is added. If a point and two edges have been selected, up to two [Point to object constraints](Sketcher_ConstrainPointOnObject.md) can also be added. See [Examples](#Between_two_edges_at_point.md).
7.  Optionally keep creating constraints.
8.  To finish, right-click or press **Esc**, or start another geometry or constraint creation tool.

### Run-once mode 

1.  Do one of the following:
    -   Select a single line.
    -   Select a single circular arc.
    -   Select two lines.
    -   Select a point and two edges (in any order).
2.  Invoke the tool as explained above.
3.  Optionally [edit the constraint value](Sketcher_Workbench#Edit_constraints.md).
4.  An Angle constraint is added. If a point and two edges have been selected, up to two [Point on object constraints](Sketcher_ConstrainPointOnObject.md) can also be added. See [Examples](#Between_two_edges_at_point.md).

## Examples

### Single line 

<img alt="" src=images/Sketcher_ConsraintAngle_mode1.png  style="width:400px;">


<div class="mw-translate-fuzzy">

Constrângerea stabilește unghiul polar al direcției liniei. Este unghiul dintre linie și axa X a schiței.


</div>

### Single circular arc 

<img alt="" src=images/Sketcher_ConsraintAngle_mode2.png  style="width:400px;">


<div class="mw-translate-fuzzy">

In acest mod, constrângerea fixată unghiulară a unui arc circular.


</div>

### Between two lines 

<img alt="" src=images/Sketcher_ConsraintAngle_mode3.png  style="width:400px;">


<div class="mw-translate-fuzzy">

În acest mod, constrângerea stabilește unghiul dintre două linii. Nu este necesar ca liniile să se intersecteze.


</div>

### Between two edges at point 

<img alt="" src=images/Sketcher_ConsraintAngle_mode4.png  style="width:400px;">

The angle between the two edges at a given point is fixed. The point can be any point, e.g. the center of a circle, the endpoint of an edge, or the origin, it can belong to either or both edges, and it can also be a [Point object](Sketcher_CreatePoint.md). If required [Point on object constraint(s)](Sketcher_ConstrainPointOnObject.md) are added to ensure the point lies on both (extended) edges. These additional constraints are called [helper constraints](Sketcher_helper_constraint.md).



## Script


<div class="mw-translate-fuzzy">

Constrângerea Unghiulară poate fi creată cu [macros](macros.md) și de la consola Python console utilizând următoarele:


</div>


```python
# line slope angle
Sketch.addConstraint(Sketcher.Constraint('Angle',iline,angle))

# angular span of arc
Sketch.addConstraint(Sketcher.Constraint('Angle',iarc,angle))

# angle between lines
Sketch.addConstraint(Sketcher.Constraint('Angle',iline1,pointpos1,iline2,pointpos2,angle))

# angle-via-point (no helper constraints are added automatically when from python)
Sketch.addConstraint(Sketcher.Constraint('AngleViaPoint',icurve1,icurve2,geoidpoint,pointpos,angle))
```


<div class="mw-translate-fuzzy">

unde:

  - Sketch este un obiect tip schiță

  - iline, iline1, iline2 sunt numere întregi specificând liniile printr-un număr ordinal in Sketch.

  - pointpos1, pointpos2 should be 1 for start point and 2 for end point. The choice of endpoints allows to set internal angle (or external), and it affects how the constraint is drawn on the screen.

  - geoidpoint and pointpos in AngleViaPoint are the indexes specifying the point of intersection.

  - angle este valoarea unghiului în radiani. Unghiul este contorizat între vectorii tangenți în sens antiorar. Vectorii tangenți indică de la început până la capăt liniile (sau invers, dacă punctul final este indicat liniar) și în sens antiorar pentru cercuri, arce și elipse. Cantitatea este, de asemenea, acceptată ca un unghi (de exempluApp.Units.Quantity('45 deg'))


</div>

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `iline`, `iline1`, `iline2`, `pointpos1`, `pointpos2`, `geoidpoint` and `pointpos` and contains further examples on how to create constraints from Python scripts.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainAngle/ro

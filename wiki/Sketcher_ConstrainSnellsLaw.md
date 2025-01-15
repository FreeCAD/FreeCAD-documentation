---
 GuiCommand:
   Name: Sketcher ConstrainSnellsLaw
   MenuLocation: Sketch , Sketcher constraints , Constrain refraction 
   Workbenches: Sketcher_Workbench
   Shortcut: **K** **W**
   Version: 0.15
---

# Sketcher ConstrainSnellsLaw

## Description

The <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:24px;"> [Sketcher ConstrainSnellsLaw](Sketcher_ConstrainSnellsLaw.md) tool constrains two lines to follow the law of refraction of light as it penetrates through an interface where two materials with different refraction indices meet. See [Snell\'s law](http://en.wikipedia.org/wiki/Snell%27s_law).

 <img alt="" src=images/Snells_law2_witheq.svg  style="width:" height="400px;">  
*Snell's Law*

## Usage

 <img alt="" src=images/Sketcher_SnellsLaw_Example1.png  style="width:500px;">  
*The sequence of clicks is indicated by yellow arrows with numbers, n1 and n2 show where the indices of refraction are*

1.  Prepare two lines to represent a beam of light, and an edge to act as an interface. The lines should be on different sides of the interface. The interface can be a [line](Sketcher_CreateLine.md), an [arc](Sketcher_CreateArc.md), a [circle](Sketcher_CreateCircle.md) or a [conic](Sketcher_CompCreateConic.md).
2.  Select an endpoint of the first line, an endpoint of the second line, and the interface edge. Note the selection order of the endpoints.
3.  There are several ways to invoke the tool:
    -   Select the **Sketch → Sketcher constraints → <img src="images/Sketcher_ConstrainSnellsLaw.svg" width=16px> Constrain refraction (Snell's law)** option from the menu.
    -   Use the keyboard shortcut: **K** then **W**.
4.  The **Refractive index ratio** dialog opens.
5.  Enter the **Ratio n2/n1**. Where **n2** is for the medium where the second selected line resides, and **n1** is for the first line\'s medium.
6.  A Snell\'s law constraint is added. If required the endpoints are made [coincident](Sketcher_ConstrainCoincident.md) and constrained [onto the interface](Sketcher_ConstrainPointOnObject.md). These additional constraints are called [helper constraints](Sketcher_helper_constraint.md).

## Notes

-   The actual Snell\'s law constraint enforces the plain law equation n1\*sin(theta1) = n2\*sin(theta2). It needs the line ends to be made coincident and on the interface by other constraints, otherwise the behavior is undefined. The necessary helper constraints are added automatically based on the current coordinates of the elements.
-   In Python the helper constraints must be added manually (see [Scripting](#Scripting.md)).
-   These helper constraints can be temporarily deleted and the endpoints dragged apart, which can be useful in case one wants to construct a reflected ray or birefringence rays.
-   Unlike the reality, refraction indices are associated with rays of light, but not according to the sides of the boundary. This is useful to emulate birefringence, construct paths of different wavelengths due to refraction, and easily construct angle of onset of total internal reflection.
-   Both rays can be on the same side of the interface, satisfying the constraint equation. This is physical nonsense, unless the ratio n2/n1 is 1.0, in which case the constraint emulates a reflection.
-   Arcs of circle and ellipse are also accepted as rays. But this is also physical nonsense.

## Scripting

The constraints can be created from [macros](Macros.md) and from the [Python](Python.md) console by using the following function:

 
```python
Sketch.addConstraint(Sketcher.Constraint('SnellsLaw',line1,pointpos1,line2,pointpos2,interface,n2byn1))
```

where:

  - `Sketch` is a sketch object

  - `line1` and `pointpos1` are two integers identifying the endpoint of the line in medium with refractive index of *n1*. `line1` is the line\'s index in the sketch (the value, returned by Sketch.addGeometry), and `pointpos1` should be 1 for start point and 2 for end point.

  - `line2` and `pointpos2` are the indexes specifying the endpoint of the second line (in medium *n2*)

  - `interface` is the index specifying the line indicating the position of the interface between medium *n1* and medium *n2*

  - `n2byn1` is a floating-point number equal to the ratio of refractive indices *n2/n1*

The [Sketcher scripting](Sketcher_scripting.md) page explains the values which can be used for `line1`, `pointpos1`, `line2`, `pointpos2` and `interface` and contains further examples on how to create constraints from Python scripts.

Example:

 
```python
import Sketcher
import Part
import FreeCAD

StartPoint = 1
EndPoint = 2

f = App.activeDocument().addObject("Sketcher::SketchObject","Sketch")

# add geometry to the sketch
icir = f.addGeometry(Part.Circle(App.Vector(-547.612366,227.479736,0),App.Vector(0,0,1),68.161979))
iline1 = f.addGeometry(Part.LineSegment(App.Vector(-667.331726,244.127090,0),App.Vector(-604.284241,269.275238,0)))
iline2 = f.addGeometry(Part.LineSegment(App.Vector(-604.284241,269.275238,0),App.Vector(-490.940491,256.878265,0)))
# add constraints
# helper constraints:
f.addConstraint(Sketcher.Constraint('Coincident',iline1,EndPoint,iline2,StartPoint)) 
f.addConstraint(Sketcher.Constraint('PointOnObject',iline1,EndPoint,icir)) 
# the Snell's law:
f.addConstraint(Sketcher.Constraint('SnellsLaw',iline1,EndPoint,iline2,StartPoint,icir,1.47))

App.ActiveDocument.recompute() 
```



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainSnellsLaw

 

## Introduction

 

In FreeCAD the word \"[Constraint](Constraint.md)\" is normally used to refer to a \"rule\" to draw geometrical shapes inside a <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketch](Sketch.md) (`Sketcher::SketchObject` class). A constraint limits the position of a certain geometrical element in different ways, for example, it can specify whether the element is horizontal, vertical, tangent, parallel, perpendicular, coincident with a point, concentric to another object, etc.

There are two big types of constraints:

-    **Geometric constraints**define characteristics of the shapes without specifying exact dimensions, for example, horizontality, verticality, parallelism, perpendicularity, and tangency.

-    **Datum**or **dimensional constraints** define characteristics of the shapes by specifying dimensions, for example, a numeric length or an angle.

See the information in the <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench.md) for a list of all constraints that can be applied. Some of them apply to lines, some to curves, and some to vertices. See also the [basic sketcher tutorial](Basic_Sketcher_Tutorial.md).

## Usage

1.  Create a sketch either from the <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench.md) or through the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md).
2.  Press
    -   
        **<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Sketcher NewSketch](Sketcher_NewSketch.md)**
        
        , or

    -   
        **<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Body](PartDesign_Body.md)**
        
        followed by **<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign NewSketch](PartDesign_NewSketch.md)**.
3.  Double click the created sketch to enter its edit mode.
4.  Draw a series of lines using **<img src=images/Sketcher_CreatePolyline.svg style="width:16px"> [Create polyline](Sketcher_CreatePolyline.md)**.
5.  Pick one of the lines, and use **<img src=images/Sketcher_ConstrainVertical.svg style="width:16px"> [Constrain vertical](Sketcher_ConstrainVertical.md)**.
6.  Pick one of the lines, and use **<img src=images/Sketcher_ConstrainHorizontal.svg style="width:16px"> [Constrain horizontal](Sketcher_ConstrainHorizontal.md)**.
7.  Pick the vertical line, and use **<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Constrain distance Y](Sketcher_ConstrainDistanceY.md)**; assign a distance.
8.  Pick the horizontal line, and use **<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Constrain distance X](Sketcher_ConstrainDistanceX.md)**; assign a distance.

## Notes

-   Constraints are useful to create very precise profiles which can the be turned into solid extrusions by using the **<img src=images/PartDesign_Pad.svg style="width:16px"> <img src=images/Part_Extrude.svg style="width:PartDesign Pad](PartDesign_Pad.md)** or **[16px"> [Part Extrude](Part_Extrude.md)** operations.
-   Constraints are only used within [Sketches](Sketch.md); other 2D objects such as those created with the <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft Workbench](Draft_Workbench.md) do not understand about constraints; the latter are simply placed in 3D space, and their properties define their shape and position.

 {{Sketcher Tools navi}} {{Document objects navi}} 

[Category:Glossary{{\#translation:}}](Category:Glossary.md)

# Sketcher project/en
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

This is the FreeCAD Sketcher development project. It follows the rules of the \[<http://en.wikipedia.org/wiki/Getting_Things_Done#Methodology>\| Getting things done\] process. The projects are collected in the [Development roadmap](Development_roadmap.md).

## Purpose and principles 

This is a software development project aimed to implement a Constraint Sketcher capabilities. Its about implementing some Gui elements and the binding to the constraint solver.

The development steps are planed here and tracked in the Issue tracking system to get a well formed [Change Log.](http://www.freecadweb.org/tracker/)

## Outcome

## Brainstorming

In order to improve the solving performance of the sketcher, a graph-based partitioning of the constraints system can take place. The set of the constraints and the set of the unknown parameters can be represented in a [bipartite graph](http://en.wikipedia.org/wiki/Bipartite_graph) with constraints corresponding to left nodes and unknowns to right nodes. **DONE**

A simple but often very useful preprocessing step is to recognize any disjoint subgroups so that they can be treated separately in the solver. **DONE**

Moreover one could reduce the number of the unknown parameters that are taken into account in the solution. At the beginning of a solution it should be checked which constraints are not already satisfied. By graph analysis one could find a minimum set of unknown parameters that should be taken into account in order to satisfy all unsatisfied constraints.

Going one step further, rigid sub-parts of a sketch could be detected and reduced to 3 degrees of freedom (x,y,rotation).

## Organizing

## Next actions 

For 0.14:

1.  Mouse Dragging for multiple selection
2.  List of Geometries in the task panel (similar to the list of Constraints)
3.  Add a popup menu option to convert a coincident points constraint to tangency constraints
4.  Polygon tool (convenience)
5.  Update wiki documentation on Symmetry constraint and Polyline tool (m-key)

Idea Brainstorm:

User Interface :

1.  Full Screen Grid (Units aware)
2.  Smarter Auto-constraints:
    1.  Algorithm only considers geometry that is on the screen to increase performance and improve selection
    2.  Prevent constraint conflicts
3.  Hint Lines: horizontal, vertical, perpendicular, tangent constraints?
4.  Overhaul of constraint icons by merging into one SoNode
    1.  Merge into one SoNode to improve performance
    2.  Remove need for ray pick to increase performance
    3.  Share texture memory more efficiently.
    4.  Improve algorithm for preventing overlap
    5.  Tool Bar for toggling constraint visuals independently
5.  Datum Label Improvements:
    1.  Radius label can be positioned at any angle
    2.  Remove need for storing in SoImage which isn\'t needed any more
6.  Fix Grid Edge
7.  Auto constraints whilst dragging (Point on Point, Point on Line Coincident)?
8.  Highlight entities or zoom to over constrained area of sketch
9.  Related to part design (transparent support objects)
10. Implement Sketch Plane Feature with introduction of Assembly module
11. Improve Point Selection by implementing new custom node.
12. Construction lines use dashes instead of solid lines.

For 0.13:

1.  support for arc/arc and arc/circle in the tangent constraint - **DONE** \[logari81\]
2.  support for arcs in the perpendicular constraint - **DONE** \[logari81\]
3.  zoom-independent arrows (symmetry constraint) / dimension lines - **DONE** \[mrlukeparry\]
4.  external geometry / constraints - **DONE** \[logari81\]
5.  box selection - **DONE** \[mrlukeparry\]
6.  mouse dragging of multiple selection - **SKIPPED for 0.14**
7.  better constrainess diagnostics [(Issue \#691)](http://www.freecadweb.org/tracker/view.php?id=691)- **DONE** \[logari81\]
8.  list of Geometries in the task panel (similar to the list of Constraints) - **SKIPPED for 0.14**
9.  support for points as construction geometry - **DONE** \[logari81\]
10. add a popup menu option to convert a coincident points constraint to tangency constraints - **SKIPPED for 0.14**
11. make symmetry constraint to work with symmetry points instead of symmetry lines (useful e.g. for midpoint definition) - **DONE** \[logari81\]

For 0.12:

1.  constraint parameters (datums) editable in the 3D view **DONE** \[jriegel\]
2.  synchronization between listwidgetview selection - 3D view selection - **DONE** \[wmayer\]
3.  avoid overlapping of constraints symbols **DONE** - \[mrlukeparry\]
    1.  make constraints symbols smaller, selectable and avoid overlapping when zooming out **DONE** - \[mrlukeparry\]
    2.  create constraint icons for 3D Inventor view **DONE** - \[mrlukeparry\]
    3.  make datum text size dependant on zoom **DONE** - \[mrlukeparry\]
    4.  make datum text easier to select **DONE** - \[mrlukeparry\]
    5.  Prevent text overlap on Datum Labels **DONE** - \[mrlukeparry\]
4.  testing the new solver in stand alone mode
5.  external constraints (having constraints with references outside the sketch, some edge of the 3D model e.g.) **0.13** \[jriegel\]
6.  auto-constraining **DONE** \[jriegel\]
    1.  auto-constraint for perpendicular **DONE** - \[mrlukeparry\]
7.  visualize tangency constraints **DONE** - \[mrlukeparry\]
8.  visualize point to line distance constraints and point to point distance constraints **DONE** - \[logari81\]
9.  add indexes to the constraints symbols in 3D view in order to distinguish between constraints of the same kind **DONE** - \[mrlukeparry\]
10. radius constraint (including visualization) **DONE** - \[logari81\]
11. angle constraint (including visualization) **DONE** - \[logari81\]
12. implement a fillet tool in the sketcher **DONE** \[mrlukeparry\]
    1.  provide a method of setting fillet radius [(Issue \#437)](http://www.freecadweb.org/tracker/view.php?id=437)
13. implement a trim/extend tool in the sketcher **DONE** \[logari81\]
    1.  implement an extend tool **SKIPPED** \[logari81\]
    2.  trim support on arcs **DONE** \[mrlukeparry\]
14. equal lengths constraint (including visualization) **DONE** - \[logari81\]
15. constrainess diagnostics - degree of freedom counting **DONE** - \[logari81\]
16. symmetry constraint (including visualization) **DONE** - \[logari81\]
17. implement point on object constraint **DONE** - \[mrlukeparry\]
18. Make Snap-Grid less \'greedy\' **DONE** \[mrlukeparry\]
19. Wiki page for the Sketcher Workbench **DONE** \[normandc\]


{{Sketcher Tools navi

}}  

[<img src="images/Property.png" style="width:16px"> Roadmap](Category_Roadmap.md)

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher project/en

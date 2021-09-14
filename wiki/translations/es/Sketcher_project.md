# Sketcher project/es




{{VeryImportantMessage|
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
}}


{{TOCright}}

Este es el proyecto de desarrollo del croquizador de FreeCAD. Sigue las reglas de la metodología \[<http://en.wikipedia.org/wiki/GTD#GTD_methodology>\| Getting things done\]. Los proyectos son recopilados en el [mapa de desarrollo](Development_roadmap/es.md).

## Propósito y principios 

Este es un proyecto de desarrollo de software cuya intención es implementar habilidades de restricciones en el croquizador. Trata de implementar algunos elementos de la interfaz gráfica de usuario GUI y vincularlos al solucionador de restricciones.

Los pasos de desarrollo están planificados aquí y son seguidos en el sistema de gestión de incidencias para lograr un histórico de cambios bien definido: [Sistema de gestión de incidencias](http://apps.sourceforge.net/mantisbt/free-cad/my_view_page.php)

## Resultado

## Tormenta de ideas 

Para mejorar el rendimiento del solucionador del croquizador, puede realizarse un particionado basado en gráficos del sistema de restricciones. El conjunto de las restricciones y el conjunto de los parámetros desconocidos se puede presentar en un [grafo bipartito](http://es.wikipedia.org/wiki/Grafo_bipartito) con restricciones correspondiendo en los nodos de la izquierda y los parámetros desconocidos en los nodos de la derecha. **TERMINADO**

Un simple pero muy utilizado paso de preprocesado reconoce cualquier subgrupo disjunto de modo que puedan ser tratado de forma separada en el solucionador. **TERMINADO**

Por otra parte, se podría reducir el número de parámetros desconocidos que son cogidos en cuenta en la solución. Al principio de la solución debería verificar que restricciones no están ya satisfechas. Por un análisis gráfico se podría encontrar un conjunto mínimo de parámetros desconocidos que deberían tenerse en cuenta para satisfacer todas las restricciones no satisfechas.

Dando un paso más, las subpiezas rígidas de un croquis podrían detectarse y reducirse a 3 grados de libertad (x,y,rotación).

## Organización

## Siguientes acciones 

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

[Category:Roadmap](Category:Roadmap.md)

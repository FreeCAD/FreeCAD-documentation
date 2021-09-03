 {{TOCright}}

## Import

### Supported Elements {#supported_elements}

-   primitives: cube, sphere, cylinder, square, circle, polygon, polyhedron
-   boolean: union, difference, intersection
-   linearextrude, rotateextrude
-   import (dxf, stl, off) (without scaling or transformation of origin)
-   multmatrix
-   color

### Unsupported Elements {#unsupported_elements}

-   projection
-   surface
-   render (ignored)
-   cgal operations: minkowski, glide, path, subdiv, hull

## Export

### Supported Elements {#supported_elements_1}

-   primitives: Box, Cylinder, Cone, Torus
-   boolean: Cut, Fuse, Common

### Fallback

Every object derived from Part::Feature which is not (yet) supported will get meshed and exported as a polyhedron element

## Related

-   [OpenSCAD Workbench](OpenSCAD_Workbench.md)
-   [Import Export](Import_Export.md)
-   [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md)


 {{OpenSCAD Tools navi}}

[Category:File\_Formats{{\#translation:}}](Category:File_Formats.md)

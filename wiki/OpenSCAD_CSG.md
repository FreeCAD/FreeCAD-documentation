# OpenSCAD CSG
## Import

### Supported Elements 

-   primitives   * cube, sphere, cylinder, square, circle, polygon, polyhedron
-   boolean   * union, difference, intersection
-   linearextrude, rotateextrude
-   import (dxf, stl, off) (without scaling or transformation of origin)
-   multmatrix
-   color

### Unsupported Elements 

-   projection
-   surface
-   render (ignored)
-   cgal operations   * minkowski, glide, path, subdiv, hull

## Export

### Supported Elements 

-   primitives   * Box, Cylinder, Cone, Torus
-   boolean   * Cut, Fuse, Common

### Fallback

Every object derived from Part   *   *Feature which is not (yet) supported will get meshed and exported as a polyhedron element

## Related

-   [OpenSCAD Workbench](OpenSCAD_Workbench.md)
-   [Import Export](Import_Export.md)
-   [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md)

  {{OpenSCAD Tools navi}}

[Category   *File\_Formats](Category_File_Formats.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD CSG

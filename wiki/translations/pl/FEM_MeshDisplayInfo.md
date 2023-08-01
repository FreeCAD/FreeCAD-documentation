---
- GuiCommand:
   Name:FEM MeshDisplayInfo
   Name:MES: Wyświetl informacje o siatce MES
   MenuLocation:Context menu on mesh object - Wyświetl informacje o siatce MES
   Workbenches:[MES](FEM_Workbench/pl.md)
   SeeAlso:[Poradnik dla środowiska pracy MES](FEM_tutorial/pl.md)
---

# FEM MeshDisplayInfo/pl

## Description

Displays basic statistics of existing mesh - number of nodes and elements of each type. Particularly, total number of the following features is shown:

-   Nodes,
-   Edges,
-   Faces,
-   Polygons,
-   Volumes,
-   Polyhedrons,

\* Linear edges,

-   Linear faces,
-   Linear volumes,

\* Quadratic edges,

-   Quadratic faces,
-   Quadratic triangles,
-   Quadratic quadrangles,
-   Quadratic volumes,
-   Quadratic hexahedrons,
-   Quadratic tetrahedrons,
-   Quadratic prisms,
-   Quadratic pyramids.

## Usage

1.  Create finite element mesh first (using one of the available techniques).
2.  Select the mesh in the [Tree view](Tree_view.md).
3.  Right click on it and choose the **<img src="images/FEM_MeshDisplayInfo.svg" width=16px> [Display FEM mesh info](FEM_MeshDisplayInfo.md)** option.
4.  To close the FEM Mesh Info window, click **OK**.

## Scripting


{{code|code=
# setup some model with a fem mesh to print information from
from femexamples.ccx_cantilever_faceload import setup
setup()
# print the fem mesh information
print(App.ActiveDocument.Mesh.FemMesh)
}}

will output the following result:


{{code|code=
>>> print(App.ActiveDocument.Mesh.FemMesh)
========================== Dump contents of mesh ==========================


1) Total number of nodes:       228
2) Total number of edges:       0
3) Total number of faces:       0
4) Total number of polygons:    0
5) Total number of volumes:     79
6) Total number of polyhedrons: 0

7) Total number of linear edges:    0
8) Total number of linear faces:    0
9) Total number of linear volumes:  0

10) Total number of quadratic edges:    0
11) Total number of quadratic faces:    0
12) Total number of quadratic volumes:  79
12.1) Number of quadratic hexahedrons:  0
12.2) Number of quadratic tetrahedrons: 79
12.3) Number of quadratic prisms:       0
12.4) Number of quadratic pyramids:     0

===========================================================================
}}





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshDisplayInfo/pl

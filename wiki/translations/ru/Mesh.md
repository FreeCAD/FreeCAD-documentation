# Mesh/ru
{{TOCright}}

## Введение

In FreeCAD the word \"[Mesh](Mesh.md)\" is normally used to refer to a [Mesh MeshObject](Mesh_MeshObject.md) (`Mesh   *   *MeshObject` class), a type of object that defines 3D data but is not a solid \"[Shape](Shape.md)\".

Meshes are very simple objects, containing only vertices (points), edges and triangular faces. In general, they are easy to create, modify, subdivide, and stretch, and can be passed from one application to another without any loss of detail. In addition, since meshes contain very simple data, 3D applications like animation software and video games can manage very large quantities of them (millions of triangles) without using a lot of computing resources.

However, in the field of engineering meshes present one big limitation   * they are only made of surfaces, and have no \"mass\" information, so they don\'t behave like \"solids\". This means that solid-based operations, like [boolean addition or subtraction](Part_Boolean.md), are difficult to perform on meshes. Also, since they are defined by individual points, they are hard to describe in a parametric fashion.

See [Mesh MeshObject](Mesh_MeshObject.md) for more information about this type of object, and see [Polygon mesh](https   *//en.wikipedia.org/wiki/Polygon_mesh) for generic information in computer systems.

![](images/Shape_and_mesh.svg )



*Left   * parametric [shape](Shape.md) defined by properties. Right   * [mesh](Mesh.md), defined by vertices and triangular surfaces.*

## Usage

Meshes are normally created by internal functions of the [Mesh Workbench](Mesh_Workbench.md), or by importing mesh format files, like STL and OBJ.

Essentially, every object derived from a [Mesh Feature](Mesh_Feature.md) (`Mesh   *   *Feature` class) is expected to hold and manipulate a Mesh.

Since FreeCAD is primarily designed to be a solid modeller, it is better suited to deal with solid [Shapes](Shape.md). It can import and display Meshes in the [3D view](3D_view.md), and the [Mesh Workbench](Mesh_Workbench.md) offers some commands to directly manipulate them. But in many cases the Mesh first needs to be converted to a [Shape](Shape.md) (see [Part ShapeFromMesh](Part_ShapeFromMesh.md)), or the geometry needs to be recreated using solid modelling techniques from the [Part Workbench](Part_Workbench.md) or the [PartDesign Workbench](PartDesign_Workbench.md).

## Finite element meshes 

In FreeCAD the word \"[Mesh](Mesh.md)\" may also refer to a specific object that will be used in finite element analysis (FEA).

When an object with a solid [Shape](Shape.md) is used in the [FEM Workbench](FEM_Workbench.md) it will be discretized into a triangular mesh. In this case, the resulting object is a [FEM FemMeshObject](FEM_Mesh.md) (`Fem   *   *FemMeshObject` class), and is not derived from a [Mesh Feature](Mesh_Feature.md) (`Mesh   *   *Feature` class).

For more information see [FEM Workbench](FEM_Workbench.md) and [FEM Mesh](FEM_Mesh.md).

## More information 

-   [Polygonal (mesh) geometry](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=47493)


{{Mesh Tools navi

}} {{FEM Tools navi}} {{Document objects navi}} 

[Category   *Glossary](Category_Glossary.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Mesh](Category_Mesh.md) > [FEM](Category_FEM.md) > Mesh/ru

# Shape/it
## Introduzione

In FreeCAD the word \"[Shape](Shape.md)\" is normally used to refer to a [Part TopoShape](Part_TopoShape.md) (`Part   *   *TopoShape` class), a type of object that gives an element its 3D geometrical and parametric representation (cube, pyramid, sphere, cylinder, fusion, etc.).

Essentially all objects that are displayed in the [3D view](3D_view.md) have a [TopoShape](Part_TopoShape.md), with the exception of \"[Meshes](Mesh.md)\", which have a [MeshObject](Mesh_MeshObject.md) (`Mesh   *   *MeshObject` class).

See [Part TopoShape](Part_TopoShape.md) for more information about this type of object.

![](images/Shape_and_mesh.svg )



*Left   * parametric [shape](Shape.md) defined by properties. Right   * [mesh](Mesh.md), defined by vertices and triangular surfaces.*

## Usage

Shapes are normally created by internal functions of the [Part Workbench](Part_Workbench.md), and are ultimately defined by the [OpenCASCADE Technology](OpenCASCADE.md) kernel (OCCT).

Once a Shape is created, it can be used and modified by all [workbenches](Workbenches.md) by creating [scripted objects](scripted_objects.md) around that Shape.

Essentially, every object derived from a [Part Feature](Part_Feature.md) (`Part   *   *Feature` class) is expected to hold and manipulate a Shape.

## Notes

In informal usage, a \"Shape\" may be any geometrical figure that is visible in the [3D view](3D_view.md), and thus its concept may be confused with that of \"[Body](Body.md)\" or \"[Part](Part.md)\".

However, when more precision is required, the distinction must be made.

-   A \"[Body](Body.md)\" is an object derived from a [Part Feature](Part_Feature.md) (`Part   *   *Feature` class), created with the [PartDesign Workbench](PartDesign_Workbench.md).
-   A \"Shape\" is an internal object, embedded within the \"[Body](Body.md)\".
-   A \"[Part](Part.md)\" is used to group several \"[Bodies](Body.md)\" to form an [assembly](assembly.md). A \"Part\" has a collection of \"Shapes\", but doesn\'t have a \"Shape\" of its own.


 {{Document objects navi}} 

[Category   *Glossary](Category_Glossary.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Part](Category_Part.md) > Shape/it

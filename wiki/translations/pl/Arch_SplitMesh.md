---
- GuiCommand:
   Name:Arch SplitMesh
   MenuLocation:Arch → Utilities → Split Mesh
   Workbenches:[Arch](Arch_Workbench.md)
   SeeAlso:[Arch SelectNonSolidMeshes](Arch_SelectNonSolidMeshes.md), [Arch MeshToShape](Arch_MeshToShape.md)
---

# Arch SplitMesh/pl

## Description

This tool splits a selected [Mesh](Mesh_Workbench.md) object into its separate components

## Usage

1.  Select a mesh object.
2.  Press the **<img src="images/Arch_SplitMesh.svg" width=16px> [Split Mesh](Arch_SplitMesh.md)** entry in **Arch → Utilities → Split Mesh**.

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The SplitMesh tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
new_list = splitMesh(obj, mark=True)
```

-   Splits the given mesh object (`obj`) into separated components.

-   If `mark` is `True` [non-manifold](https://en.wikipedia.org/wiki/Manifold) components will be painted red.

-    `new_list`is a list of all the individual components that make the mesh.

Example:


```python
import FreeCAD, Draft, Arch, Mesh, MeshPart

Line = Draft.makeWire([FreeCAD.Vector(0, 0, 0),FreeCAD.Vector(2000, 2000, 0)])
Wall = Arch.makeWall(Line, width=150, height=3000)
FreeCAD.ActiveDocument.recompute()

Shape = Wall.Shape.copy(False)
Shape.Placement = Wall.getGlobalPlacement()

mesh_obj = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "Mesh")
mesh_obj.Mesh = MeshPart.meshFromShape(Shape=Shape, MaxLength=520)
mesh_obj.ViewObject.DisplayMode = "Flat Lines"

new_list = Arch.splitMesh(mesh_obj)
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SplitMesh/pl

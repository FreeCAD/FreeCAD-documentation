---
- GuiCommand:
   Name:Part ShapeFromMesh‏‎
   MenuLocation:Part → Create shape from mesh...
   Workbenches:[Part](Part_Workbench.md)
   SeeAlso:[Part ConvertToSolid](Part_MakeSolid.md), [Part RefineShape](Part_RefineShape.md), [Part PointsFromMesh](Part_PointsFromMesh.md)
---

## Introduction

The **<img src="images/Part_ShapeFromMesh.svg" width=16px> [Part ShapeFromMesh](Part_ShapeFromMesh.md)** command creates a shape from a [mesh object](Mesh.md). Mesh objects have limited editing capabilities in FreeCAD, converting them to [shapes](Shape.md) will allow their use with many more boolean and modification tools.

The inverse operation is **<img src=images/Mesh_FromPartShape.svg style="width:16px"> [Mesh FromPartShape](Mesh_FromPartShape.md)** from the <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Mesh Workbench](Mesh_Workbench.md).

## Usage

1.  Select the mesh object in the [tree view](tree_view.md).
2.  Go to the menu, {{MenuCommand|Part → <img src=images/Part_ShapeFromMesh.svg style="width:16px"> Create shape from mesh}}.
3.  A popup-menu will ask for the tolerance for sewing shape; the default value is {{Value|0.1}}.
4.  A [shape](Shape.md) from the mesh object is created as a separate new object.

Analyzing and repairing of the mesh, if needed, should be done manually before launching **<img src=images/Part_ShapeFromMesh.svg style="width:16px"> [ShapeFromMesh](Part_ShapeFromMesh.md)**. Appropriate tools for this task are available in the <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Mesh Workbench](Mesh_Workbench.md).

After creation of a <img src=images/Part_RefineShape.svg style="width:Shape](Shape.md), it may be useful to use **[Convert to solid](Part_MakeSolid.md)** (necessary for [boolean operations](Part_Boolean.md)) and **[16px"> [Refine shape](Part_RefineShape.md)**.

## Links

-   [Edit STL Files In FreeCAD](https://www.youtube.com/watch?v=5lwENZeNiNg&feature=youtu.be) video by AllVisuals4U.

## Scripting

Creating a [Shape](Shape.md) from a [Mesh](Mesh.md) can be done by using the `makeShapeFromMesh` method from a [Part TopoShape](Part_TopoShape.md); you need to specify the source mesh and tolerance, and assign the result to a new [Part Feature](Part_Feature.md) object.

Notice that the mesh must be recalculated before it is converted to a Shape, otherwise there won\'t be topology information, and the conversion won\'t be successful.

 
```python
import FreeCAD as App
import Part

doc = App.newDocument()
mesh = doc.addObject("Mesh::Cube", "Mesh")
mesh.recompute()

solid = doc.addObject("Part::Feature", "Shape")
shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Mesh.Topology, 0.1)

solid.Shape = shape
solid.Placement.Base = App.Vector(15, 0, 0)
solid.purgeTouched()
doc.recompute()
```




   

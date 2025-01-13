---
 GuiCommand:
   Name: Part ShapeFromMesh‏‎
   MenuLocation: Part , Create shape from mesh...
   Workbenches: Part_Workbench
   SeeAlso: Part_MakeSolid, Part_RefineShape, Part_PointsFromMesh
---

# Part ShapeFromMesh

## Introduction

The <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:24px;"> **Part ShapeFromMesh** command creates shapes from [mesh objects](Mesh.md). Mesh objects have limited editing capabilities in FreeCAD, converting them to [shapes](Shape.md) will allow their use with many more boolean and modification commands.

The inverse operation is [Mesh FromPartShape](Mesh_FromPartShape.md) from the <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> [Mesh Workbench](Mesh_Workbench.md).

## Usage

1.  Analyzing and repairing the mesh object, if needed, should be done before launching this command. Appropriate tools for this task are available in the <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> [Mesh Workbench](Mesh_Workbench.md).
2.  Select one or more mesh objects.
3.  Select the **Part → [<img src=images/Part_ShapeFromMesh.svg style="width:16px"> Create shape from mesh** option from the menu.
4.  The **Shape from mesh** dialog opens.
5.  Optionally check the **Sew shape** checkbox and specify a tolerance:
    -   This option is usually not needed. It is meant for mesh objects that are not watertight and have small gaps between edges.
    -   If the option is selected a compound of shells, instead of a compound of faces, is created.
    -   The sewing operation may be computationally demanding.
6.  Press the **OK** button.
7.  For each selected mesh object a [shape](Shape.md) is created as a separate new object.
8.  Optionally use <img alt="" src=images/Part_RefineShape.svg  style="width:16px;"> [Part RefineShape](Part_RefineShape.md) on these objects.
9.  Optionally turn the final objects into solids with <img alt="" src=images/Part_MakeSolid.svg  style="width:16px;"> [Part MakeSolid](Part_MakeSolid.md).

## Properties

See also: [Property editor](Property_editor.md).

The Part ShapeFromMesh command creates [Part Feature](Part_Feature.md) objects with no additional properties.

## Scripting

Creating a [Shape](Shape.md) from a [Mesh](Mesh.md) can be done by using the `makeShapeFromMesh` method from a [Part TopoShape](Part_TopoShape.md); you need to specify the source mesh and tolerance, and assign the result to a new [Part Feature](Part_Feature.md) object.

Notice that the mesh must be recalculated before it is converted to a Shape, otherwise there won\'t be topology information, and the conversion won\'t be successful.

 
```python
import FreeCAD as App
import Part

doc = App.ActiveDocument
mesh = doc.addObject("Mesh::Cube", "Mesh")
mesh.recompute()

shape = Part.Shape()
shape.makeShapeFromMesh(mesh.Mesh.Topology, 0.1)

solid = doc.addObject("Part::Feature", "Solid")
solid.Shape = Part.Solid(shape.removeSplitter())
solid.Placement.Base = App.Vector(15, 0, 0)
doc.recompute()
```

## Links

-   [Edit STL Files In FreeCAD](https://www.youtube.com/watch?v=5lwENZeNiNg&feature=youtu.be) video by AllVisuals4U.




 {{Part_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ShapeFromMesh

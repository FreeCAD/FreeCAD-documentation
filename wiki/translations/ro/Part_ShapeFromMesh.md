---
 GuiCommand:
   Name: Part ShapeFromMesh‏‎
   Name/ro: Part ShapeFromMesh‏‎
   MenuLocation: Part , Create shape from mesh...
   Workbenches: Part_Workbench/ro
   SeeAlso: Part_MakeSolid/ro, Part_RefineShape/ro, Part_PointsFromMesh/ro
---

# Part ShapeFromMesh/ro

## Introduction


<div class="mw-translate-fuzzy">

## Introducere

Această comandă creează o formă dintr-un [mesh object](Glossary#Mesh.md) . Obiectele din rețea au capacități de editare limitate în FreeCAD, transformându-le în forme, permit utilizarea lor cu multe alte instrumente în FreeCAD (vezi și [ Notes](#Notes.md)).


</div>

The inverse operation is [Mesh FromPartShape](Mesh_FromPartShape.md) from the <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;"> [Mesh Workbench](Mesh_Workbench.md).

## Usage


<div class="mw-translate-fuzzy">

## Utilizare

1.  Selectați obeictul tip plasă.
2.  Choose ** Part** → **<img src="images/Part_ShapeFromMesh.png" width=32px> Create shape from mesh ...** from the top menu.
3.  A popup-menu will ask for the tolerance for sewing shape (default value: 0,1)
4.  A shape from the mesh object is created as a seperate new object.


</div>

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





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ShapeFromMesh/ro

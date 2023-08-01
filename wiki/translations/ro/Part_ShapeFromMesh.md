---
- GuiCommand:
   Name: Part ShapeFromMesh‏‎
   Name/ro: Part ShapeFromMesh‏‎
   MenuLocation: Part - Create shape from mesh...
   Workbenches: [Part](Part_Workbench/ro.md)
   SeeAlso: [Part ConvertToSolid](Part_MakeSolid/ro.md), [Part RefineShape](Part_RefineShape/ro.md), [Part PointsFromMesh](Part_PointsFromMesh/ro.md)
---

# Part ShapeFromMesh/ro

## Introduction


<div class="mw-translate-fuzzy">

## Introducere

Această comandă creează o formă dintr-un [mesh object](Glossary#Mesh.md) . Obiectele din rețea au capacități de editare limitate în FreeCAD, transformându-le în forme, permit utilizarea lor cu multe alte instrumente în FreeCAD (vezi și [ Notes](#Notes.md)).


</div>

The inverse operation is **[<img src=images/Mesh_FromPartShape.svg style="width:16px"> [Mesh FromPartShape](Mesh_FromPartShape.md)** from the <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Mesh Workbench](Mesh_Workbench.md).

## Usage


<div class="mw-translate-fuzzy">

## Utilizare

1.  Selectați obeictul tip plasă.
2.  Choose ** Part** → **<img src="images/Part_ShapeFromMesh.png" width=32px> Create shape from mesh ...** from the top menu.
3.  A popup-menu will ask for the tolerance for sewing shape (default value: 0,1)
4.  A shape from the mesh object is created as a seperate new object.


</div>


<div class="mw-translate-fuzzy">

## Limitări

There will be no analyzing or validating of the mesh object.
Analyzing and repairing of the mesh (if needed) should be done manually before conversion.
Appropriate tools are available in the [Mesh Workbench](Mesh_Workbench.md).


</div>

After creation of a [Shape](Shape.md), it may be useful to use **[<img src=images/Part_MakeSolid.svg style="width:16px"> [Convert to solid](Part_MakeSolid.md)** (necessary for [boolean operations](Part_Boolean.md)) and **[<img src=images/Part_RefineShape.svg style="width:16px"> [Refine shape](Part_RefineShape.md)**.

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



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ShapeFromMesh/ro

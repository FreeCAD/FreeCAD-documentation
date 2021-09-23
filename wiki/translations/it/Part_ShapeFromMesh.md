# Part ShapeFromMesh/it
---
- GuiCommand:/it   Name:Part ShapeFromMesh   Name/it:‏‎Crea forma da mesh   MenuLocation:Part → Crea forma da mesh...   Workbenches:[SeeAlso:[[Part ConvertToSolid/it|Converti in solido](Part_Workbench/it___Part]].md), [Affina forma](Part_RefineShape/it.md), [Crea punti da mesh](Part_PointsFromMesh/it.md)---


</div>

## Introduction


<div class="mw-translate-fuzzy">

## Introduzione

Questo comando crea una forma da un [oggetto mesh](Glossary#Mesh.md). In FreeCAD gli oggetti mesh hanno limitate capacità di editing, convertendoli in forme permette di utilizzarli con molti più strumenti (vedere anche le [Note](#Note.md)).


</div>

The inverse operation is **<img src=images/Mesh_FromPartShape.svg style="width:16px"> [Mesh FromPartShape](Mesh_FromPartShape.md)** from the <img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Mesh Workbench](Mesh_Workbench.md).

## Usage


<div class="mw-translate-fuzzy">

## Utilizzo

1.  Selezionare un oggetto mesh.
2.  Scegliere **Part → <img src="images/Part_ShapeFromMesh.svg" width=16px> Crea forma da mesh** dal menu in alto.
3.  Un menu pop-up chiede di definire la tolleranza per la chiusura (valore di default: 0,1)
4.  Dall\'oggetto mesh viene creato un nuovo oggetto forma indipendente.


</div>


<div class="mw-translate-fuzzy">

## Limitazioni

Non sono disponibili l\'analisi e la convalida dell\'oggetto mesh.


</div>

After creation of a <img src=images/Part_RefineShape.svg style="width:Shape](Shape.md), it may be useful to use **[Convert to solid](Part_MakeSolid.md)** (necessary for [boolean operations](Part_Boolean.md)) and **[16px"> [Refine shape](Part_RefineShape.md)**.

## Links

-   [Edit STL Files In FreeCAD](https://www.youtube.com/watch?v=5lwENZeNiNg&feature=youtu.be) video by AllVisuals4U.

## Script

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


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part ShapeFromMesh/it

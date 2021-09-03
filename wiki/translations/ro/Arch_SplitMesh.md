---
- GuiCommand:/ro
   Name:Arch SplitMesh
   Name/ro:Arch SplitMesh
   MenuLocation:Arch → Utilities → Split Mesh
   Workbenches:[Arch](Arch_Workbench/ro.md)
   SeeAlso:[[Arch SelectNonSolidMeshes]], [[Arch MeshToShape]]
---


</div>

## Descriere


<div class="mw-translate-fuzzy">

Acest instrument împarte un obiect selectat [ Mesh](Mesh_Workbench.md) în componentele sale separate


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește {#cum_se_folosește}


</div>


<div class="mw-translate-fuzzy">

1.  Selectați un obiect tip plasă
2.  Apăsați **<img src="images/Arch_SplitMesh.png" width=16px> '''Split Mesh'''** entry in Arch -\> Utilities menu


</div>


<div class="mw-translate-fuzzy">

## Scrip-Programare {#scrip_programare}


</div>


<div class="mw-translate-fuzzy">

Instrumentul Split Mesh poate fi utilizat în [macros](macros.md) și din consola python utilizând următoarea funcție:


</div>


```python
new_list = splitMesh(obj, mark=True)
```


<div class="mw-translate-fuzzy">

împarte obiectul tip plasă dat în componente separate.


</div>

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










---
- GuiCommand:/ro
   Name:Arch MeshToShape
   Name/ro:Arch MeshToShape
   MenuLocation:Arch → Utilities → Mesh to Shape
   Workbenches:[Arch](Arch_Workbench/ro.md)
   SeeAlso:[Arch SplitMesh](Arch_SplitMesh/ro.md), [Arch RemoveShape](Arch_RemoveShape/ro.md)
---

# Arch MeshToShape/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Acest instrument convertește un obiect selectat [ Mesh](Mesh_Workbench.md) într-un obiect [ Shape](Part_Workbench.md). Notă: Acest instrument este optimizat pentru obiectele cu fețe plate (fără curbe). Instrumentul corespunzător din [Part Workbench](Part_Workbench.md) poate fi mai potrivit pentru obiectele care conțin suprafețe curbe.


</div>

This tool is optimized for objects with flat faces (no curves). The corresponding tool **[<img src=images/Part_ShapeFromMesh.svg style="width:16px"> [Part ShapeFromMesh](Part_ShapeFromMesh.md)** from the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md) might be more suited for objects that contain curved surfaces.

## Cum se folosește 


<div class="mw-translate-fuzzy">

1.  Selectați un obiect tip plasă
2.  apăsați tasta **<img src="images/Arch_MeshToShape.png" width=16px> '''Mesh to Shape'''** în meniul Arch → Utilities menu


</div>

## Properties

## Limitations


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Acest instrument poate fi utilizat în [macros](macros.md) și din consola Python utilizând următoarea funcție:


</div>


```python
new_obj = meshToShape(obj, mark=True, fast=True, tol=0.001, flat=False, cut=True)
```


<div class="mw-translate-fuzzy">

Transformă o plasă într-op formă, unind fațetele coplanare.


</div>

Example: 
```python
import Arch, Mesh, BuildRegularGeoms

Box = FreeCAD.ActiveDocument.addObject("Mesh::Cube", "Cube")
Box.Length = 1000
Box.Width = 2000
Box.Height = 1000
FreeCAD.ActiveDocument.recompute()

new_obj = Arch.meshToShape(Box)
```


<div class="mw-translate-fuzzy">


{{docnav/ro
|[Split Mesh](Arch_SplitMesh.md)
|[Select non-solid meshes](Arch_SelectNonSolidMeshes.md)
|[Arch](Arch_Workbench.md)|IconL=Arch_SplitMesh.svg
|IconC=Workbench_Arch.svg
|IconR=Arch_SelectNonSolidMeshes.png
}}


</div>

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch MeshToShape/ro

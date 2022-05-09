---
- GuiCommand   */es
   Name   *Arch MeshToShape   Name/es   *Arch Malla a forma
   MenuLocation   *Arquitectura → Utilidades → Malla a forma
   Workbenches   *[Arquitectura](Arch_Workbench/es.md)
   SeeAlso   *[Arch SplitMesh/es](Arch_SplitMesh/es.md), [Eliminar forma](Arch_RemoveShape/es.md)
---

# Arch MeshToShape/es


</div>

## Descripción


<div class="mw-translate-fuzzy">

Esta herramienta convierte un objeto [Malla](Mesh_Workbench/es.md) seleccionado en un objeto [Forma](Part_Workbench/es.md). Esta herramienta está optimizada para objetos con caras planas (no curvas). La herramienta correspondiente del [entorno de pieza](Part_Workbench/es.md) podría ser más adecuada para objetos que contienen superficies curvas.


</div>

This tool is optimized for objects with flat faces (no curves). The corresponding tool **[<img src=images/Part_ShapeFromMesh.svg style="width   *16px"> [Part ShapeFromMesh](Part_ShapeFromMesh.md)** from the <img alt="" src=images/Workbench_Part.svg  style="width   *16px;"> [Part Workbench](Part_Workbench.md) might be more suited for objects that contain curved surfaces.

## Utilización


<div class="mw-translate-fuzzy">

1.  Selecciona un objeto malla
2.  Presiona **<img src="images/Arch_MeshToShape.png" width=16px> '''Malla a forma'''** en el menú Arquitectura → Menú utilitarios


</div>

## Properties

## Limitations

## Scripting


<div class="mw-translate-fuzzy">

## Programación


</div>


<div class="mw-translate-fuzzy">

Esta herramienta se puede utilizar en [macros](macros/es.md) y desde la consola de Python por medio de las siguientes funciones   *


</div>


```python
new_obj = meshToShape(obj, mark=True, fast=True, tol=0.001, flat=False, cut=True)
```


<div class="mw-translate-fuzzy">


   *   Covierte una malla en una forma, juntando las caras coplanares.


</div>

Example   * 
```python
import Arch, Mesh, BuildRegularGeoms

Box = FreeCAD.ActiveDocument.addObject("Mesh   *   *Cube", "Cube")
Box.Length = 1000
Box.Width = 2000
Box.Height = 1000
FreeCAD.ActiveDocument.recompute()

new_obj = Arch.meshToShape(Box)
```


<div class="mw-translate-fuzzy">


{{docnav/es
|[Split Mesh](Arch_SplitMesh.md)
|[Select non-solid meshes](Arch_SelectNonSolidMeshes.md)
|[Arch](Arch_Workbench.md)|IconL=Arch_SplitMesh.svg
|IconC=Workbench_Arch.svg
|IconR=Arch_SelectNonSolidMeshes.png
}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch MeshToShape/es

# Arch MeshToShape/cs
---
 GuiCommand:   Name: Arch MeshToShape   Name/cs: Arch MeshToShape   Workbenches: Arch_Workbench/cs   Arch---


</div>



## Popis


<div class="mw-translate-fuzzy">

Tento nástroj konvertuje vybraný objekt [Síť](Mesh_Workbench/cs.md) do objektu [Tvar](Part_Workbench/cs.md). Připomínáme, že tento nástroj je optimalizován pro objekty s plochými stranami (ne zakřivené). Obdobný nástroj z [Pracovní plochy Díl](Part_Workbench/cs.md) může být vhodnější pro objekty obsahující zakřivené povrchy.


</div>

This tool is optimized for objects with flat faces (no curves). The corresponding tool **[<img src=images/Part_ShapeFromMesh.svg style="width:16px"> [Part ShapeFromMesh](Part_ShapeFromMesh.md)** from the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md) might be more suited for objects that contain curved surfaces.



## Použití


<div class="mw-translate-fuzzy">

1.  Vyberte objekt sítě
2.  Stiskněte tlačítko **<img src="images/Arch_MeshToShape.png" width=16px> '''Síť do tvaru'''** pro vstup do Architektura → Menu Utility


</div>

## Properties

## Limitations

## Scripting


<div class="mw-translate-fuzzy">

## Skriptování


</div>


<div class="mw-translate-fuzzy">

Tento nástroj může být použit v [makrech](macros/cs.md) a z konzoly Pythonu použitím následující funkce:


</div>


```python
new_obj = meshToShape(obj, mark=True, fast=True, tol=0.001, flat=False, cut=True)
```


<div class="mw-translate-fuzzy">

zkonvertuje síť do tvaru, přitom sjednocuje koplanární (ležící v jedné rovině) plošky


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





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch MeshToShape/cs

---
 GuiCommand:
   Name: Arch MeshToShape   Name/sv: Arch MeshToShape
   MenuLocation: Arch , Utilities , Mesh to Shape
   Workbenches: Arch_Workbench/sv
   SeeAlso: Arch SplitMesh/sv, Arch RemoveShape/sv
---

# Arch MeshToShape/sv


</div>



## Beskrivning

The **Arch MeshToShape** tool converts a selected [Mesh](Mesh.md) ([Mesh Feature](Mesh_Feature.md)) object into a [Shape](Shape.md) ([Part Feature](Part_Feature.md)) object.

This tool is optimized for objects with flat faces (no curves). The corresponding tool **[<img src=images/Part_ShapeFromMesh.svg style="width:16px"> [Part ShapeFromMesh](Part_ShapeFromMesh.md)** from the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md) might be more suited for objects that contain curved surfaces.

## Usage

1.  Select a mesh object.
2.  Select the **Utils → <img src="images/Arch_MeshToShape.svg" width=16px> Mesh to Shape** option from the menu.

## Properties

## Limitations

## Scripting


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

This tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:


```python
new_obj = meshToShape(obj, mark=True, fast=True, tol=0.001, flat=False, cut=True)
```

The above code snippet converts the given `obj` (a mesh), into a shape, joining coplanar facets.

-   If `mark` is `True`, non-solid objects will be marked in red.

-   If `fast` is `True`, it uses a faster algorithm by building a shell from the facets then removing splitter.

-    `tol`is the tolerance used when converting mesh segments to wires.

-   If `flat` is `True`, it will force the wires to be perfectly planar to be sure they can be converted into faces, but this might leave gaps in the final shell.

-   If `cut` is `True`, holes in faces are made by subtraction.

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


{{docnav/sv
|[Split Mesh](Arch_SplitMesh.md)
|[Select non-solid meshes](Arch_SelectNonSolidMeshes.md)
|[Arch](Arch_Workbench.md)|IconL=Arch_SplitMesh.svg
|IconC=Workbench_Arch.svg
|IconR=Arch_SelectNonSolidMeshes.png
}}


</div>


{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch MeshToShape/sv

---
 GuiCommand:
   Name: FEM FemMesh2Mesh
   MenuLocation: Mesh , FEM mesh to mesh
   Workbenches: FEM_Workbench
   SeeAlso: FEM_tutorial
---

# FEM FemMesh2Mesh

## Description

This tool converts surfaces of 3D elements or whole 2D elements of a selected FEM mesh to [surface mesh](Mesh_MeshObject.md). Internally, it picks FEM mesh element faces that are unique (not shared by two elements) and uses them to create faces of a surface mesh. Optionally, it can be used to save a deformed mesh. This is done by adding the displacement of the FEM results to the mesh nodes (the scale of the displacement can be set using Python).


<small>(v1.0)</small> 

: The tool also creates a *Mesh2Fem* object which is a triangular FEM mesh generated from the surface mesh.

## Usage

1.  Select a FEM mesh object.
2.  Optionally also select the FEM results.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_FemMesh2Mesh.svg" width=16px> [FEM mesh to mesh](FEM_FemMesh2Mesh.md)** button.
    -   Select the **Mesh → <img src="images/FEM_FemMesh2Mesh.svg" width=16px> FEM mesh to mesh** option from the menu.

## Scripting

**Note**: The parameter *scale* was <small>(v0.21)</small> . For older versions of FreeCAD omit it from your code.

The cantilever example in FreeCAD version 1.0:

 
```python
from os.path import join
import FreeCAD as App
import Mesh
from femmesh import femmesh2mesh

path = join(App.getResourceDir(), "examples", "FEMExample.FCStd")
doc = App.openDocument(path)
fem_mesh = doc.FEMMeshGmsh.FemMesh
result = doc.CCX_Results
scale = 10  # displacement scale factor
out_mesh = femmesh2mesh.femmesh_2_mesh(fem_mesh, result, scale)
Mesh.show(Mesh.Mesh(out_mesh))
```




 {{FEM_Tools_navi}}



---
⏵ [documentation index](../README.md) > FEM FemMesh2Mesh

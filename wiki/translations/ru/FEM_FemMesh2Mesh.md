---
 GuiCommand:
   Name: FEM FemMesh2Mesh
   Name/ru: FEM FemMesh2Mesh
   MenuLocation: Mesh , FEM mesh to mesh
   Workbenches: FEM Workbench/ru
   Shortcut: 
   SeeAlso: FEM_tutorial/ru
---

# FEM FemMesh2Mesh/ru


</div>

## Description

This tool converts surfaces of 3D elements of a selected FEM mesh to mesh or converts 2D FEM mesh to mesh. Internally, it picks FEM mesh element faces that are unique (not shared by two elements) and uses them to create faces of a mesh. Optionally, it can be used to save a deformed mesh. This is done by adding the displacement of the FEM results to the mesh nodes (the scale of the displacement can be set using Python).

## Usage

1.  Select a FEM mesh object.
2.  Optionally also select the FEM results.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_FemMesh2Mesh.svg" width=16px> [FEM mesh to mesh](FEM_FemMesh2Mesh.md)** button.
    -   Select the **Mesh → <img src="images/FEM_FemMesh2Mesh.svg" width=16px> FEM mesh to mesh** option from the menu.

## Scripting

**Note**: The parameter *scale* was <small>(v0.21)</small> . For older versions of FreeCAD omit it from your code.

The cantilever example:


```python
from os.path import join
import FreeCAD as App
import Mesh
from femmesh import femmesh2mesh

path = join(App.getResourceDir(), "examples", "FemCalculixCantilever3D.FCStd")
doc = App.openDocument(path)
fem_mesh = doc.Box_Mesh.FemMesh
result = doc.CCX_Results
scale = 1  # displacement scale factor
out_mesh = femmesh2mesh.femmesh_2_mesh(fem_mesh, result, scale)
Mesh.show(Mesh.Mesh(out_mesh))
```





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM FemMesh2Mesh/ru

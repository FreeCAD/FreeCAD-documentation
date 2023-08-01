---
- GuiCommand:/ru
   Name:FEM FemMesh2Mesh
   Name/ru:FEM FemMesh2Mesh
   MenuLocation:Mesh → FEM mesh to mesh
   Workbenches:[FEM](FEM_Workbench/ru.md)
   Shortcut:
   SeeAlso:[FEM tutorial](FEM_tutorial/ru.md)
---

# FEM FemMesh2Mesh/ru


</div>

## Description

This tool converts surfaces of 3D elements of a selected FEM mesh to mesh, or converts 2D FEM mesh to mesh. Internally it picks FEM mesh element faces which are unique (not shared by two elements) and uses them to create faces of a mesh. Optionally it allows to create a deformed mesh caused by the action of the defined forces. This is done by adding the displacement of the FEM results to the mesh nodes (scale of the displacement can be set by Python).

## Usage

1.  Select a FEM mesh object.
2.  Optionally also select the FEM results.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_FemMesh2Mesh.svg" width=16px> [FEM mesh to mesh](FEM_FemMesh2Mesh.md)** button.
    -   Select the **Mesh → <img src="images/FEM_FemMesh2Mesh.svg" width=16px> FEM mesh to mesh** option from the menu.

## Scripting

**Note**: The parameter *scale* was <small>(v0.21)</small> . For older versions of FreeCAD omit it from your code.

When you just require the displacement scale factor, check your mesh object name and the scale factor in the following code:


```python
import femmesh.femmesh2mesh
mesh_obj = FEMMeshGmsh  # the name of your mesh object
scale = 5  # displacement scale factor
out_mesh = femmesh.femmesh2mesh.femmesh_2_mesh(FreeCAD.ActiveDocument.mesh_obj.FemMesh, FreeCAD.ActiveDocument.CCX_Results, scale)
import Mesh
Mesh.show(Mesh.Mesh(out_mesh))
```

The cantilever example:


```python
from os.path import join
the_file = join(FreeCAD.getResourceDir(), "examples", "FemCalculixCantilever3D.FCStd")
fc_file = FreeCAD.openDocument(the_file)
fem_mesh = fc_file.getObject("Box_Mesh").FemMesh  # do not remove the _
result = fc_file.getObject("CCX_Results")
scale = 1  # displacement scale factor
from femmesh import femmesh2mesh
out_mesh = femmesh2mesh.femmesh_2_mesh(fem_mesh, result, scale)
import Mesh
Mesh.show(Mesh.Mesh(out_mesh))
```





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM FemMesh2Mesh/ru

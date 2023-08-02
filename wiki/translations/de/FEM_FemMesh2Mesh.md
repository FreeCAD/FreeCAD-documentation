---
- GuiCommand:
   Name: FEM FemMesh2Mesh
   Name/de: FEM FemNetzZuNetz
   MenuLocation: Mesh -> FEM mesh to mesh
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_tutorial/de
---

# FEM FemMesh2Mesh/de



## Beschreibung

This tool converts surfaces of 3D elements of a selected FEM mesh to mesh, or converts 2D FEM mesh to mesh. Internally it picks FEM mesh element faces which are unique (not shared by two elements) and uses them to create faces of a mesh. Optionally it allows to create a deformed mesh caused by the action of the defined forces. This is done by adding the displacement of the FEM results to the mesh nodes (scale of the displacement can be set by Python).



## Anwendung

1.  Ein FEM-mesh-Objekt auswählen
2.  Optionally also select the FEM results.
3.  Es gibt mehrereMöglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_FemMesh2Mesh.svg" width=16px> [FEM-Netz zu Netz](FEM_FemMesh2Mesh/de.md)** drücken.
    -   Den Menüeintrag **Netz → <img src="images/FEM_FemMesh2Mesh.svg" width=16px> FEM-Netz zu Netz** auswählen.



## Skripten

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
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM FemMesh2Mesh/de

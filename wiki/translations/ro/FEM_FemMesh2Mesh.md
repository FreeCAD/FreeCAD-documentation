# FEM FemMesh2Mesh/ro
---
- GuiCommand:   Name:FEM FemMesh2Mesh   Name/ro:FEM FemMesh2Mesh   MenuLocation:Mesh → FEM mesh to mesh   |Workbenches:[Shortcut:   SeeAlso:[[FEM_tutorial/ro|FEM tutorial](FEM_Workbench/ro___FEM]].md)---


</div>



## Descriere


<div class="mw-translate-fuzzy">

Acest instrument transformă suprafețele elementelor 3D dintr-o plasă FEM selectată într-o plasă. Alegeți fațetele elementului FEM din plasă care sunt unice (nu sunt împărțite de două elemente) și le folosiți pentru a crea fațetele unei plase. Opțional, permite crearea unei plase deformate de acțiunea forțelor definite. Acest lucru se face prin adăugarea mișcării rezultatelor FEM la nodurile de plasă.


</div>




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Selectați un obiect FEM mesh (opțional selectați suplimentar rezultatele FEM)
2.  Apasă pe butonul **<img src="images/FEM_FemMesh2Mesh.png" width=24px>FEM mesh to mesh
**


</div>

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
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM FemMesh2Mesh/ro

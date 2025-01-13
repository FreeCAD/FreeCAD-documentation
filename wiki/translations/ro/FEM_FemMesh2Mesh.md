# FEM FemMesh2Mesh/ro
---
 GuiCommand:   Name: FEM FemMesh2Mesh   Name/ro: FEM FemMesh2Mesh   MenuLocation: Mesh , FEM mesh to mesh   ---


</div>



## Descriere


<div class="mw-translate-fuzzy">

Acest instrument transformă suprafețele elementelor 3D dintr-o plasă FEM selectată într-o plasă. Alegeți fațetele elementului FEM din plasă care sunt unice (nu sunt împărțite de două elemente) și le folosiți pentru a crea fațetele unei plase. Opțional, permite crearea unei plase deformate de acțiunea forțelor definite. Acest lucru se face prin adăugarea mișcării rezultatelor FEM la nodurile de plasă.


</div>


<small>(v1.0)</small> 

: The tool also creates a *Mesh2Fem* object which is a triangular FEM mesh generated from the surface mesh.




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





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM FemMesh2Mesh/ro

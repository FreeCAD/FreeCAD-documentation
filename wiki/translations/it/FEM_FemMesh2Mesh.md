---
- GuiCommand:
   Name: FEM_FemMesh2Mesh
   Name/it: Converti mesh FEM in mesh
   MenuLocation: Mesh - Converti mesh FEM in mesh
   Workbenches: [FEM](FEM_Workbench/it.md)
   Shortcut: 
   SeeAlso: [Tutorial di FEM](FEM_tutorial/it.md)
---

# FEM FemMesh2Mesh/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento converte in mesh le superfici degli elementi 3D di una mesh FEM selezionata. Sceglie le facce dell\'elemento mesh FEM che sono uniche (non condivise da due elementi) e le usa per creare le facce di una mesh. Facoltativamente consente di creare una mesh deformata dall\'azione delle forze definite. Ciò avviene aggiungendo lo spostamento dei risultati FEM ai nodi della maglia.


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un oggetto mesh FEM (opzionalmente selezionare anche i risultati FEM)
2.  Premere il pulsante **<img src="images/FEM_FemMesh2Mesh.png" width=24px>FEM mesh to mesh
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


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM FemMesh2Mesh/it

---
 GuiCommand:
   Name: FEM_FemMesh2Mesh
   Name/it: Converti mesh FEM in mesh
   MenuLocation: Mesh , Converti mesh FEM in mesh
   Workbenches: FEM_Workbench/it
   Shortcut: 
   SeeAlso: FEM_tutorial/it
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


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM FemMesh2Mesh/it

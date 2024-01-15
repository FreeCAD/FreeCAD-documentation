---
 GuiCommand:
   Name: FEM FemMesh2Mesh
   Name/fr: FEM Maillage FEM à maillage
   MenuLocation: Maillage , Maillage FEM à maillage
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
---

# FEM FemMesh2Mesh/fr

## Description

Cet outil convertit les surfaces des éléments 3D d\'un maillage FEM sélectionné en maillage ou convertit un maillage FEM 2D en maillage. En pratique, il sélectionne les faces des éléments d\'un maillage FEM qui sont uniques (non partagées par deux éléments) et les utilise pour créer les faces d\'un maillage. En outre, il peut être utilisé pour sauvegarder un maillage déformé. Cela se fait en ajoutant le déplacement des résultats FEM aux nœuds du maillage (l\'échelle du déplacement peut être définie à l\'aide de Python).



## Utilisation

1.  Sélectionnez un objet FEM maillage.
2.  Vous pouvez également sélectionner les résultats FEM.
3.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_FemMesh2Mesh.svg" width=16px> [Maillage FEM à maillage](FEM_FemMesh2Mesh/fr.md)**.
    -   Sélectionnez l\'option **Maillage → <img src="images/FEM_FemMesh2Mesh.svg" width=16px> Maillage FEM à maillage** du menu.



## Script

**Remarque** : le paramètre *scale* est {{Version/fr|0.21}}. Pour les anciennes versions de FreeCAD, il faut l\'omettre de votre code.

L\'exemple du cantilever :


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
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM FemMesh2Mesh/fr

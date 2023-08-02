---
- GuiCommand:
   Name: FEM FemMesh2Mesh
   Name/fr: FEM Maillage FEM à maillage
   MenuLocation: Maillage -> Maillage FEM à maillage
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
---

# FEM FemMesh2Mesh/fr

## Description

Cet outil convertit les surfaces des éléments 3D d\'un maillage FEM sélectionné en maillage, ou convertit un maillage FEM 2D en maillage. En pratique, il sélectionne les faces des éléments du maillage FEM qui sont uniques (non partagées par deux éléments) et les utilise pour créer les faces d\'un maillage. En outre, il permet de créer un maillage déformé par l\'action des forces définies. Ceci est fait en ajoutant le déplacement des résultats de la FEM aux nœuds du maillage (l\'échelle du déplacement peut être définie par Python).



## Utilisation

1.  Sélectionnez un objet FEM maillage.
2.  Vous pouvez également sélectionner les résultats FEM.
3.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_FemMesh2Mesh.svg" width=16px> [Maillage FEM à maillage](FEM_FemMesh2Mesh/fr.md)**.
    -   Sélectionnez l\'option **Maillage → <img src="images/FEM_FemMesh2Mesh.svg" width=16px> Maillage FEM à maillage** dans le menu.



## Script

**Remarque** : le paramètre *scale* est {{Version/fr|0.21}}. Pour les anciennes versions de FreeCAD, il faut l\'omettre de votre code.

Si vous avez seulement besoin du facteur d\'échelle de déplacement, vérifiez le nom de votre objet de maillage et le facteur d\'échelle dans le code suivant :


```python
import femmesh.femmesh2mesh
mesh_obj = FEMMeshGmsh  # the name of your mesh object
scale = 5  # displacement scale factor
out_mesh = femmesh.femmesh2mesh.femmesh_2_mesh(FreeCAD.ActiveDocument.mesh_obj.FemMesh, FreeCAD.ActiveDocument.CCX_Results, scale)
import Mesh
Mesh.show(Mesh.Mesh(out_mesh))
```

L\'exemple du cantilever :


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
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM FemMesh2Mesh/fr

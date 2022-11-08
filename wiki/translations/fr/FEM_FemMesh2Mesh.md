---
- GuiCommand   */fr
   Name   *FEM FemMesh2Mesh
   Name/fr   *FEM Maillage FEM à maillage
   MenuLocation   *Maillage → Maillage FEM à maillage
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   SeeAlso   *[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM FemMesh2Mesh/fr

## Description

Cet outil convertit les surfaces des éléments 3D d\'un maillage FEM sélectionné en maillage. En pratique, il sélectionne les faces des éléments du maillage FEM qui sont uniques (non partagées par deux éléments) et les utilise pour créer les faces d\'un maillage. En outre, il permet de créer un maillage déformé par l\'action des forces définies. Ceci est fait en ajoutant le déplacement des résultats FEM aux nœuds du maillage.

Les éléments bidimensionnels du maillage FEM ne sont pas pris en compte. Si vous devez les convertir, vous pouvez utiliser le script Python ci-dessous.

## Utilisation

1.  Sélectionnez un objet FEM maillage.
2.  Vous pouvez également sélectionner les résultats FEM.
3.  Il existe plusieurs façons de lancer la commande    *
    -   Appuyez sur le bouton **<img src="images/FEM_FemMesh2Mesh.svg" width=16px> [Maillage FEM à maillage](FEM_FemMesh2Mesh/fr.md)**.
    -   Sélectionnez l\'option **Maillage → <img src="images/FEM_FemMesh2Mesh.svg" width=16px> Maillage FEM à maillage** dans le menu.

## Script

Exemple    * téléchargez l\'exemple 3D FEM de FreeCAD à partir de l\'atelier Start et exécutez le code suivant.


```python
femmesh_obj = App.ActiveDocument.getObject("Result_mesh").FemMesh
result = App.ActiveDocument.getObject("CalculiX_static_results")
import femmesh.femmesh2mesh
out_mesh = femmesh.femmesh2mesh.femmesh_2_mesh(femmesh_obj, result)
import Mesh
Mesh.show(Mesh.Mesh(out_mesh))
```

## Convertir des éléments 2D 

Sélectionnez un maillage et lancez le script Python suivant    *


```python
import Mesh

def extend_by_triangle(i, j, k)   *
    triangle = [input_mesh.getNodeById(element_nodes[i]),
                input_mesh.getNodeById(element_nodes[j]),
                input_mesh.getNodeById(element_nodes[k])]
    return output_mesh.extend(triangle) 

selection = FreeCADGui.Selection.getSelection()
input_mesh = App.ActiveDocument.getObject(selection[0].Name).FemMesh
output_mesh = []
for element in input_mesh.Faces   *
    element_nodes = input_mesh.getElementNodes(element)
    if len(element_nodes) in [3, 6]   *  # tria3 or tria6 (ignoring mid-nodes)
        extend_by_triangle(0, 1, 2)
    elif len(element_nodes) in [4, 8]   *  # quad4 or quad8 (ignoring mid-nodes)
        extend_by_triangle(0, 1, 2)
        extend_by_triangle(2, 3, 0)

obj = Mesh.Mesh(output_mesh)
Mesh.show(obj)
```





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM FemMesh2Mesh/fr

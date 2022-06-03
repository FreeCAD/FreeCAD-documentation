---
- GuiCommand   */fr
   Name   *FEM FemMesh2Mesh
   Name/fr   *FEM Maillage à maillage MEF
   MenuLocation   *Mesh → Maillage à maillage
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   SeeAlso   *[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM FemMesh2Mesh/fr

## Description

Cet outil converti une surface un élément 3D ou un élément FEM maille sélectionné en un élément maille . En interne, l\'élément FEM maille choisi est unique (non partagé entre deux éléments) et l\'utilise pour créer une face ou un élément maille. Optionnellement il permet de créer un maillage déformé causé par les forces établies . Ceci est fait par ajout du déplacement de FEM résultant des nœuds du maillage.

Les éléments bidimensionnels du maillage FEM ne sont pas pris en compte. Si vous devez les convertir, vous pouvez utiliser le script python ci-dessous.

## Utilisation

1.  Sélectionnez un objet de maillage MEF.
2.  En option, sélectionnez également les résultats FEM.
3.  Il existe plusieurs façons d\'appeler la commande   *
    -   Appuyez sur le bouton **<img src="images/FEM_FemMesh2Mesh.svg" width=16px> [Convertir la surface maillage MEF en maillage](FEM_FemMesh2Mesh/fr.md)**.
    -   Sélectionnez l\'option **Mesh → <img src="images/FEM_FemMesh2Mesh.svg" width=16px> MEF maillage à maillage** dans le menu.

## Script

Exemple   * Téléchargez l\'exemple 3D FEM de FreeCAD à partir de l\'atelier Start et exécutez le code suivant


```python
femmesh_obj = App.ActiveDocument.getObject("Result_mesh").FemMesh
result = App.ActiveDocument.getObject("CalculiX_static_results")
import femmesh.femmesh2mesh
out_mesh = femmesh.femmesh2mesh.femmesh_2_mesh(femmesh_obj, result)
import Mesh
Mesh.show(Mesh.Mesh(out_mesh))
```

## Convertir 2D éléments 

Sélectionnez un maillage et lancez le code suivant dans la fenêtre Python de FreeCAD


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

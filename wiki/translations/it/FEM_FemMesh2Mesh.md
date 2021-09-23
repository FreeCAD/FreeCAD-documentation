---
- GuiCommand:/it
   Name:FEM_FemMesh2Mesh
   Name/it:Converti mesh FEM in mesh
   MenuLocation:Mesh → Converti mesh FEM in mesh
   Workbenches:[FEM](FEM_Workbench/it.md)
   Shortcut:
   SeeAlso:[Tutorial di FEM](FEM_tutorial/it.md)
---

# FEM FemMesh2Mesh/it


</div>

## Descrizione

Questo strumento converte in mesh le superfici degli elementi 3D di una mesh FEM selezionata. Sceglie le facce dell\'elemento mesh FEM che sono uniche (non condivise da due elementi) e le usa per creare le facce di una mesh. Facoltativamente consente di creare una mesh deformata dall\'azione delle forze definite. Ciò avviene aggiungendo lo spostamento dei risultati FEM ai nodi della maglia.

Non vengono presi in considerazione gli elementi bidimensionali della mesh FEM. Se è necessario convertirli, è possibile utilizzare il seguente script python.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un oggetto mesh FEM (opzionalmente selezionare anche i risultati FEM)
2.  Premere il pulsante **<img src="images/FEM_FemMesh2Mesh.png" width=24px>FEM mesh to mesh
**


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script

Esempioe:

-   Caricare l\'esempio FreeCAD\'s 3D FEM dall\'ambiente Start ed eseguire il seguente codice


</div>


```python
femmesh_obj = App.ActiveDocument.getObject("Result_mesh").FemMesh
result = App.ActiveDocument.getObject("CalculiX_static_results")
import femmesh.femmesh2mesh
out_mesh = femmesh.femmesh2mesh.femmesh_2_mesh(femmesh_obj, result)
import Mesh
Mesh.show(Mesh.Mesh(out_mesh))
```

## Converting 2D elements 


<div class="mw-translate-fuzzy">

## Convertire gli elementi 2D 

Selezionare una mesh e eseguire il seguente script python


</div>


```python
import Mesh

def extend_by_triangle(i, j, k):
    triangle = [input_mesh.getNodeById(element_nodes[i]),
                input_mesh.getNodeById(element_nodes[j]),
                input_mesh.getNodeById(element_nodes[k])]
    return output_mesh.extend(triangle) 

selection = FreeCADGui.Selection.getSelection()
input_mesh = App.ActiveDocument.getObject(selection[0].Name).FemMesh
output_mesh = []
for element in input_mesh.Faces:
    element_nodes = input_mesh.getElementNodes(element)
    if len(element_nodes) in [3, 6]:  # tria3 or tria6 (ignoring mid-nodes)
        extend_by_triangle(0, 1, 2)
    elif len(element_nodes) in [4, 8]:  # quad4 or quad8 (ignoring mid-nodes)
        extend_by_triangle(0, 1, 2)
        extend_by_triangle(2, 3, 0)

obj = Mesh.Mesh(output_mesh)
Mesh.show(obj)
```


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}

---
[documentation index](../README.md) > FEM FemMesh2Mesh/it

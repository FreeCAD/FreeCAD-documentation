# FEM FemMesh2Mesh/ro
---
- GuiCommand:/ro   Name:FEM FemMesh2Mesh   Name/ro:FEM FemMesh2Mesh   MenuLocation:Mesh → FEM mesh to mesh   |Workbenches:[Shortcut:   SeeAlso:[[FEM_tutorial/ro|FEM tutorial](FEM_Workbench/ro___FEM]].md)---


</div>

## Descriere

Acest instrument transformă suprafețele elementelor 3D dintr-o plasă FEM selectată într-o plasă. Alegeți fațetele elementului FEM din plasă care sunt unice (nu sunt împărțite de două elemente) și le folosiți pentru a crea fațetele unei plase. Opțional, permite crearea unei plase deformate de acțiunea forțelor definite. Acest lucru se face prin adăugarea mișcării rezultatelor FEM la nodurile de plasă.

Elementele bidimensionale din plasa FEM nu sunt luate în considerare. Dacă trebuie să le convertiți, puteți folosi mai jos un script Python.


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Selectați un obiect FEM mesh (opțional selectați suplimentar rezultatele FEM)
2.  Apasă pe butonul **<img src="images/FEM_FemMesh2Mesh.png" width=24px>FEM mesh to mesh
**


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script-Programare 

Exemplu:

-   Încărcați exemplul 3D FEM al FreeCAD din Start Workbench și executați următorul cod


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

## Conversia elementelor 2D 

Selectați o plasă și rulați următorul script python


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





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM FemMesh2Mesh/ro

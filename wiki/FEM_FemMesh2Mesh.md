---
- GuiCommand:
   Name:FEM FemMesh2Mesh
   MenuLocation:Mesh → FEM mesh to mesh
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

## Description

This tool converts surfaces of 3D elements of a selected FEM mesh to mesh. Internally it picks FEM mesh element faces which are unique (not shared by two elements) and uses them to create faces of a mesh. Optionally it allows to create a deformed mesh caused by the action of the defined forces. This is done by adding the displacement of the FEM results to the mesh nodes.

Two dimensional elements from the FEM mesh are not taken into account. If you need to convert them, you can use a python script below.

## Usage

1.  Select a FEM mesh object.
2.  Optionally also select the FEM results.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_FemMesh2Mesh.svg" width=16px> [FEM FemMesh2Mesh](FEM_FemMesh2Mesh.md)** button.
    -   Select the **Mesh → <img src="images/FEM_FemMesh2Mesh.svg" width=16px> FEM mesh to mesh** option from the menu.

## Scripting

Example: Load FreeCAD\'s 3D FEM example from the Start Workbench and run the following code

 
```python
femmesh_obj = App.ActiveDocument.getObject("Result_mesh").FemMesh
result = App.ActiveDocument.getObject("CalculiX_static_results")
import femmesh.femmesh2mesh
out_mesh = femmesh.femmesh2mesh.femmesh_2_mesh(femmesh_obj, result)
import Mesh
Mesh.show(Mesh.Mesh(out_mesh))
```

## Converting 2D elements 

Select a mesh and run the following python script

 
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




 {{FEM Tools navi}} 

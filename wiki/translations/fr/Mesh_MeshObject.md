# Mesh MeshObject/fr
## Description

Un [Mesh MeshObject](Mesh_MeshObject/fr.md), ou officiellement `Mesh::MeshObject`, est une classe qui définit une structure de données de maillage dans le logiciel. Ceci est similaire à la [Part TopoShape](Part_TopoShape/fr.md) mais pour [Mesh](Mesh/fr.md).

Les maillages sont normalement créés avec l\'[atelier Mesh](Mesh_Workbench/fr.md), ou importés à partir de STL, OBJ et de formats de fichier de maillage similaires.

Notez que l\'**<img src="images/Workbench_FEM.svg" width=16px> [atelier FEM](FEM_Workbench/fr.md)** utilise également des maillages, mais dans ce cas, il utilise une structure de données différente, appelée [FEM Mesh](FEM_Mesh/fr.md) (classe `Fem::FemMesh`). Ces informations ne s\'appliquent pas aux maillages FEM.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramme simplifié des relations entre les objets principaux du programme. La classe `Mesh::MeshObject* est incorporée dans l'objet {{incode|Mesh::Feature` et à partir de là, elle est propagée à tous les objets qui en sont dérivés.}}

## Utilisation

Le Mesh MeshObject est un objet assigné à certains [App DocumentObjects](App_DocumentObject/fr.md).

En particulier, l\'objet de base qui gère ces types d\'attributs est la [fonction Mesh](Mesh_Feature/fr.md) (`Mesh::Feature` class). Tous les objets dérivés de cette classe auront accès à un objet Mesh MeshObject.

Les objets les plus remarquables qui auront un objet Mesh MeshObject sont les suivants:

-   Tout maillage primitif créé avec le [atelier Mesh](Mesh_Workbench/fr.md).
-   Tout objet créé en important une STL, OBJ et des fichiers de format de maillage similaires.

## Script


**Voir aussi:**

[Notions de base sur les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md) et [objets scriptés](Scripted_objects/fr.md). Pour une liste complète des attributs et des méthodes, consultez l\'outil [documentation source](Source_documentation/fr.md) et l\'outil [Std PythonHelp](Std_PythonHelp/fr.md).

Tous les objets dérivés de `Mesh::Feature` auront un [Mesh MeshObject](Mesh_MeshObject/fr.md), qui est normalement accessible à partir de son attribut `Mesh`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Mesh::Cube", "Cube")
App.ActiveDocument.recompute()
print(obj.Mesh)
```

Un MeshObject possède de nombreux attributs (variables) et méthodes qui contiennent des informations à son sujet et qui permettent de faire des opérations avec lui. Ces variables et méthodes peuvent être testées dans la [console Python](Python_console/fr.md).


```python
print(obj.Mesh.Area)
print(obj.Mesh.BoundBox)
print(obj.Mesh.CountPoints)
print(obj.Mesh.Volume)

obj.Mesh.copy()
obj.Mesh.countComponents()
obj.Mesh.getEigenSystem()
obj.Mesh.write("my_file.stl")
```


{{Mesh Tools navi

}} {{Document objects navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh MeshObject/fr

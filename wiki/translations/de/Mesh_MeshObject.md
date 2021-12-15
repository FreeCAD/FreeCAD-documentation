# Mesh MeshObject/de
## Beschreibung

Ein _, aber für [Polygonnetze](Mesh/de.md).

Meshes are normally created with the [Mesh Workbench](Mesh_Workbench.md), or imported from STL, OBJ, and similar mesh file formats.

Please note that the **<img src="images/Workbench_FEM.svg" width=16px> [FEM Workbench](FEM_Workbench.md)** also uses meshes, but in this case, it uses a different data structure, called [FEM FemMesh](FEM_Mesh.md) (`Fem::FemMesh` class). This information does not apply to FEM meshes.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Simplified diagram of the relationships between the core objects in the program. The `Mesh::MeshObject* class is embedded in the {{incode|Mesh::Feature` object and from there it is propagated to all objects that are derived from it.}}

## Usage

The Mesh MeshObject is an object that is assigned to some [App DocumentObjects](App_DocumentObject.md).

In particular, the basic object that handles these types of attributes is the [Mesh Feature](Mesh_Feature.md) (`Mesh::Feature` class). All objects derived from this class will have access to a Mesh MeshObject.

The most notable objects that will have a Mesh MeshObject are the following:

-   Any primitive mesh created with the [Mesh Workbench](Mesh_Workbench.md).
-   Any object created by importing an STL, OBJ, and similar mesh format files.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), and [scripted objects](Scripted_objects.md). For a full list of attributes and methods, consult the [source documentation](Source_documentation.md), and the [Std PythonHelp](Std_PythonHelp.md) tool.

All objects derived from `Mesh::Feature` will have a [Mesh MeshObject](Mesh_MeshObject.md), which is normally accessible from its `Mesh` attribute.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("Mesh::Cube", "Cube")
App.ActiveDocument.recompute()
print(obj.Mesh)
```

A MeshObject has many attributes (variables) and methods that contain information about it, and which allow doing operations with it. These variables and methods can be tested in the [Python console](Python_console.md).


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
[documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh MeshObject/de

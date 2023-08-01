---
- GuiCommand:
   Name: Mesh TrimByPlane
   MenuLocation: Meshes - Cutting - Trim mesh with a plane
   Workbenches: [Mesh](Mesh_Workbench.md)
   SeeAlso: [Mesh PolyCut](Mesh_PolyCut.md), [Mesh PolyTrim](Mesh_PolyTrim.md)
---

# Mesh TrimByPlane/de



## Beschreibung

The **Mesh TrimByPlane** command trims faces and parts of faces on one side of a plane from a mesh object.



## Anwendung

1.  Select a single mesh object and a single [Part plane](Part_Plane.md). The (extended) plane should intersect the mesh object.

2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_TrimByPlane.svg" width=16px> [Mesh TrimByPlane](Mesh_TrimByPlane.md)** button.
    -   Select the **Meshes → Cutting → <img src="images/Mesh_TrimByPlane.svg" width=16px> Trim mesh with a plane** option from the menu.

3.  The **Trim by plane** dialog box opens.

4.  
    **Select the side you want to keep**by pressing one of the buttons:

    -   
        {{button|Below}}
        

    -   
        {{button|Above}}
        

    -   
        {{button|Split}}
        
        : removes the faces and parts of faces above the plane, and creates a new mesh object containing them.



## Skripten

See also: [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To trim a mesh with a plane use its `trimByPlane` method.


```python
import FreeCAD as App
import Mesh

# Create a non-parametric box-shaped mesh:
msh = App.ActiveDocument.addObject("Mesh::Feature", "Mesh")
msh.Mesh = Mesh.createBox(30, 40, 50)
msh.ViewObject.DisplayMode = "Flat Lines"

# Define a plane by a base point and a normal vector:
pnt = App.Vector(25, 0, 0)
nor = App.Vector(0, 0, 1)

# We need to work on a copy of the msh.Mesh object:
new_msh = msh.Mesh.copy()

# Trim that copy:
new_msh.trimByPlane(pnt, nor)

# Update msh.Mesh:
msh.Mesh = new_msh
```





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh TrimByPlane/de

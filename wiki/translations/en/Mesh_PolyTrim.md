---
- GuiCommand:
   Name:Mesh PolyTrim
   MenuLocation:Meshes - Cutting - Trim mesh
   Workbenches:[Mesh](Mesh_Workbench.md)
   SeeAlso:[Mesh PolyCut](Mesh_PolyCut.md), [Mesh TrimByPlane](Mesh_TrimByPlane.md)
---

# Mesh PolyTrim/en

## Description

The **Mesh PolyTrim** command trims faces and parts of faces from mesh objects.

## Usage

1.  During the command the [3D view](3D_view.md) cannot be changed. It is advisable to properly line up the 3d view first.
2.  Select one or more mesh objects.
3.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_PolyTrim.svg" width=16px> [Mesh PolyTrim](Mesh_PolyTrim.md)** button.
    -   Select the **Meshes → Cutting → <img src="images/Mesh_PolyTrim.svg" width=16px> Trim mesh** option from the menu.
4.  Define a polygon by picking points in the 3D view.
5.  Select an option from the 3D view context menu:
    -   
        **Inner**
        
        : removes the faces and parts of faces that are inside the polygon.

    -   
        **Outer**
        
        : removes the faces and parts of faces that are outside the polygon.

    -   
        **Split**
        
        : removes the faces and parts of faces that are outside the polygon, and creates a new mesh object containing them.

    -   
        **Cancel**
        
        : cancels the command.

## Scripting

See also: [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To trim a mesh with a polygon use its `trim` method.


```python
import FreeCAD as App
import Mesh

# Create a non-parametric box-shaped mesh:
msh = App.ActiveDocument.addObject("Mesh::Feature", "Mesh")
msh.Mesh = Mesh.createBox(30, 40, 50)
msh.ViewObject.DisplayMode = "Flat Lines"

# Define some points:
p1 = App.Vector(0, 0, 0)
p2 = App.Vector(60, 0, 0)
p3 = App.Vector(60, 60, 0)

# We need to work on a copy of the msh.Mesh object:
new_msh = msh.Mesh.copy()

# Trim that copy:
new_msh.trim([p1, p2, p3], 0) # 2nd argument: 0=inner, 1=outer.

# Update msh.Mesh:
msh.Mesh = new_msh
```





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh PolyTrim/en

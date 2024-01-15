---
 GuiCommand:
   Name: Mesh SectionByPlane
   MenuLocation: Meshes , Cutting , Create section from mesh and plane
   Workbenches: Mesh_Workbench
   SeeAlso: Mesh_CrossSections
---

# Mesh SectionByPlane

## Description

The **Mesh SectionByPlane** command creates a cross section across a mesh object. The cross section is a [Part Feature](Part_Feature.md).

## Usage

1.  Select a single mesh object and a single [Part plane](Part_Primitives.md). The (extended) plane should intersect the mesh object.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_SectionByPlane.svg" width=16px> [Create section from mesh and plane](Mesh_SectionByPlane.md)** button.
    -   Select the **Meshes → Cutting → <img src="images/Mesh_SectionByPlane.svg" width=16px> Create section from mesh and plane** option from the menu.

## Properties

See: [Part Feature](Part_Feature.md).

## Scripting

See also: [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To section a mesh use its `section` method. The method requires a second mesh object that need not be planar.

 
```python
import FreeCAD as App
import Mesh
import Part

# Create a non-parametric box-shaped mesh:
msh = App.ActiveDocument.addObject("Mesh::Feature", "Mesh")
msh.Mesh = Mesh.createBox(30, 40, 50)
msh.ViewObject.DisplayMode = "Flat Lines"

# Create a planar mesh from 3 points:
p1 = App.Vector(-20, -60, 0)
p2 = App.Vector(65, 25, 0)
p3 = App.Vector(-20, 25, 0)
msh_plane = Mesh.Mesh([p1, p2, p3])

# Find the section loops (each loop is a list of points):
loops = msh.Mesh.section(msh_plane)

# Show the loop polygon:
Part.show(Part.makePolygon(loops[0]))
```




 {{Mesh Tools navi}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh SectionByPlane

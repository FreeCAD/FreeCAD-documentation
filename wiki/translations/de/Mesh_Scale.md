---
- GuiCommand:
   Name:Mesh Scale
   Name/de:Mesh Skalieren
   MenuLocation:Netze - Skalieren...
   Workbenches:[Mesh](Mesh_Workbench/de.md)
---

# Mesh Scale/de



## Beschreibung

Der Befehl **Mesh Skalieren** passt die Größe von Netzobjekten an.



## Anwendung

1.  Select one or more mesh objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_Scale.svg" width=16px> [Mesh Scale](Mesh_Scale.md)** button.
    -   Select the **Meshes → <img src="images/Mesh_Scale.svg" width=16px> Scale...** option from the menu.
3.  The **Scaling** dialog box opens.
4.  Specify a scaling factor, the value must be larger than {{Value|0}}.
5.  Press the {{button|OK}} button to finish the command.

## Scripting

See also: [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To scale a mesh use its `transformGeometry` method.


```python
import FreeCAD as App
import Mesh

# Create a non-parametric box-shaped mesh:
msh = App.ActiveDocument.addObject("Mesh::Feature", "Mesh")
msh.Mesh = Mesh.createBox(10, 10, 10)
msh.ViewObject.DisplayMode = "Flat Lines"

# Create and scale a matrix:
mat = App.Matrix()
mat.scale(2.0, 3.0, 4.0) # Unequal scaling.

# We need to work on a copy of the msh.Mesh object:
new_msh = msh.Mesh.copy()

# Transform that copy:
new_msh.transformGeometry(mat)

# Update msh.Mesh:
msh.Mesh = new_msh
```





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Scale/de

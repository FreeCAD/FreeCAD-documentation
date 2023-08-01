---
- GuiCommand:/it
   Name:Mesh_Scale
   Name/it:Scala
   MenuLocation:Mesh → Scala...
   Workbenches:[Mesh](Mesh_Workbench/it.md)
---

# Mesh Scale/it



## Descrizione

Il comando **Scala** scala gli oggetti mesh.



## Utilizzo

1.  Selezionaare uno o più oggetti mesh.
2.  Esistono diversi modi per invocare il comando:
    -   Premere il bottone **<img src="images/Mesh_Scale.svg" width=16px> [Mesh Scale](Mesh_Scale/it.md)**.
    -   Selezionare l\'opzione **Meshes → <img src="images/Mesh_Scale.svg" width=16px> Scale...** dal menu.
3.  Il box dialogo **Scaling** si apre.
4.  Specificare un fattore di scala, il valore deve essere maggiore di {{Value|0}}.
5.  Premere il bottone {{button|OK}} per terminare il comando.



## Script

Vedere anche: [Script di base per FreeCAD](FreeCAD̠_Scripting_Basics/it.md)

Per scalare una mesh usare il suo metodo `transformGeometry`.


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
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Scale/it

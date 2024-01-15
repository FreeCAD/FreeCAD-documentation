---
 GuiCommand:
   Name: Mesh_Scale
   Name/it: Scala
   MenuLocation: Mesh , Scala...
   Workbenches: Mesh Workbench/it
---

# Mesh Scale/it



## Descrizione

Il comando **Scala** scala gli oggetti mesh.



## Utilizzo

1.  Selezionare uno o più oggetti mesh.
2.  Esistono diversi modi per invocare il comando:
    -   Premere il bottone **<img src="images/Mesh_Scale.svg" width=16px> [Scala...](Mesh_Scale/it.md)**.
    -   Selezionare l\'opzione **Mesh → <img src="images/Mesh_Scale.svg" width=16px> Scala...** dal menu.
3.  Il box dialogo **Scalatura** si apre.
4.  Specificare un fattore di scala, il valore deve essere maggiore di {{Value|0}}.
5.  Premere il bottone {{button|OK}} per terminare il comando.



## Script

Vedere anche: [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

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
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Scale/it

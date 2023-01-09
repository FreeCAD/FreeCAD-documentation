---
- GuiCommand:/it
   Name:Mesh_SectionByPlane
   Name/it:Sezione da mesh e piano
   MenuLocation:Mesh → Taglio → Sezione da mesh e piano
   Workbenches:[Mesh](Mesh_Workbench/it.md)
   SeeAlso:[Sezioni](Mesh_CrossSections/it.md)
---

# Mesh SectionByPlane/it



## Descrizione

Il comando **Sezione da mesh e piano** crea una sezione trasversale attraverso un oggetto mesh. La sezione trasversale è una [Part Feature](Part_Feature/it.md).



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un singolo oggetto mesh e un singolo [piano di Part](Part_Primitives/it.md). Il piano (esteso) deve intersecare l\'oggetto mesh.
2.  Selezionare l\'opzione **Mesh → Taglio → <img src="images/Mesh_SectionByPlane.svg" width=16px> Sezione da mesh e piano** dal menu.


</div>



## Proprietà

Vedere: [Funzioni Part](Part_Feature/it.md).

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


<div class="mw-translate-fuzzy">





</div>


{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh SectionByPlane/it

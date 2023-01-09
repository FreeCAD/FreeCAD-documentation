---
- GuiCommand:/it
   Name:Mesh_TrimByPlane
   Name/it:Rifila con un piano
   MenuLocation:Mesh → Taglio → Rifila con un piano
   Workbenches:[Mesh](Mesh_Workbench/it.md)
   SeeAlso:[Taglia la mesh](Mesh_PolyCut/it.md), [Rifila con un poligono](Mesh_PolyTrim/it.md)
---

# Mesh TrimByPlane/it



## Descrizione

Il comando **Rifila con un piano** taglia facce e parti di facce su un lato di un piano da un oggetto mesh.



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un singolo oggetto mesh e un singolo [piano di Part](Part_Primitives/it.md). Il piano (esteso) deve intersecare l\'oggetto mesh.

2.  Selezionare l\'opzione **Mesh → Taglio → <img src="images/Mesh_TrimByPlane.svg" width=16px> Rifila con un piano** dal menu.

3.  Si apre la finestra di dialogo **Rifila con un piano**.

4.  
    **Selezionare il lato da mantenere**premendo uno dei pulsanti:

    -   
        {{button|Sopra}}
        

    -   
        {{button|Sotto}}
        

    -   
        {{button|Dividi}}
        
        : rimuove le facce e le parti delle facce sopra il piano e crea un nuovo oggetto mesh che le contiene.


</div>

## Scripting

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


<div class="mw-translate-fuzzy">





</div>


{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh TrimByPlane/it

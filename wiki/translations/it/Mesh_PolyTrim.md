---
- GuiCommand:
   Name:Mesh_PolyTrim
   Name/it:Rifila con un poligono
   MenuLocation:Mesh - Taglio - Rifila con un poligono
   Workbenches:[Mesh](Mesh_Workbench/it.md)
   SeeAlso:[Taglia la mesh](Mesh_PolyCut/it.md), [Rifila con un piano](Mesh_TrimByPlane/it.md)
---

# Mesh PolyTrim/it



## Descrizione

Il comando **Rifila con un poligono** taglia facce e parti di facce da oggetti mesh.



## Utilizzo

1.  Durante il comando non è possibile modificare la [vista 3D](3D_view.md). Si consiglia di allineare correttamente prima la vista 3D.
2.  Selezionare uno o più oggetti mesh.
3.  Esistono diversi modi per invocare il comando:
    -   Premere il bottone **<img src="images/Mesh_PolyTrim.svg" width=16px> [Mesh PolyTrim](Mesh_PolyTrim.md)**.
    -   Selezionare l\'opzione **Mesh → Taglio → <img src="images/Mesh_PolyTrim.svg" width=16px> Rifila con un poligono** dal menu.
4.  Definire un poligono selezionando dei punti nella vista 3D.
5.  Selezionare un\'opzione dal menu contestuale della vista 3D:
    -   
        **Interno**
        
        : rimuove le facce che sono (parzialmente) all\'interno del poligono.

    -   
        **Esterno**
        
        : rimuove le facce che sono completamente al di fuori del poligono.

    -   
        **Dividi**
        
        : rimuove le facce che sono completamente esterne al poligono e crea un nuovo oggetto mesh che le contiene.

    -   
        **Annulla**
        
        : annulla il comando.



## Script

Vedere anche: [Script di base per FreeCAD](FreeCAD̠_Scripting_Basics/it.md)

Per tagliare una mesh con un poligono usare il suo metodo `trim`.


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
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh PolyTrim/it

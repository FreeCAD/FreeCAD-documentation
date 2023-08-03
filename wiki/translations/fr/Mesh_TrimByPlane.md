---
 GuiCommand:
   Name: Mesh TrimByPlane
   Name/fr: Mesh Ajuster par plan
   MenuLocation: Maillages , Couper , Ajuster le maillage avec un plan
   Workbenches: Mesh_Workbench/fr
   SeeAlso: Mesh_PolyCut/fr, Mesh_PolyTrim/fr
---

# Mesh TrimByPlane/fr

## Description

La commande **Ajuster par plan** permet de découper les faces et parties de faces d\'un côté d\'un plan à partir d\'un objet maillé.



## Utilisation

1.  Sélectionnez un seul objet maillé et un seul [Part Plan](Part_Plane/fr.md). Le plan (étendu) doit croiser l\'objet maillé.

2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_TrimByPlane.svg" width=16px> [Ajuster le maillage avec un plan](Mesh_TrimByPlane/fr.md)
**
    -   Sélectionnez l\'option **Maillages → Couper → <img src="images/Mesh_TrimByPlane.svg" width=16px> Ajuster le maillage avec un plan** du menu.

3.  La boîte de dialogue **Découpe par un plan** s\'ouvre.

4.  
    **Sélectionnez le côté que vous souhaitez garder**en appuyant sur l\'un des boutons:

    -   
        **En-dessous**
        

    -   
        **Au-dessus**
        

    -   
        **Scinder**
        
        : supprime les faces et les parties de faces au-dessus du plan et crée un nouveau maillage les contenant.



## Script

Voir aussi : [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour découper un maillage avec un plan, utilisez sa méthode `trimByPlane`.


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
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh TrimByPlane/fr

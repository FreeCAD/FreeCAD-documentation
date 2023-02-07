---
- GuiCommand:/fr
   Name:Mesh PolyTrim
   Name/fr:Mesh Découper
   MenuLocation:Maillages → Couper → Découper
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   SeeAlso:[Mesh Couper le maillage](Mesh_PolyCut/fr.md), [Mesh Ajuster par plan](Mesh_TrimByPlane/fr.md)
---

# Mesh PolyTrim/fr

## Description

La commande **Mesh Découper** permet de découper les faces et parties de faces à partir d\'objets maillés.



## Utilisation

1.  Pendant la commande, la [Vue 3D](3D_view/fr.md) ne peut pas être modifiée. Il est conseillé d\'aligner correctement la vue 3D en premier.
2.  Sélectionnez un ou plusieurs objets maillés.
3.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_PolyTrim.svg" width=16px> [Découper](Mesh_PolyTrim/fr.md)**.
    -   Sélectionnez l\'option **Maillages → Couper → <img src="images/Mesh_PolyTrim.svg" width=16px> Découper** dans le menu.
4.  Définissez un polygone en sélectionnant des points dans la vue 3D.
5.  Sélectionnez une option dans le menu contextuel de la vue 3D:
    -   
        **Intérieur**
        
        : supprime les faces et les parties de faces qui sont à l\'intérieur du polygone.

    -   
        **Extérieur**
        
        : supprime les faces et les parties de faces qui sont en dehors du polygone.

    -   
        **Scinder**
        
        : supprime les faces et les parties de faces qui sont en dehors du polygone et crée un nouvel objet maillé les contenant.

    -   
        **Annuler**
        
        : annule la commande.



## Script

Voir aussi : [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour découper un maillage avec un polygone, utilisez sa méthode `trim`.


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
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh PolyTrim/fr

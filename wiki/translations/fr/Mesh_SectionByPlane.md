---
- GuiCommand:
   Name: Mesh SectionByPlane
   Name/fr: Mesh Section
   MenuLocation: Maillages -> Couper -> Créer une section à partir d'un maillage et d'un plan
   Workbenches: Mesh_Workbench/fr
   SeeAlso: Mesh_CrossSections/fr
---

# Mesh SectionByPlane/fr

## Description

La commande **Section** crée une coupe transversale à travers un objet maillé. La section transversale est une [Part Feature](Part_Feature/fr.md).



## Utilisation

1.  Sélectionnez un seul objet maillage et un seul [Part Plan](Part_Primitives/fr.md). Le plan (étendu) doit croiser l\'objet maillé.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_SectionByPlane.svg" width=16px> [Créer une section à partir d'un maillage et d'un plan](Mesh_SectionByPlane/fr.md)**.
    -   Sélectionnez l\'option **Maillages → Couper → <img src="images/Mesh_SectionByPlane.svg" width=16px> Créer une section à partir d'un maillage etd'un plan** du menu.



## Propriétés

Voir: [Part Feature](Part_Feature/fr.md).



## Script

Voir aussi : [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour sectionner un maillage, utilisez sa méthode `section`. Cette méthode nécessite un deuxième objet maillé qui ne doit pas nécessairement être planaire.


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





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh SectionByPlane/fr

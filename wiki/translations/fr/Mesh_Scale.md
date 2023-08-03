---
 GuiCommand:
   Name: Mesh Scale
   Name/fr: Mesh Echelle
   MenuLocation: Maillages , Échelle...
   Workbenches: Mesh_Workbench/fr
---

# Mesh Scale/fr

## Description

La commande **Échelle** met à l\'échelle les objets maillés.



## Utilisation

1.  Sélectionnez un ou plusieurs objets maillés.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_Scale.svg" width=16px> [Échelle...](Mesh_Scale/fr.md)
**
    -   Sélectionnez l\'option **Maillages → <img src="images/Mesh_Scale.svg" width=16px> Échelle...** du menu.
3.  La boîte de dialogue **Mettre à l'échelle** s\'ouvre.
4.  Spécifiez un facteur de mise à l\'échelle, la valeur doit être supérieure à {{Value|0}}.
5.  Appuyez sur le bouton {{button|OK}} pour terminer la commande.



## Script

Voir aussi : [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

Pour mettre à l\'échelle un maillage, utilisez sa méthode `transformGeometry`.


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
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Scale/fr

---
 GuiCommand:
   Name: OpenSCAD ResizeMeshFeature
   Name/fr: OpenSCAD Redimensionner le maillage
   MenuLocation: OpenSCAD , Redimensionner le maillage
   Workbenches: OpenSCAD_Workbench/fr
---

# OpenSCAD ResizeMeshFeature/fr

## Description

Crée un nouvel objet maillé redimensionné avec un dimensionnement indépendant pour chaque axe.



## Utilisation

1.  Sélectionnez l\'objet maillé à mettre en miroir.
2.  Cliquez sur le menu **OpenSCAD** → **<img src="images/OpenSCAD_ResizeMeshFeature.svg" width=24px> Redimensionner le maillage**.
3.  Sélectionnez l\'axe souhaité dans la fenêtre de dialogue ou entrez votre propre axe personnalisé à utiliser et cliquez sur OK.

-   Un nouvel objet est créé et redimensionné, l\'objet d\'origine est masqué.

## Limitations

-   Le nouvel objet maillé n\'est pas paramétrique par rapport à l\'objet maillé d\'origine, ce qui signifie que les modifications apportées à l\'objet d\'origine ne sont pas reflétées dans le nouvel objet en miroir.



## Remarques

-   La fonction ne modifie pas le maillage existant mais renvoie un nouveau maillage.
-   La fonction est accessible via Python :


```python
import OpenSCADUtils
import Mesh
#this assumes an existing object in the document named "Mesh" that you wish to mirror
original_mesh = App.ActiveDocument.Mesh
resized_mesh = OpenSCADUtils.resizemesh(original_mesh.Mesh, FreeCAD.Base.Vector(100,50,40))
#New mesh would be 100 mm on the x axis, 50 mm on the y axis, and 40 mm on the z axis.
Mesh.show(resized_mesh)
```





{{OpenSCAD_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD ResizeMeshFeature/fr

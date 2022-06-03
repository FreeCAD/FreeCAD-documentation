---
- GuiCommand   */fr
   Name   *OpenSCAD ResizeMeshFeature
   Name/fr   *OpenSCAD Redimensionner le maillage
   MenuLocation   *OpenSCAD → Redimensionnement du maillage...
   Workbenches   *[OpenSCAD](OpenSCAD_Workbench/fr.md)
---

# OpenSCAD ResizeMeshFeature/fr

## Description

Crée un nouvel objet maillé redimensionné avec un dimensionnement indépendant pour chaque axe.

## Utilisation

1.  Sélectionnez l\'objet maillé à mettre en miroir.
2.  Cliquez sur le menu **OpenSCAD** → **<img src="images/OpenSCAD_ResizeMeshFeature.svg" width=24px> Redimensionnement du maillage...** .
3.  Sélectionnez l\'axe souhaité dans la boîte de dialogue ou entrez votre propre axe personnalisé à utiliser et cliquez sur OK.

-   Un nouvel objet est créé et redimensionné, l\'objet d\'origine est masqué.

## Limitations

-   Le nouvel objet maillé n\'est pas paramétrique par rapport à l\'objet maillé d\'origine, ce qui signifie que les modifications apportées à l\'objet d\'origine ne sont pas reflétées dans le nouvel objet en miroir.

## Remarques

-   La fonction ne modifie pas le maillage existant mais renvoie un nouveau maillage.
-   La fonction est accessible via python   *


```python
import OpenSCADUtils
import Mesh
##Cela suppose un objet existant dans le document nommé "Mesh" que vous souhaitez mettre à l'échelle
original_mesh = App.ActiveDocument.Mesh
resized_mesh = OpenSCADUtils.resizemesh(original_mesh.Mesh, FreeCAD.Base.Vector(100,50,40))
#Le nouveau maillage serait de 100 mm sur l'axe x, 50 mm sur l'axe y et 40 mm sur l'axe z.
Mesh.show(resized_mesh)
```





{{OpenSCAD_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD ResizeMeshFeature/fr

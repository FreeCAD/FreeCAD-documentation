---
 GuiCommand:
   Name: OpenSCAD ScaleMeshFeature
   Name/fr: OpenSCAD Mise à l'échelle du maillage
   MenuLocation: OpenSCAD , Mettre à l'échelle le maillage
   Workbenches: OpenSCAD_Workbench/fr
   SeeAlso: Mesh_Scale/fr
---

# OpenSCAD ScaleMeshFeature/fr

## Description

Crée un nouvel objet maillé mis à l\'échelle avec une mise à l\'échelle indépendante pour chaque axe.

## Utilisation

1.  Sélectionnez l\'objet maillé à mettre à l\'échelle.
2.  Cliquez sur le menu **OpenSCAD → Mettre à l'échelle le maillage**.
3.  Sélectionnez l\'axe souhaité dans la boîte de dialogue, ou entrez votre propre axe personnalisé à utiliser et cliquez sur OK.

-   Un nouvel objet est créé et mis à l\'échelle, l\'objet d\'origine est masqué.

## Limitations

-   Le nouvel objet maillé n\'est pas paramétrique par rapport à l\'objet maillé d\'origine, ce qui signifie que les modifications apportées à l\'objet d\'origine ne sont pas reflétées dans le nouvel objet mis à l\'échelle.

## Remarques

-   La fonction ne modifie pas le maillage existant mais renvoie un nouveau maillage.
-   La fonction est accessible via Python :


```python
import OpenSCADUtils
import Mesh
#this assumes an existing object in the document named "Mesh" that you wish to scale
original_mesh = App.ActiveDocument.Mesh
scaled_mesh = OpenSCADUtils.scalemesh(original_mesh.Mesh, FreeCAD.Base.Vector(1,0,0))
Mesh.show(scaled_mesh)
```





{{OpenSCAD_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD ScaleMeshFeature/fr

---
- GuiCommand:
   Name: OpenSCAD MirrorMeshFeature
   Name/fr: OpenSCAD Miroir du maillage 
   MenuLocation: OpenSCAD -> Miroir du maillage
   Workbenches: OpenSCAD_Workbench/fr
   SeeAlso: Part_Mirror/fr
---

# OpenSCAD MirrorMeshFeature/fr

## Description

Crée un nouvel objet maillé en miroir, symmétrisé autour de l\'axe sélectionné.

## Utilisation

1.  Sélectionnez l\'objet maillé à mettre en miroir.
2.  Cliquez sur le menu **OpenSCAD → Miroir du maillage**.
3.  Sélectionnez l\'axe souhaité dans la boîte de dialogue, ou entrez votre propre axe personnalisé à utiliser et cliquez sur OK.

-   Un nouvel objet est créé et mis en miroir, l\'objet d\'origine est masqué.

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
mirrored_mesh = OpenSCADUtils.mirrormesh(original_mesh.Mesh, FreeCAD.Base.Vector(1,0,0))
Mesh.show(mirrored_mesh)
```





{{OpenSCAD_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD MirrorMeshFeature/fr

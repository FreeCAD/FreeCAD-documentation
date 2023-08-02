---
- GuiCommand:
   Name: FEM MeshClear
   Name/fr: FEM Supprimer maillage FEM
   MenuLocation: Menu contextuel sur l'objet maillé -> Effacer le maillage FEM
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
---

# FEM MeshClear/fr

## Description

Permet à l\'utilisateur de réinitialiser le maillage à partir de l\'objet maillé FEM FreeCAD. Le maillage existe toujours mais n\'a pas de sommets, d\'arêtes, de faces ou d\'éléments. Les informations de maillage, les paramètres Netgen/Gmsh, les régions maillées, les groupes de mailles et la couche limite du maillage restent dans l\'arbre du modèle, ce qui signifie que le maillage peut être reproduit ultérieurement. L\'utilisation principale de cette fonction est d\'alléger le fichier FreeCAD, soit pour améliorer les performances lors de l\'utilisation de FreeCAD, soit pour économiser de l\'espace disque ou permettre un transfert facile des fichiers sans perdre les données de maillage.

## Utilisation

1.  Cliquez avec le bouton droit de la souris sur un objet maillé FEM <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:16px;"> [Netgen](FEM_MeshNetgenFromShape/fr.md) ou <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:16px;"> [Gmsh](FEM_MeshGmshFromShape/fr.md) dans la [Vue en arborescence](Tree_view/fr.md).
2.  Sélectionnez l\'option **<img src="images/FEM_MeshClear.svg" width=16px> Effacer le maillage FEM** dans le menu contextuel.

## Remarques

Les objets de l\'arborescence du modèle sont maintenus car ils représentent les données de maillage mais le maillage est maintenant effacé du fichier FreeCAD.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MeshClear/fr

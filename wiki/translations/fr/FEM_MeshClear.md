---
- GuiCommand:/fr
   Name:FEM MeshClear
   Name/fr:FEM Supprimer maillage MEF
   MenuLocation:Menu contextuel sur l'objet maillé → Supprimer maillage MEF
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[Tutoriel FEM](FEM_tutorial/fr.md)
---

# FEM MeshClear/fr

## Description

Permet à l\'utilisateur de réinitialiser le maillage à partir de l\'objet maillé MEF FreeCAD. Le maillage existe toujours mais n\'a pas de sommets, d\'arêtes, de faces ou d\'éléments. Les informations de maillage, les paramètres Netgen/Gmsh, les régions maillées, les groupes de mailles et la couche limite du maillage restent dans l\'arbre du modèle, ce qui signifie que le maillage peut être reproduit ultérieurement. L\'utilisation principale de cette fonction est d\'alléger le fichier FreeCAD, soit pour améliorer les performances lors de l\'utilisation de FreeCAD, soit pour économiser de l\'espace disque ou permettre un transfert facile des fichiers sans perdre les données de maillage.

## Utilisation

1.  Clic droit sur l\'objet maillé dans l\'arbre des modèles <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [Maillage MEF à partir d\'une forme avec Gmsh](FEM_MeshGmshFromShape/fr.md).
2.  Sélectionnez le <img alt="" src=images/FEM_MeshClear.svg  style="width:32px;"> [FEM mesh from shape by Gmsh](FEM_MeshGmshFromShape/fr.md) Effacer le maillage MEF.

## Remarques

Les objets de l\'arborescence du modèle sont maintenus car ils représentent les données de maillage mais le maillage est maintenant effacé du fichier FreeCAD.





{{FEM Tools navi

}}

---
[documentation index](../README.md) > FEM MeshClear/fr

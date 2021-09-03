---
- GuiCommand:/fr
   Name:Mesh RemeshGmsh
   Name/fr:Mesh Affinage
   MenuLocation:Maillages → Affinage...
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Mesh Tesselation](Mesh_FromPartShape/fr.md)
---

## Description

La commande **Mesh Affinage** remet à nouveau un objet maillé en utilisant le mailleur [Gmsh](https://gmsh.info/). Le nouveau maillage peut être plus fin ou plus grossier.

## Utilisation

1.  Sélectionnez un seul objet maillé.
2.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/Mesh_RemeshGmsh.svg" width=16px> [Affiner le maillage existant](Mesh_RemeshGmsh/fr.md)
**
    -   Sélectionnez l\'option **Maillages → <img src="images/Mesh_RemeshGmsh.svg" width=16px> Affinage...** dans le menu.
3.  Le panneau des tâches **Remaiilage par gmsh** s\'ouvre.
4.  Spécifiez les paramètres requis. Voir la [configuration du mailleur Gmsh](Mesh_FromPartShape/fr#Mailleur_Gmsh.md) de la commande [Mesh Tesselation](Mesh_FromPartShape/fr.md).
5.  Appuyez sur le bouton **Apply** pour remailler l\'objet maillé.
6.  Modifiez éventuellement un ou plusieurs paramètres et appuyez à nouveau sur le bouton **Apply** jusqu\'à ce que le nouveau maillage vous convienne.
7.  Appuyez sur le bouton **Close** pour fermer le panneau des tâches et terminer la commande.

## Remarques

-   Dans certains cas, cette commande produira un maillage avec des normales inversées. La commande [Mesh Inverser les normales](Mesh_FlipNormals/fr.md) peut être utilisée pour corriger cela.

## Propriétés

Voir: [Mesh Feature](Mesh_Feature/fr.md).





{{Mesh Tools navi

}}  

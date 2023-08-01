---
- GuiCommand:
   Name:Mesh RemeshGmsh
   Name/fr:Mesh Affiner
   MenuLocation:Maillages - Affiner...
   Workbenches:[Mesh](Mesh_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Mesh Créer un maillage](Mesh_FromPartShape/fr.md)
---

# Mesh RemeshGmsh/fr

## Description

La commande **Affiner** remaille un objet maillé en utilisant le mailleur [Gmsh](https://gmsh.info/). Le nouveau maillage peut être plus fin ou plus grossier.



## Utilisation

1.  Sélectionnez un seul objet maillé.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_RemeshGmsh.svg" width=16px> [Affiner...](Mesh_RemeshGmsh/fr.md)
**
    -   Sélectionnez l\'option **Maillages → <img src="images/Mesh_RemeshGmsh.svg" width=16px> Affiner...** du menu.
3.  Le panneau des tâches **Remaillage par Gmsh** s\'ouvre.
4.  Spécifiez les paramètres requis. Voir la [configuration du mailleur Gmsh](Mesh_FromPartShape/fr#Mailleur_Gmsh.md) de la commande [Mesh Créer un maillage](Mesh_FromPartShape/fr.md).
5.  Appuyez sur le bouton **Appliquer** pour remailler l\'objet maillé.
6.  Modifiez un ou plusieurs paramètres et appuyez à nouveau sur le bouton **Appliquer** jusqu\'à ce que le nouveau maillage vous convienne.
7.  Appuyez sur le bouton **Fermer** pour fermer le panneau des tâches et terminer la commande.



## Remarques

-   Dans certains cas, cette commande produira un maillage avec des normales inversées. La commande [Mesh Inverser les normales](Mesh_FlipNormals/fr.md) peut être utilisée pour corriger cela.



## Propriétés

Voir : [Mesh Feature](Mesh_Feature/fr.md).





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh RemeshGmsh/fr

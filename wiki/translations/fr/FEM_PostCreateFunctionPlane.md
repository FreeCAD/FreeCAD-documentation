---
- GuiCommand:
   Name: FEM PostCreateFunctionPlane
   Name/fr: FEM Filtre fonction plan
   MenuLocation: Résultats -> Fonctions de filtrage -> Plan
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
---

# FEM PostCreateFunctionPlane/fr

## Description

La fonction <img alt="" src=images/FEM_PostCreateFunctionPlane.svg  style="width:24px;"> **FEM Filtre fonction plan** définit la façon dont un maillage est coupé géométriquement. Elle est utilisée par <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Filtre de découpe selon une fonction](FEM_PostFilterCutFunction/fr.md) et <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Filtre d\'écrêtage selon une région](FEM_PostFilterClipRegion/fr.md).



## Utilisation



### Créer une fonction plan 

1.  Soit vous appuyez sur le bouton **<img src="images/FEM_PostCreateFunctionPlane.svg" width=16px> [Plan](FEM_PostCreateFunctionPlane/fr.md)** soit vous sélectionnez l\'option **Résultats → Fonctions de filtrage → <img src="images/FEM_PostCreateFunctionPlane.svg" width=16px> Plan** du menu.
2.  Le [panneau des tâches](Task_panel/fr.md) de la fonction Implicit s\'ouvre.
3.  Vous pouvez définir les valeurs de l\'origine et de la direction du plan de coupe.
4.  Appuyez sur le bouton **OK** pour terminer.



### Modifier une fonction plan 

Si l\'objet Plan dans la [vue 3D](3D_view/fr.md) est caché, sélectionnez l\'objet <img alt="" src=images/FEM_PostCreateFunctionPlane.svg  style="width:24px;"> Plan dans la [vue en arborescence](Tree_view/fr.md) et appuyez sur **Espace** pour le rendre visible, comme dans cet exemple :

<img alt="" src=images/FEM_Plane-Cut-Function-Example.png  style="width:300px;">



#### Déplacer le plan 

-   Cliquez et faites glisser le gros cube blanc pour déplacer le plan le long de son vecteur normal.
-   Cliquez et faites glisser la grille blanche.



#### Rotation et inclinaison du plan 

-   Cliquez et faites glisser une ligne qui relie les petits cubes au grand cube blanc pour faire tourner et incliner le plan autour de son origine.



#### Mise à l\'échelle du plan 

-   Cliquez sur l\'un des 6 petits cubes et faites-le glisser pour mettre le plan à l\'échelle. Cependant, comme l\'objet est un plan infini, la taille n\'a pas d\'importance.



## Remarques

-   Les fonctions existantes peuvent être utilisées pour différents filtres et même pour différents <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [pipelines de résultats](FEM_PostPipelineFromResult/fr.md). Il est néanmoins recommandé d\'utiliser un ensemble de fonctions distinct pour chaque pipeline afin de garder la trace des éléments dans la [Vue en arborescence](Tree_view/fr.md).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionPlane/fr

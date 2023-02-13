---
- GuiCommand:/fr
   Name:FEM PostCreateFunctionPlane
   Name/fr:FEM Filtre fonction plan
   Icon:Fem-post-geo-plane.svg
   MenuLocation:Résultats → Fonctions de filtrage → Plan
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM PostCreateFunctionPlane/fr


</div>

## Description


<div class="mw-translate-fuzzy">

La fonction <img alt="" src=images/Fem-post-geo-plane.svg  style="width:24px;"> **FEM Filtre fonction plan** définit la façon dont un maillage est coupé géométriquement. Elle est utilisée par <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Filtre de découpe selon une fonction](FEM_PostFilterCutFunction/fr.md) et <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Filtre d\'écrêtage selon une région](FEM_PostFilterClipRegion/fr.md).


</div>



## Utilisation



### Créer une fonction plan 


<div class="mw-translate-fuzzy">

1.  Il y a plusieurs façons de créer une fonction :
    -   Appuyez sur le bouton **<img src="images/Fem-post-geo-plane.svg" width=16px> [Plan](FEM_PostCreateFunctionPlane/fr.md)**.
    -   Sélectionnez l\'option **Résultats → Fonctions de filtrage → <img src="images/Fem-post-geo-plane.svg" width=16px> Plan** dans le menu.
2.  La fonction Implicit [Panneau des tâches](Task_panel/fr.md) s\'ouvre.
3.  Définissez les valeurs de l\'origine et de la direction du plan de coupe.
4.  Appuyez sur le bouton **OK** pour terminer.


</div>



### Modifier une fonction plan 


<div class="mw-translate-fuzzy">

Si l\'objet Plan dans la [Vue 3D](3D_view/fr.md) est caché, sélectionnez l\'objet <img alt="" src=images/Fem-post-geo-plane.svg  style="width:24px;"> Plan dans la [Vue en arborescence](Tree_view/fr.md) et appuyez sur **Espace** pour le rendre visible, comme dans cet exemple :


</div>

<img alt="" src=images/FEM_Plane-Cut-Function-Example.png  style="width:300px;">



#### Déplacer le plan 

-   Cliquez et faites glisser le gros cube blanc pour déplacer le plan le long de son vecteur normal.
-   Cliquez et faites glisser la grille blanche.



#### Rotation et inclinaison du plan 

-   Cliquez et faites glisser une ligne qui relie les petits cubes au grand cube blanc pour faire tourner et incliner le plan autour de son origine.



#### Mise à l\'échelle du plan 

-   Cliquez et faites glisser l\'un des 6 petits cubes sont des poignées pour ajuster la taille à l\'échelle du plan. Cependant, comme l\'objet est un plan infini, la taille n\'a pas d\'importance.



## Remarques

-   Les fonctions existantes peuvent être utilisées pour différents filtres et même pour différents <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [pipelines de résultats](FEM_PostPipelineFromResult/fr.md). Il est néanmoins recommandé d\'utiliser un ensemble de fonctions distinct pour chaque pipeline afin de garder la trace des éléments dans la [Vue en arborescence](Tree_view/fr.md).


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionPlane/fr

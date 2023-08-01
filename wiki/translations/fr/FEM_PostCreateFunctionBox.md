---
- GuiCommand:/fr
   Name:FEM PostCreateFunctionBox
   Name/fr:FEM Filtre fonction boîte
   MenuLocation:Résultats → Fonctions de filtrage → Boîte
   Workbenches:[FEM](FEM_Workbench/fr.md)
   Version:0.21
   SeeAlso:[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM PostCreateFunctionBox/fr

## Description

La fonction <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:24px;"> **FEM Filtre fonction boîte** définit la façon dont un maillage est coupé géométriquement. Elle est utilisée par <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Filtre de découpe selon une fonction](FEM_PostFilterCutFunction/fr.md) et <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Filtre d\'écrêtage selon une région](FEM_PostFilterClipRegion/fr.md).



## Utilisation



### Créer une fonction boîte 

1.  Soit vous appuyez sur le bouton **<img src="images/FEM_PostCreateFunctionBox.svg" width=16px> [Boîte](FEM_PostCreateFunctionBox/fr.md)** soit vous sélectionnez l\'option **Résultats → Fonctions de filtrage → <img src="images/FEM_PostCreateFunctionBox.svg" width=16px> Boîte** du menu.
2.  Le [panneau des tâches](Task_panel/fr.md) de la fonction Implicit s\'ouvre.
3.  Vous pouvez définir les valeurs de l\'origine et de la direction du plan de coupe.
4.  Appuyez sur le bouton **OK** pour terminer.



### Modifier une fonction boîte 

Si l\'objet Box dans la [vue en arborescence](Tree_view/fr.md) est caché, sélectionnez l\'objet <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:24px;"> Box dans la [vue 3D](3D_view/fr.md) et appuyez sur **Espace** pour le rendre visible, comme dans cet exemple :

<img alt="" src=images/FEM_Box-Cut-Function-Example.png  style="width:400px;">



#### Déplacer la boîte 

-   Cliquez et faites glisser une face de la boîte. La boîte est définie par des bords bleus.



#### Rotation et inclinaison de la boîte 

-   Cliquez et faites glisser l\'une des 3 lignes qui traversent la boîte pour la faire pivoter et l\'incliner autour de son point d\'origine.



#### Mise à l\'échelle de la boîte 

-   Cliquez et faites glisser l\'un des 8 petits cubes situés dans les coins de la boîte pour la mettre à l\'échelle.



#### Transformer la boîte 

-   Cliquez et faites glisser l\'un des 6 petits cubes autour du centre de la boîte pour en modifier la forme.



## Remarques

-   Les fonctions existantes peuvent être utilisées pour différents filtres et même pour différents <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [pipelines de résultats](FEM_PostPipelineFromResult/fr.md). Il est néanmoins recommandé d\'utiliser un ensemble de fonctions distinct pour chaque pipeline afin de garder la trace des éléments dans la [Vue en arborescence](Tree_view/fr.md).





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionBox/fr

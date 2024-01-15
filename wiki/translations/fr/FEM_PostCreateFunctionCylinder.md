---
 GuiCommand:
   Name: FEM PostCreateFunctionCylinder
   Name/fr: FEM Filtre fonction cylindre
   MenuLocation: Résultats , Fonctions de filtrage , Cylindre
   Workbenches: FEM_Workbench/fr
   Version: 0.21
   SeeAlso: FEM_tutorial/fr
---

# FEM PostCreateFunctionCylinder/fr

## Description

La fonction <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:24px;"> **FEM Filtre fonction cylindre** définit la façon dont un maillage est coupé géométriquement. Elle est utilisée par <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Filtre de découpe selon une fonction](FEM_PostFilterCutFunction/fr.md) et <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Filtre d\'écrêtage selon une région](FEM_PostFilterClipRegion/fr.md).



## Utilisation



### Créer une fonction cylindre 

1.  Appuyer soit sur le bouton **<img src="images/FEM_PostCreateFunctionCylinder.svg" width=16px> [Cylindre](FEM_PostCreateFunctionCylinder/fr.md)** soit sélectionner l\'option **Résultats → Fonctions de filtrage → <img src="images/FEM_PostCreateFunctionCylinder.svg" width=16px> Cylindre** du menu.
2.  Le [panneau des tâches](Task_panel/fr.md) de la fonction Implicit s\'ouvre.
3.  Vous pouvez définir les valeurs de l\'origine et de la direction du plan de coupe.
4.  Appuyer sur le bouton **OK** pour terminer.



### Modifier une fonction cylindre 

Si l\'objet Cylinder dans la [vue en arborescence](Tree_view/fr.md) est caché, sélectionnez l\'objet <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:24px;"> Cylinder dans la [vue 3D](3D_view/fr.md) et appuyez sur **Espace** pour le rendre visible, comme dans cet exemple :

<img alt="" src=images/FEM_Cylinder-Cut-Function-Example.png  style="width:400px;">



#### Déplacer le cylindre 

-   Cliquez et faites glisser le gros cube blanc pour déplacer le cylindre le long de son vecteur normal.
-   Cliquez et faites glisser la grille blanche.



#### Rotation et inclinaison du cylindre 

-   Cliquez et faites glisser une ligne qui relie les petits cubes au grand cube blanc pour faire tourner et incliner le cylindre autour de son origine.



#### Mise à l\'échelle du cylindre 

-   Cliquez et faites glisser l\'un des 6 petits cubes pour mettre le cylindre à l\'échelle.



## Remarques

-   Les fonctions existantes peuvent être utilisées pour différents filtres et même pour différents <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [pipelines de résultats](FEM_PostPipelineFromResult/fr.md). Il est néanmoins recommandé d\'utiliser un ensemble de fonctions distinct pour chaque pipeline afin de garder la trace des éléments dans la [Vue en arborescence](Tree_view/fr.md).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionCylinder/fr

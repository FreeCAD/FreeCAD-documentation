---
- GuiCommand:
   Name: FEM PostCreateFunctionSphere
   Name/fr: FEM Filtre fonction sphère
   MenuLocation: Résultats -> Fonctions de filtrage -> Sphère
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
---

# FEM PostCreateFunctionSphere/fr

## Description

La fonction <img alt="" src=images/FEM_PostCreateFunctionSphere.svg  style="width:24px;"> **FEM Filtre fonction sphère** définit la façon dont un maillage est coupé géométriquement. Elle est utilisée par <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Filtre de découpe selon une fonction](FEM_PostFilterCutFunction/fr.md) et <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Filtre d\'écrêtage selon une région](FEM_PostFilterClipRegion/fr.md).



## Utilisation



### Créer une fonction sphère 

1.  Soit vous appuyez sur le bouton **<img src="images/FEM_PostCreateFunctionSphere.svg" width=16px> [Sphère](FEM_PostCreateFunctionSphere/fr.md)** soit vous sélectionnez l\'option **Résultats → Fonctions de filtrage → <img src="images/FEM_PostCreateFunctionSphere.svg" width=16px> Sphère** du menu.
2.  Le [panneau des tâches](Task_panel/fr.md) de la fonction Implicit s\'ouvre.
3.  Vous pouvez définir les valeurs de l\'origine et du rayon de la sphère de section.
4.  Appuyez sur le bouton **OK** pour terminer.



### Modifier une fonction sphère 

Si l\'objet Sphere dans la [vue en arborescence](Tree_view/fr.md) est caché, sélectionnez l\'objet <img alt="" src=images/FEM_PostCreateFunctionSphere.svg  style="width:24px;"> Sphere dans la [vue 3D](3D_view/fr.md) et appuyez sur **Espace** pour le rendre visible, comme dans cet exemple :

<img alt="" src=images/FEM_Sphere-Cut-Function-Example.png  style="width:400px;">



#### Déplacer la sphère 

-   Cliquez et faites glisser la grille sphérique pour déplacer la sphère.



#### Mise à l\'échelle de la sphère 

-   Cliquez et faites glisser l\'un des 8 petits cubes pour mettre la sphère à l\'échelle.



## Remarques

-   Les fonctions existantes peuvent être utilisées pour différents filtres et même pour différents <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [pipelines de résultats](FEM_PostPipelineFromResult/fr.md). Il est néanmoins recommandé d\'utiliser un ensemble de fonctions distinct pour chaque pipeline afin de garder la trace des éléments dans la [vue en arborescence](Tree_view/fr.md).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionSphere/fr

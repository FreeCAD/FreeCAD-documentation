---
- GuiCommand:/fr
   Name:FEM PostCreateFunctionSphere
   Name/fr:FEM Filtre fonction sphère
   Icon:Fem-post-geo-sphere.svg
   MenuLocation:Résultats → Fonctions de filtrage → Sphère
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM PostCreateFunctionSphere/fr


</div>

## Description


<div class="mw-translate-fuzzy">

La fonction <img alt="" src=images/Fem-post-geo-sphere.svg  style="width:24px;"> **FEM Filtre fonction sphère** définit la façon dont un maillage est coupé géométriquement. Elle est utilisée par <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:16px;"> [Filtre de découpe selon une fonction](FEM_PostFilterCutFunction/fr.md) et <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:16px;"> [Filtre d\'écrêtage selon une région](FEM_PostFilterClipRegion/fr.md).


</div>



## Utilisation



### Créer une fonction sphère 


<div class="mw-translate-fuzzy">

1.  Il y a plusieurs façons de créer une fonction :
    -   Appuyez sur le bouton **<img src="images/Fem-post-geo-sphere.svg" width=16px> [Sphère](FEM_PostCreateFunctionSphere/fr.md)**.
    -   Sélectionnez l\'option **Résultats → Fonctions de filtrage → <img src="images/Fem-post-geo-plane.svg" width=16px> Sphère** dans le menu.
2.  La fonction Implicit [Panneau des tâches](Task_panel/fr.md) s\'ouvre.
3.  Définissez les valeurs de l\'origine et du rayon de la sphère de section.
4.  Appuyez sur le bouton **OK** pour terminer.


</div>



### Modifier une fonction sphère 


<div class="mw-translate-fuzzy">

Si l\'objet Sphere dans la [Vue en arborescence](Tree_view/fr.md) est caché, sélectionnez l\'objet <img alt="" src=images/Fem-post-geo-sphere.svg  style="width:24px;"> Sphere dans la [Vue 3D](3D_view/fr.md) et appuyez sur **Espace** pour le rendre visible, comme dans cet exemple :


</div>

<img alt="" src=images/FEM_Sphere-Cut-Function-Example.png  style="width:400px;">



#### Déplacer la sphère 

-   Cliquez et faites glisser la grille sphérique pour déplacer la sphère.



#### Mise à l\'échelle de la sphère 

-   Cliquez et faites glisser l\'un des 8 petits cubes autour de la grille sphérique pour ajuster la taille de la sphère.



## Remarques

-   Les fonctions existantes peuvent être utilisées pour différents filtres et même pour différents <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:16px;"> [pipelines de résultats](FEM_PostPipelineFromResult/fr.md). Il est néanmoins recommandé d\'utiliser un ensemble de fonctions distinct pour chaque pipeline afin de garder la trace des éléments dans la [vue en arborescence](Tree_view/fr.md).


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctionSphere/fr

---
- GuiCommand   */fr
   Name   *FEM CompPostCreateFunctions
   Name/fr   *FEM Fonctions de filtrage
   MenuLocation   *Résultats → Fonctions de filtrage
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   SeeAlso   *[Tutoriel FEM](FEM_tutorial/fr.md)
---

# FEM PostCreateFunctions/fr

## Description

**FEM Fonctions de filtrage** est un bouton icône dans la barre d\'outils des résultats de FEM qui regroupe les outils permettant de créer des fonctions pour les filtres de résultats <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width   *16px;"> [Filtre de découpe selon une fonction](FEM_PostFilterCutFunction/fr.md) et <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width   *16px;"> [Filtre d\'écrêtage selon une région](FEM_PostFilterClipRegion/fr.md). Ils définissent comment le maillage est coupé géométriquement. Cliquez sur la flèche vers le bas à sa droite pour développer les icônes situées en dessous et sélectionner un outil.

## Types

Pour le moment, vous pouvez choisir entre deux fonctions géométriques    *

-   <img alt="" src=images/Fem-post-geo-plane.svg  style="width   *32px;"> [FEM Plan](FEM_PostCreateFunctionPlane/fr.md)
-   <img alt="" src=images/Fem-post-geo-sphere.svg  style="width   *32px;"> [FEM Sphère](FEM_PostCreateFunctionSphere/fr.md)

## Utilisation

Pour créer une fonction, utilisez le bouton de la barre d\'outils <img alt="" src=images/Fem-post-geo-plane.svg  style="width   *32px;"> ou <img alt="" src=images/Fem-post-geo-sphere.svg  style="width   *32px;"> (selon ce qui est visible). Notez le petit triangle à côté qui vous permet de choisir le type de fonction. Vous pouvez également utiliser le menu **Résultats → Fonctions de filtrage → <img src="images/Fem-post-geo-plane.svg" width=16px> Plan / <img src="images/Fem-post-geo-sphere.svg" width=16px> Sphère**.

Pour modifier une fonction, voir les sections ci-dessous.

Les fonctions existantes peuvent être utilisées pour différents filtres et même pour différents [pipelines de résultats](FEM_PostPipelineFromResult/fr.md). Il est néanmoins recommandé d\'utiliser pour chaque pipeline son propre ensemble de fonctions afin de garder la vue d\'ensemble dans la [vue en arborescence](Tree_view/fr.md).

### Plan

Les plans apparaissent dans la vue en arborescence avec l\'icône <img alt="" src=images/Fem-post-geo-plane.svg  style="width   *32px;">. Lorsqu\'ils sont rendus visibles dans la vue en arborescence, ils ressemblent à ceci    *

<img alt="" src=images/FEM_Plane-Cut-Function-Example.png  style="width   *400px;">

Pour déplacer le plan, cliquez sur le gros cube blanc qui est perpendiculaire au plan et maintenez le bouton de la souris enfoncé pendant le déplacement de la souris. Ou cliquez sur la grille blanche et maintenez le bouton de la souris enfoncé pendant le déplacement de la souris.

Pour faire pivoter et incliner le plan, cliquez sur une ligne qui relie les petits cubes au grand cube blanc et maintenez le bouton de la souris enfoncé pendant le déplacement de la souris.

Les 6 petits cubes sont des poignées pour ajuster la taille. Cependant, comme l\'objet est un plan infini, la taille n\'a pas d\'importance.

### Sphère

Les sphères apparaissent dans la vue en arborescence avec l\'icône <img alt="" src=images/Fem-post-geo-sphere.svg  style="width   *32px;">. Lorsqu\'elles sont rendues visibles dans la vue en arborescence, elles ressemblent à ceci    *

<img alt="" src=images/FEM_Sphere-Cut-Function-Example.png  style="width   *400px;">

Les 8 petits cubes autour de la grille sphérique sont des poignées pour ajuster la taille de la sphère. Pour les utiliser, cliquez sur un cube et maintenez le bouton de la souris enfoncé pendant le déplacement de la souris.

Pour déplacer la position de la sphère, cliquez sur la grille sphérique et maintenez le bouton de la souris enfoncé pendant le déplacement de la souris.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostCreateFunctions/fr

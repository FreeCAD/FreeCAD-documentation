---
- GuiCommand   */fr
   Name   *FEM ClippingPlaneAdd
   Name/fr   *FEM Plan de coupe
   MenuLocation   *Utilitaires → Plan de coupe
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   SeeAlso   *[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM ClippingPlaneAdd/fr

## Description

Ajoute un plan de coupe pour l\'ensemble de la vue du modèle. Tous les objets visibles seront coupés par ce plan, qu\'il s\'agisse de modèles géométriques, de maillages ou de pipelines de résultats.

Le plan de coupe est le même que celui que vous obtenez en utilisant la fonction [Std Basculer le plan de coupe](Std_ToggleClipPlane/fr.md), à la différence que le plan de coupe est persistant. Il partage donc la même fonctionnalité qui consiste à ne fournir que des coupes creuses.

## Utilisation

Pour créer un plan de coupe, utilisez le bouton de la barre d\'outils **<img src="images/FEM_ClippingPlaneAdd.svg" width=16px> '''Plan de coupe'''** ou le menu **Utilitaires → <img src="images/FEM_ClippingPlaneAdd.svg" width=16px> Plan de coupe**. Il est possible d\'avoir plusieurs plans de coupes.

Bien que le plan soit persistant, il n\'apparaîtra pas dans la [vue en arborescence](Tree_view/fr.md). Le plan apparaît dans la vue du modèle comme ceci    *

<img alt="" src=images/FEM_Clipping-Plane-Example.png  style="width   *400px;">

Pour déplacer le plan, cliquez sur le gros cube blanc qui est perpendiculaire au plan et maintenez le bouton de la souris enfoncé pendant le déplacement de la souris.

Pour faire pivoter et incliner le plan, cliquez sur une ligne qui relie les petits cubes au grand cube blanc et maintenez le bouton de la souris enfoncé pendant le déplacement de la souris.

Les 6 petits cubes sont des poignées pour ajuster la taille. Cependant, comme l\'objet est un plan infini, la taille n\'a pas d\'importance.

Pour supprimer tous les plans de coupe, utilisez la fonction [Supprimer les plans de coupe](FEM_ClippingPlaneRemoveAll/fr.md). La suppression d\'un seul plan n\'est pas possible.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ClippingPlaneAdd/fr

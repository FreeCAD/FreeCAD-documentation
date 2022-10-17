---
- GuiCommand   */fr
   Name   *FEM ConstraintInitialFlowVelocity
   Name/fr   *FEM Contrainte de vitesse initiale d'écoulement
   MenuLocation   *Modèle → Contraintes du fluide → Contrainte de vitesse initiale d'écoulement
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   SeeAlso   *[FEM Contrainte de vitesse d'écoulement](FEM_ConstraintFlowVelocity/fr.md), [FEM Contrainte de pression initiale](FEM_ConstraintInitialPressure/fr.md)
---

# FEM ConstraintInitialFlowVelocity/fr

## Description

Crée une contrainte de vitesse initiale d\'écoulement pour une analyse d\'écoulement de fluide.

## Utilisation

1.  Vous pouvez soit appuyer sur le bouton de la barre d\'outils **<img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> '''Contrainte de vitesse initiale d'écoulement'''** soit sélectionner le menu **Modèle → Contraintes du fluide → <img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> Contrainte de vitesse initiale d'écoulement**.
2.  Saisissez une valeur de vitesse d\'écoulement initiale pour l\'analyse. La valeur est entrée comme une combinaison des 3 composantes principales des vecteurs cartésiens (X,Y,Z).
3.  Pour une analyse 3D, sélectionnez un \"solide\" (corps) de votre modèle. Pour une analyse 2D, sélectionnez une face.

## Limitation

-   La contrainte ne peut pas être orientée autrement qu\'en utilisant les composantes cartésiennes principales. Il s\'agit d\'une limitation d\'Elmer.

## Remarques

Dans les analyses les plus simples, il n\'est pas nécessaire de spécifier la vitesse d\'écoulement initiale, mais cela est recommandé comme une bonne pratique.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialFlowVelocity/fr

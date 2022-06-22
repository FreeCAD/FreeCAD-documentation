---
- GuiCommand   */fr
   Name   *FEM ConstraintInitialFlowVelocity
   Name/fr   *FEM Contrainte de vitesse d'écoulement initiale
   MenuLocation   *Modèle → Contraintes du fluide → Contrainte de vitesse initiale d'écoulement
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   SeeAlso   *[FEM Contrainte de vitesse d'écoulement](FEM_ConstraintFlowVelocity/fr.md)
---

# FEM ConstraintInitialFlowVelocity/fr

## Description

Crée une contrainte de vitesse initiale d\'écoulement pour une analyse d\'écoulement de fluide.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande   *
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> [Contrainte de vitesse initiale d'écoulement](FEM_ConstraintInitialFlowVelocity/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Contraintes du fluide → <img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> Contrainte de vitesse initiale d'écoulement** dans le menu.
2.  Entrez une valeur de vitesse initiale d\'écoulement pour l\'analyse.
3.  La valeur est entrée comme une combinaison des 3 principales composantes des vecteurs cartésiens (X, Y, Z).

## Limitations

-   La contrainte applique la vitesse initiale d\'écoulement à tous les nœuds du modèle FEA.
-   La contrainte ne peut pas être orientée autrement qu\'en utilisant les principaux composants cartésiens.

## Remarques

Dans les analyses les plus simples, il n\'est pas nécessaire de spécifier la vitesse d\'écoulement initiale, mais cela est recommandé comme une bonne pratique.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialFlowVelocity/fr

---
- GuiCommand:/fr
   Name:FEM ConstraintInitialFlowVelocity
   Name/fr:FEM Contrainte vitesse d'écoulement initiale
   MenuLocation:Model → Fluid Constraints → Constraint initial flow velocity
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[FEM Contrainte de vitesse d'écoulement](FEM_ConstraintFlowVelocity/fr.md)
---

# FEM ConstraintInitialFlowVelocity/fr

## Description

Applique une condition aux limites de vitesse d\'écoulement à une face en 3D ou à une arête en 2D.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> [Créer une contrainte FEM une vitesse initiale d'écoulement](FEM_ConstraintInitialFlowVelocity/fr.md)**.
    -   Sélectionnez l\'option **Model → Fluid Constraints → <img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> Contrainte vitesse initiale d'écoulement** dans le menu.
2.  Entrez une valeur de vitesse d\'écoulement initiale pour l\'analyse.
3.  La valeur est entrée comme une combinaison des 3 principales composantes des vecteurs cartésiens (X, Y, Z).

## Limitations

-   La contrainte applique la vitesse d\'écoulement initiale à tous les nœuds du modèle FEA.
-   La contrainte ne peut pas être orientée autrement qu\'en utilisant les principaux composants cartésiens.

## Remarques

Dans les analyses les plus simples, il n\'est pas nécessaire de spécifier la vitesse d\'écoulement initiale mais elle est recommandée comme meilleure pratique.





{{FEM Tools navi

}}

---
[documentation index](../README.md) > FEM ConstraintInitialFlowVelocity/fr

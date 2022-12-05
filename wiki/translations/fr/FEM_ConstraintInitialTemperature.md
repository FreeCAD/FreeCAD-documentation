---
- GuiCommand:/fr
   Name:FEM ConstraintInitialTemperature
   Name/fr:FEM Contrainte de température initiale
   MenuLocation:Modèle → Contraintes thermiques → Contrainte de température initiale
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM ConstraintInitialTemperature/fr

## Description

Crée une contrainte de température initiale pour une analyse thermo-mécanique.

## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintInitialTemperature.svg" width=16px> [Contrainte de température initiale](FEM_ConstraintInitialTemperature/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Contraintes thermiques → <img src="images/FEM_ConstraintInitialTemperature.svg" width=16px> Contrainte de température initiale** dans le menu.
2.  Entrez une valeur de température initiale pour l\'analyse.

## Limitations

Cette contrainte applique la température initiale à tous les nœuds du modèle FEA - il n\'est pas possible de sélectionner des régions individuellement.

## Remarques

-   Cette contrainte utilise la carte \*INITIAL CONDITIONS de CalculiX. La contrainte de température initiale est expliquée à l\'adresse <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node215.html>.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialTemperature/fr

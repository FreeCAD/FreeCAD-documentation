---
- GuiCommand:/fr
   Name:FEM ConstraintInitialTemperature
   Name/fr:FEM Contrainte température initiale
   MenuLocation:Model → Thermal Constraints → Constraint initial temperature
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[Tutoriel FEM](FEM_tutorial/fr.md)
---

# FEM ConstraintInitialTemperature/fr

## Description

Crée une contrainte de température initiale pour une analyse thermo-mécanique.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintInitialTemperature.svg" width=16px> [Creates a FEM constraint for initial temperature...](FEM_ConstraintInitialTemperature/fr.md)**.
    -   Sélectionnez l\'option **Model → Thermal Constraints → <img src="images/FEM_ConstraintInitialTemperature.svg" width=16px> Constraint initial temperature** dans le menu.
2.  Entrez une valeur de température initiale pour l\'analyse.

## Limitations

La contrainte applique la température initiale à tous les nœuds du modèle FEA.

## Remarques

1.  La contrainte utilise \*\*INITIAL CONDITIONS de la carte dans CalculiX. La contrainte temperature initial est expliquée à <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node215.html>





{{FEM Tools navi

}}

---
[documentation index](../README.md) > FEM ConstraintInitialTemperature/fr

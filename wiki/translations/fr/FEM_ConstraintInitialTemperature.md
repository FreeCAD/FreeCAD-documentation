---
 GuiCommand:
   Name: FEM ConstraintInitialTemperature
   Name/fr: FEM Température initiale
   MenuLocation: Modèle , Conditions limites et charges thermiques , Température initiale
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
---

# FEM ConstraintInitialTemperature/fr

## Description

Définit une température initiale pour une analyse thermomécanique.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyer sur le bouton **<img src="images/FEM_ConstraintInitialTemperature.svg" width=16px> [Température initiale](FEM_ConstraintInitialTemperature/fr.md)**.
    -   Sélectionner l\'option **Modèle → Conditions limites et charges thermiques → <img src="images/FEM_ConstraintInitialTemperature.svg" width=16px> Température initiale** du menu.
2.  Entrer une valeur de température initiale pour l\'analyse.

## Limitations

Cet outil applique la température initiale à tous les nœuds du modèle FEA - il n\'est pas possible de sélectionner des régions individuellement.



## Remarques

-   Cet outil utilise le jeu de paramètres \*INITIAL CONDITIONS de CalculiX. Il est expliqué à l\'adresse <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node215.html>.
-   La température initiale doit être définie pour toutes les analyses thermomécaniques effectuées avec CalculiX, même celles en régime permanent.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialTemperature/fr

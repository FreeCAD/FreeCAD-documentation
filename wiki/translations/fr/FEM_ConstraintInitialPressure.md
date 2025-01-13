---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ConstraintInitialPressure
   Name/fr: FEM Pression initiale
   MenuLocation: Modèle , Conditions limites de fluide , Condition de pression initiale
   Workbenches: FEM_Workbench/fr
   Version: 0.21
   SeeAlso: FEM_ConstraintInitialFlowVelocity/fr
}}{{GuiCommandFemInfo/fr
   Solvers: Elmer
}}
---

# FEM ConstraintInitialPressure/fr

## Description

Crée une condition de pression initiale pour une analyse d\'écoulement de fluide.



## Utilisation

1.  Appuyer soit sur le bouton de la barre d\'outils **<img src="images/FEM_ConstraintInitialPressure.svg" width=16px> [Condition de pression initiale](FEM_ConstraintInitialPressure/fr.md)** soit sélectionner **Modèle → Conditions limites de fluide → Condition de pression initiale** du menu.
2.  Saisir une valeur de pression initiale.
3.  Pour une analyse 3D, sélectionner un \"solide\" (corps) de votre modèle. Pour une analyse 2D, sélectionner une face.



## Remarques

Pour des analyses simples, il n\'est pas nécessaire de spécifier la pression initiale, mais dans ces cas également, il est recommandé de le faire en tant que meilleure pratique.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialPressure/fr

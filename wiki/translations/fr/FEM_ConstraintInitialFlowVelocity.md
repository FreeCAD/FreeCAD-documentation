---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ConstraintInitialFlowVelocity
   Name/fr: FEM Vitesse initiale d'écoulement
   MenuLocation: Modèle , Conditions limites de fluide , Condition de vitesse d'écoulement initial
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_ConstraintFlowVelocity/fr, FEM_ConstraintInitialPressure/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: Elmer
}}
---

# FEM ConstraintInitialFlowVelocity/fr

## Description

Crée une condition de vitesse initiale d\'écoulement pour une analyse d\'écoulement de fluide.



## Utilisation

1.  Appuyer soit sur le bouton de la barre d\'outils **<img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> [Condition de vitesse d'écoulement initial](FEM_ConstraintInitialFlowVelocity/fr.md)** soit sélectionner **Modèle → Conditions limites de fluide → <img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> Condition de vitesse d'écoulement initial** du menu.
2.  Saisir une valeur de vitesse d\'écoulement initiale pour l\'analyse. La valeur est entrée comme une combinaison des 3 composantes principales des vecteurs cartésiens (X,Y,Z).
3.  Pour une analyse 3D, sélectionner un \"solide\" (corps) de votre modèle. Pour une analyse 2D, sélectionner une face. Toutefois, il est également possible de sélectionner une face (par exemple, l\'entrée d\'un tuyau) en 3D ou un bord en 2D.



## Formules

Pour une description de la saisie des formules, voir la section \"Formules\" de la page [Vitesse d\'écoulement comme condition limite](FEM_ConstraintFlowVelocity/fr#Formules.md).



## Remarques

Dans les analyses simples, il n\'est pas nécessaire de spécifier la vitesse d\'écoulement initiale, mais cela est recommandé comme une bonne pratique.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialFlowVelocity/fr

---
 GuiCommand:
   Name: FEM ConstraintInitialFlowVelocity
   Name/fr: FEM Contrainte de vitesse initiale d'écoulement
   MenuLocation: Modèle , Contraintes du fluide , Contrainte de vitesse initiale d'écoulement
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_ConstraintFlowVelocity/fr, FEM_ConstraintInitialPressure/fr
---

# FEM ConstraintInitialFlowVelocity/fr

## Description

Crée une contrainte de vitesse initiale d\'écoulement pour une analyse d\'écoulement de fluide.



## Utilisation

1.  Vous pouvez soit appuyer sur le bouton de la barre d\'outils **<img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> '''Contrainte de vitesse initiale d'écoulement'''** soit sélectionner le menu **Modèle → Contraintes du fluide → <img src="images/FEM_ConstraintInitialFlowVelocity.svg" width=16px> Contrainte de vitesse initiale d'écoulement**.
2.  Saisissez une valeur de vitesse d\'écoulement initiale pour l\'analyse. La valeur est entrée comme une combinaison des 3 composantes principales des vecteurs cartésiens (X,Y,Z).
3.  Pour une analyse 3D, sélectionnez un \"solide\" (corps) de votre modèle. Pour une analyse 2D, sélectionnez une face. Toutefois, il est également possible de sélectionner une face (par exemple, l\'entrée d\'un tuyau) en 3D ou un bord en 2D.



## Formules

Pour une description de la saisie des formules, voir la section \"Formules\" de la page [Contrainte de vitesse d\'écoulement](FEM_ConstraintFlowVelocity/fr#Formules.md).



## Remarques

Dans les analyses simples, il n\'est pas nécessaire de spécifier la vitesse d\'écoulement initiale, mais cela est recommandé comme une bonne pratique.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialFlowVelocity/fr

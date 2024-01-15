---
 GuiCommand:
   Name: FEM ConstraintElectrostaticPotential
   Name/fr: FEM Potentiel électrostatique
   MenuLocation: Modèle , Conditions limites électromagnétiques , Condition limite de potentiel électrostatique
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_Example_Capacitance_Two_Balls/fr, FEM_tutorial/fr
---

# FEM ConstraintElectrostaticPotential/fr



## Description

Crée une condition limite FEM pour le potentiel électrostatique. À utiliser avec les équations [électrostatiques](FEM_EquationElectrostatic/fr.md) ou de [force électrique](FEM_EquationElectricforce/fr.md).



## Utilisation

1.  Appuyez soit sur le bouton **<img src="images/FEM_ConstraintElectrostaticPotential.svg" width=16px> [Condition limite de potentiel électrostatique](FEM_ConstraintElectrostaticPotential/fr.md)** ou utilisez le menu **Modèle → Conditions limites électromagnétiques → <img src="images/FEM_ConstraintElectrostaticPotential.svg" width=16px> Condition limite de potentiel électrostatique**.
2.  Dans la [vue 3D](3D_view/fr.md), sélectionnez l\'objet auquel la condition limite doit être appliquée.
3.  Appuyez sur le bouton **Ajouter**.

## Options

La boîte de dialogue propose les paramètres suivants :

![](images/FEM_ElectrostaticPotential_dialog.png )

-   **Potentiel** : potentiel électrique en V.
-   *non spécifié* : pour déclarer le potentiel comme inconnu au solveur.
-   **Champ vectoriel** : pour permettre l\'entrée des composantes d\'un champ de vecteurs potentiels.
-   **x** : partie réelle/imaginaire du potentiel dans la direction des x en V.Pour les systèmes de coordonnées autres que cartésien 3D, ce sera la première coordonnée du système au lieu de x.
-   **y** : partie réelle/imaginaire du potentiel dans la direction des y dans V.Pour les systèmes de coordonnées autres que cartésien 3D, ce sera la deuxième coordonnée du système au lieu de y.
-   **z** : partie réelle/imaginaire du potentiel dans la direction des z dans V.Pour les systèmes de coordonnées autres que cartésien 3D, ce sera la troisième coordonnée du système au lieu de z. Si le système de coordonnées n\'a pas de troisième coordonnée, ce paramètre sera ignoré.
-   **Cases à cocher x, y, z** : pour déclarer le potentiel correspondant comme inconnu au solveur.
-   **Potentiel constant** : option pour définir un potentiel constant.
-   **Champ lointain/Infinité électrique** : option pour faire l\'approximation sphérique en sorte que le volume au-dessus de la face s\'étend à l\'infini.
-   **Calculer la force électrique** : option pour déclencher le calcul de la force électrique en utilisant en utilisant l\'[FEM Équation de force électrique](FEM_EquationElectricforce/fr.md).
-   **Capacité du corps :** nombre de corps (ou de faces) avec une capacité.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintElectrostaticPotential/fr

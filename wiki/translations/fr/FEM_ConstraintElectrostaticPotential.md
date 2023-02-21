---
- GuiCommand:/fr
   Name:FEM ConstraintElectrostaticPotential
   Name/fr:FEM Contrainte de potentiel électrostatique
   MenuLocation:Modèle → Contraintes électrostatiques → Contrainte de potentiel électrostatique
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[FEM Exemple calcul capacité de deux sphères](FEM_Example_Capacitance_Two_Balls/fr.md), [FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM ConstraintElectrostaticPotential/fr



## Description

Crée une contrainte FEM pour le potentiel électrostatique. A utiliser avec [FEM Equation électrostatique](FEM_EquationElectrostatic/fr.md) ou [FEM Équation force électrique](FEM_EquationElectricforce/fr.md).



## Utilisation

1.  Appuyez soit sur le bouton **<img src="images/FEM_ConstraintElectrostaticPotential.svg" width=16px> [Contrainte de potentiel électrostatique](FEM_ConstraintElectrostaticPotential/fr.md)** ou utilisez le menu **Modèle → Contraintes électrostatiques → <img src="images/FEM_ConstraintElectrostaticPotential.svg" width=16px> Contrainte de potentiel électrostatique**.
2.  Dans la [Vue 3D](3D_view/fr.md), sélectionnez l\'objet auquel la contrainte doit être appliquée.
3.  Appuyez sur le bouton **Ajouter**.

## Options

La boîte de dialogue propose les paramètres suivants :

![](images/FEM_ElectrostaticPotential_dialog.png )

-   **Potentiel** : potentiel électrique en V.
-   **non spécifié** : pour déclarer le potentiel comme inconnu au solveur.
-   **Champ vectoriel** : pour permettre l\'entrée des composantes d\'un champ de vecteurs potentiels.
-   **x** : partie réelle/imaginaire du potentiel dans la direction des x en V.Pour les systèmes de coordonnées autres que cartésien 3D, ce sera la première coordonnée du système au lieu de x.
-   **y** : partie réelle/imaginaire du potentiel dans la direction des y dans V.Pour les systèmes de coordonnées autres que cartésien 3D, ce sera la deuxième coordonnée du système au lieu de y.
-   **z** : partie réelle/imaginaire du potentiel dans la direction des z dans V.Pour les systèmes de coordonnées autres que cartésien 3D, ce sera la troisième coordonnée du système au lieu de z. Si le système de coordonnées n\'a pas de troisième coordonnée, ce paramètre sera ignoré.
-   **Cases à cocher x, y, z** : pour déclarer le potentiel correspondant comme inconnu au solveur.
-   **Potentiel constant** : option pour définir un potentiel constant.
-   **Champ lointain/Infinité électrique** : Option pour faire l\'approximation sphérique que le volume au-dessus de la face s\'étend à l\'infini.
-   **Calculer la force électrique** : option pour déclencher le calcul de la force électrique en utilisant en utilisant l\'[FEM Équation de force électrique](FEM_EquationElectricforce/fr.md).
-   **Capacité du corps :** : compteur du corps (ou de la face) avec une capacité.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintElectrostaticPotential/fr

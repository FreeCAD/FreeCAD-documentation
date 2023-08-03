---
 GuiCommand:
   Name: FEM EquationFlow
   Name/fr: FEM Equation d'écoulement
   MenuLocation: Résolution , Équation d'écoulement
   Workbenches: FEM_Workbench/fr
   Version: 0.17
   SeeAlso: 
---

# FEM EquationFlow/fr

Cette équation calcule les mouvements de fluides visqueux à l\'aide des [équations de Navier-Stokes](https://fr.wikipedia.org/wiki/%C3%89quations_de_Navier-Stokes).

Pour plus d\'informations sur les mathématiques de l\'équation, voir [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Navier-Stokes Equations*.



## Utilisation

1.  Après avoir ajouté un solveur Elmer comme décrit [ici](FEM_SolverElmer/fr#.C3.89quations.md), sélectionnez-le dans la [Vue en arborescence](Tree_view/fr.md)
2.  Utilisez maintenant le bouton de la barre d\'outils <img alt="" src=images/FEM_EquationFlow.svg  style="width:24px;"> ou le menu **Résolution → Équation d'écoulement**.
3.  Modifiez les [paramètres du solveur de l\'équation](#Param.C3.A8tres_du_solveur.md) ou les [paramètres généraux du solveur](FEM_SolverElmer_SolverSettings/fr.md) si nécessaire.



## Paramètres du solveur 

Pour les paramètres généraux du solveur, voir les [paramètres du solveur Elmer](FEM_SolverElmer_SolverSettings/fr.md).

L\'équation d\'écoulement fournit ces paramètres spéciaux :

-    **Div Discretization**: défini à *true* pour un écoulement incompressible pour une discrétisation plus stable lorsque le [nombre de Reynolds](https://fr.wikipedia.org/wiki/Nombre_de_Reynolds) augmente.

-    **Flow Model**: modèle d\'écoulement à utilisé. La valeur par défaut *Full* inclut la convection et les termes de la dérivée temporelle dans le modèle. Le modèle *No convection* désactive les termes de convection et le modèle *Stokes* désactive les termes de convection et les termes de dérivée temporelle (explicite).

-    **Gradp Discretization**: si défini à *true*, les [conditions aux limites de Dirichlet](https://fr.wikipedia.org/wiki/Condition_aux_limites_de_Dirichlet) de la pression peuvent être utilisées. Le flux de masse est également disponible comme condition limite naturelle.

-    **Variable**: optionnel uniquement pour les calculs en 2D : vous pouvez changer la valeur par défaut de *3* à *2*.**Remarque** : dans ce cas, aucune des contraintes de vitesse d\'écoulement ne peut avoir une composante z spécifiée.

Équation :

-    **Convection**: type de convection à utiliser dans l\'<img alt="" src=images/FEM_EquationHeat.svg  style="width:24px;"> [équation de chaleur](FEM_EquationHeat/fr.md).**Remarque** : pour les écoulements thermiques, cette propriété doit être réglée à *Computed* (par défaut).

-    **Magnetic Induction**: si définie à *true*, l\'équation d\'induction magnétique sera résolue en même temps que les [Équations de Navier-Stokes](https://fr.wikipedia.org/wiki/%C3%89quations_de_Navier-Stokes).



### Remarques à propos de convergence 

Si les résultats du solveur ne convergent pas, vous pouvez essayer les choses suivantes (dans l\'ordre donné) :

1.  Réduire la valeur de **Relaxation Factor**, voir les [réglages de systèmes non linéaires](FEM_SolverElmer_SolverSettings/fr#Facteur_de_relaxation.md).
2.  Augmenter la valeur de **Nonlinear Newton After Iterations**, voir [réglages de systèmes non linéaires](FEM_SolverElmer_SolverSettings/fr#Système_non_linéaire.md).
3.  Réduire le nombre de cœurs CPU utilisés, voir les [FEM Préférences](FEM_Preferences/fr#Elmer.md).
4.  Augmenter la densité du maillage (le rendre plus fin).



## Informations sur les contraintes 

L\'équation électrostatique prend en compte les contraintes suivantes si elles sont définies :

-   <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:32px;"> [Contrainte de vitesse d\'écoulement](FEM_ConstraintFlowVelocity/fr.md)
-   <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:32px;"> [Contrainte de vitesse initiale d\'écoulement](FEM_ConstraintInitialFlowVelocity/fr.md)
-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Contrainte de pression](FEM_ConstraintPressure/fr.md)
-   <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:32px;"> [Contrainte de pression initiale](FEM_ConstraintInitialPressure/fr.md) ({{Version/fr|0.21}})



### Remarques

-   Sauf pour les calculs en 2D, pour toutes les contraintes ci-dessus, il est important qu\'elles agissent sur une face ou un corps. Les contraintes pour la 3D définies sur des lignes ou des sommets ne sont pas reconnues par le solveur Elmer.
-   Puisque la <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:24px;"> [Contrainte de pression](FEM_ConstraintPressure/fr.md) ne peut être définie que sur des faces, les contraintes de pression ne peuvent pas être utilisées pour les calculs en 2D.
-   S\'il n\'y a pas de <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:24px;"> [Contraintes de pression](FEM_ConstraintPressure/fr.md), la <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:24px;"> [Contrainte de pression initiale](FEM_ConstraintInitialPressure/fr.md) ne sera prise en compte que si **Gradp Discretization** est réglé sur *true*.



## Résultats

Les résultats sont la vitesse en $\rm m/s$ et la pression en $\rm Pa$. Si aucune valeur pour la <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:24px;"> [Contrainte de pression initiale](FEM_ConstraintInitialPressure/fr.md) et la <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:24px;"> [Contrainte de pression](FEM_ConstraintPressure/fr.md) n\'ait donnée, la pression résultante sera relative et non absolue. Comme une pression doit agir sur une face, les résultats de pression absolue ne peuvent pas être obtenus dans les simulations 2D.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationFlow/fr

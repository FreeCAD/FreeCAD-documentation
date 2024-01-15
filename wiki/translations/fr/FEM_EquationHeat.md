---
 GuiCommand:
   Name: FEM EquationHeat
   Name/fr: FEM Équation de chaleur
   MenuLocation: Résolution , Équation de chaleur
   Workbenches: FEM_Workbench/fr
   Version: 0.17
   SeeAlso: FEM_tutorial/fr
---

# FEM EquationHeat/fr

## Description

Cette équation décrit le transfert de chaleur dans les corps rigides et fluides.

Pour plus d\'informations sur les mathématiques de l\'équation, voir [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Heat Equation*.



## Utilisation

1.  Après avoir ajouté un solveur Elmer comme décrit [ici](FEM_SolverElmer/fr#.C3.89quations.md), sélectionnez-le dans la [vue en arborescence](Tree_view/fr.md)
2.  Utilisez maintenant le bouton de la barre d\'outils <img alt="" src=images/FEM_EquationHeat.svg  style="width:24px;"> ou le menu **Résolution → Equation de chaleur**.
3.  Modifiez les [paramètres du solveur de l\'équation](#Param.C3.A8tres_du_solveur.md) ou les [paramètres généraux du solveur](FEM_SolverElmer_SolverSettings/fr.md) si nécessaire.



## Paramètres du solveur 

Pour les paramètres généraux du solveur, voir les [paramètres du solveur Elmer](FEM_SolverElmer_SolverSettings/fr.md).

L\'équation de la chaleur fournit ces réglages spéciaux :

-    **Bubbles**: il existe également une formulation résiduelle sans bulles de la méthode des éléments finis stabilisés. Elle est plus précise et n\'inclut pas de termes ad hoc. Cependant, elle peut être plus coûteuse en termes de calcul. Si **Remarque** : si, au cours de la *première itération du solveur*, vous obtenez cette erreur : ERROR:: IterSolve: Numerical Error: System diverged over maximum tolerance.La méthode **Bubbles** a échoué. Dans ce cas, mettez **[Stabilize](FEM_SolverElmer_SolverSettings/fr#Base.md)** à *true*.

Equation :

-    **Convection**: type de convection à utiliser dans l\'équation de la chaleur.**Remarque** : si cette valeur n\'est pas mise à *None*, **[Stabilize](FEM_SolverElmer_SolverSettings/fr#Base.md)** doit être mise à *true* sinon le terme de convection ne sera pas considéré pour l\'équation de la chaleur.

-    **Phase Change Model**: modèle utilisé pour les changements de phase (de la glace à l\'eau, etc.). Le modèle *Spatial 1* est la méthode de capacité de chaleur apparente, *Spatial 2* et *Temporel* sont les méthodes de capacité de chaleur effective.Pour plus d\'informations sur les modèles, voir [ce papier](https://blog.rwth-aachen.de/gfd/files/2017/07/BT_2013_Schueller_elmer_icemole.pdf) (section 2.5.2.2) (en allemand). Dans l\'article, il est également montré que *Spatial 1* a des problèmes numériques sur des gradients de température plus importants et que *Spatial 2* est préférable pour le changement de phase de la glace à l\'eau.



## Informations sur les caractéristiques d\'analyse 

L\'équation de chaleur prend en compte les caractéristiques d\'analyse suivantes si elles sont activées :

-   <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:32px;"> [Source de chaleur du corps](FEM_ConstraintBodyHeatSource/fr.md)
-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Température initiale](FEM_ConstraintInitialTemperature/fr.md)
-   <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:32px;"> [Condition limite de température](FEM_ConstraintTemperature/fr.md)



### Remarque

À l\'exception des calculs en 2D, pour toutes les caractéristiques d\'analyse ci-dessus, il est important qu\'elles agissent sur une face ou un corps. Les fonctions en 3D définies sur des lignes ou des sommets ne sont pas reconnues par le solveur Elmer.



## Résultat

Le résultat est la température en Kelvin.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationHeat/fr

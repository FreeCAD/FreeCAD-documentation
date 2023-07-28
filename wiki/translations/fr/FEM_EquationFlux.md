---
- GuiCommand:/fr
   Name:FEM EquationFlux
   Name/fr:FEM Équation de flux
   MenuLocation:Résolution → Équation de flux
   Workbenches:[FEM](FEM_Workbench/fr.md)
   Version:0.17
   SeeAlso:
---

# FEM EquationFlux/fr

Cette équation est utilisée pour calculer les flux résultant généralement d\'équations de type Poisson. Il s\'agit notamment de l\'<img alt="" src=images/FEM_EquationHeat.svg  style="width:24px;"> [Equation de chaleur](FEM_EquationHeat/fr.md) et l\'<img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> [Equation électrostatique](FEM_EquationElectrostatic/fr.md).

Pour plus d\'informations sur les mathématiques de l\'équation, voir [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Flux Computation*.



## Utilisation

1.  Après avoir ajouté un solveur Elmer comme décrit [ici](FEM_SolverElmer/fr#.C3.89quations.md), sélectionnez-le dans la [vue en arborescence](Tree_view/fr.md)
2.  Utilisez le bouton de la barre d\'outils <img alt="" src=images/FEM_EquationFlux.svg  style="width:24px;"> ou le menu **Résolution → Equation de flux**.
3.  Ajoutez maintenant une équation de chaleur (bouton de la barre d\'outils <img alt="" src=images/FEM_EquationHeat.svg  style="width:24px;"> ou menu **Résolution → [Equation de chaleur](FEM_EquationHeat/fr.md)**) ou une équation électrostatique (bouton de la barre d\'outils <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> ou menu **Résolution → [Equation électrostatique](FEM_EquationElectrostatic/fr.md)**). Ceci est important car l\'équation de flux a besoin des contraintes définies pour ces équastions.
4.  Lorsque vous utilisez l\'équation électrostatique, changez la propriété **Flux Coefficient** en *None* et la propriété **Flux Variable** en *Potential*.
5.  Modifiez les [paramètres du solveur de l\'équation](#Param.C3.A8tres_du_solveur.md) ou les [paramètres généraux du solveur](FEM_SolverElmer_SolverSettings/fr.md) si nécessaire.



## Paramètres du solveur 

Pour les paramètres généraux du solveur, voir les [paramètres du solveur Elmer](FEM_SolverElmer_SolverSettings/fr.md).

L\'équation de flux fournit ces paramètres spéciaux :

-    **Average Within Materials**: si *true*, la continuité est appliquée au sein du même matériau dans la discrétisation de Galerkin discontinue en utilisant les termes de pénalité de la formulation de Galerkin discontinue.

-    **Calculate Flux**: calcule le vecteur flux.

-    **Calculate Flux Abs**: calcule la valeur absolue du vecteur flux. Nécessite que **Calculate Flux** soit vrai.

-    **Calculate Flux Magnitude**: calcule l\'amplitude du champ de vecteurs. Nécessite que En fait, c\'est la même chose que **Calculate Flux Abs** mais cela nécessite moins de mémoire car l\'équation matricielle n\'est résolue qu\'une seule fois. L\'inconvénient est que des valeurs négatives peuvent être introduites.

-    **Calculate Grad**: calcule le gradient du flux.

-    **Calculate Grad Abs**: calcule le gradient absolu du flux. Exige que **Calculate Grad** soit vrai.

-    **Calculate Grad Magnitude**: calcule l\'amplitude du champ de vecteurs. Nécessite que En fait, c\'est la même chose que **Calculate Grad Abs** mais cela nécessite moins de mémoire car l\'équation matricielle n\'est résolue qu\'une seule fois. L\'inconvénient est que des valeurs négatives peuvent être introduites.

-    **Discontinuous Galerkin**: pour les champs discontinus, l\'approximation Galerkin standard impose la continuité, ce qui peut ne pas être physique. Pour remédier à cela, définissez cette propriété sur *true*. Alors le résultat peut être discontinu et peut même être visualisé comme tel.

-    **Enforce Positive Magnitude**: si cette propriété est à *true*, les valeurs négatives des champs d\'amplitude calculés sont mises à zéro.

-    **Flux Coefficient**: nom du coefficient de proportionnalité pour calculer le flux.

-    **Flux Variable**: nom de la variable potentielle utilisée pour calculer le gradient.



## Informations sur les contraintes 

L\'équation de flux n\'a pas de contraintes propres. Elle prend les contraintes de l\'<img alt="" src=images/FEM_EquationHeat.svg  style="width:24px;"> [Equation de chaleur](FEM_EquationHeat/fr.md) ou de l\'<img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> [Equation électrostatique](FEM_EquationElectrostatic/fr.md).



## Résultats

Les résultats disponibles dépendent des [paramètres du solveur](#Param.C3.A8tres_du_solveur.md). Si aucun des paramètres de **Calculate *** n\'a été défini sur *true*, rien n\'est calculé. Sinon, les résultats correspondants seront également disponibles.

Le flux résultant est soit le flux de chaleur $\rm W/m^2$ (faussement appelé \"flux de température\"), soit le flux potentiel en $\rm W/m^2$ ($\rm A\cdot V/m^2$).





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationFlux/fr

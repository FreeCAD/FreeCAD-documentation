---
 GuiCommand:
   Name: FEM EquationElectricforce
   Name/fr: FEM Équation de force électrique
   MenuLocation: Résolution , Équations électromagnétiques , Équation de force électrique
   Workbenches: FEM_Workbench/fr
   Version: 0.19
   SeeAlso: FEM_EquationElectrostatic/fr
---

# FEM EquationElectricforce/fr

## Description

Cette équation décrit la force électrostatique agissant sur une surface.

Pour plus d\'informations sur les mathématiques de l\'équation, voir [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Electrostatic force*.



## Utilisation

1.  Après avoir ajouté un solveur Elmer comme décrit [ici](FEM_SolverElmer/fr#.C3.89quations.md), sélectionnez-le dans la [vue en arborescence](Tree_view/fr.md).
2.  Utilisez le bouton de la barre d\'outils <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:24px;"> ou le menu **Résolution → Équations électromagnétiques → Équation de force électrique**.
3.  Utilisez maintenant le bouton de la barre d\'outils <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> ou le menu **Résolution → Équations électromagnétiques → [Équation électrostatique](FEM_EquationElectrostatic/fr.md)**. Ceci est important car l\'équation de force électrique a besoin du champ potentiel calculé par l\'équation électrostatique.
4.  Changez les [paramètres du solveur de l\'équation](#Param.C3.A8tres_du_solveur.md) ou les [paramètres généraux du solveur](FEM_SolverElmer_SolverSettings/fr.md) si nécessaire.

L\'équation de la force électrique ne calcule la force que pour les faces avec un <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> [potentiel électrostatique](FEM_ConstraintElectrostaticPotential/fr.md) avec l\'option **Calculer la force électrique** de la condition aux limites est utilisée.



## Paramètres du solveur 

Pour les paramètres généraux du solveur, voir les [paramètres du solveur Elmer](FEM_SolverElmer_SolverSettings/fr.md).

L\'équation de la force électrique fournit ce paramètre spécial :

-    **Exec Solver**: par défaut, l\'équation n\'est résolue qu\'après un pas de temps. Cela signifie qu\'elle est résolue une fois que la solution des autres équations a convergé. Lorsque le réglage est à *Always*, l\'équation est résolue après chaque itération par pas de temps. (Pour les simulations en [état stationnaire](FEM_SolverElmer_SolverSettings#Type.md), la simulation entière est un pas de temps).



## Informations sur les caractéristiques d\'analyse 

L\'équation de la force électrique n\'a pas de caractéristiques d\'analyse propres. Elle prend la <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> [condition limite du potentiel électrostatique](FEM_ConstraintElectrostaticPotential/fr.md) de l\'<img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> [équation électrostatique](FEM_EquationElectrostatic/fr.md). Dans la condition limite, il est important d\'utiliser l\'option **Calculer la force électrique**.



## Résultat

Le résultat est la densité de force électrique en $\rm N/m^2$.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationElectricforce/fr

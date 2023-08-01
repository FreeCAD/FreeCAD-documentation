---
- GuiCommand:
   Name:FEM EquationElectrostatic
   Name/fr:FEM Equation électrostatique
   MenuLocation:Résolution → Équations électromagnétiques → Équation électrostastique
   Workbenches:[FEM](FEM_Workbench/fr.md)
   Version:0.19
   SeeAlso:[FEM Équation de force électrique](FEM_EquationElectricforce/fr.md), [FEM Exemple calcul capacité de deux sphères](FEM_Example_Capacitance_Two_Balls/fr.md)
---

# FEM EquationElectrostatic/fr

Cette équation permet d\'effectuer des analyses électrostatiques en utilisant le [Théorème de Gauss](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Gauss_(%C3%A9lectromagn%C3%A9tisme)).

Pour plus d\'informations sur les mathématiques de l\'équation, voir [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Electrostatics*.



## Utilisation

1.  Après avoir ajouté un solveur Elmer comme décrit [ici](FEM_SolverElmer/fr#.C3.89quations.md), sélectionnez-le dans la [vue en arborescence](Tree_view/fr.md)
2.  Utilisez maintenant le bouton de la barre d\'outils <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:24px;"> ou le menu **Résolution → Équations électromagnétiques → Équation électrostastique**.
3.  Modifiez les [paramètres du solveur de l\'équation](#Param.C3.A8tres_du_solveur.md) ou les [paramètres généraux du solveur](FEM_SolverElmer_SolverSettings/fr.md) si nécessaire.



## Paramètres du solveur 

Pour les paramètres généraux du solveur, voir les [paramètres du solveur Elmer](FEM_SolverElmer_SolverSettings/fr.md).

L\'équation électrostatique fournit ces paramètres spéciaux :

-    **Calculate Capacitance Matrix**: calcule la matrice de capacité. La matrice contient les charges ponctuelles des nœuds de la maille.

-    **Calculate Electric Energy**: calcule l\'[énergie potentielle électrostatique](https://fr.wikipedia.org/wiki/%C3%89nergie_potentielle_%C3%A9lectrostatique).

-    **Calculate Electric Field**: calcule le [champ électrique](https://fr.wikipedia.org/wiki/Champ_%C3%A9lectrique).

-    **Calculate Electric Flux**: calcule le [flux électrique](https://fr.wikipedia.org/wiki/Flux_%C3%A9lectrique).

-    **Calculate Surface Charge**: calcule la [charge de surface (en)](https://en.wikipedia.org/wiki/Surface_charge).

-    **Capacitance Matrix Filename**: fichier dans lequel la matrice de capacité est sauvegardée. Il n\'est utilisé que si **Calculate Capacitance Matrix** est réglé à *true*.

-    **Constant Weights**: si la pondération constante des résultats est utilisée.

-    **Potential Difference**: différence de potentiel en Volt pour laquelle la capacité est calculée. Elle n\'est utilisée que si **Calculate Capacitance Matrix** est réglé à*false*. Par conséquent, ce paramètre spécifie en fait la tension entre les électrodes d\'un simple condensateur. Notez que la tension donnée doit être cohérente avec les potentiels définis dans les conditions aux limites.



## Informations sur les contraintes 

L\'équation électrostatique prend en compte les contraintes suivantes si elles sont définies :

-   <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> [Contrainte de potentiel électrostatique](FEM_ConstraintElectrostaticPotential/fr.md)
-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:24px;"> [Constante de permittivité du vide](FEM_ConstantVacuumPermittivity/fr.md)



### Remarque

Sauf pour les calculs en 2D, pour les <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> [Contraintes de potentiel électrostatique](FEM_ConstraintElectrostaticPotential/fr.md), il est important qu\'elles agissent sur une face ou un corps. Les contraintes pour la 3D définies sur des lignes ou des sommets ne sont pas reconnues par le solveur Elmer.



## Résultats

Les résultats disponibles dépendent des [paramètres du solver](#Param.C3.A8tres_du_solveur.md). Si aucun des paramètres de **Calculate *** n\'a été défini sur *true*, seuls la densité de force électrique et le potentiel électrique sont calculés. Sinon, les résultats correspondants seront également disponibles.

Les résultats possibles sont :

-   Densité d\'énergie électrique en $\rm J/m^3$
-   Champ électrique en $\rm V/m$
-   Flux électrique en $\rm A\cdot s/m^2$
-   Densité de force électrique en $\rm N/m^2$
-   Potentiel en $\rm V$
-   Charges potentielles en $\rm C$





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationElectrostatic/fr

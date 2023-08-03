---
 GuiCommand:
   Name: FEM EquationMagnetodynamic2D
   Name/fr: FEM Équation magnétodynamique 2D
   MenuLocation: Résolution , Équations électromagnétiques , Équation magnétodynamique 2D
   Workbenches: FEM_Workbench/fr
   Version: 0.21
   SeeAlso: FEM_EquationMagnetodynamic/fr
---

# FEM EquationMagnetodynamic2D/fr

Cette équation effectue des analyses en utilisant une version 2D des [équations de Maxwell](https://fr.wikipedia.org/wiki/%C3%89quations_de_Maxwell) lorsque l\'inconnue est la composante z (ou composante φ).

Pour plus d\'informations sur les mathématiques de l\'équation, voir le [Manuel des modèles d\'Elmer (en)](http://www.elmerfem.org/blog/documentation/), section *Computation of Magnetic Fields in 2D*.

Pour des analyses plus générales en 3D utilisant les équations de Maxwell, FreeCAD prend en charge l\'[équation magnétodynamique](FEM_EquationMagnetodynamic/fr.md) d\'Elmer. Néanmoins, s\'il est possible d\'effectuer l\'analyse en 2D, cela est recommandé car les mathématiques sont alors plus simples et le temps de calcul est donc plus rapide.



## Utilisation

1.  Après avoir ajouté un solveur Elmer comme décrit [ici](FEM_SolverElmer/fr#.C3.89quations.md), sélectionnez-le dans la [vue en arborescence](Tree_view/fr.md)
2.  Utilisez maintenant le bouton de la barre d\'outils <img alt="" src=images/FEM_EquationMagnetodynamic2D.svg  style="width:24px;"> ou le menu **Résolution → Équations électromagnétiques → Équation magnétodynamique 2D**.
3.  Modifiez les [paramètres du solveur de l\'équation](#Param.C3.A8tres_du_solveur.md) ou les [paramètres généraux du solveur](FEM_SolverElmer_SolverSettings/fr.md) si nécessaire.



## Paramètres du solveur 

Pour les paramètres généraux du solveur, voir les [paramètres du solveur Elmer](FEM_SolverElmer_SolverSettings/fr.md).

L\'équation magnétodynamique 2D fournit ces paramètres spéciaux :

-    **Angular Frequency**: fréquence d\'actionnement harmonique. Elle n\'est utilisée que si **Is Harmonic** est réglé à *true*.

-    **Calculate Current Density**: calcule la [densité de courant](https://fr.wikipedia.org/wiki/Densit%C3%A9_de_courant).

-    **Calculate Electric Field**: calcule le [champ vectoriel électrique](https://fr.wikipedia.org/wiki/Champ_%C3%A9lectrique).

-    **Calculate Elemental Fields**: calcule les champs électromagnétiques pour chaque élément du maillage. Ceci est utile pour voir les discontinuités dans les mailles.**Remarque** : pour le moment FreeCAD ne peut pas afficher ces résultats correctement. C\'est pourquoi il n\'est pour l\'instant d\'aucune utilité pratique.

-    **Calculate Harmonic Loss**: calcule la perte de puissance harmonique linéaire et quadratique. Voir le [Manuel des modèles d\'Elmer (en)](http://www.elmerfem.org/blog/documentation/), section *Loss Estimation Using the Fourier Series* pour plus de détails.

-    **Calculate Joule Heating**: calcule l\'[effet Joule](https://fr.wikipedia.org/wiki/Effet_Joule).

-    **Calculate Magnetic Strength**: calcule l\'[intensité du champ magnétique](https://fr.wikipedia.org/wiki/Champ_magn%C3%A9tique).

-    **Calculate Maxwell Stress**: calcule le champ du [tenseur des contraintes de Maxwell](https://fr.wikipedia.org/wiki/Tenseur_des_contraintes_de_Maxwell).

-    **Calculate Nodal Fields**: calcule les champs pour chaque noeud du maillage. La valeur par défaut est *true*. Si aucune autre **Calculate *** n\'est définie à *true*, seule la densité de flux magnétique est calculé.

-    **Calculate Nodal Forces**: calcule les forces pour chaque nœud du maillage. Les résultats peuvent être utilisés pour une analyse mécanique ultérieure.

-    **Calculate Nodal Heating**: calcule le champ scalaire de la chaleur par effet Joule pour chaque noeud de maillage.

-    **Is Harmonic**: si la force motrice est actionnée de manière harmonique (courant alternatif). Si la valeur est *true*, **Angular Frequency** doit avoir une valeur \> 0.



## Informations sur les contraintes 

L\'équation magnétodynamique 2D prend en compte les contraintes suivantes si elles sont définies :

-   <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:24px;"> [Contrainte de potentiel électrostatique](FEM_ConstraintElectrostaticPotential/fr.md)
-   <img alt="" src=images/FEM_ConstraintCurrentDensity.svg  style="width:24px;"> [Contrainte de densité de courant](FEM_ConstraintCurrentDensity/fr.md)
-   <img alt="" src=images/FEM_ConstraintMagnetization.svg  style="width:24px;"> [Contrainte de magnétisation](FEM_ConstraintMagnetization/fr.md)
-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:24px;"> [Constante de permittivité du vide](FEM_ConstantVacuumPermittivity/fr.md)



## Résultats

Les résultats disponibles dépendent des [paramètres du solveur](#Paramètres_du_solveur.md). Si aucun des paramètres **Calculate *** n\'a été réglé à *true*, seul le potentiel électrique (appelé **av** dans les résultats) est calculé. Sinon, les résultats correspondants seront également disponibles.

Les résultats possibles sont :

-   Densité de courant en $\rm A/m^2$
-   Valeurs du vecteur champ électrique en $\rm V/m$.
-   Puissance harmonique perdue en $\rm W$.
-   Densité du flux magnétique en $\rm T$.
-   Valeurs du tenseur des contraintes de Maxwell en $\rm As/m^3$.
-   Intensité du champ magnétique en $\rm A/m$.
-   Force nodale en $\rm N$
-   Effet Joule en $\rm J$
-   Potentiel en $\rm V$





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationMagnetodynamic2D/fr

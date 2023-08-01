---
- GuiCommand:
   Name:FEM EquationMagnetodynamic
   Name/fr:FEM Équation magnétodynamique
   MenuLocation:Résolution → Équations électromagnétiques → Équation magnétodynamique
   Workbenches:[FEM](FEM_Workbench/fr.md)
   Version:0.21
   SeeAlso:[FEM Équation magnétodynamique 2D](FEM_EquationMagnetodynamic2D/fr.md)
---

# FEM EquationMagnetodynamic/fr

Cette équation effectue des analyses en utilisant les [équations de Maxwell](https://fr.wikipedia.org/wiki/%C3%89quations_de_Maxwell).

Pour plus d\'informations sur les mathématiques de l\'équation, voir le [Manuel des modèles d\'Elmer (en)](http://www.elmerfem.org/blog/documentation/), section *Computation of Magnetic Fields in 3D*.

S\'il est possible de calculer en 2D, des mathématiques plus simples peuvent être utilisées, ce qui permet des temps de résolution plus rapides. Pour le 2D, FreeCAD prend donc en charge l\'[équation magnétodynamique 2D](FEM_EquationMagnetodynamic2D/fr.md) d\'Elmer.



## Utilisation

1.  Après avoir ajouté un solveur Elmer comme décrit [ici](FEM_SolverElmer/fr#Équations.md), sélectionnez-le dans la [vue en arborescence](Tree_view/fr.md).
2.  Utilisez maintenant le bouton de la barre d\'outils <img alt="" src=images/FEM_EquationMagnetodynamic.svg  style="width:24px;"> ou le menu **Résolution → Équations électromagnétiques → Équation magnétodynamique**.
3.  Modifiez les [paramètres du solveur de l\'équation](#Paramètres_du_solveur.md) ou les [paramètres généraux du solveur](FEM_SolverElmer_SolverSettings/fr.md) si nécessaire.
4.  Il est recommandé de définir dans les [paramètres du solveur de systèmes linéaires](FEM_SolverElmer_SolverSettings/fr#Système_linéaire.md), **Linear Iterative Method** à **BiCGStabl**, **BiCGstabl Degree** à **4** et **Linear Preconditioning** à **None**. Cela garantit que l\'équation peut être résolue dans la plupart des cas. Si c\'est le cas, ces paramètres peuvent être modifiés si nécessaire.



## Paramètres du solveur 

Pour les paramètres généraux du solveur, voir les [paramètres du solveur Elmer](FEM_SolverElmer_SolverSettings/fr.md).

L\'équation magnétodynamique fournit ces paramètres spéciaux :



### Système linéaire 

-    **Linear System Refactorize**: refactorise la matrice du système.



### Magnétodynamique

-    **Angular Frequency**: fréquence d\'actionnement harmonique. Elle n\'est utilisée que si **Is Harmonic** est réglé à *true*.

-    **Automated Source Projection BCs**: voir le [Manuel des modèles d\'Elmer (en)](http://www.elmerfem.org/blog/documentation/), section *Computation of Magnetic Fields in 3D* pour plus d\'informations.

-    **FixInput Current Density**: assure l\'absence de divergence de la densité de courant.

-    **Is Harmonic**: si la force motrice est actionnée de manière harmonique (courant alternatif). Si elle est définie à *true*, **Angular Frequency** doit avoir une valeur \> 0.

-    **Lagrange Gauge Penalization Coefficient**: voir le [Manuel des modèles d\'Elmer (en)](http://www.elmerfem.org/blog/documentation/), section *Computation of Magnetic Fields in 3D* pour plus d\'informations.

-    **Quadratic Approximation**: permet une approximation de second ordre du courant d\'entraînement.Remarque : l\'ordre par défaut des [maillages de Gmsh](FEM_MeshGmshFromShape/fr.md) dans FreeCAD est de 2ème ordre. Lorsque vous utilisez des maillages de 2ème ordre, il est obligatoire de mettre cette option à *true*. Sinon vous obtiendrez cette erreur : *ERROR:: GetEdgeBasis: Can\'t handle but linear elements, sorry.*.Cependant, pour la plupart des applications, un maillage d\'ordre 1 est suffisant. Une exception est le cas où un filtre Isocontour doit être appliqué pour visualiser les résultats. Dans ce cas, il est recommandé d\'utiliser un maillage d\'ordre 2 et donc de définir **Quadratic Approximation** à *true*.

-    **Static Conductivity**: voir le [Manuel des modèles d\'Elmer (en)](http://www.elmerfem.org/blog/documentation/), section *Computation of Magnetic Fields in 3D* pour plus d\'informations.

-    **Use Lagrange Gauge**: voir le [Manuel des modèles d\'Elmer (en)](http://www.elmerfem.org/blog/documentation/), section *Computation of Magnetic Fields in 3D* pour plus d\'informations.

-    **Use Piola Transform**: doit être *true* si les fonctions de base pour l\'interpolation des éléments arête sont sélectionnés pour être des membres de la famille optimale des éléments de bord ou si une approximation de second ordre est utilisée.

-    **Use Tree Gauge**: voir le [Manuel des modèles d\'Elmer (en)](http://www.elmerfem.org/blog/documentation/), section *Computation of Magnetic Fields in 3D* pour plus d\'informations. Sera ignoré si **Use Piola Transform** est à *true*.



### Résultats

-    **Calculate Current Density**: calcule la [densité de courant](https://fr.wikipedia.org/wiki/Densit%C3%A9_de_courant).

-    **Calculate Electric Field**: calcule le [champ vectoriel électrique](https://fr.wikipedia.org/wiki/Champ_%C3%A9lectrique).

-    **Calculate Elemental Fields**: calcule les champs électromagnétiques pour chaque élément du maillage. Ceci est utile pour voir les discontinuités dans les mailles.**Remarque** : pour le moment FreeCAD ne peut pas afficher ces résultats correctement. C\'est pourquoi il n\'est pour l\'instant d\'aucune utilité pratique.

-    **Calculate Harmonic Loss**: calcule la perte de puissance harmonique linéaire et quadratique. Voir le [Manuel des modèles d\'Elmer (en)](http://www.elmerfem.org/blog/documentation/), section *Loss Estimation Using the Fourier Series* pour plus de détails.

-    **Calculate Joule Heating**: calcule l\'[effet Joule](https://fr.wikipedia.org/wiki/Effet_Joule).

-    **Calculate Magnetic Strength**: calcule l\'[intensité du champ magnétique](https://fr.wikipedia.org/wiki/Champ_magn%C3%A9tique).

-    **Calculate Maxwell Stress**: calcule le champ du [tenseur de contrainte de Maxwell](https://fr.wikipedia.org/wiki/Tenseur_des_contraintes_de_Maxwell).

-    **Calculate Nodal Fields**: calcule les champs pour chaque noeud du maillage. La valeur par défaut est *true*. Si aucune autre **Calculate *** n\'est définie à *true*, il calcule uniquement la densité de flux magnétique.

-    **Calculate Nodal Forces**: calcule les forces pour chaque nœud du maillage. Les résultats peuvent être utilisés pour une analyse mécanique ultérieure.

-    **Calculate Nodal Heating**: calcule le champ scalaire de la chaleur par effet Joule pour chaque noeud de la maille.



## Informations sur les contraintes 

L\'équation magnétodynamique prend en compte les contraintes suivantes si elles sont définies :

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
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationMagnetodynamic/fr

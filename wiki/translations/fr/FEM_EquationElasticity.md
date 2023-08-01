---
- GuiCommand:
   Name:FEM EquationElasticity
   Name/fr:FEM Équation d'élasticité
   MenuLocation:Résolution → Équations mécaniques → Équation d'élasticité
   |Workbenches:[FEM](FEM_Workbench/fr.md)
   Version:0.17
   SeeAlso:[FEM Équation de déformation](FEM_EquationDeformation/fr.md), [FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM EquationElasticity/fr

## Description

Cette équation décrit les propriétés mécaniques des corps rigides.

Pour plus d\'informations sur les mathématiques de l\'équation, voir [Elmer models manual](http://www.elmerfem.org/blog/documentation/), section *Linear Elasticity*.



## Utilisation

1.  Après avoir ajouté un solveur Elmer comme décrit [ici](FEM_SolverElmer/fr#.C3.89quations.md), sélectionnez-le dans la [vue en arborescence](Tree_view/fr.md).
2.  Utilisez maintenant le bouton de la barre d\'outils <img alt="" src=images/FEM_EquationElasticity.svg  style="width:24px;"> ou le menu **Résolution → Équations mécaniques → Équation d'élasticité**.
3.  Modifiez les [paramètres du solveur de l\'équation](#Param.C3.A8tres_du_solveur.md) ou les [paramètres généraux du solveur](FEM_SolverElmer_SolverSettings/fr.md) si nécessaire.

**Remarque** : pour les analyses de déformation non linéaire, vous devez utiliser l\'<img alt="" src=images/FEM_EquationDeformation.svg  style="width:32px;"> [équation de déformation](FEM_EquationDeformation/fr.md) ({{Version/fr|0.21}}). L\'équation d\'élasticité ne concerne que les déformations linéaires.

**Remarque** : si vous utilisez plus d\'un cœur de CPU pour le solveur ({{Version/fr|0.21}}), vous ne pouvez pas utiliser les paramètres par défaut du solveur. Cependant, l\'utilisation d\'un seul CPU et des paramètres de solveur par défaut est dans de nombreux cas plus rapide que l\'utilisation de plusieurs CPU car le solveur d\'élasticité n\'est rapide que lorsque **Linear Solver Type** est réglé à *Direct* (la valeur par défaut est décrite [ici](FEM_SolverElmer_SolverSettings/fr#Système_linéaire.md)). Pour la résolution multi-CPU, on ne peut utiliser que la **Linear Direct Method** de *MUMPS*. Cependant, MUMPS n\'est pas disponible en téléchargement direct.



## Paramètres du solveur 

Pour les paramètres généraux du solveur, voir les [Paramètres du solveur Elmer](FEM_SolverElmer_SolverSettings/fr.md).

L\'équation d\'élasticité fournit ces paramètres spéciaux :

-    **Calculate Pangle**: si les angles principaux doivent être calculés.

-    **Calculate Principal**: si toutes les contraintes doivent être calculées.

-    **Calculate Strains**: si les déformations doivent être calculées. Ceci calculera également les contraintes, même si **Calculate Principal** ou **Calculate Stresses** sont *false*.

-    **Calculate Stresses**: si les contraintes doivent être calculées. Par rapport à **Calculate Principal**, le critère d\'élasticité de Tresca et la contrainte principale ne seront pas calculés.

-    **Constant Bulk System**: voir le manuel d\'Elmer pour plus d\'informations.

-    **Displace Mesh**: si le maillage peut être déformé. Par défaut \'à *true* et doit être mis à *false* pour les analyses de fréquence propre.

-    **Fix Displacement**: si les déplacements ou les forces sont fixés, **Model Lumping** est automatiquement utilisé.

-    **Geometric Stiffness**: considère la rigidité géométrique du corps.

-    **Incompressible**: calcul du matériau incompressible en liaison avec le matériau viscoélastique de Maxwell et une **Variable** personnalisée.

-    **Maxwell Material**: calcul du modèle de matériau viscoélastique.

-    **Model Lumping**: utilise la [modélisation par blocs fonctionnels](https://fr.wikipedia.org/wiki/Bloc_fonctionnel).

-    **Model Lumping Filename**: fichier permettant de sauvegarder les résultats de la modélisation par blocs fonctionnels.

-    **Stability Analysis**: si *true*, **Eigen Analysis** devient une analyse de stabilité (analyse de flambage). Sinon, une analyse modale est effectuée.

-    **Update Transient System**: voir le manuel d\'Elmer pour plus d\'informations.

-    **Variable**: variable pour l\'équation d\'élasticité. Ne modifiez cette variable que si **Incompressible** est définie à *true*, conformément au manuel d\'Elmer.

Valeurs propres :

-    **Eigen Analysis**: si une analyse propre doit être effectuée (calcul des modes propres et des fréquences propres).

-    **Eigen System Complex**: doit être à *true* si le système propre est complexe. Il doit être à *false* pour une analyse des valeurs propres amortie.

-    **Eigen System Compute Residuals**: calcule les résidus du système de valeurs propres.

-    **Eigen System Damped**: définit une analyse propre amortie. Ne peut être utilisé que si **[Type de solveur linéaire](FEM_SolverElmer_SolverSettings/fr#Syst.C3.A8me_lin.C3.A9aire.md)** est *Iterative*.

-    **Eigen System Select**: sélection des valeurs propres qui sont calculées. Notez que la sélection de *Largest\** provoque une exécution infinie pour un solveur Elmer récent (à partir d\'août 2022).

-    **Eigen System Tolerance**: tolérance de convergence pour la résolution itérative du système propre. La valeur par défaut est 100 fois la **[Type de solveur linéaire](FEM_SolverElmer_SolverSettings/fr#Syst.C3.A8me_lin.C3.A9aire.md)**.

-    **Eigen System Values**: numéro du mode propre le plus élevé qui doit être calculé.

Équation :

-    **Contrainte plane**: calcule la solution en fonction de la situation de contrainte plane. S\'applique uniquement à la géométrie 2D.



## Informations sur les contraintes 

L\'équation d\'élasticité prend en compte les contraintes suivantes si elles sont définies :

-   <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Contrainte d\'immobilisation](FEM_ConstraintFixed/fr.md)
-   <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [Contrainte de déplacement](FEM_ConstraintDisplacement/fr.md)
-   <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Contrainte de force](FEM_ConstraintForce/fr.md)
-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Contrainte de température initiale](FEM_ConstraintInitialTemperature/fr.md)
-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Contrainte de pression](FEM_ConstraintPressure/fr.md)
-   <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Contrainte de poids propre](FEM_ConstraintSelfWeight/fr.md)
-   <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Contrainte de ressort](FEM_ConstraintSpring/fr.md)



### Remarque

-   Sauf pour les calculs en 2D, pour toutes les contraintes ci-dessus, il est important qu\'elles agissent sur une face. Les contraintes pour la 3D définies sur des lignes ou des sommets ne sont pas reconnues par le solveur Elmer.



## Analyse en mode propre 

Pour effectuer une analyse en mode propre (calcul des modes et fréquences propres), vous devez

1.  Définir **Eigen Analysis** : à *true*.
2.  Définir **Displace Mesh** : à *false* (faux)
3.  Définir **Eigen System Values** : mettre le nombre le plus élevé de modes propres qui vous intéresse. Plus ce nombre est petit, plus le temps d\'exécution du solveur est court puisque les modes supérieurs peuvent être omis du calcul.
4.  Ajouter une [Contrainte d\'immobilisation](FEM_ConstraintFixed/fr.md) et définir au moins une face du corps comme fixe.
5.  Lancer le solveur.

Il est fortement recommandé d\'utiliser **Linear Solver Type** réglé à *Direct* (valeur par défaut) car cela est beaucoup plus rapide et les résultats sont plus précis.



## Analyse de flambage 

Pour effectuer une analyse de flambage, vous devez procéder de la même manière que pour une [Analyse en mode propre](#Analyse_en_mode_propre.md), et en plus :

-   Définir **Analyse de stabilité** à *true*.



## Résultats

Les résultats disponibles dépendent des [paramètres du solveur](#Param.C3.A8tres_du_solveur.md). Si aucun des paramètres de **Calculate *** n\'a été défini à *true*, seul le déplacement est calculé. Sinon, les résultats correspondants seront également disponibles. Si **Eigen Analysis** est réglée à *true*, tous les résultats seront disponibles pour chaque mode propre calculé.

Si **Eigen Analysis** a été réglée à *true*, les fréquences propres seront affichées à les logs du solveur dans le dialogue du solveur et également dans le document **SolverElmerOutput** qui sera créé dans l\'arborescence une fois que le solveur aura terminé.

**Remarque :** le vecteur de déplacement du mode propre $\vec{d}$ a une valeur arbitraire puisque le résultat est

$\quad
\vec{d} = c\cdot\vec{u}$

alors que $\vec{u}$ est le vecteur propre et $c$ est un nombre complexe.





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationElasticity/fr

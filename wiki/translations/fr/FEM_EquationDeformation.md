---
- GuiCommand:
   Name: FEM EquationDeformation
   Name/fr: FEM
   MenuLocation: Résolution -> Équations mécaniques -> Équation de déformation
   Workbenches: FEM_Workbench/fr
   Version: 0.21
   SeeAlso: FEM_EquationElasticity/fr, FEM_tutorial/fr
---

# FEM EquationDeformation/fr

## Description

Cette équation décrit la déformation élastique non linéaire des corps rigides.

Pour plus d\'informations sur les mathématiques de l\'équation, voir le [manuel des modèles d\'Elmer (en)](http://www.elmerfem.org/blog/documentation/), section *Finite Elasticity*.



## Utilisation

1.  Après avoir ajouté un solveur Elmer comme décrit [ici](FEM_SolverElmer/fr#.C3.89quations.md), sélectionnez-le dans la [vue en arborescence](Tree_view/fr.md).
2.  Utilisez maintenant le bouton de la barre d\'outils <img alt="" src=images/FEM_EquationDeformation.svg  style="width:24px;"> ou le menu **Résolution → Équations mécaniques → Équation de déformation**.
3.  Modifiez les [paramètres du solveur de l\'équation](#Param.C3.A8tres_du_solveur.md) ou les [paramètres généraux du solveur](FEM_SolverElmer_SolverSettings/fr.md) si nécessaire.



## Paramètres du solveur 

Pour les paramètres généraux du solveur, voir les [paramètres du solveur Elmer](FEM_SolverElmer_SolverSettings/fr.md).

L\'équation de déformation fournit ces paramètres spéciaux :

-    **Calculate Pangle**: si les angles principaux doivent être calculés.

-    **Calculate Principal**: si toutes les contraintes doivent être calculées.

-    **Calculate Strains**: si les déformations doivent être calculées. Les contraintes seront également calculées, même si **Calculate Principal** ou **Calculate Stresses** sont réglés à *false*.

-    **Calculate Stresses**: si les contraintes doivent être calculées. Par rapport à **Calculate Principal**, le critère d\'élasticité de Tresca et la contrainte principale ne seront pas calculés.

-    **Initialize State Variables**: voir le manuel d\'Elmer pour plus d\'informations.

-    **Mixed Formulation**: voir le manuel d\'Elmer pour plus d\'informations.

-    **Neo Hookean Model**: utilise le modèle de matériau néo-hookéen.

-    **Variable**: variable pour l\'équation d\'élasticité. Changez ici le *3* en *2* si vous avez une géométrie 2D. Dans le cas particulier où **Mixed Formulation** et **Neo Hookean Model** sont réglés à *true*, le nombre de variables doit être égal aux dimensions de la géométrie + 1, donc pour une géométrie 3D, le *3* doit être remplacé par *4*.

Équation :

-    **Plane Stress**: calcule la solution en fonction de la situation de contrainte plane. S\'applique uniquement à la géométrie 2D.



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



## Résultats

Les résultats disponibles dépendent des [paramètres du solveur](#Param.C3.A8tres_du_solveur.md). Si aucun des paramètres de **Calculate *** n\'a été défini sur *true*, seul le déplacement est calculé. Dans le cas contraire, les résultats correspondants seront également disponibles.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM EquationDeformation/fr

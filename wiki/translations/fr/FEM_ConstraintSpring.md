---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ConstraintSpring
   Name/fr: FEM Ressort
   MenuLocation: Modèle , Conditions limites et charges mécaniques , Ressort
   Workbenches: FEM_Workbench/fr
   Version: 0.20
}}
{{GuiCommandFemInfo/fr
   Solvers: Elmer
}}
---

# FEM ConstraintSpring/fr

## Description

Définit une condition limite de ressort à utiliser pour les analyses mécaniques à l\'aide du <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [solveur Elmer](FEM_SolverElmer/fr.md).


{{Version/fr|0.21}}

: la contrainte de ressort peut être utilisée pour les équations de <img alt="" src=images/FEM_EquationDeformation.svg  style="width:32px;"> [Déformation](FEM_EquationDeformation/fr.md) et d\'<img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Elasticité](FEM_EquationElasticity/fr.md).



## Utilisation

1.  Utilisez soit le bouton de la barre d\'outils **<img src="images/FEM_ConstraintSpring.svg" width=16px> [Ressort](FEM_ConstraintSpring/fr.md)** soit **Modèle → Conditions limites et charges mécaniques → <img src="images/FEM_ConstraintSpring.svg" width=16px> Ressort** du menu.
2.  Appuyez sur le bouton **Ajouter**.
3.  Dans la [vue 3D](3D_view/fr.md), sélectionnez les faces auxquelles le ressort doit être appliqué. Pour supprimer des faces de la sélection, appuyez sur le bouton **Supprimer** et cliquez dessus.
4.  Spécifiez la rigidité normale ou tangentielle (en N/m) et sélectionnez celle qu\'Elmer doit utiliser.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintSpring/fr

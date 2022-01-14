---
- GuiCommand:/fr
   Name:FEM ConstraintForce
   Name/fr:FEM Contrainte de force
   MenuLocation:Model → Mechanical Constraints → Constraint force
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[FEM Contrainte de pression](FEM_ConstraintPressure/fr.md)
---

# FEM ConstraintForce/fr

## Description

Cette commande applique une force de valeur donnée \[N\] à la géométrie cible sélectionnée.

## Utilisation

Appliquer une force à une face, une ligne ou un point :

-   Dans l\'atelier FEM, cliquez sur <img alt="Constraint Force" src=images/FEM_ConstraintForce.svg  style="width:24px;"> ou sélectionnez **Model** → **Mechanical Constraints** → **Constraint force** pour ouvrir la boîte de dialogue des propriétés de la contrainte de force.

-   Si le maillage est affiché, vous devez le masquer (sélectionnez l\'objet maillé et appuyez sur la **barre d'espace** ou cliquez droit et sélectionnez **Cacher l'élément**) et afficher le modèle d\'origine.

-   Cliquez sur une *face*, une *ligne* ou un *point* sur lequel une force doit être appliquée. Il apparaîtra dans la liste des objets géométriques.

-   Remplissez **Load [N]** avec une valeur de force en \[N\].

-    **Direction**: Dans un cas typique, vous laisserez ce champ vide pour appliquer une force dans la direction normale. Vous pouvez inverser la direction de la force en cliquant sur **Direction inverse**. Dans d\'autres cas, vous devez choisir une face/un plan ou une arête, qui sert de référence pour la direction de la force.

![](images/FEM_ConstraintForce_example.JPG )

-   Cliquez sur **OK** pour terminer le dialogue et créer l\'objet **[<img src=images/FEM_ConstraintForce.svg style="width:24px"> Contrainte de force**.

## Remarques

La force définie est appliquée uniformément aux objets sélectionnés. Par exemple, si vous définissez une contrainte de force de 200 N appliquée à deux faces ayant la même surface, chaque face sera chargée uniformément de 100 N.





{{FEM Tools navi

}}

---
[documentation index](../README.md) > FEM ConstraintForce/fr

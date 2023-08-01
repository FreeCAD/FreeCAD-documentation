---
- GuiCommand:
   Name:FEM ConstraintForce
   Name/fr:FEM Contrainte de force
   MenuLocation:Modèle → Contraintes mécaniques → Contrainte de force
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[FEM Contrainte de pression](FEM_ConstraintPressure/fr.md)
---

# FEM ConstraintForce/fr

## Description

Cette commande applique une force de valeur donnée \[N\] à la géométrie cible sélectionnée.

## Utilisation

1.  Il existe plusieurs façons de lancer la commande permettant d\'appliquer une force à une face, une ligne ou un point :
    -   Cliquez sur **<img src="images/FEM_ConstraintForce.svg" width=16px> [Contrainte de force](FEM_ConstraintForce/fr.md)
**
    -   Sélectionnez l\'option **Modèle → Contraintes mécaniques → <img src="images/FEM_ConstraintForce.svg" width=16px> Contrainte de force** dans le menu.

2.  Si le maillage est affiché, vous devez le masquer (sélectionnez l\'objet maillé et appuyez sur la **barre d'espace** ou cliquez droit et sélectionnez **Cacher l'élément**) et afficher le modèle original.

3.  Cliquez sur une *face*, une *ligne* ou un *point* sur lequel une force doit être appliquée. L\'objet apparaîtra dans la liste des objets géométriques.

4.  Renseignez **Charge [N]** avec une valeur de force en \[N\].

5.  
    **Direction**: dans un cas typique, vous laisserez ce champ vide pour appliquer une force dans la direction normale. Vous pouvez inverser la direction de la force en cliquant sur **Inverser la direction**. Dans d\'autres cas, vous devez choisir une face/un plan ou une arête, qui sert de référence pour la direction de la force.

6.  Cliquez sur **OK** pour terminer et l\'objet **[<img src=images/FEM_ConstraintForce.svg style="width:24px"> ConstraintForce** est crée.

![](images/FEM_ConstraintForce_example.JPG )

## Remarques

-   La force définie est appliquée uniformément aux objets sélectionnés. Par exemple, si vous définissez une contrainte de force de 200 N appliquée à deux faces ayant la même surface, chaque face sera chargée uniformément de 100 N.





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintForce/fr

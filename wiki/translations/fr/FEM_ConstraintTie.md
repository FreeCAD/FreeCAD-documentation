---
- GuiCommand:/fr
   Name:FEM ConstraintTie
   Name/fr:FEM Contrainte de liaison
   MenuLocation:Model → Mechanical Constraints → Constraint tie
   Workbenches:[FEM](FEM_Workbench/fr.md)
   Version:0.19
   SeeAlso:[FEM Contrainte de pression](FEM_ConstraintPressure.md)
---

## Description

Définit une contrainte de liaison qui relie les deux surfaces sélectionnées de telle sorte que (par opposition à la façon dont le contact fonctionne) elles ne peuvent pas se séparer ou glisser l\'une sur l\'autre tout au long de l\'analyse. Ainsi, les surfaces restent collées en permanence.

## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintTie.svg" width=16px> [FEM Contrainte de liaison](FEM_ConstraintTie/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Contraintes mécaniques → <img src="images/FEM_ConstraintTie.svg" width=16px> Lien de contrainte** dans le menu.
2.  Appuyez sur le bouton **Ajouter** dans le panneau des tâches, puis cliquez sur la face que vous souhaitez ajouter à la définition de la contrainte de liaison. Deux faces exactement doivent être ajoutées, l\'une après l\'autre.
3.  En option, définissez Tolerance - la contrainte de lien sera appliquée uniquement aux noeuds séparés de la surface opposée par une distance qui ne sera pas supérieure à celle spécifiée ici.


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}  

---
 GuiCommand:
   Name: FEM ConstraintTie
   Name/fr: FEM Contrainte de liaison
   MenuLocation: Modèle , Conditions limites et charges mécaniques , Contrainte de liaison
   Workbenches: FEM_Workbench/fr
   Version: 0.19
   SeeAlso: FEM_ConstraintPressure/fr
---

# FEM ConstraintTie/fr

## Description

Définit une contrainte de liaison qui relie les deux surfaces sélectionnées de telle sorte que (par opposition à la façon dont le contact fonctionne) elles ne peuvent pas se séparer ou glisser l\'une sur l\'autre tout au long de l\'analyse. Ainsi, les surfaces restent collées en permanence.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyer sur le bouton **<img src="images/FEM_ConstraintTie.svg" width=16px> [Contrainte de liaison](FEM_ConstraintTie/fr.md)**.
    -   Sélectionner l\'option **Modèle → Conditions limites et charges mécaniques → <img src="images/FEM_ConstraintTie.svg" width=16px> Contrainte de liaison** du menu.
2.  Appuyer sur le bouton **Ajouter** dans le panneau des tâches, puis cliquez sur la face que vous souhaitez ajouter à la définition de la contrainte de liaison. Deux faces exactement doivent être ajoutées, l\'une après l\'autre.
3.  Vous pouvez définir une Ttlérance : la contrainte de liaison sera appliquée uniquement aux noeuds séparés de la surface opposée par une distance qui ne sera pas supérieure à celle spécifiée ici.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM ConstraintTie/fr

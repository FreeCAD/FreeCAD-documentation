---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ConstraintFixed
   Name/fr: FEM Condition de limite fixe
   MenuLocation: Modèle , Conditions limites et charges mécaniques , Condition de limite fixe
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_ConstraintContact/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: Tous
}}
---

# FEM ConstraintFixed/fr

## Description

Crée une condition limite FEM pour une entité géométrique fixe en verrouillant tous les degrés de liberté disponibles des nœuds sous-jacents à l\'entité géométrique sélectionnée (6 degrés de liberté pour les éléments poutre et coque, 3 pour les éléments solides).



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintFixed.svg" width=16px> [Condition de limite fixe](FEM_ConstraintFixed/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Conditions limites et charges mécaniques → <img src="images/FEM_ConstraintFixed.svg" width=16px> Condition de limite fixe** du menu.
2.  Appuyez sur le bouton **Ajouter**.
3.  Dans la [vue 3D](3D_view/fr.md), sélectionnez l\'objet auquel la condition de limite doit être appliquée, qui peut être un sommet, une arête ou une face (mais tous les objets doivent être du même type). Pour supprimer des objets de la sélection, appuyez sur le bouton **Supprimer** et cliquez dessus.

## Limitations

Vous ne pouvez pas mélanger les objets dans la même condition limite. Utilisez une condition limite pour chaque type d\'objet.



## Remarques

-   Cette fonction utilise le [jeu de paramètres \*BOUNDARY de CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node163.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintFixed/fr

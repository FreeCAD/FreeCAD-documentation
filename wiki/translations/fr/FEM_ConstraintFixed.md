---
 GuiCommand:
   Name: FEM ConstraintFixed
   Name/fr: FEM Condition de limite fixe
   MenuLocation: Modèle , Conditions limites et charges mécaniques , Condition de limite fixe
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_ConstraintContact/fr
---

# FEM ConstraintFixed/fr

## Description

Crée une condition limite FEM pour une entité géométrique fixe en verrouillant tous les degrés de liberté disponibles des nœuds sous-jacents à l\'entité géométrique sélectionnée (6 degrés de liberté pour les éléments poutre et coque, 3 pour les éléments solides).



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintFixed.svg" width=16px> [Condition de limite fixe](FEM_ConstraintFixed/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Conditions limites et charges mécaniques → <img src="images/FEM_ConstraintFixed.svg" width=16px> Condition de limite fixe** du menu.
2.  Dans la [vue 3D](3D_view/fr.md), sélectionnez l\'objet auquel la condition limite doit être appliquée, qui peut être un sommet (coin), une arête ou une face.

## Limitations

Vous ne pouvez pas mélanger les objets dans la même condition limite. Utilisez une condition limite pour chaque type d\'objet.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintFixed/fr

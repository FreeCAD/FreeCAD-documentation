---
 GuiCommand:
   Name: FEM ConstraintPlaneRotation
   Name/fr: FEM Contrainte multi-points de plan
   MenuLocation: Modèle , Fonctions d'analyse géométrique , Contrainte multi-points de plan
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_ConstraintTransform/fr
---

# FEM ConstraintPlaneRotation/fr

## Description

Crée une contrainte FEM multipoints (MPC) pour maintenir les nœuds d\'une surface plane sur le même plan.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyer sur le bouton **<img src="images/FEM_ConstraintPlaneRotation.svg" width=16px> [Contrainte multi-points de plan](FEM_ConstraintPlaneRotation/fr.md)**.
    -   Sélectionner l\'option **Modèle → Fonctions d'analyse géométrique → <img src="images/FEM_ConstraintPlaneRotation.svg" width=16px> Contrainte multi-points de plan** du menu.
2.  Dans la [vue 3D](3D_view/fr.md), sélectionner l\'objet auquel la contrainte multipoints doit être appliquée, qui peut être une face.

## Limitations

1.  La contrainte multipoint plane ne peut être appliquée qu\'à une seule face plane.
2.  Lorsqu\'une contrainte multipoint plane est appliquée à la même face qu\'une condition de limite de déplacement/fixe, la condition de limite de déplacement/fixe est prioritaire.



## Remarques

1.  La contrainte utilise le jeu de paramètres \*MPC dans CalculiX. le jeu de paramètres est expliqué en détail à <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node220.html>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintPlaneRotation/fr

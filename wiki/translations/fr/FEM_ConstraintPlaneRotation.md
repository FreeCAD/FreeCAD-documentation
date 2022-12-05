---
- GuiCommand:/fr
   Name:FEM ConstraintPlaneRotation
   Name/fr:FEM Contrainte de rotation du plan
   MenuLocation:Modèle → Contraintes géométriques → Contrainte de rotation plane
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[FEM Contrainte de transformation](FEM_ConstraintTransform/fr.md)
---

# FEM ConstraintPlaneRotation/fr

## Description

Crée une contrainte FEM pour maintenir les nœuds d\'une surface planaire dans le même plan.

## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintPlaneRotation.svg" width=16px> '''Contrainte de rotation plane'''**.
    -   Sélectionnez l\'option **Modèle → Contraintes géométriques → <img src="images/FEM_ConstraintPlaneRotation.svg" width=16px> Contrainte de rotation plane** dans le menu.
2.  Dans la [Vue 3D](3D_view/fr.md), sélectionnez l\'objet auquel la contrainte doit être appliquée, qui peut être une face.

## Limitations

1.  La contrainte de rotation plane ne peut être appliquée qu\'à une seule face planaire.
2.  Lorsqu\'une contrainte de rotation plane est appliquée à la même face qu\'une contrainte de déplacement/fixe, la contrainte de déplacement/fixe a la préférence.

## Remarques

1.  La contrainte utilise la carte \*MPC dans CalculiX. La carte est expliquée en détail à <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node220.html>





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintPlaneRotation/fr

---
- GuiCommand:/fr
   Name:FEM ConstraintPlaneRotation
   Name/fr:FEM Contrainte de rotation du plan
   MenuLocation:Model → Geometrical Constraints → Constraint plane rotation
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[FEM Contrainte de transformation](FEM_ConstraintTransform/fr.md)
---

## Description

Crée une contrainte FEM pour conserver les nœuds dans une surface plane dans le même plan.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintPlaneRotation.svg" width=16px> [Create a FEM constraint for plane rotation face](FEM_ConstraintPlaneRotation/fr.md)**.
    -   Sélectionnez l\'option {{MenuCommand|Model → Geometrical Constraints → <img src="images/FEM_ConstraintPlaneRotation.svg" width=16px> Constraint plane rotation}} dans le menu.
2.  Dans la [Vue 3D](3D_view/fr.md), sélectionnez l\'objet auquel la contrainte doit être appliquée, qui peut être une face.

## Limitations

1.  La contrainte de plan de rotation ne peut être appliquée qu\'à une seule face plane.
2.  Lorsqu\'une contrainte de plan de rotation est appliquée à la même face ayant une contrainte de déplacement ou de fixation, la contrainte de déplacement ou de fixation prévaut.

## Notes

1.  La contrainte utilise la carte \*MPC dans CalculiX. La carte est expliquée en détail à <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node220.html>





{{FEM Tools navi

}}  

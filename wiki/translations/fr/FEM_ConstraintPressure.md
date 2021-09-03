---
- GuiCommand:/fr
   Name:FEM ConstraintPressure
   Name/fr:FEM Contrainte de pression
   MenuLocation:Model → Mechanical Constraints → Constraint pressure
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[FEM Contrainte de force](FEM_ConstraintForce/fr.md)
---

## Description

Applique une contrainte de pression sur une face.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande:
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintPressure.svg" width=16px> [Creates a FEM constraint for a pressure cting on a face](FEM_ConstraintPressure/fr.md)**.
    -   Sélectionnez l\'option {{MenuCommand|Model → Mechanical Constraints → <img src="images/FEM_ConstraintPressure.svg" width=16px> Constraint pressure}} dans le menu.
2.  Cliquez sur **Add reference** et sélectionnez la face dans la [vue 3D](3D_view/fr.md).
3.  Modifiez la fenêtre appropriée pour spécifier la charge de pression en MPa.
4.  Cochez la case pour inverser la direction si nécessaire.

## Remarques

-   La répartition de la pression sur la face est toujours uniforme et perpendiculaire à la face.

-   Pression sur les faces: <https://tracker.freecadweb.org/view.php?id=3050>





{{FEM Tools navi

}}  

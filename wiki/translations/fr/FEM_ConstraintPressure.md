---
 GuiCommand:
   Name: FEM ConstraintPressure
   Name/fr: FEM Charge de pression
   MenuLocation: Modèle , Conditions limites et charges mécaniques , Charge de pression
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_ConstraintForce/fr
---

# FEM ConstraintPressure/fr

## Description

Applique une charge de pression à une face.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyer sur le bouton **<img src="images/FEM_ConstraintPressure.svg" width=16px> [Charge de pression](FEM_ConstraintPressure/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Conditions limites et charges mécaniques → <img src="images/FEM_ConstraintPressure.svg" width=16px> Charge de pression** du menu.
2.  Cliquer sur **Ajouter** et sélectionner la face dans la [vue 3D](3D_view/fr.md).
3.  Modifier la fenêtre appropriée pour spécifier la charge de pression en MPa.
4.  Cocher la case pour inverser la direction si nécessaire.



## Remarques

-   La répartition de la pression sur une face est toujours uniforme et toujours perpendiculaire à la face.

-   Pression sur les coques : <https://github.com/FreeCAD/FreeCAD/issues/5699>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintPressure/fr

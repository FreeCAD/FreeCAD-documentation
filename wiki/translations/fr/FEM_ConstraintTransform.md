---
- GuiCommand:
   Name: FEM ConstraintTransform
   Name/fr: FEM Contrainte de transformation
   MenuLocation: Modèle - Contraintes géométriques - Contrainte de transformation
   Workbenches: [FEM](FEM_Workbench/fr.md)
   SeeAlso: [FEM Contrainte de rotation plane](FEM_ConstraintPlaneRotation/fr.md)
---

# FEM ConstraintTransform/fr

## Description

Transforme le système de coordonnées d\'une face en un système de coordonnées particulier - rectangulaire ou cylindrique.



## Utilisation

1.  Appliquer d\'abord une [Contrainte de déplacement](FEM_ConstraintDisplacement/fr.md) à une face.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintTransform.svg" width=16px> [Contrainte de transformation](FEM_ConstraintTransform/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Contraintes géométriques → <img src="images/FEM_ConstraintTransform.svg" width=16px> Contrainte de transformation** depuis le menu.
3.  Sélectionnez la transformation rectangulaire ou cylindrique. La première peut être appliquée à n\'importe quelle face, la seconde n\'est disponible que pour les faces cylindriques.
4.  Sélectionnez une face à laquelle la contrainte de déplacement a été précédemment appliquée. Appuyez sur le bouton **Ajouter**.
5.  Pour une transformation rectangulaire, spécifiez une rotation autour de chacun des trois axes.

## Limitations

-   La transformation cylindrique ne peut être appliquée qu\'aux faces cylindriques.



## Remarques

-   Cette contrainte peut être utilisée pour simuler la torsion mais uniquement pour les barres cylindriques ou les pièces contenant de telles barres utilisées pour transmettre un couple.
-   La contrainte utilise la carte \*TRANSFORM de CalculiX.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM ConstraintTransform/fr

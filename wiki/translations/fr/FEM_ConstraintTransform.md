---
 GuiCommand:
   Name: FEM ConstraintTransform
   Name/fr: FEM Système de coordonnées locales
   MenuLocation: Modèle , Fonctions d'analyse géométrique , Système de coordonnées locales
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_ConstraintPlaneRotation/fr
---

# FEM ConstraintTransform/fr

## Description

Transforme le système de coordonnées d\'une face en un système de coordonnées particulier - rectangulaire ou cylindrique.



## Utilisation

1.  Appliquer d\'abord une [Condition limite de déplacement](FEM_ConstraintDisplacement/fr.md) à une face.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyer sur le bouton **<img src="images/FEM_ConstraintTransform.svg" width=16px> [Système de coordonnées locales](FEM_ConstraintTransform/fr.md)**.
    -   Sélectionner l\'option **Modèle → Fonctions d'analyse géométrique → <img src="images/FEM_ConstraintTransform.svg" width=16px> Système de coordonnées locales** du menu.
3.  Sélectionner la transformation rectangulaire ou cylindrique. La première peut être appliquée à n\'importe quelle face, la seconde n\'est disponible que pour les faces cylindriques.
4.  Sélectionner une face à laquelle la condition limite de déplacement a été précédemment appliquée. Appuyez sur le bouton **Ajouter**.
5.  Pour une transformation rectangulaire, spécifier une rotation autour de chacun des trois axes.

## Limitations

-   La transformation cylindrique ne peut être appliquée qu\'aux faces cylindriques.



## Remarques

-   Cette fonction peut être utilisée pour simuler la torsion mais uniquement pour les barres cylindriques ou les pièces contenant de telles barres utilisées pour transmettre un couple.
-   La fonction utilise le jeu de paramètres \*TRANSFORM de CalculiX.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM ConstraintTransform/fr

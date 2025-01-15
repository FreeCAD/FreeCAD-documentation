---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ConstraintTransform
   Name/fr: FEM Système de coordonnées locales
   MenuLocation: Modèle , Fonctions d'analyse géométrique , Système de coordonnées locales
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_ConstraintPlaneRotation/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX
}}
---

# FEM ConstraintTransform/fr

## Description

Transforme le système de coordonnées d\'une face en un système de coordonnées défini par l\'utilisateur - rectangulaire ou cylindrique. Ce système de coordonnées affecte les conditions limites et les définitions des charges. Par exemple, vous pouvez l\'utiliser pour fixer les déplacements dans la direction normale d\'une face inclinée. Il suffit de sélectionner la composante appropriée de la [condition limite de déplacement](FEM_ConstraintDisplacement/fr.md).



## Utilisation

1.  Appliquer d\'abord une [Condition limite de déplacement](FEM_ConstraintDisplacement/fr.md) à une face.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyer sur le bouton **<img src="images/FEM_ConstraintTransform.svg" width=16px> [Système de coordonnées locales](FEM_ConstraintTransform/fr.md)**.
    -   Sélectionner l\'option **Modèle → Fonctions d'analyse géométrique → <img src="images/FEM_ConstraintTransform.svg" width=16px> Système de coordonnées locales** du menu.
3.  Sélectionner la transformation rectangulaire ou cylindrique. La première peut être appliquée à n\'importe quelle face, la seconde n\'est disponible que pour les faces cylindriques.
4.  Sélectionner une face à laquelle la condition limite de déplacement a été précédemment appliquée. Appuyez sur le bouton **Ajouter**.
5.  Pour une transformation rectangulaire, spécifiez une rotation autour de chacun des trois axes. Les flèches affichées sur la face représentent les nouvelles directions (X - rouge, Y - vert et Z - bleu).

## Limitations

-   La transformation cylindrique ne peut être appliquée qu\'aux faces cylindriques.



## Remarques

-   Cette fonction peut être utilisée pour simuler la torsion mais uniquement pour les barres cylindriques ou les pièces contenant de telles barres utilisées pour transmettre un couple.
-   La fonction utilise le [jeu de paramètres \*TRANSFORM de CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node253.html).





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintTransform/fr

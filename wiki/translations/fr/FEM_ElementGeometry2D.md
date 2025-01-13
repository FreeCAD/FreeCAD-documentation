---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ElementGeometry2D
   Name/fr: FEM Épaisseur d'un élément 2D
   MenuLocation: Modèle , Géométrie de l'élement , Épaisseur d'un élément 2D
   Workbenches: FEM_Workbench/fr
   Shortcut: **C** **S**
   SeeAlso: FEM_tutorial/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: Tous
}}
---

# FEM ElementGeometry2D/fr

## Description

**Épaisseur d\'un élément 2D** est utilisé pour définir l\'épaisseur des éléments FEM 2D (coque et {{Version/fr|1.0}} : contrainte/déformation plane), tous ou situés sur la surface choisie.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ElementGeometry2D.svg" width=16px> [Épaisseur d'un élément 2D](FEM_ElementGeometry2D/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Géométrie de l'élément → <img src="images/FEM_ElementGeometry2D.svg" width=16px> Épaisseur d'un élément 2D** du menu.
2.  Spécifiez l\'épaisseur de la coque.
3.  Si vous le souhaitez, appuyez sur le bouton **Ajouter** dans le panneau des tâches, puis cliquez sur la face à laquelle vous souhaitez attribuer une épaisseur prescrite. Si la sélection des faces est vide, toutes les faces restantes (dont l\'épaisseur n\'est pas définie par d\'autres [éléments de géométrie 2D](FEM_ElementGeometry2D/fr.md)) seront automatiquement assignées.

## Limitations

-   Actuellement, les analyses combinant des éléments de coque avec des éléments solides ou des éléments de bord ne sont pas prises en charge.



## Propriétés


**Thickness**

: spécifie l\'épaisseur des éléments 2D.



## Remarques

-   Pour afficher les résultats du solveur CalculiX sur le maillage développé à l\'épaisseur prescrite, la propriété `Beam Shell Result Output 3D` dans le [Solveur CalculiX](FEM_SolverCalculixCxxtools/fr.md) doit être définie à `True`.

Cette fonction utilise le [jeu de paramètres \*\*SHELL SECTION de CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node238.html) pour les coques et le [jeu de paramètres \*SOLID SECTION](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node239.html) pour les éléments de contrainte et de déformation planes.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry2D/fr

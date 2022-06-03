---
- GuiCommand   */fr
   Name   *FEM ElementGeometry2D
   Name/fr   *FEM Élément de géométrie 2D
   MenuLocation   *Modèle → Géométrie de l'élement → Épaisseur de coque
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   Shortcut   ***C** **S**
   SeeAlso   *[Tutoriel FEM](FEM_tutorial/fr.md)
---

# FEM ElementGeometry2D/fr

## Description

**Élément de géométrie 2D** est utilisé pour définir l\'épaisseur d\'éléments FEM 2D, soit tous, soit posés sur la surface choisie.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande   *
    -   Appuyez sur le bouton **<img src="images/FEM_ElementGeometry2D.svg" width=16px> [Epaisseur de la coque](FEM_ElementGeometry2D.md)**.
    -   Sélectionnez l\'option **Modèle → Géométrie de l'élement → <img src="images/FEM_ElementGeometry2D.svg" width=16px> Epaisseur de la coque** dans le menu.
2.  Définissez un paramètre d\'épaisseur.
3.  Si vous le souhaitez, appuyez sur le bouton **Add** dans le panneau des tâches, puis cliquez sur la face pour laquelle vous souhaitez avoir une épaisseur prescrite. Si la sélection de faces est libre, toutes les faces restantes (dont l\'épaisseur n\'est pas définie par d\'autres [éléments de géométrie 2D](FEM_ElementGeometry2D/fr.md)) seront automatiquement affectées.

## Limitations

-   L\'analyse combinant des éléments de coque avec des éléments solides ou des arêtes n\'est pas prise en charge dans la version actuelle (FreeCAD 0.18).

## Propriétés


**Thickness**

   * Spécifie l\'épaisseur de la coque.

## Script

## Remarques

Pour afficher les résultats du solveur CalculiX sur le maillage développé à l\'épaisseur prescrite, la propriété `Beam Shell Result Output 3D` dans le [Solveur CalculiX](FEM_SolverCalculixCxxtools/fr.md) doit être définie sur `True`.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry2D/fr

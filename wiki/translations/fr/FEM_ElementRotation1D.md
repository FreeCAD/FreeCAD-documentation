---
- GuiCommand:/fr
   Name:FEM ElementRotation1D
   Name/fr:FEM Rotation élément type poutre
   MenuLocation:Modèle → Géométrie de l'élement → Rotation d'un élément type poutre
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[Tutoriel FEM](FEM_tutorial/fr.md)
---

# FEM ElementRotation1D/fr

## Description

**Rotation élément type poutre** est utilisé pour faire tourner le profilé d\'une poutre autour de l\'axe des éléments de la poutre.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ElementRotation1D.svg" width=16px> [Rotation d'un élément type poutre](FEM_ElementRotation1D/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Géométrie de l'élément → <img src="images/FEM_ElementRotation1D.svg" width=16px> Rotation d'un élément type poutre** dans le menu.
2.  Spécifiez l\'angle selon lequel le profilé de la poutre doit être tourné.

## Options



## Propriétés

## Limitations

-   Pour l\'instant, les rotations multiples ne sont pas prises en charge (une seule rotation est appliquée à tous les éléments de type poutre du modèle).



## Remarques

-   Pour visualiser la section transversale tournée, il est nécessaire de définir `Beam Shell Result Output 3D` dans le [FEM Solveur CalculiX standard](FEM_SolverCalculixCxxtools/fr.md) sur `True` et de lancer l\'analyse.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementRotation1D/fr

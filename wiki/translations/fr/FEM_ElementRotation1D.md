---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ElementRotation1D
   Name/fr: FEM Rotation d'un élément 1D
   MenuLocation: Modèle , Géométrie de l'élement , Rotation d'un élément 1D
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_tutorial/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX
}}
---

# FEM ElementRotation1D/fr

## Description

**Rotation d\'un élément 1D** est utilisé pour faire tourner le profilé d\'un élément type poutre autour de l\'axe des éléments de la poutre.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ElementRotation1D.svg" width=16px> [Rotation d'un élément 1D](FEM_ElementRotation1D/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Géométrie de l'élément → <img src="images/FEM_ElementRotation1D.svg" width=16px> Rotation d'un élément 1D** du menu.
2.  Spécifiez l\'angle selon lequel le profilé de l\'élément doit être tourné.



## Propriétés


**Rotation**

: spécifie l\'angle de rotation.

## Limitations

-   Actuellement, les rotations multiples ne sont pas prises en charge (une seule rotation est appliquée à toutes les poutres du modèle).



## Remarques

-   Pour visualiser la section transversale tournée, il est nécessaire de définir `Beam Shell Result Output 3D` dans le [FEM Solveur CalculiX standard](FEM_SolverCalculixCxxtools/fr.md) sur `True` et de lancer l\'analyse.
-   Cette fonction utilise le [jeu de paramètres \*BEAM SECTION de CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node162.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementRotation1D/fr

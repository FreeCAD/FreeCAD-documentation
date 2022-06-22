---
- GuiCommand   */fr
   Name   *FEM ElementGeometry1D
   Name/fr   *FEM Coupe transversale élément type poutre
   MenuLocation   *Modèle → Géométrie de l'élement → Coupe tranversale de poutre
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   Shortcut   ***C** **B**
   SeeAlso   *[Tutoriel FEM](FEM_tutorial/fr.md)
---

# FEM ElementGeometry1D/fr

## Description

**Coupe transversale élément type poutre** est utilisé pour définir les sections transversales d\'éléments de type poutre. Pour l\'instant, les types de sections transversales suivantes disponibles sections    * rectangulaire, circulaire et tube.

## Utilisation

1.  Il existe plusieurs façons de lancer la commande    *
    -   Appuyez sur le bouton **<img src="images/FEM_ElementGeometry1D.svg" width=16px> [Coupe tranversale de poutre](FEM_ElementGeometry1D/fr.md)** bouton.
    -   Sélectionnez l\'option **Modèle → Géométrie de l'élément → <img src="images/FEM_ElementGeometry1D.svg" width=16px> Coupe transversale de poutre** dans le menu.
2.  Choisissez le type de section transversale et spécifiez les dimensions nécessaires    *
    -   Rectangulaire    * largeur et hauteur,
    -   Circulaire    * diamètre,
    -   Tube    * diamètre et épaisseur.
3.  En option, appuyez sur le bouton **Ajouter** dans le panneau des tâches, puis cliquez sur l\'arête à laquelle vous voulez donner une section transversale prescrite. Si la sélection de l\'arête est libre, toutes les arêtes restantes (dont la section transversale n\'est pas définie par d\'autres [Eléments de géométries 1D](FEM_ElementGeometry1D/fr.md)) seront automatiquement attribuées.

## Options

## Propriétés

## Limitations

## Remarques

-   Pour visualiser les résultats du solveur CalculiX sur le maillage étendu à la section transversale prescrite, la propriété `Beam Shell Result Output 3D` dans le [FEM Solveur CalculiX standard](FEM_SolverCalculixCxxtools/fr.md) doit être définie sur `True`.

## Script





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry1D/fr

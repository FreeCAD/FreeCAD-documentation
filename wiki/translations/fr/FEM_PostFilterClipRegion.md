---
- GuiCommand   */fr
   Name   *FEM PostFilterClipRegion
   Name/fr   *FEM Filtre d'écrêtage d'une région
   MenuLocation   *Résultats → Filtre d'écrêtage de la région
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   SeeAlso   *[Tutoriel FEM](FEM_tutorial/fr.md)
---

# FEM PostFilterClipRegion/fr

## Description

Filtre un champ à l\'aide d\'une sphère ou d\'un plan coupant le modèle.

## Utilisation

1.  Sélectionnez un [pipeline de résultats](FEM_PostPipelineFromResult/fr.md) précédemment créé.
2.  Lancez la commande de l\'une des façons suivantes    *
    -   Appuyez sur le bouton **<img src="images/FEM_PostFilterClipRegion.svg" width=16px> [Filtre d'écrêtage de la région](FEM_PostFilterClipRegion/fr.md)**.
    -   Sélectionnez l\'option **Résultats → <img src="images/FEM_PostFilterClipRegion.svg" width=16px> Filtre d'écrêtage de la région** dans le menu.
3.  Ajustez les **Options d'affichage des résultats** comme pour le pipeline [pipeline de résultats](FEM_PostPipelineFromResult/fr.md). Cachez ce pipeline pour voir l\'effet d\'un filtre d\'écrêtage de la région.
4.  Appuyez sur le bouton **<img src="images/List-add.svg" width=16px> Créer** et sélectionnez **<img src="images/Fem-post-geo-plane.svg" width=16px> Plan** ou **<img src="images/Fem-post-geo-sphere.svg" width=16px> Sphère**, ou choisissez un plan/sphère existant dans la liste déroulante. Si nécessaire, ajustez les paramètres du plan/sphère pour vous assurer qu\'il intersecte le modèle.
5.  Le modèle sera découpé à l\'aide du plan/sphère. Sélectionnez l\'option **A l'envers** pour inverser la coupe. Sélectionnez l\'option **Couper les cellules** pour lisser la région découpée en éliminant les parties des éléments finis qui dépassent.
6.  Cliquez sur le bouton **OK** pour terminer la commande.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterClipRegion/fr

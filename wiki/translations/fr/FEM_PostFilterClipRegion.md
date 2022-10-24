---
- GuiCommand   */fr
   Name   *FEM PostFilterClipRegion
   Name/fr   *FEM Filtre d'écrêtage selon une région
   MenuLocation   *Résultats → Filtre d'écrêtage selon une région
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   SeeAlso   *[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM PostFilterClipRegion/fr

## Description

Filtre un champ à l\'aide d\'une sphère ou d\'un plan coupant le modèle.

<img alt="" src=images/FEM_Region-Cut-Filter-Example.png  style="width   *400px;">

*Un filtre d\'écrêtage selon une région avec une sphère comme fonction de découpe.Le pipeline original est l\'objet semi-transparent.*

## Utilisation

1.  Sélectionnez un [pipeline de résultats](FEM_PostPipelineFromResult/fr.md) précédemment créé.
2.  Lancez la commande soit en    *
    -   Appuyant sur le bouton **<img src="images/FEM_PostFilterClipRegion.svg" width=16px> '''Filtre de découpe selon une région'''**.
    -   Sélectionnez l\'option **Résultats → <img src="images/FEM_PostFilterClipRegion.svg" width=16px> Filtre de découpe selon une région** dans le menu.
3.  Ajustez les **Options d'affichage des résultats** comme pour le [pipeline de résultats](FEM_PostPipelineFromResult/fr.md). Vous devrez peut-être masquer le pipeline pour voir l\'effet du filtre dans l\'aperçu.
4.  Ou
    -   S\'il n\'y a pas encore de [fonction de filtre](FEM_PostCreateFunctions/fr.md) définie, appuyez sur le bouton **<img src="images/List-add.svg" width=16px> Créer
** et sélectionnez **<img src="images/Fem-post-geo-plane.svg" width=16px> Plan** ou **<img src="images/Fem-post-geo-sphere.svg" width=16px> Sphère**
    -   Choisissez une fonction de filtrage existante dans la liste. Si nécessaire, ajustez les paramètres de coupe pour vous assurer qu\'elle intersecte le modèle. Notez que les paramètres de coupe modifiés changeront également les paramètres de la fonction de filtre utilisée.
5.  Le modèle sera coupé à l\'aide de la fonction de filtrage. Sélectionnez l\'option **Inverser** pour inverser la coupe. Sélectionnez l\'option **Couper des cellules** pour lisser la région découpée en éliminant les parties des éléments finis qui dépassent.
6.  Cliquez sur le bouton **OK** pour terminer la commande.

**Remarque**    * s\'il n\'existe pas encore de fonction de filtrage, vous ne pouvez définir directement un **champ** après sa création que lorsque <img alt="" src=images/FEM_PostApplyChanges.svg  style="width   *24px;"> [Appliquer les modifications](FEM_PostApplyChanges/fr.md) est activé. Sinon, vous pouvez le faire d\'abord après avoir rouvert le menu du dialogue du filtre.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterClipRegion/fr

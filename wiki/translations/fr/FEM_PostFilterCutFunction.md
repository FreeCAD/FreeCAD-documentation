---
- GuiCommand   */fr
   Name   *FEM PostFilterCutFunction
   Name/fr   *FEM Filtre de fonction de découpe
   MenuLocation   *Résultats → Filtre de fonction de découpe
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   SeeAlso   *[FEM Pipeline de résultats](FEM_PostPipelineFromResult/fr.md), [FEM Fonctions de filtrage](FEM_PostCreateFunctions/fr.md), [FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM PostFilterCutFunction/fr

## Description

Affiche les résultats sur une sphère ou un plan traversant le modèle.

<img alt="" src=images/FEM_Function-Cut-Filter-Example.png  style="width   *400px;">

*Un filtre de fonction de découpe avec pour sphère comme fonction de découpe.Le pipeline original est l\'objet semi-transparent.*

## Utilisation

1.  Sélectionnez un [pipeline de résultats](FEM_PostPipelineFromResult/fr.md) précédemment créé.
2.  Lancez la commande soit en    *
    -   Appuyant sur le bouton **<img src="images/FEM_PostFilterCutFunction.svg" width=16px> '''Filtre de fonction de découpe'''**.
    -   Utilisation du menu **Résultats → <img src="images/FEM_PostFilterCutFunction.svg" width=16px> Filtre de fonction de découpe**.
3.  Ajustez les options d\'affichage de **Résultats** comme pour le pipeline [result](FEM_PostPipelineFromResult.md). Vous devrez peut-être masquer le pipeline pour voir l\'effet du filtre dans l\'aperçu.
4.  Soit
    -   S\'il n\'y a pas encore de [fonction de filtre](FEM_PostCreateFunctions/fr.md) définie, appuyez sur le bouton **<img src="images/List-add.svg" width=16px> Créer
** et sélectionnez **<img src="images/Fem-post-geo-plane.svg" width=16px> Plan** ou **<img src="images/Fem-post-geo-sphere.svg" width=16px> Sphère**
    -   Choisissez une fonction de filtrage existante dans la liste. Si nécessaire, ajustez les paramètres de coupe pour vous assurer qu\'elle intersecte le modèle. Notez que les paramètres de coupe modifiés changeront également les paramètres de la fonction de filtrage utilisée.
5.  Les résultats seront affichés sur la surface de la fonction de filtrage.
6.  Cliquez sur le bouton **OK** pour terminer la commande.

**Remarque**    * s\'il n\'existe pas encore de fonction de filtrage, vous ne pouvez définir directement un **champ** après sa création que lorsque <img alt="" src=images/FEM_PostApplyChanges.svg  style="width   *24px;"> [Appliquer les modifications](FEM_PostApplyChanges/fr.md) est activé. Sinon, vous pouvez le faire d\'abord après avoir rouvert le menu du dialogue du filtre.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterCutFunction/fr

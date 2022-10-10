---
- GuiCommand   */fr
   Name   *FEM PostFilterWarp
   Name/fr   *FEM Filtre de visualisation des déformations
   MenuLocation   *Résultats → Filtre de visualisation des déformations
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   SeeAlso   *[Tutoriel FEM](FEM_tutorial/fr.md)
---

# FEM PostFilterWarp/fr


</div>

## Description


<div class="mw-translate-fuzzy">

Affiche la forme déformée du modèle en utilisant un facteur d\'échelle spécifié.


</div>

The result will be the same like with the *Displacement* slider of the [result show](FEM_ResultShow.md) dialog with the difference that the displacement is for the Warp filter in the SI unit meter. For example if you use a [unit system](Preferences_Editor#Units.md) where the length unit is mm and set a displacement factor of 100 in the [result show](FEM_ResultShow.md) dialog, you need to set for the Warp filter a factor of 100.000 to get the same result.

![](images/FEM_Warp-Filter-Example.gif )

*A warp filter of the displacement of a beam clamped on one side.*

## Utilisation


<div class="mw-translate-fuzzy">

1.  Sélectionnez un [pipeline de résultats](FEM_PostPipelineFromResult/fr.md) précédemment créé.
2.  Lancez la commande de l\'une des façons suivantes    *
    -   Appuyez sur le bouton **<img src="images/FEM_PostFilterWarp.svg" width=16px> [Filtre de visualisation des déformations](FEM_PostFilterWarp/fr.md)**.
    -   Sélectionnez l\'option **Résultats → <img src="images/FEM_PostFilterWarp.svg" width=16px> Filtre de visualisation des déformations** dans le menu.
3.  Ajustez les **Résultats** options d\'affichage comme pour le pipeline [result](FEM_PostPipelineFromResult.md). Cachez ce pipeline pour voir l\'effet d\'un filtre Warp.
4.  Spécifiez directement le **Facteur de déformation** ou utilisez le curseur pour le définir. Les champs **Déformation mini** et **Déformation max** vous permettent de régler la plage du curseur.
5.  Cliquez sur le bouton **OK** pour terminer la commande.


</div>





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterWarp/fr

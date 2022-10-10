---
- GuiCommand   */fr
   Name   *FEM PostFilterDataAlongLine
   Name/fr   *FEM Filtre d'écrêtage selon une ligne
   MenuLocation   *Résultats → Filtre d'écrêtage selon une ligne
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   SeeAlso   *[Tutoriel FEM](FEM_tutorial/fr.md)
---

# FEM PostFilterDataAlongLine/fr


</div>

## Description

Trace les valeurs d\'un champ le long d\'une ligne spécifiée.

![](images/FEM_Line-Clip-Filter-Example.png )

*A line clip filter inside a [Region clip filter](FEM_PostFilterClipRegion.md).The Region clip filter is the semi-transparent object.The part of the line outside the Region clip filter is set to a value of zero and therefore appears blue.*

## Utilisation


<div class="mw-translate-fuzzy">

1.  Sélectionnez un [pipeline de résultats](FEM_PostPipelineFromResult/fr.md) précédemment créé.
2.  Lancez la commande de l\'une des façons suivantes    *
    -   Appuyez sur le bouton **<img src="images/FEM_PostFilterDataAlongLine.svg" width=16px> [Filtre d'écrêtage selon une ligne](FEM_PostFilterDataAlongLine/fr.md)**.
    -   Sélectionnez l\'option **Résultats → <img src="images/FEM_PostFilterDataAlongLine.svg" width=16px> Filtre d'écrêtage selon une ligne** dans le menu.
3.  Spécifiez les coordonnées de deux points définissant la ligne le long de laquelle les résultats doivent être évalués. En option, appuyez sur le bouton **Sélectionner les points** et choisissez les points manuellement sur la surface du maillage.
4.  En option, spécifiez la **Résolution**.
5.  Sélectionnez un **Champs** dans la liste déroulante.
6.  Appuyez sur le bouton **Créer un tracé**. Un tracé XY de la valeur du champ en fonction de la longueur de la ligne sera créé dans une fenêtre séparée.
7.  Cliquez sur le bouton **OK** pour terminer la commande.


</div>





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterDataAlongLine/fr

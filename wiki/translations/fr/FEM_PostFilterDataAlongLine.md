---
- GuiCommand:
   Name: FEM PostFilterDataAlongLine
   Name/fr: FEM Filtre d'écrêtage selon une ligne
   MenuLocation: Résultats -> Filtre d'écrêtage selon une ligne
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_PostPipelineFromResult/fr, FEM_tutorial/fr
---

# FEM PostFilterDataAlongLine/fr

## Description

Trace les valeurs d\'un champ le long d\'une ligne spécifiée.

![](images/FEM_Line-Clip-Filter-Example.png )

*Un filtre d\'écrêtage selon une ligne à l\'intérieur d\'un [Filtre d\'écrêtage selon une région](FEM_PostFilterClipRegion/fr.md).Le filtre d\'écrêtage selon une région est l\'objet semi-transparent.La partie de la ligne à l\'extérieur du filtre d\'écrêtage selon une région est définie à une valeur de zéro et apparaît donc en bleu.*



## Utilisation

1.  Sélectionnez un [pipeline de résultats](FEM_PostPipelineFromResult/fr.md) précédemment créé ou un autre filtre.
2.  Lancez la commande soit en :
    -   Appuyant sur le bouton **<img src="images/FEM_PostFilterDataAlongLine.svg" width=16px> '''Filtre d'écrêtage selon une ligne'''**.
    -   Utilisant le menu **Résultats → <img src="images/FEM_PostFilterDataAlongLine.svg" width=16px> Filtre d'écrêtage selon une ligne**.
3.  Spécifiez les coordonnées de deux points définissant la ligne le long de laquelle les résultats doivent être évalués. En option, appuyez sur le bouton **Sélectionner les points** et choisissez les points manuellement sur la surface du maillage.
4.  En option, spécifiez la **Résolution**.
5.  Sélectionnez un **Champs** dans la liste déroulante.
6.  Appuyez sur le bouton **Créer un tracé**. Un tracé XY de la valeur du champ en fonction de la longueur de la ligne sera créé dans une fenêtre séparée.
7.  Cliquez sur le bouton **OK** pour terminer la commande.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterDataAlongLine/fr

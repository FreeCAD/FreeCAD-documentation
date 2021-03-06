---
- GuiCommand   */fr
   Name   *FEM PostFilterClipScalar
   Name/fr   *FEM Filtre d'écrêtage scalaire
   MenuLocation   *Résultats → Filtre d'écrêtage scalaire
   Workbenches   *[FEM](FEM_Workbench/fr.md)
   SeeAlso   *[Tutoriel FEM](FEM_tutorial/fr.md)
---

# FEM PostFilterClipScalar/fr

## Description

Filtre un champ en utilisant une valeur scalaire spécifiée.

## Utilisation

1.  Sélectionnez un [pipeline de résultats](FEM_PostPipelineFromResult/fr.md) précédemment créé.
2.  Lancez la commande de l\'une des façons suivantes    *
    -   Appuyez sur le bouton **<img src="images/FEM_PostFilterClipScalar.svg" width=16px> [Filtre d'écrêtage scalaire](FEM_PostFilterClipScalar/fr.md)**.
    -   Sélectionnez l\'option **Résultats → <img src="images/FEM_PostFilterClipScalar.svg" width=16px> Filtre d'écrêtage scalaire** dans le menu.
3.  Ajustez les options d\'affichage de **Résultats** comme pour le [pipeline de résultats](FEM_PostPipelineFromResult/fr.md). Masquez ce pipeline pour voir l\'effet d\'un Filtre d\'écrêtage scalaire.
4.  Sélectionnez le type **Scalaire** dans la liste déroulante.
5.  Spécifiez la valeur du **Filtre scalaire** directement ou utilisez le curseur.
6.  Par défaut, toutes les régions dont la valeur du champ est inférieure à la valeur spécifiée seront masquées. Sélectionnez l\'option **Inverser l'écrêtage** pour inverser l\'affichage et masquer les régions dont la valeur est supérieure à la valeur spécifiée.
7.  Cliquez sur le bouton **OK** pour terminer la commande.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterClipScalar/fr

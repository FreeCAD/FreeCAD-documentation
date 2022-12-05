---
- GuiCommand:/fr
   Name:FEM PostFilterClipScalar
   Name/fr:FEM Filtre d'écrêtage scalaire
   MenuLocation:Résultats → Filtre d'écrêtage scalaire
   Workbenches:[FEM](FEM_Workbench/fr.md)
   SeeAlso:[FEM Pipeline de résultats](FEM_PostPipelineFromResult/fr.md), [FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM PostFilterClipScalar/fr

## Description

Filtre un champ en utilisant une valeur scalaire spécifiée.

<img alt="" src=images/FEM_Scalar-Clip-Filter-Example.png  style="width:400px;">

*Un résultat de Filtre d\'écrêtage scalaire.Le pipeline original est l\'objet semi-transparent.*

Un filtre scalaire peut être combiné avec d\'autres filtres. Voici par exemple un filtre scalaire sur un [filtre des déformations](FEM_PostFilterWarp/fr.md) (semi-transparent) :

<img alt="" src=images/FEM_Scalar-Clip-Filter-On-Warp-Example.png  style="width:600px;">

## Utilisation

1.  Sélectionnez un [pipeline de résultats](FEM_PostPipelineFromResult/fr.md) précédemment créé ou un autre filtre existant.
2.  Lancez la commande soit en :
    -   Appuyant sur le bouton **<img src="images/FEM_PostFilterClipScalar.svg" width=16px> '''Filtre d'écrêtage scalaire'''**.
    -   Utilisation du menu **Résultats → <img src="images/FEM_PostFilterClipScalar.svg" width=16px> Filtre d'écrêtage scalaire**.
3.  Ajustez les options d\'affichage de **Résultats** comme pour le [pipeline de résultats](FEM_PostPipelineFromResult/fr.md). Masquez ce pipeline pour voir l\'effet d\'un Filtre d\'écrêtage scalaire.
4.  Sélectionnez le type **Scalaire** dans la liste déroulante.
5.  Spécifiez la valeur **Filtre scalaire** directement ou utilisez le curseur.
6.  Par défaut, toutes les régions dont la valeur du champ est inférieure à la valeur spécifiée seront masquées. Sélectionnez l\'option **Inverser l'écrêtage** pour inverser l\'affichage et masquer les régions dont la valeur est supérieure à la valeur spécifiée.
7.  Cliquez sur le bouton **OK** pour terminer la commande.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterClipScalar/fr

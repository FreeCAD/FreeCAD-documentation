---
 GuiCommand:
   Name: FEM CreateElementsSet
   Name/fr: FEM Effacer des éléments
   MenuLocation: Maillage , Effacer des éléments
   Workbenches: FEM_Workbench/fr
   Version: 1.0
   SeeAlso: FEM_tutorial/fr
---

# FEM CreateElementsSet/fr

## Description

Masque les éléments sélectionnés par un polygone dans le maillage FEM ou le maillage des résultats, ce qui permet de supprimer de la vue les parties sélectionnées du maillage et de voir les éléments à l\'intérieur du maillage.



## Utilisation

1.  Sélectionnez un maillage FEM (créé par Netgen/Gmsh ou importé) ou le maillage des résultats dans l\'arborescence.
2.  Sélectionnez l\'option **Maillage → <img src="images/FEM_CreateElementsSet.svg" width=16px> Effacer les éléments** du menu.
3.  Vous pouvez rentrer le nom de l\'objet de l\'outil qui sera créé dans l\'arborescence.
4.  Appuyez sur le bouton **Polygones** et cliquez sur n\'importe quel endroit dans la vue 3D pour définir le polygone de sélection.
5.  Cliquez avec le bouton droit de la souris et sélectionnez *Intérieur* ou *Extérieur* (pour choisir si les éléments à l\'intérieur du polygone de sélection doivent être effacés ou ceux à l\'extérieur) ou *Annuler* si vous voulez quitter l\'outil de sélection polygonale.
6.  Les éléments sélectionnés seront cachés du maillage et le nombre d\'éléments cachés et conservés sera affiché dans la vue rapport.
7.  Cliquez sur le bouton **OK**. Vous remarquerez de nouveaux objets dans l\'arborescence, un objet nommé comme vous l\'avez spécifié (*ElementSet* par défaut) et un objet nommé *NewFemMesh* ou *NewResultMesh* en fonction de la saisie. Dans le cas du maillage des résultats, il y aura également une copie du maillage original nommée *StartResultMesh*. L\'objet *ElementSet* peut être utilisé pour accéder à nouveau à l\'outil.
8.  Pour supprimer les nouveaux objets de l\'arborescence et ne conserver que le maillage original, double-cliquez sur l\'objet *ElementSet* et appuyez sur le bouton **Restaurer**. Le maillage original ne sera pas automatiquement remis en visibilité.



## Remarques

-   Pour masquer d\'autres éléments du même maillage FEM après la première utilisation de l\'outil, vous devez sélectionner manuellement le nouveau maillage (modifié). Ce n\'est pas le cas avec les maillages de résultats.





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > FEM CreateElementsSet/fr

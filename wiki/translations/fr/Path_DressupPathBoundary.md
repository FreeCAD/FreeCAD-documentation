---
 GuiCommand:
   Name: Path DressupPathBoundary
   Name/fr: Path Limitation d'une zone
   MenuLocation: Path , Finition du parcours , Limitation de la zone
   Workbenches: Path_Workbench/fr
   SeeAlso: Path_DressupTag/fr, Path_DressupRampEntry/fr
---

# Path DressupPathBoundary/fr

## Description

L\'outil <img alt="" src=images/Path_DressupPathBoundary.svg  style="width:24px;"> [Limitation d\'une zone](Path_DressupPathBoundary.md) permet de restreindre l\'étendue d\'un parcours à une plus petite partie de l\'objet. Par exemple, restreindre un parcours de contour à une seule face ou une partie du modèle.



## Utilisation

1.  Sélectionnez un parcours tel qu\'un contour, profil ou une opération de poche
2.  Sélectionnez l\'option **Path → Finition du parcours → <img src="images/Path_DressupPathBoundary.svg" width=16px> Limitation de la zone** du menu.

## Options

-   **Créer une boîte**
-   **Créer un cylindre**
-   **Étendre la boîte englobante du modèle** : un moyen très pratique de limiter un parcours consiste à sélectionner cette option et à utiliser des valeurs négatives.
-   **Utiliser le solide existant**

## Limitations

-   L\'option *Créer une boîte* ne définit que les dimensions de la boîte, pas son origine. Pour modifier son origine, il est nécessaire d\'ajuster sa *position* dans la [vue en arborescence](Tree_view/fr.md).





{{Path_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path DressupPathBoundary/fr

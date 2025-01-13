---
 GuiCommand:
   Name: CAM DressupCAMBoundary
   Name/fr: CAM Limitation d'une zone
   MenuLocation: CAM , Finition du parcours , Limiter à une zone
   Workbenches: CAM_Workbench/fr
   SeeAlso: CAM_DressupTag/fr, CAM_DressupRampEntry/fr
---

# CAM DressupPathBoundary/fr

## Description

L\'outil <img alt="" src=images/CAM_DressupPathBoundary.svg  style="width:24px;"> [Limitation d\'une zone](CAM_DressupPathBoundary/fr.md) permet de restreindre l\'étendue d\'un parcours à une plus petite partie de l\'objet. Par exemple, restreindre un parcours de contour à une seule face ou une partie du modèle.



## Utilisation

1.  Sélectionnez un parcours tel qu\'un contour, contournage ou une opération de poche
2.  Sélectionnez l\'option **CAM → Finition du parcours → <img src="images/CAM_DressupPathBoundary.svg" width=16px> Limiter à une zone** du menu.

## Options

-   **Créer une boîte**
-   **Créer un cylindre**
-   **Étendre la boîte englobante du modèle** : un moyen très pratique de limiter un parcours consiste à sélectionner cette option et à utiliser des valeurs négatives.
-   **Utiliser le solide existant**

## Limitations

-   L\'option *Créer une boîte* ne définit que les dimensions de la boîte, pas son origine. Pour modifier son origine, il est nécessaire d\'ajuster sa *position* dans la [vue en arborescence](Tree_view/fr.md).





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM DressupPathBoundary/fr

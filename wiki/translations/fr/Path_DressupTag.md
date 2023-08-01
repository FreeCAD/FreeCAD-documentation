---
- GuiCommand:
   Name:Path DressupTag
   Name/fr:Path Attache
   MenuLocation:Path → Finition du parcours → Attache
   Workbenches:[Path](Path_Workbench/fr.md)
   SeeAlso:[Path Rampe d'entrée](Path_DressupRampEntry/fr.md), [Path Dégagement d'angles](Path_DressupDogbone/fr.md) , [Path Lame rotative](Path_DressupDragKnife/fr.md)
---

# Path DressupTag/fr

## Description

L\'outil <img alt="" src=images/Path_DressupTag.svg  style="width:24px;"> [Attaches](Path_DressupTag/fr.md) ajoute au parcours existant (généralement un parcours de découpe de contour 2D) un certains nombres d\'attaches qui maintiennent la pièce en place. Sans elles, une partie (qui n\'est pas fixée à la base) risque de s\'envoler de manière incontrôlable lors de la coupe finale. Les attaches sont destinées à être cassées à la main (ou à l'aide d'un ciseau) puis ébarbées à la lime.

Une vidéo expliquant cette fonctionnalité est disponible à l\'adresse suivante : <https://www.youtube.com/watch?v=JZ4prlR6sps>



## Utilisation

1.  Sélectionner un contour ou un profil
2.  Sélectionnez l\'option **Path → Finition du parcours → <img src="images/Path_DressupTag.svg" width=16px> Attache** du menu.

## Options

-   **Angle** : contrôle l\'angle de plongée et de remontée lors de la mise en caisse d\'une attache.
-   **Hauteur** : contrôle la hauteur du haut de l\'attache par rapport au bas de la coupe du profil.
-   **Rayon** : rayon du congé de l\'attache.
-   **Facteur de segmentation** : nombre de segments pour obtenir une attache arrondie.
-   **Largeur** : largeur totale de l\'attache.

Les attaches sont automatiquement générées à intervalles réguliers le long du contour, en commençant par le bord le plus grand. Vous avez la possibilité de supprimer celles que vous n\'aimez pas ou de modifier leur emplacement afin qu\'elles apparaissent sur les parties convexes du travail où il sera plus facile de limer la matière en excès.





{{Path_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path DressupTag/fr

---
- GuiCommand:/fr
   Name:Path DressupTag
   Name/fr:Path Languettes de maintien
   MenuLocation:Path → Trajectoires additionelles → Languettes de maintien
   Workbenches:[Path](Path_Workbench/fr.md)
   SeeAlso:[Path Rampe d'entrée](Path_DressupRampEntry/fr.md), [Path Dégagement d'angles](Path_DressupDogbone/fr.md) , [Path Lame rotative](Path_DressupDragKnife/fr.md)
---

# Path DressupTag/fr

## Description

Cet outil ajoute au tracé existant (généralement un tracé de découpe de contour 2D) un certains nombres d\'attaches qui maintiennent la pièce en place. Sans elles, une partie (qui n\'est pas fixée à la base) risque de s\'envoler de manière incontrôlable lors de la coupe finale. Les attaches sont destinées à être cassées à la main (ou à l'aide d'un ciseau) puis ébarbées à la lime.

Une explication vidéo de cette fonctionnalité est donnée à: <https://www.youtube.com/watch?v=JZ4prlR6sps>

## Utilisation

1.  Sélectionnez un objet contour ou profil [Path](Path_Workbench/fr.md)
2.  Cliquez sur l\'élément de menu <img alt="" src=images/Path_Dressup.svg  style="width:16px;"> [Languettes de maintien](Path_DressupTag/fr.md)

## Options

-   Angle - Contrôle l\'angle de plongée et de remontée quand une attache est enclavée.
-   Height - Contrôle la hauteur du haut de l\'attache à partir du bas de la coupe du profil.
-   Radius - Le rayon du congé pour l\'attache.
-   Segmentation Factor - Nombre de segments pour approximer une attache arrondie.
-   Width - Largeur totale de l\'attache.

Les attaches sont automatiquement générées à intervalles réguliers le long du contour, en commençant par le bord le plus grand. Vous avez la possibilité de supprimer celles que vous n\'aimez pas ou de modifier leur emplacement afin qu\'elles apparaissent sur les parties convexes du travail où il sera plus facile de limer la matière en excès.





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path DressupTag/fr

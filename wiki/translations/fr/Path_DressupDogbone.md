---
- GuiCommand:/fr
   Name:Path DressupDogbone
   Name/fr:Path Dégagement des angles
   MenuLocation:Path → Finition du parcours → Dégagement des angles
   Workbenches:[Path](Path_Workbench/fr.md)
   SeeAlso:[Path Attaches](Path_DressupTag/fr.md), [Path Rampe d'entrée](Path_DressupRampEntry/fr.md), [Path Lame rotative](Path_DressupDragKnife/fr.md)
---

# Path DressupDogbone/fr

## Description

L\'outil <img alt="" src=images/Path_DressupDogbone.svg  style="width:24px;"> [Dégagement des angles](Path_DressupDogbone/fr.md) ajoute une finition à un parcours existant en surcoupant les angles intérieurs d\'un profil ou d\'un contour. Une fraise cylindrique ne peut pas couper entièrement un angle aigu sans entrer en collision avec le modèle. Dans certains cas, il peut être préférable de violer le modèle et de s\'assurer que la matière au niveau de l\'angle est enlevée. Cela est particulièrement nécessaire si les pièces doivent se croiser ou s\'imbriquer les unes dans les autres.



## Utilisation

1.  Sélectionnez un contour ou un profil d\'objets [Path](Path_Workbench/fr.md).
2.  Sélectionnez l\'option **Path → Finition du parcours → <img src="images/Path_DressupDogbone.svg" width=16px> Dégagement des angles** du menu.

## Options

-   **Côté** : côté du parcours où la modification sera ajoutée.
-   **Style** : style de surcoupe (Dégagements des angles, Dégagement des angles en T horizontal, Dégagement des angles en T vertical, Dégagement des angles en T à bord court).
-   **Incision** : algorithme à utiliser pour calculer la longueur de la surcoupe.
-   **Personnalisé** : si Incision est sélectionné, la propriété Personnalisé sera utilisée pour définir la longueur.

## Limitations

Pour déterminer le tracé de correction des coins, il faut un segment droit (G1) avant et après le coin où la correction doit être insérée.





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path DressupDogbone/fr

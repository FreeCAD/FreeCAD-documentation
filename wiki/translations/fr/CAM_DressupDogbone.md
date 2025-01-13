---
 GuiCommand:
   Name: CAM DressupDogbone
   Name/fr: CAM Dégagement des angles
   MenuLocation: CAM , Finition du parcours , Dégager des angles
   Workbenches: CAM_Workbench/fr
   SeeAlso: CAM_DressupTag/fr, CAM_DressupRampEntry/fr, CAM_DressupDragKnife/fr
---

# CAM DressupDogbone/fr

## Description

L\'outil <img alt="" src=images/CAM_DressupDogbone.svg  style="width:24px;"> [Dégagement des angles](CAM_DressupDogbone/fr.md) ajoute une finition à un parcours existant en surcoupant les angles intérieurs d\'un profil ou d\'un contour. Une fraise cylindrique ne peut pas couper entièrement un angle aigu sans entrer en collision avec le modèle. Dans certains cas, il peut être préférable de violer le modèle et de s\'assurer que la matière au niveau de l\'angle est enlevée. Cela est particulièrement nécessaire si les pièces doivent se croiser ou s\'imbriquer les unes dans les autres.



## Utilisation

1.  Sélectionnez un contour ou un profil d\'objets [CAM](CAM_Workbench/fr.md).
2.  Sélectionnez l\'option **CAM → Finition du parcours → <img src="images/CAM_DressupDogbone.svg" width=16px> Dégager des angles** du menu.

## Options

-   **Côté** : côté du parcours où la modification sera ajoutée.
-   **Style** : style de surcoupe (Dégagement, Dégagement horizontal, Dégagement vertical, Dégagement long, Dégagement court).
-   **Incision** : algorithme à utiliser pour calculer la longueur de la surcoupe.
-   **Personnalisé** : si Incision est sélectionné, la propriété Personnalisé sera utilisée pour définir la longueur.

## Limitations

Le dégagement des angles nécessite un segment de parcours droit (G1) avant et après le coin où le dégagement doit être mis.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM DressupDogbone/fr

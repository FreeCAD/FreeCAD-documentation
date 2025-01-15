---
 GuiCommand:
   Name: Std TransformManip
   Name/fr: Std Transformer
   MenuLocation: Édition , Transformer
   Workbenches: Tous
   SeeAlso: Std_UserEditMode/fr
---

# Std TransformManip/fr

## Description

La commande **Std Transformer** permet d\'appliquer des incréments de rotation et de translation à un objet.

<img alt="" src=images/Std_TransformManip_Example.png  style="width:400px;">



## Utilisation

1.  Sélectionner un objet avec une propriété **Placement**. Voir [Remarques](#Remarques.md).
2.  Il y a plusieurs façons de lancer la commande :
    -   Sélectionner l\'option **Editer → <img src="images/Std_TransformManip.svg" width=16px> Transformer** dans le menu.
    -   Sélectionner l\'option **<img src="images/Std_TransformManip.svg" width=16px> Transformer** dans le menu contextuel de la [vue en arborescence](Tree_view/fr.md).
    -   Si le [mode d\'édition](Std_UserEditMode/fr.md) est réglé sur **<img src="images/Std_UserEditModeTransform.svg" width=16px> Transformer**, vous pouvez également double-cliquer sur l\'objet dans la vue en arborescence.
3.  Le panneau de tâches **Incréments ** s\'ouvre.
4.  Vous pouvez ajuster les paramètres d\'incrémentation.
5.  Faites une ou plusieurs des choses suivantes :
    -   Appuyer et maintener le bouton gauche de la souris sur une flèche d\'axe et faites glisser l\'objet le long de cet axe.
    -   Appuyer et maintener le bouton gauche de la souris sur un plan et faites glisser l\'objet le long de ce plan.
    -   Appuyer et maintener le bouton gauche de la souris sur une sphère et faites glisser l\'objet pour le faire pivoter autour de cet axe.
6.  Faites l\'une des choses suivantes :
    -   Appuyer sur le bouton **OK** pour confirmer et terminer la commande.
    -   Appuyer sur le bouton **Annuler** pour annuler les transformations appliquées et terminer la commande. {{Version/fr|1.0}}



## Remarques

-   Dès que vous tournez/déplacez l\'objet dans la [vue 3D](3D_view/fr.md), les changements sont appliqués.
-   Certains objets ayant une propriété **Placement**, comme les esquisses, ne peuvent pas être manipulés, de même que les objets attachés à d\'autres objets.
-   Il n\'y a pas de bouton **Annuler** dans {{VersionMinus/fr|0.21}}. Dans ces versions vous pouvez appuyer sur le bouton **OK** et utiliser le <img alt="" src=images/Std_Undo.svg  style="width:16px;"> [Annuler](Std_Undo/fr.md) pour annuler les modifications après coup.



---
⏵ [documentation index](../README.md) > Std TransformManip/fr

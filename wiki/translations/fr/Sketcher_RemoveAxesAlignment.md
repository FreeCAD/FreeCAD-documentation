---
- GuiCommand:/fr
   Name:Sketcher RemoveAxesAlignment
   Name/fr:Sketcher Supprimer l'alignement des axes
   MenuLocation:Esquisse → Outils d'esquisse → Supprimer l'alignement des axes
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**Z** **R**
   Version:0.20
---

# Sketcher RemoveAxesAlignment/fr

## Description

Cet outil supprime les alignements des axes (contraintes <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:16px;"> [horizontales](Sketcher_ConstrainHorizontal/fr.md), <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:16px;"> [verticales](Sketcher_ConstrainVertical/fr.md)) des éléments sélectionnés en essayant de préserver la relation de contrainte.



## Utilisation

1.  Sélectionnez une géométrie avec des alignements des axes, par exemple un [rectangle](Sketcher_CreateRectangle/fr.md).
2.  Appuyez sur le bouton de la barre d\'outils <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:24px;"> **Supprimer l\'alignement des axes**.

Le résultat est que les contraintes (horizontales et verticales) seront supprimées. Dans l\'exemple d\'un rectangle, il reste un rectangle mais devient pivotable.

<img alt="" src=images/SketcherRemoveAxesAlignmentStart.png  style="width:300px;"> 
*Un rectangle sélectionné avec des contraintes horizontales et verticales.*

<img alt="" src=images/SketcherRemoveAxesAlignmentResult.png  style="width:300px;"> 
*Le rectangle après l'utilisation de Supprimer l'alignement des axes.*





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RemoveAxesAlignment/fr

---
- GuiCommand:/fr
   Name:Sketcher RemoveAxesAlignment
   Name/fr:Sketcher Supprimer l'alignement des axes
   MenuLocation:Sketch → Outils d'esquisse → Supprimer l'alignement des axes
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Version:0.20
---

## Description

Cet outil supprime les alignements d\'axe (<img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:16px;"> [Horizontal](Sketcher_ConstrainHorizontal/fr.md), <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:16px;"> [Vertical](Sketcher_ConstrainVertical/fr.md)) des éléments sélectionnés en essayant de préserver la relation de contrainte.

## Utilisation

1.  Sélectionnez une géométrie avec des alignements d\'axes, par exemple un [rectangle](Sketcher_CreateRectangle/fr.md).
2.  Appuyez sur le bouton de la barre d\'outils <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:24px;"> **Modifie les contraintes pour supprimer l\'alignement des axes\...**.

Le résultat est que les contraintes (horizontales et verticales) seront supprimées. Dans l\'exemple d\'un rectangle, il reste un rectangle mais devient pivotable.

<img alt="" src=images/SketcherRemoveAxesAlignmentStart.png  style="width:300px;"> 
*Un rectangle sélectionné avec des contraintes horizontales et verticales.*

<img alt="" src=images/SketcherRemoveAxesAlignmentResult.png  style="width:300px;"> 
*Le rectangle après l'utilisation de Supprimer l'alignement des axes.*





{{Sketcher Tools navi

}} 

---
 GuiCommand:
   Name: Sketcher RemoveAxesAlignment
   Name/fr: Sketcher Supprimer l'alignement des axes
   MenuLocation: Esquisse , Outils d'esquisse , Supprimer l'alignement des axes
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **Z** **R**
   Version: 0.20
---

# Sketcher RemoveAxesAlignment/fr

## Description

L\'outil <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:24px;"> [Sketcher Supprimer l\'alignement des axes](Sketcher_RemoveAxesAlignment/fr.md) supprime l\'alignement des axes des arêtes sélectionnées en remplaçant les contraintes [horizontales](Sketcher_ConstrainHorizontal/fr.md) et [verticales](Sketcher_ConstrainVertical/fr.md) par des contraintes [parallèle](Sketcher_ConstrainParallel/fr.md) et [perpendiculaire](Sketcher_ConstrainPerpendicular/fr.md). Les arêtes peuvent alors être pivotées sans perdre leur relation orthogonale.



## Utilisation

1.  Sélectionnez deux arêtes ou plus avec des contraintes horizontales ou verticales, par exemple un [rectangle](Sketcher_CreateRectangle/fr.md).
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_RemoveAxesAlignment.svg" width=16px> [Supprimer l'alignement des axes](Sketcher_RemoveAxesAlignment/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse → <img src="images/Sketcher_RemoveAxesAlignment.svg" width=16px> Supprimer l'alignement des axes** du menu.
    -   Utilisez le raccourci clavier : **Z** puis **R**.



## Exemple

<img alt="" src=images/SketcherRemoveAxesAlignmentStart.png  style="width:300px;"> 
*Un rectangle sélectionné avec des contraintes horizontales et verticales.*

<img alt="" src=images/SketcherRemoveAxesAlignmentResult.png  style="width:300px;"> 
*Le rectangle après l'utilisation de l'outil.*





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RemoveAxesAlignment/fr

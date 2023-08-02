---
- GuiCommand:
   Name: Assembly3 ConstraintColinear
   Name/fr: Assembly3 Contrainte colinéaire
   Icon: Assembly_ConstraintColinear.svg
   Workbenches: Assembly3_Workbench/fr
---

# Assembly3 ConstraintColinear/fr

## Description

La commande <img alt="" src=images/Assembly_ConstraintColinear.svg  style="width:16px;"> [Contrainte colinéaire](Assembly3_ConstraintColinear/fr.md) contraint deux lignes 2D telles que des lignes non subdivisées réalisées avec l\'atelier Draft en relation avec le plan de travail.

Elle relie les positions des deux lignes 2D de manière à ce que l\'origine du système de coordonnées implicites (ICS) d\'une ligne se trouve sur l\'axe z du SCI de l\'autre ligne, les deux axes z étant orientés dans la même direction.

## Utilisation

1.  Sélectionner deux lignes 2D.
2.  Lancez la commande <img alt="" src=images/Assembly_ConstraintColinear.svg  style="width:16px;"> [Contrainte colinéaire](Assembly3_ConstraintColinear/fr.md) en utilisant :
    -   Le bouton **<img src="images/Assembly_ConstraintColinear.svg" width=16px> [Colinear](Assembly3_ConstraintColinear/fr.md)**.
3.  Appuyez sur le **<img src="images/Assembly3_workbench_icon.svg" width=16px> [Solve constraints](Assembly3_ResolveConstraints/fr.md)** ou sur le bouton **<img src="images/Assembly_QuickSolve.svg" width=16px> [Quick solve](Assembly3_QuickSolve/fr.md)** pour recalculer.

:   

    :   (si **<img src="images/Assembly_AutoRecompute.svg" width=16px> [Auto recompute](Assembly3_AutoRecompute/fr.md)** et **<img src="images/Assembly_SmartRecompute.svg" width=16px> [Smart recompute](Assembly3_SmartRecompute/fr.md)** sont désactivés).

## Remarques

Cet outil accepte également les éléments 3D, par exemple les bords ou les lignes centrales.

-   2D/3D ou 3D/2D : Au lieu de l\'axe z de l\'élément 3D, la projection de cet axe sur le plan de travail de la ligne 2D est utilisée pour positionner les lignes.
-   Les deux 3D : les lignes sont positionnées l\'une par rapport à l\'autre mais je n\'arrive pas à comprendre comment\...



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintColinear/fr

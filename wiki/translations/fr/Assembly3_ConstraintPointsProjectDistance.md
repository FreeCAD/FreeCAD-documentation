---
- GuiCommand:
   Name: Assembly3 ConstraintPointsProjectDistance
   Name/fr: Assembly3 Contrainte distance du point projeté
   Icon: Assembly_ConstraintPointsProjectDistance.svg
   Workbenches: Assembly3_Workbench/fr
---

# Assembly3 ConstraintPointsProjectDistance/fr

## Description

La commande <img alt="" src=images/Assembly_ConstraintPointsProjectDistance.svg  style="width:16px;"> [Contrainte distance du point projeté](Assembly3_ConstraintPointsProjectDistance/fr.md) contraint la distance de deux points 2D par rapport à une ligne droite.

En se basant sur la direction de la ligne (l\'axe z de son système de coordonnées implicites (ICS)), définir la distance de deux points le long de la ligne signifie ajouter la valeur de la distance à la valeur z du premier point pour obtenir la valeur z du second point (et ignorer les valeurs x et y).

## Utilisation

1.  Sélectionner deux points (2D ou 3D).
2.  Sélectionnez une ligne droite (2D ou 3D).
3.  Activez la commande <img alt="" src=images/Assembly_ConstraintPointsProjectDistance.svg  style="width:16px;"> [Contrainte distance du point projeté](Assembly3_ConstraintPointsProjectDistance/fr.md) en utilisant :
    -   Le bouton **<img src="images/Assembly_ConstraintPointsProjectDistance.svg" width=16px> [Points project distance](Assembly3_ConstraintPointsProjectDistance/fr.md)**.
4.  Appuyez sur le bouton **<img src="images/Assembly3_workbench_icon.svg" width=16px> [Solve constraints](Assembly3_ResolveConstraints/fr.md)** ou sur le bouton **<img src="images/Assembly_QuickSolve.svg" width=16px> [Quick solve](Assembly3_QuickSolve/fr.md)** pour recalculer.

:   

    :   (si **<img src="images/Assembly_AutoRecompute.svg" width=16px> [Auto recompute](Assembly3_AutoRecompute/fr.md)** et **<img src="images/Assembly_SmartRecompute.svg" width=16px> [Smart recompute](Assembly3_SmartRecompute/fr.md)** sont désactivés).



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintPointsProjectDistance/fr

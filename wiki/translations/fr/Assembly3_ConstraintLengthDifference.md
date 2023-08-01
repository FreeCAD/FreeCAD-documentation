---
- GuiCommand:
   Name:Assembly3 ConstraintLengthDifference
   Name/fr:Assembly3 Contrainte longueur différence
   Icon:Assembly_ConstraintLengthDifference.svg
   Workbenches:[Assembly3](Assembly3_Workbench/fr.md)
---

# Assembly3 ConstraintLengthDifference/fr

## Description

Cet outil contraint la longueur d\'une ligne 2D comme un segment non fractionné réalisé avec l\'établi Draft par rapport à un plan de travail.

Elle relie la longueur de la ligne 2D à la longueur d\'une autre ligne 2D ou d\'une ligne 3D, par exemple un élément d\'arête droite ou une ligne d\'esquisse.

La valeur de la longueur de la première ligne sélectionnée est égale à la valeur de la longueur de la deuxième ligne plus une valeur de différence.

:   (Ou la valeur de la longueur de la deuxième ligne sélectionnée est égale à la valeur de la longueur de la première ligne moins une valeur de différence).

## Utilisation

1.  Sélectionnez deux lignes, dont l\'une au moins doit être une ligne 2D.
2.  Appuyez sur le bouton **<img src="images/Assembly_ConstraintLengthDifference.svg" width=16px> [Length difference](Assembly3_ConstraintLengthDifference/fr.md)**.
3.  Définissez la valeur **Différence** dans le panneau des propriétés.
4.  Appuyez sur le bouton **<img src="images/Assembly3_workbench_icon.svg" width=16px> [Solve constraints](Assembly3_ResolveConstraints/fr.md)** ou sur le **<img src="images/Assembly_QuickSolve.svg" width=16px> [Quick solve](Assembly3_QuickSolve/fr.md)** pour recalculer

:   

    :   (si **<img src="images/Assembly_AutoRecompute.svg" width=16px> [Auto recompute](Assembly3_AutoRecompute/fr.md)** et **<img src="images/Assembly_SmartRecompute.svg" width=16px> [Smart recompute](Assembly3_SmartRecompute/fr.md)** sont désactivés).



---
![](images/Button_right.svg) [documentation index](../README.md) > Assembly3 ConstraintLengthDifference/fr

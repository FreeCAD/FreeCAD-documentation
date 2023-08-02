---
- GuiCommand:
   Name: Assembly3 ConstraintEqualLineArcLength
   Name/fr: Assembly3 Contrainte égalité longueur d'arc
   Icon: Assembly_ConstraintEqualLineArcLength.svg
   Workbenches: Assembly3_Workbench/fr
---

# Assembly3 ConstraintEqualLineArcLength/fr

## Description

La commande <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg  style="width:16px;"> [Contrainte égalité longueur d\'arc](Assembly3_ConstraintEqualLineArcLength/fr.md) contraint la longueur d\'une ligne 2D comme une ligne non subdivisé faite avec l\'<img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [atelier Draft Workbench](Draft_Workbench/fr.md) en relation avec un <img alt="" src=images/Assembly_Workplane.svg  style="width:16px;"> plan de travail.

Elle relie la longueur de la ligne 2D à la longueur d\'un arc (2D ou 3D ?).

La valeur de la longueur de la ligne sélectionnée est égale à la longueur de l\'arc sélectionné.

Comme je n'ai pas réussi à faire fonctionner cet outil, voici l'énoncé de l'infobulle : 

Ajoutez une contrainte \"EqualLineArcLength\" pour qu\'une ligne ait la même longueur qu\'un arc.

## Utilisation

1.  Sélectionnez la ligne 2D à contraindre.
2.  Sélectionnez un arc 2D pour lire sa valeur de longueur.
3.  Activez la commande <img alt="" src=images/Assembly_ConstraintEqualLineArcLength.svg  style="width:16px;"> [Contrainte égalité longueur d\'arc](Assembly3_ConstraintEqualLineArcLength/fr.md) en utilisant :
    -   
        **<img src="images/Assembly_ConstraintEqualLineArcLength.svg" width=16px> [Equal Line Arc Length](Assembly3_ConstraintEqualLineArcLength/fr.md)
**
        
        .
4.  Appuyez sur le bouton **<img src="images/Assembly3_workbench_icon.svg" width=16px> [Solve constraints](Assembly3_ResolveConstraints/fr.md)** ou sur le bouton **<img src="images/Assembly_QuickSolve.svg" width=16px> [Quick solve](Assembly3_QuickSolve/fr.md)** pour recalculer.

:   

    :   (si **<img src="images/Assembly_AutoRecompute.svg" width=16px> [Auto recompute](Assembly3_AutoRecompute/fr.md)** et **<img src="images/Assembly_SmartRecompute.svg" width=16px> [Smart recompute](Assembly3_SmartRecompute/fr.md)** sont désactivés).

Selon l\'ordre des types de ligne sélectionnés, les **erreurs** suivantes apparaissent :

La contrainte "EqualLineArcLength" exige que le 1er élément soit une arête linéaire.
La contrainte "EqualLineArcLength" exige que le 2ème élément soit une arête d'arc.
La contrainte "EqualLineArcLength" exige que le 2e élément soit une arête circulaire.



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintEqualLineArcLength/fr

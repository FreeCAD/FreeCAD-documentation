---
 GuiCommand:
   Name: Sketcher BSplineInsertKnot
   Name/fr: Sketcher Insérer un nœud
   MenuLocation: Esquisse , Outils d'esquisse des B-splines , Insérer un nœud
   Workbenches: Sketcher_Workbench/fr
   Version: 0.20
   SeeAlso: Sketcher_BSplineIncreaseKnotMultiplicity/fr, Sketcher_BSplineDecreaseKnotMultiplicity/fr
---

# Sketcher BSplineInsertKnot/fr

## Description

L\'outil <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:24px;"> [Sketcher Insérer un nœud dans une B-spline](Sketcher_BSplineInsertKnot/fr.md) insère un nœud dans une [B-spline](B-Splines/fr.md). Si un nœud existe déjà au paramètre spécifié, sa multiplicité est augmentée d\'une unité.



## Utilisation

1.  Sélectionner une B-spline.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **[<img src=images/Sketcher_BSplineInsertKnot.svg style="width:16px"> [Insérer un nœud ](Sketcher_BSplineInsertKnot/fr.md)**.

    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse des B-splines → <img src="images/Sketcher_BSplineInsertKnot.svg" width=16px> Insérer un nœud** du menu.

    -   
        {{Version/fr|1.0}}
        
        : cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_BSplineInsertKnot.svg" width=16px> Insérer un nœud** du menu contextuel.
3.  Déplacez le curseur à l\'endroit désiré.
4.  La position est marquée par un petit cercle et la valeur de son paramètre est indiquée.
5.  Cliquez pour insérer un noeud, ou cliquez sur un noeud existant pour augmenter sa multiplicité.
6.  Cet outil fonctionne toujours en mode continu : il est possible de continuer à insérer des nœuds et/ou d\'augmenter les valeurs de multiplicité.
7.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez l\'outil de création de géométrie ou de contrainte.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineInsertKnot/fr

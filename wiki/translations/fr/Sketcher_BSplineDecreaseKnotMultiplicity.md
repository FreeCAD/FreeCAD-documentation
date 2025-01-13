---
 GuiCommand:
   Name: Sketcher BSplineDecreaseKnotMultiplicity
   Name/fr: Sketcher Diminuer la multiplicité d'un nœud
   MenuLocation: Esquisse , Outils d'esquisse des B-splines , Diminuer la multiplicité du nœud
   Workbenches: Sketcher_Workbench/fr
   Version: 0.17
   SeeAlso: Sketcher_BSplineIncreaseKnotMultiplicity/fr
---

# Sketcher BSplineDecreaseKnotMultiplicity/fr

## Description

L\'outil <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:24px;"> [Sketcher Diminuer la multiplicité d\'un nœud](Sketcher_BSplineDecreaseKnotMultiplicity/fr.md) diminue la multiplicité d\'un nœud des [B-splines](B-Splines.md).



## Utilisation

1.  Sélectionnez un nœud d\'une B-spline.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **[<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:16px"> [Diminuer la multiplicité du nœud](Sketcher_BSplineDecreaseKnotMultiplicity/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse des B-splines → <img src="images/Sketcher_BSplineDecreaseKnotMultiplicity.svg" width=16px> Diminuer la multiplicité du nœud** du menu.



## Exemple

Voir [Sketcher Augmenter la multiplicité d\'un nœud](Sketcher_BSplineIncreaseKnotMultiplicity/fr#Exemple.md)



## Remarques

Si vous réduisez la multiplicité d\'un nœud à zéro, le nœud disparaît. Mathématiquement, il apparaît alors zéro fois dans le vecteur nœud, ce qui signifie qu\'il n\'y a plus de fonction de base. Pour comprendre cela, il faut faire un peu de mathématiques, mais c\'est également clair si vous regardez la multiplicité. Par exemple, un nœud de multiplicité 0 sur une B-spline de degré 3 signifie qu\'à la position du nœud, deux courbes de Bézier sont connectées avec une continuité *C^3^*. La dérivée troisième doit donc être égale des deux côtés du nœud. Cependant, pour une courbe de Bézier cubique, cela signifie que les deux côtés doivent faire partie de la même courbe. Il n\'y a donc plus de nœud reliant deux courbes de Bézier.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineDecreaseKnotMultiplicity/fr

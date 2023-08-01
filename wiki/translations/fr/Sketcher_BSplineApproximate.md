---
- GuiCommand:/fr
   Name:Sketcher BSplineApproximate
   Name/fr:Sketcher Convertir en B-spline
   MenuLocation:Esquisse → Outils d'esquisse des B-splines → Convertir la géometrie en B-spline
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Version:0.17
   SeeAlso:[Sketcher B-splines](Sketcher_CompCreateBSpline/fr.md)
---

# Sketcher BSplineApproximate/fr

## Description

Convertit une géométrie compatible, arêtes et courbes, en une B-spline. (voir [cette page](B-Splines/fr.md) pour plus d\'informations sur les B-splines).

<img alt="" src=images/sketcher_BSplineConvertToNurb.png  style="width:400px;"> 
*Différents objets avant conversion.*

<img alt="" src=images/sketcher_BSplineConvertToNurb1.png  style="width:400px;"> 
*Les mêmes objets après avoir été convertis en B-splines.*



## Utilisation

1.  Sélectionnez un ou plusieurs segments d\'esquisse et appuyez sur le bouton de la barre d\'outils **[<img src=images/Sketcher_BSplineApproximate.svg style="width:24px"> [Convertir la géometrie en B-spline](Sketcher_BSplineApproximate/fr.md)**.

Assurez-vous d\'avoir soit le [Degré d\'une B-spline](Sketcher_BSplineDegree/fr.md), [Polygone de contrôle d\'une B-spline](Sketcher_BSplinePolygon/fr.md), [Peigne de courbure d\'une B-spline](Sketcher_BSplineComb/fr.md), [Multiplicité des nœuds d\'une B-spline](Sketcher_BSplineKnotMultiplicity/fr.md) de la spline ou son [Poids des points de contrôle B-spline](Sketcher_BSplinePoleWeight/fr.md) visible, sinon rien ne semble se passer. Si vous avez converti des lignes droites, vous devez d\'abord [Augmenter le degré d\'une B-spline](Sketcher_BSplineIncreaseDegree/fr.md) des lignes pour les rendre \"pliables\".





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineApproximate/fr

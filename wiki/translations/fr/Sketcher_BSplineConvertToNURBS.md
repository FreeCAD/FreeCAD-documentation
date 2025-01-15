---
 GuiCommand:
   Name: Sketcher BSplineConvertToNURBS
   Name/fr: Sketcher Convertir en B-splines
   MenuLocation: Esquisse , Outils d'esquisse des B-splines , Convertir la géometrie en B-splines
   Workbenches: Sketcher_Workbench/fr
   Version: 0.17
   SeeAlso: Sketcher_CreateBSpline/fr
---

# Sketcher BSplineConvertToNURBS/fr

## Description

L\'outil <img alt="" src=images/Sketcher_BSplineConvertToNURBS.svg  style="width:24px;"> [Sketcher Convertir en B-splines](Sketcher_BSplineConvertToNURBS/fr.md) convertit les arêtes en [B-splines](B-Splines/fr.md).

<img alt="" src=images/sketcher_BSplineConvertToNurb.png  style="width:300px;"> 
*Différents objets avant conversion.*

<img alt="" src=images/sketcher_BSplineConvertToNurb1.png  style="width:300px;"> 
*Les mêmes objets après avoir été convertis en B-splines.*



## Utilisation

1.  Sélectionnez une ou plusieurs arêtes.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **[<img src=images/Sketcher_BSplineConvertToNURBS.svg style="width:16px"> [Convertir la géometrie en B-splines](Sketcher_BSplineConvertToNURBS/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse des B-splines → <img src="images/Sketcher_BSplineConvertToNURBS.svg" width=16px> Convertir la géométrie en B-splines** du menu.
3.  Les arêtes sont converties.



## Remarques

-   Assurez-vous d\'avoir soit le [Degré d\'une B-spline](Sketcher_BSplineDegree/fr.md), [Polygone de contrôle d\'une B-spline](Sketcher_BSplinePolygon/fr.md), [Peigne de courbure d\'une B-spline](Sketcher_BSplineComb/fr.md), [Multiplicité des nœuds d\'une B-spline](Sketcher_BSplineKnotMultiplicity/fr.md) de la spline ou son [Poids des points de contrôle B-spline](Sketcher_BSplinePoleWeight/fr.md) visible, sinon rien ne semble se passer.
-   Si vous avez converti des lignes droites, vous devez d\'abord [augmenter le degré d\'une B-spline](Sketcher_BSplineIncreaseDegree/fr.md) des lignes pour les rendre \"pliables\".
-   L\'outil ne supprime pas la géométrie interne des [coniques](Sketcher_Workbench/fr#Sketcher_CompCreateConic.md). Elle doit être supprimée manuellement.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineConvertToNURBS/fr

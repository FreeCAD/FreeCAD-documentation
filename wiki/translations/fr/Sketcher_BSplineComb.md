---
- GuiCommand:
   Name: Sketcher BSplineComb
   Name/fr: Sketcher Peigne de courbure d'une B-spline
   MenuLocation: Esquisse -> Outils d'esquisse des B-splines -> Afficher/masquer le peigne de courbure de la B-spline
   Workbenches: Sketcher_Workbench/fr
   Version: 0.17
   SeeAlso: Sketcher_CompCreateBSpline/fr
---

# Sketcher BSplineComb/fr

## Description

Montre ou masque l\'affichage du peigne de courbure d\'une B-spline (voir [cette page](B-Splines/fr.md) pour plus d\'informations sur les B-splines).

Le peigne de courbure indique la courbure (valeur de la dérivée de second ordre) de la B-spline à chaque position. Plus la courbure est élevée à une position, plus le peigne est éloigné de la courbe. Pour les courbures positives (\"tourner vers la droite\"), le peigne se trouve de l\'autre côté de la courbe que pour les courbures négatives.

![](images/sketcher_BSplineCurvatureShow.png ) 
*B-spline avec un point de courbure à sa position médiane - le peigne de courbure là est zéro.*



## Utilisation

1.  Sélectionnez une B-spline
2.  Soit vous utilisez le bouton de la barre d\'outils **[<img src=images/Sketcher_BSplineComb.svg style="width:16px"> [Afficher/Masquer le peigne de courbure B-spline](Sketcher_BSplineComb/fr.md)**
3.  Soit vous utilisez le menu **Esquisse → Outils d'esquisse des B-splines → [<img src=images/Sketcher_BSplineComb.svg style="width:16px"> Afficher/Masquer le peigne de courbure B-spline**.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineComb/fr

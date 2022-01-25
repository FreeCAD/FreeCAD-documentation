---
- GuiCommand:/fr
   Name:Sketcher BSplinePoleWeight
   Name/fr:Sketcher Poids des points de contrôle B-spline
   MenuLocation:Sketch → Outils d'esquisse B-Spline → Poids des points de contrôle B-spline
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Version:0.17
   SeeAlso:[Sketcher B-spline](Sketcher_CompCreateBSpline/fr.md)
---

# Sketcher BSplinePoleWeight/fr

## Description

Affiche ou masque l\'affichage des **poids** pour les points de contrôle d\'une courbe B-spline (voir [ci-dessous](#Explication_de_poids.md) pour une explication des poids).

<img alt="" src=images/sketcher_BSplineWeightShow.png  style="width:468px;"> 
*B-spline avec poids des points de contrôle affichés entre parenthèses*

## Utilisation

1.  Sélectionnez une B-spline et utilisez le bouton de la barre d\'outils **[<img src=images/Sketcher_BSplinePoleWeight.svg style="width:16px"> [Afficher/masquer le poids du point de contrôle de la spline B](Sketcher_BSplinePoleWeight/fr.md)**.

## Explication de poids 

Les B-splines sont essentiellement une combinaison de [courbes de Bézier](B-Splines/fr#Courbes_de_B.C3.A9zier.md) (bien expliqué dans ces vidéos [ici](https://www.youtube.com/watch?v=bE1MrrqBAl8) et [ici](https://www.youtube.com/watch?v=xXJylM2S72s)).

La courbe de Bézier est calculée à l\'aide de cette formule:

$\quad
\textrm{Bezier}(n,t)=\sum_{i=0}^{n}\underbrace{\binom{n}{i}}_{\text{polynomial term}}\underbrace{\left(1-t\right)^{n-i}t^{i}}_{\text{polynomial term}}\; \underbrace{P_{i}}_{\text{point coordinate}}$

*n* est ici le degré de la courbe. Ainsi une courbe de Bézier de degré *n* est un polygone d\'ordre *n*. Les facteurs $P_{i}$ sont ici en fait les coordonnées des points de contrôle des courbes de Bézier. Pour une visualisation, voir [cette page](https://pomax.github.io/bezierinfo/#control).

Le terme poids dans FreeCAD est un peu trompeur car dans la littérature, les facteurs $P_{i}$ sont souvent également appelés poids. Les poids de FreeCAD sont quelque chose de différent. L\'idée de ces poids est de modifier la spline afin que les différents points de contrôle soient \"pondérés\". L\'idée est qu\'un point avec poids 2 devrait avoir deux fois plus d\'influence qu\'un point avec poids 1. Ceci est réalisé en utilisant cette formule différente pour calculer la spline:

$\quad
\mathrm{Rational\ Bezier}(n,t)=\cfrac{\sum_{i=0}^{n}\binom{n}{i}\left(1-t\right)^{n-i}t^{i}w_{i}P_{i}}{\sum_{i=0}^{n}\binom{n}{i}\left(1-t\right)^{n-i}t^{i}w_{i}\;\;\;\,}$

où $w_{i}$ est le poids pour le point $P_{i}$.

Il s\'agit d\'une nouvelle classe de courbes de Bézier car bien que les points soient effectivement pondérés comme souhaité, la courbe n\'est plus un polynôme mais un polynôme fractionnaire. Par conséquent, ces courbes sont appelées courbes de Bézier rationnelles et les B-splines sont alors appelées B-splines rationnelles.

La conséquence est que vous gagnez en flexibilité dans la définition de la forme de la spline. Si tous les poids sont égaux, la forme de la spline ne change pas. Les pondérations les unes par rapport aux autres sont donc importantes, et non la valeur uniquement. Par exemple, cette spline a exactement la même forme que celle de la première image:

<img alt="" src=images/sketcher_BSplineWeightDouble.png  style="width:468px;"> 
*Même B-spline que dans la première image mais avec des valeurs de poids absolues différentes*

Un poids de zéro serait une singularité dans l\'équation pour calculer les courbes de Bézier rationnelles, donc FreeCAD assure qu\'il ne peut pas devenir nul. Néanmoins, les petites valeurs ont le même effet que si le point de contrôle n\'existait presque pas:

<img alt="" src=images/sketcher_BSplineWeightZero.png  style="width:468px;"> 
*Même B-spline avec un point de contrôle de poids presque nul*

## Changer de poids 

La façon de modifier les poids est décrite dans [cette page Wiki](B-Splines#Changing_the_Weight.md).





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplinePoleWeight/fr

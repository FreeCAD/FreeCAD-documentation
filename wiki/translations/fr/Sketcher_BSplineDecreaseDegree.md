---
- GuiCommand:/fr
   Name:Sketcher BSplineDecreaseDegree
   Name/fr:Sketcher Diminuer le degré d'une B-spline
   MenuLocation:Esquisse → Outils d'esquisse des B-splines → Diminuer le degré de la B-spline
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Version:0.19
   SeeAlso:[Sketcher Afficher/masquer degré d'une B-spline](Sketcher_BSplineDegree/fr.md), [Sketcher Augmenter le degré d'une B-spline](Sketcher_BSplineIncreaseDegree/fr.md)
---

# Sketcher BSplineDecreaseDegree/fr

## Description

Diminue le degré (ordre) de la B-spline (voir [cette page](B-Splines/fr.md) pour plus d\'informations sur les B-splines).

Les B-splines sont essentiellement une combinaison de [courbes de Bézier](https://fr.wikipedia.org/wiki/Courbe_de_B%C3%A9zier) (bien expliqué ces vidéos [ici](https://www.youtube.com/watch?v=bE1MrrqBAl8) et [ici](https://www.youtube.com/watch?v=xXJylM2S72s)).

Dans cette spline cubique (degré 3) il y a 3 segments, ce qui signifie que 3 courbes sont reliées à 2 nœuds
(le degré est indiqué par le nombre, l\'indication peut être modifiée à l\'aide du bouton de la barre d\'outils **[<img src=images/Sketcher_BSplineDegree.svg style="width:24px"> [Afficher/masquer le degré B-spline](Sketcher_BSplineDegree/fr.md)**):

<img alt="" src=images/Sketcher_BSplineDegree3.png  style="width:400px;"> 
*Une B-spline de degrés 3 et avec 2 nœuds qui ont chacun la multiplicité 1.*

Les segments extérieurs ont chacun 2 points de contrôle, le point intérieur aucun pour remplir la contrainte que les nœuds ont la multiplicité 1. (voir [cette page](Sketcher_BSplineDecreaseKnotMultiplicity/fr#Description.md) pour une explication de la multiplicité)

La diminution du degré ne supprimera pas les points de contrôle mais tentera à la place de conserver la forme de la spline. Par conséquent, des segments seront ajoutés. Pour notre exemple, vous voyez beaucoup de nouveaux segments de spline avec chacun un point de contrôle et la forme de la spline n\'a été que légèrement modifiée :

<img alt="" src=images/Sketcher_BSplineDegree2.png  style="width:400px;"> 
*Même B-spline où le degré a été changé de 3 à 2. Notez que la multiplicité des nœuds a également été augmentée pour conserver la forme de la spline. En effet, les nœuds ont maintenant une continuité ''C''<sup>0</sup> de sorte que la spline obtienne des "bords" lorsque vous déplacez un point de contrôle. (voir [cette page](Sketcher_BSplineDecreaseKnotMultiplicity/fr#Description.md) pour une explication de la continuité)*

Si vous prenez ce résultat et augmentez le degré, vous ne pouvez pas obtenir l\'état initial de la spline car les informations ont été perdues par la diminution précédente du degré. Pour notre exemple, l\'augmentation du degré conduit à nouveau à ceci :

<img alt="" src=images/Sketcher_BSplineDegree3again.png  style="width:400px;"> 
*Même B-spline où le degré a été changé en arrière de 2 à 3. Notez que la multiplicité des nœuds a également augmenté parce que l'information pour une continuité possible plus élevée a été perdue.*



## Utilisation

1.  Sélectionnez une arête à partir d\'une B-spline existante et appuyez sur **[<img src=images/Sketcher_BSplineDecreaseDegree.svg style="width:24px"> '''Diminuer le degré de la B-spline'''**.





{{Sketcher Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineDecreaseDegree/fr

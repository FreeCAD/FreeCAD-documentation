---
- GuiCommand:
   Name:Sketcher BSplineIncreaseDegree
   Name/fr:Sketcher Augmenter le degré d'une B-spline
   MenuLocation:Esquisse - Outils d'esquisse des B-splines - Augmenter le degré d'une B-spline
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Version:0.17
   SeeAlso:[Sketcher Afficher/masquer degré d'une B-spline](Sketcher_BSplineDegree/fr.md), [Sketcher Diminuer le degré d'une B-spline](Sketcher_BSplineDecreaseDegree/fr.md)
---

# Sketcher BSplineIncreaseDegree/fr

## Description

Augmente le degré (ordre) d\'une B-spline (voir [cette page](B-Splines/fr.md) pour plus d\'informations sur les B-splines).

Les B-splines sont essentiellement une combinaison de [courbes de Bézier](https://fr.wikipedia.org/wiki/Courbe_de_B%C3%A9zier) (bien expliqué ces vidéos [ici](https://www.youtube.com/watch?v=bE1MrrqBAl8) et [ici](https://www.youtube.com/watch?v=xXJylM2S72s)).

Dans cette spline cubique (degré 3) il y a 3 segments, ce qui signifie que 3 courbes sont reliées à 2 nœuds
(le degré est indiqué par le nombre, l\'indication peut être modifiée à l\'aide du bouton de la barre d\'outils **[<img src=images/Sketcher_BSplineDegree.svg style="width:24px"> [Afficher/masquer le degré B-spline](Sketcher_BSplineDegree/fr.md)**) :

<img alt="" src=images/Sketcher_BSplineDegree3.png  style="width:400px;"> 
*Une B-spline de degrés 3 et avec 2 nœuds qui ont chacun la multiplicité 1.*

Les segments extérieurs ont chacun 2 points de contrôle, le point intérieur aucun pour remplir la contrainte que les nœuds ont la multiplicité 1. (voir [cette page](Sketcher_BSplineDecreaseKnotMultiplicity/fr#Description.md) pour une explication de la multiplicité)

Augmenter le degré ajoutera des points de contrôle et la forme de la spline ne sera pas modifiée :

<img alt="" src=images/Sketcher_BSplineDegree4.png  style="width:400px;"> 
*Même B-spline où le degré a été changé de 3 à 4. Notez que la multiplicité des nœuds a également été augmentée.*

Si vous prenez ce résultat et diminuez le degré, vous ne pouvez pas obtenir l\'état initial de la spline car les informations ont été perdues par la diminution précédente du degré. Pour notre exemple, la diminution du degré conduit à nouveau à ceci :

<img alt="" src=images/Sketcher_BSplineDegree3from4.png  style="width:400px;"> 
*Même B-spline où le degré est passé de 4 à 3. Notez que la multiplicité des nœuds a été augmentée. En fonction de la spline, l'algorithme pour diminuer le degré peut ajouter beaucoup de nœuds pour préserver la forme de la spline, comme ici avec cet exemple.*

Vous pouvez voir que maintenant chaque segment a 2 points de contrôle et les nœuds coïncident avec chacun un autre point de contrôle. Les nœuds ont maintenant une continuité *C*^0^ de sorte que la spline obtienne des \"bords\" lorsque vous déplacez un point de contrôle. Ainsi, l\'information d\'une continuité supérieure est perdue. (voir [cette page](Sketcher_BSplineDecreaseKnotMultiplicity/fr#Description.md) pour une explication de la continuité)



## Utilisation

1.  Sélectionnez une arête à partir d\'une B-spline existante et appuyez sur **[<img src=images/Sketcher_BSplineIncreaseDegree.svg style="width:24px"> '''Augmenter le degré de la B-spline'''**.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineIncreaseDegree/fr

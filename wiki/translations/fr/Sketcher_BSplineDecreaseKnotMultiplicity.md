---
 GuiCommand:
   Name: Sketcher BSplineDecreaseKnotMultiplicity
   Name/fr: Sketcher Diminuer la multiplicité d'un nœud
   MenuLocation: Esquisse , Outils d'esquisse des B-splines , Diminuer la multiplicité de noeuds
   Workbenches: Sketcher_Workbench/fr
   Version: 0.17
   SeeAlso: Sketcher_BSplineKnotMultiplicity/fr, Sketcher_BSplineIncreaseKnotMultiplicity/fr
---

# Sketcher BSplineDecreaseKnotMultiplicity/fr

## Description

Diminue la multiplicité de nœuds d\'une B-spline (voir [cette page](B-Splines/fr.md) pour plus d\'informations sur les B-splines).

Les B-splines sont essentiellement une combinaison de [courbes de Bézier](B-Splines/fr#Courbes_de_B.C3.A9zier.md) (bien expliqué dans ces vidéos [ici](https://www.youtube.com/watch?v=bE1MrrqBAl8) et [ici](https://www.youtube.com/watch?v=xXJylM2S72s)). Les points où deux courbes de Bézier sont connectées pour former la spline sont appelés nœuds. Un nœud sur une spline de degré *d* avec la multiplicité *m* signifie que la courbe à gauche et à droite du nœud a au moins une dérivée d\'ordre égale à *n* (appelée *C*^*n*^ continuité) alors que $n=d-m$.
Voici une spline cubique ($d=3$) dont les nœuds ont la multiplicité 1. La multiplicité est indiquée par le nombre entre parenthèses. L\'indication peut être modifiée à l\'aide du bouton de la barre d\'outils **[<img src=images/Sketcher_BSplineKnotMultiplicity.svg style="width:24px"> [Afficher/masquer la multiplicité des nœuds B-spline](Sketcher_BSplineKnotMultiplicity/fr.md)** :

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity1.png  style="width:400px;"> 
*B-spline où deux nœuds ont la multiplicité 1.*

Une multiplicité de 3 changera cette spline de sorte que même les dérivées du premier ordre ne soient pas égales (continuité *C*^0^). Voici la même spline où la multiplicité des nœuds de gauche a été augmentée à 3 :

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity3.png  style="width:400px;"> 
*B-spline d'en haut avec une multiplicité de nœuds 3. Un point de contrôle a été déplacé pour montrer que le nœud a une continuité ''C''<sup>0</sup>.*

Une conséquence d\'une multiplicité plus élevée est que pour le prix de la perte de continuité, vous gagnez le contrôle local. Cela signifie que le changement d\'un point de contrôle affecte uniquement la spline localement à ce point modifié. Cela peut être vu dans cet exemple, où la spline de la première image ci-dessus a été prise et son deuxième point de contrôle du côté droit a été déplacé vers le haut :

<img alt="" src=images/Sketcher_KnotMultiplicity_locality.png  style="width:400px;"> 
*Effet de la localité dû à une multiplicité différente.*

On peut voir que la spline de multiplicité de nœud 1 est complètement modifiée tandis que celle de multiplicité 2 a conservé sa forme à son côté gauche.

**Remarque :** si vous diminuez la multiplicité, le nœud disparaît, car mathématiquement il apparaît alors zéro fois dans le vecteur de nœud, ce qui signifie qu\'il n\'y a plus de fonction de base. Comprendre cela, nécessite quelques maths, mais cela sera aussi clair quand on regarde la multiplicité: Par exemple degré = 3 puis multiplicité = 0 signifie qu\'à la position du nœud deux pièces de Bézier sont reliées avec une continuité *C*^3^. La troisième dérivé doit donc être égal des deux côtés du nœud. Cependant, pour une courbe de Bézier cubique (c\'est-à-dire un polynôme de degré 3), cela signifie que les deux côtés doivent faire partie de la même courbe. Il n\'y a donc plus de nœud reliant 2 courbes de Bézier différentes, l\'ancien nœud est alors simplement un point sur une courbe de Bézier.



## Utilisation

1.  Sélectionnez un nœud B-spline, soit :
    -   Par le bouton **[<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:16px"> [Diminuer la multiplicité des nœuds](Sketcher_BSplineDecreaseKnotMultiplicity/fr.md)**.
    -   Par le menu **Esquisse → Outils d'esquisse des B-splines → [<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:16px"> Diminuer la multiplicité de nœud**.

**Remarque :** diminuer la multiplicité de 1 à 0 supprimera le nœud car le résultat serait une courbe avec un \"bord\" à la position du nœud (continuité *C*^0^) et cela n\'est pas pris en charge. (Pour créer des courbes par un \"bord\", vous pouvez créer deux splines et les relier.)





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineDecreaseKnotMultiplicity/fr

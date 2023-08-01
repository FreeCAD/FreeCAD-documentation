---
- GuiCommand:
   Name:Sketcher BSplineIncreaseKnotMultiplicity
   Name/fr:Sketcher Augmenter la multiplicité d'un nœud
   MenuLocation:Esquisse → Outils d'esquisse des B-splines → Augmenter la multiplicité de noeuds
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Version:0.17
   SeeAlso:[Sketcher Multiplicité des nœuds d'une B-spline](Sketcher_BSplineKnotMultiplicity/fr.md), [Sketcher Diminuer la multiplicité d'un nœud](Sketcher_BSplineDecreaseKnotMultiplicity/fr.md)
---

# Sketcher BSplineIncreaseKnotMultiplicity/fr

## Description

Augmente la multiplicité de nœuds d\'une B-spline (voir [cette page](B-Splines/fr.md) pour plus d\'informations sur les B-splines).

Les B-splines sont essentiellement une combinaison de [courbes de Bézier](B-Splines/fr#Courbes_de_B.C3.A9zier.md) (bien expliqué dans ces vidéos [ici](https://www.youtube.com/watch?v=bE1MrrqBAl8) et [ici](https://www.youtube.com/watch?v=xXJylM2S72s)). Les points où deux bouts de Bézier sont connectés sont appelés nœuds. Un nœud sur une spline de degré *d* et de multiplicité *m* signifie que la courbe à gauche et à droite du nœud a au moins une dérivée d\'ordre égale à *n* (appelée continuité *C*^*n*^) alors que $n=d-m$.
Voici une spline cubique ($d=3$) dont les nœuds ont la multiplicité 1. La multiplicité est indiquée par le nombre entre parenthèses. L\'indication peut être modifiée à l\'aide du bouton de la barre d\'outils **[<img src=images/_Sketcher_BSplineKnotMultiplicity.svg style="width:24px"> [Afficher/masquer la multiplicité des nœuds B-spline](Sketcher_BSplineKnotMultiplicity/fr.md)** :

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity1.png  style="width:400px;"> 
*B-spline où deux nœuds ont la multiplicité 1.*

Une multiplicité de 3 changera cette spline de sorte que même les dérivées du premier ordre ne soient pas égales (continuité *C*^0^). Voici la même spline où la multiplicité des nœuds de gauche a été augmentée à 3 :

<img alt="" src=images/Sketcher_KnotMultiplicity_multiplicity3.png  style="width:400px;"> 
*B-spline d'en haut avec une multiplicité de nœuds 3. Un point de contrôle a été déplacé pour montrer que le nœud a une continuité ''C''<sup>0</sup>.*

Une conséquence d\'une multiplicité plus élevée est que pour le prix de la perte de continuité, vous gagnez le contrôle local. Cela signifie que le changement d\'un point de contrôle affecte uniquement la spline localement à ce point modifié. Cela peut être vu dans cet exemple, où la spline de la première image ci-dessus a été prise et son deuxième point de contrôle du côté droit a été déplacé vers le haut :

<img alt="" src=images/Sketcher_KnotMultiplicity_locality.png  style="width:400px;"> 
*Effet de la localité dû à une multiplicité différente.*

On peut voir que la spline de multiplicité de nœud 1 est complètement modifiée tandis que celle de multiplicité 2 a conservé sa forme à son côté gauche.



## Utilisation

1.  Sélectionnez un nœud B-spline, soit :
    -   par le bouton **[<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:16px"> [Augmenter la multiplicité des nœuds](Sketcher_BSplineIncreaseKnotMultiplicity/fr.md)**.
    -   par le menu **Esquisse → Outils d'esquisse des B-splines → [<img src=images/_Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:16px"> Augmenter la multiplicité des nœuds**.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineIncreaseKnotMultiplicity/fr

# B-Splines/fr
{{TOCright}}

Cette page décrit comment utiliser les B-splines dans FreeCAD. Elle donne également des informations de base sur ce que sont les B-splines et pour quelles applications elles sont utiles.



## Objectif

Si vous connaissez déjà les B-splines et leur application, vous pouvez aller directement à la section [B-splines dans FreeCAD](#B-splines_dans_FreeCAD.md).

Supposons que vous vouliez concevoir une pièce qui doit être produite avec une imprimante 3D. La pièce doit avoir un bord de cette façon :

<img alt="" src=images/B-splines_Motivation-start.png  style="width:450px;">

Vous devez imprimer la pièce dans le sens du bas vers le haut de l\'esquisse. Les structures de support extérieures peuvent ne pas être une option. Vous devez donc ajouter un support directement à votre pièce. Quelles sont vos options ?

-   Option 1 : vous pourriez ajouter une ligne du point (20, 0) au point (80, 40) :

<img alt="" src=images/B-splines_Motivation-line.png  style="width:450px;">

Cependant, cette solution nécessite beaucoup de volume, donc de poids et de matériaux.

-   Option 2 : vous pouvez relier les deux points par un arc de cercle. Pour gagner du volume, l\'arc doit se terminer tangentiellement au point (80,40). Votre solution ressemble alors à ceci :

<img alt="" src=images/B-splines_Motivation-circle.png  style="width:450px;">

OK. Mais au fond, vous n\'avez pas besoin d\'un soutien immédiat.

-   Option 3 : vous pourriez économiser un peu plus de volume si la connexion entre les 2 points est une courbe qui commence tangentiellement à (0, 20) et se termine tangentiellement à (80, 40) :

<img alt="" src=images/B-splines_Motivation-bezier.png  style="width:450px;">

Ainsi, une courbe avec laquelle vous pouvez relier deux points tangentiellement à un point de référence peut être très utile pour les constructions. Les courbes de Bézier offrent cette fonctionnalité.



## Courbes de Bézier 



### Origine

Les courbes de Bézier sont des polynômes permettant de décrire la liaison entre 2 points. Le polynôme le plus simple reliant 2 points est une droite ($A*x^1+B$) donc les courbes de Bézier linéaires sont aussi des segments de droite :

![](images/Bezier_linear_anim.gif ) 
*Animation 1 : courbe de Bézier linéaire.*

Cependant un polynôme devient utile quand on peut le contrôler. Il doit donc y avoir un point entre les deux extrémités qui nous permet de définir comment les extrémités sont connectées. Comme dans l\'exemple ci-dessus, option 3, la courbe est utile lorsqu\'elle commence et se termine tangentiellement aux lignes qui croisent les points d\'extrémité. C\'est l\'une des principales caractéristiques des courbes de Bézier. Ajoutons donc un point de contrôle entre les deux extrémités. La courbe commencera tangentiellement vers ce point de contrôle, ce qui signifie qu\'elle est tangente à la ligne que nous pouvons tracer entre le point de départ et le point de contrôle. En reculant à partir du point d\'extrémité, la courbe sera également tangente à la ligne que nous pouvons tracer entre le point de contrôle et le point d\'extrémité. L\'animation 2 montre à quoi ressemble une telle courbe.

![](images/Bezier_quadratic_anim.gif ) 
*Animation 2 : courbe de Bézier quadratique. P1 est le point de contrôle.*

L\'animation montre clairement ce qu\'est la courbe - une transition de P0 à P2 en faisant pivoter la ligne P0-P1 pour qu\'elle devienne la ligne P1-P2. Nous obtenons ainsi la caractéristique de début/fin tangentielle.

Une telle courbe ne peut être décrite que par un polynôme quadratique. (Le nombre de tours gauche/droite + 1 est l\'ordre polynomial nécessaire. Un polynôme quadratique a un seul tour, un polynôme cubique a deux tours et ainsi de suite). Par conséquent, une courbe de Bézier avec un point de contrôle est une courbe de Bézier quadratique (deuxième ordre).

Avoir un seul point de contrôle n\'est souvent pas suffisant. Prenons l\'exemple de la simulation ci-dessus. Dans l\'option 3, nous terminons la courbe de manière tangentielle dans la direction x. Mais comment relier les points (20, 0) et (80, 40) pour que la courbe se termine de manière tangentielle dans la direction des y ? Pour y parvenir, il faut d\'abord un virage à droite, puis un virage à gauche, donc un polynôme cubique (du troisième ordre). Et cela signifie que pour une courbe de Bézier, nous avons besoin (ou nous pouvons dire que nous gagnons) un deuxième point de contrôle. L\'animation 3 montre une courbe de Bézier cubique.

![](images/Bezier_cubic_anim.gif ) 
*Animation 3 : courbe de Bézier cubique.*

Pour répondre à la question, la solution avec la terminaison tangentielle de la direction y pour l\'exemple est celle-ci :

<img alt="" src=images/B-splines_Motivation-cubic-bezier.png  style="width:450px;">



### Règles

Dans la dérivation, vous avez peut-être déjà remarqué quelques \"règles\" pour les courbes de Bézier :

-   Le degré polynomial est aussi le degré des courbes.
-   Si vous avez besoin de $n$ tours, vous avez besoin d\'au moins une courbe de Bézier de $n+1$ degré.
-   Une courbe de Bézier commence toujours tangentiellement à la ligne entre le point de départ et le premier point de contrôle (et se termine tangentiellement à la ligne entre le dernier point de contrôle et le point d\'arrivée).

### Math

Si vous souhaitez comprendre le contexte mathématique, voici l\'essentiel.

Une courbe de Bézier est calculée à l\'aide de cette formule :

$\quad
\textrm{Bezier}(n,t)=\sum_{i=0}^{n}\underbrace{\binom{n}{i}}_{\text{terme polynomial}}\underbrace{\left(1-t\right)^{n-i}t^{i}}_{\text{terme polynomial}}\; \underbrace{P_{i}}_{\text{coordonnée du point}}$

*n* est ici le degré de la courbe. Ainsi une courbe de Bézier de degré *n* est un polygone d\'ordre *n*. Les facteurs $P_{i}$ sont ici en fait les coordonnées des points de contrôle des courbes de Bézier. Pour une visualisation, voir [Contrôle des courbures de Bézier](https://pomax.github.io/bezierinfo/#control).

Si vous souhaitez en savoir plus, consultez le site [Les mathématiques des courbes de Bézier](https://pomax.github.io/bezierinfo/#explanation) qui présente une origine joliment animée des mathématiques des courbes de Bézier.



## B-splines 



### Fondamentaux

[Cette vidéo](https://www.youtube.com/watch?v=bE1MrrqBAl8) énumère au début les problèmes pratiques que posent les courbes de Bézier. Par exemple, l\'ajout ou la modification d\'un point de contrôle change toute la courbe. Ces problèmes peuvent être résolus en joignant plusieurs courbes de Bézier. Le résultat est ce qu\'on appelle une spline, en particulier une B-spline (basic spline). La vidéo explique également qu\'une union de courbes de Bézier quadratiques forme une B-spline quadratique uniforme et qu\'une union de courbes de Bézier cubiques forme une B-spline cubique uniforme.

A partir des vidéos, nous pouvons rassembler des \"règles\" utiles pour les B-splines :

-   Le premier et le dernier point de contrôle sont les points de début et de fin de la spline.
-   Comme pour les courbes de Bézier, les splines commencent toujours tangentiellement à la ligne entre le point de départ et le premier point de contrôle (et se terminent tangentiellement à la ligne entre le dernier point de contrôle et le point final).
-   Une union de $S$ courbes de Bézier de degré $D$ possède $S+D$ points de contrôle.
    -   Puisque l\'on travaille dans la plupart des cas avec des B-splines cubiques, nous pouvons alors affirmer que $N$ points de contrôle conduisent à $N-3$ segments de Bézier et à leur tour à $N-4$ points de jonction des segments.
-   Une B-spline de degré $D$ offre en tout point une dérivée d\'ordre $D-1$ continue.
    -   Pour une B-spline cubique, cela signifie que la courbure (dérivée de second ordre) ne change pas lors du passage d\'un segment au suivant. C\'est une caractéristique très utile comme nous le verrons plus tard.

Si vous souhaitez en savoir plus sur les propriétés des B-splines, regardez [cette vidéo](https://www.youtube.com/watch?v=xXJylM2S72s).



#### Base

Étant donné que nous ne présenterons que les bases des B-splines, nous n\'entrerons pas ici dans les détails.

La base construit la spline. En regardant la définition des courbes de Bézier dans la section [Math](#Math.md), on se souvient qu\'une courbe de Bézier est une combinaison linéaire de polynômes avec comme facteur les coordonnées x/y de chacun des points de contrôle. Ces polynômes sont appelés polynômes de Bernstein.

Comme plusieurs courbes de Bézier sont combinées pour former une spline, nous obtenons un ensemble de polynômes de Bernstein formant la spline (ils constituent la base). Comme nous voulons surmonter les limitations mentionnées des courbes de Bézier, nous ne combinons pas géométriquement les différents polynômes de Bernstein des courbes de Bézier, mais définissons les polynômes de Bernstein sur toute la plage géométrique de la spline. Donc nous **ne combinons pas** les courbes de Bézier avec ses polynômes de Bernstein, qui seraient

$$\textrm{Bezier-combinaison}=\begin{cases}
  \sum_{i=0}^{n}P_{i}\cdot B_{i,n}(t), & 0\le t\le1\\\\\N
  \sum_{i=0}^{n}P_{i+n}\cdot B_{i,n}(t-1), & 1\le t\le2\\\\N
\cdots
\end{cases}$$

considérant que $B_{i,n}(t)$ est le i-ième polynôme de Bernstein d\'ordre $n$ et les coefficients $P_{i}$ sont les coordonnées ponctuelles des points de contrôle de la courbe de Bézier. Mais nous utilisons un **ensemble différent de fonctions** qui sont définies sur toute l\'étendue de la spline :

$$\textrm{B-spline}= \sum_{i=0}^{n}p_{i}\cdot N_{i,n}(t)$$.

Remarquez qu\'en général $N_{i,n}(t) \ne B_{i,n}(t)$, et les points de contrôle de Bézier $\{P_1, P_2, \dots\}$ sont différents des points de contrôle de B-spline $\{p_1, p_2, \dots\}$.

Les différents $N_{i,n}(t)$ sont définis par morceaux où l\'intervalle de chaque morceau est l\'intervalle d\'un segment de Bézier.

Lorsque les longueurs de tous les segments $N_{i,n}$ sont égaux, on parle d\'une spline uniforme. (Dans la littérature, cela est souvent dénoté par un temps de parcours égal $t$ par segment).

Pour comprendre comment les $p_{i}$ sont les coordonnées des points de contrôle de la spline B, voyez la première minute de [cette vidéo](https://www.youtube.com/watch?v=dPPTCy4L4rY&list=PL8bSwVy8_IcMvtI70tZoYesCS0hGVO5qd).



#### Vecteur-nœud 

Comme indiqué ci-dessus, les B-splines sont créées à partir de $N_{i,n}$ polynômes par morceaux avec une continuité jusqu\'à une certaine dérivée entre les morceaux. Les points aux extrémité de l\'intervalle de définition du segment sont appelés nœuds. Pour une spline définie sur $k$ pièces, il y a $k+1$ nœuds donnés par le soi-disant *vecteur-nœud* :$\{t_0, t_1, t_2,\dots, t_k\}$ avec $t_0 < t_1 < t_2 < \dots < t_k$.

Le vecteur-nœud comprend les nœuds des $N_{i,n}$ fonctions de base qui définissent la B-spline, voir [cette vidéo](https://www.youtube.com/watch?v=ni5NNPCVvDY). Les fonctions de base d\'une B-spline peuvent être calculées à l\'aide du vecteur-nœud et d\'un algorithme de création, voir [cette vidéo](https://www.youtube.com/watch?v=hrsO45AHtbs).

La dérivée jusqu\'à laquelle la continuité existe est donnée par la multiplicité $m$. Par conséquent, nous pouvons spécifier un vecteur avec la multiplicité pour chaque nœud : $\{m_0, m_1, \dots, m_k\}$. Un nœud sur une spline de degré *d* et de multiplicité *m* indique que la courbe à gauche et à droite du nœud a au moins une dérivée d\'ordre égale à *n* (appelée *C*^*n*^ continuité) avec $n=d-m$.



### B-splines non-uniformes 

La dérivée des B-splines à partir des courbes de Bézier a pour conséquence mathématique que dans les B-splines, chaque morceau polynomial a la même longueur. De telles B-splines sont appelées *uniformes*. Dans le cas plus général, elles peuvent mais ne doivent pas avoir la même longueur. De telles splines *non-uniformes* ont l\'avantage de pouvoir contrôler la proximité des splines par rapport à leur point de contrôle.

Mathématiquement, ceci est réalisé en définissant les différents $N_{i,n}$ morceaux à des intervalles différents. Si par exemple une spline B est définie pour l\'intervalle \[0, 1\], elle est uniforme si toutes ses 5 par exemple sont également définies dans cet intervalle. Si maintenant $N_{1,4}$ est uniquement défini dans l\'intervalle \[0, 0.6\] (en dehors de l\'intervalle, il est fixé à zéro), il est plus court et la spline devient donc non uniforme.

Comme décrit ci-dessus, les paramètres des nœuds sont décrits par le vecteur-nœud. Le vecteur-nœud stocke donc les intervalles de définition. Lorsqu\'une pièce reçoit un autre intervalle, le vecteur-nœud change également, voir [cette vidéo](https://www.youtube.com/watch?v=w-l5R70y6u0) pour une visualisation.



### B-splines rationnelles 

Une autre généralisation peut être faite pour les B-splines en introduisant des poids pour les points de contrôle. De cette façon, il est possible de contrôler \"l\'importance\" d\'un point de contrôle.

L\'équation d\'une telle spline est

$$c(n, t)=\cfrac{\sum_{i=0}^{n}d_{i}N_{i, n}(t)\cdot w_i}{\sum_{i=0}^{n}N_{i, n}(t)\cdot w_i}$$

Remarquez que la fonction n\'est plus un polynôme, mais une fonction rationnelle, et ces splines sont appelées B-splines rationnelles. Observez que lorsque tous les $w_i$ sont égaux, l\'équation se réduit à une B-spline régulière non rationnelle. Donc les B-splines non rationnelles sont un sous-ensemble des B-splines rationnelles.

Les B-splines non uniformes et rationnelles sont souvent appelées **[NURBS](https://fr.wikipedia.org/wiki/NURBS)** et sont largement utilisées dans la modélisation géométrique.



## B-splines dans FreeCAD 

FreeCAD propose de créer des B-splines uniformes ou non-uniformes de n\'importe quel degré en 2D via l\'[atelier Sketcher](Sketcher_Workbench/fr.md).



### Création

Pour créer des B-splines, allez dans une esquisse et utilisez le bouton de la barre d\'outils **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [Sketcher B-spline simple](Sketcher_CreateBSpline/fr.md)**. Ensuite, faites un clic gauche pour définir un point de contrôle, déplacez la souris en faisant un clic gauche pour définir le point de contrôle suivant et ainsi de suite. Enfin, cliquez avec le bouton droit de la souris pour terminer la définition et créer la courbe B-spline.

Par défaut, des splines cubiques uniformes sont créées, sauf qu\'il n\'y a pas assez de points de contrôle pour le faire. Ainsi, lorsque vous créez une B-spline avec seulement 2 points de contrôle, vous obtenez bien sûr une spline qui est une simple courbe de Bézier linéaire, pour 3 points de contrôle vous obtenez une courbe de Bézier quadratique, et enfin avec 5 points de contrôle vous obtenez une B-spline cubique composée de 2 segments de Bézier. {{Version/fr|0.20}} Vous pouvez également utiliser la touche D pendant la création d\'une B-spline pour définir son degré (elle tombera toujours à un degré inférieur si moins de points sont fournis).

Pour créer des B-splines périodiques (B-splines qui forment une courbe fermée), utilisez le bouton de la barre d\'outils **[<img src=images/Sketcher_CreatePeriodicBSpline.svg style="width:16px"> [Sketcher B-spline périodique](Sketcher_CreatePeriodicBSpline/fr.md)**. Il n\'est pas nécessaire de placer le dernier point de contrôle sur le premier car la courbe B-spline sera automatiquement fermée :

![](images/Sketcher_Periodic-B-spline-creation.gif )

Les B-splines peuvent également être générées à partir de segments d\'esquisse existants. Pour ce faire, sélectionnez les éléments et appuyez sur le bouton de la barre d\'outils **[<img src=images/Sketcher_BSplineApproximate.svg style="width:24px"> [Sketcher Convertir en B-spline](Sketcher_BSplineApproximate/fr.md)**.

Lors de la création d\'une courbe B-spline, son degré peut être spécifié en appuyant sur la touche **D**. Ceci permet d\'annuler l\'option par défaut qui consiste à créer une courbe B-spline cubique si possible. {{Version/fr|0.20}}



### Changer le degré 

Pour modifier le degré, sélectionnez la plaine B et utilisez les boutons de la barre d\'outils **[<img src=images/Sketcher_BSplineIncreaseDegree.svg style="width:24px"> [Sketcher Augmenter le degré d'une B-spline](Sketcher_BSplineIncreaseDegree/fr.md)** ou **[<img src=images/Sketcher_BSplineDecreaseDegree.svg style="width:24px"> [Sketcher Diminuer le degré d'une B-spline](Sketcher_BSplineDecreaseDegree/fr.md)**.

**Remarque :** diminuer le degré ne peut pas annuler une augmentation antérieure du degré, voir la page Wiki [Sketcher Diminuer le degré d\'une B-spline](Sketcher_BSplineDecreaseDegree/fr.md) pour une explication.



### Changer la multiplicité des nœuds 

Les points où deux courbes de Bézier sont connectées pour former la B-spline sont appelés nœuds. La multiplicité des nœuds détermine la façon dont les parties de Bézier sont connectées, voir la page Wiki [Sketcher Augmenter la multiplicité d\'un nœud](Sketcher_BSplineIncreaseKnotMultiplicity/fr.md) pour plus de détails.

Pour modifier la multiplicité des nœuds, utilisez les boutons de la barre d\'outils **[<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:24px"> [Sketcher Augmenter la multiplicité d'un nœud](Sketcher_BSplineIncreaseKnotMultiplicity/fr.md)** ou **[<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:24px"> [Sketcher Diminuer la multiplicité d'un nœud](Sketcher_BSplineDecreaseKnotMultiplicity/fr.md)**.

**Remarque :** la création de deux B-splines connectées l\'une à l\'autre ne s\'unira pas en une seule nouvelle B-spline. Leur point de connexion n\'est donc pas un nœud. La seule façon d\'obtenir un nouveau nœud dans une B-spline existante est de diminuer le degré. Cependant, vous risquez d\'obtenir de nombreux nouveaux nœuds. Le meilleur choix est donc de redessiner la B-spline avec plus de points de contrôle.



### Changer le poids 

Autour de chaque point de contrôle, vous voyez un cercle jaune foncé. Son rayon définit le poids du point de contrôle correspondant. Par défaut, tous les cercles ont le rayon *1*. Cela est indiqué par une contrainte de rayon pour le premier cercle du point de contrôle.

Pour créer une B-spline rationnelle, les poids doivent être rendus indépendants. Pour y parvenir, vous pouvez supprimer la contrainte selon laquelle tous les cercles sont égaux, puis définir des contraintes de rayon différentes pour les cercles.

Si aucune contrainte de rayon n\'est définie, vous pouvez également modifier le rayon en le faisant glisser :

![](images/Sketcher_Changing-control-point-weigth-dragging.gif )

Dans l\'exemple du déplacement, vous voyez qu\'un poids élevé attire la courbe vers le point de contrôle, tandis qu\'un poids très faible modifie la courbe comme si le point de contrôle n\'existait presque pas.

Lorsque vous examinez la [fonction de création](#B-splines_rationnelles.md) pour les B-splines rationnelles non uniformes, vous constatez qu\'un poids de zéro entraînerait une division par zéro. Les poids négatifs sont théoriquement possibles, mais ils ne sont pas pris en charge. Par conséquent, vous ne pouvez spécifier que des poids supérieurs à zéro.

**Remarque :** lorsque vous faites glisser des points, des nœuds ou des largeurs, les diamètres des cercles indiquant le poids changeront. Cela est dû au fait que le diamètre dépend de la longueur totale de la B-spline pour des raisons de visualisation. Le poids réel n\'est pas modifié.



### Modification des nœuds 

De nouveaux noeuds peuvent être ajoutés en utilisant le bouton **[<img src=images/Sketcher_BSplineInsertKnot.svg style="width:24px"> [Insérer un nœud dans une B-spline](Sketcher_BSplineInsertKnot/fr.md)**. {{Version/fr|0.20}}

Un nœud est supprimé en diminuant son degré à 0 (c\'est-à-dire en appliquant **[<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:24px"> [Diminuer la multiplicité d'un nœud](Sketcher_BSplineDecreaseKnotMultiplicity/fr.md)** lorsque son degré est de 1).

La modification de la valeur du paramètre d\'un nœud n\'est pas encore prise en charge.



### Information sur l\'affichage 

Comme la forme d\'une spline B ne renseigne pas beaucoup sur ses propriétés, FreeCAD propose [différents outils](Sketcher_Workbench/fr#Outils_d.27esquisse_B-spline.md) pour afficher les propriétés :

+++
| Propriété                  | Bouton de la barre d\'outils                                                                                                                         |
+++
| **Degré**                  |                                                                                                                                       |
|                            | **[<img src=images/Sketcher_BSplineDegree.svg style="width:16px"> [Sketcher Degré d'une B-spline](Sketcher_BSplineDegree/fr.md)**                                      |
|                            |                                                                                                                                                   |
+++
| **Polygone de contrôle**   |                                                                                                                                       |
|                            | **[<img src=images/Sketcher_BSplinePolygon.svg style="width:16px"> [Sketcher Polygone de contrôle d'une B-spline](Sketcher_BSplinePolygon/fr.md)**                     |
|                            |                                                                                                                                                   |
+++
| **Peigne de courbure**     |                                                                                                                                       |
|                            | **[<img src=images/Sketcher_BSplineComb.svg style="width:16px"> [Sketcher Peigne de courbure d'une B-spline](Sketcher_BSplineComb/fr.md)**                             |
|                            |                                                                                                                                                   |
+++
| **Multiplicité des nœuds** |                                                                                                                                       |
|                            | **[<img src=images/Sketcher_BSplineKnotMultiplicity.svg style="width:16px"> [Sketcher Multiplicité des nœuds d'une B-spline](Sketcher_BSplineKnotMultiplicity/fr.md)** |
|                            |                                                                                                                                                   |
+++
| **Poids**                  |                                                                                                                                       |
|                            | **[<img src=images/Sketcher_BSplinePoleWeight.svg style="width:16px"> [Sketcher Poids des points de contrôle B-spline](Sketcher_BSplinePoleWeight/fr.md)**             |
|                            |                                                                                                                                                   |
+++



### Limitations

A l\'heure actuelle (FreeCAD 0.20), il existe quelques limitations lors de l\'utilisation des splines que vous devez connaître :

1.  Vous ne pouvez pas définir de contraintes tangentielles.Dans cet exemple, vous voulez vous assurer que la spline touche la courbe bleue 2 fois tangentiellement.<img alt="" src=images/Sketcher_spline-limit-tangential.png  style="width:450px;">Cela serait utile car la ligne bleue pourrait par exemple être la frontière spatiale de votre dessin.
2.  Vous ne pouvez pas créer une courbe de décalage pour une spline B en utilisant l\'outil [Draft Décalage](Draft_Offset/fr.md).



## Cas d\'utilisation typiques 

Selon les propriétés des B-splines, il y a 3 cas d\'utilisation principaux :

1.  Les courbes qui commencent/se terminent tangentiellement à une certaine direction. L\'exemple [ci-dessus](#Motivation.md) en est un exemple.
2.  Les courbes décrivant des conceptions plus larges et offrant la liberté de changements locaux. Voir [cette exemple](#Conception.md) ci-dessous.
3.  Les courbes qui assurent une certaine continuité (dérivée). Voir [cette exemple](#Continuit.C3.A9_aux_transitions_g.C3.A9om.C3.A9triques.md) ci-dessous.



### Conception

Prenons par exemple le cas où vous concevez le boîtier d\'un mixeur de cuisine. Sa forme souhaitée doit ressembler à celle-ci :

![](images/Sketcher_spline-exmple-mixer-shell.png )

Pour définir la forme extérieure, il est avantageux d\'utiliser une B-spline car lorsque vous modifiez un point de contrôle pour changer la courbure du bas, la courbure du côté et du haut ne sera pas modifiée :

![](images/Sketcher_spline-exmple-mixer-sketch.gif )



### Continuité aux transitions géométriques 

Il existe plusieurs cas où il est physiquement nécessaire d\'avoir une certaine continuité de surface aux transitions géométriques. Prenons par exemple les parois internes d\'un canal de fluide. Lorsque le diamètre du canal change, on ne veut pas avoir de bord car les bords introduiraient des turbulences. Par conséquent, comme dans l\'exemple de [ci-dessus](#Motivation.md), on utilise des splines dans ce but.

Le développement des courbes de Bézier a été initialement déclenché par l\'industrie automobile française. Outre l\'économie de matériaux et la réduction de la traînée du flux d\'air, l\'aspect des voitures devait également être amélioré. Et lorsque vous regardez le design élégant des voitures françaises des années 60 et 70, vous constatez que les courbes de Bézier ont donné un coup de pouce au design automobile.

Prenons par exemple cette tâche dans la conception des voitures : l\'aile de la voiture doit être \"belle\". Voici un croquis de base de notre tâche :

<img alt="" src=images/Spline-Fender-sketch1.svg  style="width:250px;">

\"Avoir un bel aspect\" signifie que le client (potentiel) regarde l\'aile et ne voit pas de reflets lumineux inattendus, ni de changements soudains dans les reflets de la peinture automobile. De quoi avez-vous besoin pour éviter les changements dans les reflets ? Regarder attentivement l\'aile :

<img alt="" src=images/Spline-Fender-sketch2.svg  style="width:300px;"> 
*Dans la zone située au-dessus du bord, l'intensité de la lumière réfléchie est faible (représentée par l'ellipse rouge) car aucune lumière n'est directement réfléchie dans la direction du bord vers l'œil.*

Vous voyez que lorsqu\'il y a un bord, il y a une zone spatiale où la lumière réfléchie a moins d\'intensité et c\'est ce que vous remarquerez en regardant le garde-boue. Pour éviter cela, vous avez besoin d\'un changement continu de la pente de vos éléments de surface. La pente est la dérivée de premier ordre et comme expliqué dans la section [Fondamentaux](#Fondamentaux.md), une B-spline du second degré (quadratique) offre en chaque point une dérivée de premier ordre continue.

Mais est-ce vraiment suffisant ? Au point de transition géométrique, nous avons maintenant la même pente des deux côtés, mais la pente peut changer différemment des deux côtés. Nous avons alors cette situation :

<img alt="" src=images/Spline-Fender-sketch3.svg  style="width:300px;">

Nous avons donc également des zones dans lesquelles l\'intensité de la lumière réfléchie est différente. Pour éviter cela, nous avons besoin au point géométrique de transition d\'une continuité de la dérivée de second ordre et donc d\'une B-spline cubique.



---
![](images/Button_right.svg) [documentation index](../README.md) > B-Splines/fr

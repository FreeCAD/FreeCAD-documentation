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

Les courbes de Bézier sont des polynômes permettant de décrire la liaison entre 2 points. Le polynôme le plus simple reliant 2 points est une droite ($A*x^1+B$) donc les courbes de Bézier linéaires sont aussi linéaires :

![](images/Bezier_linear_anim.gif ) 
*Animation 1 : courbe de Bézier linéaire.*

Cependant un polynôme devient d\'abord utile quand on peut le contrôler. Il doit donc y avoir un point entre les deux extrémités qui nous permet de définir comment les extrémités sont connectées. Comme dans l\'exemple ci-dessus, option 3, la courbe est utile lorsqu\'elle commence et se termine tangentiellement aux lignes qui croisent les points d\'extrémité. C\'est l\'une des principales caractéristiques des courbes de Bézier. Ajoutons donc un point de contrôle entre les deux extrémités. La courbe commencera tangentiellement vers ce point de contrôle, ce qui signifie qu\'elle est tangente à la ligne que nous pouvons tracer entre le point de départ et le point de contrôle. En reculant à partir du point d\'extrémité, la courbe sera également tangente à la ligne que nous pouvons tracer entre le point de contrôle et le point d\'extrémité. L\'animation 2 montre à quoi ressemble une telle courbe.

![](images/Bezier_quadratic_anim.gif ) 
*Animation 2 : Courbe de Bézier quadratique. P1 est le point de contrôle.*

L\'animation montre clairement ce qu\'est la courbe - une transition de P0 à P2 en faisant pivoter la ligne P0-P1 pour qu\'elle devienne la ligne P1-P2. Nous obtenons ainsi la caractéristique de début/fin tangentielle.

Une telle courbe ne peut être décrite que par un polynôme quadratique. (Le nombre de tours gauche/droite + 1 est l\'ordre polynomial nécessaire. Un polynôme quadratique a un seul tour, un polynôme cubique a deux tours et ainsi de suite). Par conséquent, une courbe de Bézier avec un point de contrôle est une courbe de Bézier quadratique (deuxième ordre).

Avoir un seul point de contrôle n\'est souvent pas suffisant. Prenons l\'exemple de la simulation ci-dessus. Dans l\'option 3, nous terminons la courbe de manière tangentielle dans la direction x. Mais comment relier les points (20, 0) et (80, 40) pour que la courbe se termine de manière tangentielle dans la direction des y ? Pour y parvenir, il faut d\'abord un virage à droite, puis un virage à gauche, donc un polynôme cubique (du troisième ordre). Et cela signifie que pour une courbe de Bézier, nous avons besoin (ou nous pouvons dire que nous gagnons) un deuxième point de contrôle. L\'animation 3 montre une courbe de Bézier cubique.

![](images/Bezier_cubic_anim.gif ) 
*Animation 3: Courbe de Bézier cubique.*

Pour répondre à la question, la solution avec la terminaison tangentielle de la direction y pour l\'exemple est celle-ci :

<img alt="" src=images/B-splines_Motivation-cubic-bezier.png  style="width:450px;">

### Math

Si vous souhaitez comprendre le contexte mathématique, voici l\'essentiel.

Une courbe de Bézier est calculée à l\'aide de cette formule :

$\quad
\textrm{Bezier}(n,t)=\sum_{i=0}^{n}\underbrace{\binom{n}{i}}_{\text{terme polynomial}}\underbrace{\left(1-t\right)^{n-i}t^{i}}_{\text{terme polynomial}}\; \underbrace{P_{i}}_{\text{coordonnée du point}}$

*n* est ici le degré de la courbe. Ainsi une courbe de Bézier de degré *n* est un polygone d\'ordre *n*. Les facteurs $P_{i}$ sont ici en fait les coordonnées des points de contrôle des courbes de Bézier. Pour une visualisation, voir [Contrôle des courbures de Bézier](https://pomax.github.io/bezierinfo/#control).

Si vous souhaitez en savoir plus, consultez le site [Les mathématiques des courbes de Bézier](https://pomax.github.io/bezierinfo/#explanation) qui présente une origine joliment animée des mathématiques des courbes de Bézier.

### Règles

Dans le texte ci-dessus, vous avez peut-être déjà remarqué quelques \"règles\" pour les courbes de Bézier :

-   Le degré polynomial est aussi le degré des courbes.
-   Si vous avez besoin de $n$ tours, vous avez besoin d\'au moins une courbe de Bézier de $n+1$ degré.
-   Une courbe de Bézier commence toujours tangentiellement à la ligne entre le point de départ et le premier point de contrôle (et se termine tangentiellement à la ligne entre le dernier point de contrôle et le point d\'arrivée).

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

Si vous souhaitez en savoir plus sur les propriétés des B-splines, regardez la vidéo [MOOC Curves 8.2 : Propriétés des courbes B-spline](https://www.youtube.com/watch?v=xXJylM2S72s).

### Base

Le nom *B-spline* signifie *Basis spline*. Au lieu de former la spline comme une combinaison de courbes de Bézier, l\'approche consiste à modéliser **la même spline** d\'une manière différente. L\'idée est donc d\'utiliser un autre ensemble de polynômes comme base. Une combinaison linéaire de ces polynômes de base $B_D(t)$ avec l\'ordre $D$ forme la B-spline. [Cette vidéo](https://www.youtube.com/watch?v=dPPTCy4L4rY) explique la transition entre les points de contrôle de Bézier et les fonctions de base polynomiales décrivant la spline. Mathématiquement, nous pouvons décrire une B-spline avec cette formule :

$\quad
c(t)=\sum_{k=0}^{N}p_{k}B_{k, D}(t)$

Par conséquent, $p_k$ est le $k$-ème point de contrôle de la B-spline et également un facteur pour le $k$-ème polynôme de base $B_{k, D}(t)$. Chaque polynôme de base décrit la spline dans une certaine région et, par conséquent, le déplacement d\'un point de contrôle n\'affecte pas la spline entière. Pour comprendre cela, il est fortement recommandé de jeter un œil à [cette vidéo](https://www.youtube.com/watch?v=vjTyWIKviNc) à partir de la minute 2:23.

Comme expliqué dans la vidéo, les polynômes de base sont des polynômes de Bernstein. L\'ensemble des polynômes de base pour une certaine B-spline peut être visualisé de cette façon :

![](images/Bernstein_Polynomials.svg ) 
*Un ensemble de polynômes de Bernstein d'ordre 4. Ils décrivent une B-spline d'ordre 4 avec 5 points de contrôle.*

À chaque position de la spline $t$, la somme des polynômes est égale à 1 (indiquée par la ligne orange). Au départ, seul le polynôme rouge a une influence puisque tous les autres polynômes sont à 0. À $t$ plus grand, la spline est décrite par une combinaison linéaire de différents polynômes de base. Dans l\'image ci-dessus, chaque polynôme est supérieur à 1 pour toute la plage $0 < t < 1$. Ce n\'est pas nécessairement le cas. Comme le montre la vidéo, les polynômes de base ne sont fondamentalement supérieurs à 0 que pour une certaine plage de position de la spline. L\'intervalle pour lequel un polynôme de base est supérieur à 0 est décrit par le *vecteur nœud*. Si vous souhaitez en savoir plus sur le vecteur nœud, consultez le site [cette vidéo](https://www.youtube.com/watch?v=ni5NNPCVvDY).

### B-splines non-uniformes 

Une propriété des polynômes de Bernstein est que lorsque l\'on regarde les différentes parties de Bézier S-spline, la longueur du chemin de chaque partie est la même. (La longueur du chemin est souvent appelée le *temps de parcours*). Comme vous pouvez l\'imaginer, il peut être utile d\'avoir des B-splines dont les parties de Bézier ont des longueurs de chemin différentes. Ceci peut être réalisé en pondérant les différents polynômes :

$\quad
c(t)=\sum_{k=0}^{N}p_{k}B_{k, D}(t)w_k$

$w_k$ est alors le poids du $k$-ème point de contrôle. Lorsque les poids ne sont pas égaux, la B-spline est dite **non-uniforme**.

En particulier lorsque les B-splines doivent être utilisées pour la modélisation 3D, des B-splines normalisées et non uniformes sont nécessaires. La normalisation se fait par une division par les fonctions de base pondérées. Ainsi, lorsque touts les $w_k$ sont égaux, nous obtenons une B-spline uniforme, indépendante du poids lui-même :

$\quad
c(t)=\cfrac{\sum_{k=0}^{N}p_{k}B_{k, D}(t)w_k}{\sum_{k=0}^{N}B_{k, D}(t)w_k}$

Ces B-splines non uniformes et rationnelles (à cause de la division) sont souvent appelées **NURBS**. En regardant leur formule, on voit qu\'elles sont en fait une B-spline avec une base pondérée $R_{k, D}(t)$ :

$\quad
c(t)=\sum_{k=0}^{N}p_{k}R_{k, D}(t)$

alors que

$\quad
R_{k, D}=\cfrac{B_{k,D}(u)w_k}{\sum_{l=1}^N B_{l,D}(t)w_l}$

## B-splines dans FreeCAD 

FreeCAD propose de créer des B-splines uniformes ou non-uniformes de n\'importe quel degré en 2D via l\'[atelier Sketcher](Sketcher_Workbench/fr.md).

### Création

Pour créer des B-splines, allez dans une esquisse et utilisez le bouton de la barre d\'outils **[<img src=images/Sketcher_CreateBSpline.svg style="width:16px"> [Sketcher Créer une B-spline](Sketcher_CreateBSpline/fr.md)**. Ensuite, faites un clic gauche pour définir un point de contrôle, déplacez la souris en faisant un clic gauche pour définir le point de contrôle suivant et ainsi de suite. Enfin, cliquez avec le bouton droit de la souris pour terminer la définition et créer la courbe B-spline.

Par défaut, des splines cubiques uniformes sont créées, sauf qu\'il n\'y a pas assez de points de contrôle pour le faire. Ainsi, lorsque vous créez une B-spline avec seulement 2 points de contrôle, vous obtenez bien sûr une spline qui est une simple courbe de Bézier linéaire, pour 3 points de contrôle vous obtenez une courbe de Bézier quadratique, puis avec 5 points de contrôle vous obtenez une B-spline cubique composée de 2 segments de Bézier.

Pour créer des B-splines périodiques (B-splines qui forment une courbe fermée), utilisez le bouton de la barre d\'outils **[<img src=images/Sketcher_CreatePeriodicBSpline.svg style="width:16px"> [Sketcher Créer une B-spline périodique](Sketcher_CreatePeriodicBSpline/fr.md)**. Il n\'est pas nécessaire de placer le dernier point de contrôle sur le premier car la courbe B-spline sera automatiquement fermée :

![](images/Sketcher_Periodic-B-spline-creation.gif )

Les B-splines peuvent également être générées à partir de segments d\'esquisse existants. Pour ce faire, sélectionnez les éléments et appuyez sur le bouton de la barre d\'outils **[<img src=images/Sketcher_BSplineApproximate.svg style="width:24px"> [Sketcher Convertir la géométrie en B-spline](Sketcher_BSplineApproximate/fr.md)**.

Lors de la création d\'une courbe B-spline, son degré peut être spécifié en appuyant sur la touche **D**. Ceci permet d\'annuler l\'option par défaut qui consiste à créer une courbe B-spline cubique si possible. {{Version/fr|0.20}}

### Changer le degré 

Pour modifier le degré, sélectionnez la plaine B et utilisez les boutons de la barre d\'outils **[<img src=images/Sketcher_BSplineIncreaseDegree.svg style="width:24px"> [Sketcher Augmenter le degré d'une B-spline](Sketcher_BSplineIncreaseDegree/fr.md)** ou **[<img src=images/Sketcher_BSplineDecreaseDegree.svg style="width:24px"> [Sketcher Diminuer le degré d'une B-spline](Sketcher_BSplineDecreaseDegree/fr.md)**.

**Remarque :** diminuer le degré ne peut pas annuler une augmentation antérieure du degré, voir la page Wiki [Sketcher Diminuer le degré d\'une B-spline](Sketcher_BSplineDecreaseDegree/fr.md) pour une explication.

### Changer la multiplicité des nœuds 

Les points où deux courbes de Bézier sont connectées pour former la B-spline sont appelés nœuds. La multiplicité des nœuds détermine la façon dont les parties de Bézier sont connectées, voir la page Wiki [Sketcher Plus de nœuds d\'une B-spline](Sketcher_BSplineIncreaseKnotMultiplicity/fr.md) pour plus de détails.

Pour modifier la multiplicité des nœuds, utilisez les boutons de la barre d\'outils **[<img src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg style="width:24px"> [Sketcher Plus de nœuds d'une B-spline](Sketcher_BSplineIncreaseKnotMultiplicity/fr.md)** ou **[<img src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg style="width:24px"> [Sketcher Moins de nœuds d'une B-spline](Sketcher_BSplineDecreaseKnotMultiplicity/fr.md)**.

**Remarque :** la création de deux B-splines connectées l\'une à l\'autre ne s\'unira pas en une seule nouvelle B-spline. Leur point de connexion n\'est donc pas un nœud. La seule façon d\'obtenir un nouveau nœud dans une B-spline existante est de diminuer le degré. Cependant, vous risquez d\'obtenir de nombreux nouveaux nœuds. Le meilleur choix est donc de redessiner la B-spline avec plus de points de contrôle.

### Changer le poids 

Autour de chaque point de contrôle, vous voyez un cercle jaune foncé. Son rayon définit le poids du point de contrôle correspondant. Par défaut, tous les cercles ont le rayon *1*. Cela est indiqué par une contrainte de rayon pour le premier cercle du point de contrôle.

Pour créer une courbe B-spline non uniforme, les poids doivent être non uniformes. Pour cela, vous pouvez modifier la contrainte [Sketcher Rayon](Sketcher_ConstrainRadius/fr.md) du premier cercle du point de contrôle :

![](images/Sketcher_Changing-control-point-weigth-constraint.gif )

ou vous supprimez la contrainte selon laquelle tous les cercles sont égaux, puis vous définissez des contraintes de rayon différentes pour les cercles.

Si aucune contrainte de rayon n\'est définie, vous pouvez également modifier le rayon en le faisant glisser :

![](images/Sketcher_Changing-control-point-weigth-dragging.gif )

Dans l\'exemple du déplacement, vous voyez qu\'un poids élevé attire la courbe vers le point de contrôle, tandis qu\'un poids très faible modifie la courbe comme si le point de contrôle n\'existait presque pas.

Lorsque vous consultez la [fonction de création](#B-splines_non-uniformes.md) pour les B-splines rationnelles non uniformes, vous constatez qu\'un poids de zéro entraînerait une division par zéro. Par conséquent, vous ne pouvez spécifier que des poids supérieurs à zéro.

### Modification des nœuds 

De nouveaux noeuds peuvent être ajoutés en utilisant le bouton **[<img src=images/Sketcher_BSplineInsertKnot.svg style="width:24px"> [Insérer un nœud dans une B-spline](Sketcher_BSplineInsertKnot/fr.md)**. {{Version/fr|0.20}}

La suppression des nœuds n\'est pas encore possible, voir la section [Limitations](#Limitations.md).

### Information sur l\'affichage 

Comme la forme d\'une spline B ne renseigne pas beaucoup sur ses propriétés, FreeCAD propose [différents outils](Sketcher_Workbench/fr#Outils_d.27esquisse_B-spline.md) pour afficher les propriétés :

+++
| Propriété                  | Bouton de la barre d\'outils                                                                                                                         |
+++
| **Degré**                  |                                                                                                                                       |
|                            | **[<img src=images/Sketcher_BSplineDegree.svg style="width:16px"> [Sketcher Degré d'une BSpline](Sketcher_BSplineDegree/fr.md)**                                       |
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

A l\'heure actuelle (FreeCAD 0.19), il existe quelques limitations lors de l\'utilisation des splines que vous devez connaître :

1.  Vous ne pouvez pas définir de contraintes tangentielles.Dans cet exemple <img alt="" src=images/Sketcher_spline-limit-tangential.png  style="width:450px;">vous voulez vous assurer que la spline touche la courbe bleue 2 fois tangentiellement. Cela serait utile car la ligne bleue pourrait par exemple être la frontière spatiale de votre dessin.
2.  Vous ne pouvez pas insérer un nouveau point de contrôle entre deux points de contrôle existants sélectionnés. Il n\'y a pas d\'autre moyen que de redessiner la spline.
3.  Vous ne pouvez pas supprimer un point de contrôle. Dans ce cas également, vous devez redessiner la spline.
4.  Vous ne pouvez pas créer une courbe de décalage pour une spline B en utilisant l\'outil [Draft Décalage](Draft_Offset/fr.md).

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
![](images/Right_arrow.png) [documentation index](../README.md) > B-Splines/fr

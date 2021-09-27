# Plot MultiAxes tutorial/fr
{{TutorialInfo/fr
|Topic=Atelier Plot
|Level=Intermediaire
|Time=
|Author=
|FCVersion=0.19
|Files=
}}


<div class="mw-translate-fuzzy">

Assurez-vous d\'avoir lu le [tutoriel de base](Plot_Basic_tutorial/fr.md) avant de commencer avec ce tutoriel. Dans ce didacticiel, nous allons apprendre à créer et à modifier un tracé multiaxes. Vous pouvez en savoir plus sur l\'[Atelier Plot ici](Plot_Module/fr.md).


</div>

<img alt="" src=images/Plot_MultiAxes_Example.png  style="width:600px;">


<div class="mw-translate-fuzzy">

<img alt="exemple Multiaxes Plot" src=images/Plot_MultiAxes_Example.png  style="width:480px;">


<center>

exemple Plot Multiaxes.


</center>


</div>


<div class="mw-translate-fuzzy">

Dans l\'image précédente, vous pouvez voir le résultat que nous obtiendrons approximativement. Après ce tutoriel, vous apprendrez:

-   Comment créer un graphique multi-axes à partir de la console Python.
-   Comment modifier les propriétés des axes.
-   Comment contrôler la grille/légende lorsque plusieurs axes sont présents.
-   Comment modifier les étiquettes, les titres et les positions des légendes.


</div>

## Plotting data 


<div class="mw-translate-fuzzy">

## Traceur de données 

Comme nous l\'avons fait dans le [tutoriel précédent](Plot_Basic_tutorial/fr.md), nous utiliserons la console Python intégrée ou des [macros](Macros/fr.md) afin de tracer les données, à la différence que dans ce cas nous tracerons les données sur deux axes différents.


</div>

### Creating plot data 


<div class="mw-translate-fuzzy">

### Création de données Plot 

Dans cet exemple, nous allons tracer 3 fonctions, deux utilisées dans le [Tutoriel de base](Plot_Basic_tutorial/fr.md) et un polynôme. Le fait est que le polynôme aura besoin de nouveaux axes car la plage de variation est différente de toutes les autres. Les commandes suivantes créeront des tableaux de données pour nous:


</div>


```python
import math
p = range(0,1001)
x = [2.0*xx/1000.0 for xx in p]
y = [xx**2.0 for xx in x]
t = [tt/1000.0 for tt in p]
s = [math.sin(math.pi*2.0*tt) for tt in t]
c = [math.cos(math.pi*2.0*tt) for tt in t]
```


<div class="mw-translate-fuzzy">

Lorsque *x* passe de 0 à 2, la fonction *y* a une valeur maximale de 4, donc si nous essayons de tracer cette fonction avec des fonctions trigonométriques, au moins une fonction sera tronquée ou mal mise à l\'échelle, alors nous besoin d\'un tracé multiaxes. Le tracé multiaxes dans FreeCAD est orienté pour obtenir un tracé avec plusieurs axes et non pour obtenir plusieurs tracés dans le même document.


</div>

### Drawing functions, adding new axes 


<div class="mw-translate-fuzzy">

### Fonction ajoutant de nouveaux axes de dessin 

Nous allons dessiner une fonction polynomiale sur les axes principaux. Si tous vos axes ont la même taille, il importe peu de savoir quelle fonction est tracée sur quels axes, mais si votre tracé comporte des axes de taille différente (comme dans cet exemple), les axes principaux doivent être les plus grands (car ces axes ont un fond blanc). Pour ce faire, il suffit de lancer une commande


</div>


```python
try:
    from FreeCAD.Plot import Plot
except ImportError:
    from freecad.plot import Plot

Plot.plot(t,s,r"$\sin\left( 2 \pi t \right)$")
Plot.plot(t,c,r"$\cos\left( 2 \pi t \right)$")
```


<div class="mw-translate-fuzzy">

Dans cet exemple, nous transmettons directement l\'étiquette (label) de la série pour la légende. Notez que la chaîne d\'étiquettes, a le préfixe **r**, afin d\'éviter que Python ne tente d\'interpréter les caractères spéciaux (symbole **\\** qui est fréquemment utilisé dans la syntaxe [LaTeX](http://www.latex-project.org)).


</div>


<div class="mw-translate-fuzzy">

Maintenant nous pouvons tracer des fonctions trigonométriques, mais avant, créez de nouveaux axes. Dans **[FreeCAD Plot module](Plot_Module/fr.md)** lorsque vous créez de nouveaux axes, ces axes sont sélectionnés comme actifs, donc, de nouveaux **Plots**, seront associés à ces axes.


</div>


```python
Plot.addNewAxes()
Plot.plot(x,y,r"$x^2$")
```


<div class="mw-translate-fuzzy">

Comme vous pouvez le voir **Plot** est devenu fou, avec axes qui pointes, et, qui s\'empiètent, courbes de même couleur, etc.. .

Maintenant nous avons besoin d\'utiliser **[FreeCAD Plot module](Plot_Module/fr.md)**, avec la complexité de ce graphique.


</div>

## Configurer Plot 

### Configuring axes 


<div class="mw-translate-fuzzy">

### Configurer les axes 

La fonction [FreeCAD Plot module](Plot_Module/fr.md) fournit un outil, pour modifier les propriétés de chacun des axes.


</div>

![](images/Plot_Axes.svg‎ )


<div class="mw-translate-fuzzy">

![Axes configuration tool icon](images/Plot_Axes.svg‎ )


<center>

Axes configuration tool icon.


</center>


</div>


<div class="mw-translate-fuzzy">

La première chose que vous trouverez dans l\'outil, **![](images/)_[Plot_Axes](Plot_Axes/fr.md)**, est le sélecteur d\'axes actif. Pour l\'instant, nous allons travailler sur l\'ensemble des axes 1, la dernière chose que nous générons

Puisque les axes actifs sont les derniers, les axes actifs sont placés en premier.

L\'outil axes, comme l\'outil **![](images/)_[Plot_Labels](Plot_Labels/fr.md)**, permettent de définir les axes actifs, et, permettent de tracer plus de données dans l\'axe que vous souhaitez (y compris ajouter/supprimer des axes). Pour l\'instant, nous allons travailler sur les axes sélectionnés, et, qui sont associés aux fonctions trigonométriques.


</div>


<div class="mw-translate-fuzzy">

Utilisez les ascenseurs pour modifier les réglages, déplaçons le curseur gauche pour les réglages **horizontaux**, et, le curseur du bas pour les réglages **verticaux** (essayez d\'imiter l\'exemple) afin de réduire la taille des axes.

Nous pouvons alors définir l\'alignement des axes, et, changer en haut, et, à droite, en définissant un petit décalage de deux unités.


</div>

### Configuring series 


<div class="mw-translate-fuzzy">

### Configurer les Series 

Pour définir les propriétés des **![](images/)_[Plot_Series](Plot_Series/fr.md)** que nous avons fait, regardez dans [Tutoriel](Plot_Basic_tutorial/fr.md).


</div>

### Showing grid and legend 


<div class="mw-translate-fuzzy">

### Afficher la grille et les légendes 

Les **![](images/)_[Plot_Grid_(grilles)](Plot_Grid/fr.md)**, et, les **![](images/)_[Plot_Legend_(légendes)](Plot_Legend/fr.md)** apparaissent cachées avec les mêmes outils utilisés dans le [tutoriel](Plot_Basic_tutorial/fr.md), mais dans ce cas, le comportement est un peu différent, en raison de la présence de **deux axes différents**.


</div>


<div class="mw-translate-fuzzy">

Concernant les lignes de la grille, vous pouvez, afficher les lignes pour chaque ensemble d\'axes, par exemple, si vous essayez d\'afficher une grille maintenant vous montrerez uniquement la grille des fonctions trigonométriques, donc afin de montrer la grille du tracé de la fonction polynôme, vous avez besoin de mettre les axes actifs à **0** (en utilisant l\'outil de configuration des **![](images/)_[Plot_Axes](Plot_Axes/fr.md)**), pour utiliser l\'outil **![](images/)_[Plot_Grid](Plot_Grid/fr.md)** une autre fois (il faut appuyer une deuxième fois sur l\'outil).


</div>


<div class="mw-translate-fuzzy">

Au sujet de la **![](images/)_[légende_(Plot_Legend)](Plot_Legend/fr.md)**, la légende sera la même pour les deux axes, vous pouvez donc choisir les axes que vous souhaitez, afin d\'afficher la **![](images/)_[légende_(Plot_Legend)](Plot_Legend/fr.md)**, mais il est fortement recommandé, d\'utiliser les plus grands (0 dans cet exemple), parce que la position sera référée, à cet axe de coordonnées.

Il est possible que vous affichiez une légende, et, que cette légende soit très mal placée, patientez un peu, ce problème sera résolu plus tard.


</div>

### Setting axes labels 


<div class="mw-translate-fuzzy">

### Définition des étiquettes axiales 

Vous pouvez définir des étiquettes, et, des axes avec le même outil, utilisé dans [previous Tutoriel](Plot_Basic_tutorial/fr.md), à la différence près, que maintenant vous avez plus d\'axes.

Les étiquettes utilisées sur les axes, sont habituellement, une par axe, il n\'y a pas de différence significative, mais le [Module Plot de FreeCAD](Plot_Module/fr.md) permet de définir un titre en plus par axe.

Dans cet exemple nous ne ne mettons un titre, qu\'aux axes principaux, alors la valeur :


</div>


<div class="mw-translate-fuzzy">

**Axes 0:**

-   Title = Multiaxes example
-   X Label = \$x\$
-   Y Label = \$\\mathrm{f} \\left( x \\right)\$

**Axes 1:**

-   X Label = \$t\$
-   Y Label = \$\\mathrm{f} \\left( t \\right)\$


</div>


<div class="mw-translate-fuzzy">

La valeur de la police est **20** pour tous, sauf le titre, qui utilise une valeur de police de **24**.

Que se passe-t-il avec la légende, et, le titre mal placé, intersection avec le deuxième ensemble d\'axes, donc nous devons résoudre ces deux problèmes.


</div>

### Setting elements position 


<div class="mw-translate-fuzzy">

### Définition de la position des éléments 

[FreeCAD Plot module](Plot_Module/fr.md) fournit un outil pour définir la position de plusieurs éléments, comme, les **![](images/)_[titres_(Series)](Plot_Series/fr.md)**, les **![](images/)_[labels](Plot_Labels/fr.md)**, ou la **![](images/)_[légende](Plot_Legend/fr.md)**.


</div>

![](images/Plot_Positions.svg )


<div class="mw-translate-fuzzy">

![Position editor icon](images/Plot_Positions.svg‎ )


<center>

Position editor icon.


</center>


</div>


<div class="mw-translate-fuzzy">

Lorsque vous exécutez l\'outil, vous voyez une liste, avec tous les éléments modifiables.

Les éléments de titres, ainsi que les légendes, peuvent être déplacés dans les deux sens, les étiquettes des axes, ne peuvent être déplacées uniquement sur l\'orientation des axes.

Sélectionnez le titre des axes **0**, et, déplacez-le vers (**0.24,1.01**), puis sélectionnez la légende, et, déplacez-le dans une meilleure position. Vous pouvez augmenter la dimension de la police.


</div>

## Sauvegarder un fichier Plot 


<div class="mw-translate-fuzzy">

Vous pouvez maintenant enregistrer votre travail. Voir [tutoriel précédent](Plot_Basic_tutorial/fr.md) si vous ne savez pas comment faire.


</div>


{{Tutorials_navi

}} {{Plot_Tools_navi}} 

_ _

---
[documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > Plot MultiAxes tutorial/fr

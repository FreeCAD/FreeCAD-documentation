---
 TutorialInfo:r
   Topic: Atelier Plot
   Level: Intermediaire
   Time: 
   Author: 
   FCVersion: 0.19
   Files: 
---

# Plot MultiAxes tutorial/fr





Veuillez effectuer le [tutoriel de base](Plot_Basic_tutorial/fr.md) avant de commencer avec ce tutoriel. Dans ce didacticiel, nous allons apprendre à créer et à modifier un tracé multiaxes. Vous pouvez en savoir plus sur l\'[Atelier Plot ici](Plot_Workbench/fr.md).

<img alt="" src=images/Plot_MultiAxes_Example.png  style="width:600px;"> 
*Exemple de tracé multiaxe*

Dans l\'image, vous pouvez voir le résultat que nous obtiendrons approximativement. En suivant ce tutoriel, vous apprendrez :

-   Comment créer un graphe multi-axes à partir de la [console Python](Python_console/fr.md).
-   Comment éditer les propriétés des axes.
-   Comment contrôler la grille et la légende lorsque plusieurs ensembles d\'axes sont présents.
-   Comment éditer la position des étiquettes, titres et légendes.



## Traçage des données 

Comme nous l\'avons fait dans le [tutoriel précédent](Plot_Basic_tutorial/fr.md), nous allons utiliser la [console Python](Python_console/fr.md) ou des [macros](Macros/fr.md) pour tracer les données, mais dans ce cas, nous allons tracer les données en utilisant deux ensembles d\'axes.



### Création de données de tracé 

Dans cet exemple, nous allons tracer 3 fonctions, les deux utilisées dans le [tutoriel précédent](Plot_Basic_tutorial/fr.md) et une nouvelle fonction polynomiale. L\'étendue de la fonction polynomiale est différente des autres fonctions, donc de nouveaux axes sont nécessaires. Les commandes suivantes vont créer les tableaux de données pour nous :


```python
import math
p = range(0,1001)
x = [2.0*xx/1000.0 for xx in p]
y = [xx**2.0 for xx in x]
t = [tt/1000.0 for tt in p]
s = [math.sin(math.pi*2.0*tt) for tt in t]
c = [math.cos(math.pi*2.0*tt) for tt in t]
```

Comme *x* se déplace de 0 à 2, la fonction *y* a une valeur maximale de 4, donc si nous essayons de tracer cette fonction avec les fonctions trigonométriques, au moins une fonction sera tronquée ou mal mise à l\'échelle, donc nous avons besoin d\'un tracé multi-axes. Un tracé multiaxe dans FreeCAD est destiné à obtenir un tracé avec plusieurs axes, et non à obtenir plusieurs tracés dans le même document.



### Fonctions de dessin, ajout de nouveaux axes 

Nous allons tracer les fonctions trigonométriques en utilisant les axes principaux. Si tous vos axes ont la même taille, il n\'est pas important de savoir quelle fonction est tracée en premier. Mais si ce n\'est pas le cas, la fonction qui utilise les plus grands axes, dans notre cas la fonction polynomiale, doit être tracée en dernier. La légende sera attachée au dernier système d\'axes et il est plus pratique que ce soit le plus grand. Pour tracer les fonctions trigonométriques, il suffit de lancer quelques commandes.


```python
try:
    from FreeCAD.Plot import Plot
except ImportError:
    from freecad.plot import Plot

Plot.plot(t,s,r"$\sin\left( 2 \pi t \right)$")
Plot.plot(t,c,r"$\cos\left( 2 \pi t \right)$")
```

Dans cet exemple, nous transmettons directement les étiquettes des séries pour la légende. Notez que les chaînes d\'étiquettes ont le préfixe *r* afin d\'empêcher Python d\'essayer d\'interpréter des caractères spéciaux (le symbole *\\* est fréquemment utilisé dans la syntaxe [LaTeX](http://www.latex-project.org)).

Avant de pouvoir tracer la fonction polynomiale, nous devons créer de nouveaux axes. Dans l\'[atelier Plot](Plot_Workbench/fr.md), les nouveaux axes sont automatiquement sélectionnés comme axes actifs et les nouveaux tracés seront associés à ces axes.


```python
Plot.addNewAxes()
Plot.plot(x,y,r"$x^2$")
```

Comme vous pouvez le constater, votre graphique est devenu fou, avec des repères d\'axes qui se chevauchent, des courbes de la même couleur, etc. Nous devons maintenant utiliser l\'[atelier Plot](Plot_Workbench/fr.md) pour corriger ce graphique.



## Configurer Plot 



### Configurer les axes 

L\'[atelier Plot](Plot_Workbench/fr.md) fournit un outil permettant de modifier les propriétés des axes.

![](images/Plot_Axes.svg‎ ) 
*Icône de l'outil de configuration des axes*

Avec l\'outil [axes](Plot_Axes/fr.md), vous pouvez ajouter ou supprimer des axes, et définir les axes actifs, qui seront ensuite utilisés si vous tracer d\'autres données.

Pour modifier la taille du premier ensemble d\'axes, associé aux fonctions trigonométriques, il faut d\'abord l\'activer en faisant passer les axes actifs de 1 à 0. Nous pouvons ensuite déplacer les curseurs de dimension horizontale et verticale pour réduire sa taille (essayez d\'imiter l\'exemple). Nous devons également modifier l\'alignement des axes : sélectionnez respectivement haut et droite.



### Configurer les séries 

Définissez les propriétés de la série comme nous l\'avons fait dans le [tutoriel précédent](Plot_Basic_tutorial/fr.md).



### Affichage de la grille et de la légende 

La [grille](Plot_Grid/fr.md) et la [légende](Plot_Legend/fr.md) peuvent être affichées, et masquées, avec les outils déjà décrits dans le [tutoriel précédent](Plot_Basic_tutorial/fr.md) mais dans ce cas le comportement est un peu différent car il y a deux ensembles d\'axes.

Les lignes de la grille sont ajoutées à l\'ensemble des axes actifs. Pour ajouter des lignes au deuxième ensemble d\'axes dans notre exemple, il faut d\'abord l\'activer en faisant passer les axes actifs de 0 à 1 dans l\'outil [axes](Plot_Axes/fr.md).

Comme déjà mentionné, la légende sera positionnée par rapport aux derniers axes définis. Si vous montrez la légende maintenant, vous verrez qu\'elle est vraiment mal placée mais nous corrigerons cela plus tard.



### Définir les étiquettes des axes 

Lorsqu\'il s\'agit de définir les [étiquettes](Plot_Labels/fr.md) des axes, nous devons à nouveau composer avec nos deux ensembles d\'axes. Mais comme les étiquettes sont généralement définies pour tous les axes, la procédure est la même que celle décrite dans le [tutoriel précédent](Plot_Basic_tutorial/fr.md). L\'[atelier Plot](Plot_Workbench/fr.md) vous permet de définir un titre par ensemble d\'axes. Dans ce cas, nous voulons seulement définir un titre pour le dernier ensemble d\'axes, le plus grand.

**Axes 0:**

-   X Label = \$t\$
-   Y Label = \$\\mathrm{f} \\left( t \\right)\$

**Axes 1:**

-   Title = Exemple multiaxes
-   X Label = \$x\$
-   Y Label = \$\\mathrm{f} \\left( x \\right)\$

Modifiez la taille de la police de toutes les étiquettes à 20, et celle du titre à 24. Encore une fois, il y a un élément, le titre, qui est mal placé.



### Définir la position des éléments 

L\'[atelier Plot](Plot_Workbench/fr.md) fournit un outil permettant de modifier la position de plusieurs éléments de tracé, tels que les titres, les étiquettes et les légendes.

![](images/Plot_Positions.svg ) 
*Icône de l'éditeur de position*

Lorsque vous exécutez l\'outil, vous verrez une liste de tous les éléments modifiables. Les titres et les légendes peuvent être déplacés dans les deux sens, mais les étiquettes d\'axe ne peuvent être déplacées que le long de l\'axe auquel elles appartiennent. Sélectionnez le titre de l\'axe 1 et déplacez-le vers (0,24,1,01), puis sélectionnez la légende et déplacez-la vers une meilleure position. Vous pouvez également augmenter la taille de la police des étiquettes de la légende.



## Sauvegarder un fichier Plot 

Vous pouvez maintenant enregistrer votre travail. Voir le [tutoriel précédent](Plot_Basic_tutorial/fr.md) si vous ne savez pas comment faire.


{{Plot_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > [Addons](Category_Addons.md) > [Plot](Plot_Workbench.md) > Plot MultiAxes tutorial/fr

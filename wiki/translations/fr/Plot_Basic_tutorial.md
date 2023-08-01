---
- TutorialInfo:/fr
   Topic:Tutoriel de base de l'atelier Plot
   Level:Débutant
   Time:
   Author:
   FCVersion:0.19
   Files:
---

# Plot Basic tutorial/fr





Dans ce tutoriel, nous allons apprendre à créer un tracé de base à l\'aide de l\'[atelier Plot](Plot_Workbench/fr.md) et de la [console Python](Python_console/fr.md).

<img alt="" src=images/Plot_Trigonometric_Example.png  style="width:600px;"> 
*Exemple de tracé de base*

Dans l\'image, vous pouvez voir le résultat que nous obtiendrons approximativement. En suivant ce tutoriel, vous apprendrez :

-   Comment créer un Plot à partir de la [console Python](Python_console/fr.md).
-   Comment tracer des données à partir de la [console Python](Python_console/fr.md).
-   Comment afficher la <img alt="" src=images/Plot_Grid.svg  style="width:24px;"> [Plot Grille](Plot_Grid/fr.md).
-   Comment afficher la <img alt="" src=images/Plot_Legend.svg  style="width:24px;"> [Plot Légende](Plot_Legend/fr.md).
-   Comment éditer les <img alt="" src=images/Plot_Series.svg  style="width:24px;"> [Plot Séries](Plot_Series/fr.md) en introduisant le texte dans [LaTeX](http://www.latex-project.org).
-   Comment éditer les <img alt="" src=images/Plot_Labels.svg  style="width:24px;"> [Plot Etiquettes](Plot_Labels/fr.md) en introduisant le texte dans [LaTeX](http://www.latex-project.org).
-   Comment éditer les styles des séries.
-   Comment sauvegarder votre tracé.



## Traçage des données 

Pour tracer les données, vous n\'avez pas besoin de créer un nouveau document FreeCAD, allez dans la [console Python](Python_console/fr.md) et entrez les commandes ou utilisez les [macros](Macros/fr.md).



### Création d\'un document Plot 

Les tracés sont des documents spéciaux qui peuvent être créés manuellement afin d\'ajouter des données ultérieurement ou l\'atelier peut en créer un automatiquement lorsque vous commencez à tracer des données. La création de votre propre document de tracé présente deux avantages :

-   Vous pouvez définir le libellé de la fenêtre du document.
-   Vous pouvez contrôler le document dans lequel vous tracer vos données.

Pour créer un nouveau document de tracé, il suffit de lancer les commandes suivantes :


```python
try:
    from FreeCAD.Plot import Plot
except ImportError:
    from freecad.plot import Plot

Plot.figure("TrigonometricTest")
```

Dans FreeCAD version 0.19 il est nécessaire d\'installer l\'<img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [atelier Plot](Plot_Workbench/fr.md) avec le [Gestionnaire des extensions](Std_AddonMgr/fr.md), alors qu\'à partir de la version 0.20 de FreeCAD, l\'extension externe n\'est plus nécessaire pour réaliser des tracés. Les commandes ci-dessus vont créer un nouvel onglet dans la [Zone de vue principale](Main_view_area/fr.md) appelé **TrigonometricTest**. Le document nouvellement créé possède déjà un ensemble d\'axes. Chaque document de tracé possède au moins un jeu d\'axes.



### Fonctions de dessin 

Vous pouvez également commencer à travailler à partir d\'ici car, comme nous l\'avons déjà expliqué, la commande plot créera un nouveau document si nécessaire. La chose suivante à faire est de créer les données pour les fonctions sinus et cosinus que nous voulons tracer :


```python
import math
t = range(0,101)
t = [tt/100.0 for tt in t]
s = [math.sin(2.0*math.pi*tt) for tt in t]
c = [math.cos(2.0*math.pi*tt) for tt in t]
```

Ceci va créer 3 tableaux de données (avec 101 points) :

-   *t* = Temps en secondes.
-   *s* = fonction Sinus.
-   *c* = fonction Cosinus.

Afin de tracer les deux fonctions, il suffit de lancer les commandes suivantes :


```python
Plot.plot(t,s)
Plot.plot(t,c)
```

La commande **plot** permet d\'utiliser l\'étiquette de la série comme argument, mais comme nous la modifierons plus tard à l\'aide des outils de l\'atelier Plot, nous ne transmettons pas encore cette donnée.



## Configurez Plot 



### Affichage de la grille et de la légende 

Changez l\'atelier de FreeCAD en l\'[atelier Plot](Plot_Workbench/fr.md) avec **Affichage → Atelier → Plot**. (vous devez d\'abord installer l\'extension avec le [Gestionnaire des extensions](Std_AddonMgr/fr.md)). Une fois l\'atelier chargé, utilisez l\'outil [grille](Plot_Grid/fr.md) pour afficher la grille.

![](images/Plot_Grid.svg‎ ) 
*Afficher/masquer l'icône de l'outil de grille*

Vous pouvez répéter l\'action pour masquer la grille. Utilisez l\'outil [Légende](Plot_Legend/fr.md) pour afficher ou masquer la légende.

![](images/Plot_Legend.svg ) 
*Afficher/masquer l'icône de l'outil de légende*

Comme vous pouvez le voir, la légende est très petite et vide car nous n\'avons pas encore défini d\'étiquette de série. Dans l\'[atelier Plot](Plot_Workbench/fr.md), les séries sans étiquette ne sont pas affichées dans la légende.



### Définir l\'étiquette de la série 

Avec l\'outil [Séries](Plot_Series/fr.md), vous pouvez modifier les paramètres de chaque série.

![](images/Plot_Series.svg‎ ) 
*Icône de l'outil de configuration de la série*

Sélectionnez la série que vous voulez modifier, nous allons commencer par la première. Décochez **No label** et définissez cette étiquette :


```python
$y = \sin \left( 2 \pi t \right)$
```

Puisque [matplotlib](http://matplotlib.org/) prend en charge [LaTeX](http://www.latex-project.org), vous pouvez définir toutes les étiquettes et tous les titres en utilisant LaTeX. Définissez l\'étiquette suivante pour la deuxième série :


```python
$y = \cos \left( 2 \pi t \right)$
```



### Définir le style de la série 

Vous pouvez définir de nombreuses propriétés de la série. Essayez de définir les propriétés montrées dans l\'image d\'exemple, en changeant les couleurs et le style de dessin de la deuxième série.



### Définir les étiquettes des axes 

Avec l\'outil [Etiquettes](Plot_Labels/fr.md), vous pouvez définir le titre et les étiquettes des axes.

![](images/Plot_Labels.svg‎ ) 
*Icône de l'outil Étiquettes*

Définir ces données :

-   Title = Trigonometric functions example
-   X Label = \$t\$
-   Y Label = \$y = \\mathrm{f} \\left( t \\right)\$

Modifiez également la taille de la police du titre et de toutes les étiquettes à 20.



## Sauvegarder le tracé 

Avec l\'outil [Sauvegarde](Plot_Save/fr.md), vous pouvez enregistrer votre tracé sous forme de fichier image dans plusieurs formats.

![](images/Plot_Save.svg ) 
*Icône de l'outil de sauvegarde*

Sélectionnez d\'abord le chemin et le nom du fichier de sortie.

Définissez la taille de l\'image de sortie en pouces, par exemple, utilisez 11,7x8,3 pour obtenir un format **DIN A4**. DPI (Dots per inch) contrôlera la résolution de l\'image, par exemple, utilisez 100 dpi. En combinaison avec les dimensions données, vous obtiendrez une image de 1170x830 pixels.


{{Plot_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > [Addons](Category_Addons.md) > [Plot](Plot_Workbench.md) > Plot Basic tutorial/fr

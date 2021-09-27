# Plot Basic tutorial/fr
<div class="mw-translate-fuzzy">


{{TutorialInfo/fr
|Topic=Tutoriel de base de l'atelier Plot
|Level=Débutant
|Time=
|Author=
|FCVersion=
|Files=
}}


</div>


<div class="mw-translate-fuzzy">

Dans ce tutoriel, nous allons apprendre à effectuer un tracé de base à l\'aide de l\'[atelier Plot](Plot_Workbench/fr.md) et de la [console Python](Python_console/fr.md).


</div>

<img alt="" src=images/Plot_Trigonometric_Example.png  style="width:600px;">


<div class="mw-translate-fuzzy">

<img alt="Basic plot example" src=images/Plot_Trigonometric_Example.png  style="width:600px;">


<center>

Basic plot example.


</center>


</div>


<div class="mw-translate-fuzzy">

Dans l\'image précédente, vous pouvez voir le résultat que nous obtiendrons approximativement. En suivant ce tutoriel, vous apprendrez :

-   Comment créer un Plot à partir de la [console Python](Python_console/fr.md).
-   Comment tracer des données à partir de la [console Python](Python_console/fr.md).
-   Comment afficher la <img alt="" src=images/Plot_Grid.svg  style="width:24px;"> [Plot Grille](Plot_Grid/fr.md).
-   Comment afficher la <img alt="" src=images/Plot_Legend.svg  style="width:24px;"> [Plot Légende](Plot_Legend/fr.md).
-   Comment éditer les <img alt="" src=images/Plot_Series.svg  style="width:24px;"> [Plot Séries](Plot_Series/fr.md), en introduisant le texte dans [LaTeX](http://www.latex-project.org).
-   Comment éditer les <img alt="" src=images/Plot_Labels.svg  style="width:24px;"> [Plot Etiquettes](Plot_Labels/fr.md), en introduisant le texte dans [LaTeX](http://www.latex-project.org).
-   Comment éditer les styles des séries.
-   Comment sauvegarder votre tracé.


</div>

## Plotting data 


<div class="mw-translate-fuzzy">

## Créer les données Plot 

Pour tracer les données, vous n\'avez pas besoin de créer un nouveau document FreeCAD, il faut simplement aller dans la console **Python**, et, entrer les commandes, ou utilisez les [macros](Macros/fr.md).


</div>

### Creating plot document 


<div class="mw-translate-fuzzy">

### Création d\'un document Plot 

Les documents **Plot**, sont des documents spéciaux, qui peuvent être créés manuellement, pour y ajouter des données, ou le module peut en crée un automatiquement, lorsque vous démarrez le traçage de données.

Créer votre propre document **Plot** a 2 avantages :

-   Vous pouvez définir l\'étiquette de la fenêtre du document.
-   Vous pouvez contrôler facilement le document dont vous ajoutez vos données.


</div>


<div class="mw-translate-fuzzy">

Afin de créer nouveau document **Plot**, lancez simplement ces commandes :


</div>


```python
try:
    from FreeCAD.Plot import Plot
except ImportError:
    from freecad.plot import Plot

Plot.figure("TrigonometricTest")
```


<div class="mw-translate-fuzzy">

Cela va créer un nouvel onglet sur la fenêtre principale, appelée \'\'\'TrigonometricTest \'\'\'. Le nouveau document créé, a déjà un ensemble d\'axes. Chaque document **Plot** a au moins un jeu d\'axes, qui peut être supprimé, sans utiliser pleinement **matplotlib**.


</div>

### Drawing functions 


<div class="mw-translate-fuzzy">

### Fonctions de dessin 

Vous pouvez commencer à travailler ici car la commande de tracé démarre un nouveau document, mais toutes les commandes de tracé que vous exécutez ajoutent des séries au tracé créé jusqu\'à ce que vous ne créiez pas de nouveau document, il est donc généralement préférable de contrôler les documents de tracé ouverts. La première chose que nous devons faire est de créer les données pour les fonctions sinus et cosinus que nous voulons tracer:


</div>


```python
import math
t = range(0,101)
t = [tt/100.0 for tt in t]
s = [math.sin(2.0*math.pi*tt) for tt in t]
c = [math.cos(2.0*math.pi*tt) for tt in t]
```

Ceci va créer 3 tableaux de données (avec 101 points) :

-   **t** = **Temps en secondes**.
-   **s** = fonction **Sinus**.
-   **c** = fonction **Cosinus**.


<div class="mw-translate-fuzzy">

Afin de tracer les deux fonctions, il suffit de lancer les commandes suivantes :


</div>


```python
Plot.plot(t,s)
Plot.plot(t,c)
```


<div class="mw-translate-fuzzy">

Ces commandes vont tracer nos fonctions. La commande **Plot** permet d\'utiliser une **Series** d\'étiquettes, comme arguments, mais ultérieurement, nous allons modifier les données à l\'aide du module **Plot**, donc, nous ne transmettrons pas encore ces données.


</div>

## Configurez **Plot** 

### Showing grid and legend 


<div class="mw-translate-fuzzy">

### Afficher la grille, et, les légendes 

Pour modifier l\'outil **[module Plot](Plot_Module/fr.md)** de FreeCAD, allez dans le menu **Affichage -\> Workbench**. Lorsque vous avez activé, le module **Plot** utilisez l\'outil **Grid** afin de l\'afficher.


</div>

![](images/Plot_Grid.svg‎ )


<div class="mw-translate-fuzzy">

![Afficher/masquer l\'icône de l\'outil de grille](images/Plot_Grid.svg‎ )


<center>

Afficher/masquer l\'icône de l\'outil de grille.


</center>


</div>


<div class="mw-translate-fuzzy">

Vous pouvez répéter l\'action pour le cacher. Vous pouvez également afficher la légende avec l\'outil fourni.


</div>

![](images/Plot_Legend.svg )


<div class="mw-translate-fuzzy">

![Afficher/masquer l\'icône de l\'outil légende](images/Plot_Legend.svg‎ )


<center>

Afficher/masquer l\'icône de l\'outil légende.


</center>


</div>


<div class="mw-translate-fuzzy">

Comme vous pouvez le voir, la légende est vide car nous n\'avons pas encore défini d\'étiquette de série. Dans [Atelier Plot](Plot_Module/fr.md), les séries sans étiquette ne sont pas représentées dans la légende afin de vous permettre de tracer des lignes auxiliaires.


</div>

### Setting series label 


<div class="mw-translate-fuzzy">

### Définir les étiquettes des **Series** 

Avec l\'outil **Series**, vous pouvez modifier certains paramètres de la **Series**.


</div>

![](images/Plot_Series.svg‎ )


<div class="mw-translate-fuzzy">

![Icône d\'outil de configuration des séries](images/Plot_Series.svg‎ )


<center>

Icône d\'outil de configuration des séries.


</center>


</div>


<div class="mw-translate-fuzzy">

Tout d\'abord, pour toutes les lignes sélectionnées que vous souhaitez modifier, pour l\'exemple, nous allons commencer avec la première ligne.

Décochez la case **No label**, et, la valeur de cette étiquette :


</div>


```python
$y = \sin \left( 2 \pi t \right)$
```


<div class="mw-translate-fuzzy">

Étant donné que [matplotlib](http://matplotlib.org/), prend en charge [LaTeX](http://www.latex-project.org), vous pouvez définir toutes les étiquettes, ou les titres que vous voulez utiliser.

Donnez l\'étiquette suivante à la deuxième **Series** :


</div>


```python
$y = \cos \left( 2 \pi t \right)$
```

### Setting series style 


<div class="mw-translate-fuzzy">

### Définition d\'un style à la **Series** 

L\'outils **Series**, vous permet de définir un grand nombre de propriétés à la **Series**. Essayez de définir les propriétés affichées dans l\'image exemple, modifiez les couleurs de la **Series**, et, le style de dessin en une seconde.


</div>

### Setting axes labels 


<div class="mw-translate-fuzzy">

### Définition des **Labels** des axes 

Avec l\'outil **Labels**, vous pouvez définir des labels associées à tous les axes créés.


</div>

![](images/Plot_Labels.svg‎ )


<div class="mw-translate-fuzzy">

![Icône de l\'outil d\'étiquettes](images/Plot_Labels.svg‎ )


<center>

Icône de l\'outil d\'étiquettes.


</center>


</div>

Définir ces données :

-   Title = Trigonometric functions example
-   X Label = \$t\$
-   Y Label = \$y = \\mathrm{f} \\left( t \\right)\$


<div class="mw-translate-fuzzy">

Modifiez également la taille de chacun d\'eux à 20.


</div>

## Saving plot 


<div class="mw-translate-fuzzy">

## Sauvez **Plot** 

Sauvegardes avec l\'outil **Plot**, vous pouvez enregistrer votre **Plot**, dans un fichier image, dans plusieurs formats différents.


</div>

![](images/Plot_Save.svg )


<div class="mw-translate-fuzzy">

![Icône de l\'outil d\'enregistrement](images/Plot_Save.svg‎ )


<center>

Icône de l\'outil d\'enregistrement.


</center>


</div>


<div class="mw-translate-fuzzy">

Commencez par sélectionner le chemin du fichier de sortie. Vous pouvez utiliser la boîte de dialogue sélection fichier à l\'aide de la touche à droite, de la ligne d\'édition du chemin d\'accès.


</div>


<div class="mw-translate-fuzzy">

Vous pouvez définir la taille de l\'image de sortie en pouces (inches), par exemple, nous pouvons définir **11.7x8.3**, qui est un format **DIN A4**, la taille d\'une feuille de papier standard. La résolution de l\'image, dépendra du **DPI** (Dots per inch ou points par pouce), par exemple avec **100 dpi**, vous obtiendrez une image de **1170 x 830 pixels**.


</div>


{{Tutorials_navi

}} {{Plot_Tools_navi}} 

_ _

---
[documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > Plot Basic tutorial/fr

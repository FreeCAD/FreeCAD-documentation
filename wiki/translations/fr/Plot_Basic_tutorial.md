 {{TutorialInfo/fr
|Topic=Tutoriel de base de l'atelier Plot
|Level=Débutant
|Time=
|Author=
|FCVersion=
|Files=
}}

Dans ce tutoriel, nous allons apprendre à effectuer un tracé de base à l\'aide de l\'[atelier Plot](Plot_Workbench/fr.md) et de la [console Python](Python_console/fr.md).

<img alt="Basic plot example" src=images/Plot_Trigonometric_Example.png  style="width:600px;">


<center>

Basic plot example.


</center>

Dans l\'image précédente, vous pouvez voir le résultat que nous obtiendrons approximativement. En suivant ce tutoriel, vous apprendrez :

-   Comment créer un Plot à partir de la [console Python](Python_console/fr.md).
-   Comment tracer des données à partir de la [console Python](Python_console/fr.md).
-   Comment afficher la <img alt="" src=images/Plot_Grid.svg  style="width:24px;"> [Plot Grille](Plot_Grid/fr.md).
-   Comment afficher la <img alt="" src=images/Plot_Legend.svg  style="width:24px;"> [Plot Légende](Plot_Legend/fr.md).
-   Comment éditer les <img alt="" src=images/Plot_Series.svg  style="width:24px;"> [Plot Séries](Plot_Series/fr.md), en introduisant le texte dans [LaTeX](http://www.latex-project.org).
-   Comment éditer les <img alt="" src=images/Plot_Labels.svg  style="width:24px;"> [Plot Etiquettes](Plot_Labels/fr.md), en introduisant le texte dans [LaTeX](http://www.latex-project.org).
-   Comment éditer les styles des séries.
-   Comment sauvegarder votre tracé.

## Créer les données Plot {#créer_les_données_plot}

Pour tracer les données, vous n\'avez pas besoin de créer un nouveau document FreeCAD, il faut simplement aller dans la console **Python**, et, entrer les commandes, ou utilisez les [macros](Macros/fr.md).

### Création d\'un document Plot {#création_dun_document_plot}

Les documents **Plot**, sont des documents spéciaux, qui peuvent être créés manuellement, pour y ajouter des données, ou le module peut en crée un automatiquement, lorsque vous démarrez le traçage de données.

Créer votre propre document **Plot** a 2 avantages :

-   Vous pouvez définir l\'étiquette de la fenêtre du document.
-   Vous pouvez contrôler facilement le document dont vous ajoutez vos données.

Afin de créer nouveau document **Plot**, lancez simplement ces commandes :


```python
import Plot
Plot.figure("TrigonometricTest")
```

Cela va créer un nouvel onglet sur la fenêtre principale, appelée \'\'\'TrigonometricTest \'\'\'. Le nouveau document créé, a déjà un ensemble d\'axes. Chaque document **Plot** a au moins un jeu d\'axes, qui peut être supprimé, sans utiliser pleinement **matplotlib**.

### Fonctions de dessin {#fonctions_de_dessin}

Vous pouvez commencer à travailler ici car la commande de tracé démarre un nouveau document, mais toutes les commandes de tracé que vous exécutez ajoutent des séries au tracé créé jusqu\'à ce que vous ne créiez pas de nouveau document, il est donc généralement préférable de contrôler les documents de tracé ouverts. La première chose que nous devons faire est de créer les données pour les fonctions sinus et cosinus que nous voulons tracer:


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

Afin de tracer les deux fonctions, il suffit de lancer les commandes suivantes :


```python
Plot.plot(t,s)
Plot.plot(t,c)
```

Ces commandes vont tracer nos fonctions. La commande **Plot** permet d\'utiliser une **Series** d\'étiquettes, comme arguments, mais ultérieurement, nous allons modifier les données à l\'aide du module **Plot**, donc, nous ne transmettrons pas encore ces données.

## Configurez **Plot** {#configurez_plot}

### Afficher la grille, et, les légendes {#afficher_la_grille_et_les_légendes}

Pour modifier l\'outil **[module Plot](Plot_Module/fr.md)** de FreeCAD, allez dans le menu **Affichage -\> Workbench**. Lorsque vous avez activé, le module **Plot** utilisez l\'outil **Grid** afin de l\'afficher.

![Afficher/masquer l\'icône de l\'outil de grille](images/Plot_Grid.svg‎ )


<center>

Afficher/masquer l\'icône de l\'outil de grille.


</center>

Vous pouvez répéter l\'action pour le cacher. Vous pouvez également afficher la légende avec l\'outil fourni.

![Afficher/masquer l\'icône de l\'outil légende](images/Plot_Legend.svg‎ )


<center>

Afficher/masquer l\'icône de l\'outil légende.


</center>

Comme vous pouvez le voir, la légende est vide car nous n\'avons pas encore défini d\'étiquette de série. Dans [Atelier Plot](Plot_Module/fr.md), les séries sans étiquette ne sont pas représentées dans la légende afin de vous permettre de tracer des lignes auxiliaires.

### Définir les étiquettes des **Series** {#définir_les_étiquettes_des_series}

Avec l\'outil **Series**, vous pouvez modifier certains paramètres de la **Series**.

![Icône d\'outil de configuration des séries](images/Plot_Series.svg‎ )


<center>

Icône d\'outil de configuration des séries.


</center>

Tout d\'abord, pour toutes les lignes sélectionnées que vous souhaitez modifier, pour l\'exemple, nous allons commencer avec la première ligne.

Décochez la case **No label**, et, la valeur de cette étiquette :


```python
$y = \sin \left( 2 \pi t \right)$
```

Étant donné que [matplotlib](http://matplotlib.org/), prend en charge [LaTeX](http://www.latex-project.org), vous pouvez définir toutes les étiquettes, ou les titres que vous voulez utiliser.

Donnez l\'étiquette suivante à la deuxième **Series** :


```python
$y = \cos \left( 2 \pi t \right)$
```

### Définition d\'un style à la **Series** {#définition_dun_style_à_la_series}

L\'outils **Series**, vous permet de définir un grand nombre de propriétés à la **Series**. Essayez de définir les propriétés affichées dans l\'image exemple, modifiez les couleurs de la **Series**, et, le style de dessin en une seconde.

### Définition des **Labels** des axes {#définition_des_labels_des_axes}

Avec l\'outil **Labels**, vous pouvez définir des labels associées à tous les axes créés.

![Icône de l\'outil d\'étiquettes](images/Plot_Labels.svg‎ )


<center>

Icône de l\'outil d\'étiquettes.


</center>

Définir ces données :

-   Title = Trigonometric functions example
-   X Label = \$t\$
-   Y Label = \$y = \\mathrm{f} \\left( t \\right)\$

Modifiez également la taille de chacun d\'eux à 20.

## Sauvez **Plot** {#sauvez_plot}

Sauvegardes avec l\'outil **Plot**, vous pouvez enregistrer votre **Plot**, dans un fichier image, dans plusieurs formats différents.

![Icône de l\'outil d\'enregistrement](images/Plot_Save.svg‎ )


<center>

Icône de l\'outil d\'enregistrement.


</center>

Commencez par sélectionner le chemin du fichier de sortie. Vous pouvez utiliser la boîte de dialogue sélection fichier à l\'aide de la touche à droite, de la ligne d\'édition du chemin d\'accès.

Vous pouvez définir la taille de l\'image de sortie en pouces (inches), par exemple, nous pouvons définir **11.7x8.3**, qui est un format **DIN A4**, la taille d\'une feuille de papier standard. La résolution de l\'image, dépendra du **DPI** (Dots per inch ou points par pouce), par exemple avec **100 dpi**, vous obtiendrez une image de **1170 x 830 pixels**. {{Tutorials navi}} {{Plot Tools navi}} 

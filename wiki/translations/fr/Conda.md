# Conda/fr
## Introduction




Cette page est destinée à présenter Conda en tant que gestionnaire de packages, de dépendances et d\'environnement pour FreeCAD.

Actuellement, cette page répertorie principalement des liens vers des forums de discussion FreeCAD pertinents et d\'autres endroits sur le Web, mais l\'espoir est de documenter les points saillants de ces liens dans cette page.

Voir aussi un [tutoriel vidéo](https://www.youtube.com/watch?v=sCs8xlrw2nM) du contenu de cette page.

## Motivation

La motivation pour utiliser Conda est multiple, tout comme le but de Conda.

Décomposons-le.



### Conda en tant que gestionnaire de packages 

Premièrement, Conda est un gestionnaire de paquets - similaire à apt ou pip.

Cela signifie que nous pouvons installer des **packages** avec une simple conda install à partir de divers [canaux](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html#what-is-a-conda-channel) tels que [conda-forge](https://conda-forge.org/).

Conda Forge est analogue à [the Python Package Index (PyPI)](https://pypi.org/), un canal communautaire composé de milliers de contributeurs et sert [freecad](https://anaconda.org/conda-forge/freecad) en tant que package conda.



### Conda en tant que gestionnaire de dépendances 

Ensuite, Conda est un gestionnaire de dépendances, également similaire à apt ou pip.

Conda peut gérer les dépendances et installer les dépendances pour un projet comme FreeCAD.

Pourquoi ne pas simplement utiliser pip? pip fonctionne très bien pour gérer les dépendances des projets qui n\'utilisent «que» Python.

Conda fonctionne pour plusieurs langages et est donc mieux adapté pour gérer les dépendances de projets comme FreeCAD qui ont des dépendances dans une variété de langages comme C/C++ et Python.



### Conda en tant que gestionnaire d\'environnement 

Conda a le concept d\'un [environnement](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) qui est la combinaison unique de packages et de versions nécessaires pour exécuter une pièce du logiciel. Par exemple, un atelier FreeCAD.

Avec les environnements, vous pouvez facilement les «activer» et les «désactiver», ou basculer entre les versions de packages nécessaires à des logiciels particuliers.

Ceci est utile pour tester le comportement d\'un plan de travail avec un ensemble particulier de packages. Par exemple, comment se comporte un atelier dans FreeCAD 18.4 vs 19 ?

Les environnements Conda vous permettent de reproduire exactement le même environnement sur différentes machines.

Par exemple, plusieurs machines de développement locales ou un serveur de construction distant hébergé par Travis CI.



## Installation de Conda 

1\. [Installer Miniconda](https://docs.conda.io/en/latest/miniconda.html).

2\. Vérifiez que votre installation a réussi et familiarisez-vous avec la **CLI** 

## Installation de FreeCAD à l\'aide de Conda 

Tout d\'abord, vous devez décider si vous voulez installer une version **stable** de FreeCAD, ou essayer le dernier code **instable** de FreeCAD principal.

Les versions stables de FreeCAD sont disponibles sur le canal conda-forge, tandis que les dernières versions de FreeCAD principal sont disponibles sur le canal freecad/label/dev.

  Conda Channel         Stable?
   
  conda-forge         Oui ✔️
  freecad/label/dev   Non ❌

Deuxièmement, comme vous pouvez facilement créer des environnements dédiés dans conda, il est recommandé d\'en créer un pour FreeCAD.

La commande create vous permet de créer un environnement à partir d\'une liste de packages spécifiés. Dans notre cas, nous voulons créer un environnement appelé \"fcenv\" (abréviation de FreeCAD environment) à partir du package freecad et dire à conda de rechercher le package freecad en utilisant le canal conda-forge. 
```python
conda create --name fcenv --channel conda-forge freecad
``` **Astuce :** Vous pouvez également dire à conda de toujours rechercher conda-forge lors de l\'installation des packages avec la commande suivante: 
```python
conda config --add channels conda-forge
``` Les builds hebdomadaires peuvent être installés à partir du canal freecad/label/dev comme suit: 
```python
conda create --name fcenv-dev --channel freecad/label/dev freecad
```



## Discussion sur le forum FreeCAD 

-   [Let\'s talk about Conda](https://forum.freecadweb.org/viewtopic.php?t=39656)
-   [Packaging solution: (ana)conda](https://forum.freecadweb.org/viewtopic.php?f=10&t=15197)
-   [FreeCAD Conda Distribution](https://forum.freecadweb.org/viewtopic.php?f=8&t=45582)



### Voir aussi 

-   <https://docs.conda.io/en/latest/>
-   <https://conda-forge.org/docs/>
-   <https://docs.conda.io/projects/conda-build/en/latest/>
-   <https://anaconda.org/conda-forge/freecad>
-   <https://anaconda.org/freecad/freecad>
-   <https://github.com/FreeCAD/FreeCAD_Conda>
-   <https://github.com/FreeCAD/FreeCAD-AppImage>



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Conda/fr

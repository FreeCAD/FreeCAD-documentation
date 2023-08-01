# FreeCAD Scripting Basics/fr
{{TOCright}}



## Les scripts Python dans FreeCAD 

FreeCAD a été programmé dès la première ligne de code pour être totalement contrôlé par des scripts écrits en Python. Presque toutes les parties de FreeCAD, telles que l\'interface, le contenu des scènes et même la représentation de ce contenu dans les vues 3D, sont accessibles à partir de l\'interpréteur Python intégré ou de vos propres scripts. En conséquence, FreeCAD est probablement l\'une des applications d\'ingénierie les plus personnalisables et évolutives disponibles actuellement.

Si vous n\'êtes pas familier avec Python, nous vous recommandons de chercher des tutoriels sur internet et jeter un œil rapide sur sa structure. Python est un langage très facile à apprendre, en particulier parce qu\'il peut être exécuté à l\'intérieur d\'un interpréteur, de la plus simple commande jusqu\'à l\'élaboration de programmes complexes, il peut être exécuté à la volée sans avoir besoin de compilateur. FreeCAD dispose de son propre interpréteur Python intégré. Si vous ne voyez pas de fenêtre intitulée **Console Python** comme illustré ci-dessous, vous pouvez l\'activer en cliquant dans la barre d\'outils **Affichage → Panneaux → Console Python**.



### L\'interpréteur Python 

Depuis l'interpréteur, vous pouvez accéder à l\'ensemble de vos modules Python installés sur le sytème, ainsi qu\'aux modules FreeCAD intégrés et à tous les modules FreeCAD supplémentaires que vous avez installés ultérieurement. La capture d\'écran ci-dessous montre l\'interpréteur Python :

![The FreeCAD Python interpreter](images/screenshot_pythoninterpreter.jpg )

Depuis l\'interpréteur, vous pouvez exécuter du code Python et parcourir les classes et fonctions disponibles. FreeCAD fournit un navigateur de classe très pratique pour l\'exploration du monde FreeCAD : lorsque vous tapez le nom d\'une classe connue suivi d\'un point (ce qui signifie que vous voulez ajouter quelque chose après le point, à partir de cette classe), une fenêtre du navigateur de classe s\'ouvre, où vous pouvez naviguer entre sous-classes et méthodes disponibles. Lorsque vous sélectionnez quelque chose, un texte d\'aide associé (s\'il existe) s\'affiche :

![The FreeCAD class browser](images/screenshot_classbrowser.jpg )

Alors, commencez ici en tapant `App.` ou `Gui.` et voyez ce qui se passe. Une autre façon, plus typique de Python, d\'explorer le contenu des modules et des classes consiste à utiliser la commande `print(dir())`. Par exemple, taper `print(dir())` listera tous les modules actuellement chargés dans FreeCAD. `print(dir(App))` vous montrera tout ce qu\'il y a, à l\'intérieur du module App, etc.

Une autre fonctionnalité utile de l\'interpréteur est la possibilité de parcourir l\'historique des commandes et de récupérer une ligne de code que vous avez déjà tapée précédemment. Pour parcourir l\'historique des commandes, utilisez simplement **Flèche haut** ou **Flèche bas**.

Si vous cliquez avec le bouton droit de la souris dans la fenêtre de l\'interpréteur, vous avez également les options classiques d\'un traitement de texte, telles que copier tout l\'histoire (utile lorsque vous voulez expérimenter votre code avant de faire votre script final), ou d\'insérer un nom de fichier avec le chemin complet. 

### Aide Python 

Dans le menu 

## Modules intégrés 

Étant donné que FreeCAD est conçu pour pouvoir également être exécuté sans interface graphique (GUI), presque toutes ses fonctionnalités sont séparées en deux groupes : la fonctionnalité principale, nommée `App` et la fonctionnalité GUI, nommée `Gui`. Ces deux modules sont également accessibles à partir de scripts en dehors de l\'interpréteur, respectivement par les noms `FreeCAD` et `FreeCADGui`.

-   Dans le module `App`, vous trouverez tout ce qui concerne l\'application elle-même, comme les méthodes d\'ouverture ou de fermeture des fichiers et pour les documents, comme la définition du document actif ou la liste de son contenu.

-   Dans le module `Gui`, vous trouverez des outils pour accéder et gérer les éléments Gui, comme les établis et leurs barres d\'outils et plus intéressant, la représentation graphique de l\'ensemble du contenu FreeCAD.

Lister le contenu de ces modules n\'est pas très utile, car ces derniers se développent assez rapidement avec la croissance de FreeCAD. Mais les deux outils de navigation fournis (le navigateur de classe et l\'aide Python), devraient vous fournir à tout moment, une documentation complète et à jour. 

### Les objets App et Gui 

Comme nous l\'avons déjà mentionné, dans FreeCAD tout est séparé en noyau et représentation graphique. Cela inclut les objets 3D. Vous pouvez accéder à l\'édition des propriétés des objets (appelées fonctionnalités dans FreeCAD) via le module `App` et changer la façon dont ils sont représentés à l\'écran via le module `Gui`. Par exemple, un cube possède des propriétés le définissant (comme la largeur, la longueur et la hauteur) qui sont stockées dans un objet `App` et des propriétés de représentation (comme la couleur des faces, le mode de dessin) qui sont stockées dans un objet `Gui` correspondant.

Cette méthode de travail permet une multitude d\'utilisations, comme des algorithmes travaillant uniquement sur la partie des caractéristiques, sans avoir à se soucier de la partie visuelle, voire de réorienter le contenu du document à une partie non-graphique de l\'application, tels que des listes, des tableurs, ou l\'analyse d\'éléments.

Pour chaque objet `App` dans votre document, il existe un objet `Gui` correspondant. En fait, le document lui-même possède à la fois un objet `App` et un objet `Gui`. Ceci, bien sûr, ne s\'applique que lorsque vous exécutez FreeCAD avec son interface complète. Dans la version en ligne de commande, aucune interface graphique n\'existe, donc seuls les objets `App` sont disponibles. Notez que la partie `Gui` des objets, est recréée chaque fois qu\'un objet `App` est marqué \'à recalculer\', (par exemple lorsque l\'un de ses paramètres change), donc tout changement effectué directement sur l\'objet `Gui` peut être perdu.

Pour accéder à la partie `App` d\'un élément, vous tapez :


```python
myObject = App.ActiveDocument.getObject("ObjectName")
```

où `"ObjectName"` est le nom de votre objet. Vous pouvez également taper :


```python
myObject = App.ActiveDocument.ObjectName
```

Pour accéder à la partie `Gui` du même objet, vous tapez :


```python
myViewObject = Gui.ActiveDocument.getObject("ObjectName")
```

où `"ObjectName"` est le nom de votre objet. Vous pouvez également taper :


```python
myViewObject = App.ActiveDocument.ObjectName.ViewObject
```

Si vous êtes en mode ligne de commande et n\'avez pas d\'interface graphique, la dernière ligne renverra 

### Les objets dans un document 

Dans FreeCAD, tout votre travail réside dans des documents. Un document contient votre géométrie et peut être enregistré dans un fichier. Plusieurs documents peuvent être ouverts en même temps. Le document, comme la géométrie contenue à l\'intérieur, possède des objets `App` et `Gui`. L\'objet `App` contient vos caractéristiques géométriques réelles, tandis que l\'objet `Gui` contient les différentes vues de votre document. Vous pouvez ouvrir plusieurs fenêtres, chacune affichant votre travail avec un facteur de zoom différent, ou avec une direction différente. Ces vues font toutes partie de l\'objet `Gui` de votre document.

Pour accéder à la partie `App` du document actuellement ouvert (le document actif), vous tapez :


```python
myDocument = App.ActiveDocument
```

Pour créer un nouveau document, tapez :


```python
myDocument = App.newDocument("Document Name")
```

Pour accéder à la partie `Gui` du document actuellement ouvert (le document actif), vous tapez :


```python
myGuiDocument = Gui.ActiveDocument
```

Pour accéder à la vue courante, tapez :


```python
myView = Gui.ActiveDocument.ActiveView
```


{{Top}}



## Utilisation des modules supplémentaires 

Les modules 

### Création d\'objets 

Chaque module a sa propre manière de gérer la géométrie, mais une chose qu\'ils peuvent généralement tous faire, est de créer des objets dans le document. Mais le document FreeCAD reconnaît également les types d\'objets disponibles fournis par les modules :


```python
FreeCAD.ActiveDocument.supportedTypes()
```

répertorie tous les objets possibles que vous pouvez créer. Par exemple, créons un maillage (géré par le module `Mesh`) et une pièce (gérée par le module `Part`) :


```python
myMesh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "myMeshName")
myPart = FreeCAD.ActiveDocument.addObject("Part::Feature", "myPartName")
```

Le premier argument est le type d\'objet, le second le nom de l\'objet. Nos deux objets semblent presque identiques : ils ne contiennent pas encore de géométrie et la plupart de leurs propriétés sont les mêmes, lorsque vous les inspectez avec `dir(myMesh)` et `dir(myPart)`. A l\'exception d\'une chose, `myMesh` a une propriété `Mesh` et `myPart` a une propriété `Shape`. C\'est ainsi que les données de maillage et de pièce sont stockées. Par exemple, créons un cube `Part` et stockons-le dans notre objet `myPart` :


```python
import Part
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
```

Vous pouvez essayer de stocker le cube dans la propriété `Mesh` de l\'objet `myMesh`, mais cela renverra une erreur. En effet, chaque propriété est conçue pour stocker uniquement un certain type d\'objet. Dans une propriété `Mesh`, vous ne pouvez enregistrer que les éléments créés avec le module `Mesh`. Notez que la plupart des modules ont également un raccourci pour ajouter leur géométrie au document :


```python
import Part
cube = Part.makeBox(2, 2, 2)
Part.show(cube)
```


{{Top}}



### Modification d\'objets 

La modification d\'un objet se fait de la même manière :


```python
import Part
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
```

Maintenant, nous allons construire un cube plus gros :


```python
biggercube = Part.makeBox(5, 5, 5)
myPart.Shape = biggercube
```


{{Top}}



### Interroger les objets 

Vous pouvez toujours savoir de quel type d\'objet il s\'agit, comme ceci :


```python
myObj = FreeCAD.ActiveDocument.getObject("myObjectName")
print(myObj.TypeId)
```

ou vérifier si un objet est dérivé de l\'un des objets de base (créé avec une fonction Part, ou une fonction Mesh, etc) :


```python
print(myObj.isDerivedFrom("Part::Feature"))
```

Maintenant, vous pouvez vraiment commencer à vous amuser avec FreeCAD ! Pour une liste complète des modules disponibles et de leurs outils, visitez la section [Catégorie : API](:Category:API/fr.md). {{Top}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > FreeCAD Scripting Basics/fr

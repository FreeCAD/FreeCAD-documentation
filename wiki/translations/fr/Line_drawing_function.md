# Line drawing function/fr
## Introduction

Cette page montre comment des fonctionnalités avancées peuvent être facilement créées en Python. Dans cet exercice, nous allons créer un nouvel outil qui trace une ligne. Cet outil peut ensuite être lié à une commande FreeCAD, et cette commande peut être appelée par n\'importe quel élément de l\'interface, comme un élément de menu ou un bouton de barre d\'outils.



## Script principal 

Nous allons d\'abord écrire un script contenant toutes nos fonctionnalités. Ensuite, nous l\'enregistrerons dans un fichier et l\'importerons dans FreeCAD pour rendre toutes ses classes et fonctions disponibles. Lancez votre éditeur de code préféré et tapez les lignes suivantes :


```python
import FreeCADGui, Part
from pivy.coin import *

class line:

    """This class will create a line after the user clicked 2 points on the screen"""

    def __init__(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[0], self.stack[1])
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
```


{{Top}}



## Explications détaillées 


```python
import Part, FreeCADGui
from pivy.coin import *
```

En Python, lorsque vous souhaitez utiliser des fonctions d\'un autre module, vous devez l\'importer. Dans notre cas, nous aurons besoin des fonctions de l\'[atelier Part](Part_Workbench/fr.md), pour créer la ligne, et du module Gui `FreeCADGui`, pour accéder à la [Vue 3D](3D_view/fr.md). Nous avons également besoin du contenu complet de la bibliothèque Coin afin de pouvoir utiliser directement tous les objets Coin comme `SoMouseButtonEvent` etc\...


```python
class line:
```

Ici, nous définissons notre classe principale.
Mais pourquoi utilisons-nous une classe et non une fonction ? La raison en est que nous avons besoin que notre outil reste \"vivant\" en attendant que l\'utilisateur clique sur l\'écran.
\* Une fonction se termine lorsque sa tâche est terminée,

-   mais un objet, **(une classe définit un objet)** reste en vie (actif) jusqu\'à ce qu\'il soit détruit.


```python
"""This class will create a line after the user clicked 2 points on the screen"""
```

En Python, toutes les classes ou fonctions peuvent avoir une documentation string(docstring). Ceci est particulièrement utile dans FreeCAD, parce que quand vous appelez cette classe dans l\'interpréteur, la description sera affichée comme une infobulle.


```python
def __init__(self):
```

Les classes Python doivent toujours contenir une fonction `__init__` qui est exécutée lorsque la classe est appelée pour créer un objet. Ici, nous allons mettre ici tout ce que nous voulons produire lorsque notre outil de création de ligne commence (appelé).


```python
self.view = FreeCADGui.ActiveDocument.ActiveView
```

Dans une classe, vous souhaitez généralement faire précéder `self.` les noms des variables afin de rendre les variables facilement accessibles à toutes les fonctions à l\'intérieur et à l\'extérieur de la classe. Ici, nous utiliserons `self.view` pour accéder à la vue 3D active et la manipuler.


```python
self.stack = []
```

Nous créons ici une liste vide qui contiendra les points 3D envoyés par la fonction `getpoint()`.


```python
self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)
```

C\'est la partie importante. Comme il s\'agit d\'une scène [Coin3D](https://github.com/coin3d/coin/wiki), nous utilisons un mécanisme de rappel de Coin qui permet d\'appeler une fonction chaque fois qu\'un certain événement de la scène se produit. Dans notre cas, nous créons un rappel pour les événements [SoMouseButtonEvent](https://coin3d.github.io/Coin/html/classSoMouseButtonEvent.html) et nous le lions à la fonction `getpoint()`. Désormais, chaque fois qu\'un bouton de la souris est enfoncé ou relâché, la fonction `getpoint()` sera exécutée.

Remarquez qu\'il existe également une alternative à `addEventCallbackPivy()` appelée `addEventCallback()` qui ne repose pas sur pivy. Mais comme le pivot est un moyen très efficace et naturel d\'accéder à n\'importe quelle partie de la scène des pièces, il est le meilleur choix. {{Top}} 
```python
def getpoint(self, event_cb):
```

Nous définissons maintenant la fonction `getpoint()` qui sera exécutée lorsqu\'un bouton de la souris est enfoncé dans une vue 3D. Cette fonction recevra un argument que nous appellerons `event_cb`. A partir de ce rappel d\'événement, nous pouvons accéder à l\'objet événement qui contient plusieurs informations (plus d\'informations [ici](Code_snippets/fr#Observer_des_évènements_de_la_souris_dans_la_vue_3D_via_Python.md)).


```python
if event.getState() == SoMouseButtonEvent.DOWN:
```

La fonction `getpoint()` sera appelée lorsqu\'un bouton de la souris est enfoncé ou relâché. Mais nous ne voulons choisir un point 3D que lorsqu\'un bouton est pressé, sinon nous nous retrouverions avec deux points 3D très proches l\'un de l\'autre. Nous devons donc vérifier cela ici.


```python
pos = event.getPosition()
```

Ici, nous avons les coordonnées du curseur de la souris sur l\'écran.


```python
point = self.view.getPoint(pos[0], pos[1])
```

Cette fonction nous donne le vecteur (x,y,z) du point qui se trouve sur le plan focal, juste sous curseur de notre souris. Si vous êtes dans la vue de la caméra, imaginez un rayon provenant de la caméra, en passant par le curseur de la souris, et en appuyant sur le plan focal. C\'est l\'emplacement de notre point 3D. Si nous sommes en vue orthogonale, le rayon est parallèle à la direction de la vue.


```python
self.stack.append(point)
```

Nous ajoutons notre nouveau point sur la pile.


```python
if len(self.stack) == 2:
```

Avons nous tous les points ? si oui, alors nous allons tracer la ligne !


```python
l = Part.LineSegment(self.stack[0], self.stack[1])
```

Nous utilisons ici la fonction `LineSegment()` de l\'atelier Part qui crée une ligne à partir de deux vecteurs FreeCAD. La ligne n\'est liée à aucun objet de notre document actif, donc rien n\'apparaît à l\'écran.


```python
shape = l.toShape()
```

Le document FreeCAD ne peut accepter que des formes à partir de Part Module. Les formes sont le type le plus courant de Part Module. Donc, nous devons transformer notre ligne en une forme avant de l\'ajouter au document.


```python
Part.show(shape)
```

Le Part module a une fonction très pratique `show()` qui crée un nouvel objet dans le document et se lie a une forme. Nous aurions aussi pu créer un nouvel objet dans le premier document et le lier à la forme manuellement.


```python
self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
```

Maintenant, nous en avons fini avec notre ligne, nous allons supprimer le mécanisme de rappel ici. 

## Tester le script 

Maintenant, sauvegardons notre script dans un dossier où l\'interpréteur FreeCAD Python peut le trouver. Lors de l\'importation de modules, l\'interpréteur cherchera aux endroits suivants: les chemins d\'installation de Python, le dossier FreeCAD **bin** et tous les dossiers FreeCAD **Mod** (module). La meilleure solution est donc de créer un nouveau dossier dans l\'un des dossiers **Mod**. Créons là un dossier **MyScripts** et enregistrons notre script dedans sous le nom **exercise.py**.

Maintenant, tout est prêt. Démarrons FreeCAD, créons un nouveau document, et dans le numéro de l\'interpréteur Python :


```python
import exercise
```

Si aucun message d\'erreur n\'apparaît, c\'est que notre script d\'exercice a été chargé avec succès. Nous pouvons maintenant vérifier son contenu avec :


```python
dir(exercise)
```

La commande `dir()` est une commande Python intégrée qui répertorie le contenu d\'un module. Nous pouvons vérifier que notre classe `line()` est là avec :


```python
'line' in dir(exercise)
```

Maintenant, testons-le :


```python
exercise.line()
```

Cliquez deux fois dans la vue 3D et bingo: voici notre ligne! Pour la répéter, tapez à nouveau 

## Enregistrement du script 

Pour que notre nouvel outil ligne soit vraiment utile et pour éviter d\'avoir à taper tout cela, il devrait avoir un bouton dans l\'interface. Une façon de faire est de transformer notre nouveau dossier **MyScripts** en un atelier FreeCAD complet. Il suffit de mettre un fichier appelé **InitGui.py** dans le dossier **MyScripts**. **InitGui.py** contiendra les instructions pour créer un nouvel atelier et y ajouter notre nouvel outil. En plus de cela, nous devrons également changer un peu notre code d\'exercice, de sorte que l\'outil `line()` soit reconnu comme une commande officielle de FreeCAD. Commençons par créer un fichier **InitGui.py** et y écrire le code suivant :


```python
class MyWorkbench (Workbench):

    MenuText = "MyScripts"

    def Initialize(self):
        import exercise
        commandslist = ["line"]
        self.appendToolbar("My Scripts", commandslist)

Gui.addWorkbench(MyWorkbench())
```

A présent, vous comprenez probablement le script ci-dessus. Nous créons une nouvelle classe que nous appelons `MyWorkbench`, nous lui donnons un titre `MenuText` et nous définissons une fonction `Initialize()` qui sera exécutée lorsque l\'atelier est chargé dans FreeCAD. Dans cette fonction, nous chargeons le contenu de notre fichier d\'exercice et ajoutons les commandes FreeCAD trouvées à l\'intérieur à une liste de commandes. Ensuite, nous créons une barre d\'outils appelée \"Mes scripts\" et nous y assignons notre liste de commandes. Actuellement, bien sûr, nous n\'avons qu\'un seul outil, donc notre liste de commandes ne contient qu\'un seul élément. Ensuite, une fois notre atelier prêt, nous l\'ajoutons à l\'interface principale.

Mais cela ne fonctionnera toujours pas car une commande FreeCAD doit être formatée d\'une certaine manière pour fonctionner, nous devrons changer notre outil `line()`. Notre nouveau script **exercise.py** devrait ressembler à ceci :


```python
import FreeCADGui, Part
from pivy.coin import *

class line:

    """This class will create a line after the user clicked 2 points on the screen"""

    def Activated(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[0], self.stack[1])
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)

    def GetResources(self):
        return {'Pixmap': 'path_to_an_icon/line_icon.png', 'MenuText': 'Line', 'ToolTip': 'Creates a line by clicking 2 points on the screen'}

FreeCADGui.addCommand('line', line())
```

Ce que nous avons fait ici est de transformer notre fonction `__init __()` en une fonction `Activated()`. Lorsque les commandes FreeCAD sont exécutées, elles exécutent automatiquement la fonction `Activated()`. Nous avons également ajouté une fonction `GetResources()`, qui informe FreeCAD où il peut trouver l\'icône de l\'outil et quel sera le nom et l\'infobulle de notre outil. Toute image **jpg**, **png** ou **svg** fonctionnera comme une icône, elle peut être de n\'importe quelle taille, mais il est préférable d\'utiliser une taille proche de l\'aspect final, comme 16x16, 24x24 ou 32x32. Ensuite, nous ajoutons la classe `line()` en tant que commande officielle de FreeCAD avec la méthode `addCommand()`.

Ça y est, nous avons juste besoin de redémarrer FreeCAD et nous aurons un plan de travail agréable avec notre nouvel outil **ligne** tout neuf ! 

## Vous voulez en savoir plus ? 

Si vous avez aimé cet exercise, pourquoi ne pas essayer d\'améliorer ce petit outil? Il y a beaucoup de choses à faire, comme par exemple :

-   Ajouter des commentaires d\'utilisateurs : jusqu\'à présent nous avons fait un outil très dépouillé, l\'utilisateur peut être un peu perdu lors de son utilisation. Vous pouvez ajouter vos commentaires, en guidant l\'utilisateur. Par exemple, vous pourriez émettre des messages à la console FreeCAD. \"Jetez\" un oeil dans le module `FreeCAD.Console`.
-   Ajouter la possibilité d\'entrer les coordonnées 3D manuellement. Regardez les fonctions Python `input()`, par exemple.
-   Ajouter la possibilité d\'ajouter plus de 2 points.
-   Ajouter des événements pour d\'autres fonctions: Maintenant que nous venons d\'apprendre les événements de bouton de souris, si nous souhaitons également faire quelque chose quand la souris est déplacée, comme par exemple l\'affichage des coordonnées actuelles ?
-   Donnez un nom à l\'objet créé et bien d\'autres choses.

N\'hésitez pas à poser des questions ou à partager des idées sur le [forum](https://forum.freecadweb.org/)! {{Top}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Line drawing function/fr

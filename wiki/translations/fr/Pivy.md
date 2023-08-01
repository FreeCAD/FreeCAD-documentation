# Pivy/fr
{{TOCright}}

## Introduction

[Pivy](Pivy/fr.md) est une bibliothèque de liaison [Python](Python/fr.md) pour [Coin](https://github.com/coin3d), la bibliothèque de rendu 3D utilisée dans FreeCAD pour afficher des éléments dans une [3D vue](3D_view/fr.md). Coin est une implémentation open source de la spécification \"Open Inventor\" pour gérer les graphiques. Par conséquent, dans FreeCAD, les termes \"Pivy\", \"Coin\" ou \"Open Inventor\" se réfèrent essentiellement à la même chose.

Lorsqu\'il est importé dans un interpréteur Python en cours d\'exécution, Pivy nous permet de communiquer directement avec n\'importe quel Coin [Graphe de scène](Scenegraph/fr.md), tel que la [vue 3D](3D_view/fr.md), ou même d\'en créer de nouveaux. Pivy n\'est pas nécessaire pour compiler FreeCAD, mais il est requis lors de l\'exécution lors de l\'exécution d\'établis basés sur Python qui créent des formes à l\'écran, comme [Draft](Draft_Workbench/fr.md) et [Arch](Arch_Workbench/fr.md). Pour cette raison, Pivy est normalement installé lors de l\'installation d\'une distribution de FreeCAD.

La bibliothèque Coin est divisée en plusieurs éléments, Coin lui-même pour manipuler les graphes de scènes et les liaisons pour plusieurs systèmes d\'interface graphique, tels que Windows et Qt. S\'ils sont présents sur le système, ces modules sont également disponibles pour Pivy. Le module Coin est toujours présent, et c\'est ce que nous utiliserons de toute façon, car nous n\'aurons pas besoin de nous soucier d\'ancrer notre affichage 3D dans aucune interface, ce qui est déjà fait par FreeCAD. Tout ce que nous devons faire est ceci:


```python
from pivy import coin
```

## Graphe de scène 

Nous avons vu dans la page [Graphe de scène](Scenegraph/fr.md) comment une scène Coin typique est organisée. Tout ce qui apparaît dans une [vue 3D](3D_view/fr.md) est un Graphe de scène Coin organisée de la même manière. Nous avons un nœud racine et tous les objets à l\'écran sont ses enfants.

FreeCAD a un moyen facile d\'accéder a la racine d\'une scène 3D:


```python
sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()
print(sg)
```

La racine de la scène 3D sera:


```python
<pivy.coin.SoSelection; proxy of <Swig Object of type 'SoSelection *' at 0x360cb60> >
```

Vous pouvez inspecter immédiatement les enfants (branches) de la scène 3D:


```python
for node in sg.getChildren():
    print(node)
```

Certains de ces nœuds, tels que `SoSeparator` ou `SoGroup`, peuvent avoir eux-mêmes des enfants. La liste complète des objets Coin est disponible dans la documentation officielle des Coin.

Maintenant essayons d\'ajouter quelque chose à notre scène (projet).
Nous allons ajouter un beau cube rouge:


```python
col = coin.SoBaseColor()
col.rgb = (1, 0, 0)
cub = coin.SoCube()
myCustomNode = coin.SoSeparator()
myCustomNode.addChild(col)
myCustomNode.addChild(cub)
sg.addChild(myCustomNode)
```

Maintenant, nous allons essayer ceci:


```python
col.rgb = (1, 1, 0)
```

Comme vous pouvez le voir, tout est toujours accessible et modifiable à la volée. Pas besoin de recalculer ou de redessiner quoi que ce soit, Coin s\'occupe de tout. Vous pouvez ajouter des éléments à votre graphe de scène, modifier les propriétés, masquer des éléments, afficher des objets temporaires, n\'importe quoi. Bien entendu, cela ne concerne que l\'affichage dans la vue 3D. Cet affichage est recalculé par FreeCAD lors de l\'ouverture d\'un fichier et lorsqu\'un objet doit être recalculé. Ainsi, si vous modifiez l\'aspect d\'un objet FreeCAD existant, ces modifications seront perdues si l\'objet est recalculé ou lorsque vous rouvrez le fichier.

Comme déjà mentionné, dans un graphe de scène openInventor, l\'ordre est important. Un nœud affecte ce qui vient ensuite. Par exemple, si nous voulons avoir la possibilité de déplacer notre cube, nous devrons ajouter un nœud `SoTranslation` **avant** le cube:


```python
col = coin.SoBaseColor()
col.rgb = (1, 0, 0)
trans = coin.SoTranslation()
trans.translation.setValue([0, 0, 0])
cub = coin.SoCube()
myCustomNode = coin.SoSeparator()
myCustomNode.addChild(col)
myCustomNode.addChild(trans)
myCustomNode.addChild(cub)
sg.addChild(myCustomNode)
```

Pour déplacer notre cube, nous pouvons maintenant faire:


```python
trans.translation.setValue([2, 0, 0])
```

Enfin, supprimer quelque chose se fait avec:


```python
sg.removeChild(myCustomNode)
```


{{Top}}

## Rappels (callback) 

Un [mécanisme de rappel](https://fr.wikipedia.org/wiki/Fonction_de_rappel) est un système qui permet à une bibliothèque, telle que notre bibliothèque Coin, de vous rappeler, c\'est-à-dire d\'appeler une certaine fonction depuis votre objet Python en cours d\'exécution. De cette façon, Coin peut vous informer qu\'un événement spécifique s\'est produit dans la scène. Coin peut regarder des choses très différentes, telles que la position de la souris, les clics sur les boutons de la souris, les touches du clavier enfoncées et bien d\'autres.

FreeCAD dispose d\'un moyen facile pour utiliser ces rappels:


```python
from pivy import coin

class ButtonTest:
    def __init__(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.callback = self.view.addEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), self.getMouseClick) 

    def getMouseClick(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == coin.SoMouseButtonEvent.DOWN:
            print("Alert!!! A mouse button has been improperly clicked!!!")
            self.view.removeEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), self.callback)

ButtonTest()
```

Le rappel doit être initié à partir d\'un objet, car cet objet doit toujours être en cours d\'exécution lorsque le rappel se produit. Voir aussi une [liste complète des événements possibles et leurs paramètres](Code_snippets/fr#Observer_des_.C3.A9v.C3.A8nements_de_la_souris_dans_la_vue_3D_via_Python.md) ou dans la documentation officielle de Coin. {{Top}}

## Documentation

Malheureusement, Pivy n'a pas sa propre documentation. Cependant, puisqu\'il s\'agit d\'un wrapper de la bibliothèque Coin, vous pouvez lire la référence C++ pour plus d\'informations. Dans ce cas, vous devez traduire le style de nommage de la classe C++ comme vous la liriez en Python.

En C++:


```python
SoFile::getClassTypeId()
```

Dans Pivy:


```python
SoFile.getClassId()
```

-   Page d\'accueil de [Coin3D](https://github.com/coin3d).
-   Page d\'accueil de [Pivy](https://github.com/coin3d/pivy).
-   Le [wikiCoin3D](https://github.com/coin3d/coin/wiki), sur GitHub.
-   La [documentation du wiki Coin3D](https://github.com/coin3d/coin/wiki/Documentation), sur GitHub.
-   La [Documentation Coin3D](https://coin3d.github.io/Coin/html/), dernière documentation Doxygen générée automatiquement.
-   [(Open)Inventor Mentor](https://webdocs.cs.ualberta.ca/~graphics/books/mentor.pdf) - recommandé.

### Plus ancien 

Ces liens fournissent une documentation de référence pour Coin v3.x. Les différences avec la v4.x sont minimes, elles peuvent donc toujours être utiles.

-   [Documentation Coin3D](https://coin3d.bitbucket.io/Coin/index.html), sur BitBucket.
-   [Coin3D Documentation](https://grey.colorado.edu/coin3d/index.html), à l\'Université du Colorado.
-   [Ouvrir la documentation de référence Inventor](https://mevislabdownloads.mevis.de/docs/current/MeVis/ThirdParty/Documentation/Publish/OpenInventorReference/index.html), par MeVisLab.


{{Top}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Pivy/fr

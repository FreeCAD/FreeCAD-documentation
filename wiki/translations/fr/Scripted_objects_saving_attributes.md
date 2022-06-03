# Scripted objects saving attributes/fr
{{TOCright}}

## Introduction

Les [Objets créés par script](Scripted_objects/fr.md) sont reconstruits à chaque fois qu\'un [document au format FCStd](File_Format_FCStd/fr.md) est ouvert. Pour ce faire, le document conserve une référence au module et à la classe Python qui ont été utilisés pour créer l\'objet, ainsi que ses propriétés.

Les attributs de la classe utilisée pour créer l\'objet peuvent également être enregistrés, c\'est-à-dire \"sérialisés\". Ceci peut être contrôlé par les méthodes `__getstate__` et `__setstate__` de la classe.

## Sauvegarde de tous les attributs 

Par défaut, les attributs enregistrés dans une classe d\'objets sont ceux du dictionnaire `__dict__` de la classe.


```python
# various_states.py
class VariousStates   *
    def __init__(self, obj)   *
        obj.addProperty("App   *   *PropertyLength", "Length")
        obj.addProperty("App   *   *PropertyArea", "Area")
        obj.Length = 15
        obj.Area = 300
        obj.Proxy = self

        Type = dict()
        Type["Version"] = "Custom"
        Type["Release"] = "production"
        self.Type = Type
        self.Type = "Custom"
        self.ver = "0.18"
        self.color = (0, 0, 1)
        self.width = 2.5

    def execute(self, obj)   *
        pass
```

Un objet peut être créé à l\'aide de cette classe et il peut être enregistré dans **my_document.FCstd**. Si aucun [viewprovider](viewprovider/fr.md) particulier n\'est attribué au nouvel objet, sa classe proxy est simplement définie sur une valeur différente de `None`, dans ce cas, sur `1`. 
```python
import FreeCAD as App
import various_states

doc = App.newDocument()
doc.FileName = "my_document.FCStd"

obj = doc.addObject("Part   *   *FeaturePython", "Custom")
various_states.VariousStates(obj)

if App.GuiUp   *
    obj.ViewObject.Proxy = 1

doc.recompute()
doc.save()
```

Lorsque nous rouvrons le fichier, nous pouvons inspecter le dictionnaire de la classe de l\'objet. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.Proxy)
<various_states.VariousStates object at 0x7f0a899bde10>
>>> print(obj.Proxy.__dict__)
{'Type'   * {'Version'   * 'Custom', 'Release'   * 'production'}, 'ver'   * '0.18', 'color'   * [0, 0, 1], 'width'   * 2.5}
```

Nous voyons que tous les attributs qui commencent par `self` dans la classe ont été sauvegardés. Ceux-ci peuvent être de différents types, notamment chaîne de caractères, liste, flottant et dictionnaire. Le tuple original pour `self.color` a été converti en liste, mais sinon tous les attributs ont été chargés de la même manière.

## Sauvegarde d\'attributs spécifiques 

Nous pouvons définir une classe similaire à la première, qui implémente des attributs spécifiques à sauvegarder. 
```python
# various_states.py
class CustomStates   *
    def __init__(self, obj)   *
        obj.addProperty("App   *   *PropertyLength", "Length")
        obj.addProperty("App   *   *PropertyArea", "Area")
        obj.Length = 15
        obj.Area = 300
        obj.Proxy = self

        Type = dict()
        Type["Version"] = "Custom"
        Type["Release"] = "production"
        self.Type = Type
        self.ver = "0.18"
        self.color = (0, 0, 1)
        self.width = 2.5

    def execute(self, obj)   *
        pass

    def __getstate__(self)   *
        return self.color, self.width

    def __setstate__(self, state)   *
        self.color = state[0]
        self.width = state[1]
```

La valeur de retour de `__getstate__` est l\'objet qui sera sérialisé. Il peut s\'agir d\'une valeur unique ou d\'un tuple de valeurs. Lorsque l\'objet est restauré, la classe appelle la méthode `__setstate__`, en passant la variable `state` avec le contenu sérialisé. Dans ce cas, `state` est un tuple qui est décomposé dans les variables respectives pour reconstruire l\'\"état\" qui existait à l\'origine. 
```python
state = (self.color, self.width)
state = ((0, 0, 1), 2.5)
```

Nous pouvons créer un objet avec cette classe et enregistrer le document, comme dans l\'exemple précédent. Lorsque nous rouvrons le fichier, nous pouvons inspecter le dictionnaire de la classe de l\'objet. 
```python
>>> obj2 = App.ActiveDocument.Custom2
>>> print(obj2.Proxy)
<various_states.CustomStates object at 0x7fb399496630>
>>> print(obj2.Proxy.__dict__)
{'color'   * [0, 0, 1], 'width'   * 2.5}
```

Le tuple original de `self.color` a été converti en liste, mais les autres informations ont été récupérées sans problème. Au lieu de restaurer tous les attributs comme dans le cas précédent, seuls les attributs que nous avons spécifiés dans `__getstate__` et `__setstate__` ont été restaurés.

## Utilisation

### Identifier le type 

Normalement, les [objets créés par script](scripted_objects/fr.md) devraient utiliser des [propriétés](property/fr.md) pour stocker des informations, car celles-ci sont automatiquement restaurées à l\'ouverture du document.

Cependant, il arrive que la classe restitue des informations internes qui ne sont pas destinées à être modifiées, mais qu\'il est utile d\'inspecter.

Par exemple, la plupart des objets de l\'[atelier Draft](Draft_Workbench/fr.md) configurent un attribut `Type` qui peut être utilisé pour déterminer le type d\'objet utilisé.


```python
class DraftObject   *
    def __init__(self, obj, _type)   *
        self.Type = _type

    def __getstate__(self)   *
        return self.Type

    def __setstate__(self, state)   *
        if state   *
            self.Type = state
```

Tous les objets ont une propriété `TypeId`, mais pour les [objets créés par script](scripted_objects/fr.md), cette propriété n\'est pas utile car elle fait toujours référence à la classe C++ parente, par exemple, [`Part   *   *Part2DObjectPython`](Part_Part2DObject/fr.md) ou [`Part   *   *FeaturePython`](Part_Feature/fr.md). Par conséquent, le fait d\'avoir cet attribut supplémentaire `Proxy.Type` dans la classe est utile pour traiter chaque objet d\'une manière particulière.

### Migration de l\'objet 

Les informations de version peuvent être stockées à l\'intérieur de la classe afin de vérifier l\'origine d\'un objet.


```python
class CustomObject   *
    def __init__(self, obj, _type)   *
        self.Type = _type
        self.version = "0.18"

    def __getstate__(self)   *
        return self.Type, self.version

    def __setstate__(self, state)   *
        if state   *
            self.Type = state[0]
            self.version = state[1]
```

Si la structure de la classe change, c\'est-à-dire si ses propriétés ou méthodes changent, sont renommées ou supprimées, nous pourrions tester l\'attribut version afin de faire migrer l\'ancien objet vers un nouvel ensemble de propriétés ou vers une nouvelle classe. Ceci peut être fait en implémentant la méthode `onDocumentRestored`, comme expliqué dans [Migration d\'objets créés par script](Scripted_objects_migration/fr.md).


```python
class CustomObject   *
    def onDocumentRestored(self, obj)   *
        if hasattr(obj.Proxy, "version") and obj.Proxy.version   *
            if obj.Proxy.version == "0.18"   *
                self.migrate_from_018(obj)

    def migrate_from_018(self, obj)   *
        ...
```

## Liens

-   [Objets créés par script](Scripted_objects/fr.md)
-   [Migration d\'objets créés par script](Scripted_objects_migration/fr.md)
-   [Discussion sur le forum FreeCAD    * Sérialisation des objets scripts    * json ou pickle ?](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=49120)

-   [obj.Proxy.Type est un dict, pas une chaîne de caractères](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=44009), explication de `__getstate__` et `__setstate__` dans le forum.
-   [Le module Pickle](https   *//docs.python.org/3/library/pickle.html#object.__getstate__) dans la documentation Python.


 

[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripted objects saving attributes/fr

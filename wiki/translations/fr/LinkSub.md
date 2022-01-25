# LinkSub/fr
## Description

Une [LinkSub](LinkSub/fr.md) est une structure de données qui est utilisée comme une entrée pour diverses fonctions et objets. Son but est de transmettre un sous-objet ou un sous-élément (sommet, arête ou face) d\'un objet à un autre objet qui utilisera ou transformera cette géométrie.

Un LinkSub est composé d\'une liste de deux arguments. 
```python
sub = [argument1, argument2]
```

Le premier argument est une référence à un [objet document](App_DocumentObject/fr.md) et le second argument est une chaîne de texte indiquant le nom interne du sous-élément. Ce nom a un numéro commençant par un et jusqu\'au nombre total de ces sous-éléments. 
```python
sub = [obj1, "Vertex1"]
sub = [obj2, "Face1"]
sub = [obj3, "Edge1"]
```

Le deuxième argument peut lui-même être une liste de chaînes, indiquant divers sous-éléments du même objet document. 
```python
sub1 = [obj1, ["Vertex1", "Vertex2"]]
sub2 = [obj2, ["Face1", "Face3", "Face5"]]
sub3 = [obj3, ["Vertex1", "Face5", "Edge1", "Edge2"]]
```

Il est possible de voir qu\'une [LinkSubList](LinkSubList/fr.md) est une liste de structures [LinkSub](LinkSub/fr.md).

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md), [LinkSubList](LinkSubList/fr.md).

Un nouvel [Objet créé par script](scripted_objects/fr.md) peut accepter une LinkSub en ajoutant la [propriété](property/fr.md) correspondante.

Il est important de recalculer les objets avant que leurs sous-éléments ne soient utilisés comme entrée pour d\'autres objets, sinon une erreur peut se produire car la géométrie peut ne pas contenir une [Forme](Part_TopoShape/fr.md) valide.


```python
doc = App.newDocument()

cube = doc.addObject("Part::Box", "Cube")
cyl = doc.addObject("Part::Cylinder", "Cylinder")
doc.recompute()

new_obj = doc.addObject("App::FeaturePython", "New")
new_obj.addProperty("App::PropertyLinkSub", "Geometry")
new_obj.Geometry = [cube, ["Vertex1", "Vertex2"]]

new_obj2 = doc.addObject("App::FeaturePython", "New")
new_obj2.addProperty("App::PropertyLinkSub", "Geometry")
new_obj2.Geometry = [cyl, "Edge1"]

doc.recompute()
```

Le sous-élément peut ensuite être extrait de la propriété affectée et peut être manipulé pour faire quelque chose. 
```python
>>> new_obj.Geometry
(<Part::PartFeature>, ['Vertex1', 'Vertex2'])

>>> new_obj.Geometry[1]
['Vertex1', 'Vertex2']

>>> new_obj.Geometry[1][1]
'Vertex2'

>>> new_obj.Geometry[1][1].strip("Vertex")
'2'

>>> int(new_obj.Geometry[1][1].strip("Vertex"))
2
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > LinkSub/fr

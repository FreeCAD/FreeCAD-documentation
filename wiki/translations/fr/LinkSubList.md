# LinkSubList/fr
## Description

Une [LinkSubList](LinkSubList/fr.md) est une structure de données qui est utilisée comme une entrée pour diverses fonctions et objets. Son but est de transmettre un sous-objet ou un sous-élément (sommet, arête ou face) d\'un objet à un autre objet qui utilisera ou transformera cette géométrie.

Un LinkSubList est composé d\'une liste de tuples. 
```python
sublist = [tuple1, tuple2, tuple3, ...]
```

Chaque tuple contient au moins deux éléments. Le premier élément est une référence à un [objet document](App_DocumentObject/fr.md) et le deuxième élément est une chaîne de texte indiquant le nom interne du sous-élément. Ce nom a un numéro commençant par un et jusqu\'au nombre total de ces sous-éléments. 
```python
tuple1 = (obj1, "Vertex1")
tuple2 = (obj2, "Face1")
tuple3 = (obj3, "Edge1")
```

Le deuxième élément du tuple peut lui-même être une liste de chaînes, indiquant divers sous-éléments du même objet document. 
```python
tuple1 = (obj1, ["Vertex1", "Vertex2"])
tuple2 = (obj2, ["Face1", "Face3", "Face5"])
tuple3 = (obj3, ["Vertex1", "Face5", "Edge1", "Edge2"])
```

Il est possible de voir qu\'une [LinkSubList](LinkSubList/fr.md) est une liste de [LinkSub](LinkSub/fr.md) structures. Chaque tuple est en fait un [LinkSub](LinkSub/fr.md).

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md), [LinkSub](LinkSub/fr.md).

Un nouvel [Objet créé par script](scripted_objects/fr.md) peut accepter une LinkSubList en ajoutant la [propriété](property/fr.md) correspondante.

Il est important de recalculer les objets avant que leurs sous-éléments ne soient utilisés comme entrée pour d\'autres objets, sinon une erreur peut se produire car la géométrie peut ne pas contenir une [Forme](Part_TopoShape/fr.md) valide.


```python
doc = App.newDocument()

cube = doc.addObject("Part::Box", "Cube")
cyl = doc.addObject("Part::Cylinder", "Cylinder")
doc.recompute()

new_obj = doc.addObject("App::FeaturePython", "New")

new_obj.addProperty("App::PropertyLinkSubList", "Geometry")
new_obj.Geometry = [(cube, ["Vertex1", "Vertex2"]),
                    (cyl, "Edge1")]
doc.recompute()
```

Le sous-élément peut ensuite être extrait de la propriété affectée et peut être manipulé pour faire quelque chose. 
```python
>>> new_obj.Geometry
[(<Part::PartFeature>, ('Vertex1', 'Vertex2')), (<Part::PartFeature>, ('Edge1',))]

>>> new_obj.Geometry[0]
(<Part::PartFeature>, ('Vertex1', 'Vertex2'))

>>> new_obj.Geometry[0][1]
('Vertex1', 'Vertex2')

>>> new_obj.Geometry[0][1][1]
'Vertex2'

>>> new_obj.Geometry[0][1][1].strip("Vertex")
'2'

>>> int(new_obj.Geometry[0][1][1].strip("Vertex"))
2
```


{{Powerdocnavi

}}

---
[documentation index](../README.md) > LinkSubList/fr

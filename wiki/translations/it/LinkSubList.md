# LinkSubList/it
## Descrizione

Un [LinkSubList](LinkSubList/it.md) è una struttura dati che viene utilizzata come input per varie funzioni e oggetti; il suo scopo è passare un sottooggetto o sottoelemento (vertice, bordo o faccia) da un oggetto a un altro oggetto che utilizzerà o trasformerà quella geometria.

Un LinkSubList è composto da un elenco di tuple. 
```python
sublist = [tuple1, tuple2, tuple3, ...]
```

Ogni tupla contiene almeno due elementi; il primo elemento è un riferimento a un [oggetto documento](App_DocumentObject/it.md) e il secondo elemento è una stringa di testo che indica il nome interno del sottoelemento. Questo nome ha un numero che inizia con uno e va fino al numero totale di tali sottoelementi. 
```python
tuple1 = (obj1, "Vertex1")
tuple2 = (obj2, "Face1")
tuple3 = (obj3, "Edge1")
```

Il secondo elemento della tupla può essere esso stesso un elenco di stringhe, che indica vari sottoelementi dello stesso oggetto documento. 
```python
tuple1 = (obj1, ["Vertex1", "Vertex2"])
tuple2 = (obj2, ["Face1", "Face3", "Face5"])
tuple3 = (obj3, ["Vertex1", "Face5", "Edge1", "Edge2"])
```

È possibile vedere che un [LinkSubList](LinkSubList/it.md) è un elenco di strutture [LinkSub](LinkSub/it.md). Ogni tupla è infatti un [LinkSub](LinkSub/it.md).

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), [LinkSub](LinkSub/it.md).

Un nuovo [oggetto da script](scripted_objects/it.md) può accettare un LinkSubList aggiungendo la [proprietà](property/it.md) corrispondente.

It is important to recompute the objects before their subelements are used as input for other objects, otherwise an error may be produced as the geometry may not contain a valid [Shape](Part_TopoShape.md).


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

Il sottoelemento può quindi essere estratto dalla proprietà assegnata e può essere manipolato per fare qualcosa. 
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
[documentation index](../README.md) > LinkSubList/it

# LinkSubList/de
## Beschreibung

Ein [LinkSubList](LinkSubList/de.md)-Objekt ist eine Datenstruktur, die als Eingabe für verschiedene Funktionen und Objekte verwendet wird; seine Aufgabe ist es ein Unterobjekt oder Unterelement (Knoten, Kante, oder Fläche) von einem Objekt an ein anderes Objekt zu übergeben, das diese Geometrie verwendet oder verändert.

Ein LinkSubList-Objekt besteht aus einer Liste von Tupeln. 
```python
sublist = [tuple1, tuple2, tuple3, ...]
```

Each tuple contains at least two elements; the first element is a reference to a [document object](App_DocumentObject.md), and the second element is a text string indicating the internal name of the subelement. This name has a number starting with one, and up to the total number of those subelements. 
```python
tuple1 = (obj1, "Vertex1")
tuple2 = (obj2, "Face1")
tuple3 = (obj3, "Edge1")
```

The second element of the tuple can itself be a list of strings, indicating various subelements of the same document object. 
```python
tuple1 = (obj1, ["Vertex1", "Vertex2"])
tuple2 = (obj2, ["Face1", "Face3", "Face5"])
tuple3 = (obj3, ["Vertex1", "Face5", "Edge1", "Edge2"])
```

It is possible to see that a [LinkSubList](LinkSubList.md) is a list of [LinkSub](LinkSub.md) structures. Each tuple is in fact a [LinkSub](LinkSub.md).



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

A new [scripted object](scripted_objects.md) can accept a LinkSubList by adding the corresponding [property](property.md).

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

The subelement can then be extracted from the assigned property, and can be manipulated to do something. 
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



---
⏵ [documentation index](../README.md) > LinkSubList/de

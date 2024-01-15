# LinkSub/de
## Beschreibung

Ein [LinkSub](LinkSub/de.md)-Objekt ist eine Datenstruktur, die als Eingabe für verschiedene Funktionen und Objekte verwendet wird; seine Aufgabe ist es ein Unterobjekt oder Unterelement (Knoten, Kante, oder Fläche) von einem Objekt an ein anderes Objekt zu übergeben, das diese Geometrie verwendet oder verändert.

Ein LinkSub besteht aus einer Liste mit zwei Argumenten. 
```python
sub = [argument1, argument2]
```

Das erste Argument ist eine Referenz eines[Dokumentobjekts](App_DocumentObject/de.md) (document object) und das zweite Argument ist eine Text-Zeichenkette, die den internen Namen des Unterelements anzeigt. Dieser Name enthält eine Zahl, zwischen 1 und der Gesamtanzahl der Unterelemente. 
```python
sub = [obj1, "Vertex1"]
sub = [obj2, "Face1"]
sub = [obj3, "Edge1"]
```

Das zweite Argument kann selbst eine Liste von Zeichenketten sein, die verschiedene Unterelemente desselben Dokumentobjekts anzeigt. 
```python
sub1 = [obj1, ["Vertex1", "Vertex2"]]
sub2 = [obj2, ["Face1", "Face3", "Face5"]]
sub3 = [obj3, ["Vertex1", "Face5", "Edge1", "Edge2"]]
```

Man kann erkennen, dass ein [LinkSubList](LinkSubList/de.md)-Objekt eine Liste von [LinkSub](LinkSub/de.md)-Strukturen ist.



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

A new [scripted object](scripted_objects.md) can accept a LinkSub by adding the corresponding [property](property.md).

It is important to recompute the objects before their subelements are used as input for other objects, otherwise an error may be produced as the geometry may not contain a valid [Shape](Part_TopoShape.md).


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

The subelement can then be extracted from the assigned property, and can be manipulated to do something. 
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
⏵ [documentation index](../README.md) > LinkSub/de

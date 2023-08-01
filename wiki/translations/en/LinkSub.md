# LinkSub/en
## Description

A [LinkSub](LinkSub.md) is a data structure that is used as input to various functions and objects; its purpose is to pass a subobject or subelement (vertex, edge, or face) from an object to another object that will use or transform that geometry.

A LinkSub is composed of a list of two arguments. 
```python
sub = [argument1, argument2]
```

The first argument is a reference to a [document object](App_DocumentObject.md), and the second argument is a text string indicating the internal name of the subelement. This name has a number starting with one, and up to the total number of those subelements. 
```python
sub = [obj1, "Vertex1"]
sub = [obj2, "Face1"]
sub = [obj3, "Edge1"]
```

The second argument can itself be a list of strings, indicating various subelements of the same document object. 
```python
sub1 = [obj1, ["Vertex1", "Vertex2"]]
sub2 = [obj2, ["Face1", "Face3", "Face5"]]
sub3 = [obj3, ["Vertex1", "Face5", "Edge1", "Edge2"]]
```

It is possible to see that a [LinkSubList](LinkSubList.md) is a list of [LinkSub](LinkSub.md) structures.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), [LinkSubList](LinkSubList.md).

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
![](images/Button_right.svg) [documentation index](../README.md) > LinkSub/en

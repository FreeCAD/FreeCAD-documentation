# Scripted objects saving attributes/it
{{TOCright}}

## Introduzione

Gli [oggetti creati con script](Scripted_objects/it.md) vengono ricostruiti ogni volta che viene aperto un documento FCStd. Per fare ciò il documento mantiene un riferimento al modulo e alla classe Python che sono stati usati per creare l\'oggetto, insieme alle sue proprietà.

Attributes of the class used to create the object can also be saved, that is, \"serialized\". This can be further controlled by the `__getstate__` and `__setstate__` methods of the class.

## Saving all attributes 

By default, attributes saved in an object class are those from the `__dict__` dictionary of the class.


```python
# various_states.py
class VariousStates:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "Area")
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

    def execute(self, obj):
        pass
```

An object can be created using this class, and it can be saved to **my_document.FCstd**. If no particular [viewprovider](viewprovider.md) is assigned to the new object, its proxy class is simply set to a value different from `None`, in this case, to `1`. 
```python
import FreeCAD as App
import various_states

doc = App.newDocument()
doc.FileName = "my_document.FCStd"

obj = doc.addObject("Part::FeaturePython", "Custom")
various_states.VariousStates(obj)

if App.GuiUp:
    obj.ViewObject.Proxy = 1

doc.recompute()
doc.save()
```

When we re-open the file we can inspect the dictionary of the object\'s class. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.Proxy)
<various_states.VariousStates object at 0x7f0a899bde10>
>>> print(obj.Proxy.__dict__)
{'Type': {'Version': 'Custom', 'Release': 'production'}, 'ver': '0.18', 'color': [0, 0, 1], 'width': 2.5}
```

We see that all attributes that start with `self` in the class were saved. These can be of different types, including string, list, float, and dictionary. The original tuple for `self.color` was converted to a list, but otherwise all attributes were loaded the same.

## Saving specific attributes 

We can define a class similar to the first one, that implements specific attributes to save. 
```python
# various_states.py
class CustomStates:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "Area")
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

    def execute(self, obj):
        pass

    def __getstate__(self):
        return self.color, self.width

    def __setstate__(self, state):
        self.color = state[0]
        self.width = state[1]
```

The return value of `__getstate__` is the object that will be serialized. This can be a single value, or a tuple of values. When the object is restored, the class calls the `__setstate__` method, passing the `state` variable with the serialized content. In this case `state` is a tuple that is unpacked into the respective variables to reconstruct the \"state\" that original existed. 
```python
state = (self.color, self.width)
state = ((0, 0, 1), 2.5)
```

We can create an object with this class, and save the document, just like in the previous example. When we re-open the file we can inspect the dictionary of the object\'s class. 
```python
>>> obj2 = App.ActiveDocument.Custom2
>>> print(obj2.Proxy)
<various_states.CustomStates object at 0x7fb399496630>
>>> print(obj2.Proxy.__dict__)
{'color': [0, 0, 1], 'width': 2.5}
```

The original tuple for `self.color` was converted to a list, but otherwise the information was recovered fine. Instead of restoring all attributes like in the previous case, only the attributes that we specified in `__getstate__` and `__setstate__` were restored.

## Usage

### Identifying the type 

Normally, [scripted objects](scripted_objects.md) should use [properties](property.md) to store information, as these are automatically restored when the document is opened.

However, sometimes the class restore internal information which is not intended to be modified, but which is helpful to inspect.

For example, most objects of the [Draft Workbench](Draft_Workbench.md) set up a `Type` attribute that can be used to determine the type of object that is under use.


```python
class DraftObject:
    def __init__(self, obj, _type):
        self.Type = _type

    def __getstate__(self):
        return self.Type

    def __setstate__(self, state):
        if state:
            self.Type = state
```

All objects have a `TypeId` property, but for [scripted objects](scripted_objects.md) this property is not useful, as it always refers to the parent C++ class, for example, [`Part::Part2DObjectPython`](Part_Part2DObject.md) or [`Part::FeaturePython`](Part_Feature.md). Therefore, having this additional `Proxy.Type` attribute in the class is useful to treat each object in a particular way.

### Migrating the object 

Version information can be stored inside the class in order to verify the origin of an object.


```python
class CustomObject:
    def __init__(self, obj, _type):
        self.Type = _type
        self.version = "0.18"

    def __getstate__(self):
        return self.Type, self.version

    def __setstate__(self, state):
        if state:
            self.Type = state[0]
            self.version = state[1]
```

If the structure of the class changes, that is, if its properties or methods change, are renamed, or are removed, we could test the version attribute in order to migrate the older object to a new set of properties or to a new class. This can be done by implementing the `onDocumentRestored` method, as explained in [Scripted objects migration](Scripted_objects_migration.md).


```python
class CustomObject:
    def onDocumentRestored(self, obj):
        if hasattr(obj.Proxy, "version") and obj.Proxy.version:
            if obj.Proxy.version == "0.18":
                self.migrate_from_018(obj)

    def migrate_from_018(self, obj):
        ...
```

## Links

-   [Scripted objects](Scripted_objects.md)
-   [Scripted objects migration](Scripted_objects_migration.md)
-   [FreeCAD Forum Discussion: Scripted Object Serialization: json or pickle?](https://forum.freecadweb.org/viewtopic.php?f=10&t=49120)

-   [obj.Proxy.Type is a dict, not a string](https://forum.freecadweb.org/viewtopic.php?f=18&t=44009), explanation of `__getstate__` and `__setstate__` in the forum.
-   [The Pickle module](https://docs.python.org/3/library/pickle.html#object.__getstate__) in the Python documentation.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripted objects saving attributes/it

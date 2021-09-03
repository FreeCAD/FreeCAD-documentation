


{{TOCright}}

## Einführung

[Geskriptete Objekte](Scripted_objects/de.md) werden jedes Mal neu aufgebaut, wenn ein [FCStd Dokument](File_Format_FCStd/de.md) geöffnet wird. Zu diesem Zweck behält das Dokument eine Referenz auf das Modul und die Python Klasse, die zur Erstellung des Objekts verwendet wurden, zusammen mit seinen Eigenschaften.

Attribute der Klasse, die zur Erstellung des Objekts verwendet wurde, können ebenfalls gespeichert, d.h. \"serialisiert\" werden. Dies kann weiter durch die `__getstate__` und `__setstate__` Methoden der Klasse gesteuert werden.

## Speichern aller Attribute {#speichern_aller_attribute}

Standardmäßig werden in einer Objektklasse die Attribute aus dem `__dict__` Wörterbuch der Klasse gespeichert.


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

Mit dieser Klasse kann ein Objekt erstellt und unter {{Dateiname|mein_Dokument.FCstd}} gespeichert werden. Wenn dem neuen Objekt kein bestimmter [Ansichtsanbieter](viewprovider/de.md) zugewiesen ist, wird seine Proxy Klasse einfach auf einen anderen Wert als `None` gesetzt, in diesem Fall auf `1`. 
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

Wenn wir die Datei erneut öffnen, können wir das Wörterbuch der Klasse des Objekts einsehen. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.Proxy)
<various_states.VariousStates object at 0x7f0a899bde10>
>>> print(obj.Proxy.__dict__)
{'Type': {'Version': 'Custom', 'Release': 'production'}, 'ver': '0.18', 'color': [0, 0, 1], 'width': 2.5}
```

Wir sehen, dass alle Attribute, die in der Klasse mit `self` beginnen, gespeichert wurden. Diese können von unterschiedlichem Typ sein, einschließlich Zeichenfolge, Liste, Fließkommazahl und Wörterbuch. Das ursprüngliche Tupel für `self.color` wurde in eine Liste konvertiert, aber ansonsten wurden alle Attribute gleich geladen.

## Speichern besonderer Attribute {#speichern_besonderer_attribute}

Wir können eine Klasse ähnlich der ersten definieren, die bestimmte Attribute zum Speichern implementiert. 
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

### Identifying the type {#identifying_the_type}

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

### Migrating the object {#migrating_the_object}

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


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)

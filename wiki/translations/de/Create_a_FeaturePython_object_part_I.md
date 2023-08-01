# Create a FeaturePython object part I/de
{{TOCright}}



## Einführung

FeaturePython-Objekte (auch als [Skriptgenerierte Objekte](Scripted_objects/de.md) bezeichnet) bieten die Möglichkeit, FreeCAD mit Objekten zu erweitern, die sich nahtlos in die FreeCAD-Struktur integrieren.

Das ermutigt:

-   Schnelle Prototypenerstellung von neuen Objekten und Werkzeugen mit benutzerdefinierten Python-Klassen.
-   Speichern und Wiederherstellen von Daten (auch als Serialisierung bekannt) durch `App::Property`-Objekte, ohne dass ein Skript in die FreeCAD-Dokumentdatei eingebettet wird.
-   Kreative Freiheit, FreeCAD für jede Aufgabe anzupassen.

Auf dieser Seite werden wir ein funktionierendes Beispiel für eine benutzerdefinierte FeaturePython-Klasse konstruieren, wobei wir alle wichtigen Komponenten identifizieren und ein Verständnis dafür gewinnen, wie alles funktioniert, während wir vorankommen.



## Wie funktioniert es? 

FreeCAD wird mit einer Reihe von standard Objekttypen zur Verwaltung verschiedener Arten von Geometrie ausgeliefert. Einige von ihnen haben \"FeaturePython\"-Alternativen, die eine Anpassung mit einer benutzerdefinierten Python-Klasse ermöglichen.

Diese benutzerdefinierte Python-Klasse nimmt einen Verweis auf eines dieser Objekte und modifiziert es. Zum Beispiel kann die Python-Klasse dem Objekt Eigenschaften hinzufügen oder es mit anderen Objekten verknüpfen. Außerdem kann die Python-Klasse bestimmte Methoden implementieren, um das Objekt in die Lage zu versetzen, auf Dokumentereignisse zu reagieren, wodurch es möglich wird, Änderungen von Objekteigenschaften und Neuberechnungen von Dokumenten abzufangen.

Bei der Arbeit mit benutzerdefinierten Klassen und FeaturePython-Objekten ist es wichtig zu wissen, dass die benutzerdefinierte Klasse und ihr Zustand nicht im Dokument gespeichert werden, da dies die Einbettung eines Skripts in eine FreeCAD-Dokumentdatei erfordern würde, was ein erhebliches Sicherheitsrisiko darstellen würde. Nur das FeaturePython-Objekt selbst wird gespeichert (serialisiert). Da aber der Pfad des Skriptmoduls im Dokument gespeichert ist, muss ein Benutzer nur den Code der benutzerdefinierten Python-Klasse als importierbares Modul installieren und dabei der gleichen Ordnerstruktur folgen, um die verlorene Funktionalität wiederzuerlangen.

[Anfang](#top.md)



## Einrichten der Dinge 

FeaturePython-Objektklassen müssen in FreeCAD als importierbare Module fungieren. Das bedeutet, dass du sie in einem Pfad platzieren musst, der in deiner Python Umgebung existiert (oder füge ihn speziell hinzu). Für die Zwecke dieses Tutoriums werden wir den FreeCAD-Benutzerordner Macro verwenden. Aber wenn du eine andere Idee im Kopf hast, kannst du diese stattdessen verwenden.

If you don\'t know where the FreeCAD Macro folder is type `FreeCAD.getUserMacroDir(True)` in FreeCAD\'s [Python console](Python_console.md):

-   On Linux it is usually **/home/<username>/.local/share/FreeCAD/Macro/** (<small>(v0.20)</small> ) or **/home/<username>/.FreeCAD/Macro/** ({{VersionMinus|0.19}}).
-   On Windows it is **%APPDATA%\FreeCAD\Macro\**, which is usually **C:\Users\<username>\Appdata\Roaming\FreeCAD\Macro\**.
-   On macOS it is usually **/Users/<username>/Library/Application Support/FreeCAD/Macro/**.

Now we need to create some folders and files:

-   In the **Macro** folder create a new folder called **fpo**.
-   In the **fpo** folder create an empty file: **__init__.py**.
-   In the **fpo** folder, create a new folder called **box**.
-   In the **box** folder create two files: **__init__.py** and **box.py** (leave both empty for now).

Your folder structure should look like this:

Macro/
    |--> fpo/
        |--> __init__.py
        |--> box/
            |--> __init__.py
            |--> box.py

The **fpo** folder provides a nice place to play with new FeaturePython objects and the **box** folder is the module we will be working in. **__init__.py** tells Python that there is an importable module in the folder, and **box.py** will be the class file for our new FeaturePython Object.

With our module paths and files created, let\'s make sure FreeCAD is set up properly:

-   Start FreeCAD (if you haven\'t done so already).
-   Enable the [Report view](Report_view.md) (**View → Panels → Report view**).
-   Enable the [Python console](Python_console.md) (**View → Panels → Python console**) see [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

Finally, navigate to the **Macro/fpo/box** folder and open **box.py** in your favorite code editor. We will only edit that file.

[Anfang](#top.md)



## Ein FeaturePython-Objekt 

Let\'s get started by writing our class and its constructor:


```python
class box():

    def __init__(self, obj):
        """
        Default constructor
        """

        self.Type = 'box'

        obj.Proxy = self
```

**The `__init__()` method breakdown:**

+++
|                                | Parameters refer to the Python class itself and the FeaturePython object that it is attached to. |
| `def __init__(self, obj):`           |                                                                                                  |
|                                            |                                                                                                  |
+++
|                                | String definition of the custom Python type.                                                     |
| `self.Type <nowiki>=</nowiki> 'box'` |                                                                                                  |
|                                            |                                                                                                  |
+++
|                                | Stores a reference to the Python instance in the FeaturePython object.                           |
| `obj.Proxy <nowiki>=</nowiki> self`  |                                                                                                  |
|                                            |                                                                                                  |
+++

Add the following code at the top of the file:


```python
import FreeCAD as App

def create(obj_name):
    """
    Object creation method
    """

    obj = App.ActiveDocument.addObject('App::FeaturePython', obj_name)

    box(obj)

    return obj
```

**The `create()` method breakdown:**

+++
|                                       | Standard import for most Python scripts, the App alias is not required.                                                                                                                                                                        |
| `import FreeCAD as App`                     |                                                                                                                                                                                                                                                |
|                                                   |                                                                                                                                                                                                                                                |
+++
|                                       | Creates a new FreeCAD FeaturePython object with the name passed to the method. If there is no name clash, this will be the label and the name of the created object. Otherwise, a unique name and label will be created based on \'obj_name\'. |
| `obj <nowiki>=</nowiki> ... addObject(...)` |                                                                                                                                                                                                                                                |
|                                                   |                                                                                                                                                                                                                                                |
+++
|                                       | Creates our custom class instance.                                                                                                                                                                                                             |
| `box(obj)`                                  |                                                                                                                                                                                                                                                |
|                                                   |                                                                                                                                                                                                                                                |
+++
|                                       | Returns the FeaturePython object.                                                                                                                                                                                                              |
| `return obj`                                |                                                                                                                                                                                                                                                |
|                                                   |                                                                                                                                                                                                                                                |
+++

The `create()` method is not required, but it provides a nice way to encapsulate the object creation code.

[Anfang](#top.md)



### Testen des Codes 

Now we can test our new object. Save your code and return to FreeCAD. Make sure you have opened a new document, you can do this by pressing **Ctrl**+**N** or selecting **File → New**.

In the Python console type the following:


```python
from fpo.box import box
```

Now we need to create our object:


```python
mybox = box.create('my_box')
```

![ right](images/Fpo_treeview.png ) You should see a new object appear in the [Tree view](Tree_view.md) labelled \"my_box\".

Note that the icon is gray. FreeCAD is telling us that the object is not able to display anything in the [3D view](3D_view.md). Click on the object and look at its properties in the [Property editor](Property_editor.md). There is not much there, just the name of the object.

Also note that there is a small blue check mark next to the FeaturePython object in the Tree view. That is because when an object is created or changed it is \"touched\" and needs to be recomputed. Pressing the **<img src="images/Std_Refresh.svg" width=16px> [Std Refresh](Std_Refresh.md)** button will accomplish this. We will add some code to automate this later. 


Let\'s look at our object\'s attributes: 
```python
dir(mybox)
```

This will return:


```python
['Content', 'Document', 'ExpressionEngine', 'FullName', 'ID', 'InList',
...
'setPropertyStatus', 'supportedProperties', 'touch']
```

There are a lot of attributes because we\'re accessing the native FreeCAD FeaturePyton object created in the first line of our `create()` method. The `Proxy` property we added in our `__init__()` method is there too.

Let\'s inspect it with the `dir()` method:


```python
dir(mybox.Proxy)
```

This will return:


```python
['Type', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
...
'__str__', '__subclasshook__', '__weakref__']
```

We can see our `Type` property. Let\'s check it:


```python
mybox.Proxy.Type
```

This will return:


```python
'box'
```

This is indeed the assigned value, so we know we\'re accessing the custom class through the FeaturePython object.

Now let\'s see if we can make our class a little more interesting, and maybe more useful as well.

[top](#top.md)



### Hinzufügen von Eigenschaften 

Properties are the lifeblood of a FeaturePython class. Fortunately, FreeCAD supports [a number of property types](FeaturePython_Custom_Properties.md) for FeaturePython classes. These properties are attached directly to the FeaturePython object and are fully serialized when the file is saved. To avoid having to serialize data yourself, it is advisable to only use these property types.

Adding properties is done using the `add_property()` method. The syntax for the method is:

add_property(type, name, section, description)

You can view the list of supported properties by typing:


```python
mybox.supportedProperties()
```

Let\'s try adding a property to our box class. Switch to your code editor, move to the `__init__()` method, and at the end of the method add:


```python
obj.addProperty('App::PropertyString', 'Description', 'Base', 'Box description').Description = ""
```

Note how we\'re using the reference to the (serializable) FeaturePython object `obj`, and not the (non-serializable) Python class instance `self`.

Once you\'re done, save the changes and switch back to FreeCAD. Before we can observe the changes made to our code, we need to reload the module. This can be accomplished by restarting FreeCAD, but restarting FreeCAD every time we edit the code would be inconvenient. To make things easier type the following in the Python console:


```python
from importlib import reload
reload(box)
```

With the module reloaded, let\'s see what we get when we create an object:


```python
box.create('box_property_test')
```

You should see the new box object appear in the Tree view:

-   Select it and look at the Property editor. There, you should see the *Description* property.
-   Hover over the property name on the left and the tooltip should appear with the description you provided.
-   Select the field and type whatever you like. You\'ll notice that Python update commands are executed and displayed in the console as you type letters and the property changes.

[Anfang](#top.md)

Let\'s add some more properties. Return to your source code and add the following properties to the `__init__()` method:


```python
obj.addProperty('App::PropertyLength', 'Length', 'Dimensions', 'Box length').Length = 10.0
obj.addProperty('App::PropertyLength', 'Width', 'Dimensions', 'Box width').Width = '10 mm'
obj.addProperty('App::PropertyLength', 'Height', 'Dimensions', 'Box height').Height = '1 cm'
```

And let\'s also add some code to recompute the document automatically. Add the following line above the `return()` statement in the `create()` method :


```python
App.ActiveDocument.recompute()
```

**Be careful where you recompute a FeaturePython object. Recomputing should be handled by a method external to its class.**

![ right](images/fpo_box_properties.png )

Now, test your changes as follows:

-   Save your changes and reload your module.
-   Delete all objects in the Tree view.
-   Create a new box object from the Python console by calling `box.create('myBox')`.

Once the box is created and you\'ve checked to make sure it has been recomputed, select the object and look at its properties. You should note two things:

-   A new property group: *Dimensions*.
-   Three new properties: *Height*, *Length* and *Width*.

Note also how the properties have units. More specifically, they have taken on the linear units set in the user preferences (**Edit → Preference... → General → Units**). 


No doubt you noticed that three different values were entered for the dimensions: a floating-point value (`10.0`) and two different strings (`'10 mm'` and `'1 cm'`). The `App::PropertyLength` type assumes floating-point values are in millimeters, string values are parsed according to the units specified, and in the GUI all values are converted to the units specified in the user preferences (`mm` in the image). This built-in behavior makes the `App::PropertyLength` type ideal for dimensions.

[Anfang](#top.md)

### Trapping events 

The last element required for a basic FeaturePython object is event trapping. A FeaturePython object can react to events with callback functions. In our case we want the object to react whenever it is recomputed. In other words we want to trap recomputes. To accomplish this we need to add a function with a specific name, `execute()`, to the object class. There are several other events that can be trapped, both in the FeaturePython object itself and in the [ViewProvider](Viewprovider.md), which we\'ll cover in [Create a FeaturePython object part II](Create_a_FeaturePython_object_part_II.md).

For a complete reference of methods available to implement on FeautrePython classes, see [FeaturePython methods](FeaturePython_methods.md).

Add the following after the `__init__()` function:


```python
def execute(self, obj):
    """
    Called on document recompute
    """

    print('Recomputing {0:s} ({1:s})'.format(obj.Name, self.Type))
```

Test the code by again following these steps:

-   Save and reload the module.
-   Delete all objects.
-   Create a new box object.

You should see the printed output in the Python Console, thanks to the `recompute()` call we added to the `create()` method. Of course, the `execute()` method doesn\'t do anything here, except tell us that it was called, but it is the key to the magic of FeaturePython objects.

That\'s it, you now know how to build a basic, functional FeaturePython object!

[Anfang](#top.md)



### Vollständiger Code 


```python
import FreeCAD as App

def create(obj_name):
    """
    Object creation method
    """

    obj = App.ActiveDocument.addObject('App::FeaturePython', obj_name)

    box(obj)

    App.ActiveDocument.recompute()

    return obj

class box():

    def __init__(self, obj):
        """
        Default constructor
        """

        self.Type = 'box'

        obj.Proxy = self

        obj.addProperty('App::PropertyString', 'Description', 'Base', 'Box description').Description = ""
        obj.addProperty('App::PropertyLength', 'Length', 'Dimensions', 'Box length').Length = 10.0
        obj.addProperty('App::PropertyLength', 'Width', 'Dimensions', 'Box width').Width = '10 mm'
        obj.addProperty('App::PropertyLength', 'Height', 'Dimensions', 'Box height').Height = '1 cm'

    def execute(self, obj):
        """
        Called on document recompute
        """

        print('Recomputing {0:s} ({1:s})'.format(obj.Name, self.Type))
```

[Anfang](#top.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Create a FeaturePython object part I/de

# Scripted objects migration/de
## Einführung

[Geskriptete Objekte](Scripted_objects/de.md) werden jedes Mal neu aufgebaut, wenn ein [FCStd Dokument](File_Format_FCStd/de.md) geöffnet wird. Zu diesem Zweck behält das Dokument eine Referenz auf das Modul und die Python Klasse, die zur Erstellung des Objekts verwendet wurden, zusammen mit seinen Eigenschaften.


{{Code|lang=xml|code=
<Document SchemaVersion="4" ProgramVersion="0.19R20959 (Git)" FileVersion="1">
    ...
    <Properties Count="15" TransientCount="3">
    ...
    </Properties>
    <Objects Count="1" Dependencies="1">
        <ObjectDeps Name="Custom" Count="0"/>
        <Object type="Part::FeaturePython" name="Custom" id="2715" Touched="1" />
    </Objects>
    <ObjectData Count="1">
        <Object name="Custom">
            <Properties Count="9" TransientCount="0">
                ...
                <Property name="Proxy" type="App::PropertyPythonObject" status="1">
                    <Python value="eyJUeXBlIjogIkN1c3RvbSJ9" encoded="yes" module="old_module" class="OldObject"/>
                </Property>
                ...
            </Properties>
        </Object>
    </ObjectData>
</Document>
}}

Konzentriere dich besonders auf diesen Teil: {{Code|lang=xml|code=
                ...
                <Property name="Proxy" type="App::PropertyPythonObject" status="1">
                    <Python value="eyJUeXBlIjogIkN1c3RvbSJ9" encoded="yes" module="old_module" class="OldObject"/>
                </Property>
                ...
}}

Wenn der Wert von module= oder class= auf dem installierten System nicht gefunden wird, kann das Objekt nicht korrekt geladen werden. Das bedeutet, dass, sobald ein Objekt mit einer bestimmten Klasse erstellt wurde, das Modul nicht mehr verschoben oder umbenannt werden sollte, da zuvor gespeicherte Objekte sonst kaputt gehen.

Ein triftiger Grund für die Verschiebung oder Umbenennung des Moduls oder der Klasse ist jedoch die Verbesserung der Struktur und Wartbarkeit des ursprünglichen Codes, z.B. bei der Umstrukturierung einer ganzen Werkbank. In diesem Fall gibt es verschiedene Strategien, um alte Objekte auf die Verwendung einer neuen Klasse zu migrieren. Dies geschieht aus Gründen der Abwärtskompatibilität, wenn ein völliges Aufbrechen alter Dokumente vermieden werden muss.

## Altes Objekt und neues Objekt 

### Altes Objekt 

Ein altes Objekt wird in einem Baustein definiert, der sich an der Wurzel der Arbeitsbereichs befindet. 
```python
# old_module.py
class OldObject:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "Area")
        obj.Length = 15
        obj.Area = 300
        obj.Proxy = self
        self.Type = "Custom"

    def execute(self, obj):
        pass
```

Mit dieser Klasse kann ein Objekt erstellt und unter **mein_Dokument.FCstd** gespeichert werden. Wenn dem neuen Objekt kein bestimmter [Ansichtsanbieter](viewprovider/de.md) zugewiesen ist, wird seine Proxy Klasse einfach auf einen anderen Wert als `None` gesetzt, in diesem Fall auf `1`. 
```python
import FreeCAD as App
import old_module

doc = App.newDocument()
doc.FileName = "my_document.FCStd"

obj = doc.addObject("Part::FeaturePython", "Custom")
old_module.OldObject(obj)

if App.GuiUp:
    obj.ViewObject.Proxy = 1

doc.recompute()
doc.save()
```

[Python Konsole](Python_console/de.md) Sitzung, bei der die grundlegenden Eigenschaften weggelassen wurden. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.PropertiesList)
['Area', ..., ..., ..., 'Length', ..., ..., ..., ...]
>>> print(obj.Proxy)
<old_module.OldObject object at 0x7efc3c51c390>
```

### Neues Objekt 

Nun betrachten wir, dass der Arbeitsbereich umstrukturiert wird, so dass sich die Klassen nicht nur im Stammverzeichnis, sondern stattdessen in einem **objects** Verzeichnis befinden. Komplexe Arbeitsbereiche, die viele verschiedene Arten von Objekten haben, sollten in Verzeichnissen strukturiert werden, die Objekte, [AnsichtBereitsteller](Viewprovider/de.md), [Gui Befehle](Command/de.md), [Aufgabenpaneel](task_panel/de.md) Schnittstellen usw. enthalten. 
```python
# objects/new_module.py
class NewObject:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "GeneralArea")
        obj.addProperty("App::PropertyInteger", "Divisions")
        obj.Length = 30
        obj.GeneralArea = 600
        obj.Divisions = 4
        obj.Proxy = self
        self.Type = "Custom"

    def execute(self, obj):
        pass
```

Diese neue Klasse wird sich auf den gleichen Objekttyp beziehen, aber sowohl der Modulname als auch der Klassenname wurden umbenannt. Darüber hinaus haben sich auch die Eigenschaften geändert; eine Eigenschaft wurde umbenannt, und eine völlig neue Eigenschaft wurde hinzugefügt.

Wenn wir ein neues Objekt mit diesem neuen Modul erstellen, haben wir die folgende Konsolensitzung. 
```python
>>> obj2 = App.ActiveDocument.Custom2
>>> print(obj2.PropertiesList)
['Divisions', ..., 'GeneralArea', ..., ..., 'Length', ..., ..., ..., ...]
>>> print(obj2.Proxy)
<objects.new_module.NewObject object at 0x7efc1cf68c50>
```

## Methode 1. Migration durch Umleitung der Klasse 

Wir werden das ältere Objekt migrieren, indem wir die alte Klasse umleiten. Die ursprüngliche Klasse wird gelöscht, und der Name der Klasse wird einfach umgeleitet, um auf die neue Klasse zu verweisen.


```python
# old_module.py
import objects.new_module as new_module

OldObject = new_module.NewObject
```

Jedes Dokument, das versucht, `old_module.OldObject` zu laden, wird stattdessen zum Laden von `objects.new_module.NewObject` umgeleitet.

Wenn wir das Dokument öffnen und die Eigenschaften des Objekts in der [Python Konsole](Python_console/de.md) überprüfen, werden wir sehen, dass die älteren Eigenschaften erhalten bleiben, das Objekt aber eine neue Proxy Klasse hat. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.PropertiesList)
['Area', ..., ..., ..., 'Length', ..., ..., ..., ...]
>>> print(obj.Proxy)
<objects.new_module.NewObject object at 0x7f099700b2b0>
```

In diesem Fall sehen wir jedoch nicht die neuen Eigenschaften der neuen Klasse. Der Grund dafür ist einfach, dass das ältere Objekt diese Eigenschaften nicht hatte. Wenn `old_module.OldObject` zu `objects.new_module.NewObject` umgeleitet wurde, änderte sich nur die Proxy Klasse, aber die vorherigen Informationen wurden beibehalten.

Wenn das Dokument nun gespeichert und wieder geöffnet wird, sucht es automatisch nach `objects.new_module.NewObject`, und es benötigt nicht mehr `old_module.OldObject`. Die Datei **old_module.py** kann dauerhaft aus dem System entfernt werden, solange alle älteren Objekte in das neue Modul migriert worden sind. Wenn das alte Modul entfernt wird, aber ein Objekt nicht migriert wurde, zeigt die [Berichtsansicht](report_view/de.md) beim Öffnen eines Dokuments, das ein solches Objekt enthält, eine Meldung wie diese an.


{{Code|lang=bash|code=
<class 'ModuleNotFoundError'>: No module named 'old_module'
}}

Wenn es realistischerweise nicht möglich ist, alle älteren Objekte zu migrieren, z.B. weil das alte Modul viele Jahre lang in einem Arbeitsbereich verwendet wurde, muss **old_module.py** so lange beibehalten werden, wie es für notwendig erachtet wird, um den Benutzern die Möglichkeit zu geben, ihre Objekte zu migrieren.

### Vor- und Nachteile 

**Vorteile**

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Dies ist die einfachste Methode, bei der lediglich eine alte Klasse in eine neue Klasse umgeleitet werden muss.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Alte Eigenschaften bleiben erhalten, solange die neue Klasse sie nicht außer Kraft setzt.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Dies ist gut, wenn die alte Klasse und die neue Klasse die gleichen Eigenschaften haben (die gleiche Art von Daten verarbeiten), aber nur ihr Modul- oder Klassenname unterschiedlich ist.

**Nachteile**

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Die neue Klasse behält die alten Eigenschaften des Objekts bei, was nicht immer erwünscht ist.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Neue Eigenschaften oder umbenannte Eigenschaften werden nicht behandelt, so dass das Objekt zwar geladen wird, aber möglicherweise nicht das korrekte Verhalten der neuen Klasse zeigt.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Das alte Modul muss möglicherweise auf unbestimmte Zeit aufbewahrt werden, um alle alten, in der Vergangenheit erstellten Objekte zu migrieren.

## Methode 2. Migration beim Wiederherstellen des Dokuments 

Wir werden das ältere Objekt migrieren, indem wir die alte Klasse modifizieren. Der Großteil der ursprünglichen Klasse wird gelöscht, und stattdessen wird die Methode `onDocumentRestored` implementiert. Wenn diese Methode vorhanden ist, wird sie ausgeführt, wenn das Dokument versucht, ein Objekt wiederherzustellen, das die Klasse verwendet. Dies ist also die Gelegenheit, eine neue Klasse zuzuweisen, die Informationen zu manipulieren oder Nachrichten zu drucken.

In diesem Fall nehmen wir an, dass wir auch einen neuen [AnsichtBereitsteller](viewprovider/de.md) im Modul **viewp/new_view.py** definiert haben. Wenn wir diese Klasse nicht migrieren wollen, können wir nach der Prüfung `App.GuiUp` alles weglassen. 
```python
# old_module.py
import FreeCAD as App
import objects.new_module as new_module
import viewp.new_view as new_view
_wrn = App.Console.PrintWarning

class OldObject:
    def onDocumentRestored(self, obj):
        new_module.NewObject(obj)
        _wrn("New proxy class used\n")

        if App.GuiUp:
            new_view.ViewProviderNew(obj.ViewObject)
            _wrn("New viewprovider class used\n")
```

In einem komplexeren Beispiel wird zunächst geprüft, ob die Proxy Klasse dem gesuchten Typ entspricht, und erst dann mit der Migration fortgefahren, wenn es sich um den richtigen Typ handelt. 
```python
class OldObject:
    def onDocumentRestored(self, obj):
        if hasattr(obj, "Proxy") and obj.Proxy.Type == "Custom":
            _module = str(obj.Proxy.__class__)
            _module = _module.lstrip("<class '").rstrip("'>")

            if _module == "old_module.OldObject":
                self._migrate(obj)

    def _migrate(self, obj):
        _wrn("New proxy class used\n")
        new_module.NewObject(obj)

        if App.GuiUp:
            new_view.ViewProviderNew(obj.ViewObject)
            _wrn("New viewprovider class used\n")
```

Wenn wir davon ausgehen, dass wir das alte Modul bereits auf diese Weise geändert haben, werden wir, wenn wir ein Dokument mit einem alten Objekt öffnen, die Meldungen sehen, in denen die Verwendung der neuen Klassen erwähnt wird.

Wenn wir das Objekt von der [Python Konsole](Python_console/de.md) aus inspizieren, werden wir sehen, dass die älteren Eigenschaften erhalten geblieben sind, und zusätzlich wurden zusammen mit der neuen Proxy Klasse neue Eigenschaften hinzugefügt. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.PropertiesList)
['Area', 'Divisions', ..., 'GeneralArea', ..., ..., 'Length', 'Length1', ..., ..., ..., ...]
>>> print(obj.Proxy)
<objects.new_module.NewObject object at 0x7fecb0ebd7b8>
```

Die alten Eigenschaften waren `Area` und `Length`; die neuen Eigenschaften sind `Divisions`, `GeneralArea` und `Length`. Das migrierte Objekt behält die beiden ursprünglichen Eigenschaften bei und erhält drei neue Eigenschaften. Da die neue `Length` jedoch denselben Namen wie die ältere Eigenschaft hat, wird die neue Eigenschaft mit einer inkrementellen Nummer umbenannt. Vermutlich ist dies nicht das, was wir wollen. Wir können die Situation verbessern, indem wir dem Zusatz 2.1 unten folgen.

Da die Klassen den gleichen Objekttyp behandeln sollen, wünschen wir uns eine Migration, bei der sich `Area` in `GeneralArea` verwandelt und `Length` einfach dem neuen `Length` zugewiesen wird und es keine doppelten Eigenschaften gibt.

### Vor- und Nachteile 

**Vorteile**

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> This method allows us to check that the class that we are migrating is the right class, instead of simply redirecting to a newer class.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Similar to method 1, old properties are kept as long as the new class doesn\'t override them.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Unlike method 1, new properties are always added, however if they have the same name, they will be renamed.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> The migration is not immediate, we can still manipulate the information, or print messages while the object loads.

**Nachteile**

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> It is more verbose than method 1 because we need to implement the `onDocumentRestored` method to migrate the object.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> It always adds the new properties, so it may create duplicated properties in case the new properties have the same name as the old properties. This has to be handled manually.

## Methode 3. Migration beim Wiederherstellen des Dokuments, manuelle Handhabung der Eigenschaften 

This is an extension of method 2. In the `onDocumentRestored` method we need to save the values of the properties that we want, and then we can remove these original properties. This is done so that when the new class is used, it will assign the new properties without risking name collisions with the older properties.

Like in method 2, if we want we can also add the piece of code that checks that the Proxy class is the right one. In this example once more we assume that we are using a custom [viewprovider](Viewprovider.md), with at least one custom property. 
```python
# old_module.py
import FreeCAD as App
import objects.new_module as new_module
import viewp.new_view as new_view
_wrn = App.Console.PrintWarning

class OldObject:
    def onDocumentRestored(self, obj):
        old = dict()
        old["Area"] = obj.Area
        old["Length"] = obj.Length
        obj.removeProperty("Area")
        obj.removeProperty("Length")

        new_module.NewObject(obj)

        obj.GeneralArea = 3 * old["Area"]
        obj.Length = old["Length"]
        _wrn("New proxy class used; properties migrated\n")

        if App.GuiUp:
            vobj = obj.ViewObject
            old = dict()

            old["LineScale"] = vobj.LineScale
            vobj.removeProperty("LineScale")

            new_view.ViewProviderNew(vobj)

            vobj.LineScale = 1.05 * old["LineScale"]
            _wrn("New viewprovider class used; view properties migrated\n")
```

We can see that the old values are stored in an auxiliary dictionary, then the old properties are removed, then we add the new class, and finally we assign the previously saved values to the new properties. In this moment we can transform the saved values as necessary for the new class. For example, the `GeneralArea` is set to 3 times the old `Area`, and the new `Length` simply receives the value of the old `Length`. As we know how the old and new classes are supposed to behave, we have the liberty of manipulating the data to migrate the object as we want.

We can only remove properties that were added by [Python](Python.md) classes when we built the [scripted object](scripted_objects.md). Other attributes belong to the base C++ object and can\'t be removed. 
```python
>>> obj.removeProperty("Visibility")
False
```

Assuming that we already changed the old module in this way, if we open a document with an old object, we will see the messages mentioning the use of the new classes. Inspecting the object from the [Python console](Python_console.md) we see that the older properties are removed, and only the new properties exist. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.PropertiesList)
['Divisions', ..., 'GeneralArea', ..., ..., 'Length', ..., ..., ..., ...]
>>> print(obj.Proxy)
<objects.new_module.NewObject object at 0x7efd456c9b00>
```

Since in the old class the `Divisions` property didn\'t exist, nothing was done with it. It simply was created by the new `objects.new_module.NewObject` class.

### Vor- und Nachteile 

**Vorteile**

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Similar to method 2, this method allows us to check that the class that we are migrating is the right class.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> We have complete control of what to do with the old properties. Typically they will be removed so that there is no name collision with new properties added. Thus we avoid duplicated properties.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> By saving the older values, we can manipulate the information in the restoring step as we want, and assign the corresponding values to the new properties.

**Nachteile**

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> This method is very verbose compared to the previous ones, because we must implement the `onDocumentRestored` method, and handle each of the properties individually (save value, delete property, re-assign value). This is problematic if the object that we want to migrate has many properties, or their values need to be transformed in very special ways.

## Zusatz A. Erstellen der Eigenschaften nur, wenn sie noch nicht vorhanden sind 

One of the disadvantages of method 2 is that it will always try to add the new properties. If the older properties have the same name as the new properties, they will be duplicated with an incremental number, so `Length` will result in `Length1`, then `Length2`, and so on. This makes method 2 an unrealistic option in most cases, because the new class will only use one property anyway.

To improve this method, the new class can also be modified to only add the properties if they don\'t already exist by the same name. 
```python
# objects/new_module.py
class NewObject:
    def __init__(self, obj):
        if not hasattr(obj, "Length"):
            obj.addProperty("App::PropertyLength", "Length")
            obj.Length = 30
        if not hasattr(obj, "GeneralArea"):
            obj.addProperty("App::PropertyArea", "GeneralArea")
            obj.GeneralArea = 600
        if not hasattr(obj, "Divisions"):
            obj.addProperty("App::PropertyInteger", "Divisions")
            obj.Divisions = 4

        obj.Proxy = self
        self.Type = "Custom"

    def execute(self, obj):
        pass
```

In this case, since `Length` already exists, it won\'t be added again; `GeneralArea` and `Divisions` don\'t exist, so these will be added. And just like before, `Area` will be retained because it is not explicitly removed, although possibly it is no longer used in the new class. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.PropertiesList)
['Area', 'Divisions', ..., 'GeneralArea', ..., ..., 'Length', ..., ..., ..., ...]
>>> print(obj.Proxy)
<objects.new_module.NewObject object at 0x7f036bd4c6a0>
```

The same can be done for the class of the [viewprovider](viewprovider.md).

By using this method 2 + A, the result is similar to method 1 in that the object will retain all previous properties, but in addition it will gain the new properties provided by the new class.

Method 3 does not need this addendum to the new class because the older properties are explicitly removed, so there won\'t be any conflicts when installing the new properties. Nevertheless, it is still a good practice that every class adds its required properties only if these don\'t already exist. This is helpful both in the case of creating new [scripted objects](scripted_objects.md) or in migrating them.

### Vor- und Nachteile 

**Vorteile**

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> The object will retain all previous properties, but in addition it will gain new properties without repetition.

**Nachteile**

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Like method 2, it still doesn\'t deal with renamed properties. The old properties should be manually removed.

## Zusatz B. Migrieren verschiedener Versionen des alten Objekts 

Method 3 is the most complex method because the properties are handled individually. However, in this method we also have full flexibility in how we manipulate the data, and this is an advantage if we want to do complex operations.

If from the beginning we create a property that holds the version number of our object, we can use this number in the future to perform specific migration from that version to any other. We set the property to be read-only, so that we cannot overwrite it in the [property editor](property_editor.md), although it is still accessible from the [Python console](Python_console.md). 
```python
# old_module.py
class OldObject:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "Area")
        obj.addProperty("App::PropertyString", "Version")
        obj.setEditorMode("Version", 1)
        obj.Length = 15
        obj.Area = 300
        obj.Version = "0.18"
        obj.Proxy = self
        self.Type = "Custom"

    def execute(self, obj):
        pass
```

Then, when we want to migrate the object, we implement the `onDocumentRestored` method, and test for this version. 
```python
# old_module.py
import FreeCAD as App
import objects.new_module as new_module
_wrn = App.Console.PrintWarning

class OldObject:
    def onDocumentRestored(self, obj):
        if hasattr(obj, "Version") and obj.Version:
            if obj.Version == "0.18":
                _migrate_from_018(obj)
            elif obj.Version == "0.19":
                _migrate_from_019(obj)

def _migrate_from_018(obj):
    old = dict()
    old["Area"] = obj.Area
    old["Length"] = obj.Length
    obj.removeProperty("Area")
    obj.removeProperty("Length")
    obj.removeProperty("Version")

    new_module.NewObject(obj)

    obj.GeneralArea = 3 * old["Area"]
    obj.Length = old["Length"]
    obj.Version = "0.20"
    _wrn("New proxy class used; properties migrated\n")

def _migrate_from_019(obj):
    ...
```

We don\'t save the `Version` value as we will set a new `Version` number when doing the migration. As shown in the example, we can implement various functions for each corresponding version of the object that we intend to migrate. We omit the migration of the [viewprovider](viewprovider.md) properties but it follows the same pattern.

### Vor- und Nachteile 

**Vorteile**

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> We have complete control of what to do with the old properties, and how to perform the migration.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> We can implement a particular method to migrate a particular version of the old object.

**Nachteile**

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> This method is very verbose because we must have a clear idea on how to handle each of the properties of each \"version\" that we want to migrate. If our object has many different versions created over the years, we may have to prepare a long list of methods to migrate them to the newest object.

## Zusatz B2. Verwendung interner Klassenattribute anstelle von Eigenschaften 

Instead of using a [property](property.md) of the object to hold the version information, we can use an attribute of the class. In this way we \"hide\" the version information, because properties are normally public, and visible in the [property editor](property_editor.md), while class attributes can only be manipulated from the [Python console](Python_console.md). Class attributes can be saved and restored as explained in [Scripted objects saving attributes](Scripted_objects_saving_attributes.md). 
```python
# old_module.py
class OldObject:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "Area")
        obj.Length = 15
        obj.Area = 300
        obj.Proxy = self

        self.Type = "Custom"
        self.ver = "0.18"

    def execute(self, obj):
        pass
```

This attribute is inspected by looking at the `Proxy` attribute. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.Proxy.ver)
0.18
```

Then the file is modified to migrate the object. 
```python
# old_module.py
import FreeCAD as App
import objects.new_module as new_module
_wrn = App.Console.PrintWarning

class OldObject:
    def onDocumentRestored(self, obj):
        if hasattr(obj.Proxy, "ver") and obj.Proxy.ver:
            if obj.Proxy.ver == "0.18":
                _migrate_from_018(obj)

def _migrate_from_018(obj):
    old = dict()
    old["Area"] = obj.Area
    old["Length"] = obj.Length
    obj.removeProperty("Area")
    obj.removeProperty("Length")

    new_module.NewObject(obj)

    obj.GeneralArea = 3 * old["Area"]
    obj.Length = old["Length"]
    _wrn("New proxy class used; properties migrated\n")
```

When we install the new class, this new class should set the new value of the version attribute, for example, self.ver = "0.20".

## Zusatz C. Methode 3 ohne Entfernung alter Eigenschaften mit gleichem Namen 

Like in Addendum A, we can write the new class to create properties only if they aren\'t already present. Using method 3, we save the values of the older properties, and subsequently delete the older properties. However, if the new properties are named the same as the older ones, we don\'t need to delete the older ones, we can just reuse the same property, as we know the property won\'t be duplicated. If we are using Addendum B, we have a way to query the version as well.


```python
# old_module.py
import FreeCAD as App
import objects.new_module as new_module
_wrn = App.Console.PrintWarning

class OldObject:
    def onDocumentRestored(self, obj):
        if hasattr(obj, "Version") and obj.Version:
            if obj.Version == "0.18":
                _migrate_from_018(obj)

def _migrate_from_018(obj):
    old = dict()
    old["Area"] = obj.Area
    obj.removeProperty("Area")

    new_module.NewObject(obj)

    obj.GeneralArea = 3 * old["Area"]
    obj.Version = "0.20"
    _wrn("New proxy class used; properties migrated\n")
```

As we see in the example, the old `Area` property is deleted and migrated to the new `GeneralArea` property as usual. We do not need to delete `Length` nor `Version` because in the new class they are still used with the same name, and they won\'t be created again (addendum A). As we don\'t want to modify `Length`, this property is not touched at all; it is migrated to the new class silently. However, we do update `Version` to the new value. We omit the migration of the [viewprovider](viewprovider.md) properties but it follows the same pattern.

This should work like method 3, meaning that the old properties are removed and only the new properties remain in the new object. The only difference is that we omit removing and recreating the properties that are named the same. This process should work as long as the old [property](property.md) and the new [property](property.md) have the same type (for example, `App::PropertyLength` or `App::PropertyArea`), so the old property can pass its value directly. However, if the new property has a different type than the old property, then the old property should be removed, otherwise the old property will completely overwrite the new property, which is probably not what we want because the new class will be expecting the new type and not the old type.

### Vor- und Nachteile 

**Vorteile**

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Like method 3, this method allows us complete control of the migration of the old information.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> We avoid writing code that removes and recreates properties that are named the same.

**Nachteile**

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Like method 3, this method is still very verbose because we have to handle the properties carefully.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> If a new [property](property.md) and an old [property](property.md) share the same name, the new property will be overwritten, which may be undesired behavior, especially if the two properties have different types. In this case, removing the old property, and migrating its value manually is still necessary.

## Zusammenfassung

Jede der Methoden hat eine empfohlene Anwendung:

-   Methode 1. Das Modul wird verschoben oder umbenannt, aber die Eigenschaften sind die gleichen. Einfache Umleitung von Klassen, da die Eigenschaften überhaupt nicht geändert werden müssen.
-   Methode 2+A. Einfache Migrationsszenarien. Anzeige einer Nachricht, wenn das Objekt von einer Klasse in eine andere migriert wird. Die Eigenschaften sind vom gleichen Typ und brauchen überhaupt nicht geändert zu werden.
-   Methode 3, 3+A oder 3+B. Komplexe Migrationsszenarien. Volle Kontrolle über die Eigenschaften, Löschen der alten Eigenschaften und Hinzufügen neuer Eigenschaften. Ein Identifikator zur Kenntnis der Version des Objekts ist nützlich, um die richtige Funktion zur Durchführung der Migration zu wählen (Zusatz B oder B2).

Vermeide vorzugsweise Folgendes:

-   Methode 2. Die Eigenschaften werden dupliziert, wenn die neue Klasse nicht auf vorhandene Eigenschaften prüft (Zusatz A).
-   Methode 3+C. Nur verwenden, wenn die alten Eigenschaften und die neuen Eigenschaften vom gleichen Typ sind. Andernfalls verwende Methode 3 oder 3+B, um ältere Eigenschaften zu entfernen, und behandele sie genau nach Bedarf.

## Verweise

-   [Migrating and upgrading old scripted objects](https://forum.freecadweb.org/viewtopic.php?t=42948)
-   [Migrate old scripted objects](https://forum.freecadweb.org/viewtopic.php?f=18&t=46218)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Scripted objects migration/de

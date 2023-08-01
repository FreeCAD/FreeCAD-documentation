# Object name/de
## Einleitung


{{TOCright}}

Alle Objekte im Programm haben einen [Objektnamen](Object_name/de.md), der sie in einem bestimmten Dokument eindeutig identifiziert.

Diese Informationen gelten für alle Objekte, die von einem Dokumentobjekt ([App DocumentObject](App_DocumentObject/de.md), d.h. der Klasse {{Incode|App::DocumentObject}})abgeleitet sind, die im Wesentlichen alle Objekte umfasst, die in einem Dokument erstellt werden können.



## Namen

Namen besitzen verschiedene Eigenschaften:

-   Der `Name` darf nur einfache alphanumerische Zeichen, und den Unterstrich enthalten, `[_0-9a-zA-Z]`.
-   Der `Name` darf nicht mit einer Zahl beginnen; er muss mit mit einem Buchstaben oder Unterstrich beginnen, `[_a-zA-Z]`.
-   Der `Name` wird zum Zeitpunkt der Erstellung des Objekts vergeben und kann danach nicht mehr verändert werden. Der Name kann nie geändert werden.
-   Der `Name` darf im gesamten Dokument nur ein einziges Mal vorkommen. Dabei ist es egal, ob zwei Objekte komplett unterschiedlich sind wie z.B. eine [PartDesign Tasche](PartDesign_Pocket/de.md) und eine [Arch Wand](Arch_Wall/de.md); sie müssen unterschiedliche Namen besitzen.
-   Werden Objekte der gleichen Art erstellt, wird der Name mit einer fortlaufenden Zahl ergänzt; ds ergibt `Box`, `Box001`, `Box002` usw. Das verhindert doppelte Namen.
-   Sobald ein Objekt gelöscht wurde, kann sein `Name` wieder für ein neu erstelltes Objekt verwendet werden. Das heißt, wenn die Objekte `Box`, `Box001` und `Box002` vorhanden sind und das erste gelöscht wird, bekommt das nächste Objekt [Part Box](Part_Box.md) nicht den Namen `Box003`, sondern wieder `Box`, da diese Zeichenkette erneut verwendet werden kann. Es ist zu beachten, dass die Namen `Box001` oder `Box002` nicht in `Box` geändert werden können, da sie unveränderlich sind.

Zusammengefasst stellt der `Name` einen eindeutigen Identifikator (unique identifier, UID) eines Objekts dar. Da ein eindeutiger `Name` sehr eingeschränkt ist, besitzen Objekte auch noch die Eigenschaft `Label`, die ermöglicht, das Objekt \"umzubenennen\", also eine besser beschreibende Benennung hinzuzufügen. Der interne `Name` bleibt tatsächlich unverändert, aber die vom Benutzer editierbare Benennung `Label` kann in den meisten Fällen an Stelle des `Namens` verwendet werden. In der üblichen Verwendung im Programm bezieht sich \"umbenennen\" auf das `Label` (Benennung) und nicht auf den wirklichen `Namen` des Objekts.



## Benennungen

There are various properties for Labels:

-   The `Label` can accept any UTF8 string, including accents and spaces.
-   The [tree view](tree_view.md) actually displays the `Label` of the object, not the `Name`. Therefore, whenever a new object is created, it is a good practice to change the `Label` to a more descriptive string. To rename (relabel) the object, select it in the tree view and press **F2** (or rather **Return** on macOS), or open the context menu (right-click) and choose **Rename**.
-   Even after an object was renamed (relabelled), the internal `Name` will still be reported in many places, for example, in the [status bar](Status_bar.md) or in the [selection view](Selection_view.md), when the object is selected.
-   Since the internal functions of the program refer to the objects by `Name`, many dialogs will display the `Name` first, followed by the user editable `Label` in parentheses, for example, `Box (Extruded piece)`.
-   By default the `Label` is unique, just like the `Name`. However, this behavior can be changed in the [preferences editor](Preferences_Editor.md), **Edit → Preferences → General → Document → Allow duplicate object labels in one document**. This means that in general the `Label` is not unique in the document, and may actually be repeated. However, the recommendation is to keep the `Label` unique, as this is probably what is most useful to identify different objects. When writing custom functions that manipulate objects, the methods should use the `Name` of the object rather than its `Label` to guarantee that the correct object is used.
-   When using [expressions](Expressions.md), for example, in the [property editor](Property_editor.md) or in a [spreadsheet](Spreadsheet.md), the Label can be referenced using double brackets made of the less than and greater than symbols.


```python
<<Custom Label With Spaces>>.Height
<<Label may use UTF8 characters>>.Width
```

### Label2

It is a simple string that can contain arbitrary text, and therefore can be used for documenting (describing with more detail) the created object.

-   In the [tree view](Tree_view.md) edit the field next to the icon, under \"Description\", by clicking on it and pressing **F2** (or rather **Return** on macOS).
-   You can also change this property by modifying the `Label2` attribute from the [Python console](Python_console.md).
-   The **Label2** attribute is normally hidden in the [property editor](Property_editor.md) but can be made visible by opening the context menu (right click) and selecting **Show all**.



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md) und [Skriptgenerierte Objekte](Scripted_objects/de.md).

Any object in the software is internally created with the `addObject()` method of the document. The majority of 2D and 3D objects that the user will see in the [3D view](3D_view.md) are derived from a [Part Feature](Part_Feature.md). In the following example, the object created is a [Part Box](Part_Box.md).


```python
import FreeCAD as App

doc = App.newDocument()
obj = doc.addObject("Part::Box", "Name")
obj.Label = "Custom label"
```

### Name

The `addObject` function has two basic string arguments.

-   The first argument indicates the type of object, in this case, `"Part::Box"`.
-   The second argument is a string that defines the `Name` attribute. If it is not provided, it defaults to the same name as the class of the object, that is, `"Part__Box"`, where the two invalid symbols, the colons `::`, are replaced by two underscores `__`.
    -   The `Name` can only include simple alphanumeric characters, and the underscore, `[_0-9a-zA-Z]`. If other symbols are given, these will be converted to underscores; for example, `"A+B:C*"` is converted to `"A_B_C_"`.
    -   The `Name` cannot start with a number; it must start with a letter or the underscore, `[_a-zA-Z]`. For example, `"123ABC"` is converted to `"_23ABC"`.
    -   The `Name` is fixed at creation time; it cannot be modified afterwards.
    -   The `Name` must be unique in the entire document. If the same `"Name"` is used, a sequential number will be appended automatically so that the resulting names are unique; for example, if `"Name"` already exists, then new objects will be called `"Name001"`, `"Name002"`, `"Name003"`, etc.



### Benennung

The `Label` is a property of the created object and can be changed to a more meaningful text.

-   Upon creating the object, the `Label` is the same as the `Name`.
-   However, unlike the `Name`, the `Label` can accept any UTF8 string, including accents and spaces.
-   The `Label` can be changed at any point in time just by assigning the desired string, obj.Label = "New label"



### Ein Objekt mit Namen oder Benennung aufrufen 

All objects in a document are data attributes of the corresponding [Document](App_DocumentObject.md) object. The attribute\'s name correspond to the internal `Name` of the object.


```python
import FreeCAD as App

obj1 = App.ActiveDocument.Box
obj2 = App.ActiveDocument.Box001
obj3 = App.ActiveDocument.Box002
```

This is equivalent to using the `getObject` method of the Document. 
```python
import FreeCAD as App

obj1 = App.ActiveDocument.getObject('Box')
obj2 = App.ActiveDocument.getObject('Box001')
obj3 = App.ActiveDocument.getObject('Box002')
```

However, it is also possible to get the object by the more descriptive `Label`. 
```python
import FreeCAD as App

obj1 = App.ActiveDocument.getObjectsByLabel("Concrete wall")[0]
obj2 = App.ActiveDocument.getObjectsByLabel("Custom parallelepiped")[0]
obj3 = App.ActiveDocument.getObjectsByLabel("Some special name for this cube__002")[0]
```

Given that the `Label` is in general not unique, the `getObjectsByLabel` method returns a list with all objects found with that `Label`. However, if the `Label` is unique in the document then the first element in that list should be the desired object.



---
![](images/Button_right.svg) [documentation index](../README.md) > Object name/de

# Object name/pt-br
## Introdução


{{TOCright}}

All objects in the program have an [object name](Object_name.md) that uniquely identifies them in a given [Document](App_Document.md).

This information applies to all objects derived from [App DocumentObject](App_DocumentObject.md) (`App::DocumentObject` class), which essentially comprises all objects that are possible to create in a document.

## Nomes

There are various properties for Names:

-   The `Name` can only include simple alphanumeric characters, and the underscore, `[_0-9a-zA-Z]`.
-   The `Name` cannot start with a number; it must start with a letter or the underscore, `[_a-zA-Z]`.
-   The `Name` is assigned at the creation time of the object; afterwards it is no longer editable. The object can never be renamed.
-   The `Name` must be unique in the entire document. It doesn\'t matter if two objects are of completely different types, for example, one is a [PartDesign Pocket](PartDesign_Pocket.md) and the other is an [Arch Wall](Arch_Wall.md). They must have different names.
-   When creating an object of the same type, normally the name is increased with a sequential number, thus `Box`, `Box001`, `Box002`, etc. This prevents naming collision.
-   Once the object is deleted, its `Name` becomes available to be used by a newly created object. This means that if `Box`, `Box001`, and `Box002` exist, and we delete the first item, the next box created with [Part Box](Part_Box.md) will not be `Box003`, it will be `Box` again, because this string is available to be used once more. Notice that it is not possible to rename `Box001` or `Box002` to `Box` since their names are fixed.

In summary, the `Name` essentially acts like a unique identifier (UID) for an object. Since a unique `Name` is very restrictive, all objects also have a `Label` property which allows \"renaming\" the object to something more descriptive. The internal `Name` actually remains fixed, but the user editable `Label` can be used in most situations where the `Name` would be used. In common usage in the program and the documentation, \"renaming\" means changing the `Label` and not the actual `Name` of the object.

## Labels

There are various properties for Labels:

-   The `Label` can accept any UTF8 string, including accents and spaces.
-   The [tree view](tree_view.md) actually displays the `Label` of the object, not the `Name`. Therefore, whenever a new object is created, it is a good practice to change the `Label` to a more descriptive string. To rename (relabel) the object, select it in the tree view and press **F2**, or open the context menu (right-click) and choose **Rename**.
-   Even after an object was renamed (relabelled), the internal `Name` will still be reported in many places, for example, in the [status bar](status_bar.md) or in the [selection view](selection_view.md), when the object is selected.
-   Since the internal functions of the program refer to the objects by `Name`, many dialogs will display the `Name` first, followed by the user editable `Label` in parentheses, for example, `Box (Extruded piece)`.
-   By default the `Label` is unique, just like the `Name`. However, this behavior can be changed in the [preferences editor](Preferences_Editor.md), **Edit → Preferences → General → Document → Allow duplicate object labels in one document**. This means that in general the `Label` is not unique in the document, and may actually be repeated. However, the recommendation is to keep the `Label` unique, as this is probably what is most useful to identify different objects. When writing custom functions that manipulate objects, the methods should use the `Name` of the object rather than its `Label` to guarantee that the correct object is used.
-   When using [expressions](expressions.md), for example, in the [property editor](property_editor.md) or in a [spreadsheet](spreadsheet.md), the Label can be referenced using double brackets made of the less than and greater than symbols.


```python
<<Custom Label With Spaces>>.Height
<<Label may use UTF8 characters>>.Width
```

### Label2 <small>(v0.19)</small> 

This property was introduced in v0.19. It is a simple string that can contain arbitrary text, and therefore can be used for documenting (describing with more detail) the created object.

-   In the [tree view](tree_view.md) edit the field next to the icon, under \"Description\", by clicking on it and pressing **F2**.
-   You can also change this property by modifying the `Label2` attribute from the [Python console](Python_console.md).
-   The **Label2** attribute is normally hidden in the [property editor](property_editor.md) but can be made visible by opening the context menu (right click) and selecting **Show all**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), and [scripted objects](scripted_objects.md).

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

### Label

The `Label` is a property of the created object and can be changed to a more meaningful text.

-   Upon creating the object, the `Label` is the same as the `Name`.
-   However, unlike the `Name`, the `Label` can accept any UTF8 string, including accents and spaces.
-   The `Label` can be changed at any point in time just by assigning the desired string, obj.Label = "New label"

### Getting an object by Name or Label 

All objects in a document are data attributes of the corresponding [Document](App_Document.md) object. The attribute\'s name correspond to the internal `Name` of the object.


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
[documentation index](../README.md) > Object name/pt-br

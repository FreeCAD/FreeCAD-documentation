# FeaturePython Custom Properties/de
{{TOCright}}

## Einführung


<div class="mw-translate-fuzzy">

Eigenschaften sind die wahren Bausteine von PythonFunktions Objekten. Durch sie wird der Benutzer in der Lage sein, mit Deinem Objekt zu interagieren und es zu modifizieren. Nachdem du ein neues PythonFunktions Objekt in deinem Dokument erstellt hast (obj=FreeCAD.ActiveDocument.addObject(\"App::FeaturePython\", \"Box\")), kannst du eine Liste der verfügbaren Eigenschaften durch Ausgabe erhalten:


</div>


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "Box")
```

You can get a list of the available properties by issuing:


```python
obj.supportedProperties()
```

##  Erstellen eines FeaturePython Objekts und Hinzufügen einer Eigenschaft zu diesem 


<div class="mw-translate-fuzzy">

Dieser Code erstellt ein Objekt mit dem internen Namen `InternalObjectName` (automatisch umbenannt in `InternalObjectName001` und so weiter, wenn ein Objekt mit dem Namen `InternalObjectName` bereits existiert) und gibt ihm die benutzerfreundliche Bezeichnung `Benutzerfreundliche Bezeichnung` (diese Bezeichnung wird in der [Baumansicht](Tree_view/de.md) und der [Comboansicht](Combo_view/de.md) angezeigt. [Ausdrücke](Expressions/de.md) können mit `<<Benutzerfreundliches Etikett>>` auf dieses Objekt durch sein Etikett verweisen.


</div>


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
```


<div class="mw-translate-fuzzy">


</div>


```python
obj.addProperty("App::PropertyBool", "ThePropertyName", "Subsection", "Description for tooltip")
```


`App::PropertyBool`

is the type of the property. The different types are described in more detail below.

You can also use the short form which omits the last two arguments. The subsection defaults to `Base`, and the tooltip is not displayed with this form.


```python
obj.addProperty("App::PropertyBool", "ThePropertyName")
```

To get or set the property, use `obj.ThePropertyName`:


```python
# set
obj.ThePropertyName = True
# get
thePropertyValue = obj.ThePropertyName
```

If the type of the property is [App::PropertyEnumeration](#App:_PropertyEnumeration.md), the setter has a special behavior: setting a list of strings defines the cases allowed by the enumeration, setting a string selects one of these cases. To set the list of possible cases and set the current one, use:


```python
# allowed cases
obj.ThePropertyName = ["aaa", "bbb", "ccc"]
# set
obj.ThePropertyName = "bbb"
```

## App::PropertyAcceleration

A {{TODO}}acceleration property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyAcceleration", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyAngle

An angle property. It can contain an `angle` value. You can use \"Value\" variable to get float variable. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyAngle", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = 180
obj.ThePropertyName # returns 180.0 deg
obj.ThePropertyName.Value # returns 180.0
```

## App::PropertyArea

A {{TODO}}area property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyArea", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyBool

A boolean property. It can contain `True` and `False`. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyBool", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = True
obj.ThePropertyName = False
obj.ThePropertyName # returns False
```

## App::PropertyBoolList

A property containing a list of booleans. It can contain a Python list of booleans, e.g. `[True, False, True]`. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyBoolList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = [True, False, True]
obj.ThePropertyName    # returns [True, False, True]
obj.ThePropertyName[1] # returns False
```

## App::PropertyColor

A color property. It can contain tuple of four `float` values. Each item can take values between 0.0 and 1.0. You can set red, green and blue values. Also you can set step transparency too. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyColor", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = (0.0, 1.0, 0.5, 0.8) # (Red, Green, Blue, Transparency)
obj.ThePropertyName # returns (0.0, 1.0, 0.5, 0.8)
```

## App::PropertyColorList

A {{TODO}}colorList property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyColorList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyDirection

A {{TODO}}direction property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyDirection", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyDistance

A distance property. It can contain a `distance` value. You can use \"Value\" variable to get float variable. Values always must be in millimeters unit. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyDistance", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = 500
obj.ThePropertyName # returns 500.0 mm
obj.ThePropertyName.Value # returns 500.0
```

## App::PropertyEnumeration

An enumeration property. The allowed items are defined by setting the property to a list. After that, it can contain items of the given list. The list of allowed items can be changed by setting the property to a list again. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyEnumeration", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = ["Foo", "Bar", "Baz"]  # set allowed items
obj.ThePropertyName = "Foo"                  # choose single item
obj.ThePropertyName = ["Foo", "Bar", "Quux"] # change allowed items
obj.ThePropertyName = "Quux"                 # choose single item
obj.ThePropertyName # returns "Quux"
```

As of FreeCAD 0.20, you can also group enumerations, which are displayed in the GUI using a submenu interface. To group, use the `|` character (vertical pipe) as a separator, e.g.:


```python
obj.ThePropertyName = [
    "Group 1 <nowiki>|</nowiki> Item A", 
    "Group 1 <nowiki>|</nowiki> Item B", 
    "Group 2 <nowiki>|</nowiki> Another item", 
    "Group 2 <nowiki>|</nowiki> Last item"
] # set allowed items
obj.ThePropertyName = "Group 1 <nowiki>|</nowiki> Item A" # choose single item
```

The GUI will display this as a menu structure:

-   Group 1
    -   Item A
    -   Item B
-   Group 2
    -   Another item
    -   Last item

## App::PropertyExpressionEngine

A {{TODO}}expressionEngine property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyExpressionEngine", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyFile

A filename property. It can contain a string indicating the path to a filename {{TODO}}:(Does it allow relative paths or absolute paths or both?). For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyFile", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyFileIncluded

A {{TODO}}fileIncluded property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyFileIncluded", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyFloat

A float property. It can contain a `float` value. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyFloat", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = 15.7
obj.ThePropertyName # returns 15.7
```

## App::PropertyFloatConstraint

A float constraint property. It can contain a `float` value. By using this property you can set start and finish values. Also you can set step interval too. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyFloatConstraint", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = (50.0, 0.0, 100.0, 1.0) # (Default, Start, Finish, Step)
obj.ThePropertyName # returns 50.0
```

## App::PropertyFloatList

A float list property. It can contain list of `float` values. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyFloatList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = [12.7, 5.8, 28.6, 17.22] # It can also be an empty list.
obj.ThePropertyName # returns [12.7, 5.8, 28.6, 17.22]
```

## App::PropertyFont

A {{TODO}}font property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyFont", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyForce

A {{TODO}}force property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyForce", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyFrequency

A {{TODO}}frequency property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyFrequency", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyInteger

An integer property. It can contain an integer value. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyInteger", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = 25
obj.ThePropertyName # returns 25
```

## App::PropertyIntegerConstraint

An integer constraint property. It can contain an `integer` value. By using this property you can set start and finish values. Also you can set step interval too. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyIntegerConstraint", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = (50, 0, 100, 1) # (Default, Start, Finish, Step)
obj.ThePropertyName # returns 50
```

## App::PropertyIntegerList

An integer list property. It can contain list of `integer` values. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyIntegerList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = [12, 5, 28, 17] # It can also be an empty list.
obj.ThePropertyName # returns [12, 5, 28, 17]
```

## App::PropertyIntegerSet

A {{TODO}}integerSet property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyIntegerSet", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLength

A length property. It can contain a `length` value. You can use \"Value\" variable to get float variable. Values always must be in millimeters unit. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLength", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = 500
obj.ThePropertyName # returns 500 mm
obj.ThePropertyName.Value # returns 500
```

## App::PropertyLink

A link property. It can contain link to an object. When you call this property, it will return the linked object. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
link_obj=FreeCAD.ActiveDocument.addObject("App::FeaturePython","LinkObjectName")
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLink", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = link_obj
obj.ThePropertyName # returns link_obj
```

## App::PropertyLinkChild

A {{TODO}}linkChild property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkChild", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkGlobal

A {{TODO}}linkGlobal property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkGlobal", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkHidden

A {{TODO}}linkHidden property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkHidden", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkList

A link list property. It can contain list of linked objects. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
link_obj0=FreeCAD.ActiveDocument.addObject("App::FeaturePython","LinkObjectName0")
link_obj1=FreeCAD.ActiveDocument.addObject("App::FeaturePython","LinkObjectName1")
link_obj2=FreeCAD.ActiveDocument.addObject("App::FeaturePython","LinkObjectName2")

obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = [link_obj0, link_obj1, link_obj2]
obj.ThePropertyName # returns [link_obj0, link_obj1, link_obj2]
```

## App::PropertyLinkListChild

A {{TODO}}linkListChild property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkListChild", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkListGlobal

A {{TODO}}linkListGlobal property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkListGlobal", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkListHidden

A {{TODO}}linkListHidden property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkListHidden", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkSub

A {{TODO}}linkSub property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkSub", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkSubChild

A {{TODO}}linkSubChild property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkSubChild", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkSubGlobal

A {{TODO}}linkSubGlobal property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkSubGlobal", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkSubHidden

A {{TODO}}linkSubHidden property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkSubHidden", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkSubList

A {{TODO}}linkSubList property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkSubList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkSubListChild

A {{TODO}}linkSubListChild property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkSubListChild", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkSubListGlobal

A {{TODO}}linkSubListGlobal property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkSubListGlobal", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkSubListHidden

A {{TODO}}linkSubListHidden property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkSubListHidden", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyMap

A {{TODO}}map property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyMap", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyMaterial

A material property. It can contain a FreeCAD material object. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
import FreeCAD
material=FreeCAD.Material()

obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyMaterial", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = material
obj.ThePropertyName # returns material
```

## App::PropertyMaterialList

A material list property. It can contain list of materials. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
import FreeCAD
material0 = FreeCAD.Material()
material1 = FreeCAD.Material()
material2 = FreeCAD.Material()

obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython","InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyMaterialList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = [material0, material1, material2] # It can also be an empty list.
obj.ThePropertyName # returns [material0, material1, material2]
```

## App::PropertyMatrix

A {{TODO}}matrix property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyMatrix", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyPath

A path property. It can contain a string representing a path to a folder {{TODO}}:(does it also allow paths to files? does it allow relative or absolute paths or both?). For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPath", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyPercent

A {{TODO}}percent property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPercent", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyPersistentObject

A {{TODO}}persistentObject property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPersistentObject", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyPlacement

A placement property. It can contain `placement` object. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
import FreeCAD
placement = FreeCAD.Placement()
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython","InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPlacement", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = placement
obj.ThePropertyName # returns placement
```

## App::PropertyPlacementLink

A {{TODO}}placementLink property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPlacementLink", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyPlacementList

A placement list property. It can contain list of `placements`. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
import FreeCAD
placement0 = FreeCAD.Placement()
placement1 = FreeCAD.Placement()
placement2 = FreeCAD.Placement()

obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython","InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPlacementList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = [placement0, placement1, placement2]
obj.ThePropertyName # returns [placement0, placement1, placement2]
```

## App::PropertyPosition

A {{TODO}}position property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPosition", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyPrecision

A {{TODO}}precision property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPrecision", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyPressure

A {{TODO}}pressure property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPressure", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyPythonObject

A {{TODO}}pythonObject property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPythonObject", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyQuantity

A {{TODO}}quantity property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyQuantity", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyQuantityConstraint

A {{TODO}}quantityConstraint property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyQuantityConstraint", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertySpeed

A {{TODO}}speed property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertySpeed", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyString

A {{TODO}}string property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyString", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyStringList

A {{TODO}}stringList property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyStringList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyUUID

A {{TODO}}uUID property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyUUID", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyVacuumPermittivity

A {{TODO}}vacuumPermittivity property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyVacuumPermittivity", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyVector

A vector property. It can contain a FreeCAD `vector` object. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
import FreeCAD
vector = FreeCAD.Vector(0, -2, 5)

obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyVector", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = vector
obj.ThePropertyName # returns Vector(0, -2, 5)
```

## App::PropertyVectorDistance

A {{TODO}}vectorDistance property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyVectorDistance", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyVectorList

A vector list property. It can contain list of `vectors`. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
import FreeCAD
v0 = FreeCAD.Vector(0, 10, 0)
v1 = FreeCAD.Vector(0, 10, 0)
v2 = FreeCAD.Vector(30, -10, 0)
v3 = FreeCAD.Vector(0, -10, 0)

obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython","InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyVectorList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = [v0, v1, v2, v3]
obj.ThePropertyName # returns [Vector(0, 10, 0), Vector(0, 10, 0), Vector(30, -10, 0), Vector(0, -10, 0)]
```

## App::PropertyVolume

A {{TODO}}volume property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyVolume", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyXLink

A {{TODO}}xLink property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyXLink", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyXLinkList

A {{TODO}}xLinkList property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyXLinkList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyXLinkSub

A {{TODO}}xLinkSub property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyXLinkSub", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyXLinkSubList

A {{TODO}}xLinkSubList property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyXLinkSubList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Mesh::PropertyCurvatureList

A {{TODO}}curvatureList property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Mesh::PropertyCurvatureList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Mesh::PropertyMeshKernel

A mesh kernel property. It can contain a `mesh` object. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
import Mesh
mesh = Mesh.Mesh()

obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Mesh::PropertyMeshKernel", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = mesh
obj.ThePropertyName # returns mesh
```

## Mesh::PropertyNormalList

A {{TODO}}normalList property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Mesh::PropertyNormalList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Part::PropertyFilletEdges

A {{TODO}}filletEdges property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Part::PropertyFilletEdges", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Part::PropertyGeometryList

A {{TODO}}geometryList property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Part::PropertyGeometryList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Part::PropertyPartShape

A part shape property. It can contain `shape` object. For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
import Part
part = Part.Shape()

obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Part::PropertyPartShape", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = part
obj.ThePropertyName # returns part
```

## Part::PropertyShapeHistory

A {{TODO}}shapeHistory property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Part::PropertyShapeHistory", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Path::PropertyPath

A {{TODO}}path property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Path::PropertyPath", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Path::PropertyTool

A {{TODO}}tool property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Path::PropertyTool", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Path::PropertyTooltable

A {{TODO}}tooltable property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Path::PropertyTooltable", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Sketcher::PropertyConstraintList

A {{TODO}}constraintList property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Sketcher::PropertyConstraintList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Spreadsheet::PropertyColumnWidths

A {{TODO}}columnWidths property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Spreadsheet::PropertyColumnWidths", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Spreadsheet::PropertyRowHeights

A {{TODO}}rowHeights property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Spreadsheet::PropertyRowHeights", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Spreadsheet::PropertySheet

A {{TODO}}sheet property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Spreadsheet::PropertySheet", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Spreadsheet::PropertySpreadsheetQuantity

A {{TODO}}spreadsheetQuantity property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Spreadsheet::PropertySpreadsheetQuantity", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## TechDraw::PropertyCenterLineList

A {{TODO}}centerLineList property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("TechDraw::PropertyCenterLineList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## TechDraw::PropertyCosmeticEdgeList

A {{TODO}}cosmeticEdgeList property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("TechDraw::PropertyCosmeticEdgeList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## TechDraw::PropertyCosmeticVertexList

A {{TODO}}cosmeticVertexList property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("TechDraw::PropertyCosmeticVertexList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## TechDraw::PropertyGeomFormatList

A {{TODO}}geomFormatList property. It can contain {{TODO}}\"allowed type and/or values\". For more details, see the section about [Creating a FeaturePython object and adding a property to it](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("TechDraw::PropertyGeomFormatList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Developer Documentation](Category_Developer Documentation.md) > FeaturePython Custom Properties/de

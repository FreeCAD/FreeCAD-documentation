# Property/ru
## Introduction


<div class="mw-translate-fuzzy">


{{Property/ru}}


</div>

Properties play a very important role in FreeCAD. As objects in FreeCAD are \"parametric\", this means that their behavior is defined by their properties, and how these properties are used as input for their class methods. See also [FeaturePython Custom Properties](FeaturePython_Custom_Properties.md) and [PropertyLink: InList and OutList](PropertyLink__InList_and_OutList.md)

## All property types 

Custom [scripted objects](scripted_objects.md) can use any of the property types defined in the base system:


```python
Acceleration
Angle
Area
Bool
BoolList
Color
ColorList
Direction
Distance
ElectricPotential
Enumeration
ExpressionContainer
ExpressionEngine
File
FileIncluded
Float
FloatConstraint
FloatList
Font
Force
Frequency
Geometry
Integer
IntegerConstraint
IntegerList
IntegerSet
Length
Link
LinkList
LinkSubList
Lists
Map
Material
MaterialList
Matrix
PartShape
Path
Percent
Placement
PlacementLink
PlacementList
Position
Precision
Pressure
PythonObject
Quantity
QuantityConstraint
Rotation
Speed
Stiffness
String
StringList
VacuumPermittivity
Vector
VectorDistance
VectorList
Volume
```

Internally, the property name is prefixed with `App::Property`: 
```python
App::PropertyBool
App::PropertyFloat
App::PropertyFloatList
...
```

Remember that these are property **types**. A single object may have many properties of the same type, but with different names.

For example:


```python
obj.addProperty("App::PropertyFloat", "Length")
obj.addProperty("App::PropertyFloat", "Width")
obj.addProperty("App::PropertyFloat", "Height")
```

This indicates an object with three properties of type \"Float\", named \"Length\", \"Width\", and \"Height\", respectively.

## Scripting


**See also:**

[FreeCAD scripting basics](FreeCAD_Scripting_Basics.md)

A [scripted object](scripted_objects.md) is created first, and then properties are assigned. 
```python
obj = App.ActiveDocument.addObject("Part::Feature", "CustomObject")

obj.addProperty("App::PropertyFloat", "Velocity", "Parameter", "Body speed")
obj.addProperty("App::PropertyBool", "VelocityEnabled", "Parameter", "Enable body speed")
```

In general, **Data** properties are assigned by using the object\'s `addProperty()` method. On the other hand, **View** properties are normally provided automatically by the parent object from which the scripted object is derived.

For example:

-   Deriving from `App::FeaturePython` provides only 4 **View** properties: \"Display Mode\", \"On Top When Selected\", \"Show In Tree\", and \"Visibility\".
-   Deriving from `Part::Feature` provides 17 **View** properties: the previous four, plus \"Angular Deflection\", \"Bounding Box\", \"Deviation\", \"Draw Style\", \"Lighting\", \"Line Color\", \"Line Width\", \"Point Color\", \"Point Size\", \"Selectable\", \"Selection Style\", \"Shape Color\", and \"Transparency\".

Nevertheless, **View** properties can also be assigned using the view provider object\'s `addProperty()` method. 
```python
obj.ViewObject.addProperty("App::PropertyBool", "SuperVisibility", "Base", "Make the object glow")
```

## Source code 

In the source code, properties are located in various **src/App/Property*** files.

They are imported and initialized in `[https://github.com/FreeCAD/FreeCAD/blob/9c27f1078e5ec516fe882aac1a27f5c6c6174554/src/App/Application.cpp#L1681-L1758 src/App/Application.cpp]`. {{Code|lang=cpp|code=
#include "Property.h"
#include "PropertyContainer.h"
#include "PropertyUnits.h"
#include "PropertyFile.h"
#include "PropertyLinks.h"
#include "PropertyPythonObject.h"
#include "PropertyExpressionEngine.h"
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Property/ru

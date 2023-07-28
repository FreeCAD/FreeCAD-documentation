# Property/pt-br
## Introdução

A [property](Property.md) is a piece of information like a number or a text string that is attached to a FreeCAD document or an object in a document. Public properties can be viewed and modified in the [Property editor](Property_editor.md).

Properties play a very important role in FreeCAD. As objects in FreeCAD are \"parametric\", this means that their behavior is defined by their properties, and how these properties are used as input for their class methods. See also [FeaturePython Custom Properties](FeaturePython_Custom_Properties.md) and [PropertyLink: InList and OutList](PropertyLink__InList_and_OutList.md)



## Todos os tipos de propriedade 

Custom [scripted objects](Scripted_objects.md) can use any of the property types defined in the base system:

++++
| Name                                  | Unit (if any)           | Remark                                                                                        |
+=======================================+=========================+===============================================================================================+
| Acceleration                          | m/s\^2                  |                                                                                               |
++++
| AmountOfSubstance                     | mol                     |                                                                                               |
++++
| Angle                                 | °                       |                                                                                               |
++++
| Area                                  | m\^2                    |                                                                                               |
++++
| Bool                                  |                         |                                                                                               |
++++
| BoolList                              |                         |                                                                                               |
++++
| Color                                 |                         |                                                                                               |
++++
| ColorList                             |                         |                                                                                               |
++++
| CurrentDensity                        | A/m\^2                  |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| Density                               | kg/m\^3                 |                                                                                               |
++++
| Direction                             |                         |                                                                                               |
++++
| DissipationRate                       | m\^2/s\^3               |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| Distance                              | m                       |                                                                                               |
++++
| DynamicViscosity                      | Pa\*s                   |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| ElectricalCapacitance                 | F                       |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| ElectricalConductance                 | S                       |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| ElectricalConductivity                | S/m                     |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| ElectricalInductance                  | H                       |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| ElectricalResistance                  | Ohm                     |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| ElectricCharge                        | C                       |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| ElectricCurrent                       | A                       |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| ElectricPotential                     | V                       |                                                                                |
|                                       |                         | <small>(v0.20)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| Enumeration                           |                         |                                                                                               |
++++
| ExpressionEngine                      |                         |                                                                                               |
++++
| File                                  |                         |                                                                                               |
++++
| FileIncluded                          |                         |                                                                                               |
++++
| Float                                 |                         |                                                                                               |
++++
| FloatConstraint                       |                         |                                                                                               |
++++
| FloatList                             |                         |                                                                                               |
++++
| Font                                  |                         |                                                                                               |
++++
| Force                                 | N                       |                                                                                               |
++++
| Frequency                             | Hz                      |                                                                                               |
++++
| HeatFlux                              | W/m\^2                  |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| Integer                               |                         |                                                                                               |
++++
| IntegerConstraint                     |                         |                                                                                               |
++++
| IntegerList                           |                         |                                                                                               |
++++
| IntegerSet                            |                         |                                                                                               |
++++
| InverseArea                           | 1/m\^2                  |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| InverseLength                         | 1/m                     |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| InverseVolume                         | 1/m\^3                  |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| KinematicViscosity                    | m\^2/s                  |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| Length                                | m                       |                                                                                               |
++++
| Link                                  |                         |                                                                                               |
++++
| LinkChild                             |                         |                                                                                               |
++++
| LinkGlobal                            |                         |                                                                                               |
++++
| LinkHidden                            |                         |                                                                                               |
++++
| LinkList                              |                         |                                                                                               |
++++
| LinkListChild                         |                         |                                                                                               |
++++
| LinkListGlobal                        |                         |                                                                                               |
++++
| LinkListHidden                        |                         |                                                                                               |
++++
| LinkSub                               |                         |                                                                                               |
++++
| LinkSubChild                          |                         |                                                                                               |
++++
| LinkSubGlobal                         |                         |                                                                                               |
++++
| LinkSubHidden                         |                         |                                                                                               |
++++
| LinkSubList                           |                         |                                                                                               |
++++
| LinkSubListChild                      |                         |                                                                                               |
++++
| LinkSubListGlobal                     |                         |                                                                                               |
++++
| LinkSubListHidden                     |                         |                                                                                               |
++++
| LuminousIntensity                     | cd                      |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| MagneticFieldStrength                 | A/m                     |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| MagneticFlux                          | Wb or V\*s              |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| MagneticFluxDensity                   | T                       |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| Magnetization                         | A/m                     |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| Map                                   |                         |                                                                                               |
++++
| Mass                                  | kg                      |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| Material                              |                         |                                                                                               |
++++
| MaterialList                          |                         |                                                                                               |
++++
| Matrix                                |                         |                                                                                               |
++++
| PartShape                             |                         | a Part property, is accessed as`Part::PropertyPartShape` |
++++
| Path                                  |                         |                                                                                               |
++++
| Percent                               |                         |                                                                                               |
++++
| PersistentObject                      |                         |                                                                                               |
++++
| Placement                             |                         |                                                                                               |
++++
| PlacementLink                         |                         |                                                                                               |
++++
| PlacementList                         |                         |                                                                                               |
++++
| Position                              |                         |                                                                                               |
++++
| Power                                 | W                       |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| Precision                             |                         |                                                                                               |
++++
| Pressure                              | Pa                      |                                                                                               |
++++
| PythonObject                          |                         |                                                                                               |
++++
| Quantity                              |                         |                                                                                               |
++++
| QuantityConstraint                    |                         |                                                                                               |
++++
| Rotation                              |                         |                                                                                               |
++++
| ShearModulus                          | Pa                      |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| SpecificEnergy                        | m\^2/s\^2 or J/kg       |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| SpecificHeat                          | J/kg/K                  |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| Speed                                 | m/s                     |                                                                                               |
++++
| Stiffness                             | m/s\^2                  |                                                                                               |
++++
| Stress                                | Pa                      |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| String                                |                         |                                                                                               |
++++
| StringList                            |                         |                                                                                               |
++++
| Temperature                           | K                       |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| ThermalConductivity                   | W/m/K                   |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| ThermalExpansionCoefficient           | 1/K                     |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| ThermalTransferCoefficient            | W/m\^2/K                |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| Time                                  | s                       |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| UltimateTensileStrength               | Pa                      |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| UUID                                  |                         |                                                                                               |
++++
| VacuumPermittivity                    | s\^4\*A\^2 / (m\^3\*kg) |                                                                                               |
++++
| Vector                                |                         |                                                                                               |
++++
| VectorDistance                        |                         |                                                                                               |
++++
| VectorList                            |                         |                                                                                               |
++++
| Velocity                              | m/s                     |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| Volume                                | l or m\^3               |                                                                                               |
++++
| VolumeFlowRate                        | l/s or m\^3/s           |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| VolumetricThermalExpansionCoefficient | 1/K                     |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| Work                                  | J                       |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| XLink                                 |                         |                                                                                               |
++++
| XLinkList                             |                         |                                                                                               |
++++
| XLinkSub                              |                         |                                                                                               |
++++
| XLinkSubList                          |                         |                                                                                               |
++++
| YieldStrength                         | Pa                      |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++
| YoungsModulus                         | Pa                      |                                                                                |
|                                       |                         | <small>(v0.21)</small>                                                                               |
|                                       |                         |                                                                                            |
++++

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

A [scripted object](Scripted_objects.md) is created first, and then properties are assigned. 
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



## Código fonte 

In the source code, properties are located in various **src/App/Property*** files.

They are imported and initialized in `[https://github.com/FreeCAD/FreeCAD/blob/9c27f1078e5ec516fe882aac1a27f5c6c6174554/src/App/Application.cpp#L1681-L1758 src/App/Application.cpp]`.


{{Code|lang=cpp|code=
#include "Property.h"
#include "PropertyContainer.h"
#include "PropertyUnits.h"
#include "PropertyFile.h"
#include "PropertyLinks.h"
#include "PropertyPythonObject.h"
#include "PropertyExpressionEngine.h"
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Property/pt-br

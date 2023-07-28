# Property/it
## Introduzione

Una [proprietà](Property/it.md) è una parte di informazione sotto forma di numero o di stringa di testo che viene allegata a un documento di FreeCAD oppure a un oggetto di un documento. Le proprietà pubbliche possono essere visualizzate e, se consentito, modificate nell\'[editore delle proprietà](Property_editor/it.md).

In FreeCAD le proprietà svolgono un ruolo molto importante. Dato che gli oggetti in FreeCAD sono \"parametrici\", ciò significa che il loro comportamento è definito dalle loro proprietà e dal modo in cui queste proprietà vengono utilizzate come input per i loro metodi delle classi. Vedere anche [FeaturePython Custom Properties](FeaturePython_Custom_Properties/it.md) e [PropertyLink: InList e OutList](PropertyLink:_InList_and_OutList/it.md)



## Tutti i tipi di proprietà 

In FreeCAD gli oggetti [script personalizzati](Scripted_objects/it.md) possono utilizzare uno qualsiasi dei tipi di proprietà definiti nel sistema di base:

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

Internamente, il nome della proprietà ha il prefisso `App::Property`: 
```python
App::PropertyBool
App::PropertyFloat
App::PropertyFloatList
...
```

Ricordare che queste sono della proprietà **types**. Un singolo oggetto può avere molte proprietà dello stesso tipo, ma con nomi diversi.

Per esempio:


```python
obj.addProperty("App::PropertyFloat", "Length")
obj.addProperty("App::PropertyFloat", "Width")
obj.addProperty("App::PropertyFloat", "Height")
```

Ciò indica un oggetto con tre proprietà di tipo \"Float\", denominate rispettivamente \"Length\", \"Width\", e \"Height\".



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Prima viene creato un [oggetto script](Scripted_objects/it.md), quindi gli vengono assegnate le proprietà. 
```python
obj = App.ActiveDocument.addObject("Part::Feature", "CustomObject")

obj.addProperty("App::PropertyFloat", "Velocity", "Parameter", "Body speed")
obj.addProperty("App::PropertyBool", "VelocityEnabled", "Parameter", "Enable body speed")
```

In generale, le proprietà **Data** sono assegnate usando il metodo `addProperty()` dell\'oggetto. D\'altra parte, le proprietà **View** sono normalmente fornite automaticamente dall\'oggetto genitore da cui deriva l\'oggetto script.

Per esempio:

-   Derivato da `App::FeaturePython` fornisce solo 4 proprietà **View**: \"Display Mode\", \"On Top When Selected\", \"Show In Tree\", e \"Visibility\".
-   Derivato da `Part::Feature` fornisce 17 proprietà **View**: le quattro precedenti più \"Angular Deflection\", \"Bounding Box\", \"Deviation\", \"Draw Style\", \"Lighting\", \"Line Color\", \"Line Width\", \"Point Color\", \"Point Size\", \"Selectable\", \"Selection Style\", \"Shape Color\", e \"Transparency\".

Tuttavia, le proprietà **View** possono anche essere assegnate usando il metodo `addProperty()` dell\'oggetto fornitore della vista.


```python
obj.ViewObject.addProperty("App::PropertyBool", "SuperVisibility", "Base", "Make the object glow")
```



## Codice sorgente 

Nel codice sorgente, le proprietà si trovano in vari file **src/App/Property***.

Vengono importati e inizializzati in `[https://github.com/FreeCAD/FreeCAD/blob/9c27f1078e5ec516fe882aac1a27f5c6c6174554/src/App/Application.cpp#L1681-L1758 src/App/Application.cpp]`.


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
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Property/it

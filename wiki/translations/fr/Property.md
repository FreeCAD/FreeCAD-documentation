# Property/fr
## Introduction

Une [propriété](Property/fr.md) est une information, telle qu\'un nombre ou une chaîne de texte, attachée à un document FreeCAD ou à un objet d\'un document. Les propriétés peuvent être visualisées et modifiées avec l\'[éditeur de propriétés](Property_editor/fr.md).

Les propriétés jouent un rôle très important dans FreeCAD. Comme les objets dans FreeCAD sont \"paramétriques\", cela signifie que leur comportement est défini par leurs propriétés et par la manière dont ces propriétés sont utilisées comme entrée pour leurs méthodes de classe. Voir aussi [Propriétés personnalisées de FeaturePython](FeaturePython_Custom_Properties/fr.md) et [PropertyLink: InList et OutList](PropertyLink:_InList_and_OutList/fr.md)



## Tous les types de propriétés 

Les [objets créés par script](Scripted_objects/fr.md) personnalisés dans FreeCAD peuvent avoir des propriétés des types suivants :

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

En interne, le nom de la propriété est préfixé par `App::Property` : 
```python
App::PropertyBool
App::PropertyFloat
App::PropertyFloatList
...
```

Rappelez-vous qu\'il s\'agit de propriétés **types**. Un même objet peut avoir plusieurs propriétés du même type, mais avec des noms différents.

Par exemple :


```python
obj.addProperty("App::PropertyFloat", "Length")
obj.addProperty("App::PropertyFloat", "Width")
obj.addProperty("App::PropertyFloat", "Height")
```

Cela indique un objet avec trois propriétés de type \"Float\", nommées respectivement \"Length\", \"Width\" et \"Height\".



## Script


**Voir aussi :**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Un [objet scripté](Scripted_objects/fr.md) est créé en premier, puis les propriétés lui sont attribuées. 
```python
obj = App.ActiveDocument.addObject("Part::Feature", "CustomObject")

obj.addProperty("App::PropertyFloat", "Velocity", "Parameter", "Body speed")
obj.addProperty("App::PropertyBool", "VelocityEnabled", "Parameter", "Enable body speed")
```

En général, les propriétés **Data** sont affectées à l\'aide de la méthode `addProperty()` de l\'objet. D\'autre part, les propriétés **View** sont normalement fournies automatiquement par l\'objet parent à partir duquel l\'objet scripté est dérivé.

Par exemple :

-   Dériver de `App::FeaturePython` fournit uniquement 4 propriétés **View**: \"Display Mode\", \"On Top When Selected\", \"Show In Tree\" et \"Visibility\".
-   Dériver de `Part::Feature` fournit 17 propriétés **View** : les quatre précédentes, plus \"Angular Deflection\", \"Zone de sélection\", \"Deviation\", \"Draw Style\", \"Lighting\", \"Line Color\", \"Line Width\", \"Point Color\", \"Point Size\", \"Selectable\", \"Selection Style\", \"Shape Color\", et \"Transparency\".

Néanmoins, les propriétés **View** peuvent également être affectées à l\'aide de la méthode `addProperty()` de l\'objet viewprovider.


```python
obj.ViewObject.addProperty("App::PropertyBool", "SuperVisibility", "Base", "Make the object glow")
```



## Code source 

Dans le code source, les propriétés se trouvent dans divers fichiers **src/App/Property*** .

Ils sont importés et initialisés dans `[https://github.com/FreeCAD/FreeCAD/blob/9c27f1078e5ec516fe882aac1a27f5c6c6174554/src/App/Application.cpp#L1681-L1758 src/App/Application.cpp]`.


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
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Property/fr

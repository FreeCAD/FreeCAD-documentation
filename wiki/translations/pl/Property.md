# Property/pl
## Wprowadzenie

[Właściwości](Property.md) to informacje takie jak liczba lub łańcuch tekstowy, który jest dołączony do dokumentu FreeCAD, lub obiektu w dokumencie. Właściwości ogólnodostępne można przeglądać i modyfikować w [Edytorze właściwości](Property_editor.md).

Właściwości odgrywają bardzo ważną rolę w FreeCAD. Ponieważ obiekty w FreeCAD są **parametryczne**, oznacza to, że ich zachowanie jest definiowane przez ich właściwości, i jak te właściwości są wykorzystywane jako dane wejściowe dla ich metod klasowych. Zobacz również [Właściwości niestandardowe funkcji Python](FeaturePython_Custom_Properties/pl.md) oraz [wskaźnik właściwości: InList oraz OutList](PropertyLink:_InList_and_OutList/pl.md).



## Wszystkie rodzaje właściwości 

Niestandardowe [obiekty tworzone skryptami](Scripted_objects/pl.md) mogą używać dowolnych typów właściwości zdefiniowanych w systemie bazowym:

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

Wewnętrzne, nazwa właściwości jest poprzedzona przez `App::Property`: 
```python
App::PropertyBool
App::PropertyFloat
App::PropertyFloatList
...
```

Pamiętajcie, że to są właściwości **typów**. Pojedynczy obiekt może mieć wiele właściwości tego samego typu, ale o różnych nazwach.

Dla przykładu:


```python
obj.addProperty("App::PropertyFloat", "Length")
obj.addProperty("App::PropertyFloat", "Width")
obj.addProperty("App::PropertyFloat", "Height")
```

Wskazuje to obiekt o trzech właściwościach typu **Float**, nazwanych odpowiednio Długość, Szerokość i Wysokość.



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

[Obiekty tworzone skryptami](Scripted_objects/pl.md) jest generowany w pierwszej kolejności, a następnie przypisywane są mu właściwości. 
```python
obj = App.ActiveDocument.addObject("Part::Feature", "CustomObject")

obj.addProperty("App::PropertyFloat", "Velocity", "Parameter", "Body speed")
obj.addProperty("App::PropertyBool", "VelocityEnabled", "Parameter", "Enable body speed")
```

Ogólnie rzecz biorąc, właściwości **Dane** są przypisywane za pomocą metody obiektu `addProperty()`. Z drugiej strony, właściwości **Widok** są zazwyczaj dostarczane automatycznie przez obiekt nadrzędny, z którego pochodzi skrypt.

Na przykład:

-   Pochodzący z `App::FeaturePython` dostarcza tylko 4 właściwości **widoku**: Tryb wyświetlania, Na górze po wybraniu, Pokaż w drzewie, i Widoczność.
-   Pochodzący z `Part::Feature` dostarcza 17 właściwości **widoku**: poprzednie cztery, plus Odchylenie kątowe, Ramka wiążąca, Odchylenie, Styl rysowania, Oświetlenie, Kolor linii, Szerokość linii, Kolor punktu, Rozmiar punktu, Wybór, Styl wyboru, Kolor kształtu i Przezroczystość.

Niemniej jednak, właściwości **widoku** można również przypisać za pomocą metody obiektu dostawcy widoku `addProperty()`.


```python
obj.ViewObject.addProperty("App::PropertyBool", "SuperVisibility", "Base", "Make the object glow")
```



## Kod źródłowy 

W kodzie źródłowym właściwości znajdują się w różnych plikach **src/App/Property***.

Są one importowane i inicjowane w `[https://github.com/FreeCAD/FreeCAD/blob/9c27f1078e5ec516fe882aac1a27f5c6c6174554/src/App/Application.cpp#L1681-L1758 src/App/Application.cpp]`.


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
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Property/pl

# Quantity
The quantity is a combination of a floating point number and a unit. It is used throughout all of FreeCAD to handle parameters and all other kind of input/output.

## General

In a CAD or CAE system it is very important to keep track of the unit of a value. Lots of trouble can arise when mixing up units or calculating results in different systems of units. One famous disaster is the [crash of the Mars Climate Orbiter](http   *//en.wikipedia.org/wiki/Mars_Climate_Orbiter#Cause_of_failure) due to a unit mix-up. Even in the same system of units the units come in lots of different flavours always tailored to the field of use. Simple examples are e.g. velocity in km/h (cars), m/s (robotics) or mm/minute (milling). A CAD system has to keep track of units reliably. Also it has to do calculations with them and check on the right unit for special parameters.

For that reason the FreeCAD Quantity framework was created. It includes all the code and objects to deal with units, unit calculations, user input, conversion to other systems of units and the pretty output of units and values. In the long run no parameter in FreeCAD should be just a number.

### Supported units 

The FreeCAD input parser supports a bunch of units and systems of units. FreeCAD supports the Greek letter \'µ\' for micro but also accepts \'u\' as a replacement. A complete list of all supported units can be [found here](Expressions#Units.md).

The detailed specifications you will find in the code   *

-   [Quantity lexer](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Base/QuantityLexer.c)
-   [Quantity definitions](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Base/Quantity.cpp#l167)

## Internal representation 

All physical units can be expressed as a combination of the seven [SI-Units](http   *//en.wikipedia.org/wiki/International_System_of_Units)   *

<img alt="" src=images/SI-Derived-Units.jpg  style="width   *750px;">

An easy way to express a unit is an integer array of size 7 (number of base units) that defines what the unit is. The signature of the 7 base units are   *

-   LENGTH   * \[1,0,0,0,0,0,0\]
-   MASS   * \[0,1,0,0,0,0,0\]
-   TIME   * \[0,0,1,0,0,0,0\]
-   ELECTRIC CURRENT   * \[0,0,0,1,0,0,0\]
-   THERMODYNAMIC TEMPERATURE   * \[0,0,0,0,1,0,0\]
-   AMOUNT OF SUBSTANCE   * \[0,0,0,0,0,1,0\]
-   LUMINOUS INTENSITY   * \[0,0,0,0,0,0,1\]

Using these seven units we are then able to express all derived units defined in [Guide for the Use of the International System of Units (SI)](http   *//physics.nist.gov/cuu/pdf/sp811.pdf) and create new ones as needed such as for instance   *

-   MASS DENSITY   * \[-3,1,0,0,0,0,0\]
-   AREA   * \[0,2,0,0,0,0,0\]

Since angle is physically dimensionless, but nevertheless important to a CAD system we add one more virtual unit for Angle. This makes a vector of 8 in the FreeCAD unit signature.

## Units calculator 

Often you are in need of converting values from one system of units to another. For example you have old parameter tables with wired units. In these cases FreeCAD offers a conversion tool called Units-Calculator which helps in translating units.

Its description in detail is here   * [Std_UnitsCalculator](Std_UnitsCalculator.md)

## InputField

The InputField is a QLineEdit derived Qt widget to handle all kinds of user interaction with quantities and parameters. It features the following properties   *

-   parsing arbitrary value/unit input
-   checking on the right unit (if given) and give the user feedback
-   special context menu for operations on quantities/values
-   history management (save the last used values)
-   save often needed values as shortcut in context menu
-   selecting values with mouse wheel and arrow keys (tbd)
-   selecting with middle mouse button and mouse move (tbd)
-   Python integration for usage in Python only dialogs (tbd)

The UnitsCalculator uses the InputField already.

Main documentation   * [InputField](InputField.md)

Code   *

-   [InputField.h](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Gui/InputField.h)
-   [InputField.cpp](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Gui/InputField.cpp)

## Python scripting 

The Unit and Quantity system in FreeCAD is (as nearly everything) fully accessibly via Python.

### Unit

The Unit class represents the fingerprint of any physical unit. As described in the Basics section a vector of eight numbers is used to represent this fingerprint. The Unit class allows the handling and calculation based on this information.

 
```python

from FreeCAD import Units

# creating a unit with certain signature
Units.Unit(0,1)      # Mass     (kg)
Units.Unit(1)        # Length   (mm)
Units.Unit(-1,1,-2)  # Pressure (kg/mm*s^2)

# using predefined constants
Units.Unit(Units.Length)
Units.Unit(Units.Mass)
Units.Unit(Units.Pressure)

# parsing unit out of a string
Units.Unit('kg/(m*s^2)')    # Pressure
Units.Unit('Pa')            # the same as combined unit Pascale
Units.Unit('J')             # Joule (work,energy) mm^2*kg/(s^2)

# you can use units from all supported systems of units
Units.Unit('psi')           # imperial pressure
Units.Unit('lb')            # imperial  mass
Units.Unit('ft^2')          # imperial area

# comparing units
Units.Unit(0,1) == Unit(Units.Mass)

# getting type of unit
Units.Unit('kg/(m*s^2)').Type == 'Pressure'

# calculating
Units.Unit('kg') * Units.Unit('m^-1*s^-2') == Units.Unit('kg/(m*s^2)')

``` The unit is mainly used to describe a certain type of unit for a parameter. Therefore a special property type in FreeCAD can pass a unit to check and ensure the right unit. A unit and a float value is called quantity.

### Quantity

 
```python

from FreeCAD import Units

# to create a quantity you need a value (float) and a unit
Units.Quantity(1.0,Units.Unit(0,1))     # Mass       1.0 kg
Units.Quantity(1.0,Units.Unit(1))       # Length    1.0 mm
Units.Quantity(1.0,Units.Unit(-1,1,-2)) # Pressure  1.0 kg/mm*s^2
Units.Quantity(1.0,Units.Pressure)      # Pressure  1.0 kg/mm*s^2

# you can directly give a signature
Units.Quantity(1.0,0,1)     # Mass       1.0 kg
Units.Quantity(1.0,1)       # Length    1.0 mm
Units.Quantity(1.0,-1,1,-2) # Pressure  1.0 kg/mm*s^2

# parsing quantities out of a string
Units.Quantity('1.0 kg/(m*s^2)') # Pressure
Units.Quantity('1.0 Pa')         # the same as combined Unit Pascale
Units.Quantity('1.0 J')          # Joule (Work,Energy) mm^2*kg/(s^2)

# You can use a point or comma as float delimiter
Units.Quantity('1,0 m')
Units.Quantity('1.0 m')

# you can use units from all supported systems of units
Units.Quantity('1.0 psi')  # imperial pressure
Units.Quantity('1.0 lb')   # imperial mass
Units.Quantity('1.0 ft^2') # imperial area

# the quantity parser can do calculations too
Units.Quantity('360/5 deg')        # splitting circle 
Units.Quantity('1/16 in')          # fractions
Units.Quantity('5.3*6.3 m^2')      # calculating an area
Units.Quantity('1/(log(2.3)/sin(pi)*3.4)+1.8e-3 m')
Units.Quantity('1ft 3in')          # imperial style

# and for sure calculation and comparison
Units.Quantity('1 Pa') * Units.Quantity(2.0) == Units.Quantity('2 Pa')
Units.Quantity('1 m') * Units.Quantity('2 m') == Units.Quantity('2 m^2')
Units.Quantity('1 m') * Units.Quantity('2 ft') + Units.Quantity('2 mm^2')
Units.Quantity('1 m') > Units.Quantity('2 ft')

# accessing the components
Units.Quantity('1 m').Value # get the number (always internal system (mm/kg/s))
Units.Quantity('1 m').Unit  # get the unit
Units.Quantity('1 m') == Units.Quantity( Units.Quantity('1 m').Value , Units.Quantity('1 m').Unit)

# translating the value into other units than the internal system (mm/kg/s)
Units.Quantity('1 km/h').getValueAs('m/s')                  # translate value
Units.Quantity('1 m').getValueAs(2.45,1)                    # translation value and unit signature
Units.Quantity('1 kPa').getValueAs(Units.Pascal)            # predefined standard units 
Units.Quantity('1 MPa').getValueAs(Units.Quantity('N/m^2')) # a quantity
          
```

### User facing values 

Normally in scripts you can use Quantity for all kinds of calculations and checking, but there comes the time you have to output information to the user. You could use getValueAs() to force a certain unit, but normally the user sets his preferred unit-schema in the preferences. This unit-schema does all the translations to the representation the user likes to see. At the moment there are three schemes implemented   *

-   1   * Internal (mm/kg/s)
-   2   * MKS (m/kg/s)
-   3   * US customary (in/lb)

There can be easily additional schemas implemented in the future\...

The Quantity class has two options to use the actual schema translation   *

 
```python
from FreeCAD import Units

# Use the translated string   *
Units.Quantity('1m').UserString           # '1000 mm' in 1; '1 m' in 2; and '1.09361 yr' in 3
``` This does the job if you only need a string. But sometimes you need more control, e.g. if you want to have a dialog button which dials up and down. Then you need more information about the translation output. Therefore the getUserPreferred() method of quantity is used   *

 
```python
Units.Quantity('22 m').getUserPreferred() # gets a tuple   *('22 m', 1000.0, 'm')
Units.Quantity('2  m').getUserPreferred() # Tuple   * ('2000 mm', 1.0, 'mm')
``` Here you get more information using a tuple (three items). You get the string as before, plus the factor of the value and the raw string with only the unit chosen by the translation schema. With this information you can implement a much richer user interaction.

The code of the schema translation can be found here   *

-   [Internal](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Base/UnitsSchemaInternal.cpp)
-   [MKS](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Base/UnitsSchemaMKS.cpp)
-   [Imperial](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Base/UnitsSchemaImperial1.cpp)

### Precision

The precision of quantities is within FreeCAD dialogs the number of decimals specified [in the preferences](Preferences_Editor#Units.md). To use this settings for your script (for example in dialogs), you can get it with this code   *  
```python
import FreeCAD

params = App.ParamGet("User parameter   *BaseApp/Preferences/Units")
params.GetInt('Decimals') # returns an int
```

## Appendix

### Parser supported units 

Although all physical units can be described with the seven SI units, most of the units used in technical areas are common combined units (like Pa = N/m\^2 Pascal ). Therefore the units parser in FreeCAD supports lot of SI and Imperial combined units. These units are defined in src/Base/QuantityParser.l file and can be further expanded in the future.

 
```python

from FreeCAD import Units

 "nm"  = Units.Quantity(1.0e-6    ,Units.Unit(1));         // nano meter
 "µm"  = Units.Quantity(1.0e-3    ,Units.Unit(1));         // micro meter
 "mm"  = Units.Quantity(1.0       ,Units.Unit(1));         // milli meter
 "cm"  = Units.Quantity(10.0      ,Units.Unit(1));         // centi meter
 "dm"  = Units.Quantity(100.0     ,Units.Unit(1));         // deci meter
 "m"   = Units.Quantity(1.0e3     ,Units.Unit(1));         // meter
 "km"  = Units.Quantity(1.0e6     ,Units.Unit(1));         // kilo meter
 "l"   = Units.Quantity(1000000.0 ,Units.Unit(3));         // liter dm^3
                                                  
 "µg"  = Units.Quantity(1.0e-9    ,Units.Unit(0,1));       // micro gram
 "mg"  = Units.Quantity(1.0e-6    ,Units.Unit(0,1));       // milli gram
 "g"   = Units.Quantity(1.0e-3    ,Units.Unit(0,1));       // gram
 "kg"  = Units.Quantity(1.0       ,Units.Unit(0,1));       // kilo gram
 "t"   = Units.Quantity(1000.0    ,Units.Unit(0,1));       // ton
                                                  
 "s"   = Units.Quantity(1.0       ,Units.Unit(0,0,1));     // second (internal standard time)
 "min" = Units.Quantity(60.0      ,Units.Unit(0,0,1));     // minute
 "h"   = Units.Quantity(3600.0    ,Units.Unit(0,0,1));     // hour  
                                                  
 "A"   = Units.Quantity(1.0       ,Units.Unit(0,0,0,1));   // Ampere (internal standard electric current)
 "mA"  = Units.Quantity(0.001     ,Units.Unit(0,0,0,1));   // milli Ampere         
 "kA"  = Units.Quantity(1000.0    ,Units.Unit(0,0,0,1));   // kilo Ampere         
 "MA"  = Units.Quantity(1.0e6     ,Units.Unit(0,0,0,1));   // Mega Ampere         
                                                  
 "K"   = Units.Quantity(1.0       ,Units.Unit(0,0,0,0,1)); // Kelvin (internal standard thermodynamic temperature)
 "mK"  = Units.Quantity(0.001     ,Units.Unit(0,0,0,0,1)); // Kelvin         
 "µK"  = Units.Quantity(0.000001  ,Units.Unit(0,0,0,0,1)); // Kelvin         

 "mol" = Units.Quantity(1.0       ,Units.Unit(0,0,0,0,0,1)); // Mole (internal standard amount of substance)        

 "cd"  = Units.Quantity(1.0       ,Units.Unit(0,0,0,0,0,0,1)); // Candela (internal standard luminous intensity)        

 "deg" = Units.Quantity(1.0         ,Units.Unit(0,0,0,0,0,0,0,1)); // degree (internal standard angle)
 "rad" = Units.Quantity(180/M_PI    ,Units.Unit(0,0,0,0,0,0,0,1)); // radian         
 "gon" = Units.Quantity(360.0/400.0 ,Units.Unit(0,0,0,0,0,0,0,1)); // gon         

 "in"  = Units.Quantity(25.4        ,Units.Unit(1));       // inch
 "\""  = Units.Quantity(25.4        ,Units.Unit(1));       // inch
 "fo"  = Units.Quantity(304.8       ,Units.Unit(1));       // foot
 "'"   = Units.Quantity(304.8       ,Units.Unit(1));       // foot
 "th"  = Units.Quantity(0.0254      ,Units.Unit(1));       // thou
 "yd"  = Units.Quantity(914.4       ,Units.Unit(1));       // yard

 "lb"  = Units.Quantity(0.45359237   ,Units.Unit(0,1));    // pound
 "oz"  = Units.Quantity(0.0283495231 ,Units.Unit(0,1));    // ounce
 "st"  = Units.Quantity(6.35029318   ,Units.Unit(0,1));    // Stone
 "cwt" = Units.Quantity(50.80234544  ,Units.Unit(0,1));    // hundredweights
```

  

[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Quantity

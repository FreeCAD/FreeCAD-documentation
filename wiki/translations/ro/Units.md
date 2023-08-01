# Units/ro
Some reading about units:

-   [Metrology](http://en.wikipedia.org/wiki/Metrology)
-   [SI system](http://en.wikipedia.org/wiki/International_System_of_Units)
-   [Imperial units](http://en.wikipedia.org/wiki/Imperial_units)
-   [SI derived units](http://en.wikipedia.org/wiki/SI_derived_unit)
-   [angle units](http://en.wikipedia.org/wiki/Degree_%28angle%29)
-   [unit implemented in OCC](https://github.com/3drepo/occt/blob/master/src/UnitsAPI/Units.dat)

## Examples


```python
# -- some examples of the FreeCAD unit translation system --
# make a shortcut for the examples
pq = FreeCAD.Units.parseQuantity

# 10 meters in internal numbers
pq('10 m')

# doing math
pq('3/8 in')

# combined stuff
pq('100 km/h')

# transfer to other units
pq('100 km/h')/tu('m/s')

# derived units (Ohm)
pq('m^2*kg*s^-3*A^-2')

# or
pq('(m^2*kg)/(A^2*s^3)')

# angles 
pq('2*pi rad') # full circle

# as gon
pq('2*pi rad') / tu('gon')

# more imperial
tu('1ft (3+7/16)in')

# or 
pq('1\' (3+7/16)"') # the ' we have to escape because of python

# trigonometry
pq('sin(pi)')

# Using translated units as parameters, this command will create a 50.8mm x 20mm x 10mm box
b = Part.makeBox(pq('2in'), pq('2m')/100, 10)
```

## Supported units 

A complete list of all supported units can be [found here](Expressions#Units.md).

## See Also 

-   The [Expressions](Expressions#Units.md) page for a list of all known units.
-   The documentation of [Quantity](Quantity.md).
-   The [Std UnitsCalculator](Std_UnitsCalculator.md) tool.



---
⏵ [documentation index](../README.md) > Units/ro

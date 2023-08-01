# Units/pl
{{TOCright}}

Oto kilka lektur na temat jednostek:

-   [Metrologia](http://en.wikipedia.org/wiki/Metrology)
-   [System SI](http://en.wikipedia.org/wiki/International_System_of_Units)
-   [Jednostki brytyjskie](http://en.wikipedia.org/wiki/Imperial_units)
-   [Jednostki pochodne SI](http://en.wikipedia.org/wiki/SI_derived_unit)
-   [jednostki kątowe](http://en.wikipedia.org/wiki/Degree_%28angle%29)
-   [jednostka wdrożona w OCC](https://github.com/3drepo/occt/blob/master/src/UnitsAPI/Units.dat)

## Przykłady


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

## Obsługiwane jednostki 

Pełna lista wszystkich obsługiwanych jednostek znajduje się [na tej stronie](Expressions/pl#Units.md).

## Zobacz również 

-   Strona [Wyrażenia](Expressions/pl#Jednostki.md) zawierająca listę wszystkich znanych jednostek.
-   Dokumentacja [Ilość](Quantity/pl.md),
-   Narzędzie [Kalkulator jednostek](Std_UnitsCalculator/pl.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > Units/pl

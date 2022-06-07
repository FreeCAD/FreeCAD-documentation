# Units/it
{{TOCright}}


<div class="mw-translate-fuzzy">

Alcune letture sulle unità di misura   *

-   [Sistema Internazionale di Misura SI](http   *//it.wikipedia.org/wiki/Sistema_internazionale_di_unit%C3%A0_di_misura)
-   [Sistema imperiale britannico](http   *//it.wikipedia.org/wiki/Sistema_imperiale_britannico)
-   [SI derived unit](http   *//en.wikipedia.org/wiki/SI_derived_unit) (in italiano si trovano nella stessa pagina del SI)
-   [Grado d\'arco - Unità angolari](http   *//it.wikipedia.org/wiki/Grado_d%27arco)


</div>

## Esempi


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


<div class="mw-translate-fuzzy">

## Unità di misura supportate 

Un elenco completo di tutte le unità supportate [si trova quì](Expressions/it#Unità.md).


</div>


<div class="mw-translate-fuzzy">

## Prossime azioni 

-   Implementing Quantity and Unit classes (mostly done)
-   Implementing InputField as User front end (in progress)
-   UnitsCalculator as test bed (in progress)
-   [Quantity](Quantity/it.md) documentation (in progress)
-   [UnitsCalculator](Std_UnitsCalculator/it.md) documentation
-   Update Material framework to work only with Quantities
-   Test Cases


</div>

-   The [Expressions](Expressions#Units.md) page for a list of all known units.
-   The documentation of [Quantity](Quantity.md).
-   The [Std UnitsCalculator](Std_UnitsCalculator.md) tool.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Units/it

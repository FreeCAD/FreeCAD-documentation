# Units/de
{{TOCright}}

Einige Artikel zu Einheiten:

-   [Metrologie](https://de.wikipedia.org/wiki/Metrologie) (Meßwesen)
-   [SI System](https://de.wikipedia.org/wiki/Internationales_Einheitensystem)
-   [Angloamerikanisches Maßsystem (Imperiale Einheiten)](https://de.wikipedia.org/wiki/Angloamerikanisches_Ma%C3%9Fsystem)
-   [Abgeleitete SI Einheiten](https://de.wikipedia.org/wiki/Internationales_Einheitensystem#Abgeleitete_SI-Einheiten_mit_besonderem_Namen)
-   [Grad(Winkel)](https://de.wikipedia.org/wiki/Grad_(Winkel))
-   [In OCC implementierte Einheiten](https://github.com/3drepo/occt/blob/master/src/UnitsAPI/Units.dat)

## Beispiele


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

## Unterstützte Einheiten 

Eine vollständige Liste aller unterstützter Einheiten kann man [hier](Expressions/de#Einheiten.md) finden.

## Siehe auch 

-   Die Seite [Ausdrücke](Expressions/de#Einheiten.md) für eine Auflistung aller bekannten Einheiten.
-   Die Dokumentation der [Größen](Quantity.md).
-   Das Werkzeug [Std Einheitenrechner](Std_UnitsCalculator/de.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > Units/de

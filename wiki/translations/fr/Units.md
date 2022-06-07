# Units/fr
{{TOCright}}

Un peu de lecture sur les unités    *

-   [Métrologie](https   *//fr.wikipedia.org/wiki/M%C3%A9trologie)
-   [Système international d\'unités](https   *//fr.wikipedia.org/wiki/Système_international_d'unités)
-   [Système d\'unités impériales](https   *//fr.wikipedia.org/wiki/Syst%C3%A8me_d%27unit%C3%A9s_imp%C3%A9riales)
-   [Unité dérivée du Système international](https   *//fr.wikipedia.org/wiki/Unités_dérivées_du_système_international)
-   [Degré (angle)](https   *//fr.wikipedia.org/wiki/Degré_(angle))
-   [Unités implémentées dans OCC](https   *//github.com/3drepo/occt/blob/master/src/UnitsAPI/Units.dat)

## Exemples


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

## Unités supportées 

Une liste complète de toutes les unités prises en charge peut être [trouvée ici](Expressions/fr#Unités.md).

## Voir aussi 

-   La page [Expressions](Expressions/fr#Unit.C3.A9s.md) pour une liste de toutes les unités connues.
-   La documentation de [Quantity](Quantity/fr.md).
-   L\'outil [Std Convertisseur d\'unités](Std_UnitsCalculator/fr.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > Units/fr

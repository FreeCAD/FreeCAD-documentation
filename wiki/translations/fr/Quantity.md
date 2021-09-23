# Quantity/fr
 Quantity est une combinaison d\'un nombre à virgule flottante et d\'une unité. Quantity est utilisé dans l\'ensemble de FreeCAD pour gérer les paramètres et toutes sortes d\'autres entrées/sorties.

## Généralité

Dans un système CAO ou CAE il est très important de garder une trace de l\'unité d\'une valeur. Beaucoup de problèmes peuvent survenir lors du mélange des unités ou des résultats de calculs dans des systèmes d\'unités différentes. Une catastrophe célèbre est [la perte de la sonde Mars Climate Orbiter](http://fr.wikipedia.org/wiki/Mars_Climate_Orbiter#Perte_de_la_sonde) à cause d\'une confusion d\'interprétation d\'unité. Même dans le même système d\'unité, les unités sont de type différents, et toujours adaptés à son domaine d\'utilisation. Un petit exemple, la vitesse interprétée en km/h (voitures), en m/s pour la (robotique) ou calcul de l\'avance de l\'outil en mm/minute (fraisage). Un système de CAO dois rester fiable avec toutes les unités. Donc, il faut compter sur elle et utiliser la bonne unité pour les paramètres spéciaux.

C\'est pour cela que la FreeCAD Quantity framework a été créé. Il comprend le code et les objets à traiter avec les unités, calculs d\'unités, entrées utilisateurs, conversion dans d\'autres systèmes d\'unités et affichage des unités et des valeurs. À long terme, aucun paramètre ne devrait être dans FreeCAD, juste un nombre.

### Unités supportées 

L\'analyseur de FreeCAD prend en charge un tas d\'unités et d\'unités-systme. Nous utilisons la lettre grecque pour micro **\" µ \"** mais peut être substituée par la lettre **\" u \"**. Une liste complète de toutes les unités prises en charge peut être [trouvée ici](Expressions/fr#Unités.md).

Vous pouvez trouver plus de détails dans le code :

-   [Quantity lexer](https://github.com/FreeCAD/FreeCAD/blob/master/src/Base/QuantityLexer.c)
-   [Quantity definitions](https://github.com/FreeCAD/FreeCAD/blob/master/src/Base/Quantity.cpp#l167)

## Représentation interne 

Toutes les unités physiques peuvent être exprimées dans sept combinaisons [SI-Units](http://en.wikipedia.org/wiki/International_System_of_Units):
<img alt="" src=images/SI-Derived-Units.jpg  style="width:750px;">

Un moyen facile d\'exprimer une unité est un tableau d\'entiers de taille 7 (nombre d\'unités de base) qui définit ce qu\'est l\'unité.
La signature des 7 unités de base sont :

-   **LENGTH**: \[1,0,0,0,0,0,0\]
-   **MASS**: \[0,1,0,0,0,0,0\]
-   **TIME**: \[0,0,1,0,0,0,0\]
-   **ELECTRIC CURRENT**: \[0,0,0,1,0,0,0\]
-   **THERMODYNAMIC TEMPERATURE**: \[0,0,0,0,1,0,0\]
-   **AMOUNT OF SUBSTANCE**: \[0,0,0,0,0,1,0\]
-   **LUMINOUS INTENSITY**: \[0,0,0,0,0,0,1\]

De ces 7 unités, nous sommes alors en mesure d\'exprimer toutes les unités dérivées, définies dans [Guide for the Use of the International System of Units (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf) et au besoin d\'en créer de nouvelles comme par exemple :

-   **MASS DENSITY**: \[-3,1,0,0,0,0,0\]
-   **AREA**: \[0,2,0,0,0,0,0\]

Puisque l\'angle est sans dimension physiquement, mais néanmoins important dans un système de CAO, nous ajouterons une unité plus virtuelle pour Angle. Ce qui rend le vecteur à 8 dans la signature d\'unité de FreeCAD.

## Conversion d\'unités 

Souvent, vous avez besoin de convertir des unités d\'un système à un autre. Par exemple, vous avez un vieux tableau de paramètres avec des unités filaires. Dans ce cas FreeCAD offre un outil de conversion appelé Units-Calculator qui vous aide à traduire les unités.

Sa description est détaillée ici :

[Std Convertisseur d\'unités](Std_UnitsCalculator/fr.md)

## Champ a entrer 

InputField est un QLineEdit dérivé Qt widget pour gérer tous les types d\'interaction de l\'utilisateur avec les paramètres et les quantités. Il dispose à la suite des propriétés :

-   l\'analyse arbitraire d\'entrée valeur/unité
-   vérification sur l\'exactitude de l\'unité (si) et donner une rétroaction
-   menu contextuel spécial sur les opérations quantités/valeurs
-   gestion de l\'historique (sauf les dernières valeurs utilisées)
-   enregistrer fréquemment les valeurs avec le raccourci dans le menu contextuel
-   sélectionnez des valeurs avec action sur les touches de souris et flèche (à définir)
-   sélectionnez avec le bouton central de la souris et le déplacement de la souris (à définir)
-   intégration python pour l\'utilisation dans la console python (à définir)

UnitsCalculator utilise déjà InputField.

Main documentation: [InputField](InputField/fr.md)

Code:

-   [InputField.h](https://github.com/FreeCAD/FreeCAD/blob/master/src/Gui/InputField.h)
-   [InputField.cpp](https://github.com/FreeCAD/FreeCAD/blob/master/src/Gui/InputField.cpp)

## Script Python 

Les système Unit et Quantity sont entièrement accessibles via Python dans (presque tout) FreeCAD.

### Unit

La **Unit class** représente l\'empreinte digitale de n\'importe quelle unité physique. Comme décri dans la section plus haut, un vecteur de 8 nombres est utilisé pour représenter cette empreinte. La **Unit class** permet la manutention et le calcul grâce à cette information.


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

```

**Unit** est principalement utilisé pour décrire un paramètre d\'un certain type d\'unité. Un Type particulier de propriété peut être porté dans le système d\'unités de FreeCAD pour vérifier et garantir l\'unité adéquate. Une **Unit** et une valeur **float** sont appelés **Quantity**.

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

### Valeurs face vers l\'utilisateur 

Normalement, dans un script, vous pouvez utiliser Quantity pour tout genre de calcul et vérification, mais il peut mettre un certain temps pour afficher les informations à l\'utilisateur. Vous pouvez utiliser getValueAs() pour forcer une certaine unité, mais normalement l\'utilisateur définit son schéma-unité préféré dans les préférences. Ce schéma-unité donne toutes les représentations de la conversions que l\'utilisateur veut voir. À l\'heure actuelle, il y a 3 schémas mis en place :

-   1: Internal (mm/kg/s)
-   2: MKS (m/kg/s)
-   3: US customary (in/lb)

A l\'avenir il peut y avoir des schémas supplémentaires faciles à ajouter \...

La class Quantity a deux options d\'utilisation pour la conversion réelle du schéma :


```python
from FreeCAD import Units

# Use the translated string:
Units.Quantity('1m').UserString           # '1000 mm' in 1; '1 m' in 2; and '1.09361 yr' in 3
```

Procédure à suivre, si vous n\'avez besoin que d\'une chaîne. Mais si vous avez besoin d\'un plus grand contrôle, par exemple si vous voulez avoir une boîte de dialogue avec boutons up et down. Alors vous avez besoin de plus d\'informations de la conversion affichée. Alors la méthode **getUserPreferred()** de Quantity est utilisée :


```python
Units.Quantity('22 m').getUserPreferred() # gets a tuple:('22 m', 1000.0, 'm')
Units.Quantity('2  m').getUserPreferred() # Tuple: ('2000 mm', 1.0, 'mm')
```

Ici, vous obtenez deux informations comme un tuple de taille 3. Vous obtenez la chaîne telle qu\'elle était avant, plus le facteur de conversion du nombre et la chaîne brute avec uniquement l\'unité choisie par le schéma de conversion. Avec cette information, vous pouvez implémenter une interaction utilisateur beaucoup plus riche.

Vous pouvez voir ici le code pour la conversion du schéma :

-   [Interne](https://github.com/FreeCAD/FreeCAD/blob/master/src/Base/UnitsSchemaInternal.cpp)
-   [MKS](https://github.com/FreeCAD/FreeCAD/blob/master/src/Base/UnitsSchemaMKS.cpp)
-   [Impérial](https://github.com/FreeCAD/FreeCAD/blob/master/src/Base/UnitsSchemaImperial1.cpp)

### Précision

La précision des quantités est dans les boîtes de dialogue FreeCAD le nombre de décimales spécifié [dans les préférences](Preferences_Editor/fr#Units.md). Pour utiliser ces paramètres pour votre script (par exemple dans les boîtes de dialogue), vous pouvez l\'obtenir avec ce code: 
```python
import FreeCAD

params = App.ParamGet("User parameter:BaseApp/Preferences/Units")
params.GetInt('Decimals') # returns an int
```

## Appendice

### Analyseur de prise en charge des unités 

Bien que toutes les unités physiques peuvent être décrite avec les sept unités du SI, la plupart des unités utilisées dans le domaine technique sont combinées (comme Pa = N/m\^2 Pascal). L\'analyseur d\'unités dans FreeCAD supporte la combinaison des unités des systèmes SI et Imperial. Ces unités sont définies dans le fichier **src/Base/QuantityParser.l** et peut être étendu dans le futur.


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


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)

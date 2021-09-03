


<div class="mw-translate-fuzzy">

Aquí hay algunos enlaces con información sobre unidades:

-   [Sistema Internacional de Unidades SI](http://es.wikipedia.org/wiki/Sistema_Internacional_de_Unidades)
-   [Sistema Británico](http://en.wikipedia.org/wiki/Imperial_units)
-   [Unidades derivadas del Sistema Internacional](http://es.wikipedia.org/wiki/Unidades_derivadas_del_Sistema_Internacional)
-   [Unidades angulares](http://es.wikipedia.org/wiki/Grado_sexagesimal)


</div>

## Ejemplos


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


<div class="mw-translate-fuzzy">

## Unidades soportadas {#unidades_soportadas}

Aquí están las unidades definidas en FreeCAD hasta el momento. Es sencillo añadir una nueva unidad definida por el usuario. La definición está [Aquí](http://free-cad.svn.sourceforge.net/viewvc/free-cad/trunk/src/Base/UnitsApi.l?view=markup).


</div>

## Propósito y principios: Propuesta de una extensión del sistema de gestión de unidades {#propósito_y_principios_propuesta_de_una_extensión_del_sistema_de_gestión_de_unidades}

En las próximas secciones se propone un sistema de gestión de unidades, desarrollando el concepto de *sistema de unidades*, activado durante la ejecución de FreeCAD. El interés de definir tal concepto es trabajar de forma más sencilla con diversos tipos de unidades **físicas** (incluso creadas por el usuario), sin incrementar la complejidad de la gestión de unidades para el usuario, o para los desarrolladores de FreeCAD.

En resumen, los eventos de escalado de unidades están localizados de forma precisa, y llevados de un modo genérico.

Lograr tal flexibilidad se requiere principalmente cuando se empieza a trabajar con propiedades de materiales que pueden tener unidades muy diferentes, dificiles de manejar una a una manualmente.

El razonamiento propuesto permite manejar las unidades como se describe en la [Guía para el uso de las unidades del Sistema Internacional (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf) y en el [Sistema internacional de unidades (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf) ambos de NIST.

En esta propuesta, se requiere en la sección [Tormenta de ideas](Units/es#Tormenta_de_ideas.md) un primer recordatorio de los posibles contextos en los que se podría utilizar la gestión de unidades.

En la sección [Organización](Units/es#Organización.md), presentamos el modelo de datos retenido para lograr la gestión de unidades, basado en 3 objetos, la *unidad*, el *diccionario de unidades*, y el *sistema de unidades*. Finalmente, también se presenta una breve API de un cuarto objeto denominado *gestor de unidades*.

## Resultado

Gracias a esta extensión, una de las intenciones es hacer más sencillo el escalado de unidades que puede suceder entre diferentes tareas. Por ejemplo, los dibujos técnicos se pueden realizar en el sistema de unidades estándar, mientras que el modelado para elementos finitos se puede gestionar en un sistema de unidades que se ajuste mejor a él.

El intercambio de datos entre estos dos tipos de actividades se hace más sencilla con esta extensión.

## Tormenta de ideas {#tormenta_de_ideas}

En esta sección se destacan los contextos del uso del sistema de gestión de unidades. Desde estops contextos, podemos definir sus especificaciones técnicas.

Esencialmente se dan 2 contextos como ejemplo.

### Contexto 1: Apertura de un archivo de datos {#contexto_1_apertura_de_un_archivo_de_datos}

Este es posiblemente el caso más frecuente. Recibes un archivo que contiene por ejemplo un modelo geométrico, o describiendo un material con bastantes propiedades. El modelo geométrico se expresa en metros, o las propiedades del material de acuerdo al sistema internacional de unidades.

Que mal..

Esperabas un modelado para cálculo por elementos finitos, y trabajas en milimetros para la longitud y MegaPascales para la tensión, toneladas para la masa\...

En este contexto, la gestión de unidades se requiere para escalar los datos de un sistema de unidades inicial definido en el archivo de entrada a un sistema de unidades objetivo definido por el usuario.

### Contexto 2: Cambiando el sistema de unidades durante la ejecución {#contexto_2_cambiando_el_sistema_de_unidades_durante_la_ejecución}

En este caso, puedes ser al mismo tiempo el que realiza el dibujo, y el que maneja el modelo para cálculo por elementos finitos. De modo similar al caso anterior, el sistema de unidades para estas dos tareas no es la misma, y necesitas cambiar el sistema de unidades inicial a tu preferido en tiempo de ejecución.

## Organización

### Escalado lógico de unidades {#escalado_lógico_de_unidades}

En la sección [Tormenta de ideas](Units/es#Tormenta_de_ideas.md) se han presentado 2 contextos de utilización del escalado de unidades. Algunos aspectos deberían destacarse de estos dos contextos.


<div class="mw-translate-fuzzy">

#### Coherencia de unidades a través de la ejecución de FreeCAD {#coherencia_de_unidades_a_través_de_la_ejecución_de_freecad}

El sistema propuesto está basado en una suposición fundamental: el usuario está trabajando en un sistema de unidades coherente. Por ejemplo, esto significa que si el usuario expresa las longitudes en milímetros, necesariamente las áreas se expresarán en milímetros cuadrados, no metros cuadrados. Esta es la **Hipótesis uno**.


</div>

#### Sistema de unidades {#sistema_de_unidades}

Debido a la *hipótesis uno*, es posible y relevante definir un sistema de unidades. Un sistema de unidades se aplica a:

-   Una ejecución de FreeCAD en la que estés trabajando
-   o se puede aplicar globalmente al contexto de un archivo de entrada

De acuerdo con la [Guía para el uso del Sistema Internacional de Unidades (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf) de NIST, hay 7 unidades físicas base. Seleccionamos expresar un sistema de unidades en términos de dichas 7 unidades base.

Cuando se trabaja en una instancia de FreeCAD, el usuario de este modo tiene que definir primero el sistema de unidades de acuerdo al cual está trabajando antes de decidir cambiar a otro sistema de unidades, o antes de importar datos de un archivo de entrada.

Este sistema de unidades se aplicará hasta que el usuario decida cambiarlo. Si lo hace, todos los datos con dimensiones serán escalados.

Considerando la *hipótesis uno*, todos los datos que el usuario introduzca manualmente en FreeCAD se asumen que sean coherentes con el sistema de unidades escogido.

El beneficio de trabajar con un *sistema de unidades* definido al nivel de la instancia de ejecución de FreeCAD, o a nivel del archivo de entrada de datos (en lugar de *unidades* que son definidas a nivel de datos) es que la gestión de unidades se simplifica considerablemente.

Estos son algunos ejemplos de sistemas de unidades.

-   metro, kilogramo, segundo, amperio, Kelvin, mol, candela
-   milímetro, tonelada, milisegundo, amperio, Kelvin, mol, candela
-   milímetro, kilogramo, milisegundo, amperio, Kelvin, mol, candela
-   \...

#### Unidades base y derivadas {#unidades_base_y_derivadas}

Las unidades derivadas son creadas por combinación de las unidades base. Por ejemplo, una velocidad (m/s) combina la longitud y el tiempo. Una interesante imagen presentando la relación entre las unidades base y las derivadas se puede ver [aquí](http://physics.nist.gov/cuu/pdf/SIDiagramColorAnnot.pdf) también de NIST.

Gracias a la definición del *sistema de unidades*, es posible para el usuario trabajar con cualquier tipo de unidades derivadas, sin necesidad de que los desarrolladores de FreeCAD lo tengan previsto por anticipado.

#### Símbolos de unidades base y derivadas {#símbolos_de_unidades_base_y_derivadas}

De acuerdo al [Sistema internacional de unidades (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf), los símbolos para especificar una unidad están aprobados oficialmente. Dos consecuencias se pueden destacar de esto.

-   No es sencillo para un programa informático trabajar con símbolos de unidades porque por ejemplo algunos utilizan letras griegas. De ahí que puedan ser algo difíciles de procesar por un programa
-   Mientras que algunas unidades y sus símbolos se pueden utilizar ampliamente, pueden no estar aprobados oficialmente, como por ejemplo la unidad *tonelada* (mira la página 32 del [Sistema Internacional de unidades (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf))

Para superar estas limitaciones y permanecer flexible, el sistema propuesto está a favor del uso de unidades de magnitud en lugar de símbolos de unidades, el cual se mantiene no obstante por razones de ergonomía.

### Modelo de datos {#modelo_de_datos}

Los tres objetos principales del sistema de gestión de unidades se han presentado, denominándose *unidad*, *diccionario de unidades* y *sistema de unidades*.

#### Unidad

As a foreword, it is important to highlight that a *unit* object in itself only indicates a **dimension** like length, mass, time\... It doesn\'t specify a **magnitude** like meter, millimeter, kilometer\... This last information is specified through the unit system.

##### Dimension

Compulsory string indicating the *dimension* of the unit. The *dimension* of the 7 base units are indicated below (from [Guide for the Use of the International System of Units (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf)).

-   LENGTH
-   MASS
-   TIME
-   ELECTRIC CURRENT
-   THERMODYNAMIC TEMPERATURE
-   AMOUNT OF SUBSTANCE
-   LUMINOUS INTENSITY

*Dimension* attribute allows identifying the unit. Two units cannot share the same *dimension*.

##### Signature

Compulsory integer array of size 7 (number of base units) that defines what the unit is. The signature of the 7 base units are:

-   LENGTH: \[1,0,0,0,0,0,0\]
-   MASS: \[0,1,0,0,0,0,0\]
-   TIME: \[0,0,1,0,0,0,0\]
-   ELECTRIC CURRENT: \[0,0,0,1,0,0,0\]
-   THERMODYNAMIC TEMPERATURE: \[0,0,0,0,1,0,0\]
-   AMOUNT OF SUBSTANCE: \[0,0,0,0,0,1,0\]
-   LUMINOUS INTENSITY: \[0,0,0,0,0,0,1\]

From these 7 units, we are then able to express all derived units defined in [Guide for the Use of the International System of Units (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf) and create new ones as needed such as for instance:

-   MASS DENSITY: \[-3,1,0,0,0,0,0\]
-   AREA: \[0,2,0,0,0,0,0\]

*Signature* is the attribute thanks to which unit scaling can be achieved in a generic way.

##### Symbols

Array of \[real, string\] (meaning \[*magnitude*, *symbol*\]) that lists all *symbols* known by FreeCAD. Thanks to this array, the unit scaling API becomes more ergonomic because *symbols* and related *magnitudes* are linked.

This array can be extended as required.

For instance, the list of *symbols* of the LENGTH unit, and their related *magnitudes* is:

[1e+12,"Tm"],[1e+09,"Gm"],[1e+06,"Mm"],
[1e+03,"km"],[1e+02,"hm"],[1e+01,"dam"],
[1e+00,"m"],[1e-01,"dm"],[1e-02,"cm"],
[1e-03,"mm"],[1e-06,"µm"],[1e-09,"nm"],
[1e-12,"pm"],[1e-15,"fm"]

Standard *symbols* can be found on [NIST website](http://physics.nist.gov/cuu/Units/units.html) and p23 to 26 and p32 (*metric ton* or *tonne*) of [The International System of Units (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf).

#### Unit dictionary {#unit_dictionary}

All the units available in FreeCAD, and new ones created by the user, should be stored in *unit dictionary*, which is an XML file (FreeCAD configuration file), so as to be retrieved when needed, i.e. when achieving unit scaling.

##### Units

Array of units, contained in the *unit dictionary*.

#### Unit system {#unit_system}

A *unit system* is the object that allows the user defining the current unit *magnitude* of each base units with which she/he is working. For instance, knowing that the user is working with millimeter, tonne, and second, thanks to the use of a unit system, FreeCAD can know that energy is expressed in terms of milliJoule, force in terms of Newton, and stress in terms of MegaPascal. Hence a unit system is only defined by a *name* (for instance *Standard unit system*) and a *magnitude table* specifying for each of the 7 base units, what is its corresponding *magnitude*.

##### Name

String allowing to the user identifying what is the unit system.

##### Magnitudes

By specifying the magnitude of the 7 base units, a unit system is defined.

For instance \[1e-03, 1e+03, 1, 1, 1, 1, 1\], meaning millimeter, tonne, second, ampere, Kelvin, mole, candela

#### Unit management API {#unit_management_api}

Only the logic of some methods is presented, in order to highlight some features. These methods could belong to an object called *Unit manager*.

##### Checking the unit dictionary {#checking_the_unit_dictionary}

###### isValid

The unit dictionary can be an XML file (FreeCAD configuration file). It contains a list of defined units. Such a dictionary is required for the proposed unit management system to work.

It must fulfills some conditions that should be checked before activating the unit management system. These conditions are:

-   check that all base units are defined
-   check that a *dimension* is not defined twice through the units
-   check that a *symbol* is not defined twice in all the existing symbols
-   check that the *signatures* of all units have all the same size
-   chacke that a *standard symbol* (for which *magnitude* is 1) is defined for all units

###### isCompatibleWithThisSignature

A unit dictionary defines a set of units and their known magnitudes. When managing a unit, it is relevant to check that its signature is compatible with the set of units registered in the unit dictionary, so as to process it. This check includes:

-   check that the input *signature* length is of the same size than the unit dictionary unit *signatures*

##### Scaling units {#scaling_units}

###### scaleUnitFromSymbolToSymbol

Knowing a value, an initial unit by its symbol, the target unit by its symbol, scale the value.

###### scaleUnitFromSymbolToUnitSystem

Knowing a value, an initial unit by its symbol, the target unit system, scale the value.

###### scaleUnitFromUnitSystemToSymbol

Knowing a value, an initial unit system, the target unit by its symbol, scale the value.

#### Motivations for such a management: example of application {#motivations_for_such_a_management_example_of_application}

Let\'s assume that we are going to setup a finite element model. To build our model, we need the mesh, material properties, and to define numerical parameters. Considering that they can be tens of material properties to manage, expressed with different units, sometimes not always very common, it is interesting for the user to only have to specify a global unit system, without caring much.

FreeCAD would then just do the job.

As FreeCAD developpers and FreeCAD users do not necessarily know all units that can be defined in the material property files, it is interesting to rely on a generic system.

Let\'s assume that in such a file we have a fair number of exotic material properties expressed with exotic units, and that we want to work in a specific unit system.

It is easy with the proposed extension to scale any of these properties by knowing their signatures, magnitudes, and the target unit system.

For each of the properties, the scaling is obtained by multiplying the initial property value with the factor $\frac{initialMagnitude}{targetMagnitude}$.

The *targetMagnitude* is then simply obtained with the operation $\prod_{bu} targetMagnitude_{bu}^{signature_{bu}}$, *bu* standing for *base unit*.

It becomes thus very easy to manage any number of properties with any kind of units with very few lines of Python.

## See Also {#see_also}

-   The [Expressions](Expressions#Units.md) page for a list of all known units.
-   The documentation of [Quantity](Quantity.md).
-   The [Std UnitsCalculator](Std_UnitsCalculator.md) tool.


{{Powerdocnavi

}} 

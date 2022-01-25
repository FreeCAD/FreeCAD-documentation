# Units/pt-br
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

## Purpose and principles: proposal of an extension of the unit management system 

An extension unit management system is proposed in the following sections, developping the concept of *unit system*, activated during a running FreeCAD instance. The interest in defining such a new concept is to work more easily with as many type of **physical** units as one wants (even user-created ones), without increasing the complexity of unit management for the user, nor for FreeCAD developpers.

In short, event of unit scaling are localized precisely, and carried out in a generic fashion.

Achieving such a flexibility is most notably required when one starts to deal with material properties that can have very different units, difficult to manage one by one manually.

The reasoning proposed allows handling the units such as described in the [Guide for the Use of the International System of Units (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf) and [The International System of Units (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf) both from NIST.

In this proposal, one first recall in [Brainstorming](Units#Brainstorming.md) section what are the possible contexts for which unit management is required.

In [Organizing](Units#Organizing.md) section, we present the data model retained to achieve unit management, based on 3 objects, the *unit*, the *unit dictionary*, and the *unit system*. Finally, a short API of a 4th object called the *unit manager* is presented as well.

## Outcome

Thanks to this extension, one aims to ease unit scaling that can occurs between different business tasks. For instance, technical drawings can be done in standard unit system, while FE modelling can be managed in an unit system more suited for it.

The exchange of data between these two kind of activities become easier with this extension.

## Brainstorming

In this section are highlighted the contexts of use of such an unit management system. From these contexts, we are then able to defined its technical specifications.

Essentially 2 contexts are given as example.

### Context 1: opening a data file 

This case is probably the most frequent case. You receive a file containing for instance a geometrical model, or describing a material with quite a lot of properties. The geometrical model is expressed in meters, or the material properties according the international unit system.

Too bad\...

You are an expert FE modelling, and you usually work with millimeter for length, MegaPascal for stress, tonne for mass\...

In this context, unit management is required to scale data from an initial unit system defined in the input file to a user-defined target unit system.

### Context 2: switching the unit system at runtime 

In this case, you can be at the same time the guy that carries out a drawing, and the guy that will manage the FE modelling. Similarly to the previous case, the unit systems for these 2 tasks are not the same, and you need to switch the initial unit system at runtime to your favorite one.

## Organizing

### Logic of unit scaling 

In the [Brainstorming](Units#Brainstorming.md) section have been presented 2 contexts when using unit scaling. Some items should be highlighted from these two contexts.

#### Unit coherence throughout the FreeCAD running instance 

The system proposed is based on a primary assumption: the user is working in a coherent unit system. For instance, this means that if the user expresses length in millimeters, necessarily areas will be expressed in terms of squared millimeters, not squared meters. This is **hypothesis one**.

#### Unit system 

Because of *hypothesis one*, it is possible and relevant to define an unit system. An unit system applies to:

-   a running FreeCAD instance into which you are working
-   or it may also apply globally to the content of an input file

According [Guide for the Use of the International System of Units (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf) from NIST, they are 7 physical base units. We chose to express a unit system in terms of these 7 base units.

When working within an instance of FreeCAD, the user has thus to define first the unit system according to which she/he is working before she/he decides to switch to another unit system, or before importing data from an input file.

This unit system will apply till the user decides to change it. If she/he does, all data with dimensions will be scaled.

Considering *hypothesis one*, all data that the user will input manually in FreeCAD are assumed to be coherent with the chosen unit system.

The benefit to work with a *unit system* defined at a FreeCAD running instance level, or at data file level (instead of *unit* which are defined at the data level) is then that unit management is considerably simplified.

Here are some examples of unit systems.

-   meter, kilogram, second, ampere, Kelvin, mole, candela
-   millimeter, tonne, millisecond, ampere, Kelvin, mole, candela
-   millimeter, kilogramme, millisecond, ampere, Kelvin, mole, candela
-   \...

#### Base and derived units 

Derived units are created by combination of base units. For instance, an acceleration (m/s) combines at the same time length and time. An interesting picture presenting the relationships between base and derived units can be seen [here](http://physics.nist.gov/cuu/pdf/SIDiagramColorAnnot.pdf) also from NIST.

Thanks to the definition of *unit system*, it is possible for the user to work with any kind of derived units, without the need for FreeCAD developpers to foresee them in advance.

#### Base and derived unit symbols 

According to [The International System of Units (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf), the symbols to specify a units are officially approved. Two consequences can be highlighted from this.

-   it is not easy for a computer program to work with unit symbols because some are greek letters for instance. Hence they can be a bit difficult to process by a program
-   while some units and their symbols can be used widely, they may be not approved officially, like for instance *tonne* unit (see p32 of [The International System of Units (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf))

To overcome these limitations and remain flexible, the proposed system favors the use of unit magnitudes instead of unit symbols, which remain nonetheless available for an ergonomy reason.

### Data model 

The three core objects of the unit management system are presented, namely the *unit*, the *unit dictionary* and the *unit system*.

#### Unit

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

#### Unit dictionary 

All the units available in FreeCAD, and new ones created by the user, should be stored in *unit dictionary*, which is an XML file (FreeCAD configuration file), so as to be retrieved when needed, i.e. when achieving unit scaling.

##### Units

Array of units, contained in the *unit dictionary*.

#### Unit system 

A *unit system* is the object that allows the user defining the current unit *magnitude* of each base units with which she/he is working. For instance, knowing that the user is working with millimeter, tonne, and second, thanks to the use of a unit system, FreeCAD can know that energy is expressed in terms of milliJoule, force in terms of Newton, and stress in terms of MegaPascal. Hence a unit system is only defined by a *name* (for instance *Standard unit system*) and a *magnitude table* specifying for each of the 7 base units, what is its corresponding *magnitude*.

##### Name

String allowing to the user identifying what is the unit system.

##### Magnitudes

By specifying the magnitude of the 7 base units, a unit system is defined.

For instance \[1e-03, 1e+03, 1, 1, 1, 1, 1\], meaning millimeter, tonne, second, ampere, Kelvin, mole, candela

#### Unit management API 

Only the logic of some methods is presented, in order to highlight some features. These methods could belong to an object called *Unit manager*.

##### Checking the unit dictionary 

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

##### Scaling units 

###### scaleUnitFromSymbolToSymbol

Knowing a value, an initial unit by its symbol, the target unit by its symbol, scale the value.

###### scaleUnitFromSymbolToUnitSystem

Knowing a value, an initial unit by its symbol, the target unit system, scale the value.

###### scaleUnitFromUnitSystemToSymbol

Knowing a value, an initial unit system, the target unit by its symbol, scale the value.

#### Motivations for such a management: example of application 

Let\'s assume that we are going to setup a finite element model. To build our model, we need the mesh, material properties, and to define numerical parameters. Considering that they can be tens of material properties to manage, expressed with different units, sometimes not always very common, it is interesting for the user to only have to specify a global unit system, without caring much.

FreeCAD would then just do the job.

As FreeCAD developpers and FreeCAD users do not necessarily know all units that can be defined in the material property files, it is interesting to rely on a generic system.

Let\'s assume that in such a file we have a fair number of exotic material properties expressed with exotic units, and that we want to work in a specific unit system.

It is easy with the proposed extension to scale any of these properties by knowing their signatures, magnitudes, and the target unit system.

For each of the properties, the scaling is obtained by multiplying the initial property value with the factor $\frac{initialMagnitude}{targetMagnitude}$.

The *targetMagnitude* is then simply obtained with the operation $\prod_{bu} targetMagnitude_{bu}^{signature_{bu}}$, *bu* standing for *base unit*.

It becomes thus very easy to manage any number of properties with any kind of units with very few lines of Python.

## See Also 

-   The [Expressions](Expressions#Units.md) page for a list of all known units.
-   The documentation of [Quantity](Quantity.md).
-   The [Std UnitsCalculator](Std_UnitsCalculator.md) tool.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Units/pt-br

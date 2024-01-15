# Material
## Overview




This page is about the Material data system in FreeCAD.

It is currently being edited to reflect changes to the Material system currently under development.

## Abstract

In a departure from how it was implemented in previous versions, materials are no longer implemented as a simple dictionary. The previous system had the advantage of simplicity with the disadvantage of a limited range when describing material properties.

In the new system properties are defined separately as a series of YAML files. Properties are then combined into a property description with values specified for the required properties. Newer data types, such as arrays, mean that this can no longer be accessed using simple dictionaries. Rather an API is used to access the material property and data values. This allows for greater capabilities than was previously possible.

## Tools

There are some good resources out there handle materials more easy:

-   [Units calculator](http://www.dimensionengine.com/) to get your material information in the Unit needed for FreeCAD
-   [<http://www.matweb.com/>](http://www.matweb.com/) [free of charge](http://matweb.com/reference/terms.aspx) Material database with thousands of material values
-   [UUID generator](https://www.uuidgenerator.net/) to create unique UUIDs for new models. A Version 4 UUID is recommended.

## Properties

In contrast with the previous materials standard, material properties are clearly defined. They have been designed to be granular and extensible. Properties can inherit multiple properties adding only what is different. This will improve searching and simplify implementation.

Currently there is no dedicated property editor. It can be edited using any YAML tool, or a simple editor such as nano or notepad.

The property definition files are referred to as models.

### Example Property Model YAML file 


```python
 Model:
   Name: 'Linear Elastic'
   UUID: '7b561d1d-fb9b-44f6-9da9-56a4f74d7536'
   URL: 'https://en.wikipedia.org/wiki/Linear_elasticity'
   Description: >
     Materials that are linearly elastic obey Hooke's law i.e. the stress and
     strain relationship is linear
   DOI: "10.1016/j.ijplas.2004.06.004"
   Inherits:
     - Density:
       UUID: '454661e5-265b-4320-8e6f-fcf6223ac3af'
     - IsotropicLinearElastic:
       UUID: 'f6f9e48c-b116-4e82-ad7f-3659a9219c50'
   AngleOfFriction:
     Type: 'Quantity'
     Units: 'deg'
     URL: 'https://en.wikipedia.org/wiki/Friction#Angle_of_friction'
     Description: >
       Further information can be found at
       https://en.wikipedia.org/wiki/Mohr%E2%80%93Coulomb_theory
   CompressiveStrength:
     Type: 'Quantity'
     Units: 'kPa'
     URL: 'https://en.wikipedia.org/wiki/Compressive_strength'
     Description: "Compressive strength in [FreeCAD Pressure unit]"
```

Rather than a large monolithic definition file, properties are granular, typically focused on a specific task. Models fall into two basic categories:

-   Physical models: identified by the keyword \'Model\' as shown here, these define physical properties of the material
-   Appearance models: identified by the keyword \'AppearanceModel\', these define how the material will be displayed.

Each model has a unique identifier, or UUID, that is used to reference it internally. Consistency of this UUID is important as changing it for one document can also affect other documents. As a general rule, additions to the definition don\'t require an identifier change, as they can still be used in other documents, but value changes would require a new UUID.

An optional URL can link to a detailed description of the material property being described. Given that this is a description of the property and not the material itself it should be pretty generic at this point. A shorter description, typically one or two lines, can be included in the model description as well.

Each material can also include a DOI (Digital Object Identifier) that links through <https://www.doi.org/> to a research publication or similar item of interest.

#### Inheritance

Inheritance is a new capability. There are two principal use cases.

One use case is to provide the ability to tweak models without breaking other documents. For example, in cases where a property type is different, you can define a derived property model that only changes that specific property without breaking any existing documents that reference it.

A second use case is to group properties in a searchable fashion. For example, all physical objects have density, and in many cases that will be all the information available for that material. In cases where linear elasticity properties are available, we would want to include those as well. In yet another example where the elasticity is different in different directions, such as wood, we can define yet another model that is derived from density. Information is not duplicated across the 3 property models. Additionally, we can do a search for materials that have the density property and return all three models.

The example shown above inherits from two other property definitions. It does this by specifying the \'Inherits\' keyword followed by a list of the model names and identifiers. If there is no inheritance this section may be omitted.

#### Properties 

Properties are defined by providing the name of the property followed by a series of descriptors. The \'Type\' descriptor is always required. The remaining descriptors are only required if required to complete the Type information. The URL and description are optional but recommended where possible.

  Name          Description
   
  Type          The property type. See the next section
  Columns       Columns in 2D or 3D arrays. See description below.
  Units         The units associated with the Quantity type.
  URL           A link to a detailed description of the property.
  Description   A short description of the property.

  : Property Descriptors

#### Property Types 

  Type Name         Description
   
  String            A character string.
  Integer           An unsigned integer.
  Float             A floating point number.
  URL               A URL such as <https://www.freecad.org>.
  Quantity          A FreeCAD quantity that includes a floating point numeric value and units appropriate to the property.
  Color             A string in the form of (r,g,b,a) or (r,g,b) where r=red, g=green, b=blue, a=alpha as floating point values between 0 and 1.
  File              Path to a file.
  FileList          A list of file paths. See description below.
  Image             Embedded image file saved as Base64. This can result in a very large material card file.
  ImageList         A list of embedded image files saved as Base64. This can result in a very large material card file. See description below.
  List              A list of string values.
  MultiLineString   A character string that spans multiple lines.
  2DArray           A 2 dimensional array. See description below.
  3DArray           A 3 dimensional array. See description below.

  : Property Types

#### Lists

There are three list types: \'List\', \'FileList\', and \'ImageList\'. In reality all three are the same except that they use different editors. For the \'FileList\', each entry has a file chooser. Similarly the \'ImageList\' opens the image editor. \'ImageList\' is different in that it is a very large string representation of an image and may produce extremely large material card files. Use with caution.

#### 2D Arrays 

Arrays have some unique properties compared to other property types. Each of the array columns need to be described necessitating the addition of the \'Columns\' property. The columns property is then a list of properties describing each column.

2D arrays have a minimum of 2 columns, and only support the \'Quantity\' property type. This may be expanded to other property types in future.

Values in the array are specified by providing a value from the first column.


```python
  TestArray2D3Column:
    Type: '2DArray'
    Columns:
      Temperature:
        Type: 'Quantity'
        Units: 'C'
        URL: ''
        Description: "Temperature"
      Density:
        Type: 'Quantity'
        Units: 'kg/m^3'
        URL: 'https://en.wikipedia.org/wiki/Density'
        Description: "Density in [FreeCAD Density unit]"
      InitialYieldStress:
        Type: 'Quantity'
        Units: 'kPa'
        URL: ''
        Description: >
          Saturation stress for Voce isotropic hardening [FreeCAD Pressure unit]
    URL: ''
    Description: >
      2 Dimensional array showing density and initial yield stress with temperature
```

#### 3D Arrays 

3D arrays are similar in implementation to 2D arrays described in the previous sections. There is a \'Columns\' keyword followed by a list of properties to describe the columns. The first column describes the depth or 3rd dimension of the array, with the remaining columns describing the remaining columns. This can be thought of as an indexed list of 2 dimensional arrays.

Since a 2 dimensional array requires a minimum of 2 dimensions, this will require a minimum of 3 columns.

Values in the array are accessed by first specifying the depth, then the value from the first column of the 2D array (the second column here).


```python
  TestArray3D:
    Type: '3DArray'
    Columns:
      Temperature:
        Type: 'Quantity'
        Units: 'C'
        URL: ''
        Description: "Temperature"
      Stress:
        Type: 'Quantity'
        Units: 'MPa'
        URL: ''
        Description: "Stress"
      Strain:
        Type: 'Quantity'
        Units: 'MPa'
        URL: ''
        Description: "Strain"
    URL: ''
    Description: >
      3 Dimensional array showing stress and strain as
      a function of temperature
```

#### A note about arrays 

These are a new feature not previously available. Many capabilities may be added in the future that aren\'t currently implemented. For example, arrays with columns of strings are potentially useful but not currently implemented.

Interpolation is an important feature that isn\'t currently implemented. For example, an array with row entry values of 1 and 2 will only return exact matches. So a lookup of 1.5 will return an error. In future, the arrays will determine an approximate value by interpolating from available data.

## Material Database 

Given that above standard is implemented, it would be stupid to store all the properties again and again to objects. Basically we can build up a Material DB with the Name as a primary key. So if you have no special needs for your material, you just define e.g. Name=Steel and FreeCAD can retrieve all properties from that DB. Every additional property you set in the map overrides the one from the DB.

In the future we can host that DB somwhere in the Web and build up a general OpenSource material DB.

At the moment I think of a compiled in mini dataset with a set of \"basic\" materials and its basic properties and a SQLite based full version.

## Material.py

Since handling material-properties is a tedious work we should implement a Python front-end module called **Material.py** [https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Material/Material.py source](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Material/Material.py_source.md). This will be the place to implement all kind of helper methods for material handling.

-   Calculation of Mass out of Volume and Density
-   Translation in different unit systems
-   Calculation needed in special application (e.g. FEM)
-   and anything else we don\'t know yet

The module should be implemented that way it can run in FreeCAD or stand alone on the command line (material-property-map has be given as python map).

## The FreeCAD material card file format 

Working with materials means often import/export material-definitions. Therefore a file format is needed. Since we have only key/value form, we can use a simple and easy to read and parse file format. Therefore the [ini-file](http://en.wikipedia.org/wiki/INI_file) format is chosen. Its standardized and there are already parser available. E.g the [Config parser module in python](http://docs.python.org/2/library/configparser.html).

Each material definition resides in a file with the ending **.FCMat**. Some of these files are part of the FreeCAD source and get compiled into the binary. This is to save overhead in distribution and access. But also files can be placed and searched on different places to allow additional non-standard material definitions.

### Example .FCMat file 


```python
 ; last modified 1 April 2001 by John Doe
 
 Name=Steel_Cast
 Father=Steel
 Source=Some material book everyone knows (or not) ;Some comment
  
 [EN10027]
 ; steel standard EN 10027-1
 Name=S235JR+AR      
 
 [Graphic]
 EmissiveColor = 255,255,255
```

## Material properties 

Here now the description of agreed material-properties. Feel free to add a subsection for the material-properties of you field of expertise.

### General

  property name    Description                                                                                                                                                                       Unit/Data-Type
    
  Name             Unique name of the property, following the rules described above                                                                                                                  ASCII string 7-bit
  Father           Name of the material group this material belongs to. If defined this material inherits all the father properties. That means if not defined the father properties will be used.   ASCII string 7-bit
  Description      A placeholder for a longer description of the material                                                                                                                            ASCII string 7-bit
  SpecificWeight   The specific weight (also known as the unit weight) is the weight per unit volume of a material. see: [Specific_weight](http://en.wikipedia.org/wiki/Specific_weight)             kg/mm$^3$
  Vendor           Specifies the brand or vendor of the material                                                                                                                                     ASCII string 7-bit
  ProductURL       An URL where to find more information about the material                                                                                                                          ASCII string 7-bit
  SpecificPrice    The price per unit of this material. Units can vary a lot (USD/m$^3$, EUR/piece, etc\...)                                                                                         ASCII string 7-bit

  : General material properties

**ToDos:** add some properties with an ordering system for materials (metal, alloy, mineral, wood, \....)

### Mechanical

  property name                         Description                                                                                                                                                                                                                                                                                                                            Unit/Data-Type
    
  Young\'s Modulus                      Young\'s modulus, also known as the tensile modulus or elastic modulus, is a measure of the stiffness of an elastic material and is a quantity used to characterize materials. See: [Young\'s modulus](http://en.wikipedia.org/wiki/Young%27s_modulus)                                                                                 kg\*mm\^-1\*s\^-2 (kPa)
  Poisson\'s Ratio                      The lateral contraction of materials under tension as a fraction of their elongation. See: [Poisson\'s Ratio](https://en.wikipedia.org/wiki/Poisson%27s_ratio)                                                                                                                                                                         Dimensionless (-)
  Yield Strength                        The stress at which a ductile material (like steel) starts to develop plastic (irreversible) deformation. See: [Yield Strength](https://en.wikipedia.org/wiki/Yield_(engineering))                                                                                                                                                     N\'\*mm\^-2 (MPa)
  Ultimate Tensile Strength (UTS)       The stress at which the material ruptures. For ductile materials this may be after experiencing significant plastic deformation (see Yield Strength). For brittle material Yield strength and Ultimate Tensile Strength coincide. See: [UTS](https://en.wikipedia.org/wiki/Ultimate_tensile_strength)                                  N\'\*mm\^-2 (MPa)
  Yield Points                          Used in a FEM non-linear material object to describe a ductile uni-axial stress-strain curve of a material. The values are entered as (yield stress, plastic strain) tuples, where the first combination is (Yield Strength, 0) and the last (UTS, Fracture Strain) See: [YieldPoints](https://en.wikipedia.org/wiki/Work_hardening)   (N\'\*mm\^-2 (MPa), dimensionless (-)
  Uniaxial Compressive Strength (FCK)   The compressive strength of concrete, defined as the strength of a 150 mm size cube tested at 28 days. See [FCK](http://eurocodes.jrc.ec.europa.eu/doc/WS2008/EN1992_1_Walraven.pdf)                                                                                                                                                   N\'\*mm\^-2 (MPa)
  Friction Angle (PHI)                  The angle of internal friction of a granular material like sand or concrete, as used in the Mohr-Coulomb yield criterion. See [PHI](https://en.wikipedia.org/wiki/Mohr%E2%80%93Coulomb_theory)                                                                                                                                         degrees (-)
  Hardness                              Des\...                                                                                                                                                                                                                                                                                                                                
  EN-10027-1                            In case of steel material the [Steel grade](http://en.wikipedia.org/wiki/Steel_grades) as defined in the [European standard](http://en.wikipedia.org/wiki/European_Committee_for_Standardization) No. 10027-1.                                                                                                                         string ASCII 7-bit

  : Material properties used in mechanical or structural engineering

**ToDos:** further add properties needed for mechanical design.

### Graphical

This section defines material-properties which are related to the visual appearance of the material. The

  property name    Description                                                                                          Unit/Data-Type
    
  AmbientColor     Ambient color in the Coin3D color model                                                              float,float,float range: 0.0-1.0
  DiffuseColor     Diffuse color in the Coin3D color model                                                              float,float,float range: 0.0-1.0
  SpecularColor    Specular color in the Coin3D color model                                                             float,float,float range: 0.0-1.0
  EmissiveColor    Emissive color in the Coin3D color model                                                             float,float,float range: 0.0-1.0
  SectionColor     Color shown when the material is cut in the Coin3D color model                                       float,float,float range: 0.0-1.0
  Shininess        Ambient color in the Coin3D color model                                                              float range: 0.0-1.0
  Transparency     Ambient color in the Coin3D color model                                                              float range: 0.0-1.0
  VertxShader      Vertex shader program as defined in [GlSl](http://de.wikipedia.org/wiki/OpenGL_Shading_Language)     Multi line string ASCII 7-bit
  FragmentShader   Fragment shader program as defined in [GlSl](http://de.wikipedia.org/wiki/OpenGL_Shading_Language)   Multi line string ASCII 7-bit

  : visual appearance

### Thermal

  property name                 Description                                                                                                                                                          Unit/Data-Type
    
  ThermalConductivity           The [thermal conductivity (R or lambda coefficient)](http://en.wikipedia.org/wiki/Thermal_conductivity) that indicates the capacity to transfer heat of a material   W/m²K
  ThermalExpansionCoefficient                                                                                                                                                                        
  SpecificHeat                                                                                                                                                                                       

  : Thermal properties

### Architecture and BIM 

  property name       Description                                                                                                                                                                                                                                                                                                                                                 Unit/Data-Type
    
  StandardCodeXXXX    Where XXXX is the name of the standard (for example taken from [the BlenderBIM standards repository](https://github.com/Moult/IfcClassification/tree/master/ifc)). For example, StandardCodeUniclass2. The value is the specific code of this material in the given standard. This property can appear several times, each with a different standard code   String ASCII 7-bit
  FireStandard        The fire rating standard used in the material                                                                                                                                                                                                                                                                                                               String ASCII 7-bit
  FireClass           The [fire resistance class](http://en.wikipedia.org/wiki/Fire-resistance_rating) of the material in the above standard                                                                                                                                                                                                                                      String ASCII 7-bit
  SoundTransmission   The sound transmission coefficient of this material                                                                                                                                                                                                                                                                                                         W/m$^2$K
  Finish              The type of finishing/coating of this material                                                                                                                                                                                                                                                                                                              String ASCII 7-bit
  Color               The color specification of this material. This is not necessarily the color to display in the viewport, but might be for ex. the color name specified in a furnisher\'s catalog                                                                                                                                                                             String ASCII 7-bit
  UnitsArea           The number of units of this material necessary to fill a certain area. For example, in the case of a brick, 45 bricks/m²                                                                                                                                                                                                                                    Units/m$^2$

  : Material properties used in architectural design

## TODO

-   add sustainability & LEED properties

 {{FEM Tools navi}}



---
⏵ [documentation index](../README.md) > [Developer](Category_Developer.md) > [Developer Documentation](Category_Developer Documentation.md) > [Roadmap](Category_Roadmap.md) > [BIM](Category_BIM.md) > [File_Formats](Category_File_Formats.md) > [Arch](Category_Arch.md) > [FEM](Category_FEM.md) > Material

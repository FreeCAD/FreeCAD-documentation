 

## Overview

 

This page is about the Material data system in FreeCAD.

## Abstract

Since it is hard, or even impossible, to define a fixed or complete set of material properties, we go a more open way. Every object in FreeCAD which has to deal with material will have a Property named \"Material\". This is comprised of a key/value list that can hold an infinite number of material properties. Since this is a very open and extensible way to deal with such data, it also holds the danger of disorganization and chaos. Therefore this page defines some rules and basic properties for dealing with such material-property-maps.

## Rules

Every property set has only one mandatory entry which is \"Name\". This is the primary key of the material. The rest of the material properties are optional or can be retrieved out of a material DB.

Property names (key) are ordered by strings separated by underscores. The first substring is named by the application or standard, the following can be used to further group the properties. The Values can also be grouped by underscores, e.g. to separate different sorts of steel. Examples:

-   Name=Steel\_Cast
-   SpecificWeight=7.85 (at 20° in kg/mm3)
-   EN10027\_name = S235JR+AR (steel standard EN 10027-1)
-   FEM\_YoungsModulus = xx (in mm−1·kg·s−2)
-   FEM\_YoungsModulus\_Z
-   FEM\_YoungsModulus\_X

Each property has a human readable description on this Material page, with links to further information (e.g. Wikipedia).

For each property a unit has to be defined, based on the FreeCAD internal unit mm-kg-s! That allows consistent usage and translation.

The key (name) and the value of the property uses only ASCII characters (7-bit). The keys are written in Camel-Case but interpreted case-insensitive.

The underscores allow later a tree view property editor/viewer which allow folding.

## Tools

There are some good resources out there handle materials more easy:

-   [Units calculator](http://www.dimensionengine.com/) to get your material information in the Unit needed for FreeCAD
-   [<http://www.matweb.com/>](http://www.matweb.com/) [free of charge](http://matweb.com/reference/terms.aspx) Material database with thousands of material values

## Material Database {#material_database}

Given that above standard is implemented, it would be stupid to store all the properties again and again to objects. Basically we can build up a Material DB with the Name as a primary key. So if you have no special needs for your material, you just define e.g. Name=Steel and FreeCAD can retrieve all properties from that DB. Every additional property you set in the map overrides the one from the DB.

In the future we can host that DB somwhere in the Web and build up a general OpenSource material DB.

At the moment I think of a compiled in mini dataset with a set of \"basic\" materials and its basic properties and a SQLite based full version.

## Material.py

Since handling material-properties is a tedious work we should implement a Python front-end module called {{FileName|Material.py}}. This will be the place to implement all kind of helper methods for material handling.

-   Calculation of Mass out of Volume and Density
-   Translation in different unit systems
-   Calculation needed in special application (e.g. FEM)
-   and anything else we don\'t know yet

The module should be implemented that way it can run in FreeCAD or stand alone on the command line (material-property-map has be given as python map).

## The FreeCAD material card file format {#the_freecad_material_card_file_format}

Working with materials means often import/export material-definitions. Therefore a file format is needed. Since we have only key/value form, we can use a simple and easy to read and parse file format. Therefore the [ini-file](http://en.wikipedia.org/wiki/INI_file) format is chosen. Its standardized and there are already parser available. E.g the [Config parser module in python](http://docs.python.org/2/library/configparser.html).

Each material definition resides in a file with the ending {{FileName|.FCMat}}. Some of these files are part of the FreeCAD source and get compiled into the binary. This is to save overhead in distribution and access. But also files can be placed and searched on different places to allow additional non-standard material definitions.

### Example .FCMat file {#example_.fcmat_file}


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

## Material properties {#material_properties}

Here now the description of agreed material-properties. Feel free to add a subsection for the material-properties of you field of expertise.

### General

  property name    Description                                                                                                                                                                       Unit/Data-Type
  ---------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------
  Name             Unique name of the property, following the rules described above                                                                                                                  ASCII string 7-bit
  Father           Name of the material group this material belongs to. If defined this material inherits all the father properties. That means if not defined the father properties will be used.   ASCII string 7-bit
  Description      A placeholder for a longer description of the material                                                                                                                            ASCII string 7-bit
  SpecificWeight   The specific weight (also known as the unit weight) is the weight per unit volume of a material. see: [Specific\_weight](http://en.wikipedia.org/wiki/Specific_weight)            kg/mm$^3$
  Vendor           Specifies the brand or vendor of the material                                                                                                                                     ASCII string 7-bit
  ProductURL       An URL where to find more information about the material                                                                                                                          ASCII string 7-bit
  SpecificPrice    The price per unit of this material. Units can vary a lot (USD/m$^3$, EUR/piece, etc\...)                                                                                         ASCII string 7-bit

  : General material properties

**ToDos:** add some properties with an ordering system for materials (metal, alloy, mineral, wood, \....)

### Mechanical

  property name                         Description                                                                                                                                                                                                                                                                                                                            Unit/Data-Type
  ------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------
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
  ---------------- ---------------------------------------------------------------------------------------------------- ----------------------------------
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
  ----------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------
  ThermalConductivity           The [thermal conductivity (R or lambda coefficient)](http://en.wikipedia.org/wiki/Thermal_conductivity) that indicates the capacity to transfer heat of a material   W/m²K
  ThermalExpansionCoefficient                                                                                                                                                                        
  SpecificHeat                                                                                                                                                                                       

  : Thermal properties

### Architecture and BIM {#architecture_and_bim}

  property name       Description                                                                                                                                                                                                                                                                                                                                                 Unit/Data-Type
  ------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------
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

[Category:Developer{{\#translation:}}](Category:Developer.md) [Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Roadmap{{\#translation:}}](Category:Roadmap.md) [Category:BIM{{\#translation:}}](Category:BIM.md) [Category:File\_Formats{{\#translation:}}](Category:File_Formats.md)

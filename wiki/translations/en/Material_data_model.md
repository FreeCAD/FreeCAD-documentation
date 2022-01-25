# Material data model/en
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

## Purpose and principles 

By storing material properties in an unified data structure, one aims to ease data retrieval that can be carried out in different contexts:

-   when building a finite element model
-   when rendering a 3D model
-   to be able to track changes in a material of a *component* created in FreeCAD, for [PDM](http://en.wikipedia.org/wiki/Product_Data_Management) applications,
-   BIM application (architecture and construction industry)

To manage material properties, it is proposed to create a specific data model that will be instanced when a new material is created whithin FreeCAD.

It will be possible to create a material either by defining by hand its properties through a material workbench, or by reading material properties from a file. The formats of such files is to be defined (some already exist, like MatML, STEP AP235 & IGR45\...).

Also, it will be possible to save the material properties in a collection of files in a format still to be chosen as well. The collection of files that can be stored in a common directory will form the FreeCAD material database.

Through this data model, material can be defined in FreeCAD without the need to define a *component*.

A new pointer will be created in the *component* data model, to link to a material that has been defined through the material data model.

## Outcome

Through this material data model, it is proposed to offer a tool to manage easily material data within FreeCAD.

## Brainstorming

## Organizing

Different kinds of data need to be managed to describe a material. A material data model is proposed below. Some examples of the data that can be stored within this structure are given as well.

### Material data model 

In addition to classical \"string\" attributes like a name, and a family, 3 different specific kinds of information need to be managed to describe a material in FreeCAD.

-   properties: generic structure to store data describing the engineering properties of the material
-   chemical composition: chemical composition of the material
-   appearance: information describing how the material will look like in FreeCAD (color, shininess\...)

All of these kind of information do not need necessarily to be defined for the material to exist. Finally, below is the list of attributes retained to describe a material in FreeCAD.

#### Name

A string indicating the name of the material. It is its designation.

#### Family

A string indicating the family of the material, such as for instance:

-   metal
-   plastic
-   \...

Additionnally, it is proposed to create a map between the families (for instance stored in a XML file) so as to be able to browse the FreeCAD material database.

Such a map could for instance contain a tree presenting relationships between families, like:

-   metal -\> steel -\> flat carbon steel -\> advanced high strength steel
-   metal -\> aluminium -\> casted aluminium

#### Manufacturer

A string indicating the manufacturer of the material.

#### URL

A string indicating the web page presenting the material.

#### Properties

##### Description

The material data model includes a collection of properties. The size of such a collection is not fixed and may be extended with new user-defined properties.

A property contains the following attributes.

-   name: string
-   symbol: string to write the symbol of the properties (?in Latex math format?)
-   type: \"scalar\" or \"array\"
-   value: scalar (if it is a scalar)
-   values: array (if it is an array)
-   parameterNames: array of strings (for \"array\" type property)
-   parameterValues: array of scalars (for \"array\" type property)
-   unit & unitMagnitude (specific object described in [Units](Units.md)) (to be noted: examples include unitMagnitude, while I am not completely sure that this should be defined at property level. The unit system may be defined at material level)
-   direction: a vector indicating in which direction is to be understood the property value. The vector is itself a FreeCAD object expressed in the global coordinate system or in a user-defined coordinate system
-   notes: string that can be used to describe a bit more the property like what is its meaning, how has it been measured\... It can also help to understand the name of the properties

Material properties will be identified thanks to their name in order to process them, i.e. for instance writing the Yield strength in a finite element model. In order to ease material data creation within FreeCAD, a standardized list of property names along with their standard units will be proposed to the user. Nonetheless, the user is free to create new properties, with new names, new units, and so on\...

Below is proposed the dictionary of standard properties. Feel free to add new ones.


<?xml version="1.0" encoding="UTF-8"?>



  
        
     








Notes: \"Mean Lankford coefficient is representative of the anisotropy of a thin metal sheet.\" \"The Hardening coefficient is representative of the hardening capacity of a metal. It appears in Hollomon formula that can relates cumulated plastic strain to stress.\"

##### Example 1: Cost per tonne 

A first example is given below to show how a *Cost per tonne* property can be stored.

-   name: Cost per tonne
-   symbol: not applicable
-   type: scalar
-   value: 500
-   values: not applicable (but could be: for instance different cost values per different countries)
-   parameterNames: not applicable (but could be: for instance different cost values for different countries)
-   parameterValues: not applicable (but could be: for instance different cost values for different countries)
-   parameterUnits: not applicable
-   unit & unitMagnitude: \[\[ 0, -3, 0, 0, 0, 0, 0\], 1\]
    -   meaning m\^(-3) (more details about unit & unit system specifications in [Units](Units.md) page)
-   direction: not applicable

##### Example 2: Yield strength 

A second example is given below to show how the *Yield strength* property can be stored.

-   name: Yield stress
-   symbol: YS
-   type: scalar
-   value: 450
-   values: not applicable
-   parameterNames: not applicable
-   parameterValues: not applicable
-   parameterUnits: not applicable
-   unit & unitMagnitude: \[\[ -1, 1, -2, 0, 0, 0, 0\], 1\]
    -   meaning Pa (more details about unit & unit system specifications in [Units](Units.md) page)
-   direction: \[ 1, 0, 0\] in global coordinate system
    -   given a steel sheet, this means that the *Yield strength* given is expressed in *x* direction, that can be for instance the rolling direction

##### Example 3: Strain hardening 

A third example is given below to show how the *Strain hardening* property can be stored. This is a more complex example because *Strain hardening* is represented by a serie of curves. The curves represent the stress evolution with respect to plastic strain. 3 curves have been obtained at different strain rates. All curves have been obtained at room temperature.

-   name: Strain hardening
-   symbol: not applicable
-   type: scalar
-   value: not applicable
-   values: \[\[0., 100, 150, 200\], \[ 0., 120, 180, 210\], \[ 0., 140, 190, 220\]\]
-   parameterNames: \[Plastic strain, Strain rate, Temperature\]
-   parameterValues:
    -   The 1st three arrays represents plastic strain evolutions
    -   The 2nd serie of three arrays represents the strain rate evolutions. A single value is given in each of the arrays, meaning that the strain rate doesn\'t change for each the corresponding stress evolutions.
    -   The last serie of a single array represents temperature evolutions. This time a single value is written in a single array, meaning that temperature doesn\'t change for a given array of stress, and this applies for all stress arrays.
        1.  1st serie: \[\[\[0. , 0.4, 0.8, 1\], \[ 0, 0.4, 0.8, 1\], \[ 0, 0.4, 0.8, 1\]\],
        2.  2nd serie: \[\[0.\] , \[100\] , \[1000.\] \],
        3.  3rd serie: \[\[18.\] \],\]
-   parameterUnits & parameterUnitMagnitudes: \[\[\[ 0, 0, 0, 0, 0, 0, 0\], 1\], \[\[ 0, 0, -1, 0, 0, 0, 0\], 1\], \[\[ 0, 0, 0, 0, 1, 0, 0\], 1\]\]
    -   meaning none, s\^(-1) and, K (more details about unit & unit system specifications in [Units](Units.md) page)
-   unit & unitMagnitude: \[\[ -1, 1, -2, 0, 0, 0, 0\], 1\]
    -   meaning Pa (more details about unit & unit system specifications in [Units](Units.md) page)
-   direction: not applicable

#### Chemical composition 

\[Yet to be filled up\]

#### Appearance

\[Yet to be filled up\]

#### Notes

A string where the user can add its own comments about the material.

### Material data model applications: some examples 

##### Example 1: Brick masonry 

###### Name 

Brick masonry

###### Family 

?string?

###### Properties 

-   *Weight*: 1kg/m³
-   *Cost per cubic meter*: 1€/m³
-   *Number of bricks por base unit*: ?float?
-   *Volume of mortar por base unit*: ?float?
-   *Mortar type*: ?string?
-   *Brick type*: ?string?
-   *Fire resistance class*: ?string?
-   *Thermal conductivity*: 1 W/mK

###### Manufacturer 

?string?

###### URL 

?string?

###### Notes 

Notes about maintainance, special cares to be taken, etc\...

CSI/MasterFormat code (as there are several systems used in the industry which give to all material a special code, I propose to enter it in the notes, because it doesn\'t appear to me relevant create a specific properties that we won\'t be able to name exactly).

## Next actions 

-   Define a set of names for classical properties, that we can define in a dictionary (FreeCAD configuration file). These properties will most notably be re-used in other contexts like the FEM module.
-   Fill up *Chemical composition* section.
-   Fill up *Appearance* section.
-   Define a set of default chemical components.
-   Review by other people.
-   Implement in C++ data model and ability to write/read in a file (ISO 10303-45 through SCL?).
-   Implement XML dictionaries to store default properties, with their units, that can be used by the user.
-   Implement python GUI to handle this data.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > [Material](Material_Workbench.md) > Material data model/en

# Material data model/es



**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

## Propósito y principios 

Para almacenar propiedades de materiales en una estructura de datos unificada, una de las intenciones es facilitar la recuperación de datos que pueden llevarse en diferentes contextos:

-   Cuando se construye un modelo para elementos finitos
-   Cuando se renderiza un modelo 3D
-   Para permitir registrar cambios en un material de un *componente* creado en FreeCAD, para aplicaciones [PDM](http://en.wikipedia.org/wiki/Product_Data_Management),
-   Aplicación BIM (industria de arquitectura y construcción)

Para manejar propiedades de materiales, se ha propuesto crear un modelo de datos específico que será replicado cuando un nuevo material sea creado con FreeCAD.

Ello posibilitará crear un material ya sea definiendo manualmente sus propiedades a través del entorno de materiales, o leyendo las propiedades del material desde un archivo. El formato de dichos archivos está por definir (algunos ya existen, como MatML, STEP AP235 & IGR45\...).

También, será posible guardar las propiedades del material en una colección de archivos en un formato también aún pendiente de escoger. La colección de archivos que puede ser guardada en un directorio común formará la base de datos de materiales de FreeCAD.

A través de este modelo de datos, los materiales pueden ser definidos en FreeCAD sin la necesidad de definir un *componente*.

Un nuevo puntero se creará en el modelo de datos del *componente*, para vincularlo a un material que ha sido definido a través del modelo de datos de materiales.

## Resultado

A través de este modelo de datos de materiales, se propone ofrecer una herramienta para manejar sencillamente datos de materiales con FreeCAD.

## Ideas

## Organización

Diferentes tipos de datos se necesitan manejar para describir un material. Un modelo de datos de materiales se propone más abajo. También se indican algunos ejemplos de los datos que se pueden almacenar con esta estructura.

### Modelo de datos de materiales 

En adición al clásico atributo de \"cadena de texto\" como un nombre, y una familia, 3 diferentes tipos específicos de información se necesita manejar para describir un material en FreeCAD.

-   Propiedades: Estructura genérica para almacenar fatos describiendo las propiedades físicas del material
-   Composición química: Composición química del material
-   Apariencia: Información describiendo como se mostrará el material en FreeCAD (color, brillo\...)

Todos estos tipos de información no es necesario que se definan para que el material exista. Finalmente, abajo se muestra la lista de atributos mantenidos para describir un material en FreeCAD.

#### Nombre

Una cadena de texto indicando el nombre del material. Es su designación.

#### Familia

Una cadena de texto indicando la familia del material, como por ejemplo:

-   metal
-   plástico
-   \...

Adicionalmente, se ha propuesto crear un mapa entre las familias (por ejemplo almacenado en un archivo XML) de modo que permita navegar por la base de datos de materiales de FreeCAD.

Dicho mapa podría por ejemplo contener un árbol presentando relaciones entre familias, como:

-   metal -\> acer -\> acero al carbono laminado -\> Acero avanzado de alta resistencia

-   metal -\> aluminio -\> aluminio fundido

#### Fabricante

Una cadena de texto indicando el fabricante del material.

#### URL

Una cadena de texto indicando la página web presentando el material.

#### Propiedades

##### Descripción

El modelo de datos de materiales incluye una colección de propiedades. El tamaño de dicha colección no es fijo y puede extenderse con propiedades definidas por el usuario.

Una propiedad contiene los siguientes atributos.

-   name: Cadena de texto
-   symbol: Cadena de texto para escribir el símbolo de las propiedades (¿en formato matemático de Latex?)
-   type: \"escalar\" o \"matriz\"
-   value: escalar (si es un escalar)
-   values: matriz (si es una matriz)
-   parameterNames: matriz de cadenas de texto (para propiedades de tipo \"matriz\")
-   parameterValues: matriz de escalares (para propiedades de tipo \"matriz\")
-   unit & unitMagnitude (objeto específico descrito en [Unidades](Units/es.md))(Atención: Los ejemplos incluyen unitMagnitude, aunque no estoy completamente seguro de que deba estar definido en el nivel de las propiedades. El sistema de unidades debe estar definido en el nivel del material)
-   direction: Un vector indicando en que dirección se encuentra para entender el valor de la propiedad. Los vectores son en si mismos objetos de FreeCAD expresados en el sistema de coordenadas global o en un sistema de coordenadas definido por el usuario.
-   notes: Cadenas de texto que se pueden utilizar para describir algo más la propiedad como que significa, como se mide\... También puede ayudar a entender el nombre de las propiedades

Las propiedades de los materiales serán identificadas gracias a su nombre para procesarlas, por ejemplo escribiendo el límite de elasticidad en un modelo de elementos finitos. Para facilitar la creación de datos de materiales con FreeCAD, una lista normalizada de nombres de propiedades con sus unidades por defecto será propuesta al usuario. Aunque el usuario es libre de crear nuevas propiedades, con nuevos nombres, nuevas unidades, etc.

Abajo está propuesto el diccionario de propiedades estándar. Eres libre de añadir otra nuevas.


<?xml version="1.0" encoding="UTF-8"?>



  
        
     








Notes: \"Mean Lankford coefficient is representative of the anisotropy of a thin metal sheet.\" \"The Hardening coefficient is representative of the hardening capacity of a metal. It appears in Hollomon formula that can relates cumulated plastic strain to stress.\"

##### Ejemplo 1: Coste por tonelada 

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

##### Ejemplo 2: Límite de elasticidad 

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

##### Ejemplo 3: Endurecimiento por acritud 

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

\[\[\[0. , 0.4, 0.8, 1\], \[ 0, 0.4, 0.8, 1\], \[ 0, 0.4, 0.8, 1\]\],

\[\[0.\] , \[100\] , \[1000.\] \],

\[\[18.\] \],\]

-   parameterUnits & parameterUnitMagnitudes: \[\[\[ 0, 0, 0, 0, 0, 0, 0\], 1\], \[\[ 0, 0, -1, 0, 0, 0, 0\], 1\], \[\[ 0, 0, 0, 0, 1, 0, 0\], 1\]\]
    -   meaning none, s\^(-1) and, K (more details about unit & unit system specifications in [Units](Units.md) page)
-   unit & unitMagnitude: \[\[ -1, 1, -2, 0, 0, 0, 0\], 1\]
    -   meaning Pa (more details about unit & unit system specifications in [Units](Units.md) page)
-   direction: not applicable

#### Composición química 

\[Yet to be filled up\]

#### Apariencia

\[Yet to be filled up\]

#### Notas

A string where the user can add its own comments about the material.

### Aplicaciones del modelo de datos de materiales: Algunos ejemplos 

##### Ejemplo 1: Mampostería de ladrillos 

###### Nombre 

Brick masonry

###### Familia 

?string?

###### Propiedades 

-   *Weight*: 1kg/m³
-   *Cost per cubic meter*: 1€/m³
-   *Number of bricks por base unit*: ?float?
-   *Volume of mortar por base unit*: ?float?
-   *Mortar type*: ?string?
-   *Brick type*: ?string?
-   *Fire resistance class*: ?string?
-   *Thermal conductivity*: 1 W/mK

###### Fabricante 

?string?

###### URL 

?string?

###### Notas 

Notes about maintainance, special cares to be taken, etc\...

CSI/MasterFormat code (as there are several systems used in the industry which give to all material a special code, I propose to enter it in the notes, because it doesn\'t appear to me relevant create a specific properties that we won\'t be able to name exactly).


<div class="mw-translate-fuzzy">

## Siguientes acciones 

-   Define a set of names for classical properties, that we can define in a dictionary (FreeCAD configuration file). These properties will most notably be re-used in other contexts like the FEM module.

-   Fill up *Chemical composition* section.
-   Fill up *Appearance* section.

-   Define a set of default chemical components.

-   Review by other people.

-   Implement in C++ data model and ability to write/read in a file (ISO 10303-45 through SCL?).
-   Implement XML dictionaries to store default properties, with their units, that can be used by the user.
-   Implement python GUI to handle this data.


</div>



[Category:Roadmap](Category:Roadmap.md)

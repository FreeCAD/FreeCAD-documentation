# Feature editing/es
{{TOCright}}

## Introducción

Esta página explica la forma en que [Ambiente de trabajo Diseño de piezas](PartDesign_Workbench/es.md) está destinado a ser utilizado a partir de FreeCAD 0.17.

Mientras el [Ambiente de Trabajo de Pieza](Part_Workbench/es.md) y otros Ambientes de Trabajo de FreeCAD permiten crear piezas mediante la combinación de formas, el ambiente de trabajo de diseño de piezas se basa en **operaciones**. Una operación modifica la forma de una pieza.

## Metodología de edición de operaciones 

La primera operación es conoce como **operación base**. A medida que se van añadiendo operaciones, cada operación toma la forma resultante de la operación anterior y añade o quita material, creando una dependencia lineal entre cada operación y la siguiente. Desde el punto de vista de las operaciones sustractivas, esta metodología se asemeja al proceso de fabricación. Por ejemplo, a un bloque se le hace un corte a un lado, posteriormente a otro lado, luego se perforan agujeros, a continuación se redondean bordes, etc.

Todas las operaciones aparecen listadas de forma secuencial en el árbol del proyecto y pueden ser editadas en cualquier momento. El resultado de la última operación, aquella que ocupa el lugar inferior en la lista de operaciones, es el que determina la forma de la pieza final.

Las operaciones se clasifican en las siguientes categorías:

-   **Basadas en perfil**: Estas operaciones utilizan un perfil como punto de partida para definir la forma del material que va a ser añadido (operación aditiva) o eliminado (operación sustractiva). El perfil puede ser un croquis, una cara plana de la geometría (en cuyo caso el perfil se extrae de sus aristas), una **forma unida** o un objeto del banco de trabajo Draft que haya sido incluido en el cuerpo activo con anterioridad.

-   **Aditiva**: añade material al resultado de la operación anterior. Los iconos de las operaciones aditivas se caracterizan porque predomina en ellos el amarillo.

-   **Sustractiva**: elimina material del modelo existente. Los iconos de las operaciones sustractivas se caracterizan porque predominan en ellos el rojo y el azul.

-   **Basadas en Primitivas**: son operaciones basadas en primitivas geométricas como por ejemplo el cubo, el cilindro, el cono, el toro. Pueden ser tanto aditivas como sustractivas.

-   **Operaciones de transformación**: aplican transformaciones a una o varias operaciones anteriores (operación reflexión o simetría, patrón de repetición lineal, patrón de repetición polar o una transformada múltiple fruto de la combinación de las anteriores).

-   **Operaciones de alteración**: operaciones que alteran una arista o una cara determinada, como redondeos, chaflanes o cortes inclinados.

-   **Operaciones de procedimiento**: se dice de operaciones que no están basadas en croquis, como las operaciones de transformación y las de alteración.

## Cuerpo

Trabajar en PartDesign requiere primero crear un <img alt="" src=images/PartDesign_Body.png  style="width:24px;"> **[Cuerpo](PartDesign_Body/es.md)**. El Diseño de piezas Cuerpo es un contenedor que agrupa una secuencia de operaciones formando un único sólido continuo.

![](images/PartDesign_Body_tree.png )

¿Qué es un único solido continuo? Es un objeto producido a partir de un único bloque de material. Si el objeto incluye clavos, tornillos, pegamento y soldado, entonces no es un único sólido continuo. Como ejemplo práctico, una silla de madera estaría hecha de múltiples cuerpos, con uno para cada uno de sus subcomponentes (patas, listones, asiento, etc.).

Un documento de FreeCAD puede contener varios cuerpos. Diferentes cuerpos puede combinarse para formar un único sólido continuo.

Solo un cuerpo puede estar activo en un documento. El cuerpo activo obtiene las nuevas operaciones creadas. Un cuerpo puede activarse o desactivarse haciendo doble clic sobre él. Un cuerpo activado se resalta en azul claro. El color de resaltado se puede configurar en las preferencias en Display / Colors / Active container desde la versión 0.18.

Cuando una pieza requiere del empleo de varios cuerpos, estos pueden ser agrupados dentro de un contenedor de propósito general llamado <img alt="" src=images/Std_Part.svg  style="width:24px;"> [contenedor de Pieza](Std_Part/es.md). De esta forma todos los cuerpos se pueden trasladar de forma solidaria como si fueran un único objeto.

### Gestión de visibilidad de un cuerpo 

Un cuerpo queda representado por el resultado de la última operación en él contenida. Por defecto dicha operación es conoce como Punta. Un analogía es *la punta del iceberg*: sólo la punta es visible sobre el agua, mientras que la mayoría del iceberg permanece oculto bajo el agua. Cuando se añade una nueva operación a un cuerpo, la visibilidad de las anteriores operaciones queda deshabilitada, y la nueva operación se convierte en la punta del cuerpo.

Sólo puede haber una característica visible a la vez. Es posible [cambiar la visibilidad](Std_ToggleVisibility/es.md) de cualquier característica en el cuerpo, seleccionándola en el árbol del Modelo y presionando la **Barra espaciadora**, en efecto retrocediendo en la historia del cuerpo.

### Origen del cuerpo 

El cuerpo tiene un origen que consiste en planos de referencia (XY, XZ, YZ) y ejes (X, Y, Z). Dichos planos y ejes puede ser utilizados en los croquis y operaciones del mismo. Los croquis pueden ser fijados a uno de los planos del origen.

### Moviendo y reordenando operaciones 

Es posible cambiar la Punta a una operación anterior dentro del cuerpo a fin de insertar nuevas operaciones u objetos (como croquis o geometría de referencia). También es posible reordenar operaciones dentro de un cuerpo, o mover operaciones de un cuerpo a otro. Dichas operaciones son accesibles mediante el menú contextual que se despliega seleccionando un objeto u operación dentro del body y haciendo click con el botón derecho del ratón. Sin embargo cabe destacar que el programa puede evitar dicha operación si el objeto contiene dependencias en el cuerpo origen, como por ejemplo si está fijada a una cara del mismo. En el caso específico de un croquis es condición indispensable que el mismo no contenta enlaces a geometría externa.

### Diferencia con otros sistemas de CAD 

Una diferencia fundamental entre FreeCAD y otros programas, como Catia, es que FreeCAD no permite tener muchos sólidos desconectados en el mismo <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> **[Diseño de piezas cuerpo](PartDesign_Body/es.md)**. Es decir, una nueva característica siempre debe ser construida sobre la anterior. O dicho de otra manera, la nueva característica debería \"tocar\" la característica anterior, de modo que ambas características se fusionen y se conviertan en un único sólido. No puedes tener sólidos \"flotantes\".

<img alt="" src=images/PartDesign_Body_non-contiguous.png  style="width:550px;">


<div class="mw-translate-fuzzy">



*Diferencia entre Catia y FreeCAD. Izquierda: Catia permite cuerpos desconectados de las características anteriores del cuerpo. Derecha: en FreeCAD esto causa un error; la característica más nueva siempre debe contactar o intersecarse con la característica anterior para que se fusione con ella, y se convierta en un único sólido contiguo.*


</div>

## Geometría de referencia 

La geometría de referencia consiste en planos personalizados, lineas, puntos o formas externas enlazadas. Pueden ser creados para ser usados como referencia por bocetos y características. Hay una multitud de posibilidades de adjuntar objetos de referencia.

In some CAD systems you can define a datum plane that is offset from the previous body and you can create a disconnected solid. So, placing a lot of datum planes, and building objects on them is okay and won\'t cause an error. Typically, you would eventually adjust the planes to their final positions, so that the individual objects are fused together.

In FreeCAD, as mentioned in the previous section, disconnected solids are **NOT** allowed, so a sketch on a datum plane that would create a non-contiguous solid will fail.

In FreeCAD, datum planes make sense if you are placing sketches (and padding, pocketing, etc.) in non-standard orientations, that is, in planes offset or rotated around the three main axes. Since sketches can also be placed in non-standard orientations in the same way as datum planes, often there is no need to use datum planes.

Datum planes also make sense if there will be more than one sketch in the same non-standard orientation. In this case a datum plane can be used and the orientation only needs to be adjusted for the datum plane to adjust all associated sketches and the features created from the sketches.

Both sketches and datum planes should be attached to base planes. Referencing generated geometry (geometry that is the result of a feature creating operation, for example a pad or pocket) should be avoided since faces and edges get renamed and renumbered and the references no longer refer to the same thing. This is called topological instability and is due the way FreeCAD uses some external geometric libraries. Hopefully this will be improved in the future. (See Advice for creating stable models below).

Even if not used for supporting sketches, datum objects are still helpful as visual indicators, to draw attention to important features or distances in the modelling process. (Though, simply adding geometry to a sketch also provides similar visual feedback.)

<img alt="" src=images/PartDesign_Body_non-contiguous_slanted.png  style="width:550px;">



*Difference between Catia and FreeCAD. Left: Catia allows disconnected bodies from the previous features of the body. In FreeCAD this causes an error; Right: the newer feature should always contact or intersect the previous feature, so that it is fused to it, and becomes a single contiguous solid. In this example, the new solid is based on a datum plane that is rotated around the Y axis.*

## Referencia cruzada 


<div class="mw-translate-fuzzy">

Es posible realizar referencias cruzadas entre cuerpos mediante la utilización de geometría de referencia. Por ejemplo la forma unida de referencia permite copiar caras de un cuerpo como geometría de referencia en otro cuerpo. Esto permite construir una caja con una tapa ajustada de forma fácil utilizando un cuerpo para la caja y otro para la tapa. FreeCAD evita la creación de enlaces entre cuerpos no intencionados preguntado al usuario siempre que esto vaya a producirse.


</div>

## Fijación

La fijación de objetos no es una herramienta específica del banco de trabajo de diseño de pieza. Dicha funcionalidad pertenece al banco de trabajo de pieza y puede encontrarse en el menú Pieza. Sin embargo es una herramienta que se utiliza principalmente en el banco de trabajo de diseño de pieza para fijar croquis y geometría de referencia a planos y ejes de referencia del cuerpo. Hay multitud de formas de fijación. La posibilidad de utilizar una desviación u offset incrementa substancialmente la versatilidad de las distintas posibilidades de fijación.


<div class="mw-translate-fuzzy">

Para más información, ver la página de [Fijación](Part_EditAttachment/es.md).


</div>

## Consejos para la creación de modelos estables 


<div class="mw-translate-fuzzy">

La idea de modelado paramétrico implica que el cambio de valores de ciertos parámetros provocan que el modelo cambie adaptándose a los nuevos valores. Sin embargo, cuando se hacen cambios severos, el modelo puede romperse debido al [problema de denominación topológica](topological_naming_problem/es.md) que aún no está resuelto en FreeCAD. La rotura puede minimizarse si se respetan los siguientes principios de diseño:


</div>


<div class="mw-translate-fuzzy">

-   Evitar fijar croquis sobre caras en la medida de lo posible. Es preferible fijar los croquis sobre los planos del origen del cuerpo o sobre planos de geometría de referencia.
-   Al crear geometría de referencia, no fijarla a la topología, sino a planos/ejes del origen del cuerpo o a croquis.
-   Utilizar un \"croquis maestro\". Dicho croquis es un croquis preferiblemente no demasiado complejo que contenga los elementos geométricos básicos del modelo a crear. Dichos elementos pueden utilizarse al modelar el resto de las operaciones. Dicho \"croquis maestro\" es generalmente el primero en el cuerpo, aunque no es un requerimiento que lo sea.
-   Ante la necesidad insuperable de tener que referenciar una operación intermedia, como por ejemplo una operación de vaciado de espesor, conviene referenciar la operación más antigua en la que el elemento a referenciar esté presente. Cabe destacar que a partir de esta versión ya no es necesario referenciar la operación anterior. Al utilizar la operación más antigua cualquier cambio en operaciones intermedias no dará lugar a un modelo inválido. Similarmente es preferible referenciar un croquis que aristas o vértices de un sólido.


</div>

## Flujo de trabajo de construcción del cuerpo 

There are several workflows that are possible with the [PartDesign Workbench](PartDesign_Workbench.md). What should always be noticed is that all the features created inside a [PartDesign Body](PartDesign_Body.md) will be fused together to obtain the final object.

### Diferentes dibujos 

Sketches need to be supported by a plane. This plane can be one of the main planes (XY, XZ, or YZ) defined by the Origin of the Body. A sketch is either extruded into a positive solid (additive), with a tool like <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Pad](PartDesign_Pad.md), or into a negative solid (subtractive), with a tool like <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [PartDesign Pocket](PartDesign_Pocket.md). The first adds volume to the final shape of the body, while the latter cuts volume from the final shape. Any number of sketches and partial solids can be created in this way; the final shape (tip) is the result of fusing these operations together. Naturally, the Body can\'t consist of only subtractive operations, as the final shape should be a solid with a positive, non-zero volume.

<img alt="" src=images/PartDesign_workflow_1.svg  style="width:600px;">

### Características secuenciales 

Sketches can be supported by the faces of previous solid operations. This may be necessary if you need to access a face that is only available after a certain feature has been created. However, this workflow isn\'t recommended since, if the original feature is modified, the following features in the sequence may break. This is the [topological naming problem](Topological_naming_problem.md).

<img alt="" src=images/PartDesign_workflow_2.svg  style="width:600px;">

### Uso de los planos de datos para el apoyo 

Datum planes are useful to support the sketches. These auxiliary planes should be attached to the base planes of the body.

*Note: In many cases, a sketch attached to a base plane with attachment offsets can accomplish the same function. Datums are particularly useful when multiple sketches or other constructs will use the datum. This means all changes to the datum will be apply to attached sketches, etc. Adding a single sketch to a datum, rather than using attachment offsets in the sketch properties, is an extra step and is essentially redundant.*

As with sketches, it is possible to attach Datum planes to generated geometry (edges, faces of previously created solids), ***but this is not recommended*** since it can cause the topological naming problem.

In addition, a <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:24px;"> [PartDesign ShapeBinder](PartDesign_ShapeBinder.md) can be used to import external geometry into the body to serve as reference; then sketches can be attached to this auxiliary body, either using datum planes or not.

*Again, the ShapeBinder should be based on Sketches from the previous body, not generated geometry.*

Using datum objects is often the best way to produce stable models, when used with base planes and attachment offsets, although it requires a bit more work from the user. For details about basic attachment see: [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md) *Note: while this tutorial talks about sketches, datum attachment is done in similar fashion.*

## Tutoriales

The [tutorials](Tutorials.md) page provides some examples of using the [feature editing](Feature_editing.md) method of the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md).

-   [Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md)
-   [Basic Part Design Tutorial](Basic_Part_Design_Tutorial.md)
-   [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md)

## Related

-   [Constructive solid geometry](Constructive_solid_geometry.md)

<img alt="" src=images/PartDesign_workflow_3.svg  style="width:600px;">


{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [PartDesign](Category_PartDesign.md) > Feature editing/es

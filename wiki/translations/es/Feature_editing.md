# Feature editing/es
## Introducción


<div class="mw-translate-fuzzy">

Esta página explica la forma en que [Ambiente de trabajo Diseño de piezas](PartDesign_Workbench/es.md) está destinado a ser utilizado a partir de FreeCAD 0.17.


</div>



## Cuerpo


<div class="mw-translate-fuzzy">

Trabajar en PartDesign requiere primero crear un <img alt="" src=images/PartDesign_Body.png  style="width:24px;"> **[Cuerpo](PartDesign_Body/es.md)**. El Diseño de piezas Cuerpo es un contenedor que agrupa una secuencia de operaciones formando un único sólido continuo.


</div>

<img alt="" src=images/PartDesign_Feature_example.png  style="width:400px;">



*Feature editing in practice. From left to right:<br>
Body with a [box](PartDesign_AdditiveBox.md) feature.<br>
Body with a box and a [chamfer](PartDesign_Chamfer.md) feature.<br>
Body with a box, a chamfer and a [pocket](PartDesign_Pocket.md) feature.*


<div class="mw-translate-fuzzy">

Solo un cuerpo puede estar activo en un documento. El cuerpo activo obtiene las nuevas operaciones creadas. Un cuerpo puede activarse o desactivarse haciendo doble clic sobre él. Un cuerpo activado se resalta en azul claro. El color de resaltado se puede configurar en las preferencias en Display / Colors / Active container desde la versión 0.18.


</div>

![](images/PartDesign_Body_tree.png )

### What is a contiguous solid? 


<div class="mw-translate-fuzzy">

¿Qué es un único solido continuo? Es un objeto producido a partir de un único bloque de material. Si el objeto incluye clavos, tornillos, pegamento y soldado, entonces no es un único sólido continuo. Como ejemplo práctico, una silla de madera estaría hecha de múltiples cuerpos, con uno para cada uno de sus subcomponentes (patas, listones, asiento, etc.).


</div>

In FreeCAD version 1.0 an experimental property was introduced that allows the Body to have non-contiguous solids. This can also be set in the [Preferences](PartDesign_Preferences#General.md) as default for newly created Bodies. This is not intended to be used to build, as in the example, a chair in one Body. It is meant to allow features that may produce disconnected solids that will be made contiguous by later features.


<div class="mw-translate-fuzzy">

Cuando una pieza requiere del empleo de varios cuerpos, estos pueden ser agrupados dentro de un contenedor de propósito general llamado <img alt="" src=images/Std_Part.svg  style="width:24px;"> [contenedor de Pieza](Std_Part/es.md). De esta forma todos los cuerpos se pueden trasladar de forma solidaria como si fueran un único objeto.


</div>



### Gestión de visibilidad de un cuerpo 


<div class="mw-translate-fuzzy">

Un cuerpo queda representado por el resultado de la última operación en él contenida. Por defecto dicha operación es conoce como Punta. Un analogía es *la punta del iceberg*: sólo la punta es visible sobre el agua, mientras que la mayoría del iceberg permanece oculto bajo el agua. Cuando se añade una nueva operación a un cuerpo, la visibilidad de las anteriores operaciones queda deshabilitada, y la nueva operación se convierte en la punta del cuerpo.


</div>


<div class="mw-translate-fuzzy">

Sólo puede haber una característica visible a la vez. Es posible [cambiar la visibilidad](Std_ToggleVisibility/es.md) de cualquier característica en el cuerpo, seleccionándola en el árbol del Modelo y presionando la **Barra espaciadora**, en efecto retrocediendo en la historia del cuerpo.


</div>



### Moviendo y reordenando operaciones 


<div class="mw-translate-fuzzy">

Es posible cambiar la Punta a una operación anterior dentro del cuerpo a fin de insertar nuevas operaciones u objetos (como croquis o geometría de referencia). También es posible reordenar operaciones dentro de un cuerpo, o mover operaciones de un cuerpo a otro. Dichas operaciones son accesibles mediante el menú contextual que se despliega seleccionando un objeto u operación dentro del body y haciendo click con el botón derecho del ratón. Sin embargo cabe destacar que el programa puede evitar dicha operación si el objeto contiene dependencias en el cuerpo origen, como por ejemplo si está fijada a una cara del mismo. En el caso específico de un croquis es condición indispensable que el mismo no contenta enlaces a geometría externa.


</div>

<img alt="" src=images/PartDesign_workflow.svg  style="width:400px;">



*Schematic representation of the PartDesign workflow.*



## Geometría de referencia 


<div class="mw-translate-fuzzy">

La geometría de referencia consiste en planos personalizados, lineas, puntos o formas externas enlazadas. Pueden ser creados para ser usados como referencia por bocetos y características. Hay una multitud de posibilidades de adjuntar objetos de referencia.


</div>

In FreeCAD, datum planes make sense if you are placing sketches in non-standard orientations, that is, on planes offset or rotated around the three main axes. But since sketches can also be placed in non-standard orientations and have the same attachment options as datum planes, there is often no need to use them. Datum planes make the most sense if there is more than one sketch with the same non-standard orientation. Adjusting the orientation of the datum plane will then adjust all associated sketches and the features created from those sketches.

Although FreeCAD version 1.0 already has code to mitigate the [topological naming problem](Topological_naming_problem.md), it is still best practice to attach both sketches and datum planes to the base planes of the Body\'s Origin whenever possible. Referencing generated geometry (geometry that is the result of a feature operation, for example a pad or pocket) may yet result in less stable models. See [Advice for creating stable models](#Advice_for_creating_stable_models.md) below.



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



## Tutoriales

The [tutorials](Tutorials.md) page provides some examples of using the feature editing method of the [PartDesign Workbench](PartDesign_Workbench.md).

-   [Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md)
-   [Basic Part Design Tutorial 019](Basic_Part_Design_Tutorial_019.md)
-   [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md)

## Related

-   [Constructive solid geometry](Constructive_solid_geometry.md)


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > [PartDesign](Category_PartDesign.md) > Feature editing/es

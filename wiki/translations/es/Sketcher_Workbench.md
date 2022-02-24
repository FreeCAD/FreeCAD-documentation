# <img alt="El icono del Ambiente de trabajo Croquizador" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/es


{{TOCright}}

## Introducción

El FreeCAD <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Ambiente de trabajo Croquizador](Sketcher_Workbench/es.md) se utiliza para crear geometrías 2D destinadas a ser utilizadas en el <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Ambiente de trabajo DiseñoPieza](PartDesign_Workbench/es.md), <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> y otros Ambiente de trabajo. Generalmente, un dibujo 2D se considera el punto de partida para la mayoría de los modelos CAD, ya que un boceto 2D puede ser \"extruido\" para crear una forma 3D; otros bocetos 2D pueden ser utilizados para crear otras características como bolsas, crestas o extrusiones sobre las formas 3D previamente construidas. Junto con las operaciones booleanas definidas en el <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Ambiente de trabajo piezas](Part_Workbench/es.md), el Croquis forma la base de la [geometría sólida constructiva](constructive_solid_geometry/es.md) (CSG) método de construcción de sólidos. Además, junto con el <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Ambiente de trabajo DiseñoPieza](PartDesign_Workbench/es.md) operaciones, el Sketcher también forma la base de la [edición de características](feature_editing/es.md) metodología de la creación de sólidos.

El ambiente de trabajo Croquizador presenta \"restricciones\", que permiten que las formas 2D sigan definiciones geométricas precisas en términos de longitud, ángulos y relaciones (horizontalidad, verticalidad, perpendicularidad, etc.). Un solucionador de restricciones calcula el alcance de las restricciones de la geometría 2D y permite la exploración interactiva de los grados de libertad del croquis.

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*Un croquis completamente restringido‎*

## Basics of constraint sketching 


<div class="mw-translate-fuzzy">

## Bases de croquizado con restricciones 

Para explicar como funciona el Croquizador, puede ser útil compararlo con el sistema de dibujo \"tradicional\".


</div>

#### Traditional Drafting 


<div class="mw-translate-fuzzy">

#### Dibujo tradicional 

El modo de dibujo tradicional es inherente a las antiguos [mesas de dibujo](http://es.wikipedia.org/wiki/Mesa_de_dibujo). [Las vistas (2D) ortogonales](http://es.wikipedia.org/wiki/Sistema_di%C3%A9drico) eran dibujadas manualmente y previstas para producir dibujos técnicos (también conocidos como planos detallados). Los objectos se dibujaban precisamente al tamaño o dimensión pretendida. Si querías dibujar una línea horizontal de longitud 100mm que comience en el (0,0), activabas la herramienta línea, pulsabas en la pantalla o introducías las coordenadas (0,0) para el primer punto, luego hacías un segundo clic o introducías las coordenadas del segundo punto en (100,0). O dibujabas la línea sin preocuparse de su posición, y la movías después. Cuando terminabas de dibujar geometría, le añadías cotas.


</div>

#### Constraint Sketching 


<div class="mw-translate-fuzzy">

#### Croquizar con restricciones 

El **módulo de croquizado** se aleja de esta lógica. Los objetos no tienen porque dibujarse exactamente como se pretenden, porque serán definidos después por restricciones geométricas y dimensionales. Los objetos se pueden dibujar sin excesivo rigor, y mientras estén sin restringir se pueden modificar. Están en realidad \"flotando\" y se pueden mover, estirar, girar, escalar, etc. Esto ofrece una gran flexibilidad en el proceso de diseño.


</div>

#### What are constraints? 


<div class="mw-translate-fuzzy">

#### ¿Qué son las restricciones? 

Las restricciones se utilizan para limitar los grados de libertad de un objeto. Por ejemplo, una línea tiene 4 [grados de libertad](#Degrees_Of_Freedom.md) (en inglés Degrees Of Freedom, generalmente abreviado como \" DOF \"): Se puede mover horizontal o verticalmente, se puede estirar, y puede girarse.


</div>

Aplicando una restricción horizontal o vertical, o una restricción angular (relativa a otra línea o a uno de los ejes), se limitará su capacidad de girar, aunque seguirá con 3 grados de libertad. Bloqueando uno de sus extremos en relación con el origen eliminará otros 2 grados de libertad. Y aplicando una restricción dimensional se eliminará el último grado de libertad. La línea se considerará que está entonces **completamente restringida**.

Múltiples objetos pueden ser restringidos con respecto a otro. Dos líneas se pueden unir por uno de sus puntos con la restricción de coincidencia de puntos. Un ángulo se puede definir entre ellas, o se pueden establecer como perpendiculares. Una línea puede ser tangente a un arco o a una circunferencia, etc. Un Croquis complejo puede tener diferentes soluciones y **restringir completamente** significa encontrar una de esas posibles soluciones mediante el uso de restricciones.


<div class="mw-translate-fuzzy">

Existen dos tipos de restricciones: geométricas y dimensionales. Ambas son explicadas en la sección [\#Las herramientas](#Las_herramientas.md) más abajo.


</div>

#### What the Sketcher is not good for 


<div class="mw-translate-fuzzy">

#### ¿Para qué no es bueno el entorno de croquizado? 

El Croquizador no está pensado para producir planos detallados en 2D. Una vez que los croquis se utilizan para generar un sólido, son automáticamente ocultados. Las cotas son sólo visibles en el modo de edición del croquis.


</div>


<div class="mw-translate-fuzzy">

Si sólo necesitas producir vistas 2D para imprimir, y no quieres crear modelos 3D, mira el [Ambiente de Trabajo Croquiz](Draft_Workbench/es.md). A diferencia de los elementos de Croquiz, los objetos de Borrador no usan restricciones; son formas simples definidas en el momento de la creación. Tanto el Borrador como el Croquiz pueden utilizarse para el dibujo de geometría 2D, y la creación de sólidos 3D, aunque su uso preferido es diferente; el Croquiz se utiliza normalmente junto con [Pieza](Part_Workbench/es.md) y [DiseñoPiezas](PartDesign_Workbench/es.md) para crear sólidos; el Borrador se utiliza normalmente para dibujos planos simples sobre una cuadrícula, como cuando se dibuja un plano de arquitectura; en estas situaciones el Draft se utiliza principalmente junto con el [Ambiente de Trabajo Arquitectura](Arch_Workbench/es.md). La herramienta [BorradorACroquiz](Draft_Draft2Sketch/es.md) convierte un objeto Borrador en un objeto Croquiz, y viceversa; muchas herramientas que requieren un elemento 2D como entrada trabajan con cualquier tipo de objeto ya que una conversión interna se realiza automáticamente


</div>

## Flujo de trabajo del Croquizado 

Un croquis es siempre bidimensional (2D). Para crear un sólido, se crea un croquis con un perfil cerrado y posteriormente se extruye o se realiza una operación de revolución. De esta forma se añade la tercera dimensión y se crea un sólido tridimensional.

Si un Bosquejo tiene segmentos que se cruzan entre sí, lugares donde un Punto no está directamente en un segmento, o lugares donde hay huecos entre los puntos finales de segmentos adyacentes, Pad o Revolución no creará un sólido. A veces un Boceto que contiene líneas que se cruzan entre sí funcionará para una operación simple como Pad, pero operaciones posteriores como Patrón Lineal fallarán. Es mejor evitar cruzar las líneas. La excepción a esta regla es que no se aplica a la Geometría de Construcción (azul).

Dentro de un perfil cerrado puede haber contenidos otros perfiles interiores que no se solapen, ni con el anterior, ni entre ellos. Al aplicar la operación tridimensional estos perfiles interiores constituirán huecos en la forma tridimensional.


<div class="mw-translate-fuzzy">

Una vez que un Bosquejo está totalmente restringido, las características del Bosquejo se volverán verdes; la Geometría de Construcción permanecerá azul. Por lo general está \"terminado\" en este punto y es adecuado para su uso en la creación de un sólido 3D. Sin embargo, una vez que se cierra el cuadro de diálogo de Boceto puede valer la pena ir a <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Ambiente de trabajo Pieza](Part_Workbench/es.md) y ejecutando **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Comprobar la geometría](Part_CheckGeometry/es.md)** para asegurarse de que no hay características en el Boceto que puedan causar problemas posteriores.


</div>

## Tools


<div class="mw-translate-fuzzy">

## Las herramientas 

Todas las herramientas del Ambiente de Trabajo Croquiz se encuentran en el menú Boceto que aparece al cargar el Ambiente de Trabajo Croquiz.


</div>

### General

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Nuevo croquis](Sketcher_NewSketch/es.md): Crea un nuevo croquis en la cara o plano seleccionado. Si no se selecciona ninguna cara mientras se ejecuta esta herramienta, se le pide al usuario que seleccione un avión en una ventana emergente.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Editar croquis](Sketcher_EditSketch/es.md): Edita el croquis seleccionado. Esto abrirá el [Diálogo de Croquis](Sketcher_Dialog/es.md).

-   <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:32px;"> [Abandonar el croquis](Sketcher_LeaveSketch/es.md): Abandona el modo de edición del croquis.

-   <img alt="" src=images/Sketcher_ViewSketch.svg‎  style="width:32px;"> [Vista de croquis](Sketcher_ViewSketch/es.md): Establece la vista del modelo perpendicular al plano del croquis.

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [Ver sección](Sketcher_ViewSection/es.md): Crea un plano de sección que oculta temporalmente cualquier materia delante del plano de dibujo.

-   <img alt="" src=images/Sketcher_MapSketch.svg‎  style="width:32px;"> [Fijar croquis a cara](Sketcher_MapSketch/es.md): Traza un boceto de la cara previamente seleccionada de un sólido.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;">[Reorientar croquis](Sketcher_ReorientSketch/es.md): Permite adjuntar el boceto a uno de los planos principales.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;">[Validar el boceto](Sketcher_ValidateSketch/es.md): Verificar la tolerancia de los diferentes puntos y ajustarlos.

-   <img alt="" src=images/Sketcher_MergeSketch.svg‎  style="width:32px;"> [Fusionar croquis](Sketcher_MergeSketches/es.md): Fusiona dos o más croquis

-   <img alt="" src=images/Sketcher_MirrorSketch.svg‎  style="width:32px;"> [Reflejar croquis](Sketcher_MirrorSketch/es.md):

Reflejar un boceto a lo largo del eje X, el eje Y o el origen.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Detener la operación](Sketcher_StopOperation/es.md): cuando esté en el modo de edición, detenga la operación actual, ya sea el dibujo, la configuración de restricciones, etc.


</div>

### Geometrías de croquis 

Estas son las herramientas para la creación de objetos.

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> [Punto](Sketcher_CreatePoint/es.md): Dibuja un punto.

-   <img alt="" src=images/Sketcher_Line.svg  style="width:32px;"> [Línea](Sketcher_CreateLine/es.md): Dibuja un segmento de línea entre 2 puntos. Las líneas son infinitas en lo que respecta a ciertas restricciones.

-   <img alt="" src=images/Sketcher_CompCreateArc.png  style="width:48px;"> [Crear un arco](Sketcher_CompCreateArc/es.md): Este es un menú de iconos en la barra de herramientas de Sketcher que contiene los siguientes comandos:

:\* <img alt="" src=images/Sketcher_Arc.svg  style="width:32px;"> [Arco](Sketcher_CreateArc/es.md): Dibuja un segmento de arco dada por el centro, radio, ángulo inicial y ángulo final.

:\* <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [Arco a través de 3 Puntos](Sketcher_Create3PointArc/es.md): Dibuja un segmento de arco entre dos puntos y un tercer punto que se haya en la circumferencia.

-   <img alt="" src=images/Sketcher_CompCreateCircle.png  style="width:48px;"> [Crear un círculo](Sketcher_CompCreateCircle/es.md): Este es un menú de iconos en la barra de herramientas de Boceto que contiene los siguientes comandos:

:\* <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> [Círculo](Sketcher_CreateCircle/es.md): Dibuja un círculo desde el centro y el radio.

:\* <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [Círculo de 3 puntos](Sketcher_Create3PointCircle/es.md): Dibuja un círculo de tres puntos en la circunferencia.

-   <img alt="" src=images/Sketcher_CompCreateConic.png  style="width:32px;"> [Crear una cónica](Sketcher_CompCreateConic/es.md): El dibujante proporciona las siguientes secciones cónicas.

A diferencia de las líneas B, pueden utilizarse con todo tipo de restricciones como [Tangente](Sketcher_ConstrainTangent/es.md), [Punto en el objeto](Sketcher_ConstrainPointOnObject/es.md), o [Perpendicular](Sketcher_ConstrainPerpendicular/es.md).

-   -   <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Elipse definida por su centro](Sketcher_CreateEllipseByCenter/es.md) : Dibuja una elipse dado su punto central, un segundo punto definiendo el extremo del radio mayor y un tercer punto definiendo el extremo del radio menor.
    -   <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Elipse a través de 3 puntos](Sketcher_CreateEllipseBy3Points/es.md) : Dibuja una elipse definiendo los dos extremos de su radio mayor y un punto definiendo su radio menor.
    -   <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Arco elíptico](Sketcher_CreateArcOfEllipse/es.md) : Dibuja un arco elíptico definido por punto central, un punto definiendo el extremo del radio mayor y dos puntos definiendo los extremos del arco elíptico.
    -   <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Arco hiperbólico](Sketcher_CreateArcOfHyperbola/es.md): Dibuja un arco hiperbólico.
    -   <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Arco parabólico](Sketcher_CreateArcOfParabola/es.md): Dibuja un arco parabólico.

-   <img alt="" src=images/Sketcher_CompCreateBSpline.png  style="width:48px;"> [Crear una B-spline](Sketcher_CompCreateBSpline/es.md): Es un menú de iconos en la barra de herramientas de Sketcher que contiene los siguientes comandos:
    -   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [Crear B-spline](Sketcher_CreateBSpline/es.md): Dibuja una curva B-spline por sus puntos de control.
    -   <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [Crear B-spline periódica](Sketcher_CreatePeriodicBSpline/es.md): Dibuja una curva B-spline periódica (cerrada) por sus puntos de control.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Polilínea (línea de múltiples puntos)](Sketcher_CreatePolyline/es.md): Dibuja una línea creada por múltiples segmentos de línea. Presionando la tecla M se puede iterar entre los diferents modos.


</div>

-   <img alt="" src=images/Sketcher_CompCreateRectangles.png  style="width:48px;"> [Crear rectángulos](Sketcher_CompCreateRectangles/es.md): Es un menú de iconos en la barra de herramientas de Croquizador que contiene los siguientes comandos: {{Version/es|0.20}}

:\* <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Rectángulo](Sketcher_CreateRectangle/es.md): Dibuja un rectángulo dado por 2 puntos opuestos

:\* <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Rectángulo Centrado](Sketcher_CreateRectangle_Center/es.md): Dibuja un rectángulo a partir de un punto central y un punto de borde. {{Version/es|0.20}}

:\* <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Rectángulo Redondeado](Sketcher_CreateOblong/es.md): Dibuja un rectángulo redondeado desde 2 puntos opuestos. {{Version/es|0.20}}

-   <img alt="" src=images/Sketcher_CompCreateRegularPolygon.png  style="width:48px;"> [Crear polígono regular](Sketcher_CompCreateRegularPolygon/es.md): Es un menú de iconos en la barra de herramientas de Sketcher que contiene los siguientes comandos:

-   <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Triángulo](Sketcher_CreateTriangle/es.md): Dibuja un triángulo regular inscrito en un círculo de geometría de construcción.

-   <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Cuadrado](Sketcher_CreateSquare/es.md): Dibuja un cuadrado regular inscrito en una circumferencia en modo construcción.

-   <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width:32px;"> [Pentagon](Sketcher_CreatePentagon/es.md): Dibuja un pentágono regular inscrito en una circumferencia en modo construcción.

-   <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Hexagon](Sketcher_CreateHexagon/es.md): Dibuja un hexágono regular inscrito en un círculo de geometría de construcción.

-   <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width:32px;"> [Heptagon](Sketcher_CreateHeptagon/es.md): Dibuja un heptágono regular inscrito en un círculo de geometría de construcción.

-   <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> [Octagon](Sketcher_CreateOctagon/es.md): Dibuja un octágono regular inscrito en un círculo de geometría de construcción.

:\* <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Crear polígono regular](Sketcher_CreateRegularPolygon/es.md) : Dibuja un polígono regular seleccionando el número de lados y eligiendo dos puntos: el centro y una esquina.

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Ranura](Sketcher_CreateSlot/es.md): Dibuja un óvalo seleccionando el centro de un semicírculo y un punto final del otro semicírculo.

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Redondeo](Sketcher_CreateFillet/es.md): Hace un redondeo entre dos líneas unidas en un punto. Selecciona ambas líneas o haz clic en el punto de la esquina, y luego activa la herramienta.

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:32px;"> [Recortar](Sketcher_Trimming/es.md): Recorta una línea, círculo o arco con respecto al punto designado.

-   <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Extender](Sketcher_Extend/es.md): Extiende una línea o un arco a una línea límite, arco, elipse, arco de elipse o un punto en el espacio.

-   <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Dividir](Sketcher_Split/es.md): Divide una línea o un arco en dos, convierte un círculo en un arco manteniendo la mayoría de las restricciones. {{Version/es|0.20}}

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [Geometría externa](Sketcher_External/es.md): Crea una arista enlazada a geometría externa.

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [CarbonoCopia](Sketcher_CarbonCopy/es.md): Copia la geometría de otro boceto.

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Modo de construcción](Sketcher_ToggleConstruction/es.md): Cambia la geometría del boceto del modo de construcción. La geometría de la construcción se muestra en azul y se descarta fuera del modo de edición del boceto.

### Restricciones de croquis 

Las restricciones son utilizadas para establecer reglas entre los elementos del croquis, y para bloquear el croquis a lo largo de los ejes verticales y horizontales. Algunas restricciones crean restricciones auxiliares adicionales [Restricciones auxiliares](Sketcher_helper_constraint/es.md)

#### Geometric constraints 


<div class="mw-translate-fuzzy">

#### Restricciones geométricas 

Estas restricciones no están asociadas con datos numéricos.


</div>

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [Coincidente](Sketcher_ConstrainCoincident/es.md): Pone un punto en (coincidente con) uno o más puntos.

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [Punto sobre objeto](Sketcher_ConstrainPointOnObject/es.md): Pone un punto sobre otro objeto como una línea, un arco o un eje.

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;">[Vertical](Sketcher_ConstrainVertical/es.md): Limita las líneas o elementos de polilínea seleccionados a una verdadera orientación vertical. Se puede seleccionar más de un objeto antes de aplicar esta restricción.

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [Horizontal](Sketcher_ConstrainHorizontal/es.md): Limita las líneas o elementos de polilínea seleccionados a una verdadera orientación horizontal. Se puede seleccionar más de un objeto antes de aplicar esta restricción.

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;">[Paralelo](Sketcher_ConstrainParallel/es.md): Restringir dos o más líneas paralelas entre sí.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [Perpendicular](Sketcher_ConstrainPerpendicular/es.md): Restringe dos líneas perpendiculares entre sí, o restringe una línea perpendicular a un punto final de un arco.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [Tangente](Sketcher_ConstrainTangent/es.md): Crea una restricción tangente entre dos entidades seleccionadas, o una restricción co-lineal entre dos segmentos de línea. Un segmento de línea no tiene que estar situado directamente en un arco o círculo para ser restringido tangencialmente a ese arco o círculo.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [Iguales](Sketcher_ConstrainEqual/es.md): Limita a dos entidades seleccionadas iguales entre sí. Si se usan en círculos o arcos, sus radios serán iguales.

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [Simétrico](Sketcher_ConstrainSymmetric/es.md): Restringe dos puntos simétricamente sobre una línea, o restringe los dos primeros puntos seleccionados simétricamente sobre un tercer punto seleccionado.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Bloqueo](Sketcher_ConstrainBlock/es.md): bloquea el movimiento de un borde, es decir, impide que sus vértices cambien su posición actual. Debería ser particularmente útil para fijar la posición de las Líneas B. Ver el [Tema de foro Bloqueo de restricción](https://forum.freecadweb.org/viewtopic.php?f=9&t=26572).

#### Dimensional constraints 


<div class="mw-translate-fuzzy">

#### Restricciones dimensionales 

Se trata de restricciones asociadas a los datos numéricos, para los cuales se pueden utilizar las [expresiones](Expressions/es.md). Los datos pueden ser tomados de una [hoja de cálculo](Spreadsheet_Workbench/es.md).


</div>

-   <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Bloquear](Sketcher_ConstrainLock/es.md): Restringe el artículo seleccionado estableciendo distancias verticales y horizontales relativas al origen, bloqueando así la ubicación de ese artículo. Estas distancias de restricción pueden ser editadas más tarde.

-   <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Distancia Horizontal](Sketcher_ConstrainDistanceX/es.md): Fija la distancia horizontal entre dos puntos o puntos finales de líneas. Si solo se selecciona uno, la distancia se define respecto al origen.

-   <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;">[Distancia Vertical](Sketcher_ConstrainDistanceY/es.md): Fija la distancia vertical entre dos puntos o puntos finales de líneas. Si solo se selecciona uno, la distancia se define respecto al origen.

-   <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [Distancia](Sketcher_ConstrainDistance/es.md): Define la distancia de una línea seleccionada limitando su longitud, o define la distancia entre dos puntos limitando la distancia entre ellos.

-   <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Radio](Sketcher_ConstrainRadius/es.md): Define el radio de un arco o círculo seleccionado restringiendo el radio.
-   <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Diámetro](Sketcher_ConstrainDiameter/es.md): Define el diámetro de un arco o círculo seleccionado restringiendo el diámetro.
-   <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Radiam](Sketcher_ConstrainRadiam/es.md): Define automáticamente el radio/diámetro de un arco o círculo seleccionado (peso para un polo B-spline, diámetro para un círculo completo, radio para un arco) {{Version/es|0.20}}
-   <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Ángulo](Sketcher_ConstrainAngle/es.md): Define el ángulo interno entre dos líneas seleccionadas.


<div class="mw-translate-fuzzy">

#### Restricciones especiales 


</div>

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> [Ley de Snell](Sketcher_ConstrainSnellsLaw/es.md): restringe dos líneas para obedecer una ley de refracción para simular la luz que pasa a través de una interfaz.

-   <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width:32px;"> [Alineación interna](Sketcher_ConstrainInternalAlignment/es.md): Alinea los elementos seleccionados con la forma seleccionada (por ejemplo, una línea para convertirse en el eje principal de una elipse).

#### Constraint tools 


<div class="mw-translate-fuzzy">

#### Herramientas para las restricciones 

Las siguientes herramientas pueden utilizarse para cambiar el efecto de las restricciones:


</div>

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [Cambiar la conducción/restricción de referencia](Sketcher_ToggleDrivingConstraint/es.md): Conmuta la barra de herramientas o las restricciones seleccionadas a/desde el modo de referencia.

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Activar/Desactivar restricción](Sketcher_ToggleActiveConstraint/es.md): Activar o desactivar una restricción ya colocada. {{Version/es|0.19}}

### Herriamentas de croquis 

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Selecciona los DOF del solucionador](Sketcher_SelectElementsWithDoFs/es.md): Resalta en verde la geometría con grados de libertad (DOFs), es decir, no totalmente restringida.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width:32px;"> [Forma cercana](Sketcher_CloseShape/es.md): Crea una forma cerrada aplicando restricciones coincidentes a los puntos finales


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width:32px;"> [Conecta los bordes](Sketcher_ConnectLines/es.md): Conectar los elementos del esbozo aplicando restricciones coincidentes a los puntos finales


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width:32px;"> [Seleccione Restricciones](Sketcher_SelectConstraints/es.md): Selecciona las restricciones de un elemento de dibujo


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width:32px;"> [Seleccionar elementos asociados con restricciones](Sketcher_SelectElementsAssociatedWithConstraints/es.md): Seleccionar los elementos de bosquejo asociados a las restricciones


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:32px;"> [Seleccionar restricciones redundantes](Sketcher_SelectRedundantConstraints/es.md): Selecciona las restricciones redundantes del croquis


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:32px;"> [Seleccionar restricciones conflictivas](Sketcher_SelectConflictingConstraints/es.md): Selecciona las restricciones conflictivas del croquis


</div>

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [Mostrar/Ocultar geometría interna](Sketcher_RestoreInternalAlignmentGeometry/es.md): Recrea la geometría interna que falta/elimina la innecesaria de una elipse, arco de elipse/hiperbola/parábola o B-spline seleccionados.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width:32px;"> [Seleccionar el origen](Sketcher_SelectOrigin/es.md): Selecciona el origen del croquis


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width:32px;"> [Seleccionar el eje vertical](Sketcher_SelectVerticalAxis/es.md): Selecciona el eje vertical del croquis


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width:32px;"> [Seleccionar el eje horizontal](Sketcher_SelectHorizontalAxis/es.md): Selecciona el eje horizontal del croquis


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [Symmetría](Sketcher_Symmetry/es.md): Copia un elemento del croquis manteniéndolo simétrico a una línea seleccionada


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Clonar](Sketcher_Clone/es.md): Clona un elemento del croquis


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Copiar](Sketcher_Copy/es.md): Copia un elemento del croquis


</div>

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Muévete](Sketcher_Move/es.md): Mueve la geometría seleccionada tomando como referencia el último punto seleccionado.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [ordenación rectangular](Sketcher_RectangularArray/es.md): Crea un conjunto de elementos seleccionados de croquis


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Eliminar la alineación de los ejes](Sketcher_RemoveAxesAlignment/es.md): Elimina la alineación de los ejes intentando conservar la relación de restricción de la selección {{Version/es|0.20}}


</div>

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Eliminar toda la geometría](Sketcher_DeleteAllGeometry/es.md): Elimina toda la geometría del boceto.

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Eliminar todas las restricciones](Sketcher_DeleteAllConstraints/es.md): Elimina todas las restricciones del boceto.

### Herramientas B-spline de Croquizador 

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Mostrar/ocultar el grado de B-spline](Sketcher_BSplineDegree/es.md)

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Mostrar/ocultar el polígono de control de la B-spline](Sketcher_BSplinePolygon/es.md)

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Mostrar/ocultar peine de curvatura B-spline](Sketcher_BSplineComb/es.md)

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Mostrar/ocultar multiplicidad de nudos B-spline](Sketcher_BSplineKnotMultiplicity/de.md)

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Mostrar/ocultar el peso del punto de control de la B-spline](Sketcher_BSplinePoleWeight/es.md), <small>(v0.19)</small> 

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width:32px;"> [Convertir la geometría en B-spline](Sketcher_BSplineApproximate/es.md)

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Aumentar el grado de B-spline](Sketcher_BSplineIncreaseDegree/es.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Disminuir el grado de la B-spline](Sketcher_BSplineDecreaseDegree/es.md), <small>(v0.19)</small> 

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Aumentar la multiplicidad de nudos](Sketcher_BSplineIncreaseKnotMultiplicity/es.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Disminuir la multiplicidad de nudos](Sketcher_BSplineDecreaseKnotMultiplicity/es.md)

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md), <small>(v0.20)</small> 

### Espacio virtual del croquizador 

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Cambiar el espacio virtual](Sketcher_SwitchVirtualSpace/es.md): Permite ocultar todas las restricciones de un boceto y hacerlas visibles de nuevo.


<div class="mw-translate-fuzzy">

### Preferencias


</div>

-   <img alt="" src=images/Preferences-general.svg  style="width:32px;"> [Preferencias](Sketcher_Preferences/es.md): Preferencias para el ambiente de trabajo *Croquis*.

## Best Practices 


<div class="mw-translate-fuzzy">

## Buenas practicas 

Cada usuario de CAD desarrolla su propia forma de trabajar a lo largo del tiempo, pero hay algunos principios generales útiles a seguir.


</div>


<div class="mw-translate-fuzzy">

-   Una serie de croquis simples es más sencilla de manejar que un croquis complejo. Por ejemplo, un primer croquis se puede crear para la operación base 3D (ya sea un saliente o una revolución), mientras una segunda puede contener taladros o cajeras. Algunos detalles se pueden dejar fuera, para realizar luego como operaciones 3D. Puedes elegir evitar los redondeos en tu croquis si son muchos, y añadirlos como una operación 3D.

-   Crea siempre un perfil cerrado, o tu croquis no producirá un sólido, sino un conjunto de caras abiertas. Si no quieres que alguno de los objetos sea incluido en la creación del sólido, cámbialos a elementos de construcción con la herramienta de Modo de Contrucción.

-   Utiliza las restricciones automáticas para limitar el número de restricciones que tendrás que añadir manualmente.

-   Como regla general, aplica las restricciones geométricas primero, luego las restricciones dimensionales, y bloquea tu croquis al final. Pero recuerda: Las reglas se hacen para romperlas. Si tienes problemas manipulando tu croquis, puede ser útil restringir algunos objetos antes de completar el perfil.

-   Si es posible, centra tu croquis en el origen (0,0) con la restricción de bloqueo. Si tu croquis no es simétrico, ubica uno de sus puntos en el origen, o selecciona un buen número para las distancias de bloqueo. En la v0.12, las restricciones externas (restringiendo el croquis con respecto a geometría 3D como aristas u otros croquis) no están implementada. Esto significa q2ue para ubicar las siguientes geometrías de croquis a tu primer croquis, necesitaras definir distancias relativas a tu primer croquis manualmente. Una restricción de bloqueo de (25,75) desde el origen es más fácil de recordar que (23.47,73.02).

-   Si tienes la posibilidad de seleccionar entre la Restricción Distancia y las restricciones de Distancia Vertical o Distancia Horizontal, es mejor que utilices las últimas pues se comportan mejor a nivel de consumo de memoria.

-   En general, las mejores restricciones a utilizar son: Restricciones horizontales/verticales; Restricciones de distancia horizontal o vertical y tangencia en puntos finales. De ser posible, conviene limitar el uso de: Restricciones de Distancia; tangencia entre aristas; Punto en Objeto y simetría.

-   Si tiene dudas sobre la validez de un boceto una vez completado (las características se vuelven verdes), cierre el cuadro de diálogo Sketcher, cambie al <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Ambiente de trabajos piezas](Part_Workbench/es.md) y ejecuta **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Comprobar geometría](Part_CheckGeometry/es.md)**.


</div>

## Tutoriales

-   [Tutorial de croquis](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) por Chrisb. Este es un documento PDF de 70 páginas que sirve como un manual detallado para el croquis. Explica los fundamentos del uso del croquis, y entra en muchos detalles sobre la creación de formas geométricas, y cada una de las restricciones.
-   [Tutorial básico de dibujo](Basic_Sketcher_Tutorial/es.md) para principiantes
-   [Coquis Micro Tutorial - Prácticas de Restricción](Sketcher_Micro_Tutorial_-_Constraint_Practices/es.md)
-   [Requisito por un boceto](Sketcher_requirement_for_a_sketch/es.md) Requisito mínimo de un boceto y determinación completa de un boceto

## Guión

La página [Croquizador Guión](Sketcher_scripting/es.md) contiene ejemplos sobre cómo crear restricciones a partir de scripts de Python.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Sketcher](Category_Sketcher.md) > Sketcher Workbench/es

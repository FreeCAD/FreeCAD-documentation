# <img alt="El icono del Ambiente de trabajo PartDesign " src=images/Workbench_PartDesign.svg  style="width:64px;"> PartDesign Workbench/es


{{TOCright}}



## Introducción

El <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Ambiente de trabajo de diseño de piezas](PartDesign_Workbench/es.md) proporciona herramientas avanzadas para modelar piezas sólidas complejas. Se centra principalmente en la creación de piezas mecánicas que pueden ser fabricadas y ensambladas en un producto terminado. Sin embargo, los sólidos creados pueden ser utilizados en general para cualquier otro propósito como [diseño arquitectónico](Arch_Workbench/es.md), [análisis de elementos finitos](FEM_Workbench/es.md), o [mecanizado e impresión 3D](Path_Workbench/es.md).

El Ambiente de trabajo DiseñoPiezas está intrínsecamente relacionado con el [Ambiente de trabajo Croquizador](Sketcher_Workbench/es.md). El usuario normalmente crea un Sketch, luego utiliza la herramienta [Almohadilla DiseñoPiezas](PartDesign_Pad/es.md) para extruirlo y crear un sólido básico, y luego este sólido se modifica aún más.

Mientras que el <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Ambiente de trabajo Pieza](Part_Workbench/es.md) se basa en una metodología de [geometría sólida constructiva](constructive_solid_geometry/es.md) (CSG) para la construcción de formas, el Ambiente de trabajo DisegnoPiezas utiliza una metodología paramétrica, de edición de características, lo que significa que un sólido básico se transforma secuencialmente añadiendo características encima hasta obtener la forma final. Consulte la página [edición de características](feature_editing/es.md) para obtener una explicación más completa de este proceso y, a continuación, consulte [Creación de una pieza sencilla con DisegnoPiezas](Creating_a_simple_part_with_PartDesign/es.md) para empezar a crear sólidos.

Una discusión más detallada sobre el ambiente de trabajo Piezas frente al ambiente de trabajo de DiseñoPiezas se puede encontrar aquí: [ Piezas y DiseñoPiezas](Part_and_PartDesign/es.md).

Los cuerpos creados con PartDesign suelen estar sujetos al [problema de denominación topológica](Topological_naming_problem/es.md) que hace que las características internas cambien de nombre cuando se modifican las operaciones paramétricas. Este problema puede minimizarse siguiendo las mejores prácticas descritas en la página [edición de funciones](feature_editing/es.md), y aprovechando los objetos datum como soporte de bocetos y funciones.

<img alt="" src=images/PartDesign_Example.png  style="width:500px;">



## Herramientas

Las herramientas de Diseño de Piezas están ubicadas en el menú **Diseño de Piezas** y la barra de herramientas de Diseño de Piezas que aparece cuando se carga el Ambiente de Trabajo de Diseño de Piezas.



### Herramientas de la estructura 

Estas herramientas no son de hecho parte de l\'Ambiente de Trabajo de diseño de piezas. Pertenecen al sistema [Std Base](Std_Base/es.md). Fueron desarrolladas en la v0.17 con la intención de que fueran útiles para organizar un modelo, y crear [montajes](Std_Base/es.md); como tal, son muy útiles cuando se trabaja con cuerpos creados con este Ambiente de Trabajo.

-   <img alt="" src=images/Std_Part.svg  style="width:32px;"> [Pieza](Std_Part/es.md): añade un nuevo contenedor de Parte en el documento activo y lo hace activo.

-   <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Grupo](Std_Group/es.md): añade un contenedor de Grupo en el documento activo, que permite organizar los objetos en el [vista de árbol](Tree_view/es.md).



### DiseñoPiezas herramientas de ayuda 

-   <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> [Crear Cuerpo](PartDesign_Body/es.md): Crea un [cuerpo](Body/es.md) objeto en el documento activo y lo activa.

-   <img alt="" src=images/PartDesign_NewSketch.svg  style="width:32px;"> [Crear croquis](PartDesign_NewSketch/es.md): crea un nuevo croquis on la cara o plano seleccionados. Si no se selecciona una cara o un plano, el usuario deberá seleccionar un plano del dialogo de tareas. El interfaz alterna al [Ambiente de Trabajo de croquis](Sketcher_Workbench/es.md) mientras el croquis esté en modo edición.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Editar Croquis](Sketcher_EditSketch/es.md): Editar el croquis seleccionado.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_MapSketch.svg‎  style="width:32px;"> [Fijar croquis a cara](Sketcher_MapSketch/es.md): Fija el croquis a un plano previamente selecionado o a una cara del cuerpo activo.


</div>

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Validate sketch](Sketcher_ValidateSketch.md): verifies the tolerance of different points and adjusts them.



### Herramientas de modelado 



#### Herramientas de geometría de referencia 

-   <img alt="" src=images/PartDesign_Point.svg  style="width:32px;"> [Crear un punto de referencia](PartDesign_Point/es.md): crea un punto de referencia en el cuerpo activo.

-   <img alt="" src=images/PartDesign_Line.svg  style="width:32px;"> [Crear una línea de referencia](PartDesign_Line/es.md): crea una línea de referencia en el cuerpo activo.

-   <img alt="" src=images/PartDesign_Plane.svg  style="width:32px;"> [Crear un plano de referencia](PartDesign_Plane/es.md): crea un plano de referencia en el cuerpo activo.

-   <img alt="" src=images/PartDesign_CoordinateSystem.svg  style="width:32px;"> [Crear un sistema de coordenadas local](PartDesign_CoordinateSystem/es.md): crea un sistema de coordenadas local unido a la geometría datum en el cuerpo activo.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:32px;"> [Crear un conector de forma o forma unida](PartDesign_ShapeBinder/es.md): crea un conector de forma o forma unida en el cuerpo activo.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Crear un aglutinante de forma de subobjeto](PartDesign_SubShapeBinder/es.md): crea un aglutinante de forma a un subelemento, como una arista o una cara de otro cuerpo, conservando la posición relativa de ese elemento. {{Version/es|0.19}}


</div>

-   <img alt="" src=images/PartDesign_Clone.svg  style="width:32px;"> [Crear un clón](PartDesign_Clone/es.md): crea un clon del cuerpo seleccionado.



#### Herramientas aditivas 

Son herramientas para crear operaciones base o para añadir material a un cuerpo sólido preexistente.

-   <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Pastilla](PartDesign_Pad/es.md): extruye un sólido a partir del croquis seleccionado.

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Revolución](PartDesign_Revolution/es.md): crea un sólido de revolución alrededor de un eje a partir de un croquis. El croquis debe contener un perfil cerrado.

-   <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width:32px;"> [Solevación aditiva](PartDesign_AdditiveLoft/es.md): crea un sólido solevando un perfil y adaptándolo a al menos a una segunda sección definida por un segundo perfil.

-   <img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:32px;"> [Barrido aditivo](PartDesign_AdditivePipe/es.md): crea un sólido barriendo uno o varios croquis a lo largo de una trayectoria abierta o cerrada.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [Hélice aditiva](PartDesign_AdditiveHelix/es.md): crea un sólido barriendo un boceto a lo largo de una hélice. {{Version/es|0.19}}


</div>

-   <img alt="" src=images/PartDesign_CompPrimitiveAdditive.png  style="width:48px;"> [Crear una primitiva aditiva](PartDesign_CompPrimitiveAdditive/es.md): añade una primitiva aditiva al cuerpo activo.

  -<img alt="" src=images/PartDesign_Additive_Box.svg  style="width:32px;"> [Cubo aditivo](PartDesign_AdditiveBox/es.md): crea un cubo aditivo.

  -<img alt="" src=images/PartDesign_AdditiveCylinder.svg  style="width:32px;"> [Cilindro aditivo](PartDesign_AdditiveCylinder/es.md): crea un cilindro aditivo.

  -<img alt="" src=images/PartDesign_AdditiveSphere.svg  style="width:32px;"> [Esfera aditiva](PartDesign_AdditiveSphere/es.md): crea una esfera aditiva.

  -<img alt="" src=images/PartDesign_Additive_Cone.svg  style="width:32px;"> [Cono aditivo](PartDesign_AdditiveCone/es.md): crea un cono aditivo.

  -<img alt="" src=images/PartDesign_AdditiveEllipsoid.svg  style="width:32px;"> [Elipsoide aditivo](PartDesign_AdditiveEllipsoid/es.md): crea un elipsoide aditivo.

  -<img alt="" src=images/PartDesign_AdditiveTorus.svg  style="width:32px;"> [Toro aditivo](PartDesign_AdditiveTorus/es.md): crea un toro aditivo.

  -<img alt="" src=images/PartDesign_AdditivePrism.svg  style="width:32px;"> [Prisma aditivo](PartDesign_AdditivePrism/es.md): crea un prisma aditivo.

  -<img alt="" src=images/PartDesign_AdditiveWedge.svg  style="width:32px;"> [Cuña aditiva](PartDesign_AdditiveWedge/es.md): crea una cuña aditiva.



#### Herramientas sustractivas 

Son herramientas para sustraer material de un cuerpo existente.

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Cajera](PartDesign_Pocket/es.md): crea un cajera a partir de un croquis seleccionado.

-   <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> [Agujero](PartDesign_Hole/es.md): crea un agujero a partir de un croquis seleccionado. Este croquis puede contener varios círculos.

-   <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [Ranura](PartDesign_Groove/es.md): crea una ranura de revolución alrededor de un eje.

-   <img alt="" src=images/PartDesign_SubtractiveLoft.svg  style="width:32px;"> [Solevación sustractiva](PartDesign_SubtractiveLoft/es.md): crea un sólido solevando un perfil y adaptándolo a al menos a una segunda sección definida por un segundo perfil y sustrae dicho sólido del cuerpo activo.

-   <img alt="" src=images/PartDesign_SubtractivePipe.svg  style="width:32px;"> [Barrido sustractivo](PartDesign_SubtractivePipe/es.md): crea un sólido barriendo uno o más croquis a lo largo de una trayectoria abierta o cerrada y sustrayendo el sólido resultante del cuerpo activo.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [Hélice sustractiva](PartDesign_SubtractiveHelix/es.md): crea una forma sólida barriendo un boceto a lo largo de una hélice y la sustrae del cuerpo activo. {{Version/es|0.19}}


</div>

-   <img alt="" src=images/PartDesign_CompPrimitiveSubtractive.png  style="width:48px;"> [Crear una primitiva sustractiva](PartDesign_CompPrimitiveSubtractive/es.md): añade una primitiva sustractiva al cuerpo actual.

  -<img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:32px;"> [Cubo sustractivo](PartDesign_SubtractiveBox/es.md): añade un cubo sustractivo al cuerpo actual.

  -<img alt="" src=images/PartDesign_SubtractiveCylinder.svg  style="width:32px;"> [Cilindro sustractivo](PartDesign_SubtractiveCylinder/es.md): añade un cilindro sustractivo al cuerpo activo.

  -<img alt="" src=images/PartDesign_SubtractiveSphere.svg  style="width:32px;"> [Esfera sustractiva](PartDesign_SubtractiveSphere/es.md): añade una esfera sustractiva al cuerpo activo.

  -<img alt="" src=images/PartDesign_SubtractiveCone.svg  style="width:32px;"> [Cono sustractivo](PartDesign_SubtractiveCone/es.md): añade un cono sustractivo al cuerpo actual.

  -<img alt="" src=images/PartDesign_SubtractiveEllipsoid.svg  style="width:32px;"> [Elipsoide sustractivo](PartDesign_SubtractiveEllipsoid/es.md): añade un elipsoide sustractivo al cuerpo activo.

  -<img alt="" src=images/PartDesign_SubtractiveTorus.svg  style="width:32px;"> [Toro sustractivo](PartDesign_SubtractiveTorus/es.md): añade un toro sustractivo al cuerpo activo.

  -<img alt="" src=images/PartDesign_SubtractivePrism.svg  style="width:32px;"> [Prisma sustractivo](PartDesign_SubtractivePrism/es.md): añade un prisma sustractivo al cuerpo activo.

  -<img alt="" src=images/PartDesign_SubtractiveWedge.svg  style="width:32px;"> ‎[Cuña sustractiva](PartDesign_SubtractiveWedge/es.md): añade una cuña sustractiva al cuerpo activo.



#### Herramientas de transformación 


<div class="mw-translate-fuzzy">

Son herramientas que permite transformar operaciones existentes. Permiten elegir las operaciones a ser transformadas.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [Reflexión o simetría](PartDesign_Mirrored/es.md): refleja una o más operaciones con respecto a un plano o una cara generando su operación simétrica con respecto a dicho plano o cara.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Patrón de repetición lineal](PartDesign_LinearPattern/es.md): crea un patrón de repetición lineal basado en una o más operaciones.


</div>

-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [Patrón de repetición polar](PartDesign_PolarPattern/es.md): crea un patrón de repetición polar de una o más operaciones.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [Crear transformaciones múltiples](PartDesign_MultiTransform/es.md): crea un patrón de repetición combinando de forma sucesiva una serie de transformaciones.


</div>



#### Herramientas de alteración 


<div class="mw-translate-fuzzy">

Estas operaciones alteran las caras o aristas seleccionadas.


</div>

-   <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [Redondeado](PartDesign_Fillet/es.md): Altera una arista del cuerpo activo redondeándola.

-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [Chaflán](PartDesign_Chamfer/es.md): Altera una arista del cuerpo activo creando un chaflán.

-   <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [Corte inclinado](PartDesign_Draft/es.md): altera un cara del cuerpo activo aplicándole un corte inclinado.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Thickness.svg  style="width:32px;"> [Vaciado de espesor](PartDesign_Thickness/es.md): altera el sólido eliminando las caras seleccionadas y creando un sólido definido por una superficie de un determinado espesor.


</div>



#### Operaciones booleanas 

-   <img alt="" src=images/PartDesign_Boolean.svg  style="width:32px;"> [Operaciones booleanas](PartDesign_Boolean/es.md): importa uno o más cuerpos o clones (de diseño de piezas) en el cuerpo activo y ejecuta una operación booleana.

#### Extras

Otras funcionalidades adicionales disponibles en el menú de diseño de piezas:

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width:32px;"> [Herramienta de migración](PartDesign_Migrate/es.md): migra ficheros creados con versiones anteriores de FreeCAD. Si el fichero está basado única y exclusivamente de operaciones del banco de diseño de piezas de la versión anterior, la migración debería ser exitosa. Si el fichero contiene objetos creados utilizando diversos bancos de trabajo es de esperar que la migración falle.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [Asistente de diseño de piñones](PartDesign_Sprocket/es.md): crea un perfil de piñón que puede ser acolchado. {{Version/es|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_InternalExternalGear.svg  style="width:32px;"> [Asistente de diseño Engranajes de involuta](PartDesign_InvoluteGear/es.md): crea un perfil de engranaje de involuta que puede ser acolchado.


</div>

-   <img alt="" src=images/PartDesign_WizardShaft.svg  style="width:32px;"> [Asistente de diseño de eje](PartDesign_WizardShaft/es.md): Genera un eje a partir de una serie de valores y permite analizar fuerzas y momentos de fuerza. El eje se genera mediante revolución de un croquis que puede ser editado a posteriori.



### Elementos del menú contextua 

-   <img alt="" src=images/PartDesign_MoveTip.svg  style="width:32px;"> [Establecer Punta](PartDesign_MoveTip/es.md): redefine la punta, que es la característica expuesta fuera del Cuerpo.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [Mover objeto a otro cuerpo](PartDesign_MoveFeature/es.md): mueve el croquis, la geometría del dato o la característica seleccionada a otro Cuerpo.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [Mover objeto después de otro objeto](PartDesign_MoveFeatureInTree/es.md): permite reordenar el árbol de Cuerpos moviendo el croquis, la geometría datum o la característica seleccionada a otra posición en la lista de características.



#### Artículos compartidos con Ambiente de Trabajo Pieza 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Apariencia](Std_SetAppearance/es.md): determina la apariencia de toda la parte (transparencia del color, etc.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Asignar colores](Part_FaceColors/es.md): asigna colores a las caras de las partes.




<div class="mw-translate-fuzzy">

### Preferencias


</div>

\<!\--Las preferencias de diseño de la pieza se definen en el Ambiente de Trabajo de la pieza y tanto el Ambiente de Trabajo de diseño de la pieza como el Ambiente de Trabajo de la pieza las usan\...

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Preferences](PartDesign_Preferences/es.md): preferencias disponibles para las herramientas de PartDesign.
-   [Ajuste fino](Fine-tuning/es.md): algunos parámetros extra para ajustar el comportamiento de PartDesign.



## Tutoriales

-   [Cómo usar FreeCAD](http://help-freecad-jpg87.fr/), un sitio web que describe el flujo de trabajo para el diseño mecánico.
-   [Creando una pieza simple con PartDesign](Creating_a_simple_part_with_PartDesign/es.md)
-   [Tutorial de diseño de piezas básicas](Basic_Part_Design_Tutorial/es.md)
-   [PartDesign Bearingholder Tutorial I](PartDesign_Bearingholder_Tutorial_I/es.md) (necesita actualizarse) (en inglés)
-   [PartDesign Bearingholder Tutorial II](PartDesign_Bearingholder_Tutorial_II/es.md) (necesita actualizarse) (en inglés)

## Examples

For some ideas of what can be achieved with Part Design tools, have a look at: [PartDesign examples](PartDesign_Examples.md).

<img alt="" src=images/PartDesign_ExampleSphere-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleTorus-01.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExamplePad-09.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-05.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSpring-04.png  style="width:80px;">





 {{PartDesign_Tools_navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > PartDesign Workbench/es

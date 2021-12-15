# Release notes 0.17/es
<div id="itsfree" style="text-align:left;color:black;background:#f6f6f6;margin:1em 7em;padding:0.5em 2em;border:2px solid #a7d7f9;">

\"Esta edición de FreeCad está dedicada a nuestro amigo Roland Frank [quien nos dejó el 2017](https://forum.freecadweb.org/viewtopic.php?f=8&t=25673). Él fue un activo y muy apreciado miembro del foro de FreeCAD. Además sus video-tutoriales en los canales de Youtube [Learn FreeCAD](https://www.youtube.com/watch?v=_HEvhclR4-o&list=PL6fZ68Cq3L8k0JhxnIVjZQN26cn9idJrj) y [BPLFRE](https://www.youtube.com/watch?v=m49z0weonog&list=PLsrwVwvqYb8G4Ri0iz1JIebsOXkgoytAY) ayudaron a muchas personas a iniciarse en FreeCAD.\"


</div>


<div class="mw-translate-fuzzy">

FreeCAD 0.17 fue lanzado el 06 de abril, 2018. Puedes obtenerlo de la página de [descarga](Download/es.md). Este es un resumen de los cambios más interesantes. La lista completa de cambios puede ser vista en [MantisBT bugtracker FC 0.17 changelog](https://www.freecadweb.org/tracker/changelog_page.php?version_id=73).

Notas de anteriores lanzamientos pueden ser vistas en la página [Comenzando](Getting_started/es.md).


</div>

<img alt="" src=images/Release017_Title.jpg  style="width:800px;"> 
*Garden Railway Coach O&K (por el usuario de FreeCAD \"Garden Railway Coach O&K\", ver [Users Showcase](http://forum.freecadweb.org/viewtopic.php?f=24&t=17261))*

## Principales Novedades 

Han pasado casi dos años desde la anterior versión 0.16, pero el equipo de FreeCAD no permaneció inactivo durante este período. Más de 6,800 revisiones fueron agregadas al código fuente de FreeCAD. En comparación, ¡esto es más de tres veces el trabajo hecho entre v0.16 y v0.15! La mayoría de los entornos de trabajo existentes se beneficiaron de las mejoras y se agregaron dos nuevos entornos de trabajo. También han sido desarrollados nuevos módulos adicionales por la comunidad. Algunos de los cambios más importantes:

El entorno de trabajo \"PartDesign\" ha sido completamente revisado. Ahora hay un nuevo contenedor llamado \"Body\" que contiene una cadena de funciones y alivia la necesidad de asignar bocetos a caras planas. Nuevas herramientas para crear geometrías de referencia (datum) como puntos, ejes y planos hacen que el diseño de piezas sea mucho más versátil. ![](images/PartDesign_Body_tree.png )


<div class="mw-translate-fuzzy">

El nuevo [\"Addon manager\"](Std_AddonMgr.md) disponible en el menu \"Herramientas\" (el cual estaba previamente disponible como [addons installer macro](https://github.com/FreeCAD/FreeCAD-addons)) hace que la instalación y actualización de módulos y macros adicionales sea mucho más fácil y estandarizada para Windows, Mac OS X y Linux.


</div>

<img alt="" src=images/Addon_manager_v017.png  style="width:300px;">

El entorno \"Sketcher\" ahora soporta la creacion de B-spline con muchas formas de controlar curvas y desplegar información de estas. <img alt="" src=images/FC017_Sketcher_B-spline_01.png  style="width:300px;">

El nuevo entorno \"TechDraw\" tiene como objetivo reemplazar el entorno de trabajo \"Drawing\", y ya tiene más funcionalidades que el antiguo entorno. <img alt="" src=images/TechDraw_Workbench_Example.png  style="width:300px;">

## Generalidades

-   Yorik van Havre escribió \"_\" como un libro introductorio de como usar FreeCAD.
-   Los recálculos de documentos ahora se pueden deshabilitar / habilitar a través del menú contextual.
-   Se agregó un nuevo estilo de navegación Revit.
-   Nuevo indicador de navegación en la parte inferior derecha de la ventana de FreeCAD que permite un acceso rápido a los estilos de navegación.

![](images/FC017_Navigation_Indicator_01.png ) ![](images/FC017_Navigation_Indicator_02.png )


<div class="mw-translate-fuzzy">

-   El [dependency graph](Std_DependencyGraph.md) se benefició de mejoras gráficas.
-   La importación de archivos STEP aprovecha el nuevo [Part container](Std_Part.md) y lo usa para organizar un ensamblaje STEP en subconjuntos, siguiendo más de cerca la estructura del documento original. stpZ (un formato STEP comprimido) ahora es compatible.
-   La mayoría de los íconos de FreeCAD fueron reelaborados para cumplir mejor con las pautas del estilo Tango [Tango guidelines](http://tango.freedesktop.org/Tango_Icon_Theme_Guidelines)..


</div>

-   El proyecto FreeCAD reconoce las contribuciones de su comunidad al agregar una pestaña de créditos en el diálogo \'\' Acerca de FreeCAD \'\'. Las nuevas pestañas de Licencias y Bibliotecas incluyen la licencia de FreeCAD y proporcionan información sobre bibliotecas usadas de terceros.

<img alt="" src=images/AboutFreeCAD_Credits.png  style="width:300px;">

## Entorno de Trabajo Arch 

-   Nueva herramienta [Arch Schedule](Arch_Schedule.md): esta herramienta ha sido completamente reescrita, y ahora ofrece maneras mucho más flexible de reunir datos del documento en una hoja de cálculo, utilizando diferentes tipos de consultas, como contar todos los objetos de un cierto tipo, o resumiendo el volumen total de una cierta categoría de objetos.

-   Nuevo set de [herramienta de tuberías](Arch_Pipe.md) para diseñar sistemas de tuberías. Puede usar líneas, bocetos o cables como base para colocar tubos y crear automáticamente conexiones entre 2 o 3 tubos.


<div class="mw-translate-fuzzy">

-   La herramienta [Arch Estructura](Arch_Structure/es.md) ahora ha sido ampliada con una serie de nuevas librerías de partes para construir elementos prefabricados de hormigón.


</div>

-   Durante la edición 2017 del [Google Summer of Code](Google_Summer_of_Code.md), en la cual FreeCAD participó, la herramienta [Arch Rebar](Arch_Rebar.md) fue ampliada y se le proveyó de una interfaz de usuario amigable para agregar fácilmente varios tipos de barras estándar de refuerzo a sus estructuras de concreto.

<img alt="" src=images/Arch_Rebar_preview.png  style="width:640px;">


<div class="mw-translate-fuzzy">

-   La herramienta [Arch Ventanas](Arch_Window.md) tiene varias mejoras, tales como la posibilidad de definir subcomponentes como abatibles, mostrar símbolos de apertura, abrirse y tener paneles de persiana.


</div>

<img alt="" src=images/Arch_Door_preview.png  style="width:640px;">

-   La herramientas [Arch Ejes](Arch_Axis/es.md) también se han reescrito y permiten sistemas más complejos al combinar diferentes series de ejes. También se pueden personalizar para mostrar diferentes tipos de situaciones, como niveles.


<div class="mw-translate-fuzzy">

-   Una nueva herramienta [Arch Grid](Arch_Grid.md) permite crear fácilmente objetos base similar a un cuadriculado estirando, uniendo o dividiendo celdas. Estos objetos de rejilla se pueden usar como sistemas de ejes o como bases para arreglos complejos de ventanas o paneles.


</div>


<div class="mw-translate-fuzzy">

-   Las nuevas herramientas [Panel tools](Arch_Panel_Cut.md) fueron específicamente diseñadas para la construccion de paneles. Permiten construir un modelo compuesto por [ Arch Panels](Arch_Panel.md), y luego generan placas con los patrones que pueden ser utilizadas por [Path Workbench](Path_Workbench.md) para generar código para máquinas de corte.


</div>


<div class="mw-translate-fuzzy">

-   Una nueva herramienta [Nesting](Arch_Nest.md) (aun experimental), que permite crear paneles de corte colocando automáticamente los patrones 2D en una silueta contenedora.


</div>


<div class="mw-translate-fuzzy">

-   [Multi-materials](Arch_MultiMaterial.md) se han incorporado al Ambiente de Trabajo Arch. Permiten crear automáticamente muros multicapa o controlar los diferentes materiales de objetos compuestos como ventanas.


</div>

-   El exportador de formatos OBJ y DAE del Ambiente de Trabajo Arch ahora admite materiales, tanto al importar como al exportar.

-   Se ha agregado el soporte de importación para el formato [3DS](Arch_3DS.md).

## Ambiente de Trabajo Draft 

-   [Autogroup system](Draft_AutoGroup.md): El Ambiente de Trabajo Draft ahora presenta un botón de autogrupo en su barra de herramientas. Cuando se activa, todos los objetos Draft y Arch recién creados se colocarán automáticamente en ese grupo.


<div class="mw-translate-fuzzy">

-   _ o una [Draft Wire](Draft_Wire.md), esta herramienta te permitirá darle una pendiente/inclinación. Es decir, los puntos intermedios y finales obtendrán un valor Z más bajo, por lo que todo el objeto obtiene una inclinación constante. Esto es útil para usar Lineas o Wires como bases para objetos que necesitan una inclinación precisa, como paneles de techo o tuberías de alcantarillado.


</div>


<div class="mw-translate-fuzzy">

-   _, a menudo es necesario almacenar ubicaciones de plano de trabajo que usa con frecuencia. Esto ahora es posible colocando uno de esos \"proxies\" en su documento. Recordará la ubicación del plano de trabajo actual y también puede restaurar la vista actual y/o la visibilidad de los objetos.


</div>

<img alt="" src=images/Draft_WP_preview.png  style="width:640px;">


<div class="mw-translate-fuzzy">

-   [Draft Stretch](Draft_Stretch.md): El Ambiente de Trabajo Draft ahora tiene una herramienta de estiramiento, que permite mover los vértices de varios objetos Draft a la vez.


</div>


<div class="mw-translate-fuzzy">

-   [Draft Label](Draft_Label.md): Con esta herramienta, uno puede colocar etiquetas en el documento. Estas, al ser compuestas de una pieza de texto y una línea guía, pueden estar libre o ancladas a un objeto específico. El texto puede ser personalizado, o mostrar automáticamente el contenido de una propiedad del objeto de destino.


</div>

<img alt="" src=images/Draft_Label_Preview.png  style="width:640px;">

## Ambiente de Trabajo FEM 

-   FEM Mesh
    -   **Objeto Gmsh** es un objeto de malla, que permite usar la herramienta de malla Gmesh [Gmsh](http://gmsh.info/) dentro de FreeCAD. Varias opciones de Gmesh son compatibles.
    -   **Objeto de capa límite para gmsh** hace posible crear una capa límite.
    -   **Objeto de grupo de malla para gmsh** hace posible crear nodos y grupos de elementos. Los nombres pueden ser cambiados por el usuario.
    -   **Objeto de malla de región para gmsh** hace posible definir regiones de malla con diferentes tamaños de elementos de malla para nodos, bordes, caras y volúmenes.
    -   **GUI clear mesh tool** borra la malla pero mantiene todos los ajustes de malla. Esto es muy útil si los archivos deben ser compartidos.
    -   **GUI print mesh information tool** imprime todo tipo de información de malla.
    -   **Proveedor de vista de malla GUI** puede mostrar malla de cuádruple cara así como elementos de malla hexadecimal, pentaeder y de pirámide.
    -   \'\'\' Modelo de datos de malla \'\'\'se actualizó a SMESH a la versión 7.7.1 <https://github.com/FreeCAD/FreeCAD/commit/666a3e5a>
    -   **Mesh API** se extendió para leer los datos del grupo de malla de los datos de malla de FreeCAD SMESH FEM por Python. Esta fue la base para el objeto grupal Gmsh.
    -   **Mesh API** se amplió para exportar grupos de malla al formato de archivo inp Abaqus y CalculiX.
    -   **Herramienta de malla 2 de malla FEM**convierte una superficie de una malla de volumen en una malla para el módulo de malla de FreeCAD.
    -   **Problemas de malla:**Los Jacobianos no positivos son un problema frecuente en las mallas FEM. Los elementos que tienen Jacobianos no positivos en el solver CalculiX están coloreados en FreeCAD.
    -   **Fenics** Se ha agregado la importación y exportación del formato de malla Fenics.

-   Objetos
    -   **Objeto de rotación de haz** permite el análisis de haces girados alrededor de su eje principal.
    -   **Objeto material no lineal** agrega comportamiento de material no lineal a FreeCAD FEM. Es compatible con el cambio lineal de la curva de tensión de esfuerzo.
    -   **Material fluido** \...
    -   **Velocidad de flujo inicial de restricción** \...
    -   **Límite de fluido de restricción**
    -   **Potencial electrostático de restricción** \...
    -   **Fuente de calor del cuerpo de restricción** \...
    -   **Transformación de restricción** \...
    -   **Temperatura de restricción** \...
    -   **Contacto de restricción** \...
    -   **Rotación del plano de restricción** \...
    -   **Restricción del peso propio** \...

-   Solver
    -   **Solver frame work** se escribió desde cero durante un proyecto de Google Summer of Code.
    -   Se agregó soporte para el software de solución FEM **ElmerFEM**, <https://www.csc.fi/web/elmer>.
    -   Dentro del trabajo del Solver frame work, el tipo de análisis puede ser elegido por un **objeto de ecuación** (solo para Elmer Solver, ATM)
    -   Se agregó compatibilidad básica para el software de solución FEM **Z88**, <https://en.z88.de/z88os/>.
    -   **CalculiX** fue portado al Solver frame work. El objeto de resolución de ccxtools permanece en FreeCAD FEM porque está muy bien probado y tiene controles previos ampliados.

-   Calculix Analysis
    -   **Análisis estructural térmico acoplado** \...
    -   **Análisis de análisis de flujo de tubería 1D** \...
    -   **Modelos acoplados de Beam Shell Solid**\...

-   Post Procesamiento Estandar
    -   **Shell and beam 3D output** Permite emitir el análisis de vigas y revestimiento como un 3D sólido para ver las tensiones en secciones.
    -   **Peeq strain** Se ha agregado soporte para deformación plástica equivalente al objeto de resultado, lector de resultados y procesamiento posterior de vtk.

-   Post Processing Extendido
    -   **VTK** Se ha agregado un procesamiento de publicación extendido basado en [VTK](https://www.vtk.org/).
    -   **Filtro de clips** \...
    -   **Filtro de clip escalar** \...
    -   **Cut filter** \...
    -   **Ajustar filtro vectorial** \...
    -   **Tensiones linealizadas** \...
    -   **Datos en el punto** Una herramienta para obtener los datos del resultado para un punto específico.
    -   **Datos a lo largo de la línea** Una herramienta para obtener los resultados de una línea específica impresa como un diagrama.

-   Arreglos, código y otras cosas
    -   Se ha ampliado el \"conjunto de pruebas unitarias\" para el Ambiente de Trabajo FEM.
    -   La **base del código** ha sido mejorada enormemente.
    -   La mayoría del código FEM ha sido portado a **Python3**.
    -   Además, se han encontrado **toneladas de errores** que fueron arreglados.
    -   Todos los **íconos** han sido redibujados suigiendo las pautas.
    -   **Formateo de código** No debe haber más pestañas y espacios en blanco en todo el código fuente de FEM.
    -   El código de Python cumple con la mayoría de las reglas de **flake8**.
    -   Se corrigieron docenas de **errores tipográficos**dentro del código fuente (hasta donde sé, esto se aplica a todo FreeCAD, luzpaz los encuentra a todos como encontrar una aguja en el pajar).

-   Algunas Imágenes

<img alt="" src=images/bridge-all.png  style="width:640px;"> <img alt="" src=images/bridge-detail.png  style="width:640px;">

## Ambiente de Trabajo Part 

-   El kernel de modelado geométrico de Open Cascade se actualizó de 6.8.0 a 7.2.0 (la versión real de OCC puede depender de la plataforma / distro). Esta versión trae una gran cantidad de correcciones de errores en operaciones booleanas, algoritmo de eliminación de línea oculta, y permite agregar nuevas características al Ambiente de Trabajo Part.

-   Nuevas funciones: [ Boolean Fragments](Part_BooleanFragments.md), [ Slice](Part_Slice.md) y [ XOR](Part_XOR.md).

-   Gracias a las nuevas características anteriores, los sólidos compuestos (compsolids) ahora se pueden crear en FreeCAD. Son de gran utilidad en FEM.

-   [ Connect](Part_JoinConnect.md) Se mejoró el rendimiento y la confiabilidad, y la herramienta se hizo más versátil.

-   Nueva función: [2D Offset](Part_Offset2D.md), para hacer offset sobre planar wires.

-   Mejora: la herramienta [Part Extrude](Part_Extrude.md) ahora admite la dirección paramétrica Normal, la dirección controlada por el borde vinculado, la inversión, la segunda longitud, el segundo ángulo de inclinación y la simétrica. Además, la casilla de verificación Make Solid ahora se marca automáticamente si se abre el cuadro de diálogo y el objeto seleccionado es un wire cerrado (por ejemplo, un sketch).

-   Mejora: la herramienta [Part Revolve](Part_Revolve.md) ahora admite el enlace paramétrico al eje de revolución.


<div class="mw-translate-fuzzy">

-   La nueva utilidad [Part EditAttachment](Part_EditAttachment.md) accesible desde el menú \'\' Part → Attachment\... \'\' se puede usar para unir paramétricamente la mayoría de los tipos de objetos a otra geometría.


</div>

-   El nuevo [ Contenedor Part](Std_Part.md) se puede usar para agrupar la mayoría de los tipos de formas y moverlas como una unidad. También contiene planos y ejes estándar para adjuntar objetos. Servirá de base para el futuro Ambiente de trabajo Assembly al proporcionar una forma de mover partes. Está disponible en todos los bancos de trabajo desde una barra de herramientas junto con [ Group](Std_Group.md).

## Ambiente de Trabajo PartDesign 

El banco de trabajo PartDesign recibió cambios masivos, fruto de los esfuerzos combinados de múltiples desarrolladores durante un período de 5 años. <img alt="" src=images/PartDesign017-teaser-motor-core.png  style="width:800px;">


<div class="mw-translate-fuzzy">

-   El nuevo contenedor [ Body](PartDesign_Body.md) contiene una cadena de características de PartDesign que forman un único sólido contiguo. También contiene planos y ejes estándar para adjuntar objetos. Gracias al contenedor de Body, ya no es necesario mapear bocetos en las caras al agregar características. Este requisito era una limitación importante de la antigua PartDesign, que podría causar que muchos modelos se rompan con los cambios de parámetros. Por lo tanto, ahora se recomienda evitar el mapeo de bocetos en las caras siempre que sea posible.


</div>

-   Nuevas funciones aditivas y sustractivas: [ Primitives](PartDesign_CompPrimitiveAdditive.md), [ Loft](PartDesign_AdditiveLoft.md), [ Sweep](PartDesign_AdditivePipe.md), [ Thickness](PartDesign_Thickness.md).

-   Nuevas características de referencia, [ planes](PartDesign_Plane.md), [ líneas](PartDesign_Line.md) y [ puntos](PartDesign_Point.md) son útiles para colocar sketches, alineación y servir como ejes de revolución.

-   Nueva conmutación automática del banco de trabajo entre PartDesign y Sketcher. Al crear un nuevo boceto desde el entorno de trabajo de PartDesign, una vez que se establece el archivo adjunto de boceto, la interfaz de usuario cambia automáticamente al banco de trabajo de Sketcher y sus herramientas en el modo de edición. Cuando se cierra el boceto, la interfaz de usuario vuelve al banco de trabajo de PartDesign y restaura la vista a su estado anterior. Por lo tanto, las herramientas de Sketcher se eliminaron de las barras de herramientas de PartDesign para liberar espacio para las nuevas características de PartDesign.

## Ambiente de Trabajo Path 

El Ambiente de trabajo Path se ha revisado de forma masiva en la versión 0.17. La revisión general vio la eliminación de todos los códigos HeeksCNC más antiguos y el reemplazo de la envoltura de la libraría python con el nuevo módulo de Path-Area. Como resultado, las operaciones se han vuelto mucho más poderosas, más rápidas, con una base de código simplificada.


<div class="mw-translate-fuzzy">

-   El soporte para operaciones 2.5D está completo, incluidos [ contour](Path_Profile.md), [ face-milling](Path_MillFace.md), [ pocketing](Path_Pocket_Shape.md), [ perfiling](Path_Profile.md), y [ drilling](Path_Drilling.md).


</div>

-   Soporte limitado para operaciones [ 3D pocketing](Path_Pocket_3D.md).

-   Path puede usar [Arch Panel](Arch_Panel.md) como objeto base para agrupar varias partes para el corte 2D.

-   Introducción de [Path Job](Path_Job.md). El \"Job\" ahora es un objeto central del flujo de trabajo de path. Organiza y coordina múltiples operaciones, herramientas, material de stock, orientación de partes y alineación. Un Job personalizado puede guardarse como una \'Plantilla de trabajo\' y reutilizarse para simplificar la configuración de trabajos futuros. Job SetupSheets proporciona un mecanismo para automatizar la configuración de la profundidad y la configuración de velocidad.

-   Todas las operaciones tienen una consistente organización del panel de tareas

-   [ post-processors](Path_Post.md) nuevos o mejorados para LinuxCNC, Smoothieboard, GRBL, Phillips, OpenSBP (shopbot), Roland Modela, Centroid, Fablin y Dynapath. La mayoría de los postprocesadores admiten argumentos.

-   Mejorado [ tool library](Path_ToolLibraryEdit.md) y editor.

-   La herramienta [Path Inspect](Path_Inspect.md) permite resaltar comandos individuales para visualizar la ruta y explorar gcode.

-   La herramienta [Path Simulator](Path_Simulator.md) realiza un corte simulado en 3D para visualizar la ejecución de Path.

-   Las operaciones de Dress-up pueden usarse para refinar las operaciones principales y agregar complejidad adicional. Existen Dressups para [ \'dogbone\'](Path_DressupDogbone.md) corners, [ etiquetas de retención](Path_DressupTag.md), [ ramp entry](Path_DressupRampEntry.md), y [ dragknife](Path_DressupDragKnife.md) \'corner actions\'

## Ambiente de Trabajo Sketcher 

-   Los sketches ahora pueden adjuntarse en una amplia variedad de formas, no solo para caras planas como solían ser. De particular importancia es el accesorio perpendicular a los bordes, útil para hacer perfiles para [sweeping](Part_Sweep.md).

-   Los enlaces de geometría externa ya no están limitados solo al objeto al que se asigna el croquis. La geometría de otros bocetos es compatible. Los enlaces de geometría externa se pueden crear dentro de un Part container, o un contenedor Body, o incluso un proyecto completo si no se usan contenedores de Part y Body.

-   Automatización de visibilidad: ahora, cuando comienza a editar un sketch, los objetos que dependen de él se ocultan automáticamente para despejar la vista, y los objetos utilizados para los enlaces de geometría externos se muestran automáticamente; las visibilidades antiguas se restauran al cerrar el sketch.

-   Nuevo modo de creación continua de restricción: las herramientas de restricción ahora están activas incluso sin ningún elemento seleccionado. Presione una restricción, luego seleccione los objetos para aplicar la restricción.

-   Nuevo arco de hipérbola y arco de herramientas de creación de parábolas.

-   Nueva herramienta de edición de Extend bordes .

-   Nueva herramienta de creación B-spline, con muchas formas de controlar curvas (grado, multiplicidad de nudos, punto de control del peso) e información de visualización (polígono de control, cresta de curvatura, indicador de multiplicidad de nudos).

![](images/FC017_Sketcher_B-spline_01.png )

-   Nueva herramienta **Carbon Copy** para copiar la geometría de otro sketch.

-   El espacio virtual cambia todas las restricciones a un \"espacio virtual\" diferente, de hecho, los oculta de la vista.

-   La caja de Constraints List incluye la capacidad de ocultar la alineación interna, así como el ocultamiento individual de las restricciones con una casilla de verificación.

-   El Block constrain elimina todos los grados de libertad para un elemento de geometría en el lugar con el uso de una única restricción. Debería ser particularmente útil trabajar con B-Splines, que son engorrosos de restringir.

-   Nuevo polígono regular con número de lados definido por el usuario.

-   Solucionadores de bosquejos alternativos disponibles a través de \"Mostrar control de solucionador avanzado en la barra de tareas\" en las preferencias de Sketcher.

-   Geometry style based rendering order permite reordenar entre geometría normal, de construcción y externa. Útil cuando este tipo de geometría se superpone.

-   Ahora, el solver sustituye automáticamente una combinación de restricción coincidente + tangente con una restricción tangente punto a punto, ya que el primero es un uso incorrecto que induce un error de tolerancia que puede causar problemas adicionales en el modelo. El usuario es advertido de la sustitución por un cuadro de diálogo que se puede desactivar en las preferencias de Sketcher desactivando \"Notificar sustituciones de restricciones automáticas\".

-   Nueva casilla de verificación en la vista de tareas del modo de edición \"Evitar restricciones automáticas redundantes\"

-   Las restricciones horizontales y verticales se pueden usar para alinear los puntos seleccionados.

## Ambiente de Trabajo Spreadsheet 

-   Se agregó un importador de archivos de Excel.

## Ambiente de Trabajo Surface 

-   Una nueva adición en v0.17, el Ambiente de trabajo Surface (por ahora) tiene 4 comandos de creación de superficie.

## Ambiente de Trabajo TechDraw 


<div class="mw-translate-fuzzy">

[ TechDraw](TechDraw_Workbench.md) es un nuevo ambiente de trabajo para la creación de dibujos técnicos que tiene como objetivo reemplazar el viejo ambiente de trabajo Drawing. FreeCAD v0.17 todavía incluye el ambiente de trabajo Drawing, por lo que aún puede abrir y editar sus archivos que contienen páginas de Drawing, pero Drawing se eliminará en una versión futura. Algunas de las cosas nuevas y emocionantes que TechDraw trae:


</div>

-   La mayoría de las herramientas del Ambiente de trabajo Drawing tienen una contraparte de TechDraw.
-   Creación y manipulación de vistas más fáciles. Las vistas se pueden tomar por su borde con el mouse y arrastradas por la página. La alineación de vistas ortogonales se puede bloquear.
-   Mejor gestión del tipo de línea (duro, suave, iso, costura). Mejor eliminación de línea oculta gracias a una biblioteca actualizada [ OCC](Glossary_#_OCC.md).
-   Vista de sección, creación de vista de detalle.
-   Mejor gestión de plantillas.
-   Dimensionamiento ahora es compatible, a través de herramientas de múltiples dimensiones: horizontal, vertical, longitud, radial, diámetro, angular.
-   Herramientas de decoración: hatching, hatching compatible con la especificación Autodesk PAT, símbolos, imágenes.

## Módulos Adicionales 

Algunos de los nuevos módulos de comunidad que se crearon.

-   [ Manipulator Workbench](Manipulator_Workbench.md) está destinado a ayudar en la alineación, movimiento, rotación y medición de objetos 3D (Part Design permitido) a través de una interfaz gráfica de usuario amigable.

-   [Curves](https://github.com/tomate44/CurvesWB), una colección de herramientas para crear y editar curvas y superficies NURBS [NURBS](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline).

-   [Nurbs](https://github.com/microelly2/freecad-nurbs), una colección de scripts para gestionar superficies y curvas de forma libre.

-   [Silk](https://github.com/edwardvmills/Silk), una colección de herramientas de modelado de superficies NURBS enfocadas en bajo grado y continuidad de costura.

-   [ Flamingo Workbench](Flamingo_Workbench.md), un conjunto de comandos y objetos personalizados de FreeCAD que ayudan a acelerar el dibujo de marcos y tuberías.

-   [ Ambiente de Trabajo para Ingeniería civil / transporte](Civil_Engineering_Workbench.md)

-   [GDT](https://github.com/juanvanyo/FreeCAD-GDT), dimensionamiento geométrico y tolerancias (GD & T).

-   [InventorLoader](https://github.com/jmplonka/InventorLoader) para importar archivos de Autodesk Inventor (en desarrollo).

-   [Kicad StepUp Workbench](https://www.freecadweb.org/wiki/KicadStepUp_Workbench) está destinado a ayudar a los usuarios de KiCad y FreeCAD en la colaboración ECAD y MCAD.

_ _ _

---
[documentation index](../README.md) > [News](Category_News.md) > Release notes 0.17/es

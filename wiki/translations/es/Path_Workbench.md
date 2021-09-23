# Path Workbench/es





<img alt="El icono del Ambiente de trabajo Trayectoria" src=images/Workbench_Part.svg  style="width:128px;">


{{TOCright}}

## Introducción


<div class="mw-translate-fuzzy">

El <img alt="" src=images/Workbench_Path.svg  style="width:24px;"> [Ambiente de trabajo Trayectoria](Path_Workbench/es.md) es usado para producir instrucciones maquina para [maquinas CNC](https://en.wikipedia.org/wiki/CNC_router) a partir de un modelo 3D FreeCAD. Estos producen objetos 3D reales en maquinas CNC tales como fresadoras, tornos, cortadoras laser, o similares.Tipicamente, estas instruciones son dialeto de tipo [código G](https://es.wikipedia.org/wiki/G-code).


</div>

<img alt="" src=images/pathwb.png  style="width:600px;">


<div class="mw-translate-fuzzy">

El flujo de trabajo del ambiente de trabajo Trayectoria crea estas instrucciones maquina como sigue:

-   Un modelo 3D es la base del objeto, tipicamente creado utilizando uno o más de los bancos de trabajo [Diseño de parte](PartDesign_Workbench/es.md), [Parte](Part_Workbench/es.md) o [Boceto](Draft_Workbench/es.md).
-   Un [Objeto trabajo](Path_Job/es.md) es creado en el banco de trabajo Trayectoria. Este contiene toda la información necesaria para generar el código G para procesarlo el trabajo sobre una maquina CNC:Eso es material stock, la maquina de mecanizado tiene un cierto [Conjunto de herramientas](Path_ToolLibraryEdit/es.md) y estos siguen cierto comandos de control de velocidad y movimientos (Usualmente codigo G).
-   Herramientas son seleccionadas como son requeridas por las operaciones de trabajo.
-   Trayectorias de mecanizado son creadas utilizando por ejemplo, operaciones [Contorno](Path_Profile.md) and [Vaciado](Path_Pocket_3D.md). Esos [Objectos trayectoria](Path_objects.md) utilizan una dialecto de código G el cual es independiente de la maquina CNC.
-   Exporte el trabajo con un código G, que coincida con su máquina.

Este paso se denomina *postprocesamiento*; hay diferentes postprocesadores disponibles.


</div>

## General concepts 


<div class="mw-translate-fuzzy">

## Conceptos generales 

El ambiente de trabajo Trayectoria genera el codigo G definiendo las trayectorias requeridas para mecanizar el proyecto representado por el modelo 3D al mecanizado objetivo dentro del [el dialeto del código G de las operaciones de ruta de FreeCAD](Path_scripting#The_FreeCAD_Internal_GCode_Format/es.md), el cual luego es traducida al apropiado dialeto para el controlador CNC seleccionando el pos procesador apropiado. El código G generado de directivas y operaciones contenidas en el objecto trabajo. El flujo de trabajo lista estos en el orden que seran ejecutados. La lista esta poblada por operaciones agregar trayectorias, enmascarado de trayectorias, comandos parciales de trayectorias y modificacion de trayectorias del menu de trayectoria o botones GUI.


</div>

The G-code is generated from directives and Operations contained in a Path Job. The Job Workflow lists these in the order they will be executed. The list is populated by adding Path Operations, Path Dressups, Path Supplemental Commands, and Path Modifications from the Path Menu, or GUI buttons.


<div class="mw-translate-fuzzy">

El banco de trabajo Trayectoria provee un administrador de herramientas (Biblioteca, Tabla de herramientas), inspector de código G y herramientas de simulación. Conectan el pos procesador y permiten importar y exportar plantillas de trabajos.


</div>


<div class="mw-translate-fuzzy">

Path Workbench tiene dependencias externas que incluyen:

1.  Las unidades del modelo 3D de FreeCAD se definen en la **Editar → Preferencia → General → Configuración de unidades de la pestaña Unidades**. La configuración del postprocesador define las unidades finales de código G.
2.  La ruta del archivo de macros, y las tolerancias geométricas, se definen en la pestaña **Editar → Preferencias → Ruta → Preferencias de trabajo** ficha.
3.  Los colores se definen en la pestaña **Editar → Preferencias → Ruta → Colores de ruta** ficha.
4.  Los parámetros de etiqueta de retención se definen en la pestaña **Editar → Preferencias → Ruta → Adelantos** ficha.
5.  Que la calidad del modelo 3D base soporte los requisitos del ambiente de trabajo Trayectoria, pasa a comprobar la geometría.


</div>

## Limitaciones

Some current limitations of which you should be aware are:

-   Most of the Path Tools are not true 3D tools but only 2.5D capable. This means that they take a fixed 2D shape and can cut it down to a given depth. However, there are two tools which produce true 3D paths: **<img src="images/Path_3DPocket.svg" width=24px> [3D Pocket](Path_Pocket_3D.md)** and **<img src="images/Path_3DSurface.svg" width=24px> [3D Surface](Path_3DSurface.md)** (which is still an [experimental feature](Path_experimental.md) as of November 2020).
-   Most of Path workbench is designed for a simple, standard 3-axis (xyz) CNC mill/router, but lathe tools are under development in 0.19\_pre.
-   Most operations in Path workbench will return paths based on a standard endmill tool/bit only, regardless of the tool/bit type assigned in a given tool controller with the exception of the **<img src="images/Path_Engrave.svg" width=24px> [Engrave](Path_Engrave.md)** and **<img src="images/Path_3DSurface.svg" width=24px> [3D Surface](Path_3DSurface.md)** operations.
-   The operations within the Path workbench are not aware of clamping mechanisms in use to secure the model to your machine. Consequently, please review and simulate the paths you generate prior to sending the code to your machine. If necessary, model your clamping mechanisms in FreeCAD in order to better inspect the paths generated. Look for possible collisions with clamps or other obstacles along the paths.

## Unidades

El manejo de unidades en Path puede ser confuso. Hay varios puntos para entender:

1.  Las unidades base de FreeCAD para longitud y tiempo son \'mm\' y \'s\' respectivamente. La velocidad es así \'mm / s\'. Esto es lo que FreeCAD almacena internamente independientemente de cualquier otra cosa
2.  El esquema de unidad predeterminado usa las unidades predeterminadas. Si está utilizando el esquema predeterminado e ingresa una velocidad de avance sin una cadena de unidades, se ingresará como \'mm / s\'
3.  La mayoría de las máquinas CNC esperan una velocidad de avance en forma de \'mm / min\' o \'in / min\'. La mayoría de los procesadores posteriores convertirán automáticamente la unidad cuando generen gcode.

Schemas:

1.  El cambio de esquema en las preferencias cambia la cadena de unidad predeterminada para los campos de entrada. Si usted es un usuario de Path y prefiere diseñar en métricas, es muy recomendable que use el esquema \"Metric Small Parts & CNC\". Si diseñas en unidades de EE. UU., Ya sea el decimal imperial o el Building US funcionarán
2.  Cambiar el esquema de su unidad preferida no tendrá ningún efecto en la salida, pero ayudará a evitar errores de entrada

Salida:

1.  La generación de la unidad correcta en la salida es responsabilidad del postprocesador y solo se realiza en ese momento.
2.  La unidad de salida de la máquina no está relacionada con el esquema de la unidad seleccionada
3.  Los postprocesadores producen salida métrica (G21), salida Imperial (G20) o son configurables.
4.  Post-procesadores configurables por defecto a la métrica (G21)
5.  Si desea que su post-procesador configurable emita gcode imperial (G20), establezca el argumento correcto en la confluencia de salida de su trabajo (es decir, \--inches for linuxcnc). Esto puede almacenarse en una plantilla de trabajo y establecerse como su plantilla predeterminada para que sea automática para todos los trabajos futuros.

Inspección de Path:

1.  Si usa la herramienta Path Inspect para ver el gcode, lo verá en \'mm / s\' porque no está siendo procesado

## Heights and depths 


<div class="mw-translate-fuzzy">

## Comandos de Trayectoria 

Muchos de los comandos tienen varias alturas y profundidades: <img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Referencia visual para las propiedades de profundidad (ajustes)*


</div>

<img alt="" src=images/Path-DepthsAndHeights.gif  style="width:500px;"> 
*Visual reference for Depth properties (settings)*

## Commands

Some commands are experimental and not available by default. To enable them see [Path experimental](Path_experimental.md).

### Project Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Job.svg  style="width:32px;"> [Trabajo](Path_Job/es.md): Crea un nuevo trabajo CNC.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_PostProcess.svg  style="width:32px;"> [Post Process](Path_Post/es.md): Exporta un proyecto a código G.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Sanity.svg  style="width:32px;"> [Errores de trayectoria](Path_Sanity/es.md): Revisa el trabajo seleccionado por valores faltantes.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_ExportTemplate.svg  style="width:32px;"> [Exportar plantilla](Path_ExportTemplate/es.md): Exporta el actual trabajo como plantilla.


</div>

### Tool Commands 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Inspect.svg  style="width:32px;"> [Inspector de código G](Path_Inspect/es.md): Muestra el código G para revisión.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Simulator.svg  style="width:32px;"> [Simulador](Path_Simulator/es.md): Muestra la operación de mecanizado como si estuviera hecha sobre la maquina.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_CompleteLoop.svg  style="width:32px;"> [Completar ciclo](Path_SelectLoop/es.md): Completa un ciclo a partir de dos esquinas seleccionadas


</div>

-   <img alt="" src=images/Path_OpActiveToggle.svg  style="width:32px;"> [Toggle the Active State of the Operation](Path_OpActiveToggle.md): Activates or de-activates a path operation.

-   <img alt="" src=images/Path_ToolBitLibraryOpen.svg  style="width:32px;"> [ToolBit Library editor](Path_ToolBitLibraryOpen.md): Opens an editor to manage ToolBit libraries. <small>(v0.19)</small> 

-   <img alt="" src=images/Path_ToolBitDock.svg  style="width:32px;"> [ToolBit Dock](Path_ToolBitDock.md): Toggles the ToolBit Dock. <small>(v0.19)</small> 

### Basic Operations 

-   <img alt="" src=images/Path_Profile.svg  style="width:32px;"> [Profile](Path_Profile.md): Creates a profile operation of the entire model, or from one or more selected faces or edges. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Pocket.svg  style="width:32px;"> [Vaciado](Path_Pocket_Shape/es.md): Crea una operación de vaciado a partir de uno o mas hueco(s) seleccionados.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Drilling.svg  style="width:32px;"> [Perforado](Path_Drilling/es.md): Ejecuta un ciclo de perforado.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Face.svg  style="width:32px;"> [Mecanizado de cara](Path_MillFace/es.md): Crea una trayectoria superficial.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Helix.svg  style="width:32px;"> [Helix](Path_Helix/es.md): Crea una trayectoria helicoidal.


</div>

-   <img alt="" src=images/Path_Adaptive.svg  style="width:32px;"> [Adaptive](Path_Adaptive.md): Creates an adaptive clearing and profiling operation.

-   <img alt="" src=images/Path_Slot.svg  style="width:32px;"> [Slot](Path_Slot.md): Creates a slotting operation from selected features or custom points. [**Experimental**](Path_experimental.md). <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Engrave.svg  style="width:32px;"> [Grabado](Path_Engrave/es.md): Crea una trayectoria de grabado.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Vcarve.svg  style="width:32px;"> [TallarV](Path_Vcarve/es.md): Crea una trayectoria para una cavidad 3D


</div>

### 3D Operations 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_3DPocket.svg  style="width:32px;"> [Vaciado 3D](Path_Pocket_3D/es.md): Crea una trayectoria para un vaciado 3D.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_3DSurface.svg  style="width:32px;"> [Superficie 3D](Path_Surface/es.md): Crea una trayectoria para una superficie 3D


</div>

-   <img alt="" src=images/Path_Waterline.svg  style="width:32px;"> [Waterline](Path_Waterline.md): Creates a waterline path for a 3D surface. [**Experimental**](Path_experimental.md). <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

### Enmascarado Trajectoria 


</div>

-   <img alt="" src=images/Path_DressupPathBoundary.svg  style="width:32px;"> [Boundary Dressup](Path_DressupPathBoundary.md): Adds a boundary dressup modification to a selected path.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Dressup.svg  style="width:32px;"> [Enmascarado hueso de perro](Path_DressupDogbone/es.md): Agrega una modificación de enmascarado hueso de perro a la trayectoria seleccionada.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupDragKnife.svg  style="width:32px;"> [Enmascarado Arrastre de cuchilla](Path_DressupDragKnife/es.md): Agrega una modificación de enmascarado arrastre de cuchilla a la trayectoria seleccionada.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupLeadInOut.svg  style="width:32px;"> [Lead In Dressup](Path_DressupLeadInOut/es.md): Agrega un punto de entrada y / o salida a una ruta seleccionada


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupRampEntry.svg  style="width:32px;"> [Enmascarado entrada en rampa](Path_DressupRampEntry/es.md): Agrega una modificación de enmascarado entrada en rampa a la trayectoria seleccionada.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_DressupTag.svg  style="width:32px;"> [Tag Dressup](Path_DressupTag/es.md): Agrega una modificación de tarjeta de espera a una ruta seleccionada


</div>


<div class="mw-translate-fuzzy">

### Comandos parciales 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Fixture.svg  style="width:32px;"> [Fixtura](Path_Fixture/es.md): Cambia la posición de la fixtura.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Comment.svg  style="width:32px;"> [Comentar](Path_Comment/es.md): Inserta un comentario en el código G de una trayectoria


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Stop.svg  style="width:32px;"> [Detener](Path_Stop/es.md): Inserta un paro total de la maquina.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Custom.svg  style="width:32px;"> [Personalizar](Path_Custom/es.md): Inserta código G personalizado.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Shape.svg  style="width:32px;"> [Código G de un forma](Path_Shape/es.md): Crea un objecto trayectoria a partir de un objecto parte seleccionado.


</div>


<div class="mw-translate-fuzzy">

### Modificación de trayectoria 


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Copy.svg  style="width:32px;"> [Copiar](Path_Copy/es.md): Crea una copia parametrica de un objecto trayectoria seleccionado


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Array.svg  style="width:32px;"> [Arreglo](Path_Array/es.md): Crea un arreglo duplicando una trayectoria seleccionada


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_SimpleCopy.svg  style="width:32px;"> [Copia simple](Path_SimpleCopy/es.md): Crea una copia no paramétrica de un objecto trayectoria seleccionado.


</div>

### Miscellaneous


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Area.svg  style="width:32px;"> [Área característica](Path_Area/es.md): Crea un área característica a partir de los objetos seleccionados.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_Area_Workplane.svg  style="width:32px;"> [Plano de trabajo de área característica](Path_Area_Workplane/es.md): Crea un plano de trabajo de área característica.


</div>

### Obsolete


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Path_ToolLibraryEdit.svg  style="width:32px;"> [Administrador de herramientas](Path_ToolLibraryEdit/es.md): Edita el administrador de herramientas.


</div>

## ToolBit architecture 

Manage tools, bits, and the Tool Library. Based on the ToolBit architecture. <small>(v0.19)</small> 

-   [Path Tools](Path_Tools.md)
-   [Path ToolShape](Path_ToolShape.md)
-   [Path ToolBit](Path_ToolBit.md)
-   [Path ToolBit Library](Path_ToolBit_Library.md)
-   [Path ToolController](Path_ToolController.md)

## Other


<div class="mw-translate-fuzzy">

El ambiente de trabajo comparte muchos conceptos con otros paquetes de programas CAM pero tienen sus propias peculiaridades. Si algo va mal, este es un buen lugar para empezar.


</div>


<div class="mw-translate-fuzzy">

### Preferencias


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Preferencias\...](Path_Preferences/es.md): Preferencias desechables en herramientas de ruta.


</div>

## Archivos de guión 

See [Path scripting](Path_scripting.md).

## Tutorials

-   [Path Walkthrough for the Impatient](Path_Walkthrough_for_the_Impatient.md): a quick tutorial to get familiar with Path.

## Videos

-   [FreeCAD Path: Custom paths with Python - Part 1 - 5](https://www.youtube.com/playlist?list=PLEuOia-QxyFKgzAeTyH62GKqWKVURiWJL): a playlist with a series of 5 videos in English by sliptonic. This series shows how to work with the [Path Workbench](Path_Workbench.md).
-   [FreeCAD CAM Path Workbench](https://www.youtube.com/playlist?list=PLUrr_kHPp4vhGdLlj6IemtF-OPUlRvSTC): a playlist with a series of 7 videos in English by CAD CAM Lessons.
-   [FreeCAD CAM CNC](https://www.youtube.com/playlist?list=PLUrr_kHPp4vh2n6DcIlegK4dEKIFjmISJ) a playlist with a series of 8 videos in English by CAD CAM Lessons.





{{Path_Tools_navi

}} 

[Category:Workbenches](Category:Workbenches.md)

# Release notes 1.0/es
**FreeCAD 1.0 está en desarrollo, todavía no hay fecha de lanzamiento.**


{{Message|
¿Faltan características? Menciónelas en el hilo del foro [https   *//forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;69438 Notas de la versión v1.0].

Vea [Ayuda a FreeCAD](Help_FreeCAD/es.md) para ver formas de como contribuir a FreeCAD.
}}


{{Message|Todas la imágenes en esta página deben usar el sufijo **_relnotes_1.0**}}


{{TOCright}}

**FreeCAD 1.0** fue liberado el **DD de Mes del 2023**, consíguelo desde la página [Descarga](Download/es.md). Este es un resumen de las nuevas características y los cambios más interesantes.

Las notas de lanzamiento de versiones anteriores de FreeCAD se pueden encontrar en la [Lista de características](Feature_list/es#Notas_de_lanzamiento.md).

Marcador de posición para una imagen llamativa seleccionada por los administradores de [el foro de exhibición de usuarios](https   *//forum.freecadweb.org/viewforum.php?f=24).

## Generalidades

## Interfaz de usuario 

   
  <img alt="" src=images/Measurement-Part_relnotes_1.0.png  style="width   *384px;">   The display style of [measurement](Part_Workbench#Measure.md) results created using the [Part](Part_Workbench.md) or [PartDesign](PartDesign_Workbench.md) workbench can now be changed in the [preferences](PartDesign_Preferences#Measure.md). [Pull request #7148](https   *//github.com/FreeCAD/FreeCAD/pull/7148)
   

### Otras mejoras de la interfaz de usuario 

-   It is now possible to set a default transparency for new [Part](Part_Module.md) or [PartDesign](PartDesign_Workbench.md) objects in the [Preferences](PartDesign_Preferences.md). [Pull request #7103](https   *//github.com/FreeCAD/FreeCAD/pull/7103)
-   A button has been added to switch the colors of the [3D view](3D_view.md) background gradient in the [Preferences](Preferences_Editor#Colors.md). [Pull request #7155](https   *//github.com/FreeCAD/FreeCAD/pull/7155)
-   Commands to [store](Std_StoreWorkingView.md) and [recall](Std_RecallWorkingView.md) a temporary working view have been added. [Pull request #7525](https   *//github.com/FreeCAD/FreeCAD/pull/7525)
-   Value changes with the mouse wheel in \'input fields\' (a widget type used to enter values in task panels, for example by [Draft Line](Draft_Line.md)) are disabled if the widget doesn\'t have the focus and the [ComboBoxWheelEventFilter](Fine-tuning.md) switch is enabled. This prevents unwanted value changes while scrolling, as already was the case for spin and combo boxes. [request #7561](https   *//github.com/FreeCAD/FreeCAD/pull/7561%7CPull)
-   The toolbar button for [Edit Mode](Std_UserEditMode.md) has been removed. [Pull request #7570](https   *//github.com/FreeCAD/FreeCAD/pull/7570)
-   The toolbar buttons for [Print](Std_Print.md), [Copy](Std_Copy.md), [Paste](Std_Paste.md) and [Cut](Std_Cut.md) have been removed. [Pull request #7571](https   *//github.com/FreeCAD/FreeCAD/pull/7571) and [commit ea9a04e](https   *//github.com/FreeCAD/FreeCAD/commit/ea9a04e)

## Núcleo del sistema y API 

### Núcleo

### API


<div class="mw-collapsible mw-collapsed toccolours">

#### Nueva API de Python 


<div class="mw-collapsible-content">

-   *BSplineSurfacePy   *   *scaleKnotsToBounds*   * Scales the U and V knots lists to fit the specified bounds. [Pull request #7258](https   *//github.com/FreeCAD/FreeCAD/pull/7258) and [Pull request #7385](https   *//github.com/FreeCAD/FreeCAD/pull/7385)
-   *BSplineCurvePy   *   *scaleKnotsToBounds*   * Scales the knots list to fit the specified bounds. [Pull request #7385](https   *//github.com/FreeCAD/FreeCAD/pull/7385)

-   *ShapeFix_EdgeConnectPy*   * Clase raíz para arreglar operaciones. [commit 4d4adb93](https   *//github.com/FreeCAD/FreeCAD/commit/4d4adb93)
-   *ShapeFix_EdgePy*   * Arreglar borde inválido. [commit 4089cbfb](https   *//github.com/FreeCAD/FreeCAD/commit/4089cbfb)
-   *ShapeFix_FaceConnectPy*   * Reconstruye la conectividad entre caras en un cascarón. [commit a0eb2e9d](https   *//github.com/FreeCAD/FreeCAD/commit/a0eb2e9d)
-   *ShapeFix_FacePy*   * Class for fixing operations on faces. [commit b6cd635c](https   *//github.com/FreeCAD/FreeCAD/commit/b6cd635c)
-   *ShapeFix_FixSmallFacePy*   * Class for fixing operations on faces. [commit 4c2946c8](https   *//github.com/FreeCAD/FreeCAD/commit/4c2946c8)
-   *ShapeFix_FixSmallSolidPy*   * Fixing solids with small size. [commit b70d8d37](https   *//github.com/FreeCAD/FreeCAD/commit/b70d8d37)
-   *ShapeFix_FreeBoundsPy*   * Intended to output free bounds of the shape. [commit 1ee1aee1](https   *//github.com/FreeCAD/FreeCAD/commit/1ee1aee1)
-   *ShapeFix_RootPy*   * Root class for fixing operations. [commit f3e941a3](https   *//github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix_ShapePy*   * Class for fixing operations on shapes. [commit 87db9dcc](https   *//github.com/FreeCAD/FreeCAD/commit/87db9dcc)
-   *ShapeFix_ShapeTolerancePy*   * Modifies tolerances of sub-shapes (vertices, edges, faces). [commit 125d5b63](https   *//github.com/FreeCAD/FreeCAD/commit/125d5b63)
-   *ShapeFix_ShellPy*   * Root class for fixing operations. [commit f3e941a3](https   *//github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix_SolidPy*   * Root class for fixing operations. [commit 8d568793](https   *//github.com/FreeCAD/FreeCAD/commit/8d568793)
-   *ShapeFix_SplitCommonVertexPy*   * Class for fixing operations on shapes. [commit 4b44c54c](https   *//github.com/FreeCAD/FreeCAD/commit/4b44c54c)
-   *ShapeFix_SplitToolPy*   * Tool for splitting and cutting edges. [commit bbecc3f2](https   *//github.com/FreeCAD/FreeCAD/commit/bbecc3f2)
-   *ShapeFix_WireframePy*   * Provides methods for fixing wireframe of shape. [commit 6843a461](https   *//github.com/FreeCAD/FreeCAD/commit/6843a461)
-   *ShapeFix_WirePy*   * Class for fixing operations on wires. [commit 94f6279a](https   *//github.com/FreeCAD/FreeCAD/commit/94f6279a)
-   *ShapeFix_WireVertexPy*   * Fixing disconnected edges in the wire. [commit 8c6ffc99](https   *//github.com/FreeCAD/FreeCAD/commit/8c6ffc99)


</div>

#### API de Python eliminada 

-   *FreeCAD.EndingAdd*   * replaced by *FreeCAD.addImportType*. [Pull request #7167](https   *//github.com/FreeCAD/FreeCAD/pull/7167)
-   *FreeCAD.EndingGet*   * replaced by *FreeCAD.getImportType*. [Pull request #7167](https   *//github.com/FreeCAD/FreeCAD/pull/7167)


</div>

## Gestor de complementos 

## Ambiente de Trabajo Arch 

### Otras mejoras de Arch 

-   Los objetos [Perfil](Arch_Profile.md) ahora soportan modificaciones del tipo de perfil después de su creación. [Pull request #7217](https   *//github.com/FreeCAD/FreeCAD/pull/7217)

## Ambiente de Trabajo Draft 

-   The inaccuracy of [Draft Snap Near](Draft_Snap_Near.md) when snapping to curves was fixed. In addition, [Draft Snap Perpendicular](Draft_Snap_Perpendicular.md) can now also snap to faces and find multiple points. To snap to a vertex (e.g. a [Draft Point](Draft_Point.md)) [Draft Snap Endpoint](Draft_Snap_Endpoint.md) must now be used instead of [Draft Snap Near](Draft_Snap_Near.md). [Pull request #7132](https   *//github.com/FreeCAD/FreeCAD/pull/7132)
-   To make working with [layers](Draft_Layer.md) easier their drag and drop behavior was modified. If you drop an object from a [Std Group](Std_Group.md), or a group-like object such as an [Arch BuildingPart](Arch_BuildingPart.md), on a layer, it is no longer removed from the group, and vice versa. This works without holding down the **Ctrl** key. [Pull request #7462](https   *//github.com/FreeCAD/FreeCAD/pull/7462)
-   The [Draft PointArray](Draft_PointArray.md) command now supports more point object types. Any object with a shape and vertices, as well as a [mesh](Mesh_Workbench.md) and a [point cloud](Points_Workbench.md) can be used. [Pull request #7597](https   *//github.com/FreeCAD/FreeCAD/pull/7597)

### Otras mejoras de Draft 

-   Several [Draft PathArray](Draft_PathArray.md) related issues have been fixed. [Pull request #7506](https   *//github.com/FreeCAD/FreeCAD/pull/7506)
-   The [Draft Edit](Draft_Edit.md) command has received several improvements. For [wires](Draft_Wire.md), [B-splines](Draft_BSpline.md) and [Bézier curves](Draft_BezCurve.md) a Close/Open option has been added to the edge context menu. For B-splines and Bézier curves a Reverse option has been added to the same menu as well. The task panels have been cleaned up. [Pull request #7527](https   *//github.com/FreeCAD/FreeCAD/pull/7527) and [Pull request #7541](https   *//github.com/FreeCAD/FreeCAD/pull/7541)

## Ambiente de Trabajo FEM 

   
  <img alt="" src=images/FEM_Elmer-Multithread_relnotes_1.0.png  style="width   *384px;">Simulation result where 8 mesh regions are visible (one for every CPU core used).   It is now possible to run the solver [Elmer](FEM_SolverElmer.md) using multiple CPU cores. For more info about the caveats, see [this forum post](https   *//forum.freecadweb.org/viewtopic.php?p=610617#p610617) [Pull request #7159](https   *//github.com/FreeCAD/FreeCAD/pull/7159)
   

### Otras mejoras de FEM 

-   There is now an <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width   *24px;"> [initial pressure constraint](FEM_ConstraintInitialPressure.md) to set the initial internal pressure of fluids. [Pull request #7364](https   *//github.com/FreeCAD/FreeCAD/pull/7364)
-   The <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width   *24px;"> [body heat source constraint](FEM_ConstraintBodyHeatSource.md) now has a task panel and it is possible to set the heat for several bodies or to use several constraints for different bodies in one analysis. [Pull request #7367](https   *//github.com/FreeCAD/FreeCAD/pull/7367)
-   It is now possible to open (and this way visualize) \*.pvtu files (partitioned VTK unstructured grid data). A \*.pvtu file is also the result of an [Elmer](FEM_SolverElmer.md) simulation, when more than one CPU core was used. [Pull request #7159](https   *//github.com/FreeCAD/FreeCAD/pull/7159)
-   Critical Strain Ratio has been added to the VTK result pipeline. It gives an indication of ductile rupture for materials with a \"MaterialMechanicalNonlinear\" object. [Pull request #7467](https   *//github.com/FreeCAD/FreeCAD/pull/7467)

## Exportar

## Malla

### Otras mejoras de Mesh 

## Ambiente de Trabajo OpenSCAD 

## Ambiente de Trabajo Part 

### Otras mejoras de Part 

## Ambiente de Trabajo PartDesign 

### Otras mejoras de PartDesign 

## Ambiente de Trabajo Path 

-   Integración de Camotics. Si Camotics (versión 1.2.2 o posterior) está instalado, se agregará un nuevo icono a la barra de herramientas de Path. Seleccione un Trabajo de Path y presione el botón para abrir el cuadro de diálogo de Camotics. Luego arrastre el control deslizante para generar un sólido simulado en cualquier momento del trabajo. También puede iniciar la aplicación Camotics por completo para ejecutar la simulación animada. Esto da como resultado un postprocesamiento silencioso del trabajo y la creación de un archivo de proyecto de Camotics. [Pull request #6637](https   *//github.com/freecad/freecad/pull/6637)

-   Cadenas de sustitución adicionales para nombres de salida automática. Si la salida se divide en múltiples archivos, los nombres de archivo pueden sustituir automáticamente la etiqueta toolcontroller, WCS o etiqueta de operación. Esto se suma a las otras cadenas de sustitución existentes como fecha, nombre del trabajo, etc.

-   Implemented Chipbreaking option for peck style drill cycles. Chipbreaking emits a G73 cycle which causes the control to make a very small retraction move to break the chip without fully retracting the bit from the hole. G73 is supported natively by LinuxCNC. Some other postprocessors will have to interpret the G73 and emit control appropriate codes or decompose the retraction into G1/G0 moves. Postprocessor support for G73 decomposition has been added to the \"refactored\" postprocessors.[Pull request #7469](https   *//github.com/FreeCAD/FreeCAD/pull/7469)

## Módulo Plot 

## Ambiente de Trabajo Sketcher 

   
  ![](images/sketcher-move-piece_relnotes_1.0.gif )   Dragging a B-spline now only moves the part between knots. [Pull request #7110](https   *//github.com/FreeCAD/FreeCAD/pull/7110)
                                                                                     
   

   
  ![](images/Sketcher_BackEdit_relnotes_1.0.gif )   Possibility to seamlessly edit sketches from the front or back. When working from the back, vertices (and all geometries and constraints) are equally selectable and the section view is switched automatically. [Pull request #7417](https   *//github.com/FreeCAD/FreeCAD/pull/7417)
                                                                                 
   

### Otras mejoras de Sketcher 

-   The toolbar button for [Constrain refraction (Snell\'s law)](Sketcher_ConstrainSnellsLaw.md) has been removed. [Commit ef62fc3](https   *//github.com/FreeCAD/FreeCAD/commit/ef62fc3)
-   The toolbar buttons for [Select redundant constraints](Sketcher_SelectRedundantConstraints.md) and [Select conflicting constraints](Sketcher_SelectConflictingConstraints.md) have been removed. [Pull request #7568](https   *//github.com/FreeCAD/FreeCAD/pull/7568)
-   The toolbar button for [Stop operation](Sketcher_StopOperation.md) has been removed. [Pull request #7569](https   *//github.com/FreeCAD/FreeCAD/pull/7569)
-   Edit Control widget, \'Grid size\' label removed, \'Show grid\' checkbox renamed \'Grid\'. [Pull request #7577](https   *//github.com/FreeCAD/FreeCAD/pull/7577)

## Ambiente de Trabajo Spreadsheet 

### Otras mejoras de Spreadsheet 

## Ambiente de Trabajo TechDraw 

   
  <img alt="" src=images/TechDraw_SurfaceFinishExample_relnotes_1.0.png  style="width   *384px;">   A new [SurfaceFinishSymbol](TechDraw_SurfaceFinishSymbol.md) tool was added to allow for the creation of surface finish symbols describing roughness, lay and waviness, but also denoting the type of surface treatment. It supports both ISO and ASME styles. As shown in the image, the existing [LeaderLine](TechDraw_LeaderLine.md) tool can be used to properly refer oriented symbols to the edges of an object. [Pull request #7227](https   *//github.com/FreeCAD/FreeCAD/pull/7227)
   

### Otras mejoras de TechDraw 

-   Support for adjustable gaps for extension lines of [dimensions](TechDraw_Preferences#Dimensions.md) was added. [Pull request #7133](https   *//github.com/FreeCAD/FreeCAD/pull/7133)
-   Removed deprecated functions   * DrawViewPart   *   *replaceCenterLine, DrawViewPart   *   *replaceCosmeticEdge, DrawViewPart   *   *replaceCosmeticVertex and DrawViewPart   *   *replaceGeomFormat.

## Web

## Ambientes de trabajo externos 

### A2plus

### Assembly3

### Assembly4

### FCGear

### Ship

## Compilación

Desde este lanzamiento FreeCAD solo va a poder ser compilado usando Qt 5.x y Python 3.x. La versión de Python más baja soportada es la 3.8 de acuerdo con las [metas de desarrollo de FreeCAD 1.0](FreeCAD_1.0_Development_Cycle.md).

Para compilar FreeCAD vea las instrucciones para [Windows](Compile_on_Windows.md), [Linux](Compile_on_Linux.md) y [MacOS](Compile_on_MacOS.md).

Los sistemas operativos soportados   *

-   Windows 7, 8, 10 y 11
-   Linux Ubuntu Focal Fossa (20.04) y nuevos
-   MacOS   * 10.12 Sierra o más nuevo

## Limitaciones conocidas 

#### Windows de 32bits 

Desde FreeCAD 0.19 no soportamos oficialmente Windows de 32 bits. FreeCAD podría funcionar en estos sistemas pero no se brinda soporte.

#### Escritorio remoto en Windows 

Dependiendo de las capacidades gráficas OpenGL de una computadora, podría ser que se encuentre un bloqueo cuando se ejecuta Freecad a través de un escritorio remoto. Para solucionar esto actualice su controlador OpenGL. Solo si esto no ayuda   *

-   Descargar [esta](https   *//downloads.fdossena.com/geth.php?r=mesa64-latest) biblioteca OpenGL para Windows de 64 bits y extraerla.
-   Cambie el nombre del archivo DLL a *OpenGL32SW.DLL* y cópielo a la subcarpeta *bin* de la carpeta de instalación de FreeCAD (sobrescriba el DLL existente allí).

### MacOS   * Entorno de trabajo Start Workbench muestra una página en blanco 

Si el [entorno de trabajo Start](Start_Workbench/es.md) muestra solo una página en blanco, debe de habilitar la opción **Usar OpenGL software** en el menú **Editar → Preferencias → Mostrar**.

[Category   *News](Category_News.md) [Category   *Documentation](Category_Documentation.md) [Category   *Releases](Category_Releases.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.0/es

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

### Otras mejoras de la interfaz de usuario 

## Núcleo del sistema y API 

### Núcleo

### API


<div class="mw-collapsible mw-collapsed toccolours">

#### Nueva API de Python 


<div class="mw-collapsible-content">

-   *ShapeFix\_EdgeConnectPy*   * Root class for fixing operations. [commit 4d4adb93](https   *//github.com/FreeCAD/FreeCAD/commit/4d4adb93)
-   *ShapeFix\_EdgePy*   * Fixing invalid edge. [commit 4089cbfb](https   *//github.com/FreeCAD/FreeCAD/commit/4089cbfb)
-   *ShapeFix\_FaceConnectPy*   * Rebuilds connectivity between faces in shell. [commit a0eb2e9d](https   *//github.com/FreeCAD/FreeCAD/commit/a0eb2e9d)
-   *ShapeFix\_FacePy*   * Class for fixing operations on faces. [commit b6cd635c](https   *//github.com/FreeCAD/FreeCAD/commit/b6cd635c)
-   *ShapeFix\_FixSmallFacePy*   * Class for fixing operations on faces. [commit 4c2946c8](https   *//github.com/FreeCAD/FreeCAD/commit/4c2946c8)
-   *ShapeFix\_FixSmallSolidPy*   * Fixing solids with small size. [commit b70d8d37](https   *//github.com/FreeCAD/FreeCAD/commit/b70d8d37)
-   *ShapeFix\_FreeBoundsPy*   * Intended to output free bounds of the shape. [commit 1ee1aee1](https   *//github.com/FreeCAD/FreeCAD/commit/1ee1aee1)
-   *ShapeFix\_RootPy*   * Root class for fixing operations. [commit f3e941a3](https   *//github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix\_ShapePy*   * Class for fixing operations on shapes. [commit 87db9dcc](https   *//github.com/FreeCAD/FreeCAD/commit/87db9dcc)
-   *ShapeFix\_ShapeTolerancePy*   * Modifies tolerances of sub-shapes (vertices, edges, faces). [commit 125d5b63](https   *//github.com/FreeCAD/FreeCAD/commit/125d5b63)
-   *ShapeFix\_ShellPy*   * Root class for fixing operations. [commit f3e941a3](https   *//github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix\_SolidPy*   * Root class for fixing operations. [commit 8d568793](https   *//github.com/FreeCAD/FreeCAD/commit/8d568793)
-   *ShapeFix\_SplitCommonVertexPy*   * Class for fixing operations on shapes. [commit 4b44c54c](https   *//github.com/FreeCAD/FreeCAD/commit/4b44c54c)
-   *ShapeFix\_SplitToolPy*   * Tool for splitting and cutting edges. [commit bbecc3f2](https   *//github.com/FreeCAD/FreeCAD/commit/bbecc3f2)
-   *ShapeFix\_WireframePy*   * Provides methods for fixing wireframe of shape. [commit 6843a461](https   *//github.com/FreeCAD/FreeCAD/commit/6843a461)
-   *ShapeFix\_WirePy*   * Class for fixing operations on wires. [commit 94f6279a](https   *//github.com/FreeCAD/FreeCAD/commit/94f6279a)
-   *ShapeFix\_WireVertexPy*   * Fixing disconnected edges in the wire. [commit 8c6ffc99](https   *//github.com/FreeCAD/FreeCAD/commit/8c6ffc99)


</div>

#### API de Python cambiada 


</div>

## Gestor de complementos 

## Ambiente de Trabajo Arch 

## Ambiente de Trabajo Draft 

### Otras mejoras de Draft 

## Ambiente de Trabajo FEM 

### Otras mejoras de FEM 

## Exportar

## Malla

### Otras mejoras de Mesh 

## Ambiente de Trabajo OpenSCAD 

## Ambiente de Trabajo Part 

### Otras mejoras de Part 

## Ambiente de Trabajo PartDesign 

### Otras mejoras de PartDesign 

## Ambiente de Trabajo Path 

-   Camotics integration. If camotics (version 1.2.2 or later) is installed, a new icon will be added to the Path toolbar. Select a Path Job and press the button to open the Camotics dialog. Then drag the slider to generate a simulated solid at any point in the job. You can also launch the full camotics application to run the animated simulaton. This results in a silent post-processing of the job and creation of a camotics project file. [Pull request \#6637](https   *//github.com/FreeCAD/FreeCAD/pull/6637)

-   Additional substitution strings for automatic output naming. If output is being split into multiple files, the filenames can automatically substitute the toolcontroller label, WCS, or operation label. This is in addition to the other existing substitution strings like date, job name, etc.

## Módulo Plot 

## Ambiente de Trabajo Sketcher 

### Otras mejoras de Sketcher 

## Ambiente de Trabajo Spreadsheet 

### Otras mejoras de Spreadsheet 

## Ambiente de Trabajo TechDraw 

### Otras mejoras de TechDraw 

## Web

## Ambientes de trabajo externos 

### A2plus

### Assembly3

### Assembly4

### FCGear

### Ship

## Compilación

Since this release FreeCAD can only be compiled using Qt 5.x and Python 3.x. The lowest supported Python version is 3.8 according to the [FreeCAD 1.0 development goals](FreeCAD_1.0_Development_Cycle.md).

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
-   Cambie el nombre del archivo DLL a \'\' OpenGL32SW.DLL \'\' y cópielo a la subcarpeta \'\' bin \'\' de la carpeta de instalación de FreeCAD (sobrescriba el DLL existente allí).

[Category   *News](Category_News.md) [Category   *Documentation](Category_Documentation.md) [Category   *Releases](Category_Releases.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.0/es

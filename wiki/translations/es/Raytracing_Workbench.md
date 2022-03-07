# Raytracing Workbench/es
**L' Ambiente de trabajo Trazado de rayos es esencialmente obsoleta. Un nuevo desarrollo está ocurriendo en el [https://github.com/FreeCAD/FreeCAD-render Render Ambiente de trabajo], que se pretende que sea su sustituto. Este Ambiente de trabajo está completamente programado en Python, así que es mucho más fácil de ampliar.

Nevertheless, the information in this page is generally useful for the new workbench, as both modules work basically in the same way.
**

<img alt="El icono del Ambiente de trabajo Trazado de rayos" src=images/Workbench_PartDesign.svg  style="width:128px;">

## Introducción


{{TOCright}}

El <img alt="" src=images/Workbench_Raytracing.svg  style="width:24px;"> [Ambiente de trabajo Trazado de rayos](Raytracing_Workbench/es.md) es usado para generar imágenes fotorealistas de tus modelos al renderizarlos con un renderizador externo.

El Ambiente de trabajo trazado de rayos opera con [plantillas](Raytracing_templates/es.md), que son archivos de escena para un renderizador dado, incluyendo iluminación y posiblemente geometría adicional como son planos de suelo. Estos archivos de escena contienen apartados, en los que FreeCAD insertará la posición de la cámara, y la geometría e información de materiales de cada objeto que insertes en el proyecto. La escena modificada es exportada después al renderizador externo.

De momento, dos renderizadores son soportados [povray](http://en.wikipedia.org/wiki/POV-Ray) y [luxrender](http://en.wikipedia.org/wiki/LuxRender). Para poder renderizar directamente en FeeCAD, al menos uno de esos renderizadores debe estar instalado en tu sistema, y su ubicación debe ser configurada en las preferencias de trazado de rayos de FreeCAD. Si ningún renderizador está instalado, todavía puedes exportar un archivo de escena que puede ser utilizado por alguno de los renderizadores después, o en otra máquina.

The Raytracing workbench is essentially obsolete. New development is happening in the [Render Workbench](https://github.com/FreeCAD/FreeCAD-render), which is intended as its replacement. This workbench is fully programmed in Python so it is much easier to extend than the current workbench which is programmed in C++. Nevertheless, the information in this page is generally useful for the new workbench, as both modules work basically in the same way.

<img alt="" src=images/Raytracing_example.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

## Flujo de trabajo típico 

1.  Crea o abre un proyecto FreeCAD, agrega algunos objetos [basados en sólidos](Part_Workbench.md) (por el momento no se soportan mallas)
2.  Crea un proyecto de trazado de rayos (luxrender o povray)
3.  Selecciona los objetos que desees agregar al proyecto de trazado de rayos y agrçegalos con la herramienta \"Insertar Parte\"
4.  Exporta el proyecto o renderízalo directamente


</div>

<img alt="" src=images/Raytracing_Workbench_workflow.svg  style="width:600px;">



*Workflow of the Raytracing Workbench; the workbench prepares a project file from a given template, and then calls an external program to produce the actual rendering of the scene. The external renderer can be used independently of FreeCAD.*

### Herramientas GUI 

### Project tools 

These are the main tools for exporting your 3D work to external renderers.

-   <img alt="" src=images/Raytracing_New.svg  style="width:32px;"> [New PovRay project](Raytracing_New.md): Insert new PovRay project in the document
-   <img alt="" src=images/Raytracing_Lux.svg  style="width:32px;"> [New LuxRender project](Raytracing_Lux.md): Insert new LuxRender project in the document
-   <img alt="" src=images/Raytracing_InsertPart.svg  style="width:32px;"> [Insert part](Raytracing_InsertPart.md): Insert a view of a Part in a raytracing project
-   <img alt="" src=images/Raytracing_ResetCamera.svg  style="width:32px;"> [Reset camera](Raytracing_ResetCamera.md): Matches the camera position of a raytracing project to the current view
-   <img alt="" src=images/Raytracing_ExportProject.svg  style="width:32px;"> [Export project](Raytracing_ExportProject.md): Exports a raytracing project to a scene file for rendering in an external renderer
-   <img alt="" src=images/Raytracing_Render.svg  style="width:32px;"> [Render](Raytracing_Render.md): Renders a raytracing project with an external renderer

### Utilities

These are helper tools to perform specific tasks manually.

-   <img alt="" src=images/Raytracing_WriteView.svg  style="width:32px;"> [Export view to povray](Raytracing_WriteView.md): Write the active 3D view with camera and all its content to a povray file
-   <img alt="" src=images/Raytracing_WriteCamera.svg  style="width:32px;"> [Export camera to povray](Raytracing_WriteCamera.md): Export the camera position of the active 3D view in POV-Ray format to a file
-   <img alt="" src=images/Raytracing_WritePart.svg  style="width:32px;"> [Export part to povray](Raytracing_WritePart.md): Write the selected Part (object) as a povray file

## Preferences

-   <img alt="" src=images/Preferences-raytracing.svg  style="width:32px;"> [Preferences](Raytracing_Preferences.md): Preferences available in for the Raytracing tools.

## Tutorials

-   [Basic Raytracing tutorial](Raytracing_tutorial.md)
-   [Intermediate Raytracing tutorial](Tutorial_FreeCAD_POV_ray.md)

## Creando el archivo povray manualmente 

Las herramientas descritas anteriormente te permiten exportar la vista 3D actual y todos sus contenidos a un archivo [Povray](http://www.povray.org/). Primero, debes de cargar o crear tu información de CAD y posicionar la orientación de vista 3D como desees. Después selecciona \"Utilidades-\>Exportar Vista\...\" del menu de trazado de rayos.

![](images/FreeCAD_Raytracing.jpg )

Se te solicitará la ubicación para guardar el archivo \*.pov resultante. Después de ello puedes abrirlo en [Povray](http://www.povray.org/) y renderizar: ![](images/Povray.jpg )

Como siempre, en un renderizador puedes hacer imágenes grandes y bonitas: <img alt="" src=images/Scharniergreifer_render.jpg  style="width:800px;">

### Archivos de guión 

See the [Raytracing API example](Raytracing_API_example.md) for information on writing scenes programmatically.

### Enlaces

Sobre POV-Ray:

-   <http://www.spiritone.com/~english/cyclopedia/>
-   <http://www.povray.org/>
-   <http://es.wikipedia.org/wiki/POV-Ray>

### LuxRender

-   [LuxRender page on this wiki](LuxRender.md)
-   <http://www.luxrender.net/>

### Future possible renderers to implement 

-   <http://www.yafaray.org/>
-   <http://www.mitsuba-renderer.org/>
-   <http://www.kerkythea.net/>
-   <http://www.artofillusion.org/>

## Exporting to Kerkythea 

Although direct export to the Kerkythea XML-File-Format is not supported yet, you can export your Objects as Mesh-Files (.obj) and then import them in Kerkythea.

-   if using Kerkythea for Linux, remember to install the WINE-Package (needed by Kerkythea for Linux to run)
-   you can convert your models with the help of the mesh workbench to meshes and then export these meshes as .obj-files
-   If your mesh-export resulted in errors (flip of normals, holes \...) you may try your luck with [netfabb studio basic](http://www.netfabb.com/downloadcenter.php?basic=1)

:   Free for personal use, available for Windows, Linux and Mac OSX.
:   It has standard repair tools which will repair you model in most cases.

-   another good program for mesh analysing/repairing is [Meshlab](http://sourceforge.net/projects/meshlab/)

:   Open Source, available for Windows, Linux and Mac OSX.
:   It has standard repair tools which will repair you model in most cases (fill holes, re-orient normals, etc.)

-   you can use \"make compound\" and then \"make single copy\" or you can fuse solids to group them before converting to meshes
-   remember to set in Kerkythea an import-factor of 0.001 for obj-modeler, since Kerkythea expects the obj-file to be in m (but standard units-scheme in FreeCAD is mm)

:   Within WIndows 7 64-bit Kerkythea does not seem to be able to save these settings.
:   So remember to do that each time you start Kerkythea

-   if importing multiple objects in Kerkythea you can use the \"File → Merge\" command in Kerkythea

## Development

These pages refer to the new workbench, programmed in Python, meant to replace the current Raytracing Workbench.

-   [Render Workbench](https://github.com/FreeCAD/FreeCAD-render)
-   [Render Workbench](https://forum.freecadweb.org/viewtopic.php?f=9&t=25933) (announcement only, no discussion)
-   [FreeCAD Renderer Workbench improvements](https://forum.freecadweb.org/viewtopic.php?t=39168)


{{docnav/es|Robot_Workbench/es|Draft_Workbench/es}}


{{Raytracing Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Raytracing](Category_Raytracing.md) > Raytracing Workbench/es

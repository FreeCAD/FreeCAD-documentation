# Raytracing Workbench/pt
**The '''Raytracing Workbench''' is no longer included after version 0.20.<br>
 The external [https://github.com/FreeCAD/FreeCAD-render Render Workbench] should be used instead.**

<img alt="Raytracing workbench icon" src=images/Workbench_Raytracing.svg  style="width:128px;">



## Introdução

A [Bancada Raytracing](Raytracing_Workbench.md) é utilizada para gerar imagens fotorrealísticas de modelos ao processá-las com um renderizador externo.




The <img alt="" src=images/Workbench_Raytracing.svg  style="width:24px;"> [Raytracing Workbench](Raytracing_Workbench.md) is used to generate photorealistic images of your models by processing them with an external renderer.

A bancada Raytracing trabalha com works with [templates](Raytracing_templates.md), os quais são arquivos de projetos que definem uma cena para o seu modelo 3D. Você pode colocar luzes e geometrias, como planos de base, e também contém espaços reservados para a posição da câmera e para as informações do material dos objetos na cena. O projeto pode ser exportado para um arquivo pronto para renderização ou renderizado diretamente no FreeCAD.

Atualmente, dois renderizadores são suportados: [povray](http://en.wikipedia.org/wiki/POV-Ray) e [luxrender](http://en.wikipedia.org/wiki/LuxRender). Para poder renderizar a partir do FreeCAD, pelo menos um desses programas deve ser instalado e configurado em seu sistema. No entanto, se nenhum renderizador estiver instalado, você ainda poderá exportar um arquivo de projeto para ser renderizado em outro momento.


<div class="mw-translate-fuzzy">

The Raytracing workbench is essentially obsolete. New development is happening in the [Render Workbench](https://github.com/FreeCAD/FreeCAD-render), which is intended as its replacement. This workbench is fully programmed in Python so it is much easier to extend than the current workbench which is programmed in C++. Nevertheless, the information in this page is generally useful for the new workbench, as both modules work basically in the same way.


</div>

<img alt="" src=images/Raytracing_example.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

## Fluxo de trabalho típico 

1.  Crie ou abra um projeto do FreeCAD, adicione alguns objetos sólidos ([ Part-based](Part_Workbench.md) ou [ PartDesign-based](PartDesign_Workbench.md)); malhas atualmente não são suportadas.
2.  Crie um projeto de Raytracing (povray ou luxrender).
3.  Selecione os objetos que você deseja adicionar ao projeto Raytracing e adicione-os.
4.  Exportar o arquivo do projeto ou renderizá-lo diretamente.


</div>

<img alt="" src=images/Raytracing_Workbench_workflow.svg  style="width:600px;">



*Workflow of the Raytracing Workbench; the workbench prepares a project file from a given template, and then calls an external program to produce the actual rendering of the scene. The external renderer can be used independently of FreeCAD.*

## Tools

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

## Creating a povray file manually 

The utility tools described above allow you to export the current 3D view and all of its content to a [Povray](http://www.povray.org/) file. First, you must load or create your CAD data and position the 3D View orientation as you wish. Then choose \"Utilities → Export View\...\" from the raytracing menu.

![](images/FreeCAD_Raytracing.jpg )

You will be asked for a location to save the resulting \*.pov file. After that you can open it in [Povray](http://www.povray.org/) and render: ![](images/Povray.jpg )

As usual in a renderer you can make big and nice pictures: <img alt="" src=images/Scharniergreifer_render.jpg  style="width:800px;">

## Scripting

See the [Raytracing API example](Raytracing_API_example.md) for information on writing scenes programmatically.

## Links

### POV-Ray 

-   [POV-Ray page on this wiki](POV-Ray.md)
-   <http://www.spiritone.com/~english/cyclopedia/>
-   <http://www.povray.org/>
-   <http://en.wikipedia.org/wiki/POV-Ray>

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


<div class="mw-translate-fuzzy">


{{docnav/pt|Drawing Workbench/pt|Image Workbench/pt}}


</div>


{{Raytracing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Obsolete Workbenches](Category_Obsolete%20Workbenches.md) > [Raytracing](Category_Raytracing.md) > Raytracing Workbench/pt

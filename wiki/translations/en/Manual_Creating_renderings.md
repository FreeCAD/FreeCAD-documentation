# Manual:Creating renderings/en
{{Manual:TOC}}

In computer speak, the word [rendering](https://en.wikipedia.org/wiki/Rendering_%28computer_graphics%29) is used to describe a nice image produced from a 3D model. Of course, we could say that what we see in the FreeCAD 3D view is already nice. However, anybody who has seen a recent Hollywood movie, knows that it is possible to produce images with a computer that are almost indistinguishable from a photograph.

Of course, producing photo-realistic images requires a lot of work, in addition to a 3D application that offers specific tools for that purpose, such as precise controls for materials and lighting. Because FreeCAD is an application geared more towards technical modelling, it does not feature any advanced rendering tools.

+Fortunately, the open source world offers many applications to produce realistic images. The most famous one is probably [Blender](http://www.blender.org), which is very popular, and widely used in the film and gaming industries. 3D models can very easily and faithfully be exported from FreeCAD and imported into Blender, where you can add realistic materials and illumination, and produce the final images or even animations.

Some other open source rendering tools are made to be used inside other applications, and will take care of doing the complex calculations to produce realistic images. Through its [Raytracing Workbench](Raytracing_Workbench.md), FreeCAD can use two of these rendering tools: [POV-Ray](https://en.wikipedia.org/wiki/POV-Ray) and [Luxrender](https://en.wikipedia.org/wiki/LuxRender). POV-Ray is a very old project, and is considered a classical [raytracing](https://en.wikipedia.org/wiki/Ray_tracing_%28graphics%29) engine, while Luxrender is much newer, and is categorized as an [unbiased](https://en.wikipedia.org/wiki/Unbiased_rendering) renderer. Both have their strengths and weaknesses, depending on the type of image one wants to render. The best way to know is to look at examples on each engine\'s website.

### Installation

Before being able to use the Raytracing Workbench in FreeCAD, one of these two rendering applications needs to be installed on your system. This is usually very straightforward. They both provide installers for many platforms or are usually included in the software repositories of most Linux distributions.

Once POV-Ray or Luxrender is installed, we need to set the path to their main executable in the FreeCAD preferences. This is usually only required on Windows and Mac. On Linux, FreeCAD will pick it from the standard locations. The location of the povray or luxrender executables can be found by searching your system for files named povray (or povray.exe on Windows) and luxrender (or luxrender.exe on Windows).

![](images/Exercise_raytracing_01.jpg )

In this preferences screen we can also set the desired image size we want to produce.

### Rendering with PovRay 

We will use the table we have been modelling in the [traditional modeling](Manual:Traditional_modeling,_the_CSG_way.md) chapter to produce renderings with PovRay and Luxrender.

-   Start by loading the table.FCStd file that we modelled earlier or from the link at the bottom of this chapter.
-   Press the small down arrow next to the <img alt="" src=images/Raytrace_New.svg  style="width:16px;"> [New Povray project](Raytracing_New.md) button, and choose the **RadiosityNormal** template
-   A warning message might appear telling you that the current 3D view is not in perspective mode and the rendering will therefore differ. Correct this by choosing **No**, choosing menu **View-\>Perspective view** and choosing the RadiosityNormal template again.
-   You can also try other templates after you create a new project, simply by editing its **Template** property.
-   A new project has now been created:

![](images/Exercise_raytracing_02.jpg )

-   The new project has adopted the point of view of the 3D view as it was at the moment we pressed the button. We can change the view, and update the view position stored in the Povray project anytime, by pressing the <img alt="" src=images/Raytrace_ResetCamera.svg  style="width:16px;"> [Reset camera](Raytracing_ResetCamera.md) button.
-   The Raytracing Workbench works the same way as the [Drawing Workbench](Drawing_Workbench.md): Once a project folder is created, we must add **Views** of our objects to it. We can now do that by selecting all the objects that compose the table, and press the <img alt="" src=images/Raytrace_NewPartSegment.svg  style="width:16px;"> [Insert part](Raytracing_InsertPart.md) button:

![](images/Exercise_raytracing_03.jpg )

-   The views have taken the color and transparency values from their original parts, but you can change that in the properties of each individual view if you wish.
-   We are now ready to produce our first Povray render. Press the <img alt="" src=images/Raytrace_Render.svg  style="width:16px;"> [Render](Raytracing_Render.md) button.
-   Note for windows users: when receiving (in Povray) a warning saying \"I/O restrictions prohibit write access \...\"
    -   open Povray
    -   choose \"Options \> Script I/O Restrictions\" and make sure it is set to \"No Restrictions\"
    -   retry render
-   You will be asked to give a file name and path for the .png image that will be saved by Povray.
-   Povray will then open and calculate the image.
-   When this is done, click the image to close the Povray window. The resulting image will be loaded in FreeCAD:

![](images/Exercise_raytracing_04.jpg )

### Rendering with LuxRender 

-   Rendering with Luxrender works almost the same way. We can leave our file open and create a new Luxrender project in the same file, or reload it to start from scratch.
-   Press the little down arrow next to the <img alt="" src=images/Raytrace_Lux.svg  style="width:16px;"> [New Luxrender project](Raytracing_Lux.md) button and choose the **LuxOutdoor** template.
-   Select all the components of the table. If you still have the Povray project in your document, be sure to also select the Luxrender project itself, so the views created in the next step won\'t go in the wrong project by mistake.
-   Press the <img alt="" src=images/Raytrace_NewPartSegment.svg  style="width:16px;"> [Insert part](Raytracing_InsertPart.md) button.
-   Select the Luxrender project, and press the <img alt="" src=images/Raytrace_Render.svg  style="width:16px;"> [Render](Raytracing_Render.md) button.
-   Luxrender works differently to Povray. When you start the render, the Luxrender application will open and immediately start rendering:

![](images/Exercise_raytracing_05.jpg )

-   If you leave that window open, Luxrender will continue calculating and rendering forever, progressively refining the image. It is up to you to decide when the image has reached a sufficient quality for your needs, and stop the render.
-   There are also many controls to play with, on the left panel. All these controls will change the aspect of the image being rendered on the fly, without stopping the rendering.
-   When you feel the quality is good enough, press **Render-\>stop**, and then **File-\>Export to image-\>Tonemapped low dynamic range** to save the rendered image to a png file.

You can greatly extend the rendering possibilities of FreeCAD by creating new templates for Povray or Luxrender. This is explained in the [Raytracing Workbench](Raytracing_Workbench.md) documentation.

**Downloads**

-   The table model: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/table.FCStd>
-   The file produced during this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/render.FCStd>

**Read more**

-   [The Raytracing Workbench](Raytracing_Workbench.md)
-   [Blender](http://www.blender.org)
-   [POV-Ray](http://www.povray.org)
-   [Luxrender](http://www.luxrender.net)




{{Raytracing Tools navi}}



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Raytracing](Category_Raytracing.md) > Manual:Creating renderings/en

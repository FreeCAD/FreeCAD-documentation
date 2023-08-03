---
 TutorialInfo:o
   Topic:  Raytracing
   Level:  Beginner
   Time:  10 minutes + Render time
   Author: http://freecadweb.org/wiki/index.php?title=User:Drei Drei
   FCVersion: 0.16 or above
   Files: 
---

# Raytracing tutorial/ro



## Raytracing Workbench 


**The [Raytracing workbench](Raytracing_Workbench.md) is being superseded by the new [https://github.com/FreeCAD/FreeCAD-render Render Workbench], which is intended as its replacement. The Render Workbench can be installed through the [Addon Manager](Std_AddonMgr.md). The information here is provided because by default FreeCAD is still shipped (as of 0.19-24276) with the Raytracing Workbench, and because the new module should basically work in the same way**




<div class="mw-translate-fuzzy">

### Introducere

This tutorial is meant to introduce the reader to the basic workflow of the Raytracing Workbench, as well as most of the tools that are available to create a rendered image.


</div>

<img alt="" src=images/Raytracing_tutorial_result.png  style="width:480px;">

## Requirements

-   FreeCAD version 0.16 or above
-   [POV-Ray](http://www.povray.org/) and/or [LuxRender](https://luxcorerender.org/) is installed on the system
-   In the case of POV-Ray, it\'s not enough to have just the binary executable in place, but it also ***requires***the installation of***supporting files***. In Ubuntu, these are provided by the Recommends-flagged package [povray-includes](https://packages.ubuntu.com/search?keywords=povray-includes). Potential issues have also been seen with Linux installations requiring local configuration files to be manually created in a user\'s home folder, as discussed [here](https://forum.freecadweb.org/viewtopic.php?f=3&t=27548&start=10#p224576).
-   In the case of POV-Ray, installation of [psicofil\'s macro](https://github.com/psicofil/Macros_FreeCAD) is recommended
-   The reader has the basic knowledge to use the Part and PartDesign Workbenches

## Procedure

### Modeling

In this example a Cube is used as the study object, but models created in the Part or PartDesign Workbenches can be used instead.

1.  Create a new document
2.  Activate the Part Workbench
3.  Create a Cube. You are free to change its properties in any way.

Now we have a model with which to work.

### Preparing for the render 

1.  Switch to the Raytracing Workbench
2.  Change your View to **Perspective**. Go to **View** menu and select **Perspective**.
3.  Set the location for the renderer. Go to the **Edit** menu and select **Preferences**. Click on **Raytracing** and set the location to the executable.
4.  Set the size of the rendered image. Go to the **Edit** menu and select **Preferences**. Click on **Raytracing** and set the desired image size.

#### POV-Ray 

1.  Select <img alt="" src=images/Raytrace_New.svg  style="width:32px;"> [New PovRay project](Raytracing_New.md). From the dropdown menu pick 
**RadiosityNormal**

#### LuxRender

1.  Select <img alt="" src=images/Raytrace_Lux.svg  style="width:32px;"> [New LuxRender project](Raytracing_Lux.md). From the dropdown menu pick 
**LuxClassic**

### Setting the camera position 

1.  Position the **3D View** to the desired location and distance from the model. In this case we will use the **Axonometric View**.
2.  Select the **Project Folder** from the **Tree View**
3.  Select <img alt="" src=images/Raytrace_ResetCamera.svg  style="width:32px;"> [Reset camera](Raytracing_ResetCamera.md)

### Importing the model 

1.  Select the model to render.
2.  Select <img alt="" src=images/Raytrace_NewPartSegment.svg  style="width:32px;"> [Insert part](Raytracing_InsertPart.md)


<div class="mw-translate-fuzzy">

#### Running the Renderer 

1.  Select <img alt="" src=images/Raytracing_Render.png  style="width:32px;"> [Render](Raytracing_Render.md).
2.  Set the path to which the image will be stored.
3.  Wait for the rendering to finish. This may take a while.


</div>


<div class="mw-translate-fuzzy">

#### Viewing the results 

FreeCAD will immediately open the image after the render is finished.


</div>


<div class="mw-translate-fuzzy">

We are now finished with the basic workflow for the [Raytracing Workbench](Raytracing_Workbench.md).


</div>


{{Raytracing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Raytracing](Raytracing_Workbench.md) > Raytracing tutorial/ro

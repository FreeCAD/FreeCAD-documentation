# Manual:Creating renderings/en
{{Manual:TOC}}

[Rendering](https://en.wikipedia.org/wiki/Rendering_%28computer_graphics%29) is the process of creating highly realistic images from 3D models by simulating lighting, materials, and textures. It's commonly used in industries like film, video games, and product design, where photorealistic visualizations are necessary to showcase designs or concepts. While rendering can create images that closely resemble real-life photographs, it requires specialized tools to control things like lighting, reflections, and shadows.

FreeCAD, however, is focused primarily on technical modeling rather than artistic or visual effects. Its primary purpose is to create accurate 3D models for engineering, design, and manufacturing. As a result, FreeCAD does not feature advanced built-in rendering tools for photorealism.

However, FreeCAD does offer the [Render workbench](https://github.com/FreeCAD/FreeCAD-render?tab=readme-ov-file), which can be installed as an add-on (it's not one of the default workbenches). This workbench allows users to connect FreeCAD models with external rendering engines like Blender Cycles, LuxCoreRender, or POV-Ray. Through the Render Workbench, users can use their models and leverage these powerful external tools to render their designs with realistic lighting and textures. This approach keeps FreeCAD lightweight and focused while still providing the flexibility for photorealistic rendering when needed.

The Render Workbench in FreeCAD integrates with several external renderers, including [LuxCorerender](https://en.wikipedia.org/wiki/LuxRender), [POV-Ray](https://en.wikipedia.org/wiki/POV-Ray), and [Blender Cycles](https://www.cycles-renderer.org/). LuxCoreRender is a modern, physically-based renderer that delivers photorealistic images, but it requires significant computational power, especially for large scenes. POV-Ray, while older, remains a reliable [raytracing](https://en.wikipedia.org/wiki/Ray_tracing_%28graphics%29) engine and is less resource-intensive, though it lacks the realism of newer technologies. Blender Cycles, accessible through FreeCAD when Blender is installed, offers a powerful rendering solution with GPU and CPU support, producing high-quality images efficiently. However, it requires installing Blender separately and exporting models to Blender for rendering. Each renderer offers strengths depending on the user\'s balance of realism, performance, and system capabilities. Every option has its strengths and weaknesses, depending on the type of image one wants to render. The best way to know is to look at examples on each engine\'s website.

### Installation

Before using the Render Workbench in FreeCAD, you\'ll need to install both the workbench itself (as shown in [this section](https://wiki.freecad.org/Manual:Installing#Installing_additional_content) and one of the external rendering applications such as LuxCoreRender, POV-Ray, or Blender Cycles (with Blender installed). Installing these applications is typically straightforward, as they provide installers for various platforms and are often included in software repositories on Linux distributions. Once these tools are installed, you\'ll be able to connect FreeCAD to these renderers to produce high-quality images.

Once POV-Ray or LuxCorerender is installed, we need to set the path to their main executable in the FreeCAD preferences. This is usually only required on Windows and Mac. On Linux, FreeCAD will pick it from the standard locations. The location of the povray or luxrender executables can be found by searching your system for files named povray (or povray.exe on Windows) and luxrender (or luxrender.exe on Windows). In the **Preferences** tab you can designate the path as well as set up some parameters.

![](images/FreeCAD_Render_Preferences.png )

### Rendering with PovRay 

We will use the table we have been modelling in the [traditional modeling](Manual:Traditional_modeling,_the_CSG_way.md) chapter to produce renderings with PovRay.

-   Start by loading the table.FCStd file that we modelled earlier or from the link at the bottom of this chapter and entering the <img alt="" src=images/Render_workbench_icon.svg  style="width:16px;"> [workbench](https://github.com/FreeCAD/FreeCAD-render%7Crender).
-   Create a rendering project by pressing the button in the toolbar corresponding to your renderer. For our example, we will choose the <img alt="" src=images/Render_Povray.svg  style="width:16px;"> povray renderer.
-   Select a template suitable for your project. We will be going with the **povray_sunlight.pov** one.
-   You can also try other templates after you create a new project, simply by editing its **Template** property.
-   A new project has now been created:

![](images/FreeCAD_Render_Project.png )

-   You can add the desired objects to the project by selecting them and pressing on the <img alt="" src=images/Render_RenderingView.svg  style="width:16px;"> [rendering view](Render_RenderingView.md) option.

![](images/FreeCAD_Render_Bodies.png )

-   If we wish we can apply a material to our bodies by pressing on the <img alt="" src=images/Arch_SetMaterial.svg  style="width:16px;"> [Material](Arch_SetMaterial.md) option. For our case, we will choose the matte option.
-   We can now press on the <img alt="" src=images/Render_workbench_icon.svg  style="width:16px;"> button and our rendered result will appear in a separate window.

![](images/FreeCAD_Render_Result.png )

Truth be told, the end result is not very impressive. The rendering process is iterative and takes time and patience to achieve high-quality outcomes. Additionally, as mentioned above, POV-Ray is somewhat limited in terms of realism. Feel free to experiment with different renderers. The procedure remains largely the same, with the only difference being the selection of a different renderer at the start of the process.

**Downloads**

-   The table model: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/table.FCStd>
-   The file produced during this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/render.FCStd>

**Read more**

-   [Blender](http://www.blender.org)
-   [POV-Ray](http://www.povray.org)




{{Raytracing Tools navi}}



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Raytracing](Category_Raytracing.md) > Manual:Creating renderings/en

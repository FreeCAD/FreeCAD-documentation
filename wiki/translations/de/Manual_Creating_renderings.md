# Manual:Creating renderings/de
{{Manual:TOC}}

Rendering (Neudeutsch für den etwas sperrigen Begriff [Bildsynthese](https://de.wikipedia.org/wiki/Bildsynthese)) ist der Prozess der Erstellung hochgradig realistischer Bilder von 3D-Modellen durch die Simulation von Beleuchtung, Material und Textur. Es wird üblicherweise in der Film- und der Spieleindustrie sowie im Produktdesign eingesetzt, wo fotorealistische Visualisierungen benötigt werden, um Entwürfe und Konzepte darzustellen. Damit Bilder erstellt werden können, die echten Fotos gleichen, werden spezialisierte Werkzeuge zur Steuerung von Beleuchtung, Reflexionen und Schatten benötigt.

FreeCAD ist aber in erster Linie auf technisches Modellieren ausgerichtet und weniger auf künstlerische und visuelle Effekte. Sein vorrangiger Zweck ist es, präzise 3D-Modelle für Konstruktion, Design und Produktion zu erstellen. Daraus resultiert, dass FreeCAD keine hoch entwickelten Werkzeuge für Fotorealismus enthält.

FreeCAD stellt allerdings den Arbeitsbereich [Render](https://github.com/FreeCAD/FreeCAD-render?tab=readme-ov-file) bereit, der als Addon installiert werden kann (Es ist keiner der Standardarbeitsbereiche). Dieser Arbeitsbereich ermöglicht dem Anwender FreeCAD-Modelle mit externen Render-Programmen wie Blender Cycles, LuxCoreRender oder POV-Ray zu verbinden. Durch den Arbeitsbereich Render können Anwender ihre Modelle verwenden und diese externen Werkzeuge wirkungsvoll einsetzen, um ihre Konstruktionen mit realistischer Beleuchtung und Texturen zu rendern (synthetisieren). Diese Herangehensweise erhält FreeCAD schlank und fokussiert, während die Flexibilität, bei Bedarf Fotorealistisch zu rendern, bestehen bleibt.

Der Arbeitsbereich Render integriert einige externe Renderer in FreeCAD einschließlich [LuxCorerender](https://en.wikipedia.org/wiki/LuxRender), [POV-Ray](https://en.wikipedia.org/wiki/POV-Ray) und [Blender Cycles](https://www.cycles-renderer.org/). LuxCoreRender ist ein moderner, physikbasierter Renderer, der fotorealistische Bilder erstellt, aber eine erhebliche Rechenleistung erfordert, besonders für große Szenen. POV-Ray ist schon älter, ist aber immer noch ein zuverlässiges [Raytracing](https://de.wikipedia.org/wiki/Raytracing)-Programm und geht weniger verschwenderisch mit den Ressourcen um, dafür lässt es etwas den Realismus neuerer Technologien vermissen. Blender Cycles ist über FreeCAD erreichbar, wenn Blender installiert ist und stellt eine leistungsfähige Rendering-Lösung mit GPU- und CPU-Unterstützung zur Verfügung, die qualitativ hochwertige Bilder effizient erstellt. Allerdings erfordert dies die separate Installation von Blender und das Exportieren der Modelle zu Blender, um sie zu rendern. Jeder Renderer hat seine Stärken, abhängig von der Balance zwischen Realismus, Leistung und Systemressourcen. Jede Option hat ihre Stärken und Schwächen, abhängig von der Art der Darstellungen, die man rendern möchte. Der beste Weg sie herauszufinden, ist die Beispiele auf ihren zugehörigen Webseiten zu vergleichen.



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
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Raytracing](Category_Raytracing.md) > Manual:Creating renderings/de

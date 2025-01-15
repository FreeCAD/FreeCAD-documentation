# <img alt="Symbol des Arbeitsbereichs Render" src=images/Render_workbench_icon.svg  style="width:64px;"> Render Workbench/de






## Einleitung

Der Arbeitsbereich Render dient dazu, hochwertige Abbildungen von FreeCAD-Modellen mit Hilfe externer quelloffener Rendering-Engines zu errechnen.

Image:Pabellon_de_Barcelona.png\|Barcelona pavilion
Bildschirmaufnahme Image:Pabellon_de_Barcelona_Pov_large.png\|Barcelona pavilion
Povray-Rendering Image:Pabellon_de_Barcelona_Cycles.png\|Barcelona pavilion
Cycles-Rendering Image:Asm_V4.png\|Asm V4
Bildschirmaufnahme Image:Asm_V4_lux.png\|Asm V4
LuxCore-Rendering Image:Asm_V4_ospray2.png\|Asm V4
Ospray-Rendering Image:Church_of_the_light.png\|Church of the light
Bildschirmaufnahme Image:Church_of_the_light_lux2.png\|Church of the light
LuxCore-Rendering Image:Church_of_the_light_cycles.png\|Church of the light
Cycles-Rendering Image:Car.png\|Car
Bildschirmaufnahme Image:Car_ospray.png\|Car
Ospray-Rendering Image:Car_lux.png\|Car
LuxCore-Rendering Image:Brick_assembly.png\|Brick assembly
Bildschirmaufnahme Image:Brick_assembly_appleseed.png\|Brick assembly
Appleseed-Rendering Image:Brick_assembly_luxcore.png\|Brick assembly
Luxcore-Rendering Image:VillaSavoye.png\|Villa Savoye
Bildschirmaufnahme Image:VillaSavoye appleseed.png\|Villa Savoye
Appleseed-Rendering Image:VillaSavoye Cycles.png\|Villa Savoye
Cycles-Rendering

Als reiner Python-Arbeitsbereich fügt sich Render nahtlos in FreeCAD ein: Die ganze zu rendernde Szene - Objekte, Beleuchtung, Werkstoffe, Kamera, usw. - kann mit FreeCAD-Objekten beschrieben werden, um dann zu externen Renderern exportiert zu werden.

Verglichen mit anderen Ansätzen, die auf Computergrafikanwendungen von Drittherstellern basieren, zielt Render auf folgende Punkte ab:

-   Vermeiden, dass der Benutzer eine weitere 3D- bzw. Computergrafik-Software lernen muss; alles was man kennen muss befidet sich in FreeCAD.
-   Vereinfachung des Rendering-Workflows und Entlastung des Benutzers von Dateibearbeitungen zwischen den Programmen, wie Importieren, Exportieren, Szenen überarbeiten usw.
-   Erstellung dauerhafter Szenenkonfigurationen und besonders das Verhindern von Überarbeitungen mit einem externen Werkzeug, wann immer das Modell bearbeitet wurde.



## Unterstützte Renderer 

Gegenwärtig werden sechs Rendering-Engines unterstützt:

-   LuxCoreRender
-   Appleseed
-   Cycles (eigenständige Version)
-   Pov-Ray
-   Intel Ospray Studio
-   Pbrt-v4 (experimentell)



## Anwendung

Im Quick-Start-Modus, nach der vollständigen Installation des Arbeitsbereiches, ist das Rendern eines FreeCAD-Modells einfach nur ein Prozess, der aus vier Schritten besteht:


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  **Create a rendering project:** Press the button in the toolbar corresponding to your renderer and select a template suitable for your renderer (you may start with a \'studio\' flavour, like **appleseed_studio_light.appleseed**, **cycles_studio_light.xml**, **luxcore_studio_light.cfg**, **povray_studio_light.pov** etc.).
2.  **Add views of your objects to your rendering project:** Select both the objects and the project, and press the **Add view** button.
3.  **Set your point of view:** [Navigate in the 3D View](Manual_Navigating_in_the_3D_view.md) to the desired position and switch to [perspective](Std_PerspectiveCamera.md) mode.
4.  **Render:** Select your project and press the **Render** button in toolbar (also available from project\'s context menu).


</div>

**Und ein erstes Rendering des eigenen Modells sollte fertig sein.**

Weitere Anleitungen findet man im [GitHub-Repository](https://github.com/FreeCAD/FreeCAD-render) oder in der Online-Hilfe.



## Funktionen


<div lang="en" dir="ltr" class="mw-content-ltr">

Features include, but are not limited to:

-   Lighting: point lights, area lights, sun-sky and preset lighting templates.
-   Cameras.
-   Material management (using usual shaders: matte, glossy, glass, principled etc.) including textures.
-   Batch mode / UI mode.
-   Denoiser.
-   Halt condition (sample per pixel).
-   Meshing control: angular and linear deflections, auto-smoothing.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Links


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

More info? Just follow the link: <https://github.com/FreeCAD/FreeCAD-render>


</div>



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > [External Workbenches](Category_External%20Workbenches.md) > Render Workbench/de

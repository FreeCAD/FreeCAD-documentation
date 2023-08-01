# <img alt="POV-Ray-Rendering Workbench icon" src=images/POV-Ray-Rendering_workbench_icon.svg  style="width:64px;"> POV-Ray-Rendering Workbench/pl


{{TOCright}}



## Wprowadzenie

Środowisko POV-Ray-Rendering jest [zewnętrznym środowiskiem pracy](External_workbenches/pl.md) pozwalającym na łatwe stworzenie wizualizacji twojego projektu, nie ograniczając przy tym możliwości bardziej biegłym użytkownikom. Środowisko wykorzystuje oprogramowanie [POV-Ray](http://www.povray.org/).

<img alt="" src=images/POV-Ray-Rendering_Example.png  style="width:600px;">



## Funkcjonalności



### Teksturowanie

There are more than 100 predefined textures you can apply, but you can also define your own textures.

<img alt="" src=images/POV-Ray-Rendering_Textures.png  style="width:600px;">

#### Thumbnails and live preview 

To see the impact of the selected texture options you can check the pre-rendered thumbnail or use the live preview to render the texture.



### Oświetlenie

With the three light types: area light, point light and spot light, and their different options, you can create advanced lighting.

<img alt="" src=images/POV-Ray-Rendering_Lights.png  style="width:600px;">

#### Indirect lighting (GI) 

The workbench has the option to enable indirect lighting to create more realistic images.

<img alt="" src=images/POV-Ray-Rendering_IndirectLighting.png  style="width:600px;">

### HDRI environments 

With support for HDRI environments, beautiful environments are simple to use.

<img alt="" src=images/POV-Ray-Rendering_HDRI.png  style="width:600px;">

### User inc file 

Power users who want access to *all* options of the [POV-Ray](http://www.povray.org/) renderer can do so by creating a special file. For more details see the [Power User](https://gitlab.com/usbhub/exporttopovray/-/blob/master/doc/PowerUser.md) page on our Wiki.



## Użycie

Here is a simple demonstration of the workbench:

![](images/POV-Ray-Rendering_Demo.gif )

There are many more options on the other tabs, please explore them yourself, or you can visit our Wiki: [Workbench Wiki](https://gitlab.com/usbhub/exporttopovray/-/tree/master/doc)



## Instalacja

This workbench can be installed and updated from the <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md). The [POV-Ray](http://www.povray.org/) renderer used by the workbench has to be installed separately. For Windows users, the installer can be downloaded from the [POV-Ray Download Page](https://www.povray.org/download/), for Linux users it can usually be installed from the package manager. Look up the detailed instructions in the [POV-Ray Wiki](https://wiki.povray.org/content/HowTo:Install_POV) if you\'re on a Mac.

To complete the installation the path to the POV-Ray executable has to be defined in the workbench preferences, usually these are the default paths:

-   **Windows:** **C:/Program Files/POV-Ray/v3.7/bin/pvengine64.exe** (the **v*.*** folder may change depending on the POV-Ray version)
-   **Linux:** **/usr/bin/povray**
-   **MacOS:** Not available. If you have more information, please let us know.

<img alt="" src=images/POV-Ray-Rendering_ExePath.png  style="width:600px;">



## Przybory

-   <img alt="" src=images/POV-Ray-Rendering_OpenDialog.svg  style="width:32px;"> OpenDialog: Opens the dialog where most of the work is done. Here you can apply textures, add HDRI environments, etc. and start the rendering.

-   <img alt="" src=images/POV-Ray-Rendering_PointLight.svg  style="width:32px;"> Point Light: Inserts a Point Light.

-   <img alt="" src=images/POV-Ray-Rendering_AreaLight.svg  style="width:32px;"> Area Light: Inserts an Area Light.

-   <img alt="" src=images/POV-Ray-Rendering_SpotLight.svg  style="width:32px;"> Spot Light: Inserts a Spot Light.

## References

-   Authors:
    -   Usb Hub: <https://gitlab.com/usbhub>
    -   DerUhrmacher: <https://gitlab.com/DerUhrmacher>
-   Source code on GitHub: <https://github.com/TheRaytracers/freecad-povray-render>

## Links to POV-Ray Workbench 

-   Workbench Wiki: <https://gitlab.com/usbhub/exporttopovray/-/tree/master/doc>
-   FreeCAD Forum: <https://forum.freecadweb.org/viewtopic.php?f=9&t=48629>
-   Report bugs: Please report bugs at GitHub or the FreeCAD Forum



## Inne użyteczne odnośniki 

-   [External workbenches](External_workbenches.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > POV-Ray-Rendering Workbench/pl

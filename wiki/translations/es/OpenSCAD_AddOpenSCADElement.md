# OpenSCAD AddOpenSCADElement/es
---
- GuiCommand:/es   Name:OpenSCAD AddOpenSCADElement   Name/es:Añadir un elemento OpenSCAD   Workbenches:[[OpenSCAD_Workbench/es   OpenSCAD]]|MenuLocation:OpenSCAD -> Añadir un elemento OpenSCAD---


</div>

## Description


<div class="mw-translate-fuzzy">

#### Descripción

Añade un elemento OpenSCAD introduciendo código OpenSCAD en el panel de tareas y ejecutando el binario de OpenSCAD binary (requiere de OpenSCAD)


</div>

Cuando se selecciona \'una malla\', OpenSCAD renderiza una malla.

Cada vez que se presiona Añadir se ejecuta el código y se importan elementos.


<div class="mw-translate-fuzzy">

Esta función no proporciona ningún control de sintaxis o errores proporcionado más allá de no ofrecer un resultado de OpenSCAD. Si los elementos no especifican la ruta a utilizar \<\> e incluir\<\> las declaraciones podrían estar rotas.

Las bibliotecas deberían ser accesibles por defecto, mientras que a los ejemplos se podría acceder así


</div>

Libraries should be accessible as usual, whereas example can be reached as stated below.


```python
include <../examples/example001.scad>;
```


<div class="mw-translate-fuzzy">

incluiría el primer ejemplo conocido también como el icono de OpenSCAD


</div>

## Setup OpenSCAD within FreeCAD 

**Note:** OpenSCAD needs to be installed on your computer before FreeCAD will have this functionality
Install OpenSCAD in the appropriate manner for your operating system. See [the OpenSCAD web site](https://www.openscad.org/) for more information.

FreeCAD needs to be told where to find the OpenSCAD executable:

-   Switch to the <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> [OpenSCAD Workbench](OpenSCAD_Workbench.md) via 
**View → Workbench → OpenSCAD**
-   Open the preferences dialog **Edit → Preferences**
-   Click on \"OpenSCAD\" on the left plane
-   Click on the button labled **...** in **General Settings → General OpenSCAD Settings → OpenSCAD executable** to browse the directory or enter the path (e.g. Ubuntu based Linux distributions `/usr/bin/openscad`) directly into the line input right to the button
-   Close and restart FreeCAD

:   **Result:** A new OpenSCAD icon will appear on the tool bar, and in the OpenSCAD menu, in the FreeCAD OpenSCAD workbench.

Note: It is also possible to add another optional Parameter which controls the maximum sides of a polygon before it is considered a circle (fn).

Starting from <small>(v0.14)</small> , FreeCAD will search for the OpenSCAD executable if the setting mentioned above is empty.





{{OpenSCAD_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD AddOpenSCADElement/es

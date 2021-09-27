# <img alt="FCEngranaje Icono Ambiente de trabajo Externo" src=images/FCGear_workbench_icon.svg  style="width:64px;"> FCGear Workbench/es

## Introducción


{{TOCright}}

El [Ambiente de trabajo FCEngranaje](FCGear_Workbench/es.md) es un [Ambiente de trabajo externo](external_workbenches/es.md) para fabricar diferentes tipos de engranajes y ruedas helicoidales en FreeCAD. El modelado paramétrico permite cambiar las geometrías requeridas en cualquier momento. Por ejemplo, cambiando unos pocos parámetros, el engranaje evolvente se convierte en un engranaje recto, en un engranaje helicoidal o en un engranaje doblemente helicoidal.

Para que los resultados de FC Engranaje sean utilizables, es necesario tener ciertos conocimientos básicos sobre los diferentes tipos de engranajes. Módulo, diámetro de paso o diámetro de raíz son términos comunes y, por tanto, deben conocerse.

Junto con la impresión 3D, los usuarios domésticos tienen ahora la oportunidad de diseñar y producir engranajes y ruedas dentadas sinfín según sus propias ideas personales y, si es necesario, adaptarlas a las condiciones constructivas.

Before [FCGear Workbench](FCGear_Workbench.md) can be started, it must be installed (how it is done see below at **Installation**). After installation, the tools are available in the toolbar.

:   ![](images/FCGear_Drop-down-menu_example-en.png )
:   
    *The FCGear Drop down menu*
    

## Tipos de engranajes 

### Engranaje envolvente 

:   ![](images/Involute-Gear_example.png )
:   
    *From left to right: Spur gearing, helical gearing, double helical gearing (see [FCGear InvoluteGear](FCGear_InvoluteGear.md))*
    

### Involute Rack 

:   ![](images/Involute-Rack_example.png )
:   
    *From left to right: Spur gearing, helical gearing, double helical gearing (See [FCGear InvoluteRack](FCGear_InvoluteRack.md))*
    

### Engranaje cicloide 

:   ![](images/Cycloid-Gear_example_1.png )
:   
    *From left to right: Spur gearing, helical gearing, double helical gearing (see [FCGear CycloideGear](FCGear_CycloideGear.md))*
    

### Engranaje cónico 

:   ![](images/Bevel-Gear_example.png )
:   
    *From left to right: Spur gearing, spiral gearing (see [FCGear BevelGear](FCGear_BevelGear.md))*
    

### Engranaje sinfín 

:   ![](images/Worm-Gear_example.png )
:   
    *Above: Worm gear (see [FCGear WormGear](FCGear_WormGear.md))*
    

### Engranaje de la corona 

:   ![](images/Crown-Gear_example.png )
:   
    *Above: Crown gear (see [FCGear CrownGear](FCGear_CrownGear.md))*
    

### Timing Gear and Lantern Gear 

:   ![](images/Timing+Latern-gear_example.png )
:   
    *From left to right: Timing gearing, lantern gearing (see [FCGear TimingGear](FCGear_TimingGear.md) or [FCGear LanternGear](FCGear_LanternGear.md))*
    

## Referencias

-   Author: looooo
-   Home page: <https://github.com/looooo/FCGear>
-   Source code on github: <https://github.com/looooo/FCGear>

## Herramientas

### Barra Herramienta 

-   <img alt="" src=images/FCGear_InvoluteGear.svg  style="width:32px;"> [FCGear InvoluteGear](FCGear_InvoluteGear.md) Creates an Involute gear
-   <img alt="" src=images/FCGear_InvoluteRack.svg  style="width:32px;"> [FCGear InvoluteRack](FCGear_InvoluteRack.md) Creates an Involute rack
-   <img alt="" src=images/FCGear_CycloideGear.svg  style="width:32px;"> [FCGear CycloideGear](FCGear_CycloideGear.md) Creates a Cycloide gear
-   <img alt="" src=images/FCGear_BevelGear.svg  style="width:32px;"> [FCGear BevelGear](FCGear_BevelGear.md) Creates a Bevel gear
-   <img alt="" src=images/FCGear_WormGear.svg  style="width:32px;"> [FCGear WormGear](FCGear_WormGear.md) Creates a Worm gear
-   <img alt="" src=images/FCGear_CrownGear.svg  style="width:32px;"> [FCGear CrownGear](FCGear_CrownGear.md) Creates a Crown gear
-   <img alt="" src=images/FCGear_TimingGear.svg  style="width:32px;"> [FCGear TimingGear](FCGear_TimingGear.md) Creates a Timing gear
-   <img alt="" src=images/FCGear_LanternGear.svg  style="width:32px;"> [FCGear LanternGear](FCGear_LanternGear.md) Creates a Lantern gear

## Instalación

### Instalación automática 

The recommended method of installation as of v0.17 is via the <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Addon_Manager.md). It can be found in the 
**Tools → Addon Manager**


<div class="mw-collapsible mw-collapsed toccolours" style="width:700px">

### Instalación manual 

If there is a necessity to manually install this workbench the following instructions are provided to do so:


<div class="mw-collapsible-content">

#### Linux

-    `git clone https://github.com/looooo/FCGear.git`
    

-   link or copy the folder into {{FileName|/freecad/Mod}}

:   

    :   
        `sudo ln -s (path_to_FCGear) (path_to_freecad)/Mod`
        

#### Windows

Tested on (7/8/8.1/10) (From GitHub)

-   download ZIP-archive by clicking on button in top right corner
-   go to FreeCAD-Macro-Folder (inside FreeCAD, choose \"Edit \> Preferences \> General \> Macro to see Macro Path)
-   if you haven\'t changed the standard settings, it should be \"C:\\Users\\Your\_Windows\_User\_Name\\AppData\\Roaming\\FreeCAD\"
-   \\appdata is a HIDDEN folder, so you may have to change the settings of the file explorer to see it
-   create a sub-folder called \"FCGear\"
-   make sure to copy files and folders EXACTLY as shown above to the just created sub-folder
-   restart FreeCAD and the workbench should appear in the pull-down menu
-   within FreeCAD you can choose \"Tools \> Customize \> Workbenches\" to enable/disable workbenches

#### MacOSX

Vea las instrucciones para Linux arriba


</div>


</div>

## Enlaces a la WB de engranajes 

-   Wiki de Ambiente de trabajo: <https://github.com/looooo/FCGear/wiki>
-   Wiki de FreeCAD: [Macro\_FCGear](http://www.freecadweb.org/wiki/index.php?title=Macro_FCGear) y [Engranaje cónico](http://forum.freecadweb.org/viewtopic.php?f=3&t=12878)
-   Foro de FreeCAD: <http://forum.freecadweb.org/viewtopic.php?f=21&t=12968>
-   Tutoriales:
-   Vídeos:
-   Archivos:
-   Reportar errores: Por favor, informa de los errores en <https://github.com/looooo/FCGear/issues>

## Otros enlaces útiles 


<div class="mw-translate-fuzzy">

-   <img alt="PartDesign\_InvoluteGear" src=images/PartDesign_InvoluteGear.svg  style="width:24px;"> _.
-   [Ambientes de trabajo externos](External_workbenches/es.md): Una lista de todos los ambientes de trabajo externos actuales de FreeCAD
-   [Recetas de macros](Macros_recipes/es.md)


</div>




_ _ _

---
[documentation index](../README.md) > [External Workbenches](Category_External Workbenches.md) > FCGear Workbench/es

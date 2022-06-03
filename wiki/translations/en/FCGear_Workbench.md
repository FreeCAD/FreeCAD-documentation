# <img alt="FCGear External Workbench icon" src=images/FCGear_workbench_icon.svg  style="width   *64px;"> FCGear Workbench/en

## Introduction


{{TOCright}}

The [FCGear Workbench](FCGear_Workbench.md) is an [external workbench](external_workbenches.md) for manufacturing different types of gears and worm gears in FreeCAD. The parametric modelling allows the required geometries to be changed at any time. For example, by changing a few parameters, the involute gear becomes either a spur gear, helical gear or double helical gear.

In order for the results from FC Gear to be usable, a certain amount of basic knowledge about the different types of gearing is required. Module, pitch diameter or root diameter are common terms and should therefore be known.

In conjunction with 3D printing, home users now have the opportunity to design and produce gears and worm gears according to their own personal ideas and, if necessary, to adapt them to the constructional conditions.

Before [FCGear Workbench](FCGear_Workbench.md) can be started, it must be installed (how it is done see below at **Installation**). After installation, the tools are available in the toolbar.

   *   ![](images/FCGear_Drop-down-menu_example-en.png )
   *   
    
*The FCGear Drop down menu*
    

## Types of gears 

### Involute Gear 

   *   ![](images/Involute-Gear_example.png )
   *   
    
*From left to right   * Spur gearing, helical gearing, double helical gearing (see [FCGear InvoluteGear](FCGear_InvoluteGear.md))*
    

### Involute Rack 

   *   ![](images/Involute-Rack_example.png )
   *   
    
*From left to right   * Spur gearing, helical gearing, double helical gearing (See [FCGear InvoluteRack](FCGear_InvoluteRack.md))*
    

### Cycloide Gear 

   *   ![](images/Cycloid-Gear_example_1.png )
   *   
    
*From left to right   * Spur gearing, helical gearing, double helical gearing (see [FCGear CycloideGear](FCGear_CycloideGear.md))*
    

### Bevel Gear 

   *   ![](images/Bevel-Gear_example.png )
   *   
    
*From left to right   * Spur gearing, spiral gearing (see [FCGear BevelGear](FCGear_BevelGear.md))*
    

### Worm Gear 

   *   ![](images/Worm-Gear_example.png )
   *   
    
*Above   * Worm gear (see [FCGear WormGear](FCGear_WormGear.md))*
    

### Crown Gear 

   *   ![](images/Crown-Gear_example.png )
   *   
    
*Above   * Crown gear (see [FCGear CrownGear](FCGear_CrownGear.md))*
    

### Timing Gear and Lantern Gear 

   *   ![](images/Timing+Latern-gear_example.png )
   *   
    
*From left to right   * Timing gearing, lantern gearing (see [FCGear TimingGear](FCGear_TimingGear.md) or [FCGear LanternGear](FCGear_LanternGear.md))*
    

## References

-   Author   * looooo
-   Home page   * <https   *//github.com/looooo/FCGear>
-   Source code on github   * <https   *//github.com/looooo/FCGear>

## Tools

### Toolbar

-   <img alt="" src=images/FCGear_InvoluteGear.svg  style="width   *32px;"> [FCGear InvoluteGear](FCGear_InvoluteGear.md) Creates an Involute gear
-   <img alt="" src=images/FCGear_InvoluteRack.svg  style="width   *32px;"> [FCGear InvoluteRack](FCGear_InvoluteRack.md) Creates an Involute rack
-   <img alt="" src=images/FCGear_CycloideGear.svg  style="width   *32px;"> [FCGear CycloideGear](FCGear_CycloideGear.md) Creates a Cycloide gear
-   <img alt="" src=images/FCGear_BevelGear.svg  style="width   *32px;"> [FCGear BevelGear](FCGear_BevelGear.md) Creates a Bevel gear
-   <img alt="" src=images/FCGear_WormGear.svg  style="width   *32px;"> [FCGear WormGear](FCGear_WormGear.md) Creates a Worm gear
-   <img alt="" src=images/FCGear_CrownGear.svg  style="width   *32px;"> [FCGear CrownGear](FCGear_CrownGear.md) Creates a Crown gear
-   <img alt="" src=images/FCGear_TimingGear.svg  style="width   *32px;"> [FCGear TimingGear](FCGear_TimingGear.md) Creates a Timing gear
-   <img alt="" src=images/FCGear_LanternGear.svg  style="width   *32px;"> [FCGear LanternGear](FCGear_LanternGear.md) Creates a Lantern gear

## Installation

### Automatic installation 

The recommended method of installation as of v0.17 is via the <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Addon Manager](Std_AddonMgr.md). It can be found in the 
**Tools → Addon Manager**


<div class="mw-collapsible mw-collapsed toccolours" style="width   *700px">

### Manual installation 

If there is a necessity to manually install this workbench the following instructions are provided to do so   *


<div class="mw-collapsible-content">

#### Linux

-    `git clone https   *//github.com/looooo/FCGear.git`
    

-   link or copy the folder into **/freecad/Mod**

   *   

       *   
        `sudo ln -s (path_to_FCGear) (path_to_freecad)/Mod`
        

#### Windows

Tested on (7/8/8.1/10) (From GitHub)

-   download ZIP-archive by clicking on button in top right corner
-   go to FreeCAD-Macro-Folder (inside FreeCAD, choose \"Edit \> Preferences \> General \> Macro to see Macro Path)
-   if you haven\'t changed the standard settings, it should be \"C   *Users\\Your\_Windows\_User\_Name\\AppData\\Roaming\\FreeCAD\"
-   \\appdata is a HIDDEN folder, so you may have to change the settings of the file explorer to see it
-   create a sub-folder called \"FCGear\"
-   make sure to copy files and folders EXACTLY as shown above to the just created sub-folder
-   restart FreeCAD and the workbench should appear in the pull-down menu
-   within FreeCAD you can choose \"Tools \> Customize \> Workbenches\" to enable/disable workbenches

#### MacOSX

See instructions for Linux above


</div>


</div>

## Links to Gear WB 

-   Workbench Wiki   * <https   *//github.com/looooo/FCGear/wiki>
-   FreeCAD Wiki   * [Macro\_FCGear](http   *//www.freecadweb.org/wiki/index.php?title=Macro_FCGear) and [Bevel gear](http   *//forum.freecadweb.org/viewtopic.php?f=3&t=12878)
-   FreeCAD Forum   * <http   *//forum.freecadweb.org/viewtopic.php?f=21&t=12968>
-   Tutorials   *
-   Videos   *
-   Files   *
-   Report bugs   * Please report bugs at <https   *//github.com/looooo/FCGear/issues>

## Other useful links 

-   <img alt="PartDesign\_InvoluteGear" src=images/PartDesign_InvoluteGear.svg  style="width   *24px;"> [PartDesign InvoluteGear](PartDesign_InvoluteGear.md)   * This tool allows for the creation of a 2D profile of an Involute gear. This 2D profile is fully parametric, and can be padded with the [PartDesign Pad](PartDesign_Pad.md) feature.
-   [External Workbenches](External_workbenches.md)   * A list of all current external workbenches of FreeCAD
-   [Macros recipes](Macros_recipes.md)
-   [The cycloidal gearing (german)](https   *//vivat-geo.de/zykloidenverzahnung.html)
-   [Involute gearing (german)](https   *//vivat-geo.de/evolventenverzahnung.html)




[Category   *External Workbenches](Category_External_Workbenches.md) [Category   *Addons](Category_Addons.md) [Category   *FCGear](Category_FCGear.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [External Workbenches](Category_External Workbenches.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > FCGear Workbench/en

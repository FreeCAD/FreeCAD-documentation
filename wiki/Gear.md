# Gear
{{TOCright}}



## Introduction

This page is intended to differentiate some kind of gears by their (hopefully) correct names.
There will be not much information about the design in detail; there are enough proper descriptions in the wiki pages and elsewhere in the www.

## Gear

A Gear is a toothed wheel that can be paired with other gears, racks, chains, or belts to form a **gear train** (which is usually called a gear as well).

Native speakers, feel invited to add local synonyms, or spelling variations

### Bevel gear 

A bevel gear meshes with another bevel gear to connect two angled rotation axes.

<img alt="" src=images/Gear_Example-08.png  style="width   *200px;"> 
*Two meshing bevel gears*

The <img alt="" src=images/FCGear_BevelGear.svg  style="width   *24px;"> [FCGear BevelGear](FCGear_BevelGear.md) tool creates a basic bevel gear, a solid object that needs to be trimmed to shape in following steps.

<img alt="" src=images/Gear_Example-06.png  style="width   *200px;"> <img alt="" src=images/Gear_Example-07.png  style="width   *200px;"> 
*Left   * Raw bevel gears as created with [FCGear BevelGear](FCGear_BevelGear.md). Right   * Bevel gears trimmed to a more recognisable shape.*

### Cage gear 

See [lantern gear](#Lantern_gear.md).

### Chain wheel 

The driving gear (attached to the crank arms) of a bicycle drivetrain is usually called a chain wheel. See cog wheel and [sprocket](#Sprocket.md).

### Cog

The driven gear (attached to the rear wheel) of a bicycle drivetrain is usually called a cog. See cog wheel and [sprocket](#Sprocket.md).

### Cog wheel 

A cog wheel, or cogged wheel, is an assembly of a hub(?) and several inserted teeth, the actual cogs.

<img alt="" src=images/Gear_Example-01.png  style="width   *200px;"> 
*Cog wheel and a single cog ready to get inserted)*

Early wooden cog wheels were used to drive [lantern gears](#Lantern_gear.md). See [gear trains](#Cog_wheel_and_lantern_gear.md).
The cogs could have other angles than 90° relative to the axis to build angled gear trains   *

<img alt="" src=images/Gear_Example-04.png  style="width   *200px;"> 
*Large cog wheel resembling a Crown gear*

Cog wheels have been replaced with single body gears that are called [sprockets](#Sprocket.md) if they mesh with cylindrical teeth such as the rollers of a (roller) chain, or ladder-like roller racks.

-   In case of a bicycle\'s drivetrain the driven sprocket is called **cog** and the driving one is called [chain wheel](#chain_wheel.md).
-   In connection with rack railways the gears were still called **cog wheels** or [pinions](#Pinion.md).

### Crown gear 

A crown gear is similar to a larger bevel gear, but meshes with spur gears instead of another bevel gear. See [Crown gear and spur gear](#Crown_gear_and_spur_gear.md).

<img alt="" src=images/Gear_Example-09.png  style="width   *200px;"> 
*Crown gear*

FreeCAD provides a tools to model crown gears   *

-   <img alt="" src=images/FCGear_CrownGear.svg  style="width   *24px;"> [FCGear CrownGear](FCGear_CrownGear.md)   * Creates a crown gear.

### Double helical gear 

A double helical gear has two symmetric rows of helical teeth that have an angle other than 90° to the axis of rotation. Double helical gears mesh with other double helical gears, double helical racks, or internal double helical gears.

FreeCAD provides two tools to model double helical gears   *

-   <img alt="" src=images/FCGear_InvoluteGear.svg  style="width   *24px;"> [FCGear InvoluteGear](FCGear_InvoluteGear.md)   * Creates an involute spur gear by default.
-   <img alt="" src=images/FCGear_CycloidGear.svg  style="width   *24px;"> [FCGear CycloidGear](FCGear_CycloidGear.md)   * Creates a cycloid spur gear by default.

### Helical gear 

A helical gear has helical teeth that have an angle other than 90° to the axis of rotation. Helical gears mesh with other helical gears, helical racks, or internal helical gears. See [Skew gears](#Skew_gears.md).

FreeCAD provides two tools to model helical gears   *

-   <img alt="" src=images/FCGear_InvoluteGear.svg  style="width   *24px;"> [FCGear InvoluteGear](FCGear_InvoluteGear.md)   * Creates an involute spur gear by default.
-   <img alt="" src=images/FCGear_CycloidGear.svg  style="width   *24px;"> [FCGear CycloidGear](FCGear_CycloidGear.md)   * Creates a cycloid spur gear by default.

### Internal gear 

The <img alt="" src=images/FCGear_InternalInvoluteGear.svg  style="width   *24px;"> [FCGear InternalInvoluteGear](FCGear_InternalInvoluteGear.md) tool creates an internal involute gear.

### Lantern gear 

A lantern gear is an assembly of a front plate(?) and a back plate(?) and several bolts called **rollers** connecting both plates.

This kind of gear looks similar to an ancient lantern or a bird cage, that\'s why it\'s called **lantern gear** or **cage gear**.

<img alt="" src=images/Gear_Example-02.png  style="width   *200px;"> 
*Lantern gear and a single roller ready to get inserted*

Early wooden lantern wheels were driven by [cog wheels](#Cog_wheel.md). See [cog wheel gear trains](#Cog_wheel_gear_trains.md).

### Pinion

Pinions are [sprockets](#Sprocket.md) that are paired with [racks](#Rack_and_pinion.md).

### Sprocket

A sprocket is a gear meshing with roller racks, roller chains, or timing belts, but not with another sprocket.

FreeCAD provides three tools to model sprockets   *

-   <img alt="" src=images/FCGear_TimingGear.svg  style="width   *24px;"> [FCGear TimingGear](FCGear_TimingGear.md)   * Sprockets for timing belts (timing pulleys, toothed pulleys), creates a solid object.
-   <img alt="" src=images/FCGear_LanternGear.svg  style="width   *24px;"> [FCGear LanternGear](FCGear_LanternGear.md)   * Sprockets for chains or racks (chain wheels, cogs, pinions), creates a solid object.
-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width   *24px;"> [PartDesign Sprocket](PartDesign_Sprocket.md)   * Sprockets for bike chains (chain wheels, cogs), creates just an outline.

### Spur gear 

A spur gear has straight teeth that are aligned parallel to the axis of rotation. Spur gears mesh with other spur gears, racks, or internal gears.

FreeCAD provides two tools to model spur gears   *

-   <img alt="" src=images/FCGear_InvoluteGear.svg  style="width   *24px;"> [FCGear InvoluteGear](FCGear_InvoluteGear.md)   * Creates an involute spur gear by default.
-   <img alt="" src=images/FCGear_CycloidGear.svg  style="width   *24px;"> [FCGear CycloidGear](FCGear_CycloidGear.md)   * Creates a cycloid spur gear by default.

### Timing pulley 

Timing (belt) pulleys or or toothed pulleys are [sprockets](#Sprocket.md) to use with timing belts.

### Worm gear 

The <img alt="" src=images/FCGear_WormGear.svg  style="width   *24px;"> [FCGear WormGear](FCGear_WormGear.md) tool creates a WormGear.

## Racks

A Rack is like a gear segment having an infinite radius.

### Cycloid rack 

<img alt="" src=images/Gear_Example-12.png  style="width   *200px;"> 
*Cycloid rack*

FreeCAD provides a tool to model cycloid racks for spur gearing, helical gearing, and double helical gearing   *

-   <img alt="" src=images/FCGear_CycloidRack.svg  style="width   *24px;"> [FCGear CycloidRack](FCGear_CycloidRack.md)   * Creates a cycloid rack for spur gearing by default.

### Involute rack 

<img alt="" src=images/Gear_Example-11.png  style="width   *200px;"> 
*Involute rack*

FreeCAD provides a tool to model involute racks for spur gearing, helical gearing, and double helical gearing   *

-   <img alt="" src=images/FCGear_InvoluteRack.svg  style="width   *24px;"> [FCGear InvoluteRack](FCGear_InvoluteRack.md)   * Creates an involute rack for spur gearing by default.

### Roller rack 

## Gear trains 

### Cog wheel and lantern gear 

<img alt="" src=images/Gear_Example-GT-01.gif  style="width   *200px;"> 
*A [cog wheel](#Cog_wheel.md) on the left meshes with a [lantern gear](#Lantern_gear.md) (with its front plate removed) on the right*

<img alt="" src=images/Gear_Example-GT-02.gif  style="width   *200px;"> <img alt="" src=images/Gear_Example-05.png  style="width   *200px;"> 
*A large [cog wheel](#Cog_wheel.md) in the background (similar to a [crown gear](#Crown_gear.md)) meshes with a [lantern gear](#Lantern_gear.md)*

### Cog wheel and roller rack 

See [Rack and pinion](#Rack_and_pinion.md).

### Crown gear and spur gear 

<img alt="" src=images/Gear_Example-10.png  style="width   *200px;"> 
*A [crown gear](#Crown_gear.md) meshes with a [spur gear](#Spur_gear.md)*

### Skew gears 

<img alt="" src=images/Gear_Example-GT-03.gif  style="width   *200px;"> 
*Skew gears are paired [helical gears](#Helical_gear.md) having non-parallel and offset axes of rotation*

### Sprocket and chain 

### Rack and pinion 

<img alt="" src=images/Gear_Example-03.png  style="width   *200px;"> 
*A [pinion](#Pinion.md) (or cog wheel) meshes with a (ladder-like) roller rack*

### Rack and spur gear 

<img alt="" src=images/Gear_Example-13.png  style="width   *200px;"> <img alt="" src=images/Gear_Example-14.png  style="width   *200px;"> 
*A [spur gear](#Spur_gear.md) meshes with a rack. Left   * Cycloid gearing. Right   * Involute gearing*



---
![](images/Right_arrow.png) [documentation index](../README.md) > Gear

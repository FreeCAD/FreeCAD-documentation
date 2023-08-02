---
- GuiCommand:
   Name: FCGear WormGear
   MenuLocation: Gear -> Worm Gear
   Workbenches: FCGear_Workbench
   Shortcut: None
   Version: v0.16
   SeeAlso: PartDesign_InvoluteGear
---

# FCGear WormGear/en

## Description

The worm can be considered a special case of a helical gear. Imagine that there is only one tooth on a spur gear. Now increase the helix angle so much that the tooth winds around the spur gear several times before it emerges on the opposite side. The result would be a single thread worm.

For a single-start worm, each full turn (360 degrees) of the worm advances the gear by one tooth. So a gear with 24 teeth will provide a gear reduction of 24:1. For a multi-start worm, the gear reduction equals the number of teeth on the gear, divided by the number of starts on the worm.

A worm can only be used with a worm wheel. This is called a worm drive. Like other gear arrangements, a worm drive can reduce rotational speed or transmit higher torque. One of the major advantages of worm gear drive units are that they can transfer motion in 90 degrees. A worm drive is also self-locking.

![](images/Worm-Gear_example.png ) 
*Worm gear (No. of teeth 3)*

## Usage

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  There are several ways to invoke the command:
    -   Press the **[<img src=images/FCGear_WormGear.svg style="width:16px"> [Worm Gear](FCGear_WormGear.md)** button in the toolbar.
    -   Select the **Gear → [<img src=images/FCGear_WormGear.svg style="width:16px"> Worm Gear** option from the menu.
3.  Change the gear parameter to the required conditions (see [Properties](#Properties.md)).

## Properties

An FCGear WormGear object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|base}}

-    **diameter|Length**: Default is {{Value|5 mm}}. Pitch diameter.

-    **height|Length**: Default is {{Value|5 mm}}. Value of the worm length.

-    **module|Length**: Default is {{Value|1 mm}}. Module is the ratio of the reference diameter of the gear divided by the number of teeth (see [Notes](#Notes.md)).

-    **reverse_pitch|Bool**: Default is {{False}}, {{True}} changes the rotating direction from right to left.

-    **teeth|Integer**: Default is {{Value|3}}. Number of teeth (see [Notes](#Notes.md)).


{{Properties_Title|computed}}

-    **beta|Angle**: (read-only) Lead angle (see also the information in [Notes](#Notes.md) and [Useful formulas](#Useful_formulas.md)).


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: Default is {{Value|20 °}} (see [Notes](#Notes.md)).


{{Properties_Title|tolerance}}

-    **clearance|Float**: Default is {{Value|0.25}} (see [Notes](#Notes.md)).

-    **head|Float**: Default is {{Value|0}}. This value is used to change the tooth height.


{{Properties_Title|version}}

-    **version|String**:

## Notes

-    **beta**: If the lead angle is less than 5°, it is a self-locking gear. A typical example are the tuning pegs on a guitar or ukulele.

-    **clearance**: At a worm gearing, clearance is the distance between the tooth tip of the worm and the tooth root of the worm wheel.

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth. If the module is changed, the lead angle also changes (**beta**).

-    **teeth**: The number of teeth in a worm is called the number of threads. Correspondingly, one speaks of single, double or multiple thread worms. In general, mainly single worms are produced, but in special cases the number of starts can be up to four (sometimes also more). If the number of teeth is changed, **beta** also changes.

-    **pressure_parameter**: Only change the parameter, if sufficient knowledge of the gear geometry is available.

## Useful formulas 

-    **beta (lead angle)**= arctan (**module** \* **teeth** : **pitchdiameter (diameter)**)

-    **axial pitch**= **pi** \* **module** \* **teeth**

-    **beta (lead angle)**= arctan (**axial pitch** : (**pitchdiameter (diameter)** \* **pi**))

-    **worm length**= 4,5 \* **module** \* **pi**

## Worm wheel 

The worm wheel must be designed manually. For this purpose [FCGear InvoluteGear](FCGear_InvoluteGear.md) can be used for a simple construction. In any case, in-depth knowledge of the gear types is required.

![](images/Worm-Gear_example3.png ) 
*Worm with worm wheel*



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear WormGear/en

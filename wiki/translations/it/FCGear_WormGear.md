---
- GuiCommand:/it
   Name:FCGear WormGear
   Name/it:Vite senza fine
   MenuLocation:FCGear → Create a Worm gear
   Workbenches:[FCGear](FCGear_Workbench/it.md)
   Shortcut:None
   Version:v0.16
   SeeAlso:[PartDesign: Ingranaggio a spirale](PartDesign_InvoluteGear/it.md)
---

## Descrizione

The worm can be considered a special case of a helical gear. Imagine that there is only one tooth on a spur gear. Now increase the helix angle so much that the tooth winds around the spur gear several times before it emerges on the opposite side. The result would be a single thread worm.

For a single-start worm, each full turn (360 degrees) of the worm advances the gear by one tooth. So a gear with 24 teeth will provide a gear reduction of 24:1. For a multi-start worm, the gear reduction equals the number of teeth on the gear, divided by the number of starts on the worm.

A worm can only be used with a worm wheel. This is called a worm drive. Like other gear arrangements, a worm drive can reduce rotational speed or transmit higher torque. One of the major advantages of worm gear drive units are that they can transfer motion in 90 degrees. A worm drive is also self-locking.

:   ![](images/Worm-Gear_example.png )
:   
    *Worm gear (No. of teeth 3)*
    

## Usage

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width:22px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  Invoke the command several way:
    -   Press the <img alt="" src=images/FCGear_WormGear.svg  style="width:22px;"> [Create a Worm gear](FCGear_WormGear.md) button in the tool bar.
    -   Using the **Gear Menu → Worm gear**.
3.  Change the gear parameter to the required conditions (see **Properties → Data** below).

## Properties

### Data


{{Properties_Title|Base}}

-    **Placement**: [Placement](Placement.md) is the location and orientation of an object in space.

-    **Label**: User name of the object in the [Tree view](Tree_view.md).


{{Properties_Title|gear_parameter}}

-    **beta**: Lead angle, not changeable - is calculated automatically (see also the information in **Notes** and **Useful formulas**).

-    **clearance**: Default is 0,25 (see also the information in **Notes**).

-    **diameter**: Pitch diameter.

-    **head**: Default is 0,00. This value is used to change the tooth height.

-    **height**: Value of the worm length.

-    **module**: Module is the ratio of the reference diameter of the gear divided by the number of teeth (see also the information in **Notes**).

-    **reverse_pitch**: **True** change the rotating direction from right to left.

-    **teeth**: Number of teeth (see also the information in **Notes**).


{{Properties_Title|involute_parameter}}

-    **pressure_parameter**: Default is 20 (see also the information in **Notes**).

### View

The parameter descriptions of the **View** tab will be found in [Property editor](Property_editor.md), further below at **Example of the properties of a PartDesign object**.

## Notes

-    **beta**: If the lead angle is less than 5°, it is a self-locking gear. A typical example are the tuning pegs on a guitar or ukulele.

-    **clearance**: At a worm gearing, clearance is the distance between the tooth tip of the worm and the tooth root of the worm wheel.

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth. If the module is changed, the lead angel also changes (**beta**).

-    **teeth**: The number of teeth in a worm is called the number of threads. Correspondingly, one speaks of single, double or multiple thread worms. In general, mainly single worms are produced, but in special cases the number of starts can be up to four (sometimes also more). If the number of teeth is changed, **beta** also changes.

-    **pressure_parameter**: Only change the parameter, if sufficient knowledge of the gear geometry is available.

## Limitations

Limitations are not known yet.

## Useful formulas 

-    **beta (lead angle)**= arctan (**module** \* **teeth** : **pitchdiameter (diameter)**)

-    **axial pitch**= **pi** \* **module** \* **teeth**

-    **beta (lead angle)**= arctan (**axial pitch** : (**pitchdiameter (diameter)** \* **pi**))

-    **worm length**= 4,5 \* **module** \* **pi**

## Worm wheel 

The worm wheel must be designed manually. For this purpose **FCGear InvoluteGear** can be used for a simple construction. In any case, in-depth knowledge of the gear types is required.

:   ![](images/Worm-Gear_example3.png )
:   
    *Worm with worm wheel*
    




[Category:Addons](Category:Addons.md) [Category:FCGear](Category:FCGear.md) [Category:External Command Reference](Category:External_Command_Reference.md)

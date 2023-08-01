---
- GuiCommand:
   Name: FCGear LanternGear
   MenuLocation: Gear - Lantern Gear
   Workbenches: [FCGear](FCGear_Workbench.md)
   Shortcut: None
   Version: v0.16
   SeeAlso: 
---

# FCGear LanternGear/ru

## Описание

The lantern gear toothing is a special form of cycloidal toothing in which the rolling circle and pitch circle are of equal size. In addition, the teeth of the larger wheel in a gearbox are replaced by cylinders. The small wheel is given a cycloid gearing. This results in a one-sided point gearing. Lantern gearings can only be straight toothed.

Because their construction is very simple, they are among the oldest forms of gearing. Lantern gearings are used when large gear ratios are required, for example in the slewing gears of mills or timber handling cranes.

Lantern gear wheel with roller chains are a cost-effective and robust alternative to rack and pinion drives. By guiding the stretched lantern gear wheel chain tangentially along the lantern gear wheel, a linear movement of the chain is converted into a rotational movement of the wheel. Conversely, a linear motion of the chain can also be achieved by the rotary motion of the lantern gear wheel (motorbike/bicycle).

![](images/Lantern-Gear_example.png ) 
*Above: Lantern gear*

## Usage

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  There are several ways to invoke the command:
    -   Press the **[<img src=images/FCGear_LanternGear.svg style="width:16px"> [Lantern Gear](FCGear_LanternGear.md)** button in the toolbar.
    -   Select the **Gear → [<img src=images/FCGear_LanternGear.svg style="width:16px"> Lantern Gear** option from the menu.
3.  Change the gear parameter to the required conditions (see [Properties](#Properties.md)).

## Properties

### Data

An FCGear LanternGear object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:


{{Properties_Title|accuracy}}

-    **num_profiles|Integer**: Default is {{Value|10}}. The value normally does not need to be changed.


{{Properties_Title|base}}

-    **bolt_radius|Length**: Default is {{Value|1 mm}}. Diameter of the cylinder on the rotating disc which functions as a second \"gear wheel\".

-    **height|Length**: Default is {{Value|5 mm}}. Value of the gear width.

-    **module|Length**: Default is {{Value|1 mm}}. Module is the ratio of the reference diameter of the gear divided by the number of teeth (see [Notes](#Notes.md)).


{{Properties_Title|gear_parameter}}

-    **teeth|Integer**: Default is {{Value|15}}. Number of teeth.


{{Properties_Title|tolerance}}

-    **head|Float**: Default is {{Value|0}}.


{{Properties_Title|version}}

-    **version|String**:

## Notes

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth.

## Useful formulas 

-    **addendum diameter**= **module** \* **(teeth +2)**

-    **pitch diameter**= **module** \* **teeth**

-    **axle base**= **pitch diameter (lantern gear 1 + 2)** : 2



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear LanternGear/ru

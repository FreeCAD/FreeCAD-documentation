---
- GuiCommand:
   Name:FCGear LanternGear
   MenuLocation:FCGear → Create a Lantern gear
   Workbenches:[FCGear](FCGear_Workbench.md)
   Shortcut:None
   Version:v0.16
   SeeAlso:
---

## Description

The lantern gear toothing is a special form of cycloidal toothing in which the rolling circle and pitch circle are of equal size. In addition, the teeth of the larger wheel in a gearbox are replaced by cylinders. The small wheel is given a cycloid gearing. This results in a one-sided point gearing. Lantern gearings can only be straight toothed.

Because their construction is very simple, they are among the oldest forms of gearing. Lantern gearings are used when large gear ratios are required, for example in the slewing gears of mills or timber handling cranes.

Lantern gear wheel with roller chains are a cost-effective and robust alternative to rack and pinion drives. By guiding the stretched lantern gear wheel chain tangentially along the lantern gear wheel, a linear movement of the chain is converted into a rotational movement of the wheel. Conversely, a linear motion of the chain can also be achieved by the rotary motion of the lantern gear wheel (motorbike/bicycle).

:   ![](images/Latern_Gear_example.png )
:   
    *Above: Lantern gear*
    

## Usage

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width:22px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  Invoke the command several way:
    -   Press the <img alt="" src=images/FCGear_LaternGear.svg  style="width:22px;"> [Create a Lantern gear](FCGear_LanternGear.md) button in the tool bar.
    -   Using the **Gear Menu → Lantern gear**.
3.  Change the gear parameter to the required conditions (see **Properties → Data** below).

## Properties

### Data


{{Properties_Title|Base}}

-    **Placement**: [Placement](Placement.md) is the location and orientation of an object in space.

-    **Label**: User name of the object in the [Tree view](Tree_view.md).


{{Properties_Title|accuracy}}

-    **num_profiles**: Default is 10. The value normally does not need to be changed.


{{Properties_Title|gear_parameter}}

-    **bolt_radius**: Default is 1,00 mm. Diameter of the cylinder on the rotating disc which functions as a second \"gear wheel\".

-    **height**: Default is 5,00 mm. Value of the gear width.

-    **module**: Default is 1,00 mm. Module is the ratio of the reference diameter of the gear divided by the number of teeth (see also the information in **Notes**.

-    **teeth**: Default is 15. Number of teeth.

### View

The parameter descriptions of the **View** tab will be found in [Property editor](Property_editor.md), further below at **Example of the properties of a PartDesign object**.

## Notes

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth.

## Limitations

Limitations are not known yet.

## Useful formulas 

-    **addendum diameter**= **module** \* **(teeth +2)**

-    **ptch diameter**= **module** \* **teeth**

-    **axle base**= **pitch diameter (lantern gear 1 + 2)** : 2




[Category:Addons](Category:Addons.md) [Category:FCGear](Category:FCGear.md) [Category:External Command Reference](Category:External_Command_Reference.md)

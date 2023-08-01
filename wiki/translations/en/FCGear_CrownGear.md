---
- GuiCommand:
   Name:FCGear CrownGear
   MenuLocation:Gear → Crown Gear
   Workbenches:[FCGear](FCGear_Workbench.md)
   Shortcut:None
   Version:v0.16
   SeeAlso:[FCGear InvoluteGear](FCGear_InvoluteGear.md)
---

# FCGear CrownGear/en

## Description

The crown wheel resembles a ring-shaped curved rack. The pressure angle decreases continuously from the outer to the inner diameter. Thus, the variable peripheral speed at the crown wheel is compensated against the constant peripheral speed of the pinion. The pointed outer teeth and the steep tooth flanks on the inner diameter limit the usable tooth width. Crown gears achieve similar efficiencies as spur gears. One crown gear can drive several pinions.

Known field of application of crown gears:

-   Rear axle drives for cars and motorcycles
-   Swivel mechanism for operating tables
-   Angular milling heads
-   Powered tool systems with multiple pinions and a crown gear

![](images/Crown-Gear_example.png ) 
*Above: Crown gear*

## Usage

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  There are several ways to invoke the command:
    -   Press the **[<img src=images/FCGear_CrownGear.svg style="width:16px"> [Crown Gear](FCGear_CrownGear.md)** button in the toolbar.
    -   Select the **Gear → [<img src=images/FCGear_CrownGear.svg style="width:16px"> Crown Gear** option from the menu.
3.  The crown gear is displayed without teeth by default. (<small>(v0.21)</small> )
4.  Change the gear parameters to the required conditions (see [Properties](#Properties.md)).
5.  Set the **preview_mode** property to {{false}} to display the teeth (see [Notes](#Notes.md)).

## Properties

An FCGear CrownGear object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|accuracy}}

-    **num_profiles|Integer**: Default is {{Value|4}}. Number of profiles used for loft.

-    **preview_mode|Bool**: Default is {{True}}.


{{Properties_Title|base}}

-    **height|Length**: Default is {{Value|2 mm}}. Value for the tooth width.

-    **module|Length**: Default is {{Value|1 mm}}. Module is the ratio of the reference diameter of the gear divided by the number of teeth (see [Notes](#Notes.md)).

-    **other_teeth|Integer**: Default is {{Value|15}}. Number of teeth of the construction gear (pinion) (see [Notes](#Notes.md)).

-    **teeth|Integer**: Default is {{Value|15}}. Number of teeth.

-    **thickness|Length**: Default is {{Value|5 mm}}. Height from the tip of tooth to the lower side of the crown wheel.


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: Default is {{Value|20 °}} (see [Notes](#Notes.md)).


{{Properties_Title|version}}

-    **version|String**:

## Notes

-   The **preview_mode** property is set to {{true}} by default and when the gear is created you\'ll find this message in the report view:

    :   *Gear module: Crown gear created, preview_mode = true for improved performance. Set preview_mode property to false when ready to cut teeth.*

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth.

-    **other_teeth**: Several pinions with the same number of teeth only can be used on one crown wheel.

-    **pressure_parameter**: Only change the parameter, if sufficient knowledge of the gear geometry is available.

-   The geometry of the crown gear is primarily determined by the spur pinion geometry (**other_teeth**).

-   Create spur gear with [Involute gear](FCGear_InvoluteGear.md). The number of teeth must be identical to the parameter **other_teeth** of the crown gear.

-   Adjustments for optimal running characteristics can be made with the parameters of involute gear.

## Crown and spur gear set overview 

![](images/Crown-spur-gear-set_example.png )

-   \(1\) Spur gear
-   \(2\) Crown gear
-   \(3\) Tooth width
-   \(4\) Inner diameter
-   \(5\) Outer diameter

## Useful formulas 

-   **Inner diameter (4)**
    -   
        **inner diamter**
        
        = **module (spur gear)** \* **teeth (crown gear)** \* **cos pressure_paramter (pinion)** : **cos pressure_parameter (crown gear)**

-   **Outer diameter (5)**
    -   
        **outer diamter**
        
        = **inner diameter** + **2x height (tooth width crown gear)**



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear CrownGear/en

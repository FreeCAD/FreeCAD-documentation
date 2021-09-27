---
- GuiCommand:/it
   Name:FCGear CrownGear
   Name/it:Corona dentata
   MenuLocation:FCGear → Create an Crown gear
   Workbenches:[FCGear](FCGear_Workbench/it.md)
   Shortcut:None
   Version:v0.16
   SeeAlso:[Ingranaggi a evolvente](FCGear_InvoluteGear/it.md)
---

# FCGear CrownGear/it

## Descrizione

The crown wheel resembles a ring-shaped curved rack. The pressure angle decreases continuously from the outer to the inner diameter. Thus, the variable peripheral speed at the crown wheel is compensated against the constant peripheral speed of the pinion. The pointed outer teeth and the steep tooth flanks on the inner diameter limit the usable tooth width. Crown gears achieve similar efficiencies as spur gears. One crown gear can drive several pinions.

Known field of application of crown gears:

-   Rear axle drives for cars and motorcycles
-   Swivel mechanism for operating tables
-   Angular milling heads
-   Powered tool systems with multiple pinions and a crown gear

:   ![](images/Crown-Gear_example.png )
:   
    *Above: Crown gear*
    

## Usage

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width:22px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  Invoke the command several way:
    -   Press the <img alt="" src=images/FCGear_CrownGear.svg  style="width:22px;"> [Create a Crown gear](FCGear_CrownGear.md) button in the tool bar.
    -   Using the **Menu → Crown gear**.
3.  Change the gear parameter to the required conditions (see **Properties → Data** below).

## Properties

### Data


{{Properties_Title|Base}}

-    **Placement**: [Placement](Placement.md) is the location and orientation of an object in space.

-    **Label**: User name of the object in the [Tree view](Tree_view.md).


{{Properties_Title|accuracy}}

-    **construct**: Default is **True**. Change to **False** and the construction component disappears. **construct** belongs to **other_teeth**.

-    **num_profiles**: Number of profiles used for loft.


{{Properties_Title|gear_parameter}}

-    **height**: Value for the tooth width.

-    **module**: Module is the ratio of the reference diameter of the gear divided by the number of teeth (see also the information in **Note**).

-    **other_teeth**: Number of teeth of the **construction** gear (pinion). See also the information in **Note**.

-    **teeth**: Number of teeth

-    **thickness**: Height from the tip of tooth to the lower side of the crown wheel.


{{Properties_Title|involute_parameter}}

-    **pressure_parameter**: Default is 20 (see also the information in **Note**).

### View

The parameter descriptions of the **View** tab will be found in [Property editor](Property_editor.md), further below at **Example of the properties of a PartDesign object**.

## Notes

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth.

-    **other_teeth**: Several pinions with the same number of teeth only can be used on one crown wheel.

-    **pressure_parameter**: Only change the parameter, if sufficient knowledge of the gear geometry is available.

-   The geometry of the crown gear is primarily determined by the spur pinion geometry (**other_teeth**).

-   Create spur gear with <img alt="" src=images/FCGear_InvoluteGear.svg  style="width:22px;"> [Involute gear](FCGear_InvoluteGear.md). The number of teeth must be identical to the parameter **other_teeth** of the crown gear.

-   Adjustments for optimal running characteristics can be made with the parameters of involute gear.

## Limitations

No limitations are known.

## Crown and spur gear set overview 

:   ![](images/Crown-spur-gear-set_example.png )

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




_ _ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > FCGear CrownGear/it

---
- GuiCommand:
   Name: FCGear BevelGear
   Name/it: Ingranaggio conico
   MenuLocation: FCGear -> Create a Bevel gear
   Workbenches: FCGear Workbench/it
   Version: 0.16
---

# FCGear BevelGear/it


</div>

## Descrizione

Partly because of the noise they generate, bevel gears are not used as often as other types of gear. But they are still used in certain sectors, such as food packaging and canned food, lawn and garden equipment, machines such as drills and mills, compression systems for the gas and oil market and flow control valves.

Spiral bevel gears have curved teeth to provide softer engagement and greater tooth to tooth contact compared to a straight bevel gear. This reduces the vibration and noise. They can be used at high speeds and are typically used in motorcycle and bicycle transmissions.

![](images/Bevel-Gear_example.png ) 
*From left to right: Spur gearing, spiral gearing*

## Usage

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  There are several ways to invoke the command:
    -   Press the **[<img src=images/FCGear_BevelGear.svg style="width:16px"> [Bevel Gear](FCGear_BevelGear.md)** button in the toolbar.
    -   Select the **Gear → [<img src=images/FCGear_BevelGear.svg style="width:16px"> Bevel Gear** option from the menu.
3.  Change the gear parameter to the required conditions (see [Properties](#Properties.md)).

## Properties

An FCGear BevelGear object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|base}}

-    **height|Length**: Default is {{Value|5}}. Value for the bevel gear width.

-    **module|Length**: Default is {{Value|1}}. Module is the ratio of the reference diameter of the gear divided by the number of teeth (see [Notes](#Notes.md)).

-    **reset_origin|Bool**: If {{True}} (default) the center of the axis is at the center of the bottom of the gear (see [Notes](#Notes.md)).

-    **teeth|Integer**: Default is {{Value|15}}. Number of teeth.


{{Properties_Title|computed}}

-    **angular_backlash|Angle**: (read-only)

-    **dw|Length**: (read-only) Working pitch diameter.


{{Properties_Title|helical}}

-    **beta|Angle**: Default is {{Value|0 °}}. With the helix angle β a helical bevel gear is created -- positive value → rotation direction right, negative value → rotation direction left.


{{Properties_Title|involute}}

-    **pitch_angle|Angle**: Default is {{Value|45 °}}. Angle of taper.


{{Properties_Title|involute_parameter}}

-    **pressure_angle|Angle**: Default is {{Value|20 °}} (see [Notes](#Notes.md)).


{{Properties_Title|precision}}

-    **numpoints|Integer**: Default is {{Value|6}}. Change of the involute profile. Changing the value can lead to unexpected results.


{{Properties_Title|tolerance}}

-    **backlash|Length**: Default is {{Value|0}}. Backlash, also called lash or play, is the distance between the teeth at a gear pair.

-    **clearance|Float**: Default is {{Value|0.1}} (see [Notes](#Notes.md)).


{{Properties_Title|version}}

-    **version|String**:

## Notes

-    **clearance**: At a gear pair, clearance is the distance between the tooth tip of the first gear and the tooth root of the second gear.

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth.

-    **reset_origin**: It can be advantageous for mounting purposes if the parameter is set to **false**. The origin of the body is then at the tip of the pitch cone.

-    **pressure_parameter**: Only change the parameter, if sufficient knowledge of the gear geometry is available.

## Useful formulas 

-    **pitch diameter**= **module** \* **teeth**

-    **addendum diameter**= **pitch diameter** + 2 \* **module** \* **cos reference cone angle**

-    **tip angle 1**= **(teeth 1 + 2)** \* **(cos reference cone angle 1)** : **(teeth 2 - 2)** \* **(sin reference cone angle 1)**

-    **tip angle 2**= **(teeth 2 + 2)** \* **(cos reference cone angle 2)** : **(teeth 1 - 2)** \* **(sin reference cone angle 2)**

-    **reference cone angle 1**= **(teeth 1)** : **(teeth 2)**

-    **reference cone angle 2**= **(teeth 2)** : **(teeth 1)**

-    **axis angle total**= **reference cone angle 1** + **reference cone angle 2**

Substantive reference cone angle \[TECH.\]


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear BevelGear/it

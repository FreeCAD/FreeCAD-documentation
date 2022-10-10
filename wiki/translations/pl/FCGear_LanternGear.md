---
- GuiCommand   *
   Name   *FCGear LanternGear
   MenuLocation   *Gear → Lantern Gear
   Workbenches   *[FCGear](FCGear_Workbench.md)
   Shortcut   *None
   Version   *v0.16
   SeeAlso   *
---

# FCGear LanternGear/pl

## Opis

Zębatka latarniowa jest specjalną formą zębatki cykloidalnej, w której koło toczne i koło podziałowe są równej wielkości. Ponadto zęby większego koła w przekładni są zastąpione przez cylindry. Małe koło otrzymuje zazębienie cykloidalne. W ten sposób powstaje jednostronne przełożenie punktowe. Przekładnie latarniowe mogą mieć tylko uzębienie proste.

Because their construction is very simple, they are among the oldest forms of gearing. Lantern gearings are used when large gear ratios are required, for example in the slewing gears of mills or timber handling cranes.

Lantern gear wheel with roller chains are a cost-effective and robust alternative to rack and pinion drives. By guiding the stretched lantern gear wheel chain tangentially along the lantern gear wheel, a linear movement of the chain is converted into a rotational movement of the wheel. Conversely, a linear motion of the chain can also be achieved by the rotary motion of the lantern gear wheel (motorbike/bicycle).

![](images/Latern_Gear_example.png ) 
*Above   * Lantern gear*

## Użycie

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width   *16px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  There are several ways to invoke the command   *
    -   Press the **[<img src=images/FCGear_LanternGear.svg style="width   *16px"> [Lantern Gear](FCGear_LanternGear.md)** button in the toolbar.
    -   Select the **Gear → [<img src=images/FCGear_LanternGear.svg style="width   *16px"> Lantern Gear** option from the menu.
3.  Change the gear parameter to the required conditions (see [Properties](#Properties.md)).

## Properties

### Data

An FCGear LanternGear object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties   *


{{Properties_Title|accuracy}}

-    **num_profiles|Integer**   * Default is {{Value|10}}. The value normally does not need to be changed.


{{Properties_Title|base}}

-    **bolt_radius|Length**   * Default is {{Value|1 mm}}. Diameter of the cylinder on the rotating disc which functions as a second \"gear wheel\".

-    **height|Length**   * Default is {{Value|5 mm}}. Value of the gear width.

-    **module|Length**   * Default is {{Value|1 mm}}. Module is the ratio of the reference diameter of the gear divided by the number of teeth (see [Notes](#Notes.md)).


{{Properties_Title|gear_parameter}}

-    **teeth|Integer**   * Default is {{Value|15}}. Number of teeth.


{{Properties_Title|tolerance}}

-    **head|Float**   * Default is {{Value|0}}.


{{Properties_Title|version}}

-    **version|String**   *

## Notes

-    **module**   * Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m)   * m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth.

## Useful formulas 

-    **addendum diameter**= **module** \* **(teeth +2)**

-    **pitch diameter**= **module** \* **teeth**

-    **axle base**= **pitch diameter (lantern gear 1 + 2)**    * 2




[Category   *Addons](Category_Addons.md) [Category   *FCGear](Category_FCGear.md) [Category   *External Command Reference](Category_External_Command_Reference.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear LanternGear/pl

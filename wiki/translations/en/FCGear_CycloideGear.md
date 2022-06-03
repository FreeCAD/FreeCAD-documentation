---
- GuiCommand   *
   Name   *FCGear CycloideGear
   MenuLocation   *FCGear → Create a Cycloide gear
   Workbenches   *[FCGear](FCGear_Workbench.md)
   Shortcut   *None
   Version   *v0.16
   SeeAlso   *[[FCGear InvoluteGear]]
---

# FCGear CycloideGear/en

## Description

Cycloidal gears are very sensitive to an inaccurate adjustment of the centre distance, which then leads to a change in the transmission ratio. For these reasons, cycloidal gears are hardly found in mechanical engineering but are only used in special cases such as in the watch industry, for roots type blowers or for the drive of gear racks.

![](images/Cycloid-Gear_example_1.png ) 
*From left to right   * Spur gearing, helical gearing, double helical gearing*

## Usage

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width   *22px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  Invoke the command several way   *
    -   Press the <img alt="" src=images/FCGear_CycloideGear.svg  style="width   *22px;"> [Create a Cycloide gear](FCGear_CycloideGear.md) button in the tool bar.
    -   Using the **Gear Menu → Cycloide gear**.
3.  Change the gear parameter to the required conditions (see **Properties → Data** below).

## Properties

### Data


{{Properties_Title|Base}}

-    **Placement**   * [Placement](Placement.md) is the location and orientation of an object in space.

-    **Label**   * User name of the object in the [Tree view](Tree_view.md).


{{Properties_Title|cycloid_parameter}}

-    **inner_diameter**   * Default is 5,00. Diameter of the rolling circle of hypocycloid, normalized by the **module** (see also the information in **Notes**).

-    **outer_diameter**   * Default is 5,00. Diameter of the rolling circle of epicycloid, normalized by the **module** (see also the information in **Notes**).


{{Properties_Title|gear_parameter}}

-    **backslash**   * Default is 0,00. Backlash, also called lash or play, is the distance between the teeths at a gear pair.

-    **beta**   * With the helix angle β a helical gear is created (positive value → rotation direction right, negative value → rotation direction left).

-    **clearance**   * Default is 0,25 (see also the information in **Notes**).

-    **double_helix**   * **True** creates a double helix gear (see also the information in **Notes**)

-    **head**   * Additional length of the tip of the teeth, normalized by the **module**. Default is 0.

-    **height**   * Value of the gear width.

-    **module**   * Module is the ratio of the reference diameter of the gear divided by the number of teeth (see also the information in **Notes**).

-    **numpoints**   * Default is 15, change of the involute profile. Changing the value can lead to unexpected results.

-    **teeth**   * Number of teeth.

### View

The parameter descriptions of the **View** tab will be found in [Property editor](Property_editor.md), further below at **Example of the properties of a PartDesign object**.

## Notes

-   Cycloidal gears must always be specially matched to each other and can generally not be exchanged at will   * In a gear pair, the value of **inner_diameter** on one gear must equal the **outer_diameter** on the other, and vice versa. See also the information in **Properties cycloid parameter view** below.

-    **clearance**   * At a gear pair, clearance is the distance between the tooth tip of the first gear and the tooth root of the second gear.

-    **double_helix**   * To use the double helical gearing the helix angle β (**beta**) for the helical gearing must first be entered.

-    **module**   * Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m)   * m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth.

## Special cases 

### Straight line as hypocycloid 

To obtain a straight line, directly towards the center, as hypocycloid, use the following [expression](Expressions.md) for the **inner_diameter**   * `teeth / 2`. Such a tooth form is often found in historical clockworks and thus called \"clock toothing\". A larger **clearance** makes the effect even more visible.

### Full hypocycloid/epicycloid as tooth 

To obtain a gear made of complete hypocycloid and epicycloid curves use the following [expressions](Expressions.md)   *

-    **inner_diameter**   * `0.5 + 1e-6`

-    **outer_diameter**   * `inner_diameter`

-    **clearance**   * `(-1 + inner_diameter/1mm) * 2`

-    **head**   * `(-1 + outer_diameter/1mm) * 2`

The reference diameter is *d = m \* z*, with *m* being the **module** and *z* being the **teeth**. For a complete hypocycloid, the rolling diameter has to be *d\_i = d / (z\*2) = m\*z / (z\*2)*. And if we now normalize this by the module, we get *d\_in = m\*z / (z\*2) / m = 1 / 2*. The additional explicit tolerance value (`1e-6` in the expression above) is required to overcome coincidence issues.

Now the cycloids\' rolling circle diameters have to match the gear\'s addedum/dedendum. The addendum, i.e. the tooth length above the reference circle, is 1 + **head**. The dedendum, i.e. the tooth length below the reference circle, is 1 + **clearance**. Both are normalized by the module, thus we need a head/clearance value of *1 - d\_in*. The additional ` / 1mm` and ` * 2` are required to overcome shortcomings already fixed in the development version of the FCGear Workbench, but porting those fixes back to the stable version may break existing models.

Such \"gears\" allow the the number of teeth to be as low as *two* and are used as rotary vanes in pumps or compressors (cf. [Roots-type Supercharger](https   *//en.wikipedia.org/wiki/Roots-type_supercharger)).

### Infinitely large epicycloid 

If the radius of the epicycloid\'s rolling circle becomes infinitely large, it becomes a rolling straight line. Such a degenerated epicycloid is called involute. Gears with such a tooth form are handled by the [involute gear](FCGear_InvoluteGear.md) command. It is by far the most common tooth form Today.

## Useful formulas 

For more information see <img alt="" src=images/FCGear_InvoluteGear.svg  style="width   *22px;"> [Involute gear](FCGear_InvoluteGear.md).

## Properties cycloid parameter view 

<img alt="" src=images/CycloidGear_inner-outer-diameter_2.svg  style="width   *400px;">




[Category   *Addons](Category_Addons.md) [Category   *FCGear](Category_FCGear.md) [Category   *External Command Reference](Category_External_Command_Reference.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear CycloideGear/en

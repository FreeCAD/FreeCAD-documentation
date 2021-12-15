---
- GuiCommand:
   Name:FCGear CycloideGear
   MenuLocation:FCGear → Create a Cycloide gear
   Workbenches:[FCGear](FCGear_Workbench.md)
   Shortcut:None
   Version:v0.16
   SeeAlso:[[FCGear InvoluteGear]]
---

# FCGear CycloideGear/de

## Beschreibung

Cycloidal gears are very sensitive to an inaccurate adjustment of the centre distance, which then leads to a change in the transmission ratio. For these reasons, cycloidal gears are hardly found in mechanical engineering but are only used in special cases such as in the watch industry, for roots type blowers or for the drive of gear racks.

![](images/Cycloid-Gear_example_1.png ) 
*From left to right: Spur gearing, helical gearing, double helical gearing*

## Anwendung

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width:22px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  Invoke the command several way:
    -   Press the <img alt="" src=images/FCGear_CycloideGear.svg  style="width:22px;"> [Create a Cycloide gear](FCGear_CycloideGear.md) button in the tool bar.
    -   Using the **Gear Menu → Cycloide gear**.
3.  Change the gear parameter to the required conditions (see **Properties → Data** below).

## Eigenschaften

### Data


{{Properties_Title|Base}}

-    **Placement**: [Placement](Placement.md) is the location and orientation of an object in space.

-    **Label**: User name of the object in the [Tree view](Tree_view.md).


{{Properties_Title|cycloid_parameter}}

-    **inner_diameter**: Default is 5,00. Rolling circle of hypocycloid (see also the information in **Notes**).

-    **outer_diameter**: Default is 5,00. Rolling circle of epicycloid (see also the information in **Notes**).


{{Properties_Title|gear_parameter}}

-    **backslash**: Default is 0,00. Backlash, also called lash or play, is the distance between the teeths at a gear pair.

-    **beta**: With the helix angle β a helical gear is created (positive value → rotation direction right, negative value → rotation direction left).

-    **clearance**: Default is 0,25 (see also the information in **Notes**).

-    **double_helix**: **True** creates a double helix gear (see also the information in **Notes**)

-    **height**: Value of the gear width.

-    **module**: Module is the ratio of the reference diameter of the gear divided by the number of teeth (see also the information in **Notes**).

-    **numpoints**: Default is 15, change of the involute profile. Changing the value can lead to unexpected results.

-    **teeth**: Number of teeth.

### Ansicht

The parameter descriptions of the **View** tab will be found in [Property editor](Property_editor.md), further below at **Example of the properties of a PartDesign object**.

## Hinweise

-   Cycloidal gears must always be specially matched to each other and can generally not be exchanged at will!

-   In a gear pair, both gears have the same values for **inner_diameter** and **outer_diameter**. See also the information in **Properties cycloid parameter view** below.

-    **clearance**: At a gear pair, clearance is the distance between the tooth tip of the first gear and the tooth root of the second gear.

-    **double_helix**: To use the double helical gearing the helix angle β (**beta**) for the helical gearing must first be entered.

-    **module**: Using ISO (International Organization for Standardization) guidelines, Module size is designated as the unit representing gear tooth-sizes. Module (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). If you multiply Module by Pi, you can obtain Pitch (p). Pitch is the distance between corresponding points on adjacent teeth.

## Begrenzungen

Limitations are not known yet.

## Hilfreiche Formeln 

For more information see <img alt="" src=images/FCGear_InvoluteGear.svg  style="width:22px;"> [Involute gear](FCGear_InvoluteGear.md).

## Eigenschaften Zykloidenparameter Ansicht 

<img alt="" src=images/CycloidGear_inner-outer-diameter_2.svg  style="width:400px;">




_ _ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > FCGear CycloideGear/de

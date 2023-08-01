---
- GuiCommand:
   Name:FCGear InternalInvoluteGear
   MenuLocation:Gear - Internal Involute Gear
   Workbenches:[FCGear](FCGear_Workbench.md)
   Shortcut:None
   Version:1.0
   SeeAlso:[FCGear InvoluteGear](FCGear_InvoluteGear.md)
---

# FCGear InternalInvoluteGear/en

## Description

<img alt="" src=images/FCGear_InternalInvoluteGear-01.png  style="width:300px;">



*Internal involute gears from left to right: Spur gearing, helical gearing, double helical gearing*

## Usage

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  There are several ways to invoke the command:
    -   Press the **[<img src=images/FCGear_InternalInvoluteGear.svg style="width:16px"> [Internal Involute Gear](FCGear_InternalInvoluteGear.md)** button in the toolbar.
    -   Select the **Gear → [<img src=images/FCGear_InternalInvoluteGear.svg style="width:16px"> Internal Involute Gear** option from the menu.
3.  Change the gear parameter to the required conditions (see [Properties](#Properties.md)).

## Properties

An FCGear InternalInvoluteGear object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|accuracy}}

-    **numpoints|Integer**: Default is {{value|6}}. Change of the involute profile. Changing the value can lead to unexpected results.


{{Properties_Title|base}}

-    **height|Length**: Default is {{value|5 mm}}. Value of the gear width.

-    **module|Length**: Default is {{value|1 mm}}. Module is the ratio of the reference diameter of the gear divided by the number of teeth (see [Notes](FCGear_InvoluteGear#Notes.md)).

-    **teeth|Integer**: Default is {{value|15}}. Number of teeth (see [Notes](FCGear_InvoluteGear#Notes.md)).

-    **thickness|Length**: Default is {{value|5 mm}}. Thickness of the uncut outer part of the gear.


{{Properties_Title|computed}}

-    **angular_backlash|Angle**: (read-only)

-    **da|Length**: (read-only) Inside diameter, measured at the addendum (the tip of the teeth).

-    **df|Length**: (read-only) Root diameter, measured at the foot of the teeth.

-    **dw|Length**: (read-only) Working pitch diameter.

-    **outside_diameter|Length**: (read-only) Outside diameter.

-    **transverse_pitch|Length**: (read-only) Pitch in the plane of rotation.


{{Properties_Title|fillets}}

-    **head_fillet|Float**: Default is {{value|0 mm}}.

-    **root_fillet|Float**: Default is {{value|0 mm}}.


{{Properties_Title|helical}}

-    **beta|Angle**: Default is {{value|0 °}}. With the helix angle β a helical gear is created -- positive value → rotation direction right, negative value → rotation direction left (see [Notes](FCGear_InvoluteGear#Notes.md)).

-    **double_helix|Bool**: Default is {{false}}, {{true}} creates a double helix gear (see [Notes](FCGear_InvoluteGear#Notes.md)).

-    **properties_from_tool|Bool**: Default is {{false}}. If {{true}} and **beta** is not zero, gear parameters are recomputed internally for the rotated gear.


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: Default is {{value|20 °}} (see [Notes](FCGear_InvoluteGear#Notes.md)).

-    **shift|Float**: Default is {{value|0}}. Generates a positive and negative profile shift (see [Notes](FCGear_InvoluteGear#Notes.md)).


{{Properties_Title|precision}}

-    **simple|Bool**: Default is {{false}}, {{true}} generates a simplified display (without teeth and only a cylinder in pitch diameter).


{{Properties_Title|tolerance}}

-    **backlash|Length**: Default is {{value|0 mm}}. Backlash, also called lash or play, is the distance between the teeth at a gear pair.

-    **clearance|Float**: Default is {{value|0.25}} (see [Notes](FCGear_InvoluteGear#Notes.md)).

-    **head|Float**: Default is {{value|-0.4 mm}}. This value is used to change the tooth height.

-    **reversed_backlash|Bool**: {{true}} backlash decrease or {{false}} (default) backlash increase (see [Notes](FCGear_InvoluteGear#Notes.md)).


{{Properties_Title|version}}

-    **version|String**:

## Notes

See [FCGear InvoluteGear](FCGear_InvoluteGear#Notes.md).

## Useful formulas 

See [FCGear InvoluteGear](FCGear_InvoluteGear#Useful_formulas.md).

## Scripting



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear InternalInvoluteGear/en

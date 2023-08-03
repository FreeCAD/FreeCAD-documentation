---
 GuiCommand:
   Name: FCGear CycloidRack
   MenuLocation: Gear , Cycloid Rack
   Workbenches: FCGear_Workbench
   Shortcut: None
   Version: 1.0
   SeeAlso: FCGear_CycloidGear
---

# FCGear CycloidRack/pl

## Opis

<img alt="" src=images/FCGear_CycloidRack-01.png  style="width:200px;">



*Cycloid racks from left to right: Spur gearing, helical gearing, double helical gearing*

## Użycie

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  There are several ways to invoke the command:
    -   Press the **[<img src=images/FCGear_CycloidRack.svg style="width:16px"> [Cycloid Rack](FCGear_CycloidRack.md)** button in the toolbar.
    -   Select the **Gear → [<img src=images/FCGear_CycloidRack.svg style="width:16px"> Cycloid Rack** option from the menu.
3.  Change the gear parameter to the required conditions (see [Properties](#Properties.md)).

## Properties

An FCGear CycloidRack object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:


{{Properties_Title|accuracy}}

-    **numpoints|Integer**: Default is {{value|15}}. Number of points for spline.


{{Properties_Title|base}}

-    **add_endings|bool**: If {{True}} (default), then the total length of the rack is teeth \* pitch. If {{False}}, then the rack starts with a tooth-flank.

-    **height|Length**: Default is {{value|5 mm}}. Value of the gear width.

-    **teeth|Integer**: Default is {{value|15}}. Number of teeth.

-    **thickness|Length**: Default is {{value|5 mm}}. Thickness of the uncut part of the rack.


{{Properties_Title|computed}}

-    **transverse_pitch|Length**: (read-only) Pitch in the transverse plane.


{{Properties_Title|cycloid}}

-    **inner_diameter|Float**: Default is {{value|7.5}}. Diameter of the rolling circle of hypocycloid, normalized by the **module** (see [Notes](FCGear_CycloidGear#Notes.md)).

-    **outer_diameter|Float**: Default is {{value|7.5}}. Diameter of the rolling circle of epicycloid, normalized by the **module** (see [Notes](FCGear_CycloidGear#Notes.md)).


{{Properties_Title|fillets}}

-    **head_fillet|Float**: Default is {{value|0}}.

-    **root_fillet|Float**: Default is {{value|0}}.


{{Properties_Title|helical}}

-    **beta|Angle**: Default is {{value|0 °}}. With the helix angle β a helical gear is created (positive value → rotation direction right, negative value → rotation direction left).

-    **double_helix|Bool**: Default is {{false}}, {{true}} creates a double helix gear (see [Notes](FCGear_CycloidGear#Notes.md)).


{{Properties_Title|involute}}

-    **module|Length**: Default is {{value|1 mm}}. For racks the module equals the pitch and so is the distance between corresponding points on adjacent teeth (see [Notes](FCGear_CycloidGear#Notes.md)).


{{Properties_Title|precision}}

-    **simplified|Bool**: Default is {{false}}. If {{true}} the rack is drawn with a constant number of teeth to avoid topological renaming.


{{Properties_Title|tolerance}}

-    **clearance|Float**: Default is {{value|0.25}} (see [Notes](FCGear_CycloidGear#Notes.md)).

-    **head|Float**: Default is {{value|0}}. Additional length of the tip of the teeth, normalized by the **module**.


{{Properties_Title|version}}

-    **version|String**:

## Notes

See [FCGear CycloidGear](FCGear_CycloidGear#Notes.md).

## Useful formulas 

See [FCGear CycloidGear](FCGear_CycloidGear#Useful_formulas.md).

## Scripting



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External Command Reference.md) > FCGear CycloidRack/pl
